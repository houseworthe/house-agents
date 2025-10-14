---
name: New Agent Proposal
about: Propose a new house agent
title: '[AGENT] '
labels: new-agent
assignees: ''
---

## Agent Overview

**Proposed Name:** `house-[name]`

**One-line Description:** [What this agent does]

## Problem Statement

What high-token problem does this agent solve?
- Current token usage without agent: ~XXk
- Target token usage with agent: ~XXk
- Expected reduction: XX%

## Responsibility

What is this agent's single, focused responsibility?

## Use Cases

List 3-5 specific scenarios where this agent would be used:

1. **Use Case 1:**
   - Scenario: [Description]
   - Current approach: [How it's done now]
   - With this agent: [How it would work]
   - Token savings: ~XX%

2. **Use Case 2:**
   [...]

## Required Tools

Which tools would this agent need access to?
- [ ] Read
- [ ] Write
- [ ] Edit
- [ ] Grep
- [ ] Glob
- [ ] Bash
- [ ] WebFetch
- [ ] Task
- [ ] MCP tools (specify: mcp__*)
- [ ] Other: [specify]

## Output Format

Show an example of the condensed output this agent would return:

```markdown
## [Agent Results Title]

### Summary
[2-3 sentence overview]

### Key Findings
[Condensed, actionable information]

### Next Steps
[What to do with these results]
```

## Token Budget

What's the target token budget for this agent's output?
- Target: < XXk tokens
- Typical input: ~XXk tokens
- Typical output: ~XXk tokens

## Proactive Triggers

When should Claude Code automatically suggest this agent?
- "When user asks to [trigger condition]..."
- "When detecting pattern like [pattern]..."
- "When codebase has [characteristic]..."

## Overlap Check

Does this overlap with existing agents?
- **house-research**: [Yes/No - Explain]
- **house-mcp**: [Yes/No - Explain]
- **house-bash**: [Yes/No - Explain]

## Implementation Plan

- [ ] I have a draft YAML configuration
- [ ] I've tested this concept manually
- [ ] I can provide usage examples
- [ ] I'm willing to contribute the implementation
- [ ] I can help with documentation

## Draft Configuration

If you have a draft YAML, paste it here:

```yaml
---
name: house-[name]
description: "[When to use proactively]"
tools: [List]
model: inherit
---

[System prompt draft]
```

## Additional Notes

Any other context or considerations?

---

**Next Steps After Approval:**
1. Refine YAML configuration
2. Test with real scenarios
3. Write documentation and examples
4. Submit PR with implementation
