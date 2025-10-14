#!/bin/bash

# Setup Test Repositories for House Agents Benchmarking
# Clones three test repositories of different sizes

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPOS_DIR="$SCRIPT_DIR/repos"

echo "🏠 House Agents Benchmark Setup"
echo "==============================="
echo ""

# Create repos directory
mkdir -p "$REPOS_DIR"
mkdir -p "$SCRIPT_DIR/results"

echo "📦 Cloning test repositories..."
echo ""

# Small Repository: create-react-app template (~20 files, 2k LOC)
echo "1/3 Cloning small repository (create-react-app template)..."
if [ -d "$REPOS_DIR/small" ]; then
    echo "    ⚠️  Already exists, skipping"
else
    git clone --depth 1 --filter=blob:none --sparse \
        https://github.com/facebook/create-react-app.git \
        "$REPOS_DIR/small-temp" 2>&1 | grep -v "Cloning into" || true

    cd "$REPOS_DIR/small-temp"
    git sparse-checkout set packages/cra-template
    mv packages/cra-template "$REPOS_DIR/small"
    cd "$SCRIPT_DIR"
    rm -rf "$REPOS_DIR/small-temp"
    echo "    ✅ Small repository ready"
fi

# Medium Repository: Express.js boilerplate (~50 files, 5k LOC)
echo ""
echo "2/3 Cloning medium repository (Express.js boilerplate)..."
if [ -d "$REPOS_DIR/medium" ]; then
    echo "    ⚠️  Already exists, skipping"
else
    git clone --depth 1 \
        https://github.com/hagopj13/node-express-boilerplate.git \
        "$REPOS_DIR/medium" 2>&1 | grep -v "Cloning into" || true
    echo "    ✅ Medium repository ready"
fi

# Large Repository: Next.js blog starter (~100 files, 10k LOC)
echo ""
echo "3/3 Cloning large repository (Next.js blog starter)..."
if [ -d "$REPOS_DIR/large" ]; then
    echo "    ⚠️  Already exists, skipping"
else
    git clone --depth 1 --filter=blob:none --sparse \
        https://github.com/vercel/next.js.git \
        "$REPOS_DIR/large-temp" 2>&1 | grep -v "Cloning into" || true

    cd "$REPOS_DIR/large-temp"
    git sparse-checkout set examples/blog-starter
    mv examples/blog-starter "$REPOS_DIR/large"
    cd "$SCRIPT_DIR"
    rm -rf "$REPOS_DIR/large-temp"
    echo "    ✅ Large repository ready"
fi

echo ""
echo "📊 Repository Statistics"
echo "==============================="

for size in small medium large; do
    if [ -d "$REPOS_DIR/$size" ]; then
        file_count=$(find "$REPOS_DIR/$size" -type f \( -name "*.js" -o -name "*.jsx" -o -name "*.ts" -o -name "*.tsx" \) 2>/dev/null | wc -l | tr -d ' ')
        total_files=$(find "$REPOS_DIR/$size" -type f 2>/dev/null | wc -l | tr -d ' ')
        echo "$size: $file_count code files, $total_files total files"
    fi
done

echo ""
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "  1. Review benchmark/README.md for test instructions"
echo "  2. Run tests manually in Claude Code sessions"
echo "  3. Save conversation logs to benchmark/results/"
echo "  4. Run: python benchmark/token_counter.py analyze"

echo ""
echo "📄 Creating test fixtures for house-git..."
mkdir -p "$SCRIPT_DIR/fixtures"

# Create git fixtures from medium repo if it has history
if [ -d "$REPOS_DIR/medium/.git" ]; then
    cd "$REPOS_DIR/medium"

    # Create sample diff fixture
    git diff HEAD~2..HEAD > "$SCRIPT_DIR/fixtures/sample-git-diff.txt" 2>/dev/null || echo "No commits to diff"

    # Create sample commit log
    git log -5 --oneline > "$SCRIPT_DIR/fixtures/sample-git-log.txt" 2>/dev/null || echo "No commits"

    cd "$SCRIPT_DIR"
    echo "  ✅ Git fixtures created"
else
    echo "  ⚠️  Warning: medium repo is not a git repository"
    echo "     Git test fixtures not created"
fi

echo ""
echo "✅ All setup complete!"
