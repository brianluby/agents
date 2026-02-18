#!/usr/bin/env python3
"""Agent/skill linter for OpenCode and Claude agent markdown files.

Multi-schema validation modes:
- OpenCode schema (strict): validates OpenCode "skill" frontmatter and key ordering
- Claude schema (legacy-friendly): validates Claude agent frontmatter (name/description/model/tools)
- Auto detection (default): chooses schema per file path by presence of top-level directory segment
  'opencode' or 'claude'. Unclassified paths are skipped.

OpenCode schema (current):
- Files live under a per-skill directory, e.g. opencode/python-pro/SKILL.md
- Required frontmatter keys: name, description, license, compatibility, metadata
- Model/mode/temperature/tools are not part of the current skill frontmatter.

Exit codes:
  0 = clean
  1 = violations (unless --warn-only)
  2 = internal / usage error (e.g. no files classified under --schema auto)
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple

import yaml

ALLOWED_MODES = {"primary", "subagent", "all"}
OPENCODE_CANONICAL_ORDER = [
    "name",
    "description",
    "license",
    "compatibility",
    "metadata",
]
CLAUDE_CANONICAL_ORDER = ["name", "description", "model", "tools"]
ALLOWED_TOOLS = {
    "read",
    "write",
    "edit",
    "bash",
    "search",
    "glob",
    "grep",
    "diff",
    "format",
    "webfetch",
}
DEPRECATED_KEYS = {"tags"}


@dataclass
class Violation:
    path: Path
    message: str
    fixable: bool = False

    def format(self) -> str:
        return f"{self.path}: {self.message}{' (fixable)' if self.fixable else ''}"  # noqa: E501


@dataclass(frozen=True)
class AgentSchema:
    name: str
    canonical_order: List[str]
    enforce_order: bool
    require_keys: List[str]
    require_tools: bool
    require_temperature: bool
    require_mode: bool


OPENCODE_SCHEMA = AgentSchema(
    name="opencode",
    canonical_order=OPENCODE_CANONICAL_ORDER,
    enforce_order=True,
    require_keys=["name", "description", "license", "compatibility", "metadata"],
    require_tools=False,
    require_temperature=False,
    require_mode=False,
)

CLAUDE_SCHEMA = AgentSchema(
    name="claude",
    canonical_order=CLAUDE_CANONICAL_ORDER,
    enforce_order=False,  # allow original ordering; can still warn if requested in future
    require_keys=[],
    require_tools=False,
    require_temperature=False,
    require_mode=False,
)


def parse_frontmatter(text: str) -> Tuple[Optional[Dict[str, Any]], str]:
    if not text.startswith("---"):
        return None, text
    parts = text.split("---", 2)
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


def check_order(data: Dict[str, Any], canonical_order: List[str]) -> bool:
    filtered = [k for k in canonical_order if k in data]
    current = [k for k in data.keys() if k in canonical_order]
    return current == filtered


def rebuild_order(fm: Dict[str, Any], canonical_order: List[str]) -> Dict[str, Any]:
    new_dict: Dict[str, Any] = {}
    for key in canonical_order:
        if key in fm:
            new_dict[key] = fm[key]
    for k in fm:
        if k not in new_dict:
            new_dict[k] = fm[k]
    return new_dict


def classify_schema(path: Path, forced: str) -> Optional[AgentSchema]:
    if forced == "opencode":
        return OPENCODE_SCHEMA
    if forced == "claude":
        return CLAUDE_SCHEMA
    # auto mode
    parts = set(path.parts)
    if "opencode" in parts:
        return OPENCODE_SCHEMA
    if "claude" in parts:
        return CLAUDE_SCHEMA
    return None


def lint_file(
    path: Path,
    schema: AgentSchema,
    require_model: bool,
    fix_model: Optional[str],
    fix_order: bool,
    allow_deprecated_claude: bool,
) -> Tuple[List[Violation], bool]:
    text = path.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(text)
    violations: List[Violation] = []
    changed = False

    if fm is None:
        violations.append(Violation(path, "Missing or invalid YAML frontmatter"))
        return violations, changed

    # Deprecated keys handling
    if schema.name == "opencode":
        for k in fm.keys():
            if k in DEPRECATED_KEYS:
                violations.append(
                    Violation(path, f"Deprecated key in OpenCode schema: {k}")
                )
    else:  # claude
        if not allow_deprecated_claude:
            for k in fm.keys():
                if k in DEPRECATED_KEYS:
                    violations.append(
                        Violation(
                            path,
                            f"Deprecated key (enable with --allow-deprecated-claude): {k}",
                        )
                    )

    # Required keys (schema-specific)
    for key in schema.require_keys:
        if key not in fm:
            violations.append(Violation(path, f"Missing required key: {key}"))

    # Mode validity (Claude-only legacy support)
    if schema.name == "claude" and "mode" in fm and fm["mode"] not in ALLOWED_MODES:
        violations.append(
            Violation(
                path,
                f"Mode key ignored for Claude schema (invalid value {fm['mode']!r})",
            )
        )

    # Model handling (Claude schema only)
    if schema.name == "claude":
        if require_model and "model" not in fm:
            if fix_model:
                fm["model"] = fix_model
                changed = True
            else:
                violations.append(Violation(path, "Missing model"))

    # Temperature (Claude schema only; ignore for OpenCode skills)
    if schema.name == "claude" and "temperature" in fm:
        try:
            t = float(fm["temperature"])
            if not 0.0 <= t <= 1.0:
                violations.append(
                    Violation(
                        path, f"Out-of-range temperature (Claude non-required): {t}"
                    )
                )
        except Exception:
            violations.append(
                Violation(
                    path,
                    f"Non-numeric temperature (Claude non-required): {fm['temperature']!r}",
                )
            )

    # OpenCode skill-specific validations
    if schema.name == "opencode":
        if "compatibility" in fm and fm["compatibility"] != "opencode":
            violations.append(
                Violation(
                    path,
                    f"Invalid compatibility: {fm['compatibility']!r} (expected 'opencode')",
                )
            )
        if "metadata" in fm and not isinstance(fm["metadata"], dict):
            violations.append(Violation(path, "metadata must be a mapping"))

    # Tools
    if schema.require_tools:
        if "tools" not in fm:
            violations.append(Violation(path, "Missing tools mapping"))
        else:
            tools = fm["tools"]
            if not isinstance(tools, dict):
                violations.append(Violation(path, "tools must be a mapping"))
            else:
                bad_values = {k: v for k, v in tools.items() if not isinstance(v, bool)}
                if bad_values:
                    violations.append(
                        Violation(path, f"Non-boolean tool values: {bad_values}")
                    )
                unknown = [k for k in tools.keys() if k not in ALLOWED_TOOLS]
                if unknown:
                    violations.append(Violation(path, f"Unknown tools: {unknown}"))
    else:
        if "tools" in fm:
            tools = fm["tools"]
            if not isinstance(tools, dict):
                violations.append(
                    Violation(path, "tools must be a mapping (if present)")
                )
            else:
                bad_values = {k: v for k, v in tools.items() if not isinstance(v, bool)}
                if bad_values:
                    violations.append(
                        Violation(path, f"Non-boolean tool values: {bad_values}")
                    )
                unknown = [k for k in tools.keys() if k not in ALLOWED_TOOLS]
                if unknown:
                    violations.append(Violation(path, f"Unknown tools: {unknown}"))

    # Order check (OpenCode only)
    if schema.enforce_order:
        is_canonical = check_order(fm, schema.canonical_order)
        if not is_canonical:
            if fix_order:
                fm = rebuild_order(fm, schema.canonical_order)
                changed = True
            else:
                violations.append(
                    Violation(
                        path, "Non-canonical key order (informational)", fixable=True
                    )
                )
    else:
        is_canonical = True  # not enforced

    # Rewrite if changed
    if changed:
        # Ensure order applied if enforce_order or fix_order requested
        if schema.enforce_order:
            out_dict = rebuild_order(fm, schema.canonical_order)
        else:
            out_dict = fm
        dumped = yaml.safe_dump(out_dict, sort_keys=False).strip() + "\n"
        # Preserve body after frontmatter delimiter
        body_str = (
            body if body.startswith("\n") else body
        )  # body already includes leading newline from split
        path.write_text(f"---\n{dumped}---{body_str}", encoding="utf-8")

    return violations, changed


def scan(root: Path) -> List[Path]:
    return [p for p in root.rglob("*.md") if p.is_file()]


def main(argv: List[str]) -> int:
    parser = argparse.ArgumentParser(description="Lint agent markdown files.")
    parser.add_argument(
        "--roots", nargs="+", default=["opencode"], help="Root directories to scan"
    )
    parser.add_argument(
        "--require-model", action="store_true", help="Flag missing model as violation"
    )
    parser.add_argument(
        "--fix-missing-model",
        metavar="MODEL",
        help="Insert model into agents missing it",
    )
    parser.add_argument(
        "--check-order",
        action="store_true",
        help="Auto-fix non-canonical key order (OpenCode)",
    )
    parser.add_argument(
        "--warn-only", action="store_true", help="Exit 0 even if violations found"
    )
    parser.add_argument(
        "--list-tools", action="store_true", help="Print allowed tools and exit"
    )
    parser.add_argument(
        "--schema",
        choices=["auto", "opencode", "claude"],
        default="auto",
        help="Schema selection strategy",
    )
    parser.add_argument(
        "--allow-deprecated-claude",
        action="store_true",
        help="Allow name/tags in Claude schema without warning",
    )
    args = parser.parse_args(argv)

    if args.list_tools:
        print("Allowed tools:")
        for t in sorted(ALLOWED_TOOLS):
            print(" -", t)
        return 0

    violations: List[Violation] = []
    changed_files = 0
    scanned_files = 0
    schema_counts = {"opencode": 0, "claude": 0}

    classified_any = False

    for root in args.roots:
        root_path = Path(root)
        if not root_path.exists():
            print(f"WARN: Root not found: {root}")
            continue
        for path in scan(root_path):
            schema = classify_schema(path, args.schema)
            if schema is None:
                # Skip unclassified in auto; if explicit schema set we still skip because unmatched
                continue
            classified_any = True
            scanned_files += 1
            schema_counts[schema.name] += 1
            file_violations, changed = lint_file(
                path,
                schema,
                args.require_model or bool(args.fix_missing_model),
                args.fix_missing_model,
                args.check_order,
                args.allow_deprecated_claude,
            )
            violations.extend(file_violations)
            if changed:
                changed_files += 1

    if not classified_any:
        if args.schema == "auto":
            print(
                "No agent files classified under auto schema detection. Provide --schema opencode or --schema claude explicitly.",
                file=sys.stderr,
            )
            return 2
        else:
            print("No files matched provided roots/schema.", file=sys.stderr)
            return 2

    if violations:
        print("\nViolations:")
        for v in violations:
            print("-", v.format())

    print("\nSummary:")
    print(f"  Files scanned: {scanned_files}")
    print(f"  Violations: {len(violations)}")
    print(f"  Files modified (auto-fix): {changed_files}")
    print(
        f"  Schema counts: opencode={schema_counts['opencode']} claude={schema_counts['claude']}"
    )

    if violations and not args.warn_only:
        return 1
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except KeyboardInterrupt:
        print("Interrupted", file=sys.stderr)
        sys.exit(130)
    except Exception as e:
        print("Internal error:", e, file=sys.stderr)
        sys.exit(2)
