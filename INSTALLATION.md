# Installation Guide

This repository supports both Claude Code and OpenCode AI assistants. Choose the installation method based on your platform.

## Claude Code Installation

Claude Code expects agents to be in `~/.claude/agents/`. Since our Claude agents are now in the `claude/` subdirectory, you have two options:

### Option 1: Clone and Symlink (Recommended)

```bash
# Clone the repository
git clone https://github.com/brianluby/agents.git ~/agents-repo

# Create the Claude agents directory if it doesn't exist
mkdir -p ~/.claude

# Symlink the claude directory as the agents directory
ln -s ~/agents-repo/claude ~/.claude/agents
```

### Option 2: Clone Directly with Subdirectory

```bash
# Clone directly to the Claude directory
cd ~/.claude
git clone https://github.com/brianluby/agents.git

# Create a symlink to make the claude subdirectory accessible
ln -s agents/claude agents-claude
mv agents-claude agents
```

### Option 3: Use Git Sparse Checkout (Advanced)

```bash
cd ~/.claude
git clone --no-checkout https://github.com/brianluby/agents.git
cd agents
git sparse-checkout init
git sparse-checkout set claude/*
git checkout main

# Move claude contents up one level
mv claude/* .
rmdir claude
```

## OpenCode Installation

OpenCode now has access to all 97 agents (94 converted from Claude Code + 3 OpenCode-specific). OpenCode is flexible with agent locations and you can link agents globally or per-project:

### Global Installation

```bash
# Clone the repository
git clone https://github.com/brianluby/agents.git ~/agents-repo

# Link OpenCode agents globally
ln -s ~/agents-repo/opencode/* ~/.config/opencode/agent/
```

### Project-Specific Installation

```bash
# In your project directory
mkdir -p .opencode/agent
ln -s /path/to/agents-repo/opencode/* .opencode/agent/
```

## Shared Agents

Shared agents that work on both platforms can be linked to both locations:

```bash
# For Claude Code
ln -s ~/agents-repo/shared/* ~/.claude/agents/

# For OpenCode
ln -s ~/agents-repo/shared/* ~/.config/opencode/agent/
```

## Verifying Installation

### For Claude Code
- Restart Claude Code or reload the window
- Agents should be available for automatic invocation
- Use phrases like "use the python-pro agent" to explicitly invoke

### For OpenCode
- Run `opencode agent list` to see available agents
- Test with `opencode chat --agent agent-name`

## Troubleshooting

### Claude Code Not Finding Agents
- Ensure agents are in `~/.claude/agents/` (not in subdirectories)
- Check file permissions: `chmod -R 755 ~/.claude/agents`
- Verify YAML frontmatter is valid

### OpenCode Issues
- Check symlinks are not broken: `ls -la ~/.config/opencode/agent/`
- Ensure Markdown files have `.md` extension
- Verify `description` and `mode` fields are present

## Updating Agents

To update the agents:

```bash
cd ~/agents-repo  # or wherever you cloned it
git pull origin main
```

The symlinks will automatically use the updated files.