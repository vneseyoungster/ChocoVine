
<div align="center">

![ChocoVine Logo](assets/logo.jpeg)

# ChocoVine

**Stop prompting. Start building.**

A workflow wrapper for **Claude Code** that forces AI to think before it types.
<br />

[![License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Built%20for-Claude%20Code-purple?style=flat-square)](https://claude.ai)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-green.svg?style=flat-square)](CONTRIBUTING.md)

[Getting Started](#-getting-started) • [The Workflow](#-the-workflow) • [Commands](#-command-reference)

</div>

---

## ⚡️ The Problem
We've all been there: You ask an AI to build a feature. It blindly writes 200 lines of code. You run it. It crashes. You spend the next hour prompt-battling to fix it.

## 🌲 The Solution
**ChocoVine turns "Vibes Coding" into Engineering.**
It stops hallucinations by enforcing a strict **Plan → Test → Build** loop.

*   🛡️ **TDD Guardrails:** The AI writes a failing test first. It *cannot* mark a task complete until that test passes.
*   🧠 **Infinite Context:** Uses sub-agents to read your entire codebase without clogging up the chat memory.
*   🔎 **You are the Architect:** You approve the Plan before a single line of code is written.
*   📈 **Scales with You:** Optimized for mid-to-large codebases where "context limits" usually break other tools.

---

## 🚀 Getting Started

You need [Claude Code](https://claude.ai/claude-code) installed.

### 1. Installation

#### Option A: npx (Recommended)

```bash
# Navigate to your project
cd your-project

# Install ChocoVine directly from GitHub
npx github:vneseyoungster/ChocoVine init
```

#### Option B: Clone the Repo

```bash
# Clone and copy manually
git clone https://github.com/vneseyoungster/ChocoVine.git
cp -r ChocoVine/.claude your-project/
```

### 2. Configuration

Edit the generated `CLAUDE.md` with your project details:

```bash
# Tell ChocoVine your stack (React, Python, etc.)
nano CLAUDE.md
```

### 3. Initialization

Tell ChocoVine to scan your project so it understands your architecture patterns.

```bash
# /init auto-detects: new project wizard OR existing project scan
/init
```

---

## 🎮 How to Use

### The Magic Command (`/start`)

For 95% of tasks, you only need one command. ChocoVine handles the planning, testing, and building automatically.

```bash
/start Add a login page with Google OAuth
```

**What happens next?**
1.  🕵️ **Scan:** Claude maps your codebase structure and patterns.
2.  🗣️ **Clarify:** It asks you specific questions (e.g., "Do you want to use Firebase or Auth0?").
3.  📝 **Plan:** It presents architecture and tasks. You approve.
4.  🧪 **Test:** It creates failing tests (because the code doesn't exist yet).
5.  ✅ **Build:** It writes the code to pass those tests, validates, and reviews.

---

## 🧩 The Workflow

How do we guarantee code quality? We strictly follow the **Plan → Test → Build** loop. This prevents the "spaghetti code" effect common with other AI tools.

```mermaid
graph LR
    A[/init] --> B[/plan]
    B --> C[/build]

    subgraph Plan
    B1[Scan] --> B2[Requirements]
    B2 --> B3[Tests]
    B3 --> B4[Architecture]
    end

    subgraph Build
    C1[Implement] --> C2[Validate]
    C2 --> C3[Review]
    end

    style B3 fill:#f96,stroke:#333,stroke-width:2px
    style C1 fill:#9f6,stroke:#333,stroke-width:2px
```

---

## 📚 Command Reference

### Core Commands
| Command | Description |
| :--- | :--- |
| `/start [task]` | **The Main Event.** Runs `/plan` then `/build` automatically. |
| `/plan [task]` | **The Planner.** Scan → Requirements → Tests → Architecture. |
| `/build [session]` | **The Builder.** Implement → Validate → Review. |
| `/fix [error]` | **Bug Hunter.** Systematic debugging or quick fixes. |
| `/refactor [type]` | **Code Surgeon.** Dead code cleanup, rename/move, extract, or general refactoring. |
| `/init` | **Setup.** New project wizard OR scan existing codebase. |

### Research
| Command | Description |
| :--- | :--- |
| `/research [topic]` | **Auto-routes.** Detects Figma URLs, docs, or general topics. |
| `/research --ui [figma-url]` | **Figma → Code.** Extracts tokens, CSS, and layout. |
| `/research --docs [library]` | **External Knowledge.** Reads library documentation. |
| `/research --analyze [topic]` | **Deep Dive.** Concept exploration and trade-off analysis. |

<details>
<summary><b>🔄 Migration from v1.x</b> (Click to expand)</summary>
<br />
Commands have been consolidated for simplicity:

| Old Command | New Equivalent |
| :--- | :--- |
| `/initialize` | `/init` |
| `/project-scan` | `/init` (auto-detects existing project) |
| `/research:codebase` | Part of `/plan` (Step 1: Scan) |
| `/research:feature` | Part of `/plan` (Step 2: Requirements) |
| `/research:spec` | Part of `/plan` (Step 3: Test Spec) |
| `/generate:tests` | Part of `/plan` (Step 4: Generate Tests) |
| `/research:plan` | Part of `/plan` (Step 5: Architecture) |
| `/execute` | `/build` (Step 1-2: Implement) |
| `/code-check` | `/build` (Step 3-4: Validate & Review) |
| `/quick-fix` | `/fix` |
| `/research:ui` | `/research --ui` |
| `/research:docs` | `/research --docs` |
| `/analyze` | `/research --analyze` |

</details>

---

## ⚙️ Configuration

To get the best results, your `CLAUDE.md` needs to be accurate. This is the "System Prompt" for your project.

```markdown
# CLAUDE.md Example
- **Stack:** Next.js 14, Tailwind, Supabase, TypeScript
- **Build Command:** npm run build
- **Test Command:** npm test
- **Conventions:** Use arrow functions, no 'any' types, prefer functional components.
```

## 📄 License

MIT © 