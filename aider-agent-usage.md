# Aider Agent Usage Instructions

## Overview
Aider uses a CONVENTIONS.md file for coding conventions and supports various chat modes for different tasks. While it doesn't have "agents" in the traditional sense, it provides specialized modes and can be configured with conventions that mirror agent-like behavior.

## Installation & Setup

### Creating CONVENTIONS.md from This Repository

Since Aider uses conventions rather than agents, we'll transform the agent prompts into convention guidelines:

```bash
# Create a comprehensive CONVENTIONS.md
cat > CONVENTIONS.md << 'EOF'
# Coding Conventions for Aider

## Language-Specific Conventions

### Python Development
When writing Python code:
- Use type hints for all function signatures
- Follow PEP 8 style guidelines strictly
- Implement comprehensive pytest tests with fixtures
- Use async/await for I/O-bound operations
- Prefer composition over inheritance
- Handle exceptions with context managers
- Use dataclasses or pydantic for data structures

### JavaScript/TypeScript
When writing JavaScript or TypeScript:
- Use modern ES6+ features (destructuring, spread, arrow functions)
- Implement strict TypeScript types, avoid 'any'
- Follow functional programming patterns where appropriate
- Handle promises with async/await, not callbacks
- Use proper error boundaries in React
- Implement proper memoization for performance

### Rust Development
When writing Rust code:
- Follow ownership and borrowing rules strictly
- Use Result and Option for error handling
- Implement traits for polymorphism
- Use lifetimes explicitly when needed
- Prefer iterators over loops
- Use cargo clippy for linting

### Go Development
When writing Go code:
- Follow effective Go guidelines
- Use goroutines and channels for concurrency
- Handle errors explicitly
- Keep interfaces small
- Use defer for cleanup
- Follow standard project layout

## Task-Specific Conventions

### Security Auditing
When reviewing code for security:
- Check for SQL injection vulnerabilities
- Validate all user inputs
- Review authentication and authorization
- Look for hardcoded secrets
- Check for XSS vulnerabilities
- Verify CSRF protection
- Review rate limiting implementation

### Performance Optimization
When optimizing performance:
- Profile before optimizing
- Optimize database queries first
- Implement caching strategically
- Use pagination for large datasets
- Optimize frontend bundle size
- Implement lazy loading
- Use CDN for static assets

### Database Operations
When working with databases:
- Use migrations for schema changes
- Create proper indexes
- Use transactions for data integrity
- Implement optimistic locking
- Use connection pooling
- Write parameterized queries
- Document complex queries

### Testing
When writing tests:
- Aim for 80% code coverage minimum
- Write unit tests for all functions
- Include integration tests for APIs
- Add e2e tests for critical paths
- Use mocking for external dependencies
- Test edge cases and error conditions
- Keep tests independent and idempotent

## Code Quality Standards

### Documentation
- Write clear docstrings for all public functions
- Include examples in documentation
- Document complex algorithms
- Maintain up-to-date README
- Document API endpoints
- Include setup instructions

### Error Handling
- Never silently catch exceptions
- Log errors with appropriate context
- Return meaningful error messages
- Use custom exception types
- Implement retry logic for transient failures
- Handle network timeouts gracefully

### Code Organization
- Keep functions under 20 lines
- Limit file size to 300 lines
- Use meaningful variable names
- Group related functionality
- Follow single responsibility principle
- Maintain consistent naming conventions

## Git Workflow
- Write descriptive commit messages
- Keep commits atomic
- Use conventional commits format
- Branch from main/master
- Squash commits before merging
- Update documentation with code changes

EOF
```

## Using Aider with Agent-Like Behaviors

### Mode-Specific Configurations

Aider supports different chat modes that can emulate agent behavior:

#### 1. Architect Mode (Planning Agent)
```bash
# Use architect mode for high-level planning
aider --architect --read CONVENTIONS.md

# Or switch in chat
/chat-mode architect
```

#### 2. Code Mode (Implementation Agent)
```bash
# Use code mode for implementation
aider --code --read CONVENTIONS.md

# Or switch in chat
/chat-mode code
```

#### 3. Ask Mode (Analysis Agent)
```bash
# Use ask mode for code analysis without changes
aider --ask --read CONVENTIONS.md

# Or switch in chat
/chat-mode ask
```

### Creating Agent-Like Scripts

Transform agents into Aider command scripts:

#### Python Expert Script
```bash
#!/bin/bash
# python-expert.sh
aider \
  --read CONVENTIONS.md \
  --message "Follow Python conventions: type hints, PEP 8, pytest, async/await" \
  --file "$@" \
  --auto-commits \
  --stream
```

#### Security Auditor Script
```bash
#!/bin/bash
# security-audit.sh
aider \
  --read CONVENTIONS.md \
  --ask \
  --message "Audit for security vulnerabilities: SQL injection, XSS, CSRF, hardcoded secrets" \
  --file "$@" \
  --no-auto-commits
```

#### Test Runner Script
```bash
#!/bin/bash
# test-runner.sh
aider \
  --read CONVENTIONS.md \
  --message "Write comprehensive tests: unit, integration, edge cases" \
  --file "$@" \
  --test-cmd "pytest" \
  --auto-test
```

## Advanced Configuration

### Environment Setup

Create a `.env` file for API keys:
```bash
# .env
OPENAI_API_KEY=your-key-here
ANTHROPIC_API_KEY=your-key-here
```

### Aider Configuration File

Create `.aider.conf.yml`:
```yaml
# Model configuration
model: claude-3.5-sonnet
editor-model: claude-3.5-haiku
editor-edit-format: diff

# Behavior settings
auto-commits: true
auto-test: true
stream: true
pretty: true

# File handling
gitignore: true
check-update: false

# Conventions
read:
  - CONVENTIONS.md
  - docs/architecture.md
```

