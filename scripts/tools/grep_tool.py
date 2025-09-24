#!/usr/bin/env python3
"""grep_tool: Regex search across text files.

Features:
- UTF-8 text scanning with line numbers
- Include glob filtering and simple ignore patterns
- Limits results to avoid overwhelming output

Usage:
    from scripts.tools.grep_tool import run_grep
    out = run_grep(base_dir='.', pattern='TODO', include=['*.py'])

CLI:
    python scripts/tools/grep_tool.py --base . --pattern 'TODO' --include '*.py' --max 200
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import List, Dict, Any, Iterable

DEFAULT_MAX_MATCHES = 500


@dataclass
class Match:
    file: str
    line: int
    text: str


def iter_files(base: Path, includes: List[str] | None) -> Iterable[Path]:
    if not includes:
        yield from base.rglob('*')
    else:
        seen: set[Path] = set()
        for inc in includes:
            for p in base.rglob(inc):
                if p in seen:
                    continue
                seen.add(p)
                yield p


def run_grep(base_dir: str, pattern: str, include: List[str] | None = None, ignore: List[str] | None = None, max_matches: int = DEFAULT_MAX_MATCHES) -> Dict[str, Any]:
    base = Path(base_dir).resolve()
    if not base.exists():
        return {"error": f"Base directory not found: {base}"}

    ignore = ignore or []
    rx: re.Pattern[str]
    try:
        rx = re.compile(pattern)
    except re.error as e:
        return {"error": f"Invalid regex: {e}"}

    matches: List[Match] = []
    for path in iter_files(base, include):
        if not path.is_file():
            continue
        rel = path.relative_to(base)
        skip = False
        for ig in ignore:
            if path.match(ig):
                skip = True
                break
        if skip:
            continue
        try:
            text = path.read_text(encoding='utf-8')
        except Exception:
            continue  # Skip binary or unreadable
        for idx, line in enumerate(text.splitlines(), start=1):
            if rx.search(line):
                matches.append(Match(str(rel), idx, line[:400]))
                if len(matches) >= max_matches:
                    break
        if len(matches) >= max_matches:
            break

    return {
        "base_dir": str(base),
        "pattern": pattern,
        "count": len(matches),
        "truncated": len(matches) >= max_matches,
        "matches": [m.__dict__ for m in matches],
    }


def main(argv: List[str]) -> int:
    parser = argparse.ArgumentParser(description="Regex search across repository text files")
    parser.add_argument('--base', default='.', help='Base directory')
    parser.add_argument('--pattern', required=True, help='Regex pattern')
    parser.add_argument('--include', action='append', help='Glob include (repeatable)')
    parser.add_argument('--ignore', action='append', help='Glob ignore (repeatable)')
    parser.add_argument('--max', type=int, default=DEFAULT_MAX_MATCHES, help='Max matches (default 500)')
    args = parser.parse_args(argv)

    result = run_grep(args.base, args.pattern, args.include, args.ignore, args.max)
    print(json.dumps(result, indent=2))
    return 0 if 'error' not in result else 1


if __name__ == '__main__':  # pragma: no cover
    try:
        sys.exit(main(sys.argv[1:]))
    except KeyboardInterrupt:
        print('Interrupted', file=sys.stderr)
        sys.exit(130)
