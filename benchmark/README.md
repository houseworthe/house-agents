# House Agents Token Benchmarking

This directory contains the token testing framework for validating House Agents' token savings claims.

## Overview

The benchmarking suite tests three agents across real-world scenarios:
- **house-research**: Code search and security audits
- **house-git**: Git diff and commit analysis
- **house-bash**: Command output analysis

## Quick Start

### 1. Setup

```bash
# Activate virtual environment
source benchmark/venv/bin/activate

# Verify tiktoken is installed
python -c "import tiktoken; print('✓ tiktoken ready')"
```

### 2. Clone Test Repositories

```bash
# Run the setup script
./benchmark/setup_repos.sh
```

This clones three test repositories:
- **Small**: create-react-app template (~20 files)
- **Medium**: Express.js boilerplate (~50 files)
- **Large**: Next.js blog starter (~100 files)

### 3. Run Tests

Tests must be run **manually** in Claude Code sessions to capture real token usage:

#### Test 1: Search React Hooks (house-research)
```
# Baseline (no agent)
Search through all JavaScript files in benchmark/repos/small/ and find
components that use the useEffect hook. Show me each occurrence with
the file path and line number.

# With Agent
Use house-research to find all React components using the useEffect hook
in benchmark/repos/small/
```

#### Test 2: Security Audit (house-research)
```
# Baseline (no agent)
Search the entire codebase in benchmark/repos/medium/ for security issues:
find all instances of eval(), innerHTML usage, and SQL queries using string
concatenation. Report each finding with file path, line number, and code.

# With Agent
Use house-research to find all instances of eval(), innerHTML, or SQL
injection vulnerabilities in benchmark/repos/medium/
```

#### Test 3: Stripe Configuration (house-mcp)
```
# Baseline (no agent)
Fetch the Stripe webhooks documentation from https://stripe.com/docs/webhooks
and create a working Express.js middleware that handles subscription webhook
events (created, updated, canceled) with proper signature verification.

# With Agent
Use house-mcp to set up Stripe webhook handling for subscription events
(created, updated, canceled) with signature verification
```

#### Test 4: Test Failures (house-bash)
```
# Baseline (no agent)
cd benchmark/repos/medium && npm test
Analyze the output and tell me which tests failed, what the error messages
were, and suggest fixes for each failure.

# With Agent
Use house-bash to run npm test in benchmark/repos/medium/ and analyze failures
```

#### Test 5: npm Install (house-bash)
```
# Baseline (no agent)
cd benchmark/repos/large && npm install
Tell me what packages were installed, if there were any warnings or errors,
and summarize the key information.

# With Agent
Use house-bash to run npm install in benchmark/repos/large/ and summarize results
```

### 4. Record Results

After each test, save the conversation to a text file:

```bash
# For baseline tests
benchmark/results/test1-search-hooks-baseline-run1.txt

# For agent tests
benchmark/results/test1-search-hooks-agent-run1.txt
```

**What to save:**
- All user prompts
- All Claude responses (full text)
- Any tool outputs (Grep, Read, Bash results)

### 5. Count Tokens

```bash
# Count tokens for a specific test
python benchmark/token_counter.py benchmark/results/test1-search-hooks-baseline-run1.txt

# Analyze all results
python benchmark/token_counter.py analyze benchmark/results/
```

### 6. Generate Report

```bash
# Create comprehensive analysis
python benchmark/generate_report.py > benchmark/RESULTS.md
```

## Test Methodology

### What We Measure

1. **Total Conversation Tokens**
   - All prompts sent to Claude
   - All responses received from Claude
   - Tool outputs that enter context

2. **Time Taken**
   - From initial prompt to final response
   - Includes agent invocation latency

3. **Message Count**
   - Number of back-and-forth exchanges
   - Indicator of conversation complexity

### Baseline Definition

**Baseline tests** represent what happens when a skilled user asks main Claude to perform the task WITHOUT using agents:

- Main Claude CAN use Grep, Read, Bash tools efficiently
- Main Claude WILL try to be selective about what to read
- Main Claude WON'T dump entire files into context unnecessarily

This is a **realistic comparison**, not a worst-case strawman.

### What Makes a Fair Test

✅ **Fair:**
- Baseline: "Search for useEffect usage" → Claude uses Grep intelligently
- Agent: "Use house-research to find useEffect usage"

❌ **Unfair:**
- Baseline: "Read every file and find useEffect" → Forces inefficiency
- Agent: "Use house-research to find useEffect usage"

### Statistical Reliability

Each test should be run **3 times** (both baseline and agent):
- Accounts for variation in Claude's responses
- Provides more reliable average
- Catches outliers

### Expected Ranges

Based on the testing plan, realistic expectations:

| Agent | Best Case | Typical | Worst Case |
|-------|-----------|---------|------------|
| house-research | 85% | 70-80% | 50% |
| house-git | 90% | 75-85% | 60% |
| house-bash | 95% | 85-90% | 75% |

## Directory Structure

```
benchmark/
├── README.md                    # This file
├── token_counter.py             # Token counting utility
├── test_scenarios.json          # Test definitions
├── setup_repos.sh               # Clone test repositories
├── generate_report.py           # Create final report
├── venv/                        # Python virtual environment
├── repos/                       # Test repositories
│   ├── small/                   # create-react-app template
│   ├── medium/                  # Express.js boilerplate
│   └── large/                   # Next.js blog starter
└── results/                     # Test result files
    ├── test1-search-hooks-baseline-run1.txt
    ├── test1-search-hooks-agent-run1.txt
    └── ...
```

## Interpreting Results

### Token Savings Calculation

```
Savings = (Baseline - Agent) / Baseline × 100%
```

Example:
- Baseline: 50,000 tokens
- Agent: 5,000 tokens
- Savings: (50k - 5k) / 50k = 90%

### What Good Results Look Like

- **Excellent**: 85%+ savings
- **Good**: 70-85% savings
- **Acceptable**: 50-70% savings
- **Marginal**: 30-50% savings
- **Not Worth It**: <30% savings

### When Agents Don't Help

Agents may show lower savings when:
- Codebase is very small (<10 files)
- Task requires full context understanding
- Output is already condensed
- Agent misunderstands the task

This is EXPECTED and should be documented honestly.

## Troubleshooting

### "tiktoken not installed"
```bash
source benchmark/venv/bin/activate
pip install tiktoken
```

### "Repository clone failed"
Check network connection and GitHub access:
```bash
git clone https://github.com/facebook/create-react-app.git /tmp/test-cra
```

### "Can't count tokens from conversation"
Save conversations as plain text, not HTML or formatted output.

## Contributing Results

Found interesting test cases? Submit them:
1. Add test scenario to `test_scenarios.json`
2. Run the test (baseline + agent, 3x each)
3. Submit PR with results

## Next Steps

After running tests:
1. Review `RESULTS.md` for findings
2. Update main `README.md` with real token savings
3. Add "Limitations" section if certain scenarios don't benefit
4. Create badges for verified savings percentages
