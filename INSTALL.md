# House Agents - Installation Guide

Quick reference for installing house agents in any project.

## Quick Install Prompts

### Project-Level Installation

Copy and paste this into Claude Code in your project:

```
Copy the .claude directory from [PATH_TO_HOUSE_AGENTS] to my current project. After installation, verify the three agent files exist (.claude/agents/house-research.yaml, house-mcp.yaml, house-bash.yaml), then test house-research by finding all TODO comments in the codebase.
```

**Replace the path** with wherever you cloned/downloaded house-agents.

### User-Wide Installation

Install once, use in all projects:

```
Create ~/.claude/agents/ directory if it doesn't exist, then copy all YAML files from [PATH_TO_HOUSE_AGENTS]/.claude/agents/ to ~/.claude/agents/. List the files to confirm installation, then test with "use house-research to find README files".
```

**Replace the path** with wherever you cloned/downloaded house-agents.

## From GitHub

If you want to install from a GitHub repository:

```
Clone https://github.com/houseworthe/house-agents to /tmp/house-agents, then copy the .claude directory to my current project. Verify installation and test house-research.
```

## Verify Installation

After installation, run this in Claude Code:

```
List all available sub-agents
```

You should see:
- house-research
- house-mcp
- house-bash

## Quick Test

```
Use house-research to find all TODO comments in the codebase
```

Should return a condensed list with file:line references.

## Troubleshooting

**Agents not showing up?**

```bash
# Project-level
ls .claude/agents/

# User-level
ls ~/.claude/agents/
```

**Try the `/agents` command** in Claude Code to see all loaded agents.

**YAML syntax errors?** Check the agent files for proper formatting.

---

See [README.md](./README.md) for full documentation and [USAGE.md](./USAGE.md) for examples.
