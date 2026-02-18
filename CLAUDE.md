# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with this repository.

## Repository Overview

This repo is an agent library for Claude Code and OpenCode:
- Claude agents are flat markdown files in `claude/*.md`
- OpenCode skills are per-directory files in `opencode/<skill>/SKILL.md`
- Tooling lives in `scripts/`

There is no application runtime, server, or test suite in this repo by default.

## Useful Commands

### Environment setup
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

### Agent discovery
```bash
ls claude/*.md
ls opencode/*/SKILL.md
```

### Lint agent metadata
```bash
# OpenCode only
python scripts/lint_agents.py --roots opencode --schema opencode

# Both collections (auto schema detection)
python scripts/lint_agents.py --roots opencode claude

# OpenCode key-order auto-fix
python scripts/lint_agents.py --roots opencode --schema opencode --check-order
```

### Conversion scripts
```bash
# Single file
python scripts/convert-agent.py claude/python-pro.md opencode/python-pro/SKILL.md --to=opencode

# Bulk conversion
python scripts/convert_to_opencode.py --source-dir claude --target-dir opencode --dry-run

# Flatten skill index (symlink mode)
python scripts/flatten_agents.py --repo-root . --dest-root ~/.config/opencode/agent --mode link --strategy skip
```

## Format Expectations

### Claude files
- Path pattern: `claude/<agent>.md`
- Frontmatter typically includes `name`, `description`, and often `model`

### OpenCode skills
- Path pattern: `opencode/<skill>/SKILL.md`
- Canonical frontmatter keys:
  - `name`
  - `description`
  - `license`
  - `compatibility`
  - `metadata`

## Editing Guidance

- Keep edits small and targeted.
- Preserve semantic meaning of agent prompts.
- Do not mass rewrite agent content unless requested.
- Maintain frontmatter key order for OpenCode skills.
- Avoid introducing new tooling/config unless explicitly requested.

## Notes

- Pre-commit helper lives at `.githooks/agent-lint`.
- See `AGENTS.md` for repository-specific authoritative conventions.
