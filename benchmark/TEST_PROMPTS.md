# Test Prompts for Token Benchmarking

Copy these prompts EXACTLY into fresh Claude Code sessions. Run baseline first, then agent in a separate session.

---

## Test 1: Search for Async Functions

### 🔴 BASELINE (Run in NEW session #1)

```
I need to find all async functions in benchmark/repos/medium/.

Please search through the JavaScript files and show me:
1. Each file that contains async functions
2. The function names
3. Line numbers where they're defined

This is for a code audit, so I need to see all of them.
```

**What to expect:** Claude will use Grep to find "async" patterns, then Read files to get context and line numbers. Should return detailed findings.

**Save conversation to:** `benchmark/results/test1-async-baseline-run1.txt`

---

### 🟢 AGENT (Run in NEW session #2)

```
Use house-research to find all async functions in benchmark/repos/medium/ and report where they're defined.
```

**What to expect:** house-research agent condenses findings and returns summary with file:line references.

**Save conversation to:** `benchmark/results/test1-async-agent-run1.txt`

---

## Test 2: Security Audit

### 🔴 BASELINE (Run in NEW session #3)

```
I need to audit benchmark/repos/medium/ for security issues. Please search for:
1. Any use of eval()
2. Any use of innerHTML
3. SQL queries that use string concatenation (potential SQL injection)

For each issue found, show me:
- File path and line number
- The actual code snippet
- Why it's a security concern

This is important for a security review.
```

**What to expect:** Claude searches with Grep for multiple patterns, reads relevant files, provides detailed security analysis.

**Save conversation to:** `benchmark/results/test2-security-baseline-run1.txt`

---

### 🟢 AGENT (Run in NEW session #4)

```
Use house-research to find security vulnerabilities in benchmark/repos/medium/: eval() usage, innerHTML, and SQL injection patterns (string concatenation in queries).
```

**What to expect:** house-research returns condensed security report with findings and recommendations.

**Save conversation to:** `benchmark/results/test2-security-agent-run1.txt`

---

## Test 3: Find All TODO Comments

### 🔴 BASELINE (Run in NEW session #5)

```
Search benchmark/repos/medium/ for all TODO comments in the code.

Show me:
1. Each TODO comment text
2. File path and line number
3. Group them by priority if you can tell (URGENT, HIGH, MEDIUM, LOW)

I need this to plan our next sprint.
```

**What to expect:** Claude uses Grep for "TODO", reads files for context, organizes and categorizes findings.

**Save conversation to:** `benchmark/results/test3-todos-baseline-run1.txt`

---

### 🟢 AGENT (Run in NEW session #6)

```
Use house-research to find all TODO comments in benchmark/repos/medium/ and organize them by priority.
```

**What to expect:** house-research returns organized TODO list with file:line references.

**Save conversation to:** `benchmark/results/test3-todos-agent-run1.txt`

---

## Test 4: npm Test Analysis (house-bash)

### 🔴 BASELINE (Run in NEW session #7)

```
Please run the test suite in benchmark/repos/medium/:

cd benchmark/repos/medium && npm test

After running, analyze the results:
1. How many tests passed/failed?
2. What are the failure messages?
3. What might be causing the failures?
4. How would you fix each failure?
```

**What to expect:** Claude runs npm test via Bash, full output enters context, analyzes failures in detail.

**Save conversation to:** `benchmark/results/test4-npmtest-baseline-run1.txt`

---

### 🟢 AGENT (Run in NEW session #8)

```
Use house-bash to run npm test in benchmark/repos/medium/ and analyze any failures.
```

**What to expect:** house-bash runs test, condenses output to summary with key failures and suggested fixes.

**Save conversation to:** `benchmark/results/test4-npmtest-agent-run1.txt`

---

## Test 5: API Endpoint Inventory

### 🔴 BASELINE (Run in NEW session #9)

```
I need an inventory of all API endpoints in benchmark/repos/medium/.

Find all Express routes and tell me:
1. HTTP method (GET, POST, PUT, DELETE, etc.)
2. Route path (e.g., /api/users/:id)
3. File and line number where it's defined
4. Any middleware applied to the route

Create a table or organized list.
```

**What to expect:** Claude searches for route patterns, reads route files, extracts route definitions, creates organized output.

**Save conversation to:** `benchmark/results/test5-endpoints-baseline-run1.txt`

---

### 🟢 AGENT (Run in NEW session #10)

```
Use house-research to find all API endpoints in benchmark/repos/medium/ and list them with HTTP methods and file locations.
```

**What to expect:** house-research returns condensed endpoint inventory with file:line references.

**Save conversation to:** `benchmark/results/test5-endpoints-agent-run1.txt`

---

## Test 6: Stripe Configuration (house-mcp)

### 🔴 BASELINE (Run in NEW session #11)

