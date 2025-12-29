# Claude Code Instruction

## Command Selection Guide

**⚠️ CRITICAL: Always use the correct slash command. Never work directly - commands handle everything.**

| User Request | Command |
|--------------|---------|
| New feature, enhancement, significant change | `/start [description]` |
| Bug fix, typo, config change, small fix | `/quick-fix [problem]` |
| Need to understand codebase first | `/research:codebase [topic]` |
| Want tests first before implementing (TDD) | `/research:feature [description]` |
| Have a Figma design to implement | `/research:ui [figma-url]` |
| Need external docs/library info | `/research:docs [topic]` |
| Ready to implement (plan exists) | `/execute [task]` |
| Validate/review existing code | `/code-check [target]` |
| New project setup | `/initialize [project-name]` |
| Generate project documentation | `/project-scan [target]` |

## Rules

1. **NEVER** work directly - always invoke a command
2. **NEVER** research, plan, or implement without a command
3. Commands delegate to subagents - let them handle the details

## Git Commits

When creating commits:
- **NEVER** include "Generated with Claude Code" or AI attribution
- Write messages as a human developer would

## Project Info

Fill in after running `/initialize` or `/project-scan`:
- Tech Stack: [auto-detected]
- Source: [auto-detected]
- Tests: [auto-detected]
- Build: `npm run dev` | `npm run build` | `npm test`