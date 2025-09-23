# Codex (OpenAI) Agent Usage Instructions

## Overview
Codex uses a simplified, universal format called AGENTS.md - a single Markdown file containing natural language instructions for guiding the AI assistant. Think of it as a README for agents.

## Installation & Setup

### Creating AGENTS.md from This Repository

Since Codex expects a single AGENTS.md file rather than individual agent files, you'll need to compile the agents into one consolidated document:

```bash
# Option 1: Create a comprehensive AGENTS.md with all agents
cat > AGENTS.md << 'EOF'
# Project Agents and Conventions

This file contains specialized agent instructions for different development tasks.
Codex should use these guidelines based on the current context and task.

## Available Specialized Agents

### Python Development (python-pro)
When working with Python code:
- Use advanced features like decorators, generators, and async/await appropriately
- Follow PEP 8 and Python idioms
- Optimize performance using profiling insights
- Implement comprehensive testing with pytest
- Use type hints and static analysis tools (mypy, ruff)
- Prefer composition over inheritance
- Handle exceptions gracefully with context managers

### JavaScript/TypeScript Development (javascript-pro, typescript-pro)
When working with JavaScript or TypeScript:
- Use modern ES6+ features and async patterns
- Implement proper error handling with try-catch and promises
- Follow TypeScript best practices with strict type safety
- Optimize for both browser and Node.js environments
- Use appropriate design patterns for the framework (React, Vue, etc.)

### FastAPI Development (fastapi-pro)
When building APIs with FastAPI:
- Build high-performance async-first APIs with FastAPI 0.100+
- Use Pydantic V2 for data validation and automatic OpenAPI documentation
- Implement async SQLAlchemy 2.0 with proper connection pooling
- Design RESTful APIs with proper versioning and rate limiting
- Add OAuth2/JWT authentication with role-based access control
- Implement WebSockets for real-time communication
- Use background tasks and message queues for async processing
- Apply microservices patterns: circuit breakers, event-driven architecture
- Write comprehensive async tests with pytest-asyncio and TestClient
- Monitor with structured logging, OpenTelemetry tracing, and health endpoints

### Infrastructure & DevOps (devops-troubleshooter, kubernetes-engineer)
For infrastructure tasks:
- Debug production issues with urgency and precision
- Implement proper monitoring and observability
- Use Infrastructure as Code with Terraform
- Configure CI/CD pipelines properly
- Handle container orchestration with Kubernetes best practices
- Implement proper secret management

### Code Review & Quality (code-reviewer, security-auditor)
When reviewing or auditing code:
- Check for security vulnerabilities (OWASP Top 10)
- Ensure proper error handling and input validation
- Verify test coverage and edge cases
- Review for performance bottlenecks
- Check for code smells and technical debt
- Validate authentication and authorization implementations

### Database Operations (database-optimizer, sql-pro)
For database-related tasks:
- Optimize queries using explain plans
- Design normalized schemas with proper indexing
- Implement efficient data access patterns
- Handle migrations safely
- Use transactions appropriately
- Implement caching strategies where beneficial

### AI/ML Engineering (ai-engineer, ml-engineer)
For machine learning tasks:
- Implement proper data preprocessing pipelines
- Use appropriate model architectures
- Handle model versioning and experiment tracking
- Implement proper evaluation metrics
- Deploy models with monitoring
- Optimize for inference performance

## Testing Requirements
Always run tests after making changes:
- Unit tests for individual components
- Integration tests for feature workflows
- End-to-end tests for critical paths
- Performance tests for bottlenecks

## Code Conventions
- Follow existing code style in the project
- Use meaningful variable and function names
- Write self-documenting code
- Add comments only when necessary for complex logic
- Keep functions small and focused
- Follow DRY (Don't Repeat Yourself) principle

## Security Guidelines
- Never commit secrets or API keys
- Validate all user inputs
- Use parameterized queries for databases
- Implement proper authentication and authorization
- Follow principle of least privilege
- Keep dependencies updated

EOF
```

### Option 2: Create a Condensed AGENTS.md

For a more concise approach, create a summary file:

```bash
cat > AGENTS.md << 'EOF'
# Development Guidelines

## Agent Specializations

**Languages**: Python (decorators, async/await, pytest), JavaScript/TypeScript (ES6+, strict types), Rust (memory safety, lifetimes), Go (concurrency, channels), Java (Spring Boot, streams), FastAPI (async APIs, Pydantic V2, SQLAlchemy 2.0, microservices)

**Infrastructure**: Kubernetes orchestration, Terraform IaC, CI/CD pipelines, cloud architecture (AWS/Azure/GCP), monitoring/observability

**Quality**: Security auditing (OWASP), code review (SOLID principles), performance optimization, test automation (unit/integration/e2e)

**Data**: SQL optimization (indexes, explain plans), ETL pipelines, database migrations, caching strategies

**AI/ML**: Model training pipelines, deployment optimization, experiment tracking, LLM integration

## Key Principles
1. Write idiomatic code for each language
2. Prioritize security and performance
3. Follow existing project conventions
4. Test thoroughly before committing
5. Document complex logic clearly

## Testing Commands
- Run all tests mentioned in package.json, Makefile, or similar
- Execute linting and type checking
- Verify builds complete successfully

EOF
```

