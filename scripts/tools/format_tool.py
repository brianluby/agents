#!/usr/bin/env python3
"""format_tool: Minimal whitespace normalizer.

Operations (idempotent):
- Strip trailing spaces on each line
- Ensure file ends with a single trailing newline
- Optionally dry-run to show which files would change

Intended as a safe placeholder until richer language-aware formatters are integrated.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import List, Dict, Any


def normalize_text(text: str) -> str:
    lines = text.splitlines()
    stripped = [ln.rstrip() for ln in lines]
    return '\n'.join(stripped) + '\n'


def process_file(path: Path) -> Dict[str, Any]:
    original = path.read_text(encoding='utf-8', errors='replace')
    normalized = normalize_text(original)
    changed = normalized != original
    return {
        'file': str(path),
        'changed': changed,
        'original_sha256': hashlib.sha256(original.encode('utf-8')).hexdigest(),
        'new_sha256': hashlib.sha256(normalized.encode('utf-8')).hexdigest(),
        'new_content': normalized if changed else None,
    }


def run_format(base: str, include: List[str], dry_run: bool) -> Dict[str, Any]:
    base_path = Path(base).resolve()
    if not base_path.exists():
        return {'error': f'Base directory not found: {base_path}'}

    # Collect candidate files
    files: List[Path] = []
    patterns = include or ['**/*.md', '**/*.py']
    seen: set[Path] = set()
    for pat in patterns:
        for p in base_path.glob(pat):
            if p.is_file() and p not in seen:
                seen.add(p)
                files.append(p)

    results = []
    changed_files = 0
    for f in files:
        info = process_file(f)
        if info['changed'] and not dry_run:
            Path(info['file']).write_text(info['new_content'], encoding='utf-8')  # type: ignore[arg-type]
        if info['changed']:
            changed_files += 1
        # Drop new_content in dry-run output for brevity
        if dry_run:
            info.pop('new_content')
        results.append(info)

    return {
        'base_dir': str(base_path),
        'files_examined': len(files),
        'files_changed': changed_files,
        'dry_run': dry_run,
        'results': results,
    }


def main(argv: List[str]) -> int:
    parser = argparse.ArgumentParser(description='Normalize trailing whitespace & final newline')
    parser.add_argument('--base', default='.', help='Base directory')
    parser.add_argument('--include', action='append', help='Glob include patterns (repeatable)')
    parser.add_argument('--apply', action='store_true', help='Apply changes (otherwise dry-run)')
    args = parser.parse_args(argv)

    result = run_format(args.base, args.include or [], not args.apply)
    print(json.dumps(result, indent=2))
    return 0 if 'error' not in result else 1


if __name__ == '__main__':  # pragma: no cover
    try:
        sys.exit(main(sys.argv[1:]))
    except KeyboardInterrupt:
        print('Interrupted', file=sys.stderr)
        sys.exit(130)
