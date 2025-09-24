#!/usr/bin/env python3
"""
Convert Claude Code agents to OpenCode format.

This script converts agents from Claude Code format to OpenCode format by:
1. Adjusting YAML frontmatter
2. Mapping model names
3. Preserving system prompts
4. Organizing into appropriate OpenCode directories
"""

import os
import re
import shutil
from pathlib import Path
import yaml
import click
from rich.console import Console
from rich.table import Table
from rich.progress import track

console = Console()

# Model mapping from Claude Code to OpenCode format
MODEL_MAPPING = {
    'haiku': 'claude-3-haiku-20240307',
    'sonnet': 'claude-3-5-sonnet-20241022',
    'opus': 'claude-3-opus-20240229',
    None: 'claude-3-5-sonnet-20241022'  # Default to Sonnet if not specified
}

# Category mapping for OpenCode directory structure
CATEGORY_MAPPING = {
    'languages': 'development',
    'infrastructure': 'infrastructure',
    'quality-security': 'security',
    'specialized-domains': 'specialized',
    'business': 'business',
    'support-documentation': 'documentation',
    'research-analysis': 'analysis',
    'seo': 'marketing',
    'visual-tools': 'tools',
    'game-development': 'gaming'
}


def parse_agent_file(file_path):
    """Parse a Claude Code agent file and extract frontmatter and content."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract YAML frontmatter
    match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
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
    """Convert Claude Code frontmatter to OpenCode format."""
    if not frontmatter:
        return {}

    opencode_frontmatter = {
        'name': frontmatter.get('name', 'unnamed-agent'),
        'description': frontmatter.get('description', ''),
    }

    # Map model names
    claude_model = frontmatter.get('model')
    opencode_frontmatter['model'] = MODEL_MAPPING.get(claude_model, MODEL_MAPPING[None])

    # Handle tools
    tools = frontmatter.get('tools', 'all')
    if tools == 'all' or tools == '*':
        # OpenCode might require explicit tool listing
        opencode_frontmatter['tools'] = ['read', 'write', 'edit', 'bash', 'search']
    elif isinstance(tools, str):
        opencode_frontmatter['tools'] = [t.strip() for t in tools.split(',')]
    elif isinstance(tools, list):
        opencode_frontmatter['tools'] = tools

    return opencode_frontmatter


def determine_opencode_category(claude_category):
    """Map Claude Code category to OpenCode category."""
    return CATEGORY_MAPPING.get(claude_category, 'general')


def convert_agent(source_file, target_dir):
    """Convert a single agent file from Claude Code to OpenCode format."""
    frontmatter, body = parse_agent_file(source_file)

    if frontmatter is None:
        return False

    # Convert frontmatter
    opencode_frontmatter = convert_frontmatter(frontmatter)

    # Create new content
    new_content = f"""---
name: {opencode_frontmatter['name']}
description: {opencode_frontmatter['description']}
model: {opencode_frontmatter['model']}
tools: {', '.join(opencode_frontmatter.get('tools', ['all']))}
---

{body}"""

    # Ensure target directory exists
    target_dir.mkdir(parents=True, exist_ok=True)

    # Write converted file
    target_file = target_dir / source_file.name
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True


@click.command()
@click.option('--source-dir', default='claude', help='Source directory containing Claude Code agents')
@click.option('--target-dir', default='opencode', help='Target directory for OpenCode agents')
@click.option('--dry-run', is_flag=True, help='Show what would be done without actually converting')
def main(source_dir, target_dir, dry_run):
    """Convert Claude Code agents to OpenCode format."""
    source_path = Path(source_dir)
    target_path = Path(target_dir)

    if not source_path.exists():
        console.print(f"[red]Error: Source directory '{source_dir}' does not exist[/red]")
        return

    # Find all agent files
    agent_files = []
    for category_dir in source_path.iterdir():
        if category_dir.is_dir() and not category_dir.name.startswith('.'):
            for agent_file in category_dir.glob('*.md'):
                if agent_file.name not in ['README.md', 'TODO.md']:
                    agent_files.append((category_dir.name, agent_file))

    console.print(f"\n[bold]Found {len(agent_files)} agents to convert[/bold]\n")

    # Create conversion summary table
    table = Table(title="Conversion Plan")
    table.add_column("Claude Category", style="cyan")
    table.add_column("OpenCode Category", style="green")
    table.add_column("Agent Count", style="yellow")

    category_counts = {}
    for category, _ in agent_files:
        opencode_cat = determine_opencode_category(category)
        key = (category, opencode_cat)
        category_counts[key] = category_counts.get(key, 0) + 1

    for (claude_cat, opencode_cat), count in sorted(category_counts.items()):
        table.add_row(claude_cat, opencode_cat, str(count))

    console.print(table)
    console.print()

    if dry_run:
        console.print("[yellow]Dry run mode - no files will be converted[/yellow]")
        return

    # Convert agents
    success_count = 0
    error_count = 0

    for category, agent_file in track(agent_files, description="Converting agents..."):
        opencode_category = determine_opencode_category(category)
        target_category_dir = target_path / opencode_category

        try:
            if convert_agent(agent_file, target_category_dir):
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

    # Show created directories
    console.print(f"\n[bold]Created OpenCode directories:[/bold]")
    for dir_path in sorted(target_path.glob('*/')):
        if dir_path.is_dir():
            agent_count = len(list(dir_path.glob('*.md')))
            console.print(f"  📁 {dir_path.name}: {agent_count} agents")


if __name__ == '__main__':
    main()