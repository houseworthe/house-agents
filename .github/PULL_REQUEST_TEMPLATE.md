# Pull Request

## Description

Brief description of the changes in this PR.

## Type of Change

- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] New agent (adds a new house agent)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Code refactoring

## Changes Made

List the specific changes made in this PR:

- Change 1
- Change 2
- Change 3

## Related Issues

Closes #[issue number]
Relates to #[issue number]

## Testing

### Test Environment
- Claude Code Version: [e.g., 0.7.2]
- OS: [e.g., macOS 14.1]
- Project type: [e.g., Node.js, Python]

### Testing Performed

Describe how you tested these changes:

- [ ] Ran `./test-agents.sh` - all agents valid
- [ ] Tested with small codebase (<20 files)
- [ ] Tested with large codebase (100+ files)
- [ ] Verified token counts meet targets
- [ ] Tested edge cases and error conditions
- [ ] Updated documentation
- [ ] Added examples (if applicable)

### Test Results

**Token Impact:**
- Before: ~XXk tokens
- After: ~XXk tokens
- Improvement: XX%

**Sample Output:**
```
[Paste condensed output from your testing]
```

## For New Agents

If this PR adds a new agent, complete this section:

### Agent Details
- **Name:** `house-[name]`
- **Purpose:** [One sentence]
- **Tools Used:** [List]
- **Token Budget:** < XXk tokens

### Proactive Triggers
When should Claude Code suggest this agent automatically?
- [Trigger condition 1]
- [Trigger condition 2]

### Example Usage
```
User: "Use house-[name] to [task]"

Agent returns:
[Show expected output format]
```

### Documentation
- [ ] Added to README.md (if major feature)
- [ ] Added examples to USAGE.md
- [ ] Created example workflow in examples/
- [ ] Updated CHANGELOG.md

## Documentation

- [ ] Documentation has been updated (README, USAGE, etc)
- [ ] CHANGELOG.md has been updated
- [ ] Examples have been added or updated
- [ ] Comments have been added to complex code

## Checklist

- [ ] My code follows the style guidelines (see CONTRIBUTING.md)
- [ ] I have performed a self-review of my own code
- [ ] I have commented complex or non-obvious code
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings or errors
- [ ] I have tested my changes thoroughly
- [ ] Any dependent changes have been merged and published

## Breaking Changes

If this is a breaking change, describe:
1. What breaks?
2. How should users update their configuration?
3. Is there a migration path?

## Screenshots (if applicable)

Add screenshots showing the changes, especially for documentation or output format changes.

## Additional Notes

Any additional context or notes for reviewers.

---

**For Reviewers:**
- Does this PR solve a real problem?
- Does it achieve the claimed token savings?
- Is the code/config high quality?
- Is documentation complete and clear?
- Have edge cases been considered?
