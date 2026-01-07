# Execute Full Workflow

Run complete workflow for: $ARGUMENTS

## Overview

This command orchestrates the full TDD-first workflow. It coordinates all phases with proper gates and user approvals.

---

## Phase 0: First Entrance Check

**Before any work, check project state:**

```
IF no package.json AND no src/ directory AND no .git:
  → Project appears new/empty
  → Suggest: "/initialize [project-name]"
  → Ask user: "This looks like a new project. Would you like to run /initialize first?"

ELSE IF no docs/ directory OR no CLAUDE.md project config:
  → Existing codebase but not documented
  → Suggest: "/project-scan"
  → Ask user: "This codebase hasn't been scanned yet. Would you like to run /project-scan first for better context?"

ELSE:
  → Proceed with workflow
```

**Gate:** User confirms to proceed OR chooses initialization command

---

## Main Workflow Flow

```
┌─────────────────────────────────────────────────────────────────────┐
│                         ENTRY POINTS                                 │
├─────────────────────────────────────────────────────────────────────┤
│  New Project? → /initialize                                          │
│  Existing but undocumented? → /project-scan                          │
│  Has Figma/Design URL? → /research:ui (then return here)            │
│  Want to analyze concept? → /analyze (standalone)                    │
└──────────────────────────────┬──────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    PHASE 1: CODEBASE RESEARCH                        │
│                       /research:codebase                             │
│  • Analyze existing code & patterns                                  │
│  • Map project structure                                             │
│  • Identify integration points                                       │
│  Output: research/codebase-map.md, patterns.md, dependencies.md     │
└──────────────────────────────┬──────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│                 PHASE 2: REQUIREMENTS GATHERING                      │
│                       /research:feature                              │
│  • Brainstorming dialogue with user                                  │
│  • Gather functional & non-functional requirements                   │
│  • Document assumptions and out-of-scope                             │
│  Output: specs/requirements.md                                       │
│  GATE: User must approve requirements                                │
└──────────────────────────────┬──────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│                 PHASE 3: TEST SPECIFICATION                          │
│                       /research:spec                                 │
│  • Map requirements to test cases                                    │
│  • Define happy paths, edge cases, error scenarios                   │
│  • Create traceability matrix                                        │
│  Output: specs/test-specification.md                                 │
│  GATE: User must approve test specification                          │
└──────────────────────────────┬──────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│                  PHASE 4: GENERATE TESTS (TDD)                       │
│                       /generate:tests                                │
│  • Create actual test files from specification                       │
│  • Tests MUST fail initially (no implementation yet)                 │
│  • Verify tests fail correctly (not syntax errors)                   │
│  Output: Test files in project test directory                        │
│  GATE: All tests must fail with "missing implementation"             │
└──────────────────────────────┬──────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│                PHASE 5: IMPLEMENTATION PLANNING                      │
│                       /research:plan                                 │
│  • Design architecture to satisfy tests                              │
│  • Break into atomic tasks with test mappings                        │
│  • Each task specifies which tests it will make pass                 │
│  Output: plans/architecture.md, plans/implementation.md              │
│  GATE: User must approve architecture AND implementation plan        │
└──────────────────────────────┬──────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    PHASE 6: IMPLEMENTATION                           │
│                          /execute                                    │
│  • Execute tasks in order                                            │
│  • Run mapped tests after each task                                  │
│  • Commit after successful task completion                           │
│  • Track progress and handle deviations                              │
│  Output: Implemented code, passing tests                             │
│  GATE: All tasks complete, all tests pass                            │
└──────────────────────────────┬──────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│                      PHASE 7: VALIDATION                             │
│                        /code-check                                   │
│  • Code review (code-reviewer)                                       │
│  • Test verification (test-automator)                                │
│  • Security audit (security-auditor)                                 │
│  • Documentation update (documentation-writer)                       │
│  Output: reviews/*.md, final validation report                       │
│  GATE: All validations pass                                          │
└──────────────────────────────┬──────────────────────────────────────┘
                               │
                               ▼
                          ✓ COMPLETE
```

