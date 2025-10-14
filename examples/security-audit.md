# Security Audit Example

## Scenario

You need to audit a codebase for common security issues like:
- Use of `eval()` or `innerHTML`
- Hardcoded credentials or API keys
- SQL injection vulnerabilities
- Insecure dependencies

## Step 1: Search for Dangerous Code Patterns

**Your prompt:**
```
Use house-research to find all instances of eval(), innerHTML, or direct string concatenation in SQL queries
```

**Expected output format:**
```markdown
## Search Results: Security Issues

### Summary
Found 5 instances of potentially unsafe code patterns across 3 files.
2 are high risk, 3 are medium risk.

### Key Findings

**1. Direct eval() usage (HIGH RISK)**
- Location: `src/utils/parser.js:42`
- Details: `eval(userInput)` - evaluating unsanitized user input
- Relevance: Critical security vulnerability

**2. innerHTML with user data**
- Location: `src/components/UserProfile.js:89`
- Details: `element.innerHTML = userData.bio` - XSS risk
- Relevance: User-supplied content rendered without sanitization

[...]

### Recommended Actions
1. Replace eval() with JSON.parse()
2. Use textContent or DOMPurify for innerHTML
3. Use parameterized queries for SQL
```

## Step 2: Check for Hardcoded Secrets

**Your prompt:**
```
Use house-research to find hardcoded API keys, passwords, or tokens (search for common patterns like 'api_key', 'password =', 'token =')
```

**Expected output format:**
```markdown
## Search Results: Potential Hardcoded Secrets

### Summary
Found 3 potential secrets hardcoded in source files.

### Key Findings

**1. API Key in config file**
- Location: `config/database.js:15`
- Details: `apiKey: "sk_live_xxxxxxxxxxxx"`
- Relevance: Production API key in source control

[...]
```

## Step 3: Implement Fixes

After getting the condensed results, you can:
1. Review each finding
2. Fix the issues in your editor
3. Verify fixes with tests

## Token Comparison

| Method | Token Usage | Time |
|--------|-------------|------|
| Main Claude searching all files | ~150k tokens | 2-3 min |
| House Research agent | ~4k tokens | 30 sec |
| **Savings** | **~97%** | **~85%** |

## Next Steps

After the security audit:
```
Use house-bash to run the security linter and test suite to verify fixes
```

## Tips

- Be specific about patterns to search for
- Run multiple focused searches rather than one broad search
- Review agent findings before making changes
- Use house-bash to verify fixes with automated tests
