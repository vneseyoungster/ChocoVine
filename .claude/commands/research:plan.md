# Research Plan (Architecture & Implementation)

Create architecture and implementation plan for: $ARGUMENTS

## Overview

This command is **Phase 3** of the research flow. It takes test specifications and creates an architecture and implementation plan to make those tests pass.

**Prerequisite:** `/research:feature` must be completed first (or will be auto-invoked).

**Philosophy:** With tests already written, the implementation plan focuses on HOW to make tests pass. Each task maps directly to specific test cases for clear verification.

---

## Phase Flow Position

```
┌─────────────────────┐
│  /research:codebase │  ← Phase 1
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  /research:feature  │  ← Phase 2 (REQUIRED FIRST)
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   /research:plan    │  ← YOU ARE HERE (Phase 3)
└─────────────────────┘
```

---

## Phase 0: Verify Prerequisites

### Parse Arguments

```
IF $ARGUMENTS contains session path (plans/sessions/...):
  → Mode = FROM_SESSION
  → Load session from specified path
  → Verify test specification phase completed

ELSE IF $ARGUMENTS is task description:
  → Mode = FRESH_START
  → Check if test specification exists for this task
  → IF no tests: Auto-invoke /research:feature first
```

### GATE: Verify Test Specification Complete

Before proceeding, verify:
- [ ] Session directory exists: `plans/sessions/{date}-{task}/`
- [ ] Research findings exist: `research/codebase-map.md`
- [ ] Requirements documented: `specs/requirements.md`
- [ ] Test specification exists: `specs/test-specification.md`
- [ ] Failing test files generated

**If test specification missing:**
```
Test specification not found. Invoking Phase 2 first...
→ /research:feature $ARGUMENTS
```

---

## Phase 1: Load Test Context

### Summarize Test Specification First

**CRITICAL: Use summarize-agent to compress test artifacts before loading into context.**

```
Invoke summarize-agent with:
- plans/sessions/{session}/specs/
- plans/sessions/{session}/research/

This returns a consolidated summary of:
- requirements.md
- test-specification.md
- codebase-map.md
- patterns.md

Use this summary for planning.
```

**Invocation:**
```
Task(summarize-agent, "Summarize: plans/sessions/{session}/specs/ and plans/sessions/{session}/research/")
```

### Read Test Specification (If Needed)

Load specific artifacts only if summary lacks detail:
1. `specs/test-specification.md` - All test cases with IDs
2. `specs/requirements.md` - Requirements traceability
3. `research/patterns.md` - Code patterns to follow

### Extract Test Structure

Compile test information for planning:
- Total test count by category
- Test file locations
- Test IDs grouped by component/module
- Edge cases and error scenarios

---

## Phase 2: Architecture Design

### Invoke Solution Architect

Delegate to `solution-architect` sub-agent to:
- Design high-level solution architecture
- Make technology and pattern decisions
- Map components to test suites
- Identify risks and mitigation strategies

**Input:** Test specification and requirements
**Output:** `plans/sessions/{session}/plans/architecture.md`

### Architecture Document Template

```markdown
# Architecture: [Feature Name]

## Overview
[High-level description based on requirements and tests]

## Test Coverage Summary
- Total Tests: [N]
- Test Suites: [List]
- Coverage Areas: [List]

## Design Decisions

### Decision 1: [Topic]
- **Options Considered:** [list]
- **Selected:** [choice]
- **Rationale:** [reasoning]
- **Tests Affected:** [T1, T2, E1]

## Component Design

### Component: [Name]
- **Responsibility:** [what it does]
- **Location:** [file path]
- **Dependencies:** [list]
- **Interface:** [public API]
- **Tests:** [T1, T2, E1, ERR1] - tests this component must satisfy

## Data Flow
[Sequence diagram or flow description]

## Integration Points
- [Existing code to integrate with]
- [APIs to consume/expose]

## Risks & Mitigations
| Risk | Impact | Mitigation | Related Tests |
|------|--------|------------|---------------|
| ... | ... | ... | [ERR1, ERR2] |

## Constraints
- [Technical constraints]
- [Business constraints from requirements]
```

### Present Architecture for Review

```
ARCHITECTURE REVIEW

## Key Design Decisions
[Summary of major decisions]

## Components → Tests Mapping
| Component | Responsibility | Tests |
|-----------|---------------|-------|
| AuthService | Handle authentication | T1-T5, E1-E3 |
| TokenManager | JWT operations | T6-T10, ERR1-ERR2 |

## Identified Risks
[Risk summary with mitigations]

---
Full architecture document: plans/sessions/{session}/plans/architecture.md
```

### Architecture Approval Gate

**GATE: DO NOT proceed without explicit user approval**

Ask user:
> "Please review the architecture above. Do you approve this design, or do you have changes/questions?"

**If approved:** Proceed to task breakdown
**If changes needed:** Update architecture and present again
**If questions:** Answer questions and present again

---

## Phase 3: Task Breakdown

### Invoke Task Planner

After architecture approval, delegate to `task-planner` sub-agent to:
- Break architecture into atomic tasks
- Add exact file paths and line numbers
- Map each task to specific test IDs
- Define verification as test passing
- Establish dependencies and order

**Output:** `plans/sessions/{session}/plans/implementation.md`

### Implementation Plan Template