```
I need to implement Stripe webhook handling for my Express app.

Please fetch the Stripe webhook documentation and create a complete Express middleware that:
1. Handles subscription events (created, updated, deleted)
2. Verifies webhook signatures
3. Includes proper error handling
4. Has comments explaining important parts

Give me production-ready code I can use.
```

**What to expect:** Claude fetches Stripe docs (many tokens), reads them, generates code with full documentation context.

**Save conversation to:** `benchmark/results/test6-stripe-baseline-run1.txt`

---

### 🟢 AGENT (Run in NEW session #12)

```
Use house-mcp to set up Stripe webhook handling for subscription events (created, updated, deleted) with signature verification.
```

**What to expect:** house-mcp digests docs and returns working code with minimal explanation.

**Save conversation to:** `benchmark/results/test6-stripe-agent-run1.txt`

---

## Test 7: Git Diff Analysis (house-git)

### 🔴 BASELINE (Run in NEW session #13)

```
I need to review the recent changes in benchmark/repos/medium/.

Run this git command:
```
cd benchmark/repos/medium && git diff HEAD~5..HEAD
```

Then analyze the diff and tell me:
1. What files were changed?
2. What are the key modifications in each file?
3. Which changes are critical and need careful review?
4. Which changes are minor (docs, formatting, etc.)?
5. Are there any security implications?

Organize this by importance so I know what to focus on.
```

**What to expect:** Claude runs git diff, full diff enters context (could be 1000+ lines), analyzes in detail.

**Save conversation to:** `benchmark/results/test7-gitdiff-baseline-run1.txt`

---

### 🟢 AGENT (Run in NEW session #14)

```
Use house-git to review changes from the last 5 commits in benchmark/repos/medium/ and categorize by impact.
```

**What to expect:** house-git runs diff in separate context, returns condensed summary with Critical/Medium/Minor categorization.

**Save conversation to:** `benchmark/results/test7-gitdiff-agent-run1.txt`

---

**Note on Prerequisites:**
If medium repo doesn't have git history, run:
```bash
cd benchmark/repos/medium
git add .
git commit -m "Initial commit for testing"
# Make some changes
echo "// Test change" >> src/app.js
git commit -am "Test change 1"
# Make more changes...
```

---

## After Running Tests

### 1. Count Tokens

```bash
cd /Users/ethanhouseworth/Documents/Personal-Projects/house-agents
source benchmark/venv/bin/activate

# Count each test
for file in benchmark/results/*.txt; do
    echo "=== $(basename $file) ==="
    python benchmark/token_counter.py "$file"
    echo ""
done
```

### 2. Calculate Savings

For each test pair:
```
Savings % = (Baseline Tokens - Agent Tokens) / Baseline Tokens × 100
```

Example:
- test1-async-baseline-run1.txt: 45,000 tokens
- test1-async-agent-run1.txt: 8,000 tokens
- Savings: (45000 - 8000) / 45000 = 82.2%

### 3. Create Results Table

| Test | Baseline | Agent | Saved | % |
|------|----------|-------|-------|---|
| Test 1: Async Functions | 45k | 8k | 37k | 82% |
| Test 2: Security Audit | ? | ? | ? | ? |
| ... | ... | ... | ... | ... |

---

## Important Notes

### For Fair Testing:

1. **Use SEPARATE sessions** - Don't run baseline and agent in same conversation
2. **Copy FULL conversation** - Include all prompts, responses, and tool outputs
3. **Run 3 times each** - For statistical reliability (optional but recommended)
4. **Same task** - Make sure baseline and agent are doing the same work

### What to Save:

When saving conversations to `.txt` files, include:
- Your initial prompt
- All of Claude's responses (full text)
- Any tool outputs (Grep results, Bash output, file contents)
- Follow-up questions and answers (if any)

**Don't include:**
- UI chrome (buttons, headers, etc.)
- System messages
- Timestamps (unless they're part of output)

### If Tests Fail:

- **npm test fails**: That's fine, we're testing output analysis not success
- **Agent misunderstands**: Note it in results, this is valid data
- **Task takes forever**: Set reasonable time limit (5 min max)

---

## Quick Validation

Test the token counter works:

```bash
# Create sample
cat > benchmark/results/sample.txt << 'EOF'
User: Hello
Assistant: This is a test response with some content.
EOF

# Count it
source benchmark/venv/bin/activate
python benchmark/token_counter.py benchmark/results/sample.txt
```

Should output: `Tokens: ~15 (0.0k)`

---

## Ready to Start?

1. Copy Test 1 BASELINE prompt above
2. Open NEW Claude Code session
3. Paste prompt
4. Wait for response
5. Copy entire conversation to benchmark/results/test1-async-baseline-run1.txt
6. Repeat with Test 1 AGENT prompt in another NEW session
7. Continue for remaining tests

Good luck! This is going to prove (or disprove) those 98% savings claims. 🎯
