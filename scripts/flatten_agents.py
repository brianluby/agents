#!/usr/bin/env python3
"""flatten_agents.py

Flatten (or index) OpenCode agent markdown files into a single directory.

Modes:
  link  (default) : Create symlinks pointing to originals (non-destructive)
  copy             : Copy files (duplicates content)
  move             : Move files (removes originals)

Features:
  * Collision strategies: skip (default), overwrite, keep-both
  * keep-both appends -<category> (and numeric suffix if still colliding)
  * Relative symlinks by default (portable); --absolute for absolute targets
  * Optional annotation comment (only for move/copy) with --annotate
  * Verification of broken links: --verify-links
  * Rebuild (clean symlink index): --rebuild (link mode only)
  * Dry run support: --dry-run

Typical usage:
  Dry run (see planned actions):    python scripts/flatten_agents.py --dry-run
  Build link index (default):       python scripts/flatten_agents.py
  Keep both on collisions:          python scripts/flatten_agents.py --strategy keep-both
  Overwrite existing links/files:   python scripts/flatten_agents.py --strategy overwrite
  Copy instead of link + annotate:  python scripts/flatten_agents.py --mode copy --annotate
  Rebuild symlink index:            python scripts/flatten_agents.py --rebuild
  Verify only:                      python scripts/flatten_agents.py --verify-links

Guiding principles:
  - Non-destructive by default (link mode)
  - Predictable, explicit operations with clear console output
  - Minimal side effects unless requested
"""
from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path
from typing import Iterator, Optional, Tuple

# ---------------------------
# Discovery & Selection
# ---------------------------

def find_agents(source_root: Path) -> Iterator[Tuple[str, Path]]:
    """Yield (category, file_path) for agent markdown files under opencode/.

    Skips hidden directories and sentinel names (README.md, TODO.md).
    """
    skip_names = {"readme.md", "todo.md"}
    if not source_root.exists():  # Nothing to do if source missing
        return
    # Iterate categories deterministically for reproducibility
    for category_dir in sorted(source_root.iterdir()):
        if not category_dir.is_dir() or category_dir.name.startswith('.'):
            continue
        for md_file in sorted(category_dir.glob('*.md')):
            if md_file.name.lower() in skip_names:
                continue
            yield category_dir.name, md_file


def resolve_target(dest_root: Path, file_name: str, category: str, strategy: str) -> Optional[Path]:
    """Determine destination path honoring collision strategy.

    Returns a Path or None (if skipping due to collision and strategy=skip).
    """
    candidate = dest_root / file_name
    if not candidate.exists():
        return candidate

    if strategy == "skip":
        return None
    if strategy == "overwrite":
        return candidate
    if strategy == "keep-both":
        stem = Path(file_name).stem
        suffix = Path(file_name).suffix
        variant = dest_root / f"{stem}-{category}{suffix}"
        counter = 2
        while variant.exists():  # Ensure uniqueness
            variant = dest_root / f"{stem}-{category}-{counter}{suffix}"
            counter += 1
        return variant

    raise ValueError(f"Unknown collision strategy: {strategy}")

# ---------------------------
# File Operations
# ---------------------------

def annotate_file(path: Path, category: str) -> None:
    """Prepend a category marker comment if not already present.

    Only used for move/copy (not link) to avoid mutating shared originals.
    """
    marker = f"<!-- category: {category} -->"
    try:
        content = path.read_text(encoding='utf-8')
    except Exception as exc:  # Narrow IO failure; print warning
        print(f"Warning: could not read for annotation {path}: {exc}", file=sys.stderr)
        return
    if content.startswith(marker):  # Already annotated
        return
    try:
        path.write_text(f"{marker}\n{content}", encoding='utf-8')
    except Exception as exc:
        print(f"Warning: failed to annotate {path}: {exc}", file=sys.stderr)


def move_or_copy(src: Path, dest: Path, category: str, mode: str, annotate: bool, dry_run: bool) -> bool:
    """Move or copy a file and optionally annotate.

    Returns True if an operation occurred (even in dry-run).
    """
    verb = "MOVE" if mode == "move" else "COPY"
    if dry_run:
        print(f"[DRY] {verb} {src} -> {dest}")
        return True
    dest.parent.mkdir(parents=True, exist_ok=True)
    if mode == "move":
        shutil.move(str(src), str(dest))
    else:
        shutil.copy2(src, dest)
    if annotate:
        annotate_file(dest, category)
    print(f"[{verb}] {dest.name}")
    return True


def create_symlink(src: Path, dest: Path, overwrite: bool, absolute: bool, dry_run: bool) -> bool:
    """Create a symlink at dest pointing to src.

    Uses relative path unless absolute=True. Overwrites existing file/symlink only if overwrite is True.
    """
    if dest.exists() or dest.is_symlink():  # Destination occupied
        if not overwrite:
            print(f"[SKIP] Exists: {dest.name}")
            return False
        if dry_run:
            print(f"[DRY] UNLINK {dest}")
        else:
            if dest.is_dir():  # Safety: avoid clobbering directories
                print(f"[ERR] Destination is directory: {dest}", file=sys.stderr)
                return False
            dest.unlink()
    # Relative target increases portability across machines or path relocations
    target = str(src if absolute else Path(os.path.relpath(src, dest.parent)))
    if dry_run:
        print(f"[DRY] LINK {dest} -> {target}")
        return True
    dest.parent.mkdir(parents=True, exist_ok=True)
    os.symlink(target, dest)
    print(f"[LINK] {dest.name} -> {target}")
    return True

