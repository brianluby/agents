#!/usr/bin/env python3
"""
Convert Claude Code agents to OpenCode SKILL format.

This script converts agents from Claude Code markdown files into
OpenCode skill directories by:
1. Converting frontmatter to OpenCode schema
2. Preserving system prompt bodies
3. Writing to opencode/<agent-name>/SKILL.md
4. Supporting both flat and category-based Claude layouts
"""

import re
from pathlib import Path
import yaml
import click
from rich.console import Console
from rich.table import Table
from rich.progress import track

console = Console()

DEFAULT_METADATA = {
    "audience": "developers",
    "workflow": "general",
}


def parse_agent_file(file_path):
    """Parse a Claude Code agent file and extract frontmatter and content."""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract YAML frontmatter
    match = re.match(r"^---\n(.*?)\n---\n(.*)$", content, re.DOTALL)
    if not match:
        console.print(f"[yellow]Warning: No frontmatter found in {file_path}[/yellow]")
        return None, content

    frontmatter_str, body = match.groups()
    try:
        frontmatter = yaml.safe_load(frontmatter_str)
    except yaml.YAMLError as e:
        console.print(f"[red]Error parsing YAML in {file_path}: {e}[/red]")
        return None, content

    return frontmatter, body


def convert_frontmatter(frontmatter):
    """Convert Claude Code frontmatter to OpenCode SKILL frontmatter."""
    if not frontmatter:
        return {}

    opencode_frontmatter = {
        "name": frontmatter.get("name", "unnamed-agent"),
        "description": frontmatter.get("description", ""),
        "license": "MIT",
        "compatibility": "opencode",
        "metadata": DEFAULT_METADATA.copy(),
    }

    return opencode_frontmatter


def normalize_body(body):
    """Normalize body spacing for output consistency."""
    return body.lstrip("\n")


def discover_agent_files(source_path):
    """Discover Claude agent markdown files in flat or category-based layouts."""
    agent_files = []
    for agent_file in sorted(source_path.glob("*.md")):
        if agent_file.name not in [
            "README.md",
            "TODO.md",
        ] and not agent_file.name.startswith("."):
            agent_files.append(agent_file)

    for category_dir in sorted(source_path.iterdir()):
        if category_dir.is_dir() and not category_dir.name.startswith("."):
            for agent_file in sorted(category_dir.glob("*.md")):
                if agent_file.name not in ["README.md", "TODO.md"]:
                    agent_files.append(agent_file)

    # Dedupe in case nested patterns overlap
    return list(dict.fromkeys(agent_files))


def convert_agent(source_file, target_root):
    """Convert a single agent file from Claude Code to OpenCode SKILL format."""
    frontmatter, body = parse_agent_file(source_file)

    if frontmatter is None:
        return False

    # Convert frontmatter
    opencode_frontmatter = convert_frontmatter(frontmatter)
    output_dir = target_root / opencode_frontmatter["name"]
    output_file = output_dir / "SKILL.md"

    # Create new content
    frontmatter_yaml = yaml.safe_dump(opencode_frontmatter, sort_keys=False).strip()
    normalized_body = normalize_body(body)
    new_content = f"---\n{frontmatter_yaml}\n---\n{normalized_body}"

    # Ensure target directory exists
    output_dir.mkdir(parents=True, exist_ok=True)

    # Write converted file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(new_content)

    return True


@click.command()
@click.option(
    "--source-dir",
    default="claude",
    help="Source directory containing Claude Code agents",
)
@click.option(
    "--target-dir", default="opencode", help="Target directory for OpenCode agents"
)
@click.option(
    "--dry-run",
    is_flag=True,
    help="Show what would be done without actually converting",
)
def main(source_dir, target_dir, dry_run):
    """Convert Claude Code agents to OpenCode format."""
    source_path = Path(source_dir)
    target_path = Path(target_dir)

    if not source_path.exists():
        console.print(
            f"[red]Error: Source directory '{source_dir}' does not exist[/red]"
        )
        return

    # Find all agent files
    agent_files = discover_agent_files(source_path)

    console.print(f"\n[bold]Found {len(agent_files)} agents to convert[/bold]\n")

    table = Table(title="Conversion Plan")
    table.add_column("Source", style="cyan")
    table.add_column("Target", style="green")

    preview = agent_files[:10]
    for agent_file in preview:
        target = f"{agent_file.stem}/SKILL.md"
        table.add_row(str(agent_file.relative_to(source_path)), target)
    if len(agent_files) > len(preview):
        table.add_row("...", f"... ({len(agent_files) - len(preview)} more)")

    console.print(table)
    console.print()

    if dry_run:
        console.print("[yellow]Dry run mode - no files will be converted[/yellow]")
        return

    # Convert agents
    success_count = 0
    error_count = 0

    for agent_file in track(agent_files, description="Converting agents..."):
        try:
            if convert_agent(agent_file, target_path):
                success_count += 1
            else:
                error_count += 1
                console.print(f"[yellow]Failed to convert {agent_file}[/yellow]")
        except Exception as e:
            error_count += 1
            console.print(f"[red]Error converting {agent_file}: {e}[/red]")

    # Print summary
    console.print(f"\n[bold green]Conversion complete![/bold green]")
    console.print(f"✅ Successfully converted: {success_count} agents")
    if error_count > 0:
        console.print(f"❌ Failed conversions: {error_count} agents")

    # Show created skill directories
    console.print(f"\n[bold]Created OpenCode skill directories:[/bold]")
    for dir_path in sorted(target_path.glob("*/")):
        if dir_path.is_dir():
            has_skill = (dir_path / "SKILL.md").exists()
            if has_skill:
                console.print(f"  📁 {dir_path.name}/SKILL.md")


if __name__ == "__main__":
    main()