## Converting Repository Agents for Aider

### Conversion Script

Create a Python script to convert agents to conventions:

```python
#!/usr/bin/env python3
import os
import glob

def extract_conventions_from_agents():
    """Convert agent files to Aider conventions."""
    conventions = {
        'languages': [],
        'security': [],
        'testing': [],
        'performance': [],
        'infrastructure': []
    }

    # Process each agent file
    for filepath in glob.glob("*/*.md"):
        with open(filepath, 'r') as f:
            content = f.read()

        # Extract prompt after YAML frontmatter
        if '---' in content:
            parts = content.split('---')
            if len(parts) >= 3:
                prompt = parts[2].strip()

                # Categorize based on directory
                category = os.path.dirname(filepath)
                if category == 'languages':
                    conventions['languages'].append(prompt)
                elif category == 'quality-security':
                    conventions['security'].append(prompt)
                # Add more categories as needed

    # Generate CONVENTIONS.md
    with open('CONVENTIONS.md', 'w') as f:
        f.write("# Aider Coding Conventions\n\n")

        for category, items in conventions.items():
            if items:
                f.write(f"## {category.title()}\n\n")
                for item in items:
                    f.write(f"{item}\n\n")

    print("Created CONVENTIONS.md from agent files")

if __name__ == "__main__":
    extract_conventions_from_agents()
```

## Mode and Command Mapping

Map repository agents to Aider modes:

| Agent Type | Aider Mode | Command Example |
|------------|------------|-----------------|
| code-reviewer | ask | `/ask Review this code for issues` |
| python-pro | code | `/code Implement with Python best practices` |
| architect-reviewer | architect | `/architect Design the system architecture` |
| security-auditor | ask | `/ask Check for security vulnerabilities` |
| test-automator | code | `/code Write comprehensive tests` |
| debugger | code | `/code Fix this bug` |
| performance-engineer | ask + code | `/ask Profile performance` then `/code Optimize` |

## Command Line Usage Examples

### Basic Usage with Conventions
```bash
# Start with conventions file
aider --read CONVENTIONS.md main.py

# Multiple files with conventions
aider --read CONVENTIONS.md src/*.py tests/*.py

# Specific task with conventions
aider --read CONVENTIONS.md --message "Refactor using Python best practices" app.py
```

### Emulating Specific Agents

#### Python Expert
```bash
aider \
  --read CONVENTIONS.md \
  --message "Apply Python best practices: type hints, async/await, error handling" \
  --file src/*.py
```

#### Security Auditor
```bash
aider \
  --ask \
  --read CONVENTIONS.md \
  --message "Audit for OWASP Top 10 vulnerabilities" \
  --file src/
```

#### Database Optimizer
```bash
aider \
  --read CONVENTIONS.md \
  --message "Optimize SQL queries and add proper indexes" \
  --file models/*.py migrations/*.sql
```

## In-Chat Commands

Use these commands during Aider sessions:

```bash
# Switch modes
/chat-mode architect  # Planning mode
/chat-mode code      # Implementation mode
/chat-mode ask       # Analysis mode

# File management
/add src/*.py        # Add files to edit
/drop test_*.py      # Remove files from context
/read docs/api.md    # Read documentation

# Workflow
/undo               # Undo last change
/diff              # Show changes
/commit            # Commit changes
/test              # Run tests

# Context management
/clear             # Clear chat history
/tokens            # Check token usage
/model claude-3.5-sonnet  # Switch model
```

## Best Practices

1. **Convention Organization**:
   - Keep CONVENTIONS.md concise and scannable
   - Group related conventions together
   - Use clear headers and bullet points
   - Include concrete examples

2. **Mode Selection**:
   - Use `architect` mode for system design
   - Use `code` mode for implementation
   - Use `ask` mode for analysis and review
   - Switch modes as tasks change

3. **File Context**:
   - Only add files that need editing
   - Use `/read` for reference files
   - Drop files when done to save context
   - Keep related files together

4. **Automation**:
   - Use `--auto-commits` for automatic git commits
   - Enable `--auto-test` to run tests automatically
   - Use `--cache-prompts` for faster iterations
   - Script common workflows

## Integration with CI/CD

### GitHub Actions Example
```yaml
name: AI Code Review
on: [pull_request]

jobs:
  ai-review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: AI Security Audit
        run: |
          aider \
            --ask \
            --read CONVENTIONS.md \
            --message "Security audit for vulnerabilities" \
            --file ${{ github.event.pull_request.changed_files }}
```

### Pre-commit Hook
```bash
#!/bin/bash
# .git/hooks/pre-commit
aider \
  --ask \
  --read CONVENTIONS.md \
  --message "Check for code quality issues" \
  --file $(git diff --cached --name-only)
```

## Key Differences from Other Tools

| Feature | Aider | Claude Code | OpenCode | Codex |
|---------|-------|-------------|----------|-------|
| Agent System | Modes + Conventions | Individual agents | JSON configs | AGENTS.md |
| Configuration | CONVENTIONS.md | YAML frontmatter | opencode.json | Natural language |
| Specialization | Chat modes | Subagents | Agent types | Sections |
| Context Management | Manual /add /drop | Automatic | Configured | Automatic |
| Edit Formats | Multiple formats | Direct editing | Direct editing | Direct editing |

## Troubleshooting

- **Conventions not loading**: Check file path with `--read`
- **Wrong mode**: Switch with `/chat-mode`
- **Too much context**: Use `/drop` to remove files
- **Model issues**: Verify API keys in .env
- **Edit format problems**: Try different `--editor-edit-format`