#!/usr/bin/env python3
"""Agent linter for OpenCode and Claude agent markdown files.

Validates:
- Presence & order of frontmatter keys (description, mode, model, temperature, tools)
- Tools mapping shape (must be mapping, boolean values)
- Allowed tools set enforcement
- No deprecated keys (name, tags)
- Temperature value range 0.0-1.0
- Mode in allowed set {primary, subagent, all}
- Optional: ensures model present when requested via flag / insertion
- Optional: auto-fixes canonical ordering with --check-order
- Reports summary + non-zero exit on violations (unless --warn-only)

Usage:
  python scripts/lint_agents.py --roots opencode claude
  python scripts/lint_agents.py --fix-missing-model anthropic/claude-sonnet-4-20250514
  python scripts/lint_agents.py --check-order --roots opencode

Exit codes:
  0 = clean
  1 = violations
  2 = internal error
"""
from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple

import yaml

ALLOWED_MODES = {"primary", "subagent", "all"}
CANONICAL_ORDER = ["description", "mode", "model", "temperature", "tools"]
DEPRECATED_KEYS = {"name", "tags"}
ALLOWED_TOOLS = {"read", "write", "edit", "bash", "search", "glob", "grep", "diff", "format", "webfetch"}


@dataclass
class Violation:
    path: Path
    message: str
    fixable: bool = False

    def format(self) -> str:
        return f"{self.path}: {self.message}{' (fixable)' if self.fixable else ''}" 


def parse_frontmatter(text: str) -> Tuple[Optional[Dict[str, Any]], str]:
    if not text.startswith('---'):
        return None, text
    parts = text.split('---', 2)
    if len(parts) < 3:
        return None, text
    raw = parts[1]
    body = parts[2]
    try:
        data = yaml.safe_load(raw) or {}
        if not isinstance(data, dict):
            return None, text
        return data, body
    except Exception:
        return None, text


def check_order(data: Dict[str, Any]) -> bool:
    filtered = [k for k in CANONICAL_ORDER if k in data]
    current = [k for k in data.keys() if k in CANONICAL_ORDER]
    return current == filtered


def rebuild_order(fm: Dict[str, Any]) -> Dict[str, Any]:
    new_dict: Dict[str, Any] = {}
    for key in CANONICAL_ORDER:
        if key in fm:
            new_dict[key] = fm[key]
    for k in fm:
        if k not in new_dict:
            new_dict[k] = fm[k]
    return new_dict


def lint_file(path: Path, require_model: bool, fix_model: Optional[str], fix_order: bool) -> Tuple[List[Violation], bool]:
    text = path.read_text(encoding='utf-8')
    fm, body = parse_frontmatter(text)
    violations: List[Violation] = []
    changed = False

    if fm is None:
        violations.append(Violation(path, 'Missing or invalid YAML frontmatter'))
        return violations, changed

    # Deprecated keys
    for k in fm.keys():
        if k in DEPRECATED_KEYS:
            violations.append(Violation(path, f'Deprecated key present: {k}'))

    # Required keys
    for key in ("description", "mode"):
        if key not in fm:
            violations.append(Violation(path, f'Missing required key: {key}'))

    # Mode validity
    if 'mode' in fm and fm['mode'] not in ALLOWED_MODES:
        violations.append(Violation(path, f"Invalid mode: {fm['mode']!r}"))

    # Model handling
    if require_model and 'model' not in fm:
        if fix_model:
            fm['model'] = fix_model
            changed = True
        else:
            violations.append(Violation(path, 'Missing model'))

    # Temperature
    if 'temperature' in fm:
        try:
            t = float(fm['temperature'])
            if not 0.0 <= t <= 1.0:
                violations.append(Violation(path, f'Out-of-range temperature: {t}'))
        except Exception:
            violations.append(Violation(path, f'Non-numeric temperature: {fm['temperature']!r}'))
    else:
        violations.append(Violation(path, 'Missing temperature'))

    # Tools mapping & validation
    if 'tools' in fm:
        tools = fm['tools']
        if not isinstance(tools, dict):
            violations.append(Violation(path, 'tools must be a mapping'))
        else:
            bad_values = {k: v for k, v in tools.items() if not isinstance(v, bool)}
            if bad_values:
                violations.append(Violation(path, f'Non-boolean tool values: {bad_values}'))
            unknown = [k for k in tools.keys() if k not in ALLOWED_TOOLS]
            if unknown:
                violations.append(Violation(path, f'Unknown tools: {unknown}'))
    else:
        violations.append(Violation(path, 'Missing tools mapping'))

    # Order check
    is_canonical = check_order(fm)
    if not is_canonical:
        if fix_order:
            fm = rebuild_order(fm)
            changed = True
        else:
            violations.append(Violation(path, 'Non-canonical key order (informational)'))

    # Rewrite if changed
    if changed:
        out_dict = rebuild_order(fm) if (fix_order and not is_canonical) else rebuild_order(fm)
        dumped = yaml.safe_dump(out_dict, sort_keys=False).strip() + '\n'
        path.write_text(f"---\n{dumped}---{body}", encoding='utf-8')
    return violations, changed


def scan(root: Path) -> List[Path]:
    return [p for p in root.rglob('*.md') if p.is_file()]


def main(argv: List[str]) -> int:
    parser = argparse.ArgumentParser(description='Lint agent markdown files.')
    parser.add_argument('--roots', nargs='+', default=['opencode'], help='Root directories to scan')
    parser.add_argument('--require-model', action='store_true', help='Flag missing model as violation')
    parser.add_argument('--fix-missing-model', metavar='MODEL', help='Insert model into agents missing it')
    parser.add_argument('--check-order', action='store_true', help='Auto-fix non-canonical key order')
    parser.add_argument('--warn-only', action='store_true', help='Exit 0 even if violations found')
    parser.add_argument('--list-tools', action='store_true', help='Print allowed tools and exit')
    args = parser.parse_args(argv)

    if args.list_tools:
        print('Allowed tools:')
        for t in sorted(ALLOWED_TOOLS):
            print(' -', t)
        return 0

    violations: List[Violation] = []
    changed_files = 0
    scanned_files = 0

    for root in args.roots:
        root_path = Path(root)
        if not root_path.exists():
            print(f"WARN: Root not found: {root}")
            continue
        for path in scan(root_path):
            scanned_files += 1
            file_violations, changed = lint_file(
                path,
                args.require_model or bool(args.fix_missing_model),
                args.fix_missing_model,
                args.check_order,
            )
            violations.extend(file_violations)
            if changed:
                changed_files += 1

    if violations:
        print('\nViolations:')
        for v in violations:
            print('-', v.format())

    print('\nSummary:')
    print(f"  Files scanned: {scanned_files}")
    print(f"  Violations: {len(violations)}")
    print(f"  Files modified (auto-fix): {changed_files}")

    if violations and not args.warn_only:
        return 1
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main(sys.argv[1:]))
    except KeyboardInterrupt:
        print('Interrupted', file=sys.stderr)
        sys.exit(130)
    except Exception as e:
        print('Internal error:', e, file=sys.stderr)
        sys.exit(2)
