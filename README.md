 # 🌲 ChocoPine

**Stop stressing. Start vibing.**
Coding should be as easy (and sweet) as eating a piece of cake.

![ChocoPine Logo](assets/logo.jpeg)

## The Problem with Vibe Coding

AI coding assistants are powerful, but they come with real challenges:

### 1. Prompt Engineering is Hard
The most time-consuming part of vibe coding isn't waiting for code—it's figuring out *how to ask*. One line of wrong instruction can send your entire feature in the wrong direction. You end up spending more time crafting the perfect prompt than actually building.

### 2. Beginners Don't Know What's Happening
When Claude Code starts working, it's a black box. What files is it looking at? What's the plan? What code is being added and why? Without visibility, you can't learn, and you can't catch mistakes before they multiply.

### 3. Context Windows Fill Up Fast
Here's what most people don't realize: Claude Code's quality **degrades significantly** when context fills to around 50%. With large codebases, your AI assistant gets dumber as the conversation goes on—right when you need it most.

## Our Solution: RQPIV Workflow

Vibe-Starter-Pack solves all three problems with a structured workflow:

> **R**esearch → **Q**uestion → **P**lan → **I**mplement → **V**alidate

### Better Requirements Through Clarification
Instead of you guessing the perfect prompt, **the system asks YOU clarifying questions**. It extracts exactly what you need through dialogue, so your requirements are complete before a single line of code is written.

### Full Transparency for Learning
Every step is visible. The research phase shows you what Claude found in your codebase. The planning phase shows you exactly what will be built and where. No more black box—you understand what's happening and why.

### Context Preserved Through Sub-Agents
This is the game-changer: **different phases use separate context windows via specialized sub-agents**. Research doesn't pollute your implementation context. Your main conversation stays clean and focused. The AI stays smart throughout the entire feature build.

## Getting Started

Simply clone this repository:

```bash
git clone https://github.com/vneseyoungster/Vibe-Starter-Pack.git
```

## How to Use It

### The Simple Way

```
/rqpiv Add a login page with user authentication
```

Claude handles the full workflow automatically—researching your codebase, asking you clarifying questions, showing you the plan, implementing, and validating.

### Step-by-Step Control

```
/rqpiv-start Add a shopping cart       # Initialize the workflow
/phase-question                         # Claude asks clarifying questions
/phase-plan                             # Review the implementation plan
/phase-implement                        # Watch code get written
/phase-validate                         # Run tests and security checks
```

## What Actually Happens

| Phase | What Claude Does | What You Do |
|-------|------------------|-------------|
| **Research** | Explores your codebase structure, patterns, and conventions | Wait (sub-agents handle this in separate context) |
| **Question** | Asks specific questions about your requirements | Answer to refine the feature spec |
| **Plan** | Creates detailed architecture and implementation plan | Review and approve before coding starts |
| **Implement** | Writes code following the approved plan exactly | Watch and intervene if needed |
| **Validate** | Runs tests, security audit, code review | Confirm everything works |

## Why This Works

- **No more prompt guessing** — The questioning phase extracts what you actually need
- **No more confusion** — Every phase produces visible artifacts in `docs/`
- **No more context degradation** — Sub-agents keep your main context clean
- **No more surprises** — You approve the plan before implementation begins

## Configuration

Edit `CLAUDE.md` to tell Claude about your project:
- Tech stack (language, framework, database)
- Build commands
- Code conventions
- Directory structure

The more context you provide upfront, the better the results.

## Requirements

- Claude Code version 1.0.124+
- Sub-agent support enabled

## Documentation

- [Full Workflow Documentation](RQPIV-Workflow-PRD.md)
- [Quick Reference](CLAUDE.md)

## License

MIT

---

Built for [Claude Code](https://claude.ai/claude-code)