### Option 3: Dynamic Context-Based File

Create a more sophisticated AGENTS.md that references specific agent behaviors:

```bash
cat > AGENTS.md << 'EOF'
# AI Assistant Guidelines

This project uses specialized agent patterns for different tasks. Apply the appropriate expertise based on the current context:

## Context-Specific Behaviors

When you see **Python files** → Apply python-pro expertise:
- Advanced Python features, async programming, comprehensive testing

When you see **FastAPI applications** → Apply fastapi-pro expertise:
- Async-first development, Pydantic validation, SQLAlchemy 2.0, microservices

When you see **Kubernetes/Docker files** → Apply kubernetes-engineer expertise:
- Container best practices, orchestration patterns, security scanning

When you see **SQL/database files** → Apply sql-pro expertise:
- Query optimization, proper indexing, migration safety

When you see **Security concerns** → Apply security-auditor expertise:
- Vulnerability scanning, OWASP compliance, secure coding

When you see **Performance issues** → Apply performance-engineer expertise:
- Profiling, optimization, caching strategies

## Universal Requirements
1. Always run tests after changes
2. Follow existing code style
3. Prioritize readability and maintainability
4. Consider security implications
5. Document breaking changes

## Available Tools & Commands
- Build: Check package.json, Makefile, or build scripts
- Test: Run comprehensive test suite
- Lint: Apply code formatting and style checks
- Deploy: Follow CI/CD pipeline requirements

EOF
```

## File Placement

### Project-Level (Recommended)
Place AGENTS.md in your project root:
```bash
/your-project/
├── AGENTS.md          # Agent instructions
├── src/
├── tests/
└── package.json
```

### Multiple Locations
Codex searches for AGENTS.md files throughout the filesystem:
- `/` - System root
- `~` - User home directory
- Project repositories - Any directory with version control

**Priority**: The closest AGENTS.md to the edited file takes precedence.

## Best Practices for Codex

1. **Keep It Natural**: Write in plain English - Codex parses natural language instructions
2. **Be Specific**: Include concrete examples and clear guidelines
3. **Test Instructions**: Include how to run tests and verify changes
4. **Project Context**: Mention specific frameworks, tools, and conventions used
5. **Cascading Rules**: Place general rules at higher levels, specific rules closer to code

## Converting Individual Agents

To convert individual agents from this repository for Codex:

```python
# Simple Python script to combine agents
import os
import glob

agents = []
for file in glob.glob("*/*.md"):
    with open(file, 'r') as f:
        content = f.read()
        # Extract agent name and description from YAML front matter
        lines = content.split('\n')
        name = None
        description = None
        for line in lines:
            if line.startswith('name:'):
                name = line.split(':', 1)[1].strip()
            if line.startswith('description:'):
                description = line.split(':', 1)[1].strip()
            if line == '---' and name:
                break

        # Extract system prompt (everything after second ---)
        prompt_start = content.find('---', content.find('---') + 3) + 3
        prompt = content[prompt_start:].strip()

        if name and prompt:
            agents.append(f"### {name}\n{description}\n\n{prompt}\n")

# Write combined AGENTS.md
with open('AGENTS.md', 'w') as f:
    f.write("# AI Development Guidelines\n\n")
    f.write('\n'.join(agents))
```

## Key Differences from Claude Code

| Feature | Claude Code | Codex |
|---------|-------------|--------|
| Format | Individual .md files with YAML frontmatter | Single AGENTS.md with natural language |
| Location | `.claude/agents/` directory | Anywhere in filesystem |
| Structure | Structured with name, description, tools | Free-form Markdown |
| Model Selection | Specified per agent | Not applicable |
| Tool Control | Granular per agent | Global configuration |
| Organization | Category directories | Sections within single file |

## Interoperability

The AGENTS.md format is becoming a cross-tool standard:
- Supported by multiple AI coding assistants
- Simple Markdown format ensures compatibility
- Natural language instructions work across different AI models
- No strict schema requirements increase flexibility

## Monitoring Codex Usage

Codex actively uses AGENTS.md files for:
- Understanding project conventions
- Following testing requirements
- Applying coding standards
- Executing build and deployment commands
- Making PR descriptions

The `codex-1` system specifically looks for and follows test execution guidelines from AGENTS.md files.