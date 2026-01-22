# Agent Model Migration Plan

## Overview

This document outlines the migration plan for 81 Claude Code agents from Anthropic Claude models to alternative providers, following Anthropic's decision to discontinue OpenCode access.

**Migration Date**: January 2026
**Total Agents**: 81
**Current Distribution**: 5 Haiku | 50 Sonnet | 26 Opus

---

## Recommended Model Mapping

### Tier Mapping Summary

| Current Model | Recommended Primary | Alternative 1 | Alternative 2 | Free Option |
|---------------|---------------------|---------------|---------------|-------------|
| **Opus** | `zai-coding-plan/glm-4.7` | `google/gemini-3-flash-preview` | `openai/gpt-5.2-codex` | - |
| **Sonnet** | `zai-coding-plan/glm-4.6` | `google/gemini-2.5-flash` | `opencode/grok-code` | `minimax-m2.1-free` |
| **Haiku** | `google/gemini-2.5-flash-lite` | `openai/gpt-5-nano` | `zai-coding-plan/glm-4.5-flash` | `opencode/glm-4.7-free` |

### Rationale

**Opus Replacement: `zai-coding-plan/glm-4.7`**
- 73.8% SWE-bench (competitive with Claude Sonnet 4.5)
- MIT licensed, open weights
- ~1/7th the cost of Claude
- Preserved thinking for multi-turn conversations
- 66.7% SWE-bench Multilingual (important for polyglot agents)

