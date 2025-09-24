# TODO: Recommended New Agents

This document outlines gaps in the current agent collection and suggests new agents to improve software development outcomes.

## Critical Priority (Immediate Impact)

## High Priority (Significant Gaps)

## Medium Priority (Important for Completeness)

### 7. GitOps Engineer Agent 🔄
**File**: `gitops-engineer.md`
```yaml
name: gitops-engineer
description: Implement GitOps workflows, manage ArgoCD/Flux configurations, and maintain declarative infrastructure management.
model: sonnet
```
**Gap**: Missing declarative infrastructure and GitOps practices  
**Use case**: Infrastructure drift prevention, automated deployments

### 8. Event Architect Agent 📡
**File**: `event-architect.md`
```yaml
name: event-architect
description: Design event-driven architectures, implement event sourcing, CQRS patterns, and message streaming systems.
model: sonnet
```
**Gap**: Missing event-driven architecture expertise  
**Use case**: Scalable, decoupled system design

### 9. Chaos Engineer Agent 💥
**File**: `chaos-engineer.md`
```yaml
name: chaos-engineer
description: Design fault injection experiments, validate system resilience, and implement chaos engineering practices.
model: sonnet
```
**Gap**: No resilience testing or fault injection capabilities  
**Use case**: System reliability validation under failure conditions

### 10. Analytics Engineer Agent 📈
**File**: `analytics-engineer.md`
```yaml
name: analytics-engineer
description: Implement event tracking, design data pipelines for analytics, and create metrics frameworks for product insights.
model: sonnet
```
**Gap**: Missing analytics implementation and metrics design  
**Use case**: Data-driven product decisions, user behavior analysis

## Lower Priority (Specialized Needs)

### 11. Compliance Officer Agent 📋
**File**: `compliance-officer.md`
- GDPR, SOC2, HIPAA compliance
- Audit preparation and privacy engineering
- Model: `sonnet`

### 12. Accessibility Tester Agent ♿
**File**: `accessibility-tester.md`
- WCAG compliance and assistive technology testing
- Inclusive design practices
- Model: `sonnet`

### 13. Release Manager Agent 🚀
**File**: `release-manager.md`
- Release planning and feature flagging
- Canary deployments and rollback strategies
- Model: `sonnet`

### 14. Container Security Agent 🔐
**File**: `container-security.md`
- Container image scanning and runtime security
- Admission controllers and security policies
- Model: `sonnet`

### 15. Micro-frontend Architect Agent 🏛️
**File**: `microfrontend-architect.md`
- Module federation and micro-frontend orchestration
- Shared design systems across teams
- Model: `sonnet`

## Implementation Strategy

### Phase 1 (Critical - Weeks 1-2)
- [x] Product Manager Agent
- [x] Observability Engineer Agent
- [x] SRE Agent

### Phase 2 (High Priority - Weeks 3-4)
- [x] Platform Engineer Agent
- [x] QA Engineer Agent
- [x] Kubernetes Engineer Agent

### Phase 3 (Medium Priority - Weeks 5-8)
- [ ] GitOps Engineer Agent
- [ ] Event Architect Agent
- [ ] Chaos Engineer Agent
- [ ] Analytics Engineer Agent

### Phase 4 (Specialized - As needed)
- [ ] Compliance Officer Agent
- [ ] Accessibility Tester Agent
- [ ] Release Manager Agent
- [ ] Container Security Agent
- [ ] Micro-frontend Architect Agent

## Success Metrics

**Developer Experience**:
- Reduced onboarding time from days to hours
- Faster feature delivery with fewer production issues
- Improved code quality and system reliability

**System Reliability**:
- Higher uptime (99.9% → 99.99%)
- Faster incident resolution
- Proactive issue prevention

**Product Quality**:
- Better feature-market fit
- Reduced support tickets
- Improved user satisfaction

## Current Collection Strengths

