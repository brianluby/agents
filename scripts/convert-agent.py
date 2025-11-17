#!/usr/bin/env python3
"""
Convert agents between Claude Code and OpenCode formats.

Usage:
    python convert-agent.py <input_file> <output_file> --to=[claude|opencode]
"""

import argparse
import re
import sys
from pathlib import Path
import yaml


def parse_frontmatter(content):
    """Extract YAML frontmatter from markdown content."""
    if content.startswith("---\n"):
        parts = content.split("---\n", 2)
        if len(parts) >= 3:
            return yaml.safe_load(parts[1]), parts[2]
    return {}, content


def claude_to_opencode(frontmatter, content):
    """Convert Claude Code agent to OpenCode format."""
    opencode_fm = {
        "description": frontmatter.get("description", ""),
        "mode": "subagent",
    }

    # Map model names
    model_map = {
        "openai/gpt-4.1-mini": "haiku",
        "openai/gpt-5.1": "sonnet",
        "anthropic/claude-haiku-4-20250514": "haiku",
        "anthropic/claude-sonnet-4-20250514": "sonnet",
        "anthropic/claude-opus-4-20250514": "opus",
    }

    if "model" in frontmatter:
        opencode_fm["model"] = model_map.get(frontmatter["model"], frontmatter["model"])

    # Set temperature based on agent type
    if (
        "review" in frontmatter.get("name", "").lower()
        or "audit" in frontmatter.get("name", "").lower()
    ):
        opencode_fm["temperature"] = 0.2
    elif (
        "architect" in frontmatter.get("name", "").lower()
        or "design" in frontmatter.get("name", "").lower()
    ):
        opencode_fm["temperature"] = 0.5
    else:
        opencode_fm["temperature"] = 0.7

    # Add default tools
    opencode_fm["tools"] = {"write": True, "edit": True, "bash": True, "read": True}

    return opencode_fm, content


def opencode_to_claude(frontmatter, content, filename):
    """Convert OpenCode agent to Claude Code format."""
    claude_fm = {
        "name": Path(filename).stem,
        "description": frontmatter.get("description", ""),
    }

    # Map model names
    model_map = {"openai/gpt-4.1-mini": "haiku", "openai/gpt-5.1": "sonnet"}

    if "model" in frontmatter:
        for long_name, short_name in model_map.items():
            if long_name in frontmatter["model"]:
                claude_fm["model"] = short_name
                break

    # Extract tags from description
    tags = []
    description_lower = frontmatter.get("description", "").lower()
    tag_keywords = {
        "devops": ["devops", "deployment", "ci/cd"],
        "security": ["security", "audit", "compliance"],
        "testing": ["test", "qa", "quality"],
        "architecture": ["architect", "design", "system"],
        "database": ["database", "sql", "query"],
        "frontend": ["frontend", "ui", "react"],
        "backend": ["backend", "api", "server"],
        "ml": ["ml", "machine learning", "ai"],
    }

    for tag, keywords in tag_keywords.items():
        if any(kw in description_lower for kw in keywords):
            tags.append(tag)

    if tags:
        claude_fm["tags"] = tags

    return claude_fm, content


def format_frontmatter(data):
    """Format frontmatter as YAML."""
    return yaml.dump(data, default_flow_style=False, sort_keys=False)


def main():
    parser = argparse.ArgumentParser(description="Convert agents between formats")
    parser.add_argument("input_file", help="Input agent file")
    parser.add_argument("output_file", help="Output agent file")
    parser.add_argument(
        "--to", required=True, choices=["claude", "opencode"], help="Target format"
    )

    args = parser.parse_args()

    # Read input file
    input_path = Path(args.input_file)
    if not input_path.exists():
        print(f"Error: {args.input_file} not found")
        sys.exit(1)

    content = input_path.read_text()
    frontmatter, body = parse_frontmatter(content)

    # Convert based on target format
    if args.to == "opencode":
        new_frontmatter, new_body = claude_to_opencode(frontmatter, body)
    else:
        new_frontmatter, new_body = opencode_to_claude(
            frontmatter, body, args.output_file
        )

    # Write output file
    output_path = Path(args.output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    output_content = f"---\n{format_frontmatter(new_frontmatter)}---\n{new_body}"
    output_path.write_text(output_content)

    print(f"Converted {args.input_file} to {args.output_file}")


if __name__ == "__main__":
    main()
