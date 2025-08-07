# TODO: Recommended New Agents

This document outlines gaps in the current agent collection and suggests new agents to improve software development outcomes.

## Critical Priority (Immediate Impact)

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

## High Priority (Significant Gaps)

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
- [ ] Product Manager Agent
- [ ] Observability Engineer Agent
- [ ] SRE Agent

### Phase 2 (High Priority - Weeks 3-4)
- [ ] Platform Engineer Agent
- [ ] QA Engineer Agent
- [ ] Kubernetes Engineer Agent

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

*This TODO represents the evolution from a code-focused agent collection to a comprehensive software development lifecycle toolkit.*