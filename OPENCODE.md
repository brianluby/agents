# OPENCODE.md

This file provides guidance for using and creating OpenCode agents in this repository.

## Repository Overview

This repository contains AI agents for both Claude Code and OpenCode platforms. OpenCode agents are located in the `opencode/` directory and follow OpenCode's specific format and requirements.

## OpenCode Skill Structure

OpenCode skills are stored as directories under `opencode/`, each containing a `SKILL.md` file:

- Example: `opencode/sre-engineer/SKILL.md`

Skills use Markdown with YAML frontmatter.

### Frontmatter Specification (Canonical Order)

```yaml
---
name: sre-engineer
description: Define SLIs/SLOs, implement reliability practices, manage error budgets, and balance feature velocity with stability.
license: MIT
compatibility: opencode
metadata:
  audience: developers
  workflow: general
---
```

### Legacy Normalization (Migration Performed)

A repository-wide normalization pass was executed (September 2025) to:
- Migrate skills to canonical frontmatter: `name`, `description`, `license`, `compatibility`, `metadata`
- Remove legacy Claude-style keys from OpenCode skills (`model`, `mode`, `temperature`, `tools`)
- Normalize key ordering to the canonical order expected by `scripts/lint_agents.py`

If adding older agents, re-run the migration logic manually or follow the checklist above.

### Migration: Converting Single-Line Tools

Before:
```yaml
tools: read, write, edit, bash, search
```
Convert to:
```yaml
tools:
  read: true
  write: true
  edit: true
  bash: true
  search: true
```
Drop any tools not required by the role.

### Referencing a Template

There is no single canonical template file in this repo; copy an existing `opencode/<skill>/SKILL.md` and adjust.

## Agent Categories

### OpenCode Directory Structure

The `opencode/` directory contains agents organized into functional categories:

- **analysis/**: Data scientists, SQL experts, search specialists
- **business/**: Product managers, HR, business analysts
- **development/**: Programming language and framework specialists
- **documentation/**: Technical writers, API documenters
- **gaming/**: Unity developer, Minecraft plugin expert
- **infrastructure/**: Cloud architects, DevOps, self-hosting
- **marketing/**: SEO specialists, content strategists
- **open-source/**: License compliance guardian
- **privacy-security/**: Privacy-first architect
- **security/**: Security auditors, code reviewers
- **specialized/**: AI/ML, blockchain, finance, niche domains
- **tools/**: Diagramming, UI validation utilities

### Shared Agents

The `shared/` directory (if present) can contain cross-platform agents; otherwise conversion scripts handle translations.

## Creating OpenCode Skills

Use an existing `opencode/<skill>/SKILL.md` file as the starting point.

Key authoring steps:
1. Create a directory under `opencode/` using a lowercase hyphenated name (e.g. `cloud-architect`).
2. Add `SKILL.md` in that directory.
3. Set `name` and `description`.
4. Set `license`, `compatibility`, and `metadata`.
5. Tailor prompt sections (Purpose, Capabilities, Workflow, Quality Bar, Anti-Goals, Examples).

### Model / Tooling

Model selection and tool permissions are not stored in the OpenCode skill frontmatter in this repository.

## Converting Claude Code Agents

1. Create `opencode/<skill-name>/SKILL.md`.
2. Add OpenCode skill frontmatter (name/description/license/compatibility/metadata).
3. Copy the body prompt sections.

## Best Practices

### Open-Source Focus
- Prefer open-source tooling & highlight licensing considerations
- Offer self-hosted alternatives & local-first workflows

### Privacy & Security
- Minimize data exposure & avoid telemetry unless explicitly justified
- Leverage encryption and secure defaults (principle of least privilege)

### Transparency
- State assumptions explicitly
- Provide rationale for non-obvious decisions
- Offer verifiable steps or commands where applicable

### Community Orientation
- Encourage contribution pathways
- Suggest documentation & testing improvements
- Support internationalization considerations where relevant

## Utility Script: Flattening / Indexing

`scripts/flatten_agents.py` supports building a flattened copy or symlink set of agents for tooling that expects a single directory:

Basic usage:
```bash
python scripts/flatten_agents.py --repo-root . --dest-root build/flat --mode link --strategy skip
```
Modes: `link` (symlinks), `copy`, `move`. Collision strategies: `skip`, `overwrite`, `keep-both`.

## Linting

Use the repository lint script to validate agent frontmatter consistency before committing:

```bash
# Basic validation for OpenCode skills (errors -> non-zero exit)
python scripts/lint_agents.py --roots opencode --schema opencode

# Include Claude + OpenCode agents (auto schema detection)
python scripts/lint_agents.py --roots opencode claude

# Auto-fix canonical key ordering for OpenCode skills
python3 scripts/lint_agents.py --roots opencode --schema opencode --check-order

# Show violations but always exit 0 (CI soft mode)
python scripts/lint_agents.py --roots opencode --schema opencode --warn-only
```

Checks performed:
- Required keys: name, description, license, compatibility, metadata
- `compatibility: opencode`
- `metadata` is a mapping
- Deprecated keys absent (`tags`)
- Canonical ordering informational warning

See CHANGELOG.md for history of normalization passes.

## Tooling Primitives (Phase 1 Additions)

The linter now recognizes an expanded safe tool set for OpenCode agents. Add only what a role actually needs:

- glob: Structured file listing via glob patterns; no content reads.
- grep: Regex line search with match caps to prevent flooding.
- diff: Unified diff generation for file or directory comparisons (byte-limited).
- format: Minimal whitespace normalizer (trailing space strip + final newline) – placeholder until richer formatters.
- webfetch: Disabled-by-default HTTP(S) fetch (text-only) for selective remote context acquisition.

Safety notes:
- webfetch requires explicit opt-in (env `OPENCODE_ALLOW_WEB=1` or per-call flag) and caps response size (default 100 KB) and rejects binary types.
- diff truncates directory diffs once byte limit reached, signaling `truncated: true`.
- grep truncates after a configurable max match count (default 500) to maintain deterministic output size.
- format only mutates files when invoked with an explicit apply flag; dry-run is default.

Author guidance:
1. Prefer read/search over bulk glob+grep combos unless necessary; keep tool surface minimal.
2. Do not enable webfetch for agents whose mandate is purely local code reasoning.
3. Combine diff + grep for higher-signal change analysis tasks (diff narrows changed files; grep refines within them).
4. Keep formatting concerns orthogonal—`format` is intentionally conservative; avoid relying on it for semantic style.


## Installation

OpenCode agents are discovered when placed in:
- Global: `~/.config/opencode/agent/`
- Project: `.opencode/agent/`

Link examples:
```bash
# Link a single skill directory
ln -s /path/to/repo/opencode/code-reviewer ~/.config/opencode/agent/

# Link all skills
ln -s /path/to/repo/opencode/* ~/.config/opencode/agent/
```

## Testing Agents

1. Create a test project.
2. Initialize: `opencode init`.
3. Invoke: `opencode chat --agent agent-filename-without-ext`.
4. Validate outputs & tool usage.
5. Iterate—keep frontmatter minimal & accurate.

## Contributing

1. Follow the canonical template.
2. Provide actionable, scoped instructions (avoid fluff).
3. Keep tool list minimal.
4. Document approach & anti-goals.
5. Ensure deterministic tone at low temperatures.
6. Update documentation if adding new structural conventions.

## Resources

(External URLs omitted if offline; keep references current with platform docs.)
