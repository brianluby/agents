# OpenCode Agent Usage Instructions

## Overview
OpenCode supports two types of agents: primary agents (main assistants) and subagents. Configuration can be done through JSON config files or Markdown definitions, with support for custom system prompts, tool control, and model selection.

## Installation & Setup

### Method 1: JSON Configuration Approach

Create an `opencode.json` configuration file in your project root:

```json
{
  "agents": {
    "python-expert": {
      "description": "Python development with advanced features and optimization",
      "temperature": 0.7,
      "prompt": ".opencode/prompts/python-pro.md",
      "model": "claude-3.5-sonnet",
      "tools": {
        "read_file": true,
        "write_file": true,
        "run_command": true,
        "search": true
      },
      "permissions": {
        "file_write": "ask",
        "command_execution": "allow"
      }
    },
    "security-reviewer": {
      "description": "Security auditing and vulnerability detection",
      "temperature": 0.3,
      "prompt": ".opencode/prompts/security-auditor.md",
      "model": "claude-3-opus",
      "tools": {
        "read_file": true,
        "search": true,
        "write_file": false
      }
    }
  }
}
```

### Method 2: Markdown Agent Files

Create agent definitions as Markdown files:

```bash
# Create directory structure
mkdir -p .opencode/agents

# Convert agents from this repository
# Each .md file name becomes the agent name
cp languages/python-pro.md .opencode/agents/python.md
cp quality-security/security-auditor.md .opencode/agents/security.md
```

### Method 3: Using AGENTS.md (Compatible Format)

OpenCode also supports the AGENTS.md format for project-wide instructions:

```markdown
# AGENTS.md
## Python Development
When working with Python files, apply these conventions:
- Use type hints for all functions
- Follow PEP 8 style guidelines
- Implement comprehensive pytest tests
- Use async/await for I/O operations

## Security Review
For all code changes:
- Check for SQL injection vulnerabilities
- Validate user inputs
- Review authentication flows
- Scan for hardcoded secrets
```

## Converting This Repository for OpenCode

### Automated Conversion Script

Create a Python script to convert all agents:

```python
#!/usr/bin/env python3
import json
import os
import glob
import yaml

def parse_agent_file(filepath):
    """Parse agent markdown file and extract metadata."""
    with open(filepath, 'r') as f:
        content = f.read()

    # Extract YAML frontmatter
    if content.startswith('---'):
        yaml_end = content.find('---', 3)
        yaml_content = content[3:yaml_end]
        metadata = yaml.safe_load(yaml_content)
        prompt = content[yaml_end + 3:].strip()

        return metadata, prompt
    return None, None

def create_opencode_config():
    """Generate opencode.json from agent files."""
    config = {"agents": {}}

    # Process all agent files
    for agent_file in glob.glob("*/*.md"):
        metadata, prompt = parse_agent_file(agent_file)
        if metadata:
            agent_name = metadata.get('name', '').replace('-', '_')

            # Save prompt to separate file
            prompt_dir = ".opencode/prompts"
            os.makedirs(prompt_dir, exist_ok=True)
            prompt_file = f"{prompt_dir}/{agent_name}.md"

            with open(prompt_file, 'w') as f:
                f.write(prompt)

            # Create agent configuration
            config["agents"][agent_name] = {
                "description": metadata.get('description', ''),
                "prompt": prompt_file,
                "model": f"claude-3.5-{metadata.get('model', 'sonnet')}",
                "temperature": 0.7 if metadata.get('model') == 'haiku' else 0.5
            }

            # Configure tools based on agent type
            if 'security' in agent_name or 'review' in agent_name:
                config["agents"][agent_name]["tools"] = {
                    "read_file": True,
                    "write_file": False,
                    "run_command": False
                }

    # Write configuration
    with open('opencode.json', 'w') as f:
        json.dump(config, f, indent=2)

    print(f"Created opencode.json with {len(config['agents'])} agents")

if __name__ == "__main__":
    create_opencode_config()
```

### Manual Setup for Key Agents

#### 1. Create Agent Configurations

```bash
# Create the configuration structure
mkdir -p .opencode/agents .opencode/prompts
```

#### 2. Example Agent Definitions

**Python Expert (.opencode/agents/python.json)**:
```json
{
  "description": "Expert Python development with optimization",
  "temperature": 0.7,
  "prompt": "../prompts/python.md",
  "model": "claude-3.5-sonnet",
  "tools": {
    "read_file": true,
    "write_file": true,
    "run_command": true,
    "search": true
  }
}
```

**Security Auditor (.opencode/agents/security.json)**:
```json
{
  "description": "Security vulnerability detection and fixes",
  "temperature": 0.3,
  "prompt": "../prompts/security.md",
  "model": "claude-3-opus",
  "tools": {
    "read_file": true,
    "search": true,
    "write_file": false,
    "run_command": false
  },
  "permissions": {
    "file_write": "deny",
    "command_execution": "deny"
  }
}
```

