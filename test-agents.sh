#!/bin/bash

# House Agents Validation Script
# Tests agent YAML files for syntax errors and required fields

set -e

AGENT_DIR=".claude/agents"
FAILED=0
TESTED=0

echo "🏠 House Agents Validation"
echo "=========================="
echo ""

# Check if agent directory exists
if [ ! -d "$AGENT_DIR" ]; then
    echo "❌ Error: .claude/agents directory not found"
    echo "   Please run this script from the house-agents project root"
    exit 1
fi

# Function to validate YAML structure
validate_agent() {
    local file=$1
    local name=$(basename "$file" .md)

    echo "Testing: $name"
    TESTED=$((TESTED + 1))

    # Check if file is readable
    if [ ! -r "$file" ]; then
        echo "  ❌ Cannot read file"
        FAILED=$((FAILED + 1))
        return 1
    fi

    # Check for required frontmatter fields
    if ! grep -q "^name:" "$file"; then
        echo "  ❌ Missing 'name' field in frontmatter"
        FAILED=$((FAILED + 1))
        return 1
    fi

    if ! grep -q "^description:" "$file"; then
        echo "  ❌ Missing 'description' field in frontmatter"
        FAILED=$((FAILED + 1))
        return 1
    fi

    if ! grep -q "^tools:" "$file"; then
        echo "  ❌ Missing 'tools' field in frontmatter"
        FAILED=$((FAILED + 1))
        return 1
    fi

    if ! grep -q "^model:" "$file"; then
        echo "  ❌ Missing 'model' field in frontmatter"
        FAILED=$((FAILED + 1))
        return 1
    fi

    # Check for frontmatter delimiters
    local delimiter_count=$(grep -c "^---$" "$file" || true)
    if [ "$delimiter_count" -lt 2 ]; then
        echo "  ❌ Invalid frontmatter (need opening and closing ---)"
        FAILED=$((FAILED + 1))
        return 1
    fi

    # Check for system prompt after frontmatter
    local has_content=$(awk '/^---$/{f++}f==2' "$file" | grep -c . || true)
    if [ "$has_content" -eq 0 ]; then
        echo "  ❌ No system prompt content after frontmatter"
        FAILED=$((FAILED + 1))
        return 1
    fi

    # Check name matches filename
    local yaml_name=$(grep "^name:" "$file" | cut -d: -f2 | tr -d ' ')
    if [ "$yaml_name" != "$name" ]; then
        echo "  ⚠️  Warning: name field ($yaml_name) doesn't match filename ($name)"
    fi

    echo "  ✅ Valid"
    return 0
}

# Validate each agent file
for agent in "$AGENT_DIR"/*.md; do
    if [ -f "$agent" ]; then
        validate_agent "$agent"
        echo ""
    fi
done

# Summary
echo "=========================="
echo "Summary:"
echo "  Tested: $TESTED agents"
echo "  Failed: $FAILED agents"
echo ""

if [ $FAILED -eq 0 ]; then
    echo "✅ All agents are valid!"
    exit 0
else
    echo "❌ $FAILED agent(s) failed validation"
    exit 1
fi
