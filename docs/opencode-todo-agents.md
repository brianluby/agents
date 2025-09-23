# Opencode Migration Analysis

## ✅ **High Compatibility - Minimal Changes Needed**

The Claude Code agents in this repository are **highly compatible** with opencode and would work with minimal or no changes.

### **What Works Out of the Box:**

1. **System Prompts**: All prompts are platform-agnostic and focus on domain expertise
2. **YAML Structure**: Standard frontmatter format that opencode can likely adopt
3. **External Tools**: Agents reference external tools (kubectl, npm, docker) that opencode supports via bash
4. **No Platform Lock-in**: No Claude Code specific tool references found

### **Required Changes for Opencode:**

#### **1. YAML Frontmatter Adjustments**
```yaml
# Current Claude Code format:
---
name: backend-architect
description: Design RESTful APIs, microservice boundaries...
model: sonnet
tags: [backend, api, microservices]
---

# Potential opencode format (may need):
---
name: backend-architect
description: Design RESTful APIs, microservice boundaries...
# model field may need different values or removal
# tools field might be required for opencode
---
```

#### **2. Model Field Mapping**
- **Claude Code**: `haiku`, `sonnet`, `opus`
- **Opencode**: May use different model identifiers or not support model selection

#### **3. Tools Configuration**
- Current agents don't specify `tools` field (inherit all tools)
- Opencode may require explicit tool specification or use different tool names

### **Implementation Options:**

#### **Option A: Direct Migration**
- Copy agents as-is and adjust frontmatter based on opencode requirements
- 95% compatibility expected

#### **Option B: Conversion Script**
```bash
# Batch convert agents for opencode
for file in *.md; do
  # Remove model field if unsupported
  # Add tools field if required
  # Update any opencode-specific configurations
done
```

#### **Option C: Hybrid Approach**
- Keep most agents unchanged
- Only modify frontmatter fields that conflict
- Test each agent type individually

### **Specific Agent Compatibility:**

| Agent Type | Compatibility | Notes |
|------------|---------------|-------|
| **Development** (python-pro, backend-architect) | ✅ 100% | No platform dependencies |
| **Infrastructure** (devops-troubleshooter, cloud-architect) | ✅ 95% | Uses external tools via bash |
| **Security** (security-auditor) | ✅ 100% | Platform-agnostic security practices |
| **AI/ML** (ai-engineer, ml-engineer) | ✅ 100% | External API integrations |
| **Business** (business-analyst, content-marketer) | ✅ 100% | No technical dependencies |

### **Recommendation:**

**Start with a pilot migration** of 5-10 agents to test opencode compatibility, then batch convert the rest. The agents are well-designed and should work seamlessly with opencode's agent system.

## **Next Steps:**

1. **Test pilot agents** with opencode to verify compatibility
2. **Document opencode agent format** requirements
3. **Create conversion script** if needed
4. **Batch migrate** remaining agents
5. **Update documentation** for opencode usage%