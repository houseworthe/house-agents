#!/usr/bin/env python3
"""
Regression test: Ensures house-mcp output stays under 2k tokens
Run after any changes to house-mcp.yaml

Usage:
    python benchmark/test_house_mcp_tokens.py

Exit codes:
    0 - Passed (under target or no test file)
    1 - Failed (exceeds max tokens)
"""

import sys
from pathlib import Path
from token_counter import TokenCounter

# Token limits
MAX_TOKENS = 2000  # Hard limit - fail if exceeded
TARGET_TOKENS = 800  # Ideal target - warn if exceeded

def test_stripe_config():
    """
    Test standard Stripe webhook config query.

    To generate test output, run in Claude Code:
    "Use house-mcp to set up Stripe webhook handling for subscription events"

    Then save the agent's response to:
    benchmark/results/house-mcp-stripe-test.txt
    """
    result_file = Path("benchmark/results/house-mcp-stripe-test.txt")

    if not result_file.exists():
        print("⚠️  No test output found at:", result_file)
        print()
        print("To generate test output:")
        print('1. Run in Claude Code: "Use house-mcp to set up Stripe webhook handling"')
        print("2. Copy agent response to benchmark/results/house-mcp-stripe-test.txt")
        print("3. Re-run this test")
        print()
        print("✅ No test file = passing (for now)")
        return True

    counter = TokenCounter()
    with open(result_file) as f:
        text = f.read()
        tokens = counter.count(text)

    print(f"📊 Token Analysis")
    print(f"   File: {result_file.name}")
    print(f"   Tokens: {tokens}")
    print(f"   Target: {TARGET_TOKENS}")
    print(f"   Max: {MAX_TOKENS}")
    print()

    # Check results
    if tokens > MAX_TOKENS:
        print(f"❌ FAILED: Output exceeds {MAX_TOKENS} tokens!")
        print(f"   Exceeded by: {tokens - MAX_TOKENS} tokens")
        print()
        print("Action required:")
        print("1. Review house-mcp.yaml for verbosity")
        print("2. Ensure agent follows <800 token target")
        print("3. Consider more aggressive summarization")
        return False
    elif tokens > TARGET_TOKENS:
        print(f"⚠️  WARNING: Output exceeds target of {TARGET_TOKENS} tokens")
        print(f"   Over target by: {tokens - TARGET_TOKENS} tokens")
        print()
        print("Still passing, but consider optimization.")
        return True
    else:
        print(f"✅ PASSED: Output within target ({tokens}/{TARGET_TOKENS} tokens)")
        print()
        savings = ((MAX_TOKENS - tokens) / MAX_TOKENS) * 100
        print(f"   Token savings: {round(savings, 1)}% under max")
        return True


def test_other_scenarios():
    """
    Test other common scenarios if test files exist.

    Add more test files as needed:
    - house-mcp-wordpress-test.txt
    - house-mcp-notion-test.txt
    - etc.
    """
    test_files = [
        "house-mcp-wordpress-test.txt",
        "house-mcp-api-integration-test.txt",
    ]

    results_dir = Path("benchmark/results")
    found_tests = []

    for filename in test_files:
        filepath = results_dir / filename
        if filepath.exists():
            found_tests.append(filepath)

    if not found_tests:
        return True

    print()
    print("📋 Additional Tests")
    print()

    counter = TokenCounter()
    all_passed = True

    for filepath in found_tests:
        with open(filepath) as f:
            tokens = counter.count(f.read())

        status = "✅" if tokens <= MAX_TOKENS else "❌"
        print(f"{status} {filepath.name}: {tokens} tokens")

        if tokens > MAX_TOKENS:
            all_passed = False

    return all_passed


def main():
    """Run all token regression tests."""
    print()
    print("🔍 House MCP Token Regression Test")
    print("=" * 50)
    print()

    # Run primary test
    stripe_passed = test_stripe_config()

    # Run additional tests if they exist
    other_passed = test_other_scenarios()

    # Overall result
    print()
    print("=" * 50)

    if stripe_passed and other_passed:
        print("✅ ALL TESTS PASSED")
        return 0
    else:
        print("❌ TESTS FAILED")
        print()
        print("The house-mcp agent is producing too much output.")
        print("Review .claude/agents/house-mcp.yaml and simplify.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