✅ **Well Covered**:
- Language specialists (13 agents)
- Infrastructure automation
- Security and performance analysis
- Documentation and API design

❌ **Gaps Being Addressed**:
- Product management integration
- Modern observability practices
- Platform engineering capabilities
- Comprehensive quality assurance
- Reliability engineering

---

## Repository Improvement Initiatives 🚀

### Phase 5 (Infrastructure & Tooling)

#### Agent Discovery and Navigation 📚
- [ ] **Agent Index/Catalog**: Create interactive agent catalog with capabilities, models, and use cases
- [X] **Tag System**: Add tags to agent YAML headers for better searchability (`tags: [security, infrastructure, testing]`)
- [X] **Agent Dependency Map**: Visual diagram showing agent workflow relationships and combinations

#### Quality and Consistency 🔧
- [ ] **Agent Linting**: Validation scripts ensuring format consistency and quality standards
- [ ] **Template Generator**: CLI tool to scaffold new agents with proper structure
- [ ] **Agent Testing Framework**: Automated tests for YAML syntax and description clarity

#### Enhanced Metadata 📊
- [ ] **Usage Analytics**: Track agent usage patterns to guide improvements
- [ ] **Agent Versioning**: Version control with changelogs for agent updatecds
- [ ] **Compatibility Matrix**: Document which agents work together and interaction patterns

### Phase 6 (Documentation & Integration)

#### Documentation Improvements 📝
- [ ] **Agent Orchestration Guide**: Document common workflows and agent chains
- [ ] **Migration Guide**: Help transition from manual processes to agent-driven workflows
- [ ] **Best Practices**: Guidelines for optimal agent selection and combination

#### Integration Enhancements 🔗
- [ ] **Claude Code Integration**: Enhanced workflow management integration
- [ ] **IDE Plugins**: VSCode/IntelliJ extensions for easy agent invocation
- [ ] **Webhook Support**: Allow agents to trigger external systems

#### Advanced Agent Features 🚀
- [ ] **Agent Chaining**: Define explicit workflows where agents pass context
- [ ] **Context Sharing**: Mechanisms for cross-session agent context
- [ ] **Agent Specialization**: Framework-specific sub-agents (React, Vue under frontend-developer)

### Phase 7 (Community & Performance)

#### Community and Collaboration 👥
- [ ] **Agent Marketplace**: Community contribution system with review process
- [ ] **Agent Reviews**: Peer review system for quality and effectiveness
- [ ] **Usage Examples**: Real-world problem-solving examples

#### Performance and Optimization ⚡
- [ ] **Model Assignment Optimizer**: AI-driven model assignment based on complexity
- [ ] **Cost Tracking**: Monitor and optimize model usage costs
- [ ] **Agent Performance Metrics**: Measure effectiveness and success rates

#### Security and Governance 🔒
- [ ] **Agent Security Scanning**: Validate agents for harmful instructions
- [ ] **Permission System**: Control agent access to tools and systems
- [ ] **Audit Trail**: Track agent usage and modifications

### Phase 8 (Specialized Domains)

#### Emerging Technology Agents 🎯
- [ ] **AI/ML Operations Agent**: MLOps, model deployment, A/B testing for ML
- [ ] **Edge Computing Agent**: IoT deployment, edge optimization patterns
- [ ] **Blockchain/Web3 Agent**: Smart contracts, DeFi, tokenomics
- [ ] **Gaming Development Agent**: Game engines, multiplayer architecture, performance optimization
- [ ] **Healthcare Tech Agent**: HIPAA compliance, medical device software, clinical workflows

#### Industry-Specific Agents 🏭
- [ ] **FinTech Specialist**: PCI compliance, trading systems, regulatory reporting
- [ ] **EdTech Developer**: LMS integration, accessibility, student privacy
- [ ] **E-commerce Expert**: Payment processing, inventory management, personalization
- [ ] **Media/Content Agent**: CDN optimization, streaming, content management

