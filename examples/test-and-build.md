# Test and Build Example

## Scenario

You're working on a feature and need to:
1. Run tests frequently to check for regressions
2. Build the project to check for errors
3. Analyze test failures and build warnings
4. Keep your main conversation clean

## Problem Without House Agents

Running tests and builds produces verbose output:
- npm test: 50k-150k tokens
- npm run build: 80k-200k tokens
- Each run clutters your context
- Hard to find actual errors in the noise

## Solution: House Bash Agent

## Example 1: Running Tests

**Your prompt:**
```
Use house-bash to run the test suite and analyze any failures
```

**Expected output:**
```markdown
## Execution Results: Test Suite

### Status
❌ Failed - 3 tests failing

### Summary
Ran 47 tests in 2.3s. 44 passed, 3 failed.

### Commands Executed
1. `npm test`

### Key Results
- Total: 47 tests
- Passed: 44 (93.6%)
- Failed: 3 (6.4%)
- Duration: 2.3s

### Errors Found

**Error 1: JWT Token Validation**
```
FAIL src/auth/jwt.test.js:45
Expected expired token to be rejected
```
**Likely Cause**: JWT library not checking expiration
**Suggested Fix**: Check jwt.verify() options, ensure expiration checking is enabled

**Error 2: Password Hashing**
```
FAIL src/auth/password.test.js:23
Expected different hashes but got identical results
```
**Likely Cause**: Salt not being generated
**Suggested Fix**: Ensure bcrypt.hash() generates new salt each time

**Error 3: Rate Limiting**
```
FAIL src/auth/rateLimit.test.js:67
Expected request to be blocked but got 200 response
```
**Likely Cause**: Rate limiter not configured or Redis not running
**Suggested Fix**: Check Redis connection and middleware order

### Next Steps
1. Fix JWT expiration checking in auth/jwt.js
2. Review bcrypt salt generation
3. Verify rate limiter configuration
4. Re-run tests after fixes
```

## Example 2: Running Build

**Your prompt:**
```
Use house-bash to run the production build and check for issues
```

**Expected output:**
```markdown
## Execution Results: Production Build

### Status
✅ Success with warnings

### Summary
Build completed in 12.3s. Bundle size increased 15%.

### Commands Executed
1. `npm run build`

### Key Results
- Build time: 12.3s
- Main bundle: 245.3 KB (gzipped: 87.2 KB)
- Vendor bundle: 156.8 KB (gzipped: 52.1 KB)
- Total size: 402.1 KB

### Warnings Found

**Warning 1: Large Bundle Size**
```
asset size limit: main.js exceeds 244 KiB
```
**Suggested Fix**: Consider code splitting for Chart.js (89 KB)

**Warning 2: Deprecated API**
```
axios 'transformResponse' option is deprecated
```
**Suggested Fix**: Update to axios v1.0+ API

### Output Highlights
```
✓ Built in 12.3s
✓ 23 modules transformed

Bundle Analysis:
├─ main.js (245.3 KB)
│  ├─ React (45 KB)
│  ├─ Chart.js (89 KB) ← largest
│  └─ App code (111.3 KB)
```

### Next Steps
1. Lazy-load Chart.js (used on 2 pages only)
2. Update axios to remove deprecation warning
3. Set bundle size threshold in CI (250 KB)
```

## Example 3: Test-Driven Development Flow

When doing TDD, you run tests frequently:

**First run:**
```
Use house-bash to run tests for the auth module
```

*Get results, fix issues*

**Second run:**
```
Use house-bash to re-run auth tests
```

*Verify fixes*

**Final run:**
```
Use house-bash to run the full test suite
```

Each run returns condensed results (3-5k tokens) instead of full output (50k+ tokens).

## Example 4: Multi-Command Build Pipeline

**Your prompt:**
```
Use house-bash to run lint, test, and build in sequence
```

**Expected output:**
```markdown
## Execution Results: Build Pipeline

### Status
✅ Success

### Commands Executed
1. `npm run lint`
2. `npm test`
3. `npm run build`

### Key Results

**Linting**
- Files checked: 127
- Warnings: 0
- Errors: 0

**Tests**
- Total: 47
- Passed: 47
- Duration: 2.1s

**Build**
- Bundle size: 387.2 KB
- Build time: 11.8s
- Warnings: 0

### Next Steps
Ready to commit and push changes
```

## Token Comparison

| Operation | Without Agent | With house-bash | Savings |
|-----------|---------------|-----------------|---------|
| npm test | 120k tokens | 4k tokens | 97% |
| npm build | 180k tokens | 4k tokens | 98% |
| Full pipeline | 400k tokens | 8k tokens | 98% |

## Integration with Development Workflow

### Before Committing
```
Use house-bash to run the pre-commit checks (lint, test, build)
```

### After Changes
```
Use house-bash to verify the changes didn't break anything
```

### Debugging Test Failures
```
Use house-bash to run tests with verbose output for the failing test file
```

## Tips

1. **Run tests early and often**
   - Don't wait until everything is done
   - Use house-bash to run tests after each change
   - Keep main context clean

2. **Let the agent summarize**
   - Don't ask for full output
   - Trust the agent to identify errors
   - Review only the relevant error snippets

3. **Use specific test commands**
   - `npm test -- auth.test.js` for single file
   - `npm test -- --coverage` for coverage
   - Agent will parse and summarize appropriately

4. **Combine with other agents**
   ```
   Use house-research to find all test files
   [Review test coverage]
   Use house-bash to run the tests
   ```

## Anti-Patterns

❌ **Don't do this:**
```
Run npm test and show me the full output
```
*This defeats the purpose - you want condensed results*

❌ **Don't do this:**
```
Use house-bash to run tests, then read the log file, then analyze it...
```
*Let the agent do all of this in one call*

✅ **Do this:**
```
Use house-bash to run the test suite and analyze failures
```
*Simple, clear, gets you actionable results*

## Real-World Impact

### Development Flow
1. Make changes to code
2. `Use house-bash to run tests`
3. Get 4k token summary
4. Fix issues based on summary
5. Repeat

**Context stays clean:** Only 4k tokens per test run instead of 120k

### CI/CD Integration
Use house-bash patterns in your own scripts:
- Run command
- Parse output
- Extract key information
- Return actionable summary

This is exactly what house-bash does, and you can apply the same pattern to your automation.
