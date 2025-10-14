#!/usr/bin/env python3
"""
Token Counter for House Agents Benchmarking

Uses tiktoken to accurately count tokens for Claude models.
Provides utilities for measuring token usage in conversations.
"""

import tiktoken
import json
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any


class TokenCounter:
    """Count tokens for Claude models using tiktoken."""

    def __init__(self, model="cl100k_base"):
        """
        Initialize token counter.

        Args:
            model: Encoding to use. cl100k_base is closest to Claude's tokenizer.
        """
        self.encoding = tiktoken.get_encoding(model)
        self.model = model

    def count(self, text: str) -> int:
        """
        Count tokens in a text string.

        Args:
            text: Text to count tokens for

        Returns:
            Number of tokens
        """
        return len(self.encoding.encode(text))

    def count_messages(self, messages: List[Dict[str, str]]) -> Dict[str, int]:
        """
        Count tokens in a conversation.

        Args:
            messages: List of message dicts with 'role' and 'content' keys

        Returns:
            Dict with total, prompt, and response token counts
        """
        total = 0
        prompt_tokens = 0
        response_tokens = 0

        for msg in messages:
            tokens = self.count(msg['content'])
            total += tokens

            if msg['role'] in ['user', 'system']:
                prompt_tokens += tokens
            else:
                response_tokens += tokens

        return {
            'total': total,
            'prompt': prompt_tokens,
            'response': response_tokens
        }

    def format_count(self, count: int) -> str:
        """Format token count in human-readable form."""
        if count >= 1000:
            return f"{count/1000:.1f}k"
        return str(count)


class BenchmarkResult:
    """Store and analyze benchmark test results."""

    def __init__(self, test_name: str, test_type: str):
        """
        Initialize benchmark result.

        Args:
            test_name: Name of the test (e.g., "search-react-components")
            test_type: Type of test (baseline or agent)
        """
        self.test_name = test_name
        self.test_type = test_type  # 'baseline' or 'agent'
        self.messages = []
        self.start_time = datetime.now()
        self.end_time = None
        self.metadata = {}

    def add_message(self, role: str, content: str):
        """Add a message to the conversation."""
        self.messages.append({
            'role': role,
            'content': content,
            'timestamp': datetime.now().isoformat()
        })

    def finish(self):
        """Mark test as finished."""
        self.end_time = datetime.now()

    def calculate_tokens(self, counter: TokenCounter) -> Dict[str, int]:
        """Calculate token counts for this result."""
        return counter.count_messages(self.messages)

    def duration_seconds(self) -> float:
        """Get test duration in seconds."""
        if not self.end_time:
            return 0
        return (self.end_time - self.start_time).total_seconds()

    def to_dict(self) -> Dict[str, Any]:
        """Convert result to dictionary for JSON serialization."""
        counter = TokenCounter()
        tokens = self.calculate_tokens(counter)

        return {
            'test_name': self.test_name,
            'test_type': self.test_type,
            'start_time': self.start_time.isoformat(),
            'end_time': self.end_time.isoformat() if self.end_time else None,
            'duration_seconds': self.duration_seconds(),
            'tokens': tokens,
            'message_count': len(self.messages),
            'metadata': self.metadata
        }

    def save(self, output_dir: Path):
        """Save result to JSON file."""
        output_dir.mkdir(parents=True, exist_ok=True)
        filename = f"{self.test_name}_{self.test_type}_{int(self.start_time.timestamp())}.json"
        filepath = output_dir / filename

        with open(filepath, 'w') as f:
            json.dump(self.to_dict(), f, indent=2)

        return filepath


class BenchmarkAnalyzer:
    """Analyze and compare benchmark results."""

    def __init__(self, results_dir: Path):
        """
        Initialize analyzer.

        Args:
            results_dir: Directory containing result JSON files
        """
        self.results_dir = results_dir
        self.counter = TokenCounter()

    def load_results(self) -> List[Dict[str, Any]]:
        """Load all result files."""
        results = []
        for file in self.results_dir.glob("*.json"):
            with open(file) as f:
                results.append(json.load(f))
        return results

    def compare_test(self, test_name: str) -> Dict[str, Any]:
        """
        Compare baseline vs agent results for a specific test.

        Args:
            test_name: Name of test to compare

        Returns:
            Dict with comparison metrics
        """
        results = self.load_results()

        baseline = [r for r in results if r['test_name'] == test_name and r['test_type'] == 'baseline']
        agent = [r for r in results if r['test_name'] == test_name and r['test_type'] == 'agent']

        if not baseline or not agent:
            return None

        # Average results if multiple runs
        baseline_tokens = sum(r['tokens']['total'] for r in baseline) / len(baseline)
        agent_tokens = sum(r['tokens']['total'] for r in agent) / len(agent)

        savings = ((baseline_tokens - agent_tokens) / baseline_tokens) * 100

        return {
            'test_name': test_name,
            'baseline_tokens': int(baseline_tokens),
            'agent_tokens': int(agent_tokens),
            'tokens_saved': int(baseline_tokens - agent_tokens),
            'savings_percent': round(savings, 1),
            'baseline_runs': len(baseline),
            'agent_runs': len(agent)
        }

    def generate_report(self) -> str:
        """Generate markdown report of all test results."""
        results = self.load_results()

        # Get unique test names
        test_names = set(r['test_name'] for r in results)

        report = ["# Token Benchmark Results\n"]
        report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        report.append(f"Total tests: {len(test_names)}\n")
        report.append("\n## Summary\n")
        report.append("| Test | Baseline | With Agent | Savings | % Saved |")
        report.append("|------|----------|------------|---------|---------|")

        total_baseline = 0
        total_agent = 0

        for test_name in sorted(test_names):
            comparison = self.compare_test(test_name)
            if comparison:
                report.append(
                    f"| {comparison['test_name']} | "
                    f"{self.counter.format_count(comparison['baseline_tokens'])} | "
                    f"{self.counter.format_count(comparison['agent_tokens'])} | "
                    f"{self.counter.format_count(comparison['tokens_saved'])} | "
                    f"**{comparison['savings_percent']}%** |"
                )
                total_baseline += comparison['baseline_tokens']
                total_agent += comparison['agent_tokens']

        # Overall statistics
        if total_baseline > 0:
            overall_savings = ((total_baseline - total_agent) / total_baseline) * 100
            report.append(f"| **TOTAL** | "
                        f"**{self.counter.format_count(total_baseline)}** | "
                        f"**{self.counter.format_count(total_agent)}** | "
                        f"**{self.counter.format_count(total_baseline - total_agent)}** | "
                        f"**{round(overall_savings, 1)}%** |")

        return "\n".join(report)


def main():
    """CLI for token counter."""
    import sys

    if len(sys.argv) < 2:
        print("Usage: python token_counter.py <text_file>")
        print("       python token_counter.py analyze <results_dir>")
        sys.exit(1)

    if sys.argv[1] == "analyze":
        results_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("./results")
        analyzer = BenchmarkAnalyzer(results_dir)
        print(analyzer.generate_report())
    else:
        # Count tokens in a file
        counter = TokenCounter()
        with open(sys.argv[1]) as f:
            text = f.read()

        tokens = counter.count(text)
        print(f"Tokens: {tokens} ({counter.format_count(tokens)})")


if __name__ == "__main__":
    main()
