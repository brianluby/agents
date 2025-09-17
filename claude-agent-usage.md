# Claude Code Agent Usage Instructions

## Overview
Claude Code uses a detailed, structured format for custom subagents that enables sophisticated task delegation with fine-grained control over tools, models, and behavior.

## Installation

### Method 1: User-Level Installation (Recommended)
```bash
# Clone this repository to your home directory
cd ~
git clone https://github.com/brianluby/agents.git ~/.claude/agents

# Agents are immediately available to all Claude Code sessions
```

### Method 2: Project-Level Installation
```bash
# Clone directly into your project
cd /your/project
git clone https://github.com/brianluby/agents.git .claude/agents

# Project-level agents override user-level agents with the same name
```

## Using This Repository with Claude Code

### Direct Usage
All 81 agents in this repository are already formatted for Claude Code. Simply place them in `~/.claude/agents/` and they're ready to use:

```bash
# Copy all agents maintaining directory structure
cp -r languages infrastructure quality-security specialized-domains business support-documentation research-analysis seo game-development visual-tools ~/.claude/agents/
```

### Available Commands
- `/agents` - Interactive interface showing all available agents and tools
- Mention agent names directly: "Use the python-pro agent to refactor this code"
- Agents marked with "Use PROACTIVELY" will be automatically invoked based on context

## Agent Format Specification

### File Structure
```
~/.claude/agents/
├── category-name/
│   ├── agent-name.md
│   └── another-agent.md
└── custom-agent.md
```

### Agent File Format
```markdown
---
name: agent-name
description: When this agent should be invoked. Use PROACTIVELY for automatic invocation.
model: haiku|sonnet|opus  # Optional - defaults to parent model
tools: tool1, tool2       # Optional - inherits all if omitted
tags: [tag1, tag2]        # Optional - for organization
---

# System Prompt
Define the agent's role, expertise, and approach.
Include specific instructions, best practices, and constraints.
```

### Key Features

#### Model Selection Strategy
- **haiku**: Simple tasks, documentation, basic analysis
- **sonnet**: Standard development, most programming tasks
- **opus**: Complex analysis, security auditing, architecture

#### Tool Inheritance
- Omit `tools` field to inherit all tools including MCP tools
- Specify individual tools for granular control: `tools: Read, Write, Bash`

#### Automatic Invocation
Include "Use PROACTIVELY" in description for context-based auto-selection:
```yaml
description: "... Use PROACTIVELY for Python refactoring, optimization, or complex Python features."
```

#### Context Isolation
Each subagent operates in its own context window, preventing main thread pollution.

## Example Agents from This Repository

### Language Expert
```markdown
---
name: python-pro
description: Write idiomatic Python code with advanced features. Use PROACTIVELY for Python optimization.
model: sonnet
tools: Read, Write, Edit, Bash, Grep
---

You are a Python expert specializing in clean, performant code...
```

### Infrastructure Specialist
```markdown
---
name: kubernetes-engineer
description: Advanced Kubernetes configurations. Use PROACTIVELY for K8s implementations.
model: sonnet
---

You are a Kubernetes expert handling complex orchestration...
```

### Quality Assurance
```markdown
---
name: security-auditor
description: Review code for vulnerabilities. Use PROACTIVELY for security reviews.
model: opus
---

You are a security expert identifying and fixing vulnerabilities...
```

## Best Practices

1. **Leverage Proactive Agents**: Agents with "PROACTIVELY" will automatically engage when relevant
2. **Model Efficiency**: This repository optimizes model usage - Haiku for simple tasks, Opus for critical work
3. **Context Management**: Subagents maintain separate contexts, keeping main conversation clean
4. **Tool Optimization**: Most agents inherit all tools; specialized agents restrict to relevant tools
5. **Cascading Priority**: Project-level agents override user-level agents with same name

## Integration with Workflows

### Review Chains
```
python-pro → code-reviewer → security-auditor
```

### Parallel Execution
Claude Code can run multiple agents concurrently:
```
"Run both performance-engineer and database-optimizer in parallel"
```

### Conditional Routing
```
debugger analyzes issue → routes to error-detective or performance-engineer
```

## Troubleshooting

- **Agents not appearing**: Check `/agents` command to verify installation
- **Wrong model used**: Verify model field in agent file
- **Tools not available**: Check if tools field is restricting access
- **Agent not auto-invoked**: Ensure "Use PROACTIVELY" is in description

## Repository-Specific Notes

This repository contains 81 specialized agents organized by domain:
- 14 language experts (Python, JavaScript, Rust, etc.)
- 12 infrastructure specialists (DevOps, Cloud, Kubernetes)
- 9 quality & security agents
- 11 specialized domain experts (AI/ML, Finance, GraphQL)
- 6 business operations agents
- 6 documentation specialists
- 5 research & analysis agents
- 10 SEO specialists
- 2 game development agents
- 1 visual tool agent

All agents are pre-configured with optimal model selection and clear proactive invocation triggers.