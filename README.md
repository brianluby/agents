# AI Agents Collection for Claude Code & OpenCode

> 🙏 **This repository is forked from [wshobson/agents](https://github.com/wshobson/agents)**, the original creator of this comprehensive subagent collection. Thank you for building this amazing resource for the AI coding assistant community!

A comprehensive collection of specialized AI agents for both [Claude Code](https://docs.anthropic.com/en/docs/claude-code) and [OpenCode](https://opencode.ai/), providing domain-specific expertise across software development, infrastructure, and business operations.

## Overview

This repository provides production-ready agents that extend AI coding assistants' capabilities with specialized knowledge. The collection includes:

- **90+ Claude Code agents** - Optimized for Claude's subagent system
- **OpenCode agents** - Designed with open-source principles and privacy-first approach
- **Shared agents** - Cross-platform compatible agents

Each agent incorporates:

- Current industry best practices and standards (2024/2025)
- Production-ready patterns and enterprise architectures
- Deep domain expertise with 8-12 capability areas per agent
- Modern technology stacks and frameworks
- Optimized model selection based on task complexity

## Repository Structure

```
agents/
├── claude/          # Claude Code specific agents
│   ├── business/
│   ├── infrastructure/
│   ├── languages/
│   ├── quality-security/
│   └── ...
├── opencode/        # OpenCode specific agents
│   ├── open-source/
│   ├── privacy-security/
│   ├── infrastructure/
│   └── ...
├── shared/          # Cross-platform compatible agents
├── CLAUDE.md        # Claude Code specific documentation
├── OPENCODE.md      # OpenCode specific documentation
└── README.md        # This file
```

## Platform-Specific Documentation

- **Claude Code agents**: See [CLAUDE.md](CLAUDE.md) for setup and usage
- **OpenCode agents**: See [OPENCODE.md](OPENCODE.md) for setup and usage

## Claude Code Agent Categories

### Architecture & System Design

#### Core Architecture

| Agent | Model | Description |
|-------|-------|-------------|
| [backend-architect](claude/specialized-domains/backend-architect.md) | opus | RESTful API design, microservice boundaries, database schemas |
| [frontend-developer](claude/specialized-domains/frontend-developer.md) | sonnet | React components, responsive layouts, client-side state management |
| [graphql-architect](claude/specialized-domains/graphql-architect.md) | opus | GraphQL schemas, resolvers, federation architecture |
| [architect-review](claude/quality-security/architect-review.md) | opus | Architectural consistency analysis and pattern validation |
| [cloud-architect](claude/infrastructure/cloud-architect.md) | opus | AWS/Azure/GCP infrastructure design and cost optimization |
| [hybrid-cloud-architect](claude/infrastructure/hybrid-cloud-architect.md) | opus | Multi-cloud strategies across cloud and on-premises environments |
| [kubernetes-architect](claude/infrastructure/kubernetes-architect.md) | opus | Cloud-native infrastructure with Kubernetes and GitOps |

#### UI/UX & Mobile

| Agent | Model | Description |
|-------|-------|-------------|
| [ui-ux-designer](claude/support-documentation/ui-ux-designer.md) | sonnet | Interface design, wireframes, design systems |
| [ui-visual-validator](claude/quality-security/ui-visual-validator.md) | sonnet | Visual regression testing and UI verification |
| [mobile-developer](claude/languages/mobile-developer.md) | sonnet | React Native and Flutter application development |
| [ios-developer](claude/languages/ios-developer.md) | sonnet | Native iOS development with Swift/SwiftUI |
| [flutter-expert](claude/languages/flutter-expert.md) | sonnet | Advanced Flutter development with state management |

### Programming Languages

#### Systems & Low-Level

| Agent | Model | Description |
|-------|-------|-------------|
| [c-pro](claude/languages/c-pro.md) | sonnet | System programming with memory management and OS interfaces |
| [cpp-pro](claude/languages/cpp-pro.md) | sonnet | Modern C++ with RAII, smart pointers, STL algorithms |
| [rust-pro](claude/languages/rust-pro.md) | sonnet | Memory-safe systems programming with ownership patterns |
| [golang-pro](claude/languages/golang-pro.md) | sonnet | Concurrent programming with goroutines and channels |

#### Web & Application

| Agent | Model | Description |
|-------|-------|-------------|
| [javascript-pro](claude/languages/javascript-pro.md) | sonnet | Modern JavaScript with ES6+, async patterns, Node.js |
| [typescript-pro](claude/languages/typescript-pro.md) | sonnet | Advanced TypeScript with type systems and generics |
| [python-pro](claude/languages/python-pro.md) | sonnet | Python development with advanced features and optimization |
| [ruby-pro](claude/languages/ruby-pro.md) | sonnet | Ruby with metaprogramming, Rails patterns, gem development |
| [php-pro](claude/languages/php-pro.md) | sonnet | Modern PHP with frameworks and performance optimization |

#### Enterprise & JVM

| Agent | Model | Description |
|-------|-------|-------------|
| [java-pro](claude/languages/java-pro.md) | sonnet | Modern Java with streams, concurrency, JVM optimization |
| [scala-pro](claude/languages/scala-pro.md) | sonnet | Enterprise Scala with functional programming and distributed systems |
| [csharp-pro](claude/languages/csharp-pro.md) | sonnet | C# development with .NET frameworks and patterns |

#### Specialized Platforms

| Agent | Model | Description |
|-------|-------|-------------|
| [elixir-pro](claude/languages/elixir-pro.md) | sonnet | Elixir with OTP patterns and Phoenix frameworks |
| [unity-developer](claude/languages/unity-developer.md) | sonnet | Unity game development and optimization |
| [minecraft-bukkit-pro](claude/languages/minecraft-bukkit-pro.md) | sonnet | Minecraft server plugin development |
| [django-pro](claude/specialized-domains/django-pro.md) | sonnet | Django 5.x with async views, DRF, Celery, Django Channels |
| [fastapi-pro](claude/specialized-domains/fastapi-pro.md) | sonnet | High-performance async APIs with FastAPI, SQLAlchemy 2.0 |
| [sql-pro](claude/research-analysis/sql-pro.md) | sonnet | Complex SQL queries and database optimization |

### Infrastructure & Operations

#### DevOps & Deployment

| Agent | Model | Description |
|-------|-------|-------------|
| [devops-troubleshooter](claude/infrastructure/devops-troubleshooter.md) | sonnet | Production debugging, log analysis, deployment troubleshooting |
| [deployment-engineer](claude/infrastructure/deployment-engineer.md) | sonnet | CI/CD pipelines, containerization, cloud deployments |
| [terraform-specialist](claude/infrastructure/terraform-specialist.md) | opus | Infrastructure as Code with Terraform modules and state management |
| [kubernetes-engineer](claude/infrastructure/kubernetes-engineer.md) | sonnet | Advanced K8s configurations, operator development, cluster management |
| [platform-engineer](claude/infrastructure/platform-engineer.md) | sonnet | Internal developer platforms, service mesh, developer tooling |
| [sre-engineer](claude/infrastructure/sre-engineer.md) | opus | SLIs/SLOs, error budgets, reliability practices |
| [dx-optimizer](claude/specialized-domains/dx-optimizer.md) | sonnet | Developer experience optimization and tooling improvements |

#### Database Management

| Agent | Model | Description |
|-------|-------|-------------|
| [database-optimizer](claude/infrastructure/database-optimizer.md) | opus | Query optimization, index design, migration strategies |
| [database-admin](claude/infrastructure/database-admin.md) | sonnet | Database operations, backup, replication, monitoring |

#### Incident Response & Network

| Agent | Model | Description |
|-------|-------|-------------|
| [incident-responder](claude/infrastructure/incident-responder.md) | opus | Production incident management and resolution |
| [network-engineer](claude/infrastructure/network-engineer.md) | sonnet | Network debugging, load balancing, traffic analysis |

### Quality Assurance & Security

#### Code Quality & Review

| Agent | Model | Description |
|-------|-------|-------------|
| [code-reviewer](claude/quality-security/code-reviewer.md) | opus | Code review with security focus and production reliability |
| [security-auditor](claude/quality-security/security-auditor.md) | opus | Vulnerability assessment and OWASP compliance |
| [backend-security-coder](claude/quality-security/backend-security-coder.md) | opus | Secure backend coding practices, API security implementation |
| [frontend-security-coder](claude/quality-security/frontend-security-coder.md) | opus | XSS prevention, CSP implementation, client-side security |
| [mobile-security-coder](claude/quality-security/mobile-security-coder.md) | opus | Mobile security patterns, WebView security, biometric auth |
| [architect-reviewer](claude/quality-security/architect-review.md) | opus | Architectural consistency and pattern validation |

#### Testing & Debugging

| Agent | Model | Description |
|-------|-------|-------------|
| [test-automator](claude/quality-security/test-automator.md) | sonnet | Comprehensive test suite creation (unit, integration, e2e) |
| [tdd-orchestrator](claude/quality-security/tdd-orchestrator.md) | sonnet | Test-Driven Development methodology guidance |
| [debugger](claude/quality-security/debugger.md) | sonnet | Error resolution and test failure analysis |
| [error-detective](claude/quality-security/error-detective.md) | sonnet | Log analysis and error pattern recognition |

#### Performance & Observability

| Agent | Model | Description |
|-------|-------|-------------|
| [performance-engineer](claude/quality-security/performance-engineer.md) | opus | Application profiling and optimization |
| [observability-engineer](claude/infrastructure/observability-engineer.md) | opus | Production monitoring, distributed tracing, SLI/SLO management |
| [search-specialist](claude/research-analysis/search-specialist.md) | haiku | Advanced web research and information synthesis |

### Data & AI

#### Data Engineering & Analytics

| Agent | Model | Description |
|-------|-------|-------------|
| [data-scientist](claude/research-analysis/data-scientist.md) | opus | Data analysis, SQL queries, BigQuery operations |
| [data-engineer](claude/research-analysis/data-engineer.md) | sonnet | ETL pipelines, data warehouses, streaming architectures |

#### Machine Learning & AI

| Agent | Model | Description |
|-------|-------|-------------|
| [ai-engineer](claude/specialized-domains/ai-engineer.md) | opus | LLM applications, RAG systems, prompt pipelines |
| [ml-engineer](claude/specialized-domains/ml-engineer.md) | opus | ML pipelines, model serving, feature engineering |
| [mlops-engineer](claude/specialized-domains/mlops-engineer.md) | opus | ML infrastructure, experiment tracking, model registries |
| [prompt-engineer](claude/specialized-domains/prompt-engineer.md) | opus | LLM prompt optimization and engineering |

### Documentation & Technical Writing

| Agent | Model | Description |
|-------|-------|-------------|
| [docs-architect](claude/support-documentation/docs-architect.md) | opus | Comprehensive technical documentation generation |
| [technical-writer](claude/support-documentation/technical-writer.md) | opus | User guides, API documentation, tutorials |
| [api-documenter](claude/support-documentation/api-documenter.md) | sonnet | OpenAPI/Swagger specifications and developer docs |
| [reference-builder](claude/support-documentation/reference-builder.md) | haiku | Technical references and API documentation |
| [tutorial-engineer](claude/support-documentation/tutorial-engineer.md) | sonnet | Step-by-step tutorials and educational content |
| [mermaid-expert](claude/support-documentation/mermaid-expert.md) | sonnet | Diagram creation (flowcharts, sequences, ERDs) |

### Business & Operations

#### Business Analysis & Finance

| Agent | Model | Description |
|-------|-------|-------------|
| [business-analyst](claude/business/business-analyst.md) | sonnet | Metrics analysis, reporting, KPI tracking |
| [product-manager](claude/business/product-manager.md) | haiku | Feature prioritization, roadmaps, stakeholder alignment |
| [quant-analyst](claude/specialized-domains/quant-analyst.md) | opus | Financial modeling, trading strategies, market analysis |
| [risk-manager](claude/specialized-domains/risk-manager.md) | sonnet | Portfolio risk monitoring and management |

#### Marketing & Sales

| Agent | Model | Description |
|-------|-------|-------------|
| [content-marketer](claude/business/content-marketer.md) | sonnet | Blog posts, social media, email campaigns |
| [sales-automator](claude/business/sales-automator.md) | haiku | Cold emails, follow-ups, proposal generation |

#### Support & Legal

| Agent | Model | Description |
|-------|-------|-------------|
| [customer-support](claude/business/customer-support.md) | sonnet | Support tickets, FAQ responses, customer communication |
| [hr-pro](claude/business/hr-pro.md) | opus | HR operations, policies, employee relations |
| [legal-advisor](claude/business/legal-advisor.md) | opus | Privacy policies, terms of service, legal documentation |

### Specialized Domains

| Agent | Model | Description |
|-------|-------|-------------|
| [blockchain-developer](claude/specialized-domains/blockchain-developer.md) | sonnet | Web3 apps, smart contracts, DeFi protocols |
| [payment-integration](claude/specialized-domains/payment-integration.md) | sonnet | Payment processor integration (Stripe, PayPal) |
| [legacy-modernizer](claude/quality-security/legacy-modernizer.md) | sonnet | Legacy code refactoring and modernization |
| [context-manager](claude/research-analysis/context-manager.md) | haiku | Multi-agent context management |

### SEO & Content Optimization

| Agent | Model | Description |
|-------|-------|-------------|
| [seo-content-auditor](claude/seo/seo-content-auditor.md) | sonnet | Content quality analysis, E-E-A-T signals assessment |
| [seo-meta-optimizer](claude/seo/seo-meta-optimizer.md) | haiku | Meta title and description optimization |
| [seo-keyword-strategist](claude/seo/seo-keyword-strategist.md) | haiku | Keyword analysis and semantic variations |
| [seo-structure-architect](claude/seo/seo-structure-architect.md) | haiku | Content structure and schema markup |
| [seo-snippet-hunter](claude/seo/seo-snippet-hunter.md) | haiku | Featured snippet formatting |
| [seo-content-refresher](claude/seo/seo-content-refresher.md) | haiku | Content freshness analysis |
| [seo-cannibalization-detector](claude/seo/seo-cannibalization-detector.md) | haiku | Keyword overlap detection |
| [seo-authority-builder](claude/seo/seo-authority-builder.md) | sonnet | E-E-A-T signal analysis |
| [seo-content-writer](claude/seo/seo-content-writer.md) | sonnet | SEO-optimized content creation |
| [seo-content-planner](claude/seo/seo-content-planner.md) | haiku | Content planning and topic clusters |

## Model Configuration

Agents are assigned to specific Claude models based on task complexity and computational requirements. The system uses three model tiers:

### Model Distribution Summary

| Model | Agent Count | Use Case |
|-------|-------------|----------|
| Haiku | 12 | Quick, focused tasks with minimal computational overhead |
| Sonnet | 49 | Standard development and specialized engineering tasks |
| Opus | 29 | Complex reasoning, architecture, and critical analysis |

### Haiku Model Agents

| Category | Agents |
|----------|--------|
| Context & Reference | `context-manager`, `reference-builder`, `sales-automator`, `search-specialist` |
| SEO Optimization | `seo-meta-optimizer`, `seo-keyword-strategist`, `seo-structure-architect`, `seo-snippet-hunter`, `seo-content-refresher`, `seo-cannibalization-detector`, `seo-content-planner` |

### Sonnet Model Agents

| Category | Count | Agents |
|----------|-------|--------|
| Programming Languages | 18 | All language-specific agents (JavaScript, Python, Java, C++, etc.) |
| Frontend & UI | 5 | `frontend-developer`, `ui-ux-designer`, `ui-visual-validator`, `mobile-developer`, `ios-developer` |
| Infrastructure | 8 | `devops-troubleshooter`, `deployment-engineer`, `dx-optimizer`, `database-admin`, `network-engineer`, `flutter-expert`, `api-documenter`, `tutorial-engineer` |
| Quality & Testing | 4 | `test-automator`, `tdd-orchestrator`, `debugger`, `error-detective` |
| Business & Support | 6 | `business-analyst`, `risk-manager`, `content-marketer`, `customer-support`, `mermaid-expert`, `legacy-modernizer` |
| Data & Content | 5 | `data-engineer`, `payment-integration`, `seo-content-auditor`, `seo-authority-builder`, `seo-content-writer` |

### Opus Model Agents

| Category | Count | Agents |
|----------|-------|--------|
| Architecture & Design | 7 | `architect-reviewer`, `backend-architect`, `cloud-architect`, `hybrid-cloud-architect`, `kubernetes-architect`, `graphql-architect`, `terraform-specialist` |
| Critical Analysis | 6 | `code-reviewer`, `security-auditor`, `performance-engineer`, `observability-engineer`, `incident-responder`, `database-optimizer` |
| AI/ML Complex | 5 | `ai-engineer`, `ml-engineer`, `mlops-engineer`, `data-scientist`, `prompt-engineer` |
| Business Critical | 4 | `docs-architect`, `hr-pro`, `legal-advisor`, `quant-analyst` |
| Security Specialists | 4 | `backend-security-coder`, `frontend-security-coder`, `mobile-security-coder`, `sre-engineer` |

## OpenCode Agents

OpenCode agents are designed with open-source principles, privacy-first architectures, and transparency. All 94 Claude Code agents have been converted to OpenCode format and are available in the `opencode/` directory.

### Complete Agent Collection (97 total)

#### Development (18 agents)
All language-specific programming agents from Claude Code, including:
- Python, JavaScript, TypeScript, Go, Rust, Java, C++, C, C#
- Ruby, PHP, Elixir, Scala, Flutter, iOS development
- Django, FastAPI, and mobile development

#### Infrastructure (15 agents)
Comprehensive DevOps and cloud infrastructure agents:
- Cloud architects, Kubernetes engineers, Terraform specialists
- Database administrators, network engineers, deployment engineers
- Platform engineers, observability specialists
- **[self-hosting-specialist](opencode/infrastructure/self-hosting-specialist.md)** - Convert to self-hosted alternatives

#### Security (16 agents)
Advanced security and quality assurance agents:
- Security auditors, code reviewers, debuggers
- Frontend/backend/mobile security specialists
- Performance engineers, test automators
- **[privacy-first-architect](opencode/privacy-security/privacy-first-architect.md)** - Privacy-preserving systems

#### Specialized Domains (14 agents)
Domain-specific technical expertise:
- AI/ML engineers, blockchain developers, GraphQL architects
- Finance specialists (quant analysts, risk managers)
- Payment integration, developer experience optimization

#### Business & Marketing (17 agents)
Business operations and growth agents:
- Product managers, business analysts, HR professionals
- Content marketers, sales automators, customer support
- SEO specialists (10 dedicated SEO agents)

#### Documentation & Analysis (13 agents)
Technical writing and research agents:
- Documentation architects, API documenters, technical writers
- Data scientists, SQL specialists, search specialists
- UI/UX designers, tutorial engineers

#### Additional Categories
- **Gaming** (2 agents): Unity developer, Minecraft Bukkit specialist
- **Tools** (2 agents): Visual validators, diagram creators
- **Open Source** (1 agent): **[license-compliance-guardian](opencode/open-source/license-compliance-guardian.md)**

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
python scripts/lint_agents.py --roots opencode --fix-missing-model anthropic/claude-sonnet-4-20250514
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
docs-architect: Generate technical documentation
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
→ incident-responder → devops-troubleshooter → error-detective → performance-engineer
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
| System Architecture | `architect-reviewer` | Pattern validation, consistency analysis |

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
| Technical Docs | `docs-architect` | Comprehensive documentation generation |
| API Documentation | `api-documenter` | OpenAPI/Swagger specifications |
| Technical Writing | `technical-writer` | User guides, tutorials, documentation |
| Tutorial Creation | `tutorial-engineer` | Step-by-step educational content |
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