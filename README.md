# RQPIV Workflow System for Claude Code

A structured development workflow framework that transforms Claude Code into an intelligent orchestration system with specialized sub-agents.

## What is RQPIV?

A 5-phase methodology: **Research → Question → Plan → Implement → Validate**

It helps you build features systematically with quality gates, preventing context window pollution and ensuring consistent code quality.

## Installation

Copy these to your project:

```bash
cp -r .claude /path/to/your/project/
cp -r docs /path/to/your/project/
cp CLAUDE.md /path/to/your/project/
```

## Usage

### Option 1: Full Automated Workflow (Recommended)

```
/rqpiv Add user authentication with JWT tokens
```

This runs all 5 phases automatically, pausing for your input when needed.

### Option 2: Manual Phase-by-Phase

```
/rqpiv-start Add user authentication    # Initialize session
/phase-question                          # Get clarifying questions
/phase-plan                              # Create architecture & task plan
/phase-implement                         # Execute the plan
/phase-validate                          # Review, test, security audit
```

## How It Works

1. **You describe what you want** - Use `/rqpiv [feature]` or `/rqpiv-start [feature]`

2. **Claude researches your codebase** - Sub-agents analyze your project structure, patterns, and dependencies

3. **You answer clarifying questions** - The system asks targeted questions to understand your requirements

4. **You approve the plan** - Review the architecture and implementation plan before any code is written

5. **Code is implemented** - Following your approved plan with quality checks

6. **Everything is validated** - Code review, tests, security audit, and documentation updates

## Tips for Best Results

- **Be specific** in your feature description
- **Answer all blocking questions** before moving to planning
- **Review the architecture** carefully before approving
- **Don't skip validation** - it catches issues early

## Customization

Edit `CLAUDE.md` in your project to add:
- Your tech stack details
- Build commands
- Project-specific conventions

## Requirements

- Claude Code version 1.0.124+
- Sub-agent support enabled

## Learn More

- [Full PRD](RQPIV-Workflow-PRD.md) - Detailed documentation
- [CLAUDE.md](CLAUDE.md) - Quick reference for all agents and commands

## License

MIT

---

Made for [Claude Code](https://claude.ai/claude-code)
