# OPENCODE.md

This file provides guidance for using and creating OpenCode agents in this repository.

## Repository Overview

This repository contains AI agents for both Claude Code and OpenCode platforms. OpenCode agents are located in the `opencode/` directory and follow OpenCode's specific format and requirements.

## OpenCode Agent Structure

OpenCode agents use Markdown files with YAML frontmatter. The frontmatter configures the agent's behavior and capabilities.

### Frontmatter Specification (Canonical Order)

The recommended ordering of keys (omit any not used):

```yaml
---
description: Concise explanation of the agent's purpose
mode: subagent                 # primary | subagent | all
model: REPLACE_WITH_MODEL      # e.g. anthropic/claude-sonnet-4-20250514
temperature: 0.2               # 0.0-1.0 (determinism → creativity)
tools:                         # granular tool permissions (boolean map)
  read: true
  write: true
  edit: true
  bash: true
  search: true
# (optional additional keys: permissions, prompt, tags*, etc.)
---
```

Notes:
- `description` + `mode` are required.
- `model` is recommended (kept optional here to avoid forcing defaults during iterative authoring).
- `temperature` should be present; default to `0.2` for deterministic technical agents.
- `tools` MUST be a mapping, never a single-line string. Only include tools actually needed.
- The `name:` field is intentionally removed (filename serves as identifier).
- Legacy single-line style like `tools: read, write, edit` is unsupported—convert to the mapping form above.

### Minimal Example

```yaml
---
description: High-signal security code reviewer for backend services
mode: subagent
temperature: 0.2
tools:
  read: true
  edit: true
  search: true
---
```

### Legacy Normalization (Migration Performed)

A repository-wide normalization pass was executed (September 2025) to:
- Add `mode: subagent` where missing
- Convert legacy comma-delimited `tools:` lines to mapping form
- Remove inconsistent single-line tool declarations
- (Upcoming in this change) Remove all `name:` fields and add missing `temperature: 0.2`

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

### Referencing the Canonical Template

A maintained template lives at: `opencode/agent-template.md` — copy it when creating new agents instead of duplicating ad‑hoc snippets from documentation.

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

## Creating OpenCode Agents

Use the `opencode/agent-template.md` file as the authoritative starting point.

Key authoring steps:
1. Copy the template; rename file using lowercase hyphenated role (e.g. `cloud-architect.md`).
2. Update `description` (<= 120 chars, action-oriented).
3. Set `mode` (typically `subagent` unless designing a primary orchestration agent).
4. Choose a `model` if needed; otherwise rely on platform default.
5. Keep `temperature: 0.2` unless creative ideation is core (raise to 0.4–0.6).
6. Trim `tools` to the minimal required set.
7. Tailor prompt sections (Purpose, Capabilities, Workflow, Quality Bar, Anti-Goals, Examples).

### Model Selection

OpenCode uses fully qualified model identifiers (examples only; keep in sync with platform availability):
- `anthropic/claude-sonnet-4-20250514` – Balanced general work
- `anthropic/claude-opus-4-20250514` – Deep reasoning, complex architecture
- `anthropic/claude-haiku-4-20250514` – Fast, lightweight tasks

### Temperature Guidelines

- `0.0–0.3`: Deterministic (code review, refactors, migrations)
- `0.4–0.7`: Mixed creativity (architecture proposals, multi-step planning)
- `0.8–1.0`: High-divergence ideation (brainstorming, naming, novel design)

## Converting Claude Code Agents

1. Remove `name:` (filename is identifier).
2. Remove tag arrays not relevant to OpenCode runtime.
3. Ensure `mode: subagent` exists.
4. Add or retain `temperature` (default to 0.2 if deterministic role).
5. Convert `tools:` to mapping form (drop unused tools).
6. Adjust voice/style to align with OpenCode expectations (concise, action-oriented, transparent reasoning when valuable).

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
python scripts/flatten_agents.py --source opencode --target build/flat --mode link --strategy skip
```
Modes: `link` (symlinks), `copy`, `move`. Collision strategies: `skip`, `overwrite`, `rename`.

## Linting

Use the repository lint script to validate agent frontmatter consistency before committing:

```bash
# Basic validation (errors -> non‑zero exit)
python scripts/lint_agents.py --roots opencode --require-model

# Include Claude + OpenCode agents
python scripts/lint_agents.py --roots opencode claude --require-model

# Auto-add a default model where missing (will modify files)
python scripts/lint_agents.py --roots opencode --fix-missing-model anthropic/claude-sonnet-4-20250514

# Show violations but always exit 0 (CI soft mode)
python scripts/lint_agents.py --roots opencode --require-model --warn-only
```

Checks performed:
- Required keys: description, mode, temperature, tools (model recommended)
- `mode` in {primary, subagent, all}
- `temperature` within 0.0–1.0
- `tools` is a boolean mapping (no list or comma string)
- Deprecated keys absent (`name`, `tags`)
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
# Link a single agent
ln -s /path/to/repo/opencode/security/code-reviewer.md ~/.config/opencode/agent/

# Link an entire category
target_dir=~/.config/opencode/agent/security
mkdir -p "$target_dir"
ln -s /path/to/repo/opencode/security/* "$target_dir"/
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
