# Git Workflow Example: Pre-Merge Code Review

This example shows how to use house agents for a complete pre-merge code review workflow.

## Scenario

You have a feature branch `feature-user-dashboard` that's ready to merge into `main`. You want to:
1. Review what changed
2. Run tests to verify functionality
3. Make an informed merge decision

## Workflow

### Step 1: Analyze Branch Differences

**You:**
```
Use house-git to compare feature-user-dashboard with main
```

**Expected Output:**
```
## Git Analysis: Branch Comparison (feature-user-dashboard vs main)

### Status
📊 Summary: 15 files changed, 423 insertions(+), 87 deletions(-)
📍 Branches: feature-user-dashboard is 12 commits ahead of main

### Key Changes by Impact

**🔴 CRITICAL (Review Carefully)**
- `src/dashboard/Dashboard.js:1-145` - NEW FILE: Main dashboard component
- `api/dashboard/stats.js:1-89` - NEW FILE: Dashboard stats endpoint
- `src/auth/permissions.js:45` - Added DASHBOARD_ACCESS permission
- Relevance: New feature with auth implications

**🟡 MEDIUM (Notable Changes)**
- `components/Chart.js:23-78` - Refactored chart rendering
- `api/users/controller.js:102` - Added dashboard stats method
- `tests/dashboard.test.js:1-156` - NEW FILE: Dashboard tests
- Relevance: Core functionality modifications

**🟢 MINOR (Low Risk)**
- `styles/dashboard.css:1-89` - NEW FILE: Dashboard styling
- `docs/FEATURES.md:45` - Documented dashboard feature
- Relevance: Non-functional changes

### Merge Status
⚠️ Conflicts in 1 file: src/App.js:67 (routing setup)

### Recommendations
1. Resolve merge conflict in App.js routing
2. Verify DASHBOARD_ACCESS permission is properly enforced
3. Test dashboard with production data
4. Run full test suite before merging
```

### Step 2: Resolve Merge Conflicts (if any)

**You:** (to main Claude)
```
Read src/App.js and show me the conflict around line 67
```

[Main Claude reads file, shows conflict, helps you resolve it]

### Step 3: Run Tests

**You:**
```
Use house-bash to run npm test and analyze results
```

**Expected Output:**
```
## Execution Results: Test Suite

### Status
✅ Success

### Summary
Ran 67 tests in 4.2s. All tests passed.

### Key Results
- Total tests: 67 (was 52 before dashboard tests added)
- Passed: 67 (100%)
- New tests: 15 (all dashboard-related)
- Duration: 4.2 seconds
- Coverage: 87% (up from 84%)

### Test Categories
- Dashboard tests: 15 passed
- Auth tests: 12 passed
- User tests: 18 passed
- API tests: 22 passed

### Next Steps
1. Tests are green - safe to merge
2. Coverage improved with dashboard tests
3. Consider adding integration tests for dashboard + auth
```

### Step 4: Make Merge Decision

**You:** (to main Claude)
```
Based on the analysis:
- 15 files changed, mostly new dashboard feature
- 1 merge conflict (resolved)
- All tests passing
- Permission system properly integrated

Please merge feature-user-dashboard into main with a descriptive commit message.
```

**Main Claude:**
```
I'll merge the feature branch.

[Executes: git merge feature-user-dashboard -m "Add user dashboard feature..."]

✅ Merge completed successfully
```

## Context Window Savings

**Without house agents:**
- Full git diff output: ~800 lines × 50 tokens/line = ~40,000 tokens
- Test output: ~500 lines × 30 tokens/line = ~15,000 tokens
- **Total main context: ~55,000 tokens**

**With house agents:**
- house-git summary: ~500 tokens
- house-bash summary: ~300 tokens
- **Total main context: ~800 tokens**

**Context window savings: ~98% (54,200 tokens kept in sub-agent contexts)**

## Key Takeaways

1. **house-git** analyzes large diffs without flooding your context
2. **house-bash** runs tests and condenses output
3. Main Claude stays focused on decision-making and implementation
4. Context remains clean throughout the workflow

## Alternative: Branch with Many Commits

If your feature branch has many commits (20+), you can analyze commit history:

**You:**
```
Use house-git to analyze the last 20 commits on feature-user-dashboard
```

This gives you a commit-by-commit overview without loading every diff into context.

## Common Variations

### Variation 1: Check for Breaking Changes

**You:**
```
Use house-git to compare feature-api-refactor with main and identify any breaking changes
```

house-git will flag changes to public APIs, configuration files, and database schemas.

### Variation 2: Review Specific File Types

**You:**
```
Use house-git to review changes to migration files between feature-branch and main
```

house-git will focus on database migration files and flag any that might cause issues.

### Variation 3: Pre-Deployment Check

**You:**
```
1. Use house-git to review changes on main since last deployment tag
2. Use house-bash to run the full test suite
3. Use house-bash to build for production
```

Complete pre-deployment validation workflow.

## Tips

- **Always resolve merge conflicts before running tests** - saves time if tests fail due to conflicts
- **Use descriptive branch names** - helps house-git provide better context in summaries
- **Review critical changes manually** - house-git highlights them, but you should verify
- **Run tests in feature branch** - catch issues before merge attempt

## When NOT to Use This Workflow

- **Small changes** (<5 files, <100 lines) - just review manually
- **Hotfixes** - speed is more important than thorough review
- **Documentation-only changes** - no code to test
- **Already reviewed in PR** - if you've done a thorough GitHub PR review, agents add little value

## Next Steps

After merging:
1. Delete the feature branch: `git branch -d feature-user-dashboard`
2. Push to remote: `git push origin main`
3. Tag if this is a release: `git tag v1.2.0`
4. Update CHANGELOG.md with new feature

---

This workflow demonstrates the power of combining multiple house agents for complex tasks. The key is letting each agent handle what it does best, while main Claude orchestrates and makes decisions.
