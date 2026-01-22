# Plan

Plan feature implementation: $ARGUMENTS

---

## Step 1: Initialize Session

Create session at `plans/sessions/{date}-{slug}/`:
```
session.md          # Tracking
research/           # Codebase findings
specs/              # Requirements + test spec
plans/              # Architecture + tasks
```

Initialize `session.md` with: Task description, start time, current phase.

---

## Step 2: Codebase Scan

**Launch parallel agents:**

```
Task(codebase-explorer, "
  Map structure, entry points, key files for: $ARGUMENTS
  Output: {session}/research/codebase-map.md
", run_in_background=true)

Task(pattern-researcher, "
  Find naming conventions, patterns, testing approach for: $ARGUMENTS
  Output: {session}/research/patterns.md
", run_in_background=true)
```

Wait for agents. Summarize findings.

**Output:** `research/codebase-map.md`, `research/patterns.md`

---

## Step 3: Requirements Gathering

**Use brainstorming skill for adaptive questioning.**

Ask ONE question at a time. Offer 2-4 concrete options when possible.

**Question flow:**
1. "What problem does this solve?"
2. "Who uses this and how?"
3. "What's the scope for v1?"
4. "Any technical constraints?"

**Continue until:** All blocking questions answered + user confirms requirements.

**Write to:** `specs/requirements.md`
```markdown
# Requirements: {feature}

## Functional
- FR1: {requirement}
- FR2: {requirement}

## Non-Functional
- NFR1: {requirement}

## Out of Scope
- {explicitly excluded}

## Open Questions
- {if any remain}
```

**GATE:** User must approve requirements before proceeding.

---

## Step 4: Test Specification

**Invoke test-spec-generator:**

```
Task(test-spec-generator, "
  Generate test specification from requirements.

  Input: {session}/specs/requirements.md
  Patterns: {session}/research/patterns.md

  Map each requirement to test cases:
  - Happy paths
  - Edge cases
  - Error scenarios

  Output: {session}/specs/test-specification.md
")
```

**Test Spec Format:**
```markdown
# Test Specification

## Coverage Matrix
| Req ID | Test IDs | Description |
|--------|----------|-------------|
| FR1 | T1, T2, E1 | ... |

## Test Cases
### T1: {test name}
- **Requirement:** FR1
- **Given:** {precondition}
- **When:** {action}
- **Then:** {expected}
```

**GATE:** User must approve test specification.

---

## Step 5: Generate Failing Tests

**Invoke test-automator to write actual test files:**

```
Task(test-automator, "
  Generate failing test files from specification.

  Input: {session}/specs/test-specification.md
  Patterns: {session}/research/patterns.md

  - Use project's test framework
  - Follow existing test patterns
  - Tests MUST fail (no implementation yet)

  Output: Test files in project test directory
")
```

**Verify tests fail correctly:**
```bash
npm test 2>&1 | grep -E "(FAIL|Error)" | head -20
```

Tests should fail with "not implemented" or "undefined", NOT syntax errors.

---

## Step 6: Architecture & Tasks

**Invoke solution-architect:**

```
Task(solution-architect, "
  Design architecture to make tests pass.

  Inputs:
  - {session}/specs/test-specification.md
  - {session}/research/patterns.md

  Output: {session}/plans/architecture.md
")
```

**Then invoke task-planner:**

```
Task(task-planner, "
  Break architecture into atomic tasks.

  Each task must specify:
  - File path and line numbers
  - What tests it makes pass
  - Verification command

  Output: {session}/plans/implementation.md
")
```

**GATE:** User must approve architecture and implementation plan.

---

## Completion

```
PLANNING COMPLETE

Session: plans/sessions/{date}-{slug}/
├── research/codebase-map.md    ✓
├── research/patterns.md        ✓
├── specs/requirements.md       ✓
├── specs/test-specification.md ✓
├── plans/architecture.md       ✓
└── plans/implementation.md     ✓

Tests: {N} failing (ready to implement)
Tasks: {M} mapped to tests

Next: /build {session-path}
```

---

## On Failure

If interrupted, save progress to `session.md`:
```markdown
## Progress
- [x] Codebase scan
- [x] Requirements (approved)
- [ ] Test specification ← STOPPED HERE
- [ ] Architecture
- [ ] Tasks

Resume: /plan --resume {session-path}
```

---

## Resume

```
IF $ARGUMENTS contains --resume:
  → Load session.md
  → Find last completed phase
  → Continue from next phase
```
