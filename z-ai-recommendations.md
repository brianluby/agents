# Z.AI GLM-4.7 Integration Recommendations

## Executive Summary

This document outlines findings from Z.AI's official documentation and provides recommendations for supporting GLM-4.7 models in this agent repository.

**Key Finding**: The repository's `opencode_backup/` directory contains incorrect Z.AI model identifiers that would not work with Z.AI's actual APIs.

---

## Verified Z.AI Facts (from docs.z.ai)

### Model Identifiers

**Correct Format** (lowercase, no provider prefix):
- `glm-4.7` - Latest flagship model
- `glm-4.6` - Multimodal with 128K context
- `glm-4.5` - Earlier model
- `glm-4.5-air` - Haiku-equivalent tier

**Incorrect Formats in Repository**:
- `zai/glm-4.6` ❌ (used in opencode_backup/)
- `GLM-4.7` ❌ (uppercase, no provider prefix is actually correct but inconsistent)

### API Endpoints

1. **Standard OpenAI-Compatible API**
   ```
   https://api.z.ai/api/paas/v4
   ```

2. **GLM Coding Plan Endpoint** (coding scenarios only)
   ```
   https://api.z.ai/api/coding/paas/v4
   ```

3. **Anthropic-Compatible Endpoint** (for Claude Code)
   ```
   https://api.z.ai/api/anthropic
   ```

### Claude Code Integration Model Mapping

When using Z.AI with Claude Code via the Anthropic-compatible endpoint:

```json
{
  "ANTHROPIC_DEFAULT_OPUS_MODEL": "glm-4.7",
  "ANTHROPIC_DEFAULT_SONNET_MODEL": "glm-4.7",
  "ANTHROPIC_DEFAULT_HAIKU_MODEL": "glm-4.5-air"
}
```

**Configuration Location**: `~/.claude/settings.json`

```json
{
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "your_zai_api_key",
    "ANTHROPIC_BASE_URL": "https://api.z.ai/api/anthropic"
  }
}
```

### Z.AI Agent System (Separate from Markdown Agents)

Z.AI provides their own Agent API at `/api/v1/agents` which is:
- Completely different from Claude/OpenCode Markdown-based agent definitions
- Uses agent IDs (e.g., `general_translation`) instead of YAML frontmatter
- Has its own format with custom variables and streaming support
- **Not relevant** for this repository's agent format

---

## Current Repository Issues

### Incorrect Model Identifiers in Backup Directory

Files in `opencode_backup/` use incorrect formats:

```bash
# Found in opencode_backup/code-reviewer.md:
model: GLM-4.7  # ❌ Should be: glm-4.7

# Found in many opencode_backup/ files:
model: zai/glm-4.6  # ❌ Should be: glm-4.6
```

**Problem**: These identifiers would fail validation against Z.AI's actual APIs.

**Root Cause**: Appears to be experimental/unvalidated code that was never tested against Z.AI's real endpoints.

### Missing Infrastructure

- No Z.AI configuration automation scripts
- No documentation in `CLAUDE.md` or `OPENCODE.md` about Z.AI setup
- Model mappings in conversion scripts use incorrect `zai/` prefix
- Linter does not recognize `glm-4.x` model identifiers

---

## Two Integration Paths

### Path 1: Z.AI for Claude Code Users (Recommended)

**Approach**: Use Z.AI as Claude Code backend without modifying agent formats.

**How It Works**:
1. User configures Claude Code to use Z.AI's Anthropic-compatible endpoint
2. Claude Code's existing agents work unchanged
3. Claude Code maps model tiers (haiku/sonnet/opus) to GLM models automatically

**Advantages**:
- ✅ No agent format changes needed
- ✅ No conversion script updates required
- ✅ Existing Claude agents work immediately
- ✅ Leverages Z.AI's official Claude Code integration
- ✅ Minimal maintenance burden

**What Repository Needs**:
1. Add Z.AI configuration script to `scripts/`
2. Document Z.AI setup in `CLAUDE.md`
3. Optionally create quick-start guide

**Implementation**:

```bash
# scripts/setup-zai-claude.sh
#!/bin/bash
# Auto-configure Claude Code for Z.AI GLM-4.7

echo "Configuring Claude Code for Z.AI GLM-4.7..."

# Read API key
read -p "Enter your Z.AI API key: " ZAI_API_KEY

# Backup existing settings
cp ~/.claude/settings.json ~/.claude/settings.json.backup.$(date +%Y%m%d_%H%M%S)

# Create/update settings.json
mkdir -p ~/.claude
cat > ~/.claude/settings.json << EOF
{
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "$ZAI_API_KEY",
    "ANTHROPIC_BASE_URL": "https://api.z.ai/api/anthropic",
    "API_TIMEOUT_MS": "3000000"
  }
}
EOF

echo "✅ Claude Code configured for Z.AI"
echo "✅ Run 'claude' to start using GLM-4.7"
echo "✅ Use /status in Claude Code to verify model status"
```

### Path 2: Z.AI as OpenCode Alternative Provider

**Approach**: Add Z.AI GLM models as first-class models in OpenCode agent format.

**Advantages**:
- ✅ Direct GLM model support in OpenCode ecosystem
- ✅ Fine-grained model selection per agent
- ✅ More control over model configuration

