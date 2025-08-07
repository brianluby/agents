# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a collection of specialized AI subagents for Claude Code, designed to enhance development workflows with domain-specific expertise. Each subagent is a standalone Markdown file containing a YAML header with configuration and a system prompt defining its role and capabilities.

## Key Commands

Since this is a collection of agent definitions, there are no build, test, or lint commands. The primary operations are:

### Installation and Usage
```bash
# Install agents to Claude Code directory
cd ~/.claude
git clone https://github.com/brianluby/agents.git

# Agents are automatically available once placed in ~/.claude/agents/
```

### Agent Management
```bash
# View all available agents
ls *.md

# Search for specific agent types
grep -l "description.*security" *.md
grep -l "model: opus" *.md
```

## Architecture and Structure

### Agent File Format
Every agent follows this standardized structure:
```markdown
---
name: agent-name
description: When this subagent should be invoked
model: haiku|sonnet|opus  # Optional - specifies Claude model
tools: tool1, tool2        # Optional - defaults to all tools
---

System prompt defining the agent's role and capabilities
```

### Model Distribution Strategy
Agents are strategically assigned to different Claude models based on task complexity:

- **Haiku (9 agents)**: Simple, cost-effective tasks (data analysis, documentation)
- **Sonnet (34 agents)**: Standard development work (most programming languages, infrastructure)
- **Opus (13 agents)**: Complex analysis requiring maximum capability (security, architecture, AI/ML)

### Agent Categories

#### Language Specialists (14 agents)
Each language-specific agent follows similar patterns:
- Idiomatic code patterns and best practices
- Framework-specific expertise (e.g., Phoenix for Elixir, Spring for Java)
- Performance optimization techniques
- Comprehensive testing strategies
- Type safety where applicable

#### Infrastructure & Operations (8 agents)
Focus on production reliability:
- `devops-troubleshooter`: Production debugging and log analysis
- `incident-responder`: Critical outage response (Opus model for complexity)
- `database-optimizer`/`database-admin`: Query optimization and operations
- `terraform-specialist`: Infrastructure as Code patterns

#### Quality & Security (6 agents)
Critical system safety:
- `code-reviewer`: Configuration security emphasis, production reliability
- `security-auditor`: OWASP compliance, vulnerability scanning (Opus model)
- `performance-engineer`: Bottleneck analysis and optimization (Opus model)

#### Specialized Domains (10+ agents)
Domain-specific expertise:
- `ai-engineer`: LLM applications, RAG systems (Opus model for complexity)
- `quant-analyst`/`risk-manager`: Financial modeling and risk assessment
- `payment-integration`: Stripe, PayPal, and payment processor integration
- `legacy-modernizer`: Framework migrations and refactoring

### Common Agent Patterns

#### Proactive Invocation
Many agents specify "Use PROACTIVELY" in descriptions, meaning they should be automatically invoked based on context:
```yaml
description: "... Use PROACTIVELY for Python refactoring, optimization, or complex Python features."
```

#### Review Integration
Several agents are designed to work in review chains:
```
Primary Agent → Review Agent → Final Result
Example: payment-integration → security-auditor → Validated implementation
```

#### Model Optimization
Critical/complex agents use Opus model:
- Security auditing requiring deep analysis
- Incident response under time pressure  
- AI/ML engineering with complex architectures
- Financial modeling requiring precision

## Agent Orchestration Patterns

### Sequential Workflows
```
backend-architect → frontend-developer → test-automator → security-auditor
```

### Parallel Execution
```
performance-engineer + database-optimizer → Combined optimization recommendations
```

### Conditional Routing
```
debugger (analyzes issue) → Routes to appropriate specialist
```

## Configuration

### Claude Permissions
The repository includes `.claude/settings.local.json` with minimal permissions for find operations.

### GitHub Workflows
Contains GitHub Actions for:
- Content moderation
- New contributor welcome
- Issue templates for bug reports, feature requests, and new agent submissions

## Important Notes

- **No build system**: These are configuration files, not executable code
- **Model efficiency**: Haiku for simple tasks, Opus for critical analysis
- **Automatic delegation**: Claude Code selects agents based on context and descriptions
- **Explicit invocation**: Users can request specific agents by name
- **Integration ready**: Works with companion [Commands repository](https://github.com/brianluby/commands) for complex workflows

## Agent Development Guidelines

When creating new agents:
1. Use lowercase, hyphen-separated names
2. Write clear, specific descriptions for automatic invocation
3. Choose appropriate model based on task complexity
4. Include "Use PROACTIVELY" for context-triggered agents
5. Focus system prompts on specific domain expertise
6. Consider integration with existing agent review patterns