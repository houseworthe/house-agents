# House Agents - Installation Guide

Complete installation instructions for House Agents. Choose your installation method below.

---

## 🚀 Quick Install (Recommended)

Copy and paste these prompts directly into Claude Code. They handle everything: clone, install, verify, and test.

### Option 1: Project-Level Installation

Install agents in your current project only (`.claude/agents/` directory).

**Copy this into Claude Code:**

```
Clone https://github.com/houseworthe/house-agents to /tmp/house-agents, then copy the .claude directory to my current project. Verify the three agent files exist (.claude/agents/house-research.md, house-git.md, house-bash.md), then test house-research by finding all TODO comments in the codebase.
```

**What this does:**
1. Clones house-agents to /tmp/house-agents
2. Copies .claude/ directory to your current project
3. Verifies all 3 agent files are present
4. Tests house-research agent to confirm it works

**When to use:** You want agents only for this specific project, or you want to customize agents per-project.

---

### Option 2: User-Wide Installation

Install agents globally for ALL your projects (`~/.claude/agents/` directory).

**Copy this into Claude Code:**

```
Clone https://github.com/houseworthe/house-agents to /tmp/house-agents. Create ~/.claude/agents/ directory if it doesn't exist, then copy all .md files from /tmp/house-agents/.claude/agents/ to ~/.claude/agents/. List the installed agents and test house-research by finding README files in the codebase.
```

**What this does:**
1. Clones house-agents to /tmp/house-agents
2. Creates ~/.claude/agents/ if needed
3. Copies all 3 agent files to ~/.claude/agents/
4. Lists installed agents
5. Tests house-research to confirm it works

**When to use:** You want agents available in ALL your projects with the same configuration.

---

## 📋 Step-by-Step Manual Installation

If you prefer to run commands manually or want to understand each step:

### Step 1: Get House Agents

Clone the repository to a temporary location:

```bash
cd /tmp
git clone https://github.com/houseworthe/house-agents.git
cd house-agents
```

### Step 2: Choose Installation Method

#### Project-Level Installation

Install in your current project only:

```bash
# Navigate to your project
cd /path/to/your/project

# Copy the .claude directory
cp -r /tmp/house-agents/.claude .

# Verify installation
ls .claude/agents/
# Should show: house-bash.md, house-git.md, house-research.md
```

#### User-Wide Installation

Install globally for all projects:

```bash
# Create the user agents directory
mkdir -p ~/.claude/agents

# Copy agent files
cp /tmp/house-agents/.claude/agents/*.md ~/.claude/agents/

# Verify installation
ls ~/.claude/agents/
# Should show: house-bash.md, house-git.md, house-research.md
```

### Step 3: Verify Installation

Open Claude Code in any project and run:

```
List all available sub-agents
```

You should see:
- house-research
- house-git
- house-bash

Alternatively, use the `/agents` command in Claude Code.

### Step 4: Test Your Installation

Test each agent to ensure they work:

**Test house-research:**
```
Use house-research to find all TODO comments in the codebase
```
Expected: Condensed list with file:line references

**Test house-bash:**
```
Use house-bash to check the current git status
```
Expected: Summary of git status (not raw output)

**Test house-git:**
```
Use house-git to review my current git diff
```
Expected: Condensed summary with categorization (not raw diff output)

Note: If no git changes exist, try:
```
Use house-git to analyze the last 5 commits
```

---

## 🔧 Installation Methods Comparison

| Method | Location | Availability | Best For |
|--------|----------|--------------|----------|
| **Project-Level** | `.claude/agents/` | This project only | Project-specific agents, version control |
| **User-Wide** | `~/.claude/agents/` | All projects | Personal defaults, consistent across projects |

**Note:** Claude Code loads both levels. Project-level agents take precedence if there's a name conflict.

---

## ✅ Verification Checklist

After installation, verify everything works:

- [ ] Agents show up in `/agents` command or "List all available sub-agents"
- [ ] house-research returns condensed search results
- [ ] house-bash parses command output correctly
- [ ] house-git analyzes git diffs correctly
- [ ] No syntax errors in agent files

---

## 🐛 Troubleshooting

### Agents Not Showing Up

**Check if files exist:**
```bash
# Project-level
ls .claude/agents/

# User-level
ls ~/.claude/agents/
```

**Try the /agents command** in Claude Code to see all loaded agents.

### Agent File Syntax Errors

Run the validation script:
```bash
cd /tmp/house-agents
./test-agents.sh
```

This checks all agent files for syntax errors and required fields.

### Agents Show Up But Don't Work

1. **Restart Claude Code** - Sometimes agents need a reload
2. **Check agent files** - Ensure frontmatter has all required fields (name, description, tools, model)
3. **Test with simple task** - Try a basic search or command first
4. **Check Claude Code logs** - Look for error messages

### Permission Issues

If you get permission errors:
```bash
# Fix file permissions
chmod 644 ~/.claude/agents/*.md

# Fix directory permissions
chmod 755 ~/.claude/agents/
```

### Multiple Versions

If you have both project and user-level agents:
- **Project-level takes precedence** - Claude Code loads project agents first
- **User-level is fallback** - Used when project doesn't have specific agents
- **Remove duplicates** - Delete one version if you want consistent behavior

---

## 🔄 Updating House Agents

To update to the latest version:

```bash
# Pull latest changes
cd /tmp
rm -rf house-agents
git clone https://github.com/houseworthe/house-agents.git

# Reinstall (choose your method)
# Project-level:
cp -r /tmp/house-agents/.claude /path/to/your/project/

# User-wide:
cp /tmp/house-agents/.claude/agents/*.md ~/.claude/agents/
```

**Check for changes:**
```bash
cd /tmp/house-agents
cat CHANGELOG.md
```

---

## 🗑️ Uninstalling

### Remove Project-Level Agents

```bash
cd /path/to/your/project
rm -rf .claude/agents/
```

### Remove User-Wide Agents

```bash
rm ~/.claude/agents/house-*.md

# Or remove all agents
rm -rf ~/.claude/agents/
```

### Verify Removal

In Claude Code:
```
List all available sub-agents
```

House agents should no longer appear in the list.

---

## 📚 Next Steps

After installation:

1. **Read the usage guide** - See [USAGE.md](./USAGE.md) for detailed examples
2. **Check out examples** - Browse [examples/](./examples/) for real-world workflows
3. **Customize agents** - Edit agent files to tune behavior for your needs
4. **Join the community** - Report issues, suggest features at [GitHub](https://github.com/houseworthe/house-agents)

---

## 🆘 Need Help?

- **Questions:** Open a [Discussion](https://github.com/houseworthe/house-agents/discussions)
- **Bugs:** Create an [Issue](https://github.com/houseworthe/house-agents/issues)
- **Documentation:** See [README.md](./README.md) for overview
- **Examples:** See [USAGE.md](./USAGE.md) for workflows

---

**Quick Reference:**

| Command | Purpose |
|---------|---------|
| `List all available sub-agents` | See installed agents |
| `/agents` | Alternative way to list agents |
| `./test-agents.sh` | Validate agent files |
| `ls .claude/agents/` | Check project-level install |
| `ls ~/.claude/agents/` | Check user-wide install |
