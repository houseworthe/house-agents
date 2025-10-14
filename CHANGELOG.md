# Changelog

All notable changes to House Agents will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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

### Fixed
- Agent files now use `.md` extension (required by Claude Code) instead of `.yaml`
- Updated validation script to check for `.md` files
- Updated all documentation to reference `.md` file extension

## [0.1.0-beta] - 2025-01-13

### Added
- Initial beta release of House Agents
- Three core agents:
  - **house-research**: File and documentation search specialist
  - **house-mcp**: Tool configuration and integration specialist
  - **house-bash**: Command execution and output parsing specialist
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

[Unreleased]: https://github.com/houseworthe/house-agents/compare/v0.1.0-beta...HEAD
[0.1.0-beta]: https://github.com/houseworthe/house-agents/releases/tag/v0.1.0-beta