## Implementation Roadmap

### Quarter 1: Foundation
**Focus**: Core infrastructure and quality improvements
- Agent linting and testing framework
- Enhanced documentation
- Usage analytics implementation

### Quarter 2: Integration
**Focus**: Better tooling and developer experience  
- IDE plugins and CLI tools
- Agent orchestration capabilities
- Performance optimization

### Quarter 3: Community
**Focus**: Collaboration and governance
- Marketplace and review system
- Security and audit frameworks
- Advanced agent features

### Quarter 4: Specialization
**Focus**: Domain-specific expertise
- Industry-specific agents
- Emerging technology coverage
- Advanced workflow patterns

---

*This TODO represents the evolution from a code-focused agent collection to a comprehensive, community-driven software development lifecycle ecosystem.*

## Implemented

### 1. Product Manager Agent 🎯
**File**: `product-manager.md`
```yaml
name: product-manager
description: Prioritize features, create user stories, manage product roadmaps, and align stakeholder requirements. Use PROACTIVELY for feature planning and business-technical alignment.
model: opus
```
**Why needed**: Bridges business and technical teams, prevents building wrong features  
**Impact**: +40% development efficiency, better feature-market fit  
**Responsibilities**:
- Feature prioritization and roadmap planning
- User story creation and acceptance criteria
- Stakeholder alignment and requirements gathering
- Product metrics and KPI definition
- Competitive analysis and market research

### 2. Observability Engineer Agent 📊
**File**: `observability-engineer.md`
```yaml
name: observability-engineer
description: Implement distributed tracing, metrics, logging strategies, and APM solutions. Use PROACTIVELY for system monitoring, debugging, and performance analysis.
model: opus
```
**Why needed**: Critical for production system health and debugging  
**Impact**: -60% MTTR, prevents outages, improves system visibility  
**Responsibilities**:
- OpenTelemetry implementation and configuration
- Metrics dashboard creation (Grafana, DataDog)
- Distributed tracing setup and analysis
- Log aggregation and structured logging
- Alert configuration and SLI monitoring

### 3. Site Reliability Engineer (SRE) Agent 🛡️
**File**: `sre-engineer.md`
```yaml
name: sre-engineer
description: Define SLIs/SLOs, implement reliability practices, manage error budgets, and balance feature velocity with stability. Use PROACTIVELY for system reliability.
model: opus
```
**Why needed**: Ensures system reliability and uptime management  
**Impact**: 99.9% → 99.99% reliability, structured incident response  
**Responsibilities**:
- SLI/SLO definition and monitoring
- Error budget management and policies
- Incident response and post-mortem analysis
- Reliability engineering practices
- Capacity planning and performance testing

### 4. Platform Engineer Agent 🏗️
**File**: `platform-engineer.md`
```yaml
name: platform-engineer
description: Build internal developer platforms, configure service mesh, create developer tooling, and standardize deployment patterns. Use for developer experience optimization.
model: sonnet
```
**Why needed**: Reduces developer friction and standardizes practices  
**Impact**: -70% onboarding time, consistent deployment patterns  
**Responsibilities**:
- Internal Developer Platform (IDP) design
- Service mesh configuration (Istio, Linkerd)
- Developer tooling and automation
- Self-service infrastructure provisioning
- Golden path templates and standards

### 5. QA Engineer Agent ✅
**File**: `qa-engineer.md`
```yaml
name: qa-engineer
description: Design manual testing strategies, coordinate user acceptance testing, create comprehensive test plans, and ensure quality beyond automation.
model: sonnet
```
**Why needed**: Quality assurance beyond automated testing  
**Impact**: +30% bug detection before production, better UX  
**Responsibilities**:
- Manual testing strategy and execution
- User Acceptance Testing (UAT) coordination
- Exploratory testing and edge case discovery
- Test plan creation and test case design
- Quality metrics and reporting

