#!/usr/bin/env python3
"""diff_tool: Produce unified diffs between two filesystem paths.

Supports:
- File vs file
- Directory vs directory (recursive, matching relative paths)
- Limiting max diff size

Intended for review agents needing a safe textual diff.
"""
from __future__ import annotations

import argparse
import difflib
import json
import sys
from pathlib import Path
from typing import List, Dict, Any

MAX_DEFAULT_BYTES = 200_000


def read_text(path: Path) -> str:
    return path.read_text(encoding='utf-8', errors='replace')


def collect_files(root: Path) -> List[Path]:
    if root.is_file():
        return [root]
    files: List[Path] = []
    for p in root.rglob('*'):
        if p.is_file():
            files.append(p)
    return files


def dir_relative_map(root: Path) -> Dict[str, Path]:
    return {str(p.relative_to(root)): p for p in collect_files(root)}


def make_diff(a_path: Path, b_path: Path) -> List[str]:
    a_lines = read_text(a_path).splitlines(keepends=True)
    b_lines = read_text(b_path).splitlines(keepends=True)
    return list(difflib.unified_diff(a_lines, b_lines, fromfile=str(a_path), tofile=str(b_path)))


def diff(a: str, b: str, limit: int = MAX_DEFAULT_BYTES) -> Dict[str, Any]:
    a_path = Path(a).resolve()
    b_path = Path(b).resolve()
    if not a_path.exists():
        return {"error": f"Left path not found: {a_path}"}
    if not b_path.exists():
        return {"error": f"Right path not found: {b_path}"}

    if a_path.is_file() and b_path.is_file():
        diff_lines = make_diff(a_path, b_path)
        text = ''.join(diff_lines)
        truncated = False
        if len(text.encode('utf-8')) > limit:
            truncated = True
            text = text.encode('utf-8')[:limit].decode('utf-8', errors='ignore')
        return {"mode": "file", "bytes": len(text.encode('utf-8')), "truncated": truncated, "diff": text}

    # Directory diff
    left_map = dir_relative_map(a_path)
    right_map = dir_relative_map(b_path)
    all_keys = sorted(set(left_map.keys()) | set(right_map.keys()))
    collected: List[str] = []
    truncated = False
    current_bytes: int = 0
    for key in all_keys:
        if key not in left_map:
            collected.append(f"--- (missing)\n+++ {right_map[key]}\n@@ NEW FILE {key} @@\n")
            continue
        if key not in right_map:
            collected.append(f"--- {left_map[key]}\n+++ (missing)\n@@ DELETED FILE {key} @@\n")
            continue
        diff_lines = make_diff(left_map[key], right_map[key])
        if diff_lines:
            chunk = ''.join(diff_lines)
            b = len(chunk.encode('utf-8'))
            if current_bytes + b > limit:
                truncated = True
                remaining = limit - current_bytes
                if remaining > 0:
                    partial = chunk.encode('utf-8')[:remaining].decode('utf-8', errors='ignore')
                    collected.append(partial)
                break
            collected.append(chunk)
            current_bytes += b

    merged = ''.join(collected)
    return {"mode": "directory", "bytes": len(merged.encode('utf-8')), "truncated": truncated, "diff": merged}


def main(argv: List[str]) -> int:
    parser = argparse.ArgumentParser(description="Unified diff between two paths")
    parser.add_argument('left', help='Left path (file or directory)')
    parser.add_argument('right', help='Right path (file or directory)')
    parser.add_argument('--limit', type=int, default=MAX_DEFAULT_BYTES, help='Max diff bytes (default 200k)')
    args = parser.parse_args(argv)

    result = diff(args.left, args.right, args.limit)
    print(json.dumps(result, indent=2))
    return 0 if 'error' not in result else 1


if __name__ == '__main__':  # pragma: no cover
    try:
        sys.exit(main(sys.argv[1:]))
    except KeyboardInterrupt:
        print('Interrupted', file=sys.stderr)
        sys.exit(130)
