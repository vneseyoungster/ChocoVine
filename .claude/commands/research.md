# Research, Question & Plan

Research for: $ARGUMENTS

## Overview

The `/research` command is a **router** that directs to specialized research modes. Each mode is optimized for different research needs and follows a sequential workflow.

---

## Research Flow

The research phase follows this sequential flow for implementation tasks (TDD approach):

```
┌─────────────────────┐
│  /research:codebase │  ← Phase 1: Understand existing code & patterns
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  /research:feature  │  ← Phase 2: Requirements & test specification (TDD)
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   /research:plan    │  ← Phase 3: Architecture & implementation planning
└─────────────────────┘
```

**Standalone modes** (not part of sequential flow):
- `/research:ui` - Figma design research
- `/research:docs` - External documentation research

---

## Research Modes

| Command | Purpose | Use When |
|---------|---------|----------|
| `/research:codebase` | Analyze codebase for relevant code & patterns | First step - understanding existing code |
| `/research:feature` | Gather requirements & generate test specs (TDD) | After codebase research, define expected behavior |
| `/research:plan` | Build architecture & implementation plan | After tests written, plan to make them pass |
| `/research:ui` | Research Figma designs | Building UI from designs |
| `/research:docs` | Research external documentation | Learning libraries, finding best practices |

---

## Sequential Flow Commands

### Phase 1: `/research:codebase [task]`
**Purpose**: Analyze your codebase to understand relevant code and patterns

**Example:**
```bash
/research:codebase Add user authentication with JWT tokens
```

**What it does:**
- Maps project structure
- Identifies existing patterns and conventions
- Analyzes relevant modules and dependencies
- Documents coding standards in use
- Identifies integration points

**Output:** Session in `plans/sessions/{date}-{task}/research/`

---

### Phase 2: `/research:feature [task]` or `/research:feature [session-path]`
**Purpose**: Gather requirements and generate test specifications (TDD approach)

**Example:**
```bash
# Fresh start - will run codebase research first
/research:feature Add user authentication with JWT tokens

# From existing session - uses prior research
/research:feature plans/sessions/2024-01-15-auth/
```

**What it does:**
- Reviews codebase research findings
- Engages in brainstorming dialogue with user
- Generates clarifying questions (prioritized)
- Creates requirements document
- Identifies test scenarios from requirements
- Brainstorms edge cases and error conditions
- Generates executable failing test files
- Verifies tests fail correctly (not syntax errors)

**Why use it:**
- Writing tests first forces thinking about edge cases BEFORE implementation
- Tests define SHOULD behavior, preventing "testing around bugs"
- Each passing test = verified progress

**Output:** Requirements + test specs in `plans/sessions/{date}-{task}/specs/` + test files in project

---

### Phase 3: `/research:plan [task]` or `/research:plan [session-path]`
**Purpose**: Build architecture and implementation plan to make tests pass

**Example:**
```bash
# Fresh start - will run full research flow first
/research:plan Add user authentication with JWT tokens

# From existing session - uses prior test specification
/research:plan plans/sessions/2024-01-15-auth/
```

**What it does:**
- Reviews test specification and requirements
- Designs architecture to satisfy tests
- Maps components to test suites
- Creates implementation plan with explicit test mappings
- Each task references which tests it will make pass
- Identifies risks and mitigations

**Why use it:**
- Architecture is designed to satisfy tests, not the other way around
- Each implementation task has clear verification (specific tests)
- Task completion is objectively measured by passing tests

**Output:** Architecture plan in `plans/sessions/{date}-{task}/plans/` (with test mappings)

---

## Standalone Commands

### `/research:ui [figma-url]`
**Purpose**: Extract and document UI designs from Figma

**Example:**
```bash
/research:ui https://www.figma.com/file/ABC123/Dashboard?node-id=1-234
```

**What it does:**
- Exports design assets
- Analyzes layout structure
- Extracts design tokens (colors, typography, spacing)
- Documents component specifications
- Generates CSS code

