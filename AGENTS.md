# AGENTS.md

Authoritative quick-reference for agentic coding tools operating in this repo.

1. Project Type: Markdown agent definitions + lightweight Python/CLI conversion scripts. No native test suite; add tests only if explicitly requested.
2. Environment Setup: `python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt`.
3. Build/Run Scripts:
   - Convert single file → OpenCode: `python scripts/convert-agent.py claude/path/agent.md opencode/dev/agent.md --to=opencode`.
   - Convert single file → Claude: `python scripts/convert-agent.py opencode/dev/agent.md claude/path/agent.md --to=claude`.
   - Bulk convert (rich progress): `python scripts/convert_to_opencode.py --source-dir claude --target-dir opencode` (add `--dry-run` first).
   - Simple shell converter: `bash scripts/convert-agent-simple.sh in.md out.md opencode|claude`.
4. Lint/Format: Keep scripts <200 lines cohesive; use PEP8 (120 char soft limit), f-strings, explicit imports (one per line, stdlib → third-party → local, blank line between groups). No autoformatter configured—do minimal, surgical edits.
5. Types & Style: Prefer type hints in new/modified Python functions. Pure functions first; side effects (file writes) isolated. Use early returns; avoid deep nesting.
6. Naming: snake_case for files/functions, UPPER_SNAKE_CASE for constants, PascalCase only for classes. Markdown agent filenames remain lowercase hyphen-separated.
7. Error Handling: Validate file existence; print concise error then `sys.exit(1)` for unrecoverable CLI issues. Do not swallow exceptions silently; narrow except blocks.
8. YAML Frontmatter: Maintain existing keys; when adding keep ordering: name, description, model, tools (Claude) OR description, mode, model, temperature, tools (OpenCode). Remove deprecated `name` when migrating to OpenCode; use `scripts/lint_agents.py` to verify (`--check-order` auto-fixes ordering; allowed tools enforced: read, write, edit, bash, search).
9. Imports: Standard library first, then third-party (pyyaml, click, rich), then local scripts; no wildcard imports; sort logically (optional alphabetical within group).
10. Logging/Output: Use `print()` or rich console (already imported) for user-facing CLI; never add verbose debug unless user requests.
11. Performance: Scripts run on small sets; prefer clarity over micro-optimizations. Avoid unnecessary rereads of files.
12. Security: No network calls. Do not execute user-provided code. Only touch intended paths; never modify LICENSE.
13. Editing Policy: Change only what user asks; keep unrelated content intact. Do not mass refactor agent prompts without instruction.
14. Tests: None present. If a test is added later, run single test via `pytest path::TestClass::test_name`. Otherwise avoid adding pytest dependency.
15. PR Hygiene: Small, atomic changes; clear commit messages focusing on “why”.
16. Prohibited: Adding secret tokens, broad `git add .`, introducing new tooling (ruff/black) without request.
17. Large File Handling: Avoid printing full agent prompt bodies unless user explicitly asks.
18. Cursor/Copilot Rules: None detected (no .cursor/rules/, .cursorrules, or .github/copilot-instructions.md). If added later, update this file.
19. Autonomy: Use existing conversion patterns; preserve semantic meaning of prompts. Prefer additive over destructive edits.
20. When Unsure: Ask for clarification before restructuring directory layouts or renaming agents.

See CHANGELOG.md for repository-wide normalization & tooling history.
