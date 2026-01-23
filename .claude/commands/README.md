# Slash Commands

7 commands for the complete development workflow.

## Commands

| Command | Purpose | Lines |
|---------|---------|-------|
| `/cv:research` | Research: gather context, requirements, resolve conflicts | ~150 |
| `/cv:plan` | Plan: architecture, tasks, test specs (from research) | ~100 |
| `/cv:build` | Build: implement tasks, validate, generate manual test instructions | ~120 |
| `/cv:review` | Review: code quality, security audit, coverage check | ~120 |
| `/cv:fix` | Fix bugs: systematic-debugging or sequential-thinking | ~50 |
| `/cv:refactor` | Safe refactoring: dead code, rename, extract, general | ~150 |
| `/cv:init` | Initialize: new project wizard OR scan existing | ~100 |

---

## Quick Reference

```
New project?        -> /cv:init
Existing codebase?  -> /cv:init (scans and documents)
New feature?        -> /cv:research -> /cv:plan -> /cv:build -> [test] -> /cv:review
Bug fix?            -> /cv:fix {problem}
Research topic?     -> /cv:research {topic}
Clean up code?      -> /cv:refactor clean
Rename/move?        -> /cv:refactor rename {symbol}
Extract module?     -> /cv:refactor extract {code}
```

---

## Workflow

```
┌─────────────┐   ┌──────────┐   ┌────────────┐   ┌────────┐   ┌─────────────┐
│/cv:research │-->│ /cv:plan │-->│ /cv:build  │-->│ [test] │-->│ /cv:review  │
└─────────────┘   └──────────┘   └────────────┘   └────────┘   └─────────────┘
      │                │               │               │               │
      v                v               v               v               v
   research/        plans/        code-changes/    (manual)       reviews/
   - findings       - architecture  - task docs      npm test     - code-review
   - patterns       - tasks         build-complete                - security
   - requirements   - test-specs                                  - coverage
```

---

## `/cv:research {topic}`

**Purpose:** Gather context and requirements before planning

**Phases:**
1. **Initialize** - Create session folder structure
2. **Scan** - Parallel agents map codebase and patterns
3. **Clarify** - Adaptive Q&A with user (one question at a time)
4. **Resolve** - Handle pattern conflicts (block until resolved)
5. **Consolidate** - Write requirements.md

**Completeness Check:** Scope, success criteria, constraints, patterns, no conflicts

**Output:** `plans/sessions/{date}-{slug}/research/`

**Modes:** `--resume`, `--ui {figma-url}`, `--docs {library}`

---

## `/cv:plan {session-path}`

**Purpose:** Create implementation plan from research

**Phases:**
1. **Load** - Read research/requirements.md and patterns.md
2. **Detect** - Determine plan type (feature, fix, refactor, test-spec)
3. **Architecture** - solution-architect designs structure (GATE 1)
4. **Tasks** - task-planner breaks down into atomic tasks (GATE 2)
5. **Test Specs** - test-spec-generator creates test cases (GATE 3)

**Gates:** Each phase requires user approval before proceeding

**Output:** `{session}/plans/` (architecture.md, tasks.md, test-specs.md)

---

## `/cv:build {session-path}`

**Purpose:** Implement the plan

**Phases:**
1. **Load** - Read plans/tasks.md
2. **Execute** - For each task: find code, implement, inline validate (lint/typecheck)
3. **Validate** - Full build check (no auto-test)
4. **Summary** - Generate build-complete.md with manual test instructions

**Inline Validation:** Lint + typecheck after each file change

**Output:** `{session}/build-complete.md`, `{session}/code-changes/`

**Mode:** `--no-plan` for direct implementation

---

## `/cv:review {session-path}`

**Purpose:** Validate changes before merge

**Phases:**
1. **Load** - Find session with build-complete.md
2. **Validate** - Parallel agents: code-reviewer, security-auditor, test-automator
3. **Consolidate** - Most-severe-wins recommendation logic

**Coverage Gate:** 80% minimum (hard gate)

**Recommendation Levels:**
- APPROVE: Ready to merge
- APPROVE WITH CHANGES: Minor issues
- REQUEST CHANGES: Significant issues or coverage < 80%

**Output:** `{session}/reviews/` (code-review.md, security-audit.md, coverage-report.md, review.md)

---

## `/cv:fix {problem}`

**Routes to:**
- Bug/error -> systematic-debugging skill
- Complex reasoning -> sequential-thinking skill
- Simple -> Direct fix

**Auto-commits** if tests pass.

---

## `/cv:refactor {type}`

**Auto-detects type:**
- `clean` / `dead code` -> Dead code cleanup with severity categories
- `rename` / `move` -> Symbol refactoring with reference tracking
- `extract` / `split` -> Code extraction with dependency analysis
- Other -> General refactoring with pattern analysis

**Safety features:**
- Test verification before and after each change
- Automatic rollback on test failure
- User approval gates for risky deletions
- Atomic commits per logical unit

**Output:** `docs/reports/{refactor-type}-analysis.md`

---

## `/cv:init`

**New project:** Interactive wizard
- Project type, tech stack, preferences
- Generates structure, configs, CLAUDE.md

**Existing project:** Scan and document
- Parallel research agents
- Generates docs/, CLAUDE.md

---

## Migration from /start

The `/start` command has been removed. Use this workflow instead:

```
OLD: /start {feature}

NEW:
1. /cv:research {feature}  - Gather context and requirements
2. /cv:plan                - Create architecture, tasks, test specs
3. /cv:build               - Implement the plan
4. npm test                - Run tests manually
5. /cv:review              - Validate changes
```

**Why the change?**
- Separation of concerns: each command has one job
- User control: approve each phase before proceeding
- Flexibility: resume at any phase, skip phases if needed
- Visibility: clear artifacts at each stage

---

## Session Folder Structure

```
plans/sessions/{date}-{slug}/
├── session.md              # Progress tracking
├── research/
│   ├── codebase-findings.md
│   ├── patterns.md
│   └── requirements.md
├── plans/
│   ├── architecture.md
│   ├── tasks.md
│   └── test-specs.md
├── code-changes/
│   └── {task-slug}.md
├── reviews/
│   ├── code-review.md
│   ├── security-audit.md
│   ├── coverage-report.md
│   └── review.md
└── build-complete.md
```
