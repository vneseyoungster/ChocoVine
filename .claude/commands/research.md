# Research, Question & Plan

Research for: $ARGUMENTS

## Overview

The `/research` command is a **router** that directs to specialized research modes. Each mode is optimized for different research needs.

---

## Research Modes

| Command | Purpose | Use When |
|---------|---------|----------|
| `/research:codebase` | Analyze codebase for implementation | Implementing features, fixing bugs, refactoring |
| `/research:ui` | Research Figma designs | Building UI from designs, extracting design tokens |
| `/research:docs` | Research external documentation | Learning libraries, finding best practices, comparing tools |

---

## Quick Reference

### `/research:codebase [task]`
**Purpose**: Analyze your codebase to plan implementation

**Example:**
```bash
/research:codebase Add user authentication with JWT tokens
```

**What it does:**
- Maps project structure
- Identifies patterns and conventions
- Analyzes relevant modules
- Generates clarifying questions
- Creates architecture plan
- Produces implementation tasks

**Output:** Session in `plans/sessions/{date}-{task}/`

---

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
    |
    ├── Your own codebase
    │   └── Use /research:codebase
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
3. **Implementation task** → Routes to `/research:codebase`

---

## Examples

### Codebase Research
```bash
/research:codebase Implement dark mode toggle
/research:codebase Add API rate limiting
/research:codebase Refactor authentication module
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

For complex features, you may need multiple research modes:

**Example: Building a new dashboard feature**

```bash
# 1. Research the UI design
/research:ui https://www.figma.com/file/ABC123/Dashboard

# 2. Research the charting library
/research:docs Recharts vs Chart.js for React dashboards

# 3. Research codebase for implementation
/research:codebase Implement dashboard with analytics charts
```

---

## Workflow Integration

Research commands integrate with the RQPIV workflow:

```
/research:*        → Research & Question phases
     ↓
/execute           → Implementation phase
     ↓
/code-check        → Validation phase
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