**Sonnet Replacement: `zai-coding-plan/glm-4.6`**
- 200K context window (vs Claude's 200K)
- Excellent Claude Code/Roo Code compatibility
- Tool use during inference
- Very cost-effective

**Haiku Replacement: `google/gemini-2.5-flash-lite`**
- 887 tokens/sec (fastest proprietary model)
- $0.10/$0.40 per 1M tokens (extremely cheap)
- Stable, GA release
- Thinking can be enabled when needed

---

## Complete Agent Migration Table

### OPUS AGENTS (26) → `zai-coding-plan/glm-4.7`

| # | Agent Name | Category | New Model | Notes |
|---|------------|----------|-----------|-------|
| 1 | `ai-engineer` | AI/ML | `zai-coding-plan/glm-4.7` | Complex LLM/RAG work |
| 2 | `architect-review` | Architecture | `zai-coding-plan/glm-4.7` | System design analysis |
| 3 | `backend-architect` | Architecture | `zai-coding-plan/glm-4.7` | API/microservices design |
| 4 | `backend-security-coder` | Security | `zai-coding-plan/glm-4.7` | Security-critical |
| 5 | `blockchain-developer` | Specialized | `zai-coding-plan/glm-4.7` | Complex smart contracts |
| 6 | `cloud-architect` | Infrastructure | `zai-coding-plan/glm-4.7` | Multi-cloud design |
| 7 | `code-reviewer` | Quality | `zai-coding-plan/glm-4.7` | Deep code analysis |
| 8 | `config-security-auditor` | Security | `zai-coding-plan/glm-4.7` | Security-critical |
| 9 | `data-engineer` | Data | `zai-coding-plan/glm-4.7` | Complex pipelines |
| 10 | `data-scientist` | Data | `zai-coding-plan/glm-4.7` | ML/statistical modeling |
| 11 | `database-optimizer` | Data | `zai-coding-plan/glm-4.7` | Performance-critical |
| 12 | `devops-troubleshooter` | DevOps | `zai-coding-plan/glm-4.7` | Complex debugging |
| 13 | `frontend-security-coder` | Security | `zai-coding-plan/glm-4.7` | Security-critical |
| 14 | `hybrid-cloud-architect` | Infrastructure | `zai-coding-plan/glm-4.7` | Multi-cloud complexity |
| 15 | `incident-responder` | DevOps | `zai-coding-plan/glm-4.7` | Time-critical decisions |
| 16 | `kubernetes-architect` | Infrastructure | `zai-coding-plan/glm-4.7` | Complex K8s design |
| 17 | `legal-advisor` | Business | `zai-coding-plan/glm-4.7` | Compliance precision |
| 18 | `ml-engineer` | AI/ML | `zai-coding-plan/glm-4.7` | Production ML systems |
| 19 | `mlops-engineer` | AI/ML | `zai-coding-plan/glm-4.7` | ML infrastructure |
| 20 | `mobile-security-coder` | Security | `zai-coding-plan/glm-4.7` | Security-critical |
| 21 | `observability-engineer` | DevOps | `zai-coding-plan/glm-4.7` | Complex monitoring |
| 22 | `performance-engineer` | Quality | `zai-coding-plan/glm-4.7` | Optimization analysis |
| 23 | `security-auditor` | Security | `zai-coding-plan/glm-4.7` | Security-critical |
| 24 | `sre-engineer` | DevOps | `zai-coding-plan/glm-4.7` | Reliability engineering |
| 25 | `tdd-orchestrator` | Quality | `zai-coding-plan/glm-4.7` | Complex test workflows |
| 26 | `terraform-specialist` | Infrastructure | `zai-coding-plan/glm-4.7` | IaC complexity |

---

### SONNET AGENTS (50) → `zai-coding-plan/glm-4.6`

| # | Agent Name | Category | New Model | Notes |
|---|------------|----------|-----------|-------|
| 1 | `api-documenter` | Documentation | `zai-coding-plan/glm-4.6` | OpenAPI/docs |
| 2 | `business-analyst` | Business | `zai-coding-plan/glm-4.6` | Analytics/KPIs |
| 3 | `c-pro` | Language | `zai-coding-plan/glm-4.6` | C programming |
| 4 | `content-marketer` | Business | `zai-coding-plan/glm-4.6` | Content creation |
| 5 | `context-manager` | AI/ML | `zai-coding-plan/glm-4.6` | Context engineering |
| 6 | `cpp-pro` | Language | `zai-coding-plan/glm-4.6` | C++ programming |
| 7 | `csharp-pro` | Language | `zai-coding-plan/glm-4.6` | C#/.NET |
| 8 | `customer-support` | Business | `zai-coding-plan/glm-4.6` | Support automation |
| 9 | `database-admin` | Data | `zai-coding-plan/glm-4.6` | DB operations |
| 10 | `debugger` | Quality | `zai-coding-plan/glm-4.6` | General debugging |
| 11 | `deployment-engineer` | DevOps | `zai-coding-plan/glm-4.6` | CI/CD pipelines |
| 12 | `django-pro` | Framework | `zai-coding-plan/glm-4.6` | Django/Python web |
| 13 | `documentation-expert` | Documentation | `zai-coding-plan/glm-4.6` | Technical docs |
| 14 | `dx-optimizer` | Quality | `zai-coding-plan/glm-4.6` | Developer experience |
| 15 | `elixir-pro` | Language | `zai-coding-plan/glm-4.6` | Elixir/OTP |
| 16 | `fastapi-pro` | Framework | `zai-coding-plan/glm-4.6` | FastAPI/async |
| 17 | `flutter-expert` | Mobile | `zai-coding-plan/glm-4.6` | Flutter/Dart |
| 18 | `frontend-developer` | Web | `zai-coding-plan/glm-4.6` | React/Next.js |
| 19 | `golang-pro` | Language | `zai-coding-plan/glm-4.6` | Go programming |
| 20 | `graphql-architect` | Architecture | `zai-coding-plan/glm-4.6` | GraphQL APIs |
| 21 | `hr-pro` | Business | `zai-coding-plan/glm-4.6` | HR operations |
| 22 | `ios-developer` | Mobile | `zai-coding-plan/glm-4.6` | Swift/iOS |
| 23 | `java-pro` | Language | `zai-coding-plan/glm-4.6` | Java/Spring |
| 24 | `javascript-pro` | Language | `zai-coding-plan/glm-4.6` | JavaScript/Node |
| 25 | `kubernetes-engineer` | Infrastructure | `zai-coding-plan/glm-4.6` | K8s operations |
| 26 | `legacy-modernizer` | Quality | `zai-coding-plan/glm-4.6` | Code migration |
| 27 | `mermaid-expert` | Documentation | `zai-coding-plan/glm-4.6` | Diagram creation |
| 28 | `minecraft-bukkit-pro` | Specialized | `zai-coding-plan/glm-4.6` | Bukkit plugins |
| 29 | `mobile-developer` | Mobile | `zai-coding-plan/glm-4.6` | Cross-platform |
| 30 | `network-engineer` | Infrastructure | `zai-coding-plan/glm-4.6` | Networking |
| 31 | `payment-integration` | Specialized | `zai-coding-plan/glm-4.6` | Stripe/payments |
| 32 | `php-pro` | Language | `zai-coding-plan/glm-4.6` | PHP/Laravel |
| 33 | `platform-engineer` | Infrastructure | `zai-coding-plan/glm-4.6` | Platform tooling |
| 34 | `product-manager` | Business | `zai-coding-plan/glm-4.6` | Product strategy |
| 35 | `prompt-engineer` | AI/ML | `zai-coding-plan/glm-4.6` | Prompt design |
| 36 | `python-pro` | Language | `zai-coding-plan/glm-4.6` | Python programming |
| 37 | `qa-engineer` | Quality | `zai-coding-plan/glm-4.6` | Test strategy |
| 38 | `quant-analyst` | Finance | `zai-coding-plan/glm-4.6` | Financial modeling |
| 39 | `reference-builder` | Documentation | `zai-coding-plan/glm-4.6` | API references |
| 40 | `risk-manager` | Finance | `zai-coding-plan/glm-4.6` | Risk analysis |
| 41 | `ruby-pro` | Language | `zai-coding-plan/glm-4.6` | Ruby/Rails |
| 42 | `rust-pro` | Language | `zai-coding-plan/glm-4.6` | Rust programming |
| 43 | `scala-pro` | Language | `zai-coding-plan/glm-4.6` | Scala/Spark |
| 44 | `sql-pro` | Data | `zai-coding-plan/glm-4.6` | SQL optimization |
| 45 | `supply-chain-security` | Security | `zai-coding-plan/glm-4.6` | Dependency security |
| 46 | `test-automator` | Quality | `zai-coding-plan/glm-4.6` | Test automation |
| 47 | `typescript-pro` | Language | `zai-coding-plan/glm-4.6` | TypeScript |
| 48 | `ui-ux-designer` | Design | `zai-coding-plan/glm-4.6` | UI/UX design |
| 49 | `ui-visual-validator` | Quality | `zai-coding-plan/glm-4.6` | Visual testing |
| 50 | `unity-developer` | Specialized | `zai-coding-plan/glm-4.6` | Unity/C# games |

---

### HAIKU AGENTS (5) → `google/gemini-2.5-flash-lite`

| # | Agent Name | Category | New Model | Notes |
|---|------------|----------|-----------|-------|
| 1 | `sales-automator` | Business | `google/gemini-2.5-flash-lite` | Email/outreach |
| 2 | `search-specialist` | Research | `google/gemini-2.5-flash-lite` | Web research |
| 3 | `seo-auditor` | Marketing | `google/gemini-2.5-flash-lite` | SEO analysis |
| 4 | `seo-content-creator` | Marketing | `google/gemini-2.5-flash-lite` | Content generation |
| 5 | `seo-optimizer` | Marketing | `google/gemini-2.5-flash-lite` | SEO optimization |

---

## Alternative Configurations

### Budget-Conscious Configuration
*Minimizes cost while maintaining quality*

| Tier | Model | Cost |
|------|-------|------|
| Premium (Opus) | `zai-coding-plan/glm-4.7` | ~1/7th Claude |
| Standard (Sonnet) | `minimax-m2.1-free` | FREE |
| Economy (Haiku) | `opencode/glm-4.7-free` | FREE |

### Performance-First Configuration
*Maximum capability, higher cost*

| Tier | Model | Strength |
|------|-------|----------|
| Premium (Opus) | `openai/gpt-5.2-codex` | 56.4% SWE-bench, top cybersecurity |
| Standard (Sonnet) | `google/gemini-3-flash-preview` | 78% SWE-bench |
| Economy (Haiku) | `google/gemini-2.5-flash-lite` | 887 tok/sec |

### Google-Only Configuration
*Single vendor simplicity*

| Tier | Model |
|------|-------|
| Premium (Opus) | `google/gemini-3-pro-preview` |
| Standard (Sonnet) | `google/gemini-3-flash-preview` |
| Economy (Haiku) | `google/gemini-2.5-flash-lite` |

### Z.ai-Only Configuration
*Best value, consistent API*

| Tier | Model |
|------|-------|
| Premium (Opus) | `zai-coding-plan/glm-4.7` |
| Standard (Sonnet) | `zai-coding-plan/glm-4.6` |
| Economy (Haiku) | `zai-coding-plan/glm-4.5-flash` |

---

## Migration Script

To update all agent files, use the following sed commands:

```bash
# Navigate to agents directory
cd /Users/bluby/personal-repos/agents/claude

# Update Opus agents to GLM-4.7
for agent in ai-engineer architect-review backend-architect backend-security-coder \
  blockchain-developer cloud-architect code-reviewer config-security-auditor \
  data-engineer data-scientist database-optimizer devops-troubleshooter \
  frontend-security-coder hybrid-cloud-architect incident-responder \
  kubernetes-architect legal-advisor ml-engineer mlops-engineer \
  mobile-security-coder observability-engineer performance-engineer \
  security-auditor sre-engineer tdd-orchestrator terraform-specialist; do
  sed -i '' 's/model: opus/model: zai-coding-plan\/glm-4.7/' "${agent}.md"
done

# Update Sonnet agents to GLM-4.6
for agent in api-documenter business-analyst c-pro content-marketer context-manager \
  cpp-pro csharp-pro customer-support database-admin debugger deployment-engineer \
  django-pro documentation-expert dx-optimizer elixir-pro fastapi-pro flutter-expert \
  frontend-developer golang-pro graphql-architect hr-pro ios-developer java-pro \
  javascript-pro kubernetes-engineer legacy-modernizer mermaid-expert \
  minecraft-bukkit-pro mobile-developer network-engineer payment-integration php-pro \
  platform-engineer product-manager prompt-engineer python-pro qa-engineer \
  quant-analyst reference-builder risk-manager ruby-pro rust-pro scala-pro sql-pro \
  supply-chain-security test-automator typescript-pro ui-ux-designer \
  ui-visual-validator unity-developer; do
  sed -i '' 's/model: sonnet/model: zai-coding-plan\/glm-4.6/' "${agent}.md"
done

# Update Haiku agents to Gemini 2.5 Flash Lite
for agent in sales-automator search-specialist seo-auditor seo-content-creator \
  seo-optimizer; do
  sed -i '' 's/model: haiku/model: google\/gemini-2.5-flash-lite/' "${agent}.md"
done
```

---

## Validation Checklist

After migration, verify:

- [ ] All 81 agent files updated
- [ ] No remaining references to `haiku`, `sonnet`, or `opus`
- [ ] Test each tier with a sample prompt
- [ ] Verify API keys configured for new providers
- [ ] Update any CI/CD pipelines referencing old models
- [ ] Update documentation and README

---

## Cost Comparison (Estimated Monthly)

| Configuration | Opus Tasks (1M tok) | Sonnet Tasks (5M tok) | Haiku Tasks (10M tok) | Total |
|---------------|--------------------|-----------------------|-----------------------|-------|
| **Claude (Old)** | ~$75 | ~$75 | ~$5 | ~$155 |
| **Recommended (Z.ai + Google)** | ~$11 | ~$15 | ~$5 | ~$31 |
| **Budget (Free models)** | ~$11 | $0 | $0 | ~$11 |
| **Performance (OpenAI + Google)** | ~$55 | ~$18 | ~$5 | ~$78 |

*Estimated based on typical agent usage patterns*

---

## Rollback Plan

If issues arise, revert to original models:

```bash
cd /Users/bluby/personal-repos/agents/claude
git checkout -- *.md
```

---

## Next Steps

1. **Review** this migration plan
2. **Select** preferred configuration (recommended: Z.ai primary)
3. **Configure** API keys for chosen providers
4. **Run** migration script
5. **Test** agents across all tiers
6. **Monitor** performance and adjust as needed

---

*Document generated: January 2026*
*Last updated: Based on model benchmarks as of December 2025*