---

## Execution

### 1. Initialize Session

Create session directory structure:
```
plans/sessions/{date}-{slug}/
├── session.md        # Session tracking
├── research/         # Research artifacts
├── specs/            # Requirements & test specs
├── plans/            # Architecture & tasks
├── reviews/          # Validation reports
└── summary.md        # Final summary (created at end)
```

Initialize session tracking file with:
- Feature description
- Current phase (Research)
- Start timestamp
- Phase progress table

### 2. Detect Special Cases

**Before starting main flow, check for special scenarios:**

```
IF $ARGUMENTS contains Figma URL (figma.com/file or figma.com/design):
  → Invoke /research:ui first
  → Then continue with main flow
  → UI research informs requirements

IF $ARGUMENTS asks to "analyze" or "explain" a concept (not code):
  → Route to /analyze instead
  → This is standalone, not part of implementation flow
```

### 3. Execute Phase Sequence

**CRITICAL: Each phase MUST complete and get approval before the next.**

**Invoke commands in sequence:**

```
Step 1: /research:codebase $ARGUMENTS
        ↓ (wait for completion)

Step 2: /research:feature [session-path]
        ↓ (wait for requirements approval)

Step 3: /research:spec [session-path]
        ↓ (wait for test spec approval)

Step 4: /generate:tests [session-path]
        ↓ (wait for tests to fail correctly)

Step 5: /research:plan [session-path]
        ↓ (wait for architecture + plan approval)

Step 6: /execute [session-path]
        ↓ (wait for all tests to pass)

Step 7: /code-check [session-path]
        ↓ (wait for validations)

Done: Generate summary
```

### 4. Context Efficiency

**Before reading any referenced files/artifacts, invoke summarize-agent:**

```
IF user references files (e.g., "@/research", "based on the plan"):
  → Task(summarize-agent, "Summarize: [referenced paths]")
  → Use returned summary for context
  → Only read full content if specific details missing
```

This reduces context usage by ~70% while preserving essential information.

---

## User Interaction Points

| Phase | Interaction | Required |
|-------|-------------|----------|
| Phase 0 | Confirm project state | If new/undocumented |
| Phase 2 | Answer clarifying questions | Yes |
| Phase 2 | Approve requirements | Yes |
| Phase 3 | Approve test specification | Yes |
| Phase 5 | Approve architecture | Yes |
| Phase 5 | Approve implementation plan | Yes |
| Phase 7 | Acknowledge validation results | Yes |

---

## Decision Tree for Entry

```
START
  │
  ├─ Is codebase new/empty?
  │    YES → Ask: "Run /initialize first?"
  │           User says yes → /initialize
  │           User says no → Continue
  │
  ├─ Is codebase undocumented?
  │    YES → Ask: "Run /project-scan first?"
  │           User says yes → /project-scan
  │           User says no → Continue
  │
  ├─ Does request contain Figma URL?
  │    YES → Run /research:ui [url] first
  │         → Continue with enhanced UI context
  │
  ├─ Is request asking to analyze/explain a concept?
  │    YES → Route to /analyze [topic]
  │         → END (standalone command)
  │
  └─ DEFAULT → Execute Phase 1-7 sequence
```

---

## Abort Handling

If user requests abort:
1. Save current state to session.md
2. Document last completed action
3. Create resume instructions in session directory
4. Provide command to resume later

```
Session aborted at Phase [N].

To resume:
→ /start --resume plans/sessions/{session}/

Or continue manually:
→ /research:feature plans/sessions/{session}/  (if stopped at Phase 1)
→ /research:spec plans/sessions/{session}/     (if stopped at Phase 2)
→ /generate:tests plans/sessions/{session}/    (if stopped at Phase 3)
→ /research:plan plans/sessions/{session}/     (if stopped at Phase 4)
→ /execute plans/sessions/{session}/           (if stopped at Phase 5)
→ /code-check plans/sessions/{session}/        (if stopped at Phase 6)
```