**Output:** Research in `plans/research/ui/{date}-{design}/`

---

### `/research:docs [topic]`
**Purpose**: Research external documentation and libraries

**Example:**
```bash
/research:docs How to use Expo with React Native
```

**What it does:**
- Searches llms.txt via context7.com
- Analyzes GitHub repositories
- Aggregates documentation
- Produces comprehensive report

**Output:** Research in `plans/research/docs/{date}-{topic}/`

---

## Mode Selection Guide

```
What are you researching?
    │
    ├── Implementation task (new feature, refactor, etc.)
    │   │
    │   ├── Need to understand existing code first?
    │   │   └── Use /research:codebase
    │   │
    │   ├── Have codebase understanding, need requirements & tests?
    │   │   └── Use /research:feature
    │   │
    │   └── Have tests, need implementation plan?
    │       └── Use /research:plan
    │
    ├── UI/UX designs (Figma)
    │   └── Use /research:ui
    │
    └── External libraries/frameworks
        └── Use /research:docs
```

---

## Default Behavior

If you run `/research` without a mode specifier:

1. **Figma URL detected** → Routes to `/research:ui`
2. **Library/framework keywords** → Routes to `/research:docs`
3. **Session/plan path provided** → Routes to appropriate next phase
4. **Implementation task** → Routes to `/research:codebase` (Phase 1)

### Auto-Chaining

Each command in the sequential flow can auto-invoke prior phases if needed:

- `/research:feature` without prior codebase research → runs `/research:codebase` first
- `/research:plan` without prior tests → runs `/research:codebase` then `/research:feature` first

This ensures research artifacts are always available for later phases.

---

## Examples

### Sequential Flow (Full)
```bash
# Phase 1: Understand codebase
/research:codebase Implement dark mode toggle

# Phase 2: Gather requirements & generate tests
/research:feature plans/sessions/2024-01-15-darkmode/

# Phase 3: Create architecture & implementation plan
/research:plan plans/sessions/2024-01-15-darkmode/
```

### Sequential Flow (Shortcut)
```bash
# Jump straight to planning - auto-runs Phase 1 & 2
/research:plan Add user registration with email verification
```

### UI Research
```bash
/research:ui https://www.figma.com/file/ABC123/LoginScreen
/research:ui https://www.figma.com/design/XYZ789/Dashboard?node-id=0-1
```

### Documentation Research
```bash
/research:docs How to setup Prisma with Next.js 14
/research:docs Compare Zustand vs Jotai for state management
/research:docs React Query v5 caching strategies
```

---

## Combining Research Modes

For complex features, combine sequential flow with standalone modes:

**Example: Building a new dashboard feature**

```bash
# 1. Research the UI design (standalone)
/research:ui https://www.figma.com/file/ABC123/Dashboard

# 2. Research the charting library (standalone)
/research:docs Recharts vs Chart.js for React dashboards

# 3. Run sequential flow for implementation
/research:codebase Implement dashboard with analytics charts
/research:feature plans/sessions/2024-01-15-dashboard/
/research:plan plans/sessions/2024-01-15-dashboard/
```

---

## Workflow Integration

Research commands integrate with the RQPIV workflow (TDD approach):

```
/research:codebase  → Phase 1: Codebase Research
      ↓
/research:feature   → Phase 2: Requirements & Test Specification (TDD)
      ↓
/research:plan      → Phase 3: Architecture & Planning (to make tests pass)
      ↓
/execute            → Implementation phase
      ↓
/code-check         → Validation phase
```

Or use `/start` for the full automated workflow.

---

## Related Commands

| Command | Purpose |
|---------|---------|
| `/start` | Full workflow (Research → Execute → Validate) |
| `/execute` | Implementation phase |
| `/code-check` | Validation phase |
| `/quick-fix` | Fast fixes without full workflow |
| `/project-scan` | Generate codebase documentation |
