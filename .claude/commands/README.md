# Slash Commands

7 commands for the complete development workflow.

## Commands

| Command | Purpose | Lines |
|---------|---------|-------|
| `/plan` | Plan feature: scan → requirements → tests → architecture | ~120 |
| `/build` | Build from plan: implement → validate → review | ~100 |
| `/research` | Research: auto-routes to UI/docs/analyze | ~80 |
| `/fix` | Fix bugs: systematic-debugging or sequential-thinking | ~50 |
| `/refactor` | Safe refactoring: dead code, rename, extract, general | ~150 |
| `/init` | Initialize: new project wizard OR scan existing | ~100 |
| `/start` | Full workflow: /plan → /build | ~30 |

---

## Quick Reference

```
New project?        → /init
Existing codebase?  → /init (scans and documents)
New feature?        → /start {feature} OR /plan → /build
Bug fix?            → /fix {problem}
Research topic?     → /research {topic}
Clean up code?      → /refactor clean
Rename/move?        → /refactor rename {symbol}
Extract module?     → /refactor extract {code}
```

---

## Workflow

```
┌─────────┐     ┌───────┐     ┌─────────┐
│  /init  │ ──▶ │ /plan │ ──▶ │ /build  │
└─────────┘     └───────┘     └─────────┘
                    │
         ┌──────────┴──────────┐
         ▼          ▼          ▼
      Scan      Requirements  Architecture
      Codebase  + Tests       + Tasks
```

---

## `/plan {feature}`

**Phases:**
1. **Scan** - Map codebase, find patterns
2. **Requirements** - Adaptive Q&A until clear
3. **Test Spec** - Generate failing tests
4. **Architecture** - Design + task breakdown

**Gates:** Requirements approval, Test spec approval, Architecture approval

**Output:** `plans/sessions/{date}-{slug}/`

---

## `/build {session-path}`

**Phases:**
1. **Read** - Load plan, find code locations
2. **Implement** - Execute tasks, run mapped tests
3. **Validate** - Full test suite, typecheck, lint
4. **Review** - Code review, security audit

**Output:** Implemented code, passing tests, review reports

**Mode:** `--no-plan` for direct implementation

---

## `/research {topic}`

**Auto-detects type:**
- Figma URL → UI research (exports, analyzes with Gemini)
- Library/framework → Documentation research
- Other → Topic analysis

**Force mode:** `--ui`, `--docs`, `--analyze`

---

## `/fix {problem}`

**Routes to:**
- Bug/error → systematic-debugging skill
- Complex reasoning → sequential-thinking skill
- Simple → Direct fix

**Auto-commits** if tests pass.

---

## `/refactor {type}`

**Auto-detects type:**
- `clean` / `dead code` → Dead code cleanup with severity categories
- `rename` / `move` → Symbol refactoring with reference tracking
- `extract` / `split` → Code extraction with dependency analysis
- Other → General refactoring with pattern analysis

**Safety features:**
- Test verification before and after each change
- Automatic rollback on test failure
- User approval gates for risky deletions
- Atomic commits per logical unit

**Output:** `docs/reports/{refactor-type}-analysis.md`

---

## `/init`

**New project:** Interactive wizard
- Project type, tech stack, preferences
- Generates structure, configs, CLAUDE.md

**Existing project:** Scan and document
- Parallel research agents
- Generates docs/, CLAUDE.md

---

## `/start {feature}`

**Thin wrapper:**
1. Entry check (suggests /init if needed)
2. Runs /plan
3. Runs /build
4. Shows summary

**Resume:** `/start --resume {session-path}`

---

## Migration from Old Commands

| Old | New |
|-----|-----|
| `/research:codebase` | `/plan` (Step 2) |
| `/research:feature` | `/plan` (Step 3) |
| `/research:spec` | `/plan` (Step 4) |
| `/research:plan` | `/plan` (Step 6) |
| `/generate:tests` | `/plan` (Step 5) |
| `/execute` | `/build` (Step 2) |
| `/code-check` | `/build` (Step 3-4) |
| `/research:ui` | `/research --ui` |
| `/research:docs` | `/research --docs` |
| `/analyze` | `/research --analyze` |
| `/quick-fix` | `/fix` |
| `/initialize` | `/init` |
| `/project-scan` | `/init` |
