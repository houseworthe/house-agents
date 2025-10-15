# Contributing to House Agents

Thank you for your interest in contributing to House Agents! This document provides guidelines and instructions for contributing.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Enhancements](#suggesting-enhancements)
- [Creating New Agents](#creating-new-agents)
- [Pull Request Process](#pull-request-process)
- [Style Guidelines](#style-guidelines)

## Code of Conduct

This project follows a simple code of conduct: be respectful, constructive, and helpful. We're all here to make Claude Code better.

## How Can I Contribute?

### Reporting Bugs

Before creating a bug report:
1. Check the [existing issues](https://github.com/houseworthe/house-agents/issues) to avoid duplicates
2. Test with the latest version of Claude Code
3. Verify the agent files are properly formatted

When creating a bug report, include:
- **Clear title**: Describe the issue concisely
- **Steps to reproduce**: List exact steps to reproduce the behavior
- **Expected behavior**: What you expected to happen
- **Actual behavior**: What actually happened
- **Environment**: Claude Code version, OS, project type
- **Agent Configuration**: The relevant agent configuration (if modified)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:

- **Use a clear title**: Describe the enhancement
- **Provide detailed description**: Explain the use case and benefits
- **Include examples**: Show how the enhancement would be used
- **Consider token impact**: How does this affect context usage?

### Creating New Agents

Want to create a new house agent? Great! Here's how:

#### 1. Identify the Use Case

New agents should:
- Solve a specific high-token problem
- Have a clear, focused responsibility
- Not overlap with existing agents
- Provide condensed output (90%+ token reduction)

#### 2. Design the Agent

Create an agent file (`.md` with YAML frontmatter) in `.claude/agents/` with:

```yaml
---
name: house-yourname
description: "When to use this agent proactively. Be specific about triggers and use cases."
tools: Tool1, Tool2, Tool3
model: inherit
---

[System prompt for the agent]
```

**Key guidelines:**
- **Name**: Use `house-` prefix for consistency
- **Description**: Clear trigger conditions for proactive use
- **Tools**: Only include necessary tools
- **System prompt**: Follow the format of existing agents

#### 3. Test Thoroughly

Before submitting:
- Test with real-world use cases
- Verify token savings (use Claude Code's token counter)
- Ensure output stays under target token budget
- Test edge cases and error conditions

#### 4. Document

Add to `USAGE.md`:
- Clear examples of when to use the agent
- Sample invocations
- Expected output format
- Anti-patterns (when NOT to use)

### Pull Request Process

1. **Fork the repository** and create a branch from `main`
   ```bash
   git checkout -b feature/new-agent-name
   ```

2. **Make your changes**
   - Follow the style guidelines below
   - Update documentation as needed
   - Test your changes thoroughly

3. **Commit with clear messages**
   ```bash
   git commit -m "Add house-docker agent for container management"
   ```

4. **Push to your fork**
   ```bash
   git push origin feature/new-agent-name
   ```

5. **Open a Pull Request**
   - Use a clear title describing the change
   - Reference any related issues
   - Provide detailed description of changes
   - Include testing notes

6. **Address review feedback**
   - Be responsive to comments
   - Make requested changes promptly
   - Update the PR description if scope changes

### Review Criteria

Pull requests will be evaluated on:
- **Utility**: Does this solve a real problem?
- **Token efficiency**: Does it actually save tokens?
- **Code quality**: Is the agent file valid and well-structured?
- **Documentation**: Are examples clear and complete?
- **Testing**: Has it been tested in real scenarios?

## Style Guidelines

### Agent File Format

```yaml
---
# Use lowercase with hyphens for agent names
name: house-example

# Description should explain WHEN to use (triggers)
description: "Use proactively when [specific condition]. Returns [specific output format]."

# List only necessary tools, comma-separated
tools: Read, Grep, Glob

# Keep as 'inherit' unless specific model needed
model: inherit
---

# System prompt structure:
# 1. Opening statement (identity)
# 2. Mission (what the agent does)
# 3. Core Responsibilities (bulleted list)
# 4. Strategy (step-by-step approach)
# 5. Output Format (with examples)
# 6. Best Practices
# 7. Token Budget
# 8. Closing reminder
```

### Documentation Style

- Use clear, concise language
- Provide real-world examples
- Include file:line references
- Use code blocks for commands
- Show expected outputs
- Highlight gotchas and warnings

### Commit Messages

- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- Keep first line under 50 characters
- Add detailed description after blank line if needed

Examples:
```
Add house-docker agent for container workflows
Fix token budget in house-research system prompt
Update USAGE.md with multi-agent workflow examples
```

## Agent Design Principles

When creating or modifying agents:

1. **Single Responsibility**: Each agent should do one thing well
2. **Token Efficiency**: Target 85-98% token reduction
3. **Condensed Output**: Return only actionable information
4. **Source References**: Always cite file:line locations
5. **Clear Formatting**: Use consistent output structure
6. **Error Handling**: Gracefully handle failures
7. **Proactive Triggers**: Clear description of when to activate

## Testing Guidelines

Before submitting changes:

### For Agent Modifications
```
1. Test with small codebase (10-20 files)
2. Test with large codebase (100+ files)
3. Verify token counts (should be <5k output)
4. Test error conditions (missing files, syntax errors)
5. Verify output format matches specification
```

### For Documentation Changes
```
1. Check all links work
2. Verify code examples are valid
3. Test installation instructions
4. Check for typos and formatting
```

## Getting Help

- **Questions?** Open a [discussion](https://github.com/houseworthe/house-agents/discussions)
- **Bugs?** Open an [issue](https://github.com/houseworthe/house-agents/issues)
- **Ideas?** Start a discussion or open an issue

## Recognition

Contributors will be recognized in:
- Release notes for their contributions
- GitHub contributors page
- Special mention for new agents

Thank you for making House Agents better for everyone!