# ---------------------------
# Verification & Maintenance Utilities
# ---------------------------

def verify_links(dest_root: Path) -> int:
    """Report broken symlinks in destination directory; return count broken."""
    broken = 0
    for item in sorted(dest_root.glob('*.md')):
        if not item.is_symlink():  # Only inspect symlinks
            continue
        target_path = item.resolve(strict=False)
        if not target_path.exists():  # Dangling link
            print(f"[BROKEN] {item.name} -> {os.readlink(item)}")
            broken += 1
    if broken == 0:
        print("[OK] No broken symlink(s) detected.")
    return broken


def rebuild_links(dest_root: Path) -> None:
    """Remove only symlinks in destination (preserves real files)."""
    removed = 0
    for item in sorted(dest_root.glob('*')):
        if item.is_symlink():
            item.unlink()
            removed += 1
    print(f"[REBUILD] Removed {removed} existing symlink(s).")

# ---------------------------
# Argument Parsing
# ---------------------------

def parse_args(argv: list[str]) -> argparse.Namespace:
    """Parse CLI arguments and return populated namespace."""
    parser = argparse.ArgumentParser(
        description="Flatten OpenCode agents into a single directory via move/copy/link."  # Short help
    )
    parser.add_argument(
        "--repo-root",
        default=".",
        help="Path to repository root containing 'opencode' directory (default: current dir).",
    )
    parser.add_argument(
        "--dest-root",
        default=str(Path.home() / ".config" / "opencode" / "agent"),
        help="Destination directory for flattened files (default: ~/.config/opencode/agent/).",
    )
    parser.add_argument(
        "--mode",
        choices=["move", "copy", "link"],
        default="link",
        help="Operation mode (default: link).",
    )
    parser.add_argument(
        "--strategy",
        choices=["skip", "overwrite", "keep-both"],
        default="skip",
        help="Filename collision strategy (default: skip).",
    )
    parser.add_argument(
        "--annotate",
        action="store_true",
        help="Prepend category comment (ignored in link mode).",
    )
    parser.add_argument(
        "--absolute",
        action="store_true",
        help="Create absolute symlink targets (link mode only).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print actions without modifying filesystem.",
    )
    parser.add_argument(
        "--verify-links",
        action="store_true",
        help="Verify existing symlinks in destination then exit.",
    )
    parser.add_argument(
        "--rebuild",
        action="store_true",
        help="Remove existing symlinks in destination before processing (link mode only).",
    )
    return parser.parse_args(argv)

# ---------------------------
# Main Orchestration
# ---------------------------

def main(argv: Optional[list[str]] = None) -> None:
    """Entry point: parse args, perform requested operation(s)."""
    args = parse_args(argv or sys.argv[1:])

    source_root = (Path(args.repo_root).resolve() / "opencode")
    if not source_root.exists():  # Hard fail: nothing to process
        print(f"Error: source directory not found: {source_root}", file=sys.stderr)
        sys.exit(1)

    dest_root = Path(args.dest_root).expanduser().resolve()

    # Pure maintenance operations (verify only) short-circuit early
    if args.verify_links:
        verify_links(dest_root)
        return

    # Optional rebuild (only meaningful in link mode)
    if args.rebuild:
        if args.mode != "link":
            print("Warning: --rebuild ignored (only meaningful with --mode link).")
        else:
            if args.dry_run:
                print("[DRY] Would rebuild (remove existing symlinks).")
            else:
                rebuild_links(dest_root)

    total = 0
    acted = 0

    # Iterate all discovered agents
    for category, src_path in find_agents(source_root):
        total += 1
        target_path = resolve_target(dest_root, src_path.name, category, args.strategy)
        if target_path is None:  # Collision & skip strategy
            print(f"[SKIP] Collision (strategy=skip): {src_path.name}")
            continue

        # Execute operation based on mode
        if args.mode == "link":
            success = create_symlink(
                src=src_path,
                dest=target_path,
                overwrite=(args.strategy == "overwrite"),
                absolute=args.absolute,
                dry_run=args.dry_run,
            )
        else:
            success = move_or_copy(
                src=src_path,
                dest=target_path,
                category=category,
                mode=args.mode,
                annotate=args.annotate and args.mode in {"move", "copy"},
                dry_run=args.dry_run,
            )
        if success:
            acted += 1

    print(f"\nSummary: scanned={total}, {args.mode}d={acted}, dest={dest_root}")

    # Post-operation link verification (only when real changes applied in link mode)
    if args.mode == "link" and not args.dry_run:
        verify_links(dest_root)


if __name__ == "__main__":  # Script execution guard
    main()