**Disadvantages**:
- ❌ Requires fixing incorrect model identifiers across repository
- ❌ Requires linter validation updates
- ❌ Requires decision on model naming convention
- ❌ Higher maintenance burden
- ❌ More complex integration

**Required Changes**:

#### 1. Fix Model Mappings in Conversion Scripts

**`scripts/convert-agent.py`**:
```python
# Current (WRONG):
MODEL_MAPPING = {
    'zai/glm-4.6': 'sonnet',  # ❌
    ...
}

# Should be:
MODEL_MAPPING = {
    'glm-4.7': 'sonnet',
    'glm-4.6': 'sonnet',
    'glm-4.5': 'haiku',
    'glm-4.5-air': 'haiku',
}
```

**`scripts/convert_to_opencode.py`**:
```python
# Current (WRONG):
MODEL_MAPPING = {
    'haiku': 'claude-3-haiku-20240307',
    'sonnet': 'claude-3-5-sonnet-20241022',
    ...
}

# Should add:
MODEL_MAPPING = {
    # Existing Claude mappings...
    'haiku': 'glm-4.5-air',
    'sonnet': 'glm-4.7',
    'opus': 'glm-4.7',
}
```

#### 2. Update Linter Validation

**`scripts/lint_agents.py`**:
```python
# Add GLM model pattern recognition
ZAI_MODEL_PATTERN = r'^glm-4\.(7|6|5|5-air)$'

# Update model validation
if 'model' in fm:
    model_value = fm['model']
    # Accept both Claude and GLM formats
    if not (CLAUDE_MODEL_PATTERN.match(model_value) or
            ZAI_MODEL_PATTERN.match(model_value)):
        violations.append(Violation(path, f'Invalid model: {model_value}'))
```

#### 3. Update Templates

**`opencode/agent-template.md`**:
```yaml
---
# Example model options:
# Anthropic: anthropic/claude-sonnet-4-20250514, anthropic/claude-opus-4-20250514
# Z.AI: glm-4.7, glm-4.6, glm-4.5-air
description: High-signal [role] for [purpose]
mode: subagent
model: glm-4.7
temperature: 0.2
tools:
  read: true
  write: true
  edit: true
  bash: true
  search: true
---
```

#### 4. Design Decision: Model Naming Convention

**Option A**: Use GLM names directly in agents
```yaml
---
model: glm-4.7
---
```
- Pros: Explicit, no abstraction
- Cons: Inconsistent with existing Anthropic convention

**Option B**: Continue using Claude-tier names with provider mapping
```yaml
---
model: sonnet  # Maps to glm-4.7 via provider config
provider: zai  # New field to specify backend
---
```
- Pros: Consistent with current system
- Cons: More complexity, requires provider field

**Recommendation**: If implementing Path 2, use **Option A** (direct GLM names) for clarity.

---

## Recommendations

### Immediate Actions

1. **Delete or Archive `opencode_backup/` Directory**
   - Contains unvalidated experimental code
   - Model identifiers are incorrect
   - Could confuse users

2. **Document Z.AI Claude Code Integration** (if Path 1 chosen)
   - Add setup instructions to `CLAUDE.md`
   - Create configuration script
   - Add quick-start guide

3. **Fix Model Identifiers** (if Path 2 chosen)
   - Update all conversion scripts
   - Fix linter validation
   - Update templates

### Strategic Recommendation

**Choose Path 1 (Claude Code Integration) unless**:
- You have specific requirements to support OpenCode with Z.AI
- You need per-agent model selection beyond Claude tiers
- You're building OpenCode-specific tooling that requires different backends

**Rationale**:
- Z.AI already provides official Claude Code integration
- Path 1 requires minimal changes
- Existing agents work immediately
- Lower maintenance burden
- Leverages Z.AI's tested integration

### If Implementing Path 2

**Priority Order**:
1. Fix model identifiers in `scripts/convert-agent.py`
2. Fix model identifiers in `scripts/convert_to_opencode.py`
3. Update linter to accept GLM models
4. Update templates and documentation
5. Test conversion end-to-end with actual Z.AI API
6. Clean up `opencode_backup/` directory

**Testing Checklist**:
- [ ] Verify `glm-4.7` works with Z.AI API
- [ ] Test agent conversion scripts with GLM models
- [ ] Run linter on GLM-based agents
- [ ] Test Claude Code integration with Z.AI backend
- [ ] Document any deviations from Anthropic behavior

---

## Additional Resources

### Z.AI Documentation
- Quick Start: https://docs.z.ai
- Claude Code Integration: https://docs.z.ai/scenario-example/develop-tools/claude
- API Reference: https://docs.z.ai/api-reference/chat-completions
- GLM Models: https://docs.z.ai/docs/GLM-4.7

### Repository Documentation
- `CLAUDE.md` - Claude Code agent documentation
- `OPENCODE.md` - OpenCode agent documentation
- `AGENTS.md` - Repository conventions
- `scripts/lint_agents.py` - Agent validation

---

## Appendix: Incorrect Code in Repository

### `opencode_backup/code-reviewer.md`
```yaml
---
model: GLM-4.7  # ❌ Wrong case
---
```

### Multiple Files in `opencode_backup/`
```yaml
---
model: zai/glm-4.6  # ❌ Wrong prefix
---
```

These should be either fixed or removed to prevent confusion.

---

*Last Updated: 2025-12-30*
*Based on Z.AI documentation accessed via docs.z.ai*
