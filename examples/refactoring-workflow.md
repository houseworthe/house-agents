# Refactoring Workflow Example

## Scenario

You need to refactor an authentication system that's spread across multiple files. The goal is to:
1. Understand the current implementation
2. Identify all auth-related code
3. Make changes consistently across files
4. Verify nothing broke

## Step 1: Research Current Implementation

**Your prompt:**
```
Use house-research to find all authentication-related code (look for 'auth', 'login', 'session', 'jwt' patterns)
```

**Expected output:**
```markdown
## Search Results: Authentication System

### Summary
Found auth code in 8 files across routes/, middleware/, and utils/.
Main authentication uses JWT, session management in Express.

### Key Findings

**1. Auth Routes**
- Location: `src/routes/auth.js:15-89`
- Details: Login, register, logout endpoints
- Relevance: Main entry points for authentication

**2. JWT Middleware**
- Location: `src/middleware/auth.js:12-45`
- Details: Token verification middleware
- Relevance: Applied to protected routes

**3. Token Generation**
- Location: `src/utils/jwt.js:23-56`
- Details: Creates and signs JWT tokens
- Relevance: Core token logic

### Patterns Observed
- No refresh token implementation
- Token expiration set to 24 hours
- Missing rate limiting on auth endpoints

### Recommended Actions
1. Add refresh token support
2. Implement rate limiting
3. Add token revocation list
```

## Step 2: Plan the Refactoring

Based on house-research findings, you now know:
- Where all auth code lives
- Current patterns and issues
- What needs to change

**Make your refactoring plan with main Claude:**
```
Based on the research findings, I want to:
1. Add refresh token support to jwt.js
2. Implement token revocation in middleware
3. Add rate limiting to auth routes

Let's start with the refresh token implementation
```

## Step 3: Make Changes

Work with main Claude to implement changes:
```
Update src/utils/jwt.js to generate both access and refresh tokens
```

*Claude makes the changes to jwt.js*

```
Now update src/middleware/auth.js to handle both token types
```

*Claude makes the changes to middleware*

## Step 4: Find Related Code

**Your prompt:**
```
Use house-research to find all places where the old jwt.generateToken() function is called
```

**Expected output:**
```markdown
## Search Results: jwt.generateToken() Usage

### Summary
Found 12 calls to jwt.generateToken() across 4 files.

### Key Findings

**Calls in auth.js**
- `src/routes/auth.js:34` - Login route
- `src/routes/auth.js:58` - Register route
- `src/routes/auth.js:89` - Password reset route

**Calls in test files**
- `tests/auth.test.js:23` - Login test
- `tests/auth.test.js:45` - Register test
[...]
```

## Step 5: Update All Call Sites

Now you know exactly where to make changes:
```
Update all jwt.generateToken() calls in src/routes/auth.js to use the new API that returns both tokens
```

## Step 6: Run Tests

**Your prompt:**
```
Use house-bash to run the auth test suite and check for failures
```

**Expected output:**
```markdown
## Execution Results: Auth Test Suite

### Status
❌ Failed - 3 tests failing

### Summary
Ran 45 tests in 1.2s. 42 passed, 3 failed.

### Errors Found

**Error 1: Token Structure Mismatch**
```
FAIL tests/auth.test.js
  ● Login should return JWT token

  Expected token to be string, got object with {accessToken, refreshToken}
```

**Suggested Fix**: Update test expectations to match new token structure

[...]

### Next Steps
1. Update test files to expect {accessToken, refreshToken} object
2. Update API documentation
3. Re-run tests after fixes
```

## Step 7: Fix Test Failures

Based on house-bash results:
```
Update the test expectations in tests/auth.test.js to handle the new token structure with accessToken and refreshToken
```

## Step 8: Verify Everything Works

**Your prompt:**
```
Use house-bash to run the full test suite and check the build
```

**Expected output:**
```markdown
## Execution Results: Full Test Suite + Build

### Status
✅ Success

### Summary
All 147 tests passed. Build completed without warnings.

### Key Results
- Tests: 147 passed in 8.2s
- Build time: 3.4s
- Bundle size: unchanged
- No linting errors
```

## Complete Workflow Summary

1. **house-research** - Understand current code structure (5k tokens)
2. **main Claude** - Make targeted changes (10k tokens)
3. **house-research** - Find all affected code locations (3k tokens)
4. **main Claude** - Update all call sites (8k tokens)
5. **house-bash** - Test and verify (4k tokens)

**Total: ~30k tokens** instead of 200k+ without agents

## Tips for Refactoring with House Agents

- Start with broad research to understand the system
- Make changes incrementally
- Use house-research to find all affected code
- Use house-bash to verify changes at each step
- Keep main conversation focused on implementation
- Let agents handle the heavy searching and testing

## Anti-Patterns

❌ **Don't do this:**
```
Use house-research to understand the auth system, then use house-bash to test it, then use house-research to verify, then use house-git to review changes...
```

✅ **Do this instead:**
```
1. Use house-research (review results)
2. Make changes with main Claude
3. Use house-bash to test (review results)
4. Iterate as needed
```

Let main Claude coordinate between agents!