---

## Resume Handling

If resuming interrupted session:
1. Load session.md to determine state
2. Identify last completed phase
3. Verify artifacts exist
4. Continue from appropriate point
5. Ask user to confirm resume point

---

## Phase Indicators

- 🔍 Phase 1: Codebase Research
- 📋 Phase 2: Requirements Gathering
- 📝 Phase 3: Test Specification
- 🧪 Phase 4: Test Generation
- 🏗️ Phase 5: Implementation Planning
- 🔨 Phase 6: Implementation
- ✅ Phase 7: Validation
- ✓ Complete

---

## Error Handling

| Error Type | Action |
|------------|--------|
| New project detected | Suggest /initialize |
| Undocumented codebase | Suggest /project-scan |
| Research fails | Document gap, ask user for guidance |
| User declines requirements | Revise based on feedback |
| User declines test spec | Revise based on feedback |
| Tests pass immediately | Warning - tests should fail first |
| User declines plan | Revise based on feedback |
| Implementation fails | Document issue, attempt recovery |
| Tests fail after implementation | Return to implementation, fix issues |
| Validation fails | Return to implementation, fix issues |
| Critical blocker | Pause workflow, escalate to user |

---

## Session Artifacts

All workflow artifacts are preserved:

| Artifact | Location | Phase |
|----------|----------|-------|
| Session tracking | `session.md` | All |
| Codebase map | `research/codebase-map.md` | 1 |
| Patterns | `research/patterns.md` | 1 |
| Dependencies | `research/dependencies.md` | 1 |
| Requirements | `specs/requirements.md` | 2 |
| Test specification | `specs/test-specification.md` | 3 |
| Test files | Project test directory | 4 |
| Architecture | `plans/architecture.md` | 5 |
| Implementation plan | `plans/implementation.md` | 5 |
| Code review | `reviews/code-review.md` | 7 |
| Test report | `reviews/test-report.md` | 7 |
| Security audit | `reviews/security-audit.md` | 7 |
| Final summary | `summary.md` | 7 |

---

## Completion

Generate final summary:
- What was built
- Key decisions made
- Files changed
- All tests passing
- Validation results
- Known limitations
- Follow-up items

Update session status to COMPLETE.

Present results to user.

```
WORKFLOW COMPLETE ✓

Session: plans/sessions/{date}-{task}/

## Summary
[Brief description of what was built]

## Phases Completed
- ✓ Phase 1: Codebase Research
- ✓ Phase 2: Requirements (N functional, M non-functional)
- ✓ Phase 3: Test Specification (X test cases)
- ✓ Phase 4: Tests Generated (X failing → X passing)
- ✓ Phase 5: Architecture & Plan (Y tasks)
- ✓ Phase 6: Implementation
- ✓ Phase 7: Validation

## Test Results
- Total: X tests
- Passing: X
- Coverage: Y%

## Files Changed
- [list of modified/created files]

## Validation Status
- Code Review: ✓ PASS
- Tests: ✓ PASS
- Security: ✓ PASS
- Documentation: ✓ Updated

## Next Steps
- [Any follow-up recommendations]
```

---

## Related Commands

| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/initialize` | Initialize new project | Empty/new codebase |
| `/project-scan` | Scan & document codebase | Existing but undocumented |
| `/research:codebase` | Phase 1 standalone | Manual flow |
| `/research:feature` | Phase 2 standalone | Manual flow |
| `/research:spec` | Phase 3 standalone | Manual flow |
| `/generate:tests` | Phase 4 standalone | Manual flow |
| `/research:plan` | Phase 5 standalone | Manual flow |
| `/execute` | Phase 6 standalone | Manual flow |
| `/code-check` | Phase 7 standalone | Manual flow |
| `/research:ui` | UI design research | Figma/design URLs |
| `/analyze` | Topic analysis | Concepts, not code |
| `/quick-fix` | Quick fixes | Small, known problems |
