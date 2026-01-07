
# ChocoVine


**AI coding that actually builds what you asked for.**

ChocoVine is a workflow wrapper for **Claude Code** designed for **mid to large codebases**. It stops AI from hallucinating by forcing a structured approach: research first, plan second, tests third, code last. The result? Features that work on the first try, and a codebase that doesn't turn into spaghetti.

![alt text](assets/logo.jpeg)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Built%20for-Claude%20Code-purple)](https://claude.ai)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-green.svg)](CONTRIBUTING.md)

---

## Why ChocoVine?

We've all been there: You ask an AI to build a feature. It writes 200 lines of code. You run it. It crashes. You spend the next hour prompt-battling to fix it.

**ChocoVine fixes the "Black Box" problem:**

*   **No more regression bugs:** We force a TDD (Test Driven Development) workflow. The AI writes the test first. It *cannot* say it's finished until the test passes.
*   **Infinite Memory:** ChocoVine uses "Sub-agents" to handle research. This keeps your main chat context clean so Claude doesn't "forget" instructions halfway through.
*   **You stay in control:** You approve the Plan before a single line of code is written.
*   **Built for scale:** Optimized for mid to large codebases where context management matters most.

## Getting Started

You need [Claude Code](https://claude.ai/claude-code) installed. Then:

```bash
# 1. Clone the repo
git clone https://github.com/vneseyoungster/Vibe-Starter-Pack.git

# 2. Configure your project (tell ChocoVine about your stack)
# Edit the CLAUDE.md file with your specific setup.
```

### First Time Setup

After cloning, run one of these commands to initialize ChocoVine for your codebase:

| Command | When to Use |
| :--- | :--- |
| `/initialize [project-name]` | **New projects** - Sets up ChocoVine structure from scratch |
| `/project-scan` | **Existing codebases** - Scans and documents your project, generates architecture docs |

```bash
# For a new project:
/initialize my-awesome-app

# For an existing codebase:
/project-scan
```

This step helps ChocoVine understand your project structure, patterns, and conventions before you start building features.

---

## How to Use

### The Magic Command
For 95% of tasks, you only need one command. ChocoVine handles the research, testing, and coding automatically.

```bash
/start Add a login page with Google OAuth
```

**What happens next?**
1.  **Research:** Claude reads your existing code.
2.  **Clarify:** It asks you questions (e.g., "Do you want to use Firebase or Auth0?").
3.  **Plan:** It shows you a plan. You type `yes`.
4.  **Test:** It creates a test file that fails (because the code doesn't exist yet).
5.  **Code:** It writes the code to pass the test.

---

### Other Useful Commands

While `/start` does it all, sometimes you need specific tools:

| Command | Description | Use Case |
| :--- | :--- | :--- |
| `/quick-fix [error]` | Focused debugging | Fix a specific typo or NullPointer without running a full plan. |
| `/project-scan` | Auto-Documentation | Generate READMEs, architecture docs, and API references by scanning your project. |
| `/code-check [target]` | Code Review | Review, validate, or audit existing code for issues. |

#### Research Commands

For granular control over the research phase:

| Command | Description | Use Case |
| :--- | :--- | :--- |
| `/research:codebase [topic]` | Understand existing code | "How does the auth system work?" |
| `/research:feature [desc]` | Gather requirements | Start TDD flow with collaborative dialogue |
| `/research:ui [figma-url]` | Figma to Code | Extract CSS, design tokens, and layout from Figma |
| `/research:docs [topic]` | External documentation | Look up library docs, API references |
| `/research:spec [path]` | Generate test spec | Create test specification from requirements |
| `/research:plan [path]` | Architecture planning | Design implementation approach from spec |

---

## The Workflow (Under the Hood)

For the curious, here is how ChocoVine guarantees quality code. We strictly follow the **RSTPIV** loop:

```mermaid
graph LR
    A[Research] --> B[Specify]
    B --> C[Test]
    C --> D[Plan]
    D --> E[Implement]
    E --> F[Validate]
```

1.  **Research:** Sub-agents analyze the codebase structure.
2.  **Specify:** Requirements are gathered and confirmed by you.
3.  **Test:** **(The Secret Sauce)** Failing tests are generated based on specs.
4.  **Plan:** Architecture is decided.
5.  **Implement:** Code is written specifically to pass the tests.
6.  **Validate:** Final security and logic checks.

---

## Why Mid to Large Codebases?

ChocoVine shines on codebases with:
- **Multiple files/modules** where context matters
- **Existing patterns** that new code should follow
- **Test suites** that need to stay green
- **Team conventions** that must be respected

For small scripts or one-off files, you might not need the full workflow. But once your project grows beyond a few hundred lines, ChocoVine prevents the chaos.

---

## Configuration (`CLAUDE.md`)

To get the best results, help ChocoVine understand your project. Edit `CLAUDE.md` in your root directory:

```markdown
# CLAUDE.md
- **Stack:** React, Tailwind, Node.js, PostgreSQL
- **Build Command:** npm run build
- **Test Command:** npm test
- **Style Guide:** Airbnb standard, use arrow functions
```

## License

MIT

---

### Advanced Users (Manual Mode)

<details>
<summary>Click to view granular TDD commands</summary>

If you want step-by-step control over the agent loop, you can run phases individually:

| Phase | Command | Purpose |
| :--- | :--- | :--- |
| 1 | `/research:codebase` | Context gathering |
| 2 | `/research:feature` | Requirements dialogue |
| 3 | `/research:spec` | Test specification |
| 4 | `/generate:tests` | Write failing tests |
| 5 | `/research:plan` | Architecture design |
| 6 | `/execute` | Implementation |
| 7 | `/code-check` | Validation |

</details>
