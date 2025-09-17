# Technical Writer Agent Instructions for Agent Enhancement Project

## Project Overview
Enhance all existing agents in this repository to match the comprehensive format used by wshobson's agents. This will improve agent discoverability, clarity, and effectiveness.

## Resources
- **Template**: `agent-format-template.md` - Complete format specification
- **Example**: `enhanced-example-security-auditor.md` - Fully enhanced agent showing all sections
- **Reference**: `/tmp/wshobson-agents/` - Original examples for inspiration (especially `backend-security-coder.md`, `tdd-orchestrator.md`)

## Enhancement Requirements

### Mandatory Sections to Add/Expand

1. **Purpose Section** (REQUIRED for all agents)
   - Write 3-4 sentences describing core expertise
   - Include unique value proposition
   - Mention primary use cases
   - Keep it comprehensive but concise

2. **Capabilities Section** (REQUIRED for all agents)
   - Organize into 3-5 logical categories
   - Each category should have 4-6 specific capabilities
   - Use bullet points with bold capability names
   - Include specific tools, frameworks, and version numbers
   - Be technically detailed and accurate

3. **Behavioral Traits** (REQUIRED for all agents)
   - Add 5 standard traits minimum:
     - Communication style
     - Problem-solving approach
     - Code style preference (for coding agents)
     - Documentation philosophy
     - Testing mindset (for development agents)

4. **Knowledge Base** (REQUIRED for all agents)
   - List specific technologies with versions
   - Include industry standards followed
   - Mention tool proficiency
   - Be specific about frameworks and libraries

### Conditional Sections

5. **When to Use vs [Other Agent]** (ADD only when confusion possible)
   - Required for: security-auditor (vs backend-security-coder), python-pro (vs data-scientist)
   - Include clear use case differentiation
   - Add one-line key difference statement

6. **Integration with Other Agents** (ADD for agents that work in workflows)
   - Specify which agents pair well together
   - Define handoff points
   - Note validation relationships

### Keep Existing Content
- Maintain all current technical content
- Preserve existing tags and model selections
- Keep the "Use PROACTIVELY" pattern in descriptions

## Priority Order for Enhancement

### Phase 1 - High Priority (Most Used)
1. `languages/python-pro.md`
2. `languages/javascript-pro.md`
3. `languages/typescript-pro.md`
4. `quality-security/code-reviewer.md`
5. `quality-security/security-auditor.md`
6. `infrastructure/deployment-engineer.md`
7. `quality-security/debugger.md`

### Phase 2 - Critical Agents (Complex/Important)
8. `specialized-domains/ai-engineer.md`
9. `specialized-domains/ml-engineer.md`
10. `infrastructure/kubernetes-engineer.md`
11. `infrastructure/database-optimizer.md`
12. `specialized-domains/payment-integration.md`
13. `quality-security/test-automator.md`
14. `infrastructure/cloud-architect.md`

### Phase 3 - Specialized Agents
15. All remaining language agents (`golang-pro`, `rust-pro`, `java-pro`, etc.)
16. All infrastructure agents
17. All SEO agents (keep concise but add Purpose)
18. All business agents

### Phase 4 - Simple Agents (Can remain concise)
19. `quality-security/error-detective.md`
20. `research-analysis/search-specialist.md`
21. Simple utility agents

## Quality Checklist for Each Enhancement

Before considering an agent complete, verify:

- [ ] **Purpose section** is exactly 3-4 sentences
- [ ] **Capabilities** has 3-5 categories with 4-6 items each
- [ ] **Capabilities** include specific version numbers where applicable
- [ ] **Approach** section has 5-7 numbered principles
- [ ] **Behavioral Traits** has all 5 standard traits
- [ ] **Output Formats** lists 5+ specific deliverables
- [ ] **Knowledge Base** includes tools, standards, and frameworks
- [ ] **Example Scenarios** has 3-5 concrete examples
- [ ] No grammar or spelling errors
- [ ] Consistent formatting with template
- [ ] Technical accuracy verified
- [ ] Tags are comprehensive and accurate

## Writing Style Guidelines

### Do's
- ✅ Use active voice and action-oriented language
- ✅ Be specific about tools and versions (e.g., "Python 3.9+", "React 18")
- ✅ Include concrete examples rather than abstract descriptions
- ✅ Use consistent bullet point formatting
- ✅ Maintain professional, technical tone
- ✅ Group related items logically

### Don'ts
- ❌ Don't use vague terms like "various tools" - be specific
- ❌ Don't write generic descriptions - make each agent unique
- ❌ Don't exceed recommended section lengths
- ❌ Don't remove existing technical content
- ❌ Don't change model or tags without justification

## Example Enhancement Process

Taking `languages/python-pro.md` from current to enhanced:

1. **Read current content** - Understand existing capabilities
2. **Add Purpose** - Write comprehensive 3-4 sentence overview
3. **Expand Capabilities** - Current "Focus Areas" → Detailed categories with specifics
4. **Add Behavioral Traits** - Define the agent's personality and approach
5. **Create Knowledge Base** - List Python versions, frameworks, tools
6. **Add Examples** - 3-5 concrete scenarios the agent handles
7. **Review and Polish** - Check against quality checklist

## Validation Steps

After enhancing each agent:
1. Verify YAML frontmatter is valid
2. Check that description still includes "Use PROACTIVELY" where appropriate
3. Ensure model selection (haiku/sonnet/opus) matches complexity
4. Confirm tags are comprehensive
5. Test readability and technical accuracy

## Special Notes

### For Security Agents
- Include specific vulnerability types
- Mention compliance frameworks
- List security tools and scanners
- Add attack vectors and defense strategies

### For Language Agents
- Include language version specifics
- List major frameworks and libraries
- Mention testing frameworks
- Add package managers and build tools

### For Infrastructure Agents
- Include cloud provider specifics (AWS/Azure/GCP)
- List orchestration tools
- Mention monitoring and observability tools
- Add IaC frameworks

## Success Metrics
- Each enhanced agent should be 150-300 lines (vs current 30-100)
- Clear differentiation between similar agents
- Comprehensive capability coverage
- Improved discoverability through detailed content
- Consistent format across all agents

## Questions to Answer for Each Agent
1. What makes this agent unique?
2. What specific problems does it solve?
3. What tools/frameworks does it master?
4. How does it approach problems?
5. What does it output/deliver?
6. When should someone use this vs similar agents?

## Start with Phase 1
Begin with the high-priority agents listed in Phase 1, using the template and example provided. Each enhancement should take approximately 30-45 minutes to complete thoroughly.