```markdown
# Implementation Plan: [Feature Name]

## Summary
- **Total Tasks:** [N]
- **Phases:** [N]
- **Total Tests to Pass:** [N]

## Test-to-Task Mapping Overview

| Test ID | Test Description | Task ID | Status |
|---------|-----------------|---------|--------|
| T1 | should authenticate user | 1.1 | Pending |
| T2 | should return JWT token | 1.2 | Pending |
| E1 | should handle invalid credentials | 1.3 | Pending |

## Phase 1: [Phase Name]

### Task 1.1: [Task Name]
- **File:** `path/to/file.ts`
- **Line:** [N] (or "new file")
- **Action:** Create | Modify | Delete
- **Description:** [What to do]
- **Dependencies:** [Task IDs]
- **Makes Tests Pass:** T1, T2, E1
- **Verification:**
  ```bash
  npm test -- --testNamePattern="T1|T2|E1"
  ```

### Task 1.2: [Task Name]
- **File:** `path/to/file.ts`
- **Line:** [N]
- **Action:** Create | Modify
- **Description:** [What to do]
- **Dependencies:** [1.1]
- **Makes Tests Pass:** T3, T4, ERR1
- **Verification:**
  ```bash
  npm test -- --testNamePattern="T3|T4|ERR1"
  ```

## Phase 2: [Phase Name]
...

## Critical Path
[Tasks that block others, mapped to test groups]

## Verification Strategy

### After Each Task
Run the specific tests for that task:
```bash
npm test -- --testNamePattern="[test IDs]"
```

### After Each Phase
Run all tests for the phase:
```bash
npm test -- path/to/component.test.ts
```

### Final Verification
Run full test suite:
```bash
npm test
```

## Completion Criteria
- [ ] All [N] tests pass
- [ ] No test regressions
- [ ] Build succeeds
- [ ] Lint passes

## Ready for Implementation
This plan is ready for `/execute` to implement.
```

### Present Implementation Plan

```
IMPLEMENTATION PLAN

## Summary
- Total Tasks: [N]
- Phases: [N]
- Tests to Pass: [N]

## Task → Test Mapping
| Task | Description | Tests |
|------|-------------|-------|
| 1.1 | Create auth service | T1, T2, E1 |
| 1.2 | Implement token generation | T3, T4, ERR1 |
| ... | ... | ... |

## Verification
Each task completion is verified by running its mapped tests.
All tests passing = Feature complete.

---
Full implementation plan: plans/sessions/{session}/plans/implementation.md
```

### Plan Approval Gate

**GATE: DO NOT proceed without explicit approval**

Ask user:
> "Please review the implementation plan above. Each task is mapped to specific tests. Ready to proceed to implementation?"

**If approved:** Planning phase complete. Ready for `/execute`
**If changes needed:** Update plan and present again

---

## Phase 4: Complete

### Update Session Tracking

Update `session.md`:
```markdown
**Current Phase:** Planning Complete

## Requirements
- Documented in: specs/requirements.md

## Test Specification
- Documented in: specs/test-specification.md
- Test files generated and failing

## Architecture
- Documented in: plans/architecture.md

## Implementation Plan
- Documented in: plans/implementation.md
- [N] tasks mapped to [M] tests

## Ready For
- `/execute` to implement and make tests pass
```

### Announce Completion

```
PLANNING COMPLETE

Architecture and implementation plan created.

Session: plans/sessions/{date}-{task}/
├── specs/requirements.md       ✓
├── specs/test-specification.md ✓
├── plans/architecture.md       ✓
└── plans/implementation.md     ✓

Task Summary:
- [N] implementation tasks
- [M] tests to satisfy
- Each task maps to specific test IDs

Verification Strategy:
- Complete Task 1.1 → Run tests T1, T2, E1
- Complete Task 1.2 → Run tests T3, T4, ERR1
- All tasks complete → All tests pass

Next Step:
→ /execute [session-path] - Implement and make tests pass
```

---

## Quality Checklist

Before completing this phase:
- [ ] Test specification loaded
- [ ] Requirements understood
- [ ] Architecture document addresses all test suites
- [ ] All major decisions have documented rationale
- [ ] Components map to test groups
- [ ] Risks identified with mitigations
- [ ] Tasks are atomic and verifiable
- [ ] Every task maps to specific test IDs
- [ ] File paths and line numbers specified
- [ ] Dependencies clearly marked
- [ ] Verification commands included
- [ ] User has approved both architecture and plan

---

## Error Handling

### If test specification not found
```
Test specification not found for this task.
Running test specification phase first...
→ Invoking /research:feature
```

### If no failing tests exist
```
WARNING: No failing tests found.
Tests should fail initially (not implemented yet).
Please verify test files were generated correctly.
```

### If architecture doesn't cover all tests
```
Architecture gaps detected:
- Tests T5, T6 not covered by any component

Please update architecture to address all test cases.
```

---

## Example Usage

### From Session Path
```
/research:plan plans/sessions/2024-01-15-auth/

→ Loading test specification...
→ Found: 22 tests in 3 files (all failing)
→ Loading requirements...
→ Designing architecture to satisfy tests...
→ [User approves architecture]
→ Breaking down into implementation tasks...
→ Mapping tasks to tests:
  - Task 1.1 → T1, T2, E1
  - Task 1.2 → T3, T4, ERR1
  - ...
→ [User approves plan]
→ Ready for /execute
```

### From Fresh Start (Auto-chains)
```
/research:plan Add user authentication with JWT tokens

→ No test specification found, running prior phases...
→ /research:codebase Add user authentication with JWT tokens
→ [Research completes]
→ /research:feature [session]
→ [Questions answered, tests generated]
→ Proceeding to architecture design...
→ [Planning continues]
```

---

## Related Commands

| Command | Purpose |
|---------|---------|
| `/research:codebase` | Phase 1: Codebase research |
| `/research:feature` | Phase 2: Requirements & test specification |
| `/execute` | Implementation phase |
| `/code-check` | Validation phase |
