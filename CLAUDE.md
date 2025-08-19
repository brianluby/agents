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
find . -name "*.md" -not -path "./.git/*" | grep -v "README\|TODO\|CLAUDE\|AGENT_DEPENDENCY_MAP"

# View agents by category
ls languages/          # Language-specific programming agents
ls infrastructure/     # DevOps, cloud, and infrastructure agents  
ls quality-security/   # Code review, testing, and security agents
ls specialized-domains/# AI/ML, finance, GraphQL, and domain experts
ls business/           # Product, sales, and business-focused agents
ls support-documentation/# Technical writing and documentation agents
ls research-analysis/  # Data analysis and research agents

# Search for specific agent types
grep -l "description.*security" */*.md
grep -l "model: opus" *//*.md
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

The agents are organized into 7 main categories based on their capabilities:

#### Languages (14 agents)
Located in `languages/` - Language-specific programming expertise:
- Core languages: `python-pro`, `javascript-pro`, `typescript-pro`, `golang-pro`, `rust-pro`, `java-pro`, `cpp-pro`, `c-pro`, `csharp-pro`, `php-pro`, `elixir-pro`
- Platform-specific: `ios-developer`, `mobile-developer`, `unity-developer`
- Each follows patterns: idiomatic code, framework expertise, performance optimization, testing strategies

#### Infrastructure (12 agents) 
Located in `infrastructure/` - DevOps, cloud, and system operations:
- Operations: `devops-troubleshooter`, `incident-responder`, `sre-engineer`, `observability-engineer`
- Cloud & Infrastructure: `cloud-architect`, `terraform-specialist`, `kubernetes-engineer`, `deployment-engineer`, `platform-engineer`, `network-engineer`
- Data: `database-admin`, `database-optimizer`

#### Quality & Security (9 agents)
Located in `quality-security/` - Code quality, testing, and security:
- Review & Quality: `code-reviewer`, `architect-review`, `qa-engineer`, `test-automator`
- Debugging: `debugger`, `error-detective`, `performance-engineer`
- Maintenance: `legacy-modernizer`, `security-auditor`

#### Specialized Domains (11 agents)
Located in `specialized-domains/` - Domain-specific technical expertise:
- AI/ML: `ai-engineer`, `ml-engineer`, `mlops-engineer`, `prompt-engineer`
- Finance: `quant-analyst`, `risk-manager`, `payment-integration`
- Architecture: `backend-architect`, `frontend-developer`, `graphql-architect`
- Developer Experience: `dx-optimizer`

#### Business (6 agents)
Located in `business/` - Business operations and growth:
- Strategy: `product-manager`, `business-analyst`
- Marketing: `sales-automator`, `content-marketer`
- Support: `customer-support`, `legal-advisor`

#### Support & Documentation (6 agents)
Located in `support-documentation/` - Technical writing and documentation:
- Documentation: `technical-writer`, `docs-architect`, `api-documenter`, `reference-builder`, `tutorial-engineer`
- Design: `ui-ux-designer`

#### Research & Analysis (5 agents)
Located in `research-analysis/` - Data analysis and information gathering:
- Data: `data-scientist`, `data-engineer`, `sql-pro`
- Research: `search-specialist`, `context-manager`

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