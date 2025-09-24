#!/usr/bin/env python3
"""glob_tool: List files matching patterns relative to a root.

Design goals:
- Pure function style returning deterministic JSON-friendly data
- No network, no modification side effects
- Graceful handling of invalid patterns / empty results

Usage (library style):
    from scripts.tools.glob_tool import run_glob
    results = run_glob(base_dir=".", patterns=["**/*.md"], exclude=["build/*"]) 

CLI:
    python scripts/tools/glob_tool.py --base . --pattern '**/*.md' --exclude 'build/*'
"""
from __future__ import annotations

import argparse
import json
import sys
import re
from pathlib import Path
from typing import List, Dict, Any


def run_glob(base_dir: str, patterns: List[str], exclude: List[str] | None = None) -> Dict[str, Any]:
    base = Path(base_dir).resolve()
    if not base.exists():
        return {"base_dir": str(base), "files": [], "error": f"Base directory not found: {base}"}
    exclude = exclude or []
    matched: set[Path] = set()
    for pat in patterns:
        # (Python's glob doesn't raise re.error; pattern errors are rare but we guard anyway.)
        for p in base.glob(pat):
            if not p.is_file():
                continue
            skipped = False
            for ex in exclude:
                if p.match(ex):
                    skipped = True
                    break
            if not skipped:
                matched.add(p)
    # Sort by relative path for stability
    rels = sorted(str(p.relative_to(base)) for p in matched)
    return {"base_dir": str(base), "count": len(rels), "files": rels}


def main(argv: List[str]) -> int:
    parser = argparse.ArgumentParser(description="List files matching glob patterns.")
    parser.add_argument("--base", default=".", help="Base directory")
    parser.add_argument("--pattern", action="append", required=True, help="Glob pattern (can repeat)")
    parser.add_argument("--exclude", action="append", help="Exclude pattern (can repeat)")
    args = parser.parse_args(argv)

    result = run_glob(args.base, args.pattern, args.exclude)
    print(json.dumps(result, indent=2))
    return 0 if 'error' not in result else 1


if __name__ == "__main__":  # pragma: no cover
    try:
        sys.exit(main(sys.argv[1:]))
    except KeyboardInterrupt:
        print("Interrupted", file=sys.stderr)
        sys.exit(130)