### 6. Kubernetes Engineer Agent ☸️
**File**: `kubernetes-engineer.md`
```yaml
name: kubernetes-engineer
description: Advanced Kubernetes configurations, operator development, cluster management, and container orchestration patterns. Use for complex K8s implementations.
model: sonnet
```
**Why needed**: Container orchestration expertise for modern apps  
**Impact**: -25% infrastructure costs, improved scalability  
**Responsibilities**:
- Advanced Kubernetes patterns and best practices
- Custom Resource Definitions (CRDs) and operators
- Cluster management and node optimization
- Networking and security policies
- Multi-cluster and hybrid cloud setups

## Pending Model Policy & Linter Status (2025-09-24)

### Context
Recent enhancement added dual-schema linter (`scripts/lint_agents.py`) supporting OpenCode and legacy Claude agent formats with auto schema detection and deprecated key control.

### Current State
- Dual-schema feature committed: `feat(linter): add dual-schema support (auto/opencode/claude) with deprecated Claude key flag`.
- CHANGELOG updated under Unreleased (dual-schema entry).
- Linter enforces: required OpenCode keys (description, mode, temperature, tools), tool mapping validity, temperature range, mode values, deprecated key presence (OpenCode always; Claude unless `--allow-deprecated-claude`).
- Linter does NOT yet validate model identifier syntax; only presence when `--require-model` or `--fix-missing-model` used.

### Discovered Issue
- `opencode/business/product-manager.md` uses non-canonical model value: `model: Claude Sonnet 3.7`.
- Runtime raised `ProviderModelNotFoundError` due to unrecognized free-form label.
- Other agents use canonical slugs: `claude-3-5-sonnet-20241022`, `claude-3-opus-20240229`, `claude-3-haiku-20240307`, or new prefixed forms `anthropic/claude-sonnet-4-20250514`, `anthropic/claude-opus-4-20250514`.

### Impact
- Agents with non-canonical model strings fail to initialize.
- Inconsistent naming blocks bulk migration or automated routing logic.

### Decision Needed (Ticket Filed with OpenCode)
1. Canonical model namespace: continue `claude-3-*` vs. migrate to `anthropic/claude-*-4-*`.
2. Acceptable backward-compatible mapping list (e.g., friendly names → canonical IDs).
3. Policy for mixed versions (allow both 3.x and 4.x simultaneously or enforce one family per repo pass).

### Proposed Linter Extension (Deferred Until Decision)
- Add `--validate-model` flag (or always-on once policy fixed).
- Implement allowlist/regex patterns:
  - `^claude-3-(opus|haiku|[0-9]-?sonnet)[-0-9]*$`
  - `^anthropic/claude-(opus|sonnet)-4-\d{8}$`
- Friendly-name mapping (prior to validation):
  - "Claude Sonnet 3.7" → `claude-3-5-sonnet-20241022` (or chosen canonical substitute)
  - "Claude Sonnet 4" / "Sonnet 4" → `anthropic/claude-sonnet-4-YYYYMMDD`
- Warn (not fail) on deprecated legacy form if migration period defined.

### Deferred Actions
- [ ] Normalize `product-manager.md` model once policy resolves.
- [ ] Bulk replace any remaining friendly names (audit via `grep -R "model: .*Sonnet"`).
- [ ] Add model validation + mapping table to `scripts/lint_agents.py`.
- [ ] Document model policy in `OPENCODE.md` and template.
- [ ] Update `opencode/agent-template.md` (currently missing required keys) once model policy finalized.

### Resume Checklist
1. Retrieve ticket resolution (model naming convention).
2. Implement model regex + optional mapping (`--auto-fix-model-names`).
3. Run linter with new flag across repo; capture violations.
4. Commit normalization (one commit) + doc update (second commit).
5. Close ticket referencing commit hashes.

### Notes
- No uncommitted changes at pause point (working tree clean after dual-schema commit).
- Adding model validation before policy decision risks churn; waiting is intentional.

