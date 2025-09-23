# OPENCODE.md

This file provides guidance for using and creating OpenCode agents in this repository.

## Repository Overview

This repository contains AI agents for both Claude Code and OpenCode platforms. OpenCode agents are located in the `opencode/` directory and follow OpenCode's specific format and requirements.

## OpenCode Agent Structure

OpenCode agents use Markdown files with YAML frontmatter. The frontmatter configures the agent's behavior and capabilities.

### Required Fields

```yaml
---
description: Brief explanation of the agent's purpose and capabilities
mode: subagent  # Options: primary, subagent, all
---
```

### Optional Fields

```yaml
---
model: anthropic/claude-sonnet-4-20250514  # Full model specification
temperature: 0.7  # Controls response creativity (0.0-1.0)
tools:  # Granular tool control
  write: true
  edit: false
  bash: true
permissions:  # Action permissions
  create_files: true
  modify_files: false
prompt: custom_prompt.md  # Reference to custom prompt file
---
```

## Agent Categories

### OpenCode-Specific Categories

The `opencode/` directory contains specialized categories focused on open-source principles:

- **open-source/**: License compliance, OSS contributions, community management
- **privacy-security/**: Privacy-first architectures, self-hosted solutions
- **decentralized/**: P2P, federated systems, blockchain architectures
- **open-hardware/**: Edge computing, IoT, embedded systems
- **community/**: Community health, translations, documentation
- **infrastructure/**: DevOps, cloud, and deployment specialists
- **languages/**: Programming language experts
- **quality-testing/**: Code review, testing, and quality assurance

### Shared Agents

The `shared/` directory contains agents that work across both Claude Code and OpenCode platforms with minimal modifications.

## Creating OpenCode Agents

### Agent Template

```markdown
---
description: [Concise description of agent's purpose and when to use it]
mode: subagent
model: anthropic/claude-sonnet-4-20250514
temperature: 0.7
tools:
  write: true
  edit: true
  bash: true
  read: true
---

You are a [role] specializing in [domain/expertise].

## Purpose
[Detailed explanation of the agent's role and objectives]

## Capabilities
- [List key capabilities and areas of expertise]
- [Include specific tools, frameworks, or methodologies]

## Approach
1. [Step-by-step approach to handling tasks]
2. [Include best practices and methodologies]

## Examples
- [Example use cases or interactions]
```

### Model Selection

OpenCode uses full model specifications:
- `anthropic/claude-sonnet-4-20250514` - Standard tasks
- `anthropic/claude-opus-4-20250514` - Complex reasoning
- `anthropic/claude-haiku-4-20250514` - Quick, simple tasks

### Temperature Guidelines

- `0.0-0.3`: Deterministic tasks (code review, testing)
- `0.4-0.7`: Balanced creativity (development, architecture)
- `0.8-1.0`: Creative tasks (brainstorming, design)

## Converting Claude Code Agents

To convert a Claude Code agent to OpenCode format:

1. **Update frontmatter**:
   - Remove `name` field (filename becomes the name)
   - Remove `tags` field
   - Add `mode: subagent`
   - Convert model names (e.g., `sonnet` → `anthropic/claude-sonnet-4-20250514`)
   - Add `temperature` based on task type
   - Add `tools` configuration if needed

2. **Adjust prompt content**:
   - Maintain the system prompt structure
   - Consider adding open-source specific guidance
   - Include transparency and explainability requirements

## Best Practices

### Open-Source Focus
- Prioritize open-source tools and libraries
- Include license compatibility checks
- Suggest self-hosted alternatives
- Emphasize community collaboration

### Privacy & Security
- Design with privacy-by-default principles
- Avoid telemetry and tracking
- Implement local-first architectures
- Use encryption for sensitive data

### Transparency
- Include reasoning traces
- Provide source citations
- Explain decision-making processes
- Document assumptions clearly

### Community Orientation
- Foster collaborative development
- Include contribution guidelines
- Support internationalization
- Encourage peer review

## Installation

OpenCode agents are automatically available when placed in:
- Global: `~/.config/opencode/agent/`
- Project: `.opencode/agent/`

To use agents from this repository:

```bash
# Link individual agents
ln -s /path/to/repo/opencode/category/agent.md ~/.config/opencode/agent/

# Or link entire categories
ln -s /path/to/repo/opencode/open-source ~/.config/opencode/agent/
```

## Testing Agents

1. Create a test project
2. Initialize OpenCode: `opencode init`
3. Test agent: `opencode chat --agent agent-name`
4. Verify behavior matches expectations

## Contributing

When contributing OpenCode agents:

1. Follow the template structure
2. Include comprehensive documentation
3. Test with various use cases
4. Ensure open-source compatibility
5. Add examples and use cases

## Resources

- [OpenCode Documentation](https://opencode.ai/docs/)
- [OpenCode Agents Guide](https://opencode.ai/docs/agents/)
- [OpenCode GitHub](https://github.com/opencode/opencode)