# Changelog

All notable changes to the agent repository will be documented here.

## [Unreleased]
### Added
- Linter: `--check-order` flag auto-fixes canonical key ordering.
- Linter: Enforces allowed tools set (`read`, `write`, `edit`, `bash`, `search`).
- Pre-commit hook example: `.githooks/agent-lint` (ordering auto-fix + validation before commit).

### Changed
- Linter summary now reports actual file count instead of placeholder.

### Removed / Completed Follow-Ups
- Implemented previously listed ordering auto-fix & hook wrapper tasks.

### Planned
- Guidance for future multi-model support / per-agent overrides.

## [2025-09-24] Frontmatter Normalization, Lint Script, Model Backfill
### Added
- `scripts/lint_agents.py` linter for OpenCode + Claude agent markdown:
  - Validates required keys (`description`, `mode`, `temperature`, `tools`, optional `model`).
  - Ensures `tools` is a boolean mapping.
  - Flags deprecated keys (`name`, `tags`).
  - Optionally inserts a default `model` with `--fix-missing-model`.

- `opencode/agent-template.md` canonical template with commented YAML + structured sections.
- `CHANGELOG.md` (this file) to track repository evolution.

### Changed
- Removed all legacy `name:` keys from OpenCode agents (filename now canonical identifier).
- Added `temperature: 0.2` to all OpenCode agents missing the field.
- Backfilled `model: anthropic/claude-sonnet-4-20250514` where model absent (excluding template).
- Updated `OPENCODE.md` with canonical frontmatter ordering, migration notes, and tool mapping specification.

### Migration Notes
- Legacy single-line `tools:` declarations converted to mapping form earlier (pre-changelog but documented now).
- Future contributors should invoke: `python scripts/lint_agents.py --roots opencode claude --require-model` before committing.

### Rationale
- Standardized metadata enables automated tooling, validation, and safer bulk transformations.
- Deterministic defaults (`temperature: 0.2`) promote reproducibility for technical agents.

### Follow-Ups (Not Yet Implemented)
- Add ordering auto-fix for non-canonical key order in linter (currently informational only).
- Extend linter to optionally enforce presence of `model` across both ecosystems by default.
- Introduce Git pre-commit hook wrapper invoking the linter.

---
Historical entries prior to this date were not maintained; this changelog starts post-normalization initiative.
