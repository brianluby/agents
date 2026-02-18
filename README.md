# AI Agents Collection for Claude Code & OpenCode

> 🙏 **This repository is forked from [wshobson/agents](https://github.com/wshobson/agents)**, the original creator of this comprehensive subagent collection. Thank you for building this amazing resource for the AI coding assistant community!

A comprehensive collection of specialized AI agents for both [Claude Code](https://docs.anthropic.com/en/docs/claude-code) and [OpenCode](https://opencode.ai/), providing domain-specific expertise across software development, infrastructure, and business operations.

## Overview

This repository provides production-ready agents that extend AI coding assistants' capabilities with specialized knowledge. The collection includes:

- **81 Claude Code agents** - Optimized for Claude's subagent system
- **81 OpenCode skills** - Mirrored from the Claude collection in OpenCode format

Each agent incorporates:

- Current industry best practices and standards (2024/2025)
- Production-ready patterns and enterprise architectures
- Deep domain expertise with 8-12 capability areas per agent
- Modern technology stacks and frameworks
- Optimized model selection based on task complexity

## Repository Structure

```
agents/
├── claude/          # Claude Code agents (flat files, e.g. claude/python-pro.md)
├── opencode/        # OpenCode skills (per-skill dirs, e.g. opencode/python-pro/SKILL.md)
├── scripts/         # Conversion, linting, and utility scripts
├── docs/            # Usage and migration docs
├── CLAUDE.md        # Claude Code specific documentation
├── OPENCODE.md      # OpenCode specific documentation
└── README.md        # This file
```

## Platform-Specific Documentation

- **Claude Code agents**: See [CLAUDE.md](CLAUDE.md) for setup and usage
- **OpenCode agents**: See [OPENCODE.md](OPENCODE.md) for setup and usage

## Claude Code Agents

Claude agents live as flat markdown files in `claude/`.

Quick examples:
- `claude/code-reviewer.md`
- `claude/security-auditor.md`
- `claude/python-pro.md`
- `claude/cloud-architect.md`

To list all available Claude agents:

```bash
ls claude/*.md
```

## Model Configuration

Claude agents specify model choice in each file's frontmatter (`haiku`, `sonnet`, `opus`, or provider-specific model IDs). Model assignment is based on task complexity and expected reasoning depth.

To inspect model usage in the current repo:

```bash
rg '^model:' claude/*.md
```

## OpenCode Agents

OpenCode skills are organized as one directory per skill under `opencode/`, each with a `SKILL.md` file. The current repository mirrors 81 skills from the Claude set.

Quick examples:
- `opencode/code-reviewer/SKILL.md`
- `opencode/security-auditor/SKILL.md`
- `opencode/python-pro/SKILL.md`
- `opencode/cloud-architect/SKILL.md`

To list all available OpenCode skills:

```bash
ls opencode/*/SKILL.md
```

### OpenCode Features

- **Open-source focused**: Prioritizes FOSS tools and libraries
- **Privacy by default**: Local-first processing and data minimization
- **Transparent operation**: Includes reasoning traces and decision explanations
- **Community oriented**: Supports collaborative development patterns
- **Self-hostable**: Designed for on-premise and air-gapped deployments

## Installation

### For Claude Code

**Note**: Claude Code expects agents directly in `~/.claude/agents/`, not in subdirectories. See [INSTALLATION.md](INSTALLATION.md) for detailed setup options.

Quick setup with symlink:
```bash
git clone https://github.com/brianluby/agents.git ~/agents-repo
ln -s ~/agents-repo/claude ~/.claude/agents
```

### For OpenCode

```bash
# Clone the repository
git clone https://github.com/brianluby/agents.git

# Link OpenCode agents globally
ln -s /path/to/agents/opencode/* ~/.config/opencode/agent/

# Or link to a project
ln -s /path/to/agents/opencode/* .opencode/agent/
```

See [OPENCODE.md](OPENCODE.md) for detailed OpenCode setup instructions.

### Linting Agents

Validate agent metadata before committing:
```bash
python scripts/lint_agents.py --roots opencode claude --require-model
```
Auto-fill missing model values:
```bash
python3 scripts/lint_agents.py --roots opencode --fix-missing-model zai/glm-4.6
```
Auto-fix canonical key ordering & validate allowed tools:
```bash
python scripts/lint_agents.py --roots opencode claude --check-order --require-model
```
Soft (non-failing) report mode:
```bash
python scripts/lint_agents.py --roots opencode --require-model --warn-only
```
Install pre-commit hook:
```bash
ln -s ../../.githooks/agent-lint .git/hooks/pre-commit
```
See CHANGELOG.md for normalization history.

### Tooling Utilities (Phase 1)

The repo ships lightweight tool scripts (under `scripts/tools/`) used by some OpenCode agents or local workflows:

- `glob_tool.py` – Glob file listing (no content read)
- `grep_tool.py` – Regex line search with match cap (default 500)
- `diff_tool.py` – Unified diff (file↔file / dir↔dir) with byte limit
- `format_tool.py` – Minimal trailing-space + final newline normalizer (dry-run by default)
- `webfetch_tool.py` – Disabled-by-default HTTP(S) fetch (text-only, 100 KB cap, requires `--allow` or `OPENCODE_ALLOW_WEB=1`)

List allowed agent tool names:
```bash
python scripts/lint_agents.py --list-tools
```
Enable only what an agent strictly needs; omit `webfetch` unless remote context is essential.


## Usage

### Automatic Delegation
Claude Code automatically selects the appropriate subagent based on task context and requirements. The system analyzes your request and delegates to the most suitable specialist.

### Explicit Invocation
Specify a subagent by name to use a particular specialist:

```
"Use code-reviewer to analyze the recent changes"
"Have security-auditor scan for vulnerabilities"
"Get performance-engineer to optimize this bottleneck"
```

## Usage Examples

### Code Quality & Security
```
code-reviewer: Analyze component for best practices
security-auditor: Check for OWASP compliance
tdd-orchestrator: Implement feature with test-first approach
performance-engineer: Profile and optimize bottlenecks
```

### Development & Architecture
```
backend-architect: Design authentication API
frontend-developer: Create responsive dashboard
graphql-architect: Design federated GraphQL schema
mobile-developer: Build cross-platform mobile app
```

### Infrastructure & Operations
```
devops-troubleshooter: Analyze production logs
cloud-architect: Design scalable AWS architecture
network-engineer: Debug SSL certificate issues
database-admin: Configure backup and replication
terraform-specialist: Write infrastructure modules
```

### Data & Machine Learning
```
data-scientist: Analyze customer behavior dataset
ai-engineer: Build RAG system for document search
mlops-engineer: Set up experiment tracking
ml-engineer: Deploy model to production
```

### Business & Documentation
```
business-analyst: Create metrics dashboard
documentation-expert: Generate technical documentation
api-documenter: Write OpenAPI specifications
content-marketer: Create SEO-optimized content
```

## Multi-Agent Workflows

Subagents coordinate automatically for complex tasks. The system intelligently sequences multiple specialists based on task requirements.

### Common Workflow Patterns

**Feature Development**
```
"Implement user authentication"
→ backend-architect → frontend-developer → test-automator → security-auditor
```

**Performance Optimization**
```
"Optimize checkout process"
→ performance-engineer → database-optimizer → frontend-developer
```

**Production Incidents**
```
"Debug high memory usage"
→ incident-responder → devops-troubleshooter → debugger → performance-engineer
```

**Infrastructure Setup**
```
"Set up disaster recovery"
→ database-admin → database-optimizer → terraform-specialist
```

**ML Pipeline Development**
```
"Build ML pipeline with monitoring"
→ mlops-engineer → ml-engineer → data-engineer → performance-engineer
```

### Integration with Claude Code Commands

For sophisticated multi-agent orchestration, use the [Claude Code Commands](https://github.com/brianluby/commands) collection which provides 52 pre-built slash commands:

```
/full-stack-feature   # Coordinates 8+ agents for complete feature development
/incident-response    # Activates incident management workflow
/ml-pipeline         # Sets up end-to-end ML infrastructure
/security-hardening  # Implements security best practices across stack
```

## Subagent Format

Each subagent is defined as a Markdown file with frontmatter:

```markdown
---
name: subagent-name
description: Activation criteria for this subagent
model: haiku|sonnet|opus  # Optional: Model selection
tools: tool1, tool2       # Optional: Tool restrictions
---

System prompt defining the subagent's expertise and behavior
```

### Model Selection Criteria

- **haiku**: Simple, deterministic tasks with minimal reasoning
- **sonnet**: Standard development and engineering tasks
- **opus**: Complex analysis, architecture, and critical operations

## Agent Orchestration Patterns

### Sequential Processing
Agents execute in sequence, passing context forward:
```
backend-architect → frontend-developer → test-automator → security-auditor
```

### Parallel Execution
Multiple agents work simultaneously on different aspects:
```
performance-engineer + database-optimizer → Merged analysis
```

### Conditional Routing
Dynamic agent selection based on analysis:
```
debugger → [backend-architect | frontend-developer | devops-troubleshooter]
```

### Validation Pipeline
Primary work followed by specialized review:
```
payment-integration → security-auditor → Validated implementation
```

## Agent Selection Guide

### Architecture & Planning

| Task | Recommended Agent | Key Capabilities |
|------|------------------|------------------|
| API Design | `backend-architect` | RESTful APIs, microservices, database schemas |
| Cloud Infrastructure | `cloud-architect` | AWS/Azure/GCP design, scalability planning |
| UI/UX Design | `ui-ux-designer` | Interface design, wireframes, design systems |
| System Architecture | `architect-review` | Pattern validation, consistency analysis |

### Development by Language

| Language Category | Agents | Primary Use Cases |
|-------------------|--------|-------------------|
| Systems Programming | `c-pro`, `cpp-pro`, `rust-pro`, `golang-pro` | OS interfaces, embedded systems, high performance |
| Web Development | `javascript-pro`, `typescript-pro`, `python-pro`, `ruby-pro`, `php-pro` | Full-stack web applications, APIs, scripting |
| Web Frameworks | `django-pro`, `fastapi-pro` | Django and FastAPI development |
| Enterprise | `java-pro`, `csharp-pro`, `scala-pro` | Large-scale applications, enterprise systems |
| Mobile | `ios-developer`, `flutter-expert`, `mobile-developer` | Native and cross-platform mobile apps |
| Specialized | `elixir-pro`, `unity-developer`, `minecraft-bukkit-pro` | Domain-specific development |

### Operations & Infrastructure

| Task | Recommended Agent | Key Capabilities |
|------|------------------|------------------|
| Production Issues | `devops-troubleshooter` | Log analysis, deployment debugging |
| Critical Incidents | `incident-responder` | Outage response, immediate mitigation |
| Database Performance | `database-optimizer` | Query optimization, indexing strategies |
| Database Operations | `database-admin` | Backup, replication, disaster recovery |
| Infrastructure as Code | `terraform-specialist` | Terraform modules, state management |
| Network Issues | `network-engineer` | Network debugging, load balancing |
| Kubernetes | `kubernetes-engineer` | K8s configurations, cluster management |
| Platform Engineering | `platform-engineer` | Internal developer platforms, service mesh |
| Site Reliability | `sre-engineer` | SLIs/SLOs, error budgets, reliability practices |

### Quality & Security

| Task | Recommended Agent | Key Capabilities |
|------|------------------|------------------|
| Code Review | `code-reviewer` | Security focus, best practices |
| Security Audit | `security-auditor` | Vulnerability scanning, OWASP compliance |
| Test Creation | `test-automator` | Unit, integration, E2E test suites |
| Performance Issues | `performance-engineer` | Profiling, optimization |
| Bug Investigation | `debugger` | Error resolution, root cause analysis |
| QA Engineering | `qa-engineer` | Manual testing strategies, test plans |
| Config Security | `config-security-auditor` | Configuration security, secrets management |
| Supply Chain Security | `supply-chain-security` | Dependency scanning, SBOM generation |

### Data & Machine Learning

| Task | Recommended Agent | Key Capabilities |
|------|------------------|------------------|
| Data Analysis | `data-scientist` | SQL queries, statistical analysis |
| LLM Applications | `ai-engineer` | RAG systems, prompt pipelines |
| ML Development | `ml-engineer` | Model training, feature engineering |
| ML Operations | `mlops-engineer` | ML infrastructure, experiment tracking |

### Documentation & Business

| Task | Recommended Agent | Key Capabilities |
|------|------------------|------------------|
| Technical Docs | `documentation-expert` | Comprehensive documentation generation |
| API Documentation | `api-documenter` | OpenAPI/Swagger specifications |
| Technical Writing | `documentation-expert` | User guides, tutorials, documentation |
| Tutorial Creation | `documentation-expert` | Step-by-step educational content |
| Reference Building | `reference-builder` | Technical references, API docs |
| Product Management | `product-manager` | Feature prioritization, roadmaps |
| Business Metrics | `business-analyst` | KPI tracking, reporting |
| Legal Compliance | `legal-advisor` | Privacy policies, terms of service |

## Best Practices

### Task Delegation
1. **Automatic selection** - Let Claude Code analyze context and select optimal agents
2. **Clear requirements** - Specify constraints, tech stack, and quality standards
3. **Trust specialization** - Each agent is optimized for their specific domain

### Multi-Agent Workflows
1. **High-level requests** - Allow agents to coordinate complex multi-step tasks
2. **Context preservation** - Ensure agents have necessary background information
3. **Integration review** - Verify how different agents' outputs work together

### Explicit Control
1. **Direct invocation** - Specify agents when you need particular expertise
2. **Strategic combination** - Use multiple specialists for validation
3. **Review patterns** - Request specific review workflows (e.g., "security-auditor reviews API design")

### Performance Optimization
1. **Monitor effectiveness** - Track which agents work best for your use cases
2. **Iterative refinement** - Use agent feedback to improve requirements
3. **Complexity matching** - Align task complexity with agent capabilities

## Contributing

To add a new subagent:

1. Create a new `.md` file with appropriate frontmatter
2. Use lowercase, hyphen-separated naming convention
3. Write clear activation criteria in the description
4. Define comprehensive system prompt with expertise areas

## Troubleshooting

### Agent Not Activating
- Ensure request clearly indicates the domain
- Be specific about task type and requirements
- Use explicit invocation if automatic selection fails

### Unexpected Agent Selection
- Provide more context about tech stack
- Include specific requirements in request
- Use direct agent naming for precise control

### Conflicting Recommendations
- Normal behavior - specialists have different priorities
- Request reconciliation between specific agents
- Consider trade-offs based on project requirements

### Missing Context
- Include background information in requests
- Reference previous work or patterns
- Provide project-specific constraints

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Resources

- [Claude Code Documentation](https://docs.anthropic.com/en/docs/claude-code)
- [Subagents Documentation](https://docs.anthropic.com/en/docs/claude-code/sub-agents)
- [Claude Code GitHub](https://github.com/anthropics/claude-code)
- [Claude Code Commands](https://github.com/brianluby/commands)
