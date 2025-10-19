# Changelog

All notable changes to House Agents will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- **house-mcp agent** - MCP tool configuration specialist
  - Works with all user-configured MCP servers (inherits all MCP tools automatically)
  - Reads verbose documentation and returns minimal working configs
  - Supports any MCP server (context7, notion, puppeteer, etc.)
  - Uses Claude Haiku 4.5 for cost efficiency

### Changed
- **Sub-agents now use Claude Haiku 4.5** for better performance and cost-efficiency
  - house-research, house-bash, house-git, house-mcp now explicitly use `claude-haiku-4-5-20251001`
  - 67% cost reduction on sub-agent operations ($1/$5 vs $3/$15 per million tokens)
  - 2x faster response times compared to Sonnet 4
  - 90% of Sonnet 4.5's agentic coding performance
  - Users can override by setting `model: inherit` in agent files if desired
- Added "Model Architecture" section to README.md explaining model usage strategy
- **house-mcp moved from "Future Agents" to production** - MCP bug #7296 workaround found
  - Omitting `tools:` field allows sub-agents to inherit all MCP tools from main session
  - Updated to be MCP-agnostic (works with any configured MCP server)

### Removed
- Benchmark suite (benchmark/ directory) - manual testing more practical than automated benchmarks
- test-agents.sh script - superseded by Claude Code's built-in agent validation
- examples/test-and-build.md - example superseded by updated documentation

## [0.2.0-beta] - 2025-10-14

### Added
- **house-git**: Git analysis agent for diffs, commits, and branch comparisons
- Git workflow example in examples/git-workflow.md
- "Future Agents" section in README documenting planned agents (house-vision, house-data, house-mcp)
- Pattern 4 (Pre-Merge Review) in USAGE.md

### Changed
- Updated README to feature three production agents (research, bash, git)
- Expanded INSTALL.md with house-git testing instructions
- Updated USAGE.md with house-git examples and pre-merge workflow pattern
- Clarified MCP tool access limitation affects future agents only
- Moved house-mcp to "Future Agents" (disabled) due to MCP tool access limitation

### Fixed
- Agent files now use `.md` extension (required by Claude Code) instead of `.yaml`
- Updated validation script to check for `.md` files
- Updated all documentation to reference `.md` file extension

## [0.1.0-beta] - 2025-01-13

### Added
- Initial beta release of House Agents
- Three core agents:
  - **house-research**: File and documentation search specialist
  - **house-bash**: Command execution and output parsing specialist
  - **house-mcp**: Tool configuration specialist (later moved to Future Agents in v0.2.0)
- Comprehensive documentation:
  - README.md with overview and quick start
  - INSTALL.md with installation instructions
  - USAGE.md with detailed examples and workflows
  - CONTRIBUTING.md with contribution guidelines
- MIT License
- GitHub repository setup with issue templates and PR template

### Features
- Context-efficient sub-agents run in separate context windows
- Token reduction of 85-98% for heavy operations
- Condensed output with source references (file:line format)
- Proactive agent suggestions based on task requirements
- Support for both project-level and user-level installation

### Documentation
- 15+ real-world usage examples
- Multi-agent workflow patterns
- Anti-pattern guidance
- Token savings calculations
- Troubleshooting guide

[Unreleased]: https://github.com/houseworthe/house-agents/compare/v0.2.0-beta...HEAD
[0.2.0-beta]: https://github.com/houseworthe/house-agents/compare/v0.1.0-beta...v0.2.0-beta
[0.1.0-beta]: https://github.com/houseworthe/house-agents/releases/tag/v0.1.0-beta