## Global Rules Configuration

Create global rules that apply across all sessions:

```bash
# Global configuration
mkdir -p ~/.config/opencode
cat > ~/.config/opencode/AGENTS.md << 'EOF'
# Global Development Rules

## Personal Preferences
- Use 2 spaces for indentation
- Prefer functional programming patterns
- Always include type hints in Python
- Use conventional commits format

## Security Defaults
- Never commit API keys or secrets
- Always validate user inputs
- Use parameterized queries
- Implement rate limiting

EOF
```

## Custom Commands

Create custom commands as Markdown files:

```bash
# Create custom commands directory
mkdir -p .opencode/commands

# Create a test runner command
cat > .opencode/commands/test.md << 'EOF'
Run all tests with coverage report:
1. Execute unit tests
2. Generate coverage report
3. Run integration tests if available
4. Check for test failures
EOF

# Create a security scan command
cat > .opencode/commands/security-scan.md << 'EOF'
Perform comprehensive security audit:
1. Scan for hardcoded secrets
2. Check for SQL injection vulnerabilities
3. Review authentication mechanisms
4. Validate input sanitization
5. Check dependency vulnerabilities
EOF
```

## Key Configuration Options

### Agent Configuration Fields

| Field | Description | Example |
|-------|-------------|---------|
| `description` | **Required** - Brief description of agent's purpose | "Python expert for optimization" |
| `temperature` | LLM creativity (0.0-1.0) | 0.7 |
| `prompt` | Path to system prompt file | ".opencode/prompts/python.md" |
| `model` | Override default model | "claude-3.5-sonnet" |
| `tools` | Enable/disable specific tools | `{"read_file": true}` |
| `permissions` | Control agent actions | `{"file_write": "ask"}` |

### Permission Levels

- `allow` - Always allow the action
- `ask` - Request user confirmation
- `deny` - Never allow the action

### Tool Configuration

Available tools that can be controlled:
- `read_file` - Read file contents
- `write_file` - Modify files
- `run_command` - Execute shell commands
- `search` - Search through codebase
- `list_files` - List directory contents

## Usage Examples

### Invoke Specific Agent
```bash
# Use Python expert agent
opencode --agent python-expert "Refactor this function"

# Use security auditor
opencode --agent security-reviewer "Check for vulnerabilities"
```

### Chain Multiple Agents
```bash
# Development followed by review
opencode --agent python-expert "Implement feature" \
         --then security-reviewer "Review changes"
```

## Best Practices

1. **Model Selection**:
   - Use faster models (sonnet) for routine tasks
   - Reserve opus for complex analysis
   - Use haiku for simple documentation

2. **Tool Restrictions**:
   - Limit write access for review agents
   - Disable command execution for analysis agents
   - Grant full access only to development agents

3. **Temperature Tuning**:
   - Low (0.3-0.5) for deterministic tasks (reviews, analysis)
   - Medium (0.5-0.7) for development tasks
   - High (0.7-0.9) for creative tasks (documentation, planning)

4. **Prompt Organization**:
   - Keep prompts in `.opencode/prompts/` directory
   - Use descriptive filenames
   - Version control prompt files

## Directory Structure

Recommended project structure:
```
/your-project/
├── .opencode/
│   ├── agents/          # Agent JSON definitions
│   │   ├── python.json
│   │   └── security.json
│   ├── prompts/         # System prompts
│   │   ├── python.md
│   │   └── security.md
│   └── commands/        # Custom commands
│       └── test.md
├── opencode.json        # Main configuration
└── AGENTS.md           # Project conventions
```

## Migration from Other Tools

### From Claude Code
- Extract system prompts from YAML frontmatter
- Convert tool lists to tool configuration objects
- Map model names to OpenCode format

### From Codex
- Split AGENTS.md into individual agent prompts
- Create JSON configurations for each section
- Define tools based on agent requirements

### From Aider
- Convert CONVENTIONS.md to AGENTS.md
- Create agent configurations for different modes
- Map edit formats to appropriate agents

## Differences from Other Tools

| Feature | OpenCode | Claude Code | Codex | Aider |
|---------|----------|-------------|-------|-------|
| Config Format | JSON + Markdown | YAML + Markdown | Markdown only | Markdown |
| Agent Organization | JSON objects | Directory structure | Single file | Conventions file |
| Tool Control | Per-agent | Per-agent | Global | Global |
| Model Selection | Per-agent | Per-agent | N/A | Global |
| Permissions | Granular | Inherited | N/A | N/A |

## Troubleshooting

- **Agents not loading**: Check JSON syntax in opencode.json
- **Prompts not found**: Verify prompt file paths are relative to config
- **Tools not working**: Ensure tools are enabled in agent configuration
- **Model errors**: Verify model names match OpenCode's format