---

### Pending Copilot Model Format & Tasks (Awaiting Ticket Resolution)

#### Unknowns (Need Ticket Answer)
- Canonical provider namespace for Copilot models (e.g., `copilot/`, `github/copilot-`, or reuse `anthropic/` prefix?)
- Versioning scheme (date stamped `YYYYMMDD`, semantic `vX`, or rolling `latest` alias)
- Tier naming (e.g., `copilot-basic`, `copilot-pro`, `copilot-enterprise`, or alignment with existing `haiku/sonnet/opus` tiers)
- Tool permission defaults (do Copilot models restrict certain tools requiring conditional logic?)
- Performance vs. cost guidance to inform automatic tier selection heuristics

#### Design Goals
- Non-breaking introduction: legacy Claude 3 / 3.5 / 4 agents remain valid
- Configurable model families (avoid hardcoding Copilot regex directly in code where possible)
- Deterministic auto-fix mappings for obvious aliases (e.g., `Copilot Sonnet` → canonical slug once defined)
- Clear separation: validation layer vs. normalization layer vs. recommendation layer

#### Proposed Linter Enhancements (Deferred)
1. Externalized Model Family Spec
   - Add optional JSON/YAML config (e.g., `model_families.json`) loaded if present
   - Schema example:
     ```json
     {
       "families": [
         {"name": "claude-3", "regex": "^claude-3-(haiku|opus|5-sonnet)-\\d{8}$", "deprecated": false},
         {"name": "claude-4", "regex": "^anthropic/claude-(opus|sonnet)-4-\\d{8}$", "deprecated": false},
         {"name": "copilot", "regex": "<TBD_FROM_TICKET>", "deprecated": false}
       ],
       "mappings": {
         "Claude Sonnet 3.7": "claude-3-5-sonnet-20241022",
         "Claude Sonnet 4": "anthropic/claude-sonnet-4-20250514",
         "Copilot Sonnet": "<TBD_RESOLUTION>"
       }
     }
     ```
   - If config absent, fall back to in-code defaults (current behavior)
2. Pluggable Validation
   - Refactor validation into strategy object: `ModelValidator` applying (a) syntax check, (b) mapping, (c) policy warnings
3. Recommendation Engine (Optional Phase 2)
   - Suggest lower-cost model if temperature < threshold & tool list simple
4. Reporting Levels
   - errors: malformed/unresolvable
   - warnings: deprecated families
   - info: auto-fixes applied
5. Flags
   - `--validate-model` (activate validation layer)
   - `--auto-fix-model` (apply mappings; otherwise only suggest)
   - `--model-config PATH` (override default detection)
   - `--allow-unknown-model` (downgrade unknown family → warning)

#### Copilot-Specific Placeholder Tasks
- [ ] Capture ticket answer with exact canonical Copilot slug patterns
- [ ] Add Copilot family regex to config & code fallback
- [ ] Extend mapping table with any friendly / alias forms reported in the wild
- [ ] Implement dry-run report: `--validate-model --report=json` output for tooling consumption
- [ ] Add README/AGENTS.md bullet documenting Copilot model usage policy
- [ ] Update agent template with example Copilot model (commented) once stable
- [ ] (Optional) Add heuristic recommending Copilot vs Claude based on task category tags

#### Risk Mitigation
- Ship validation behind flag until Copilot policy stable
- Provide escape hatch (`--allow-unknown-model`) to prevent CI blockage on early adoption
- Log remediation suggestions without modifying files unless `--auto-fix-model`

#### Post-Decision Execution Order
1. Insert Copilot spec into config (or code) + mappings
2. Implement validator refactor + flags
3. Run full-repo dry run; archive JSON report for ticket closure
4. Normalize anomalies (single commit)
5. Add documentation (second commit)
6. Enable validation in CI (optional third commit) once green

---
