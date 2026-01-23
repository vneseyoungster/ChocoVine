# Plan

Create plan from research: $ARGUMENTS

---

## Step 1: Load Research

IF $ARGUMENTS contains session path:
  → Load from specified path
ELSE:
  → Find latest session with research/requirements.md

Read:
- {session}/research/requirements.md
- {session}/research/patterns.md

IF no research session found:
  → Prompt user: "No research session found. Options:
    A) Specify a session path
    B) Run /cv:research first
    C) Cancel"

---

## Step 2: Detect Plan Type

Analyze requirements for keywords:

| Pattern | Plan Type |
|---------|-----------|
| "test", "TDD", "spec" | test-spec |
| "feature", "implement", "add" | implementation |
| "bug", "fix", "error" | fix |
| "refactor", "clean", "extract" | refactor |

---

## Step 3: Architecture Design

Task(solution-architect, "
  Design architecture for: {requirements summary}
  Patterns to follow: {from patterns.md}
  Output: {session}/plans/architecture.md
")

**Output:** {session}/plans/architecture.md

**GATE 1:** Present architecture to user for approval.
- Show key design decisions
- Show component structure
- Show data flow

IF user requests changes:
  → Revise and re-present
ELSE:
  → Proceed to Step 4

---

## Step 4: Task Breakdown

Task(task-planner, "
  Break down architecture into atomic tasks.
  Architecture: {session}/plans/architecture.md
  Output: {session}/plans/tasks.md

  For each task include:
  - File paths and line numbers
  - Dependencies on other tasks
  - Acceptance criteria
")

**Output:** {session}/plans/tasks.md

**GATE 2:** Present task breakdown to user for approval.
- Show task list with dependencies
- Show estimated complexity
- Show critical path

IF user requests changes:
  → Revise and re-present
ELSE:
  → Proceed to Step 5

---

## Step 5: Test Specifications

Task(test-spec-generator, "
  Generate test specifications for tasks.
  Tasks: {session}/plans/tasks.md
  Requirements: {session}/research/requirements.md
  Output: {session}/plans/test-specs.md

  For each test include:
  - Given/When/Then format
  - Edge cases
  - Map to task ID
")

**Output:** {session}/plans/test-specs.md

**GATE 3:** Present test specifications to user for approval.
- Show test coverage mapping
- Show edge cases identified
- Show acceptance criteria alignment

IF user requests changes:
  → Revise and re-present
ELSE:
  → Planning complete

---

## Completion

PLAN COMPLETE

Session: {session-path}
Plan Type: {type}

## Plan Files
- plans/architecture.md
- plans/tasks.md
- plans/test-specs.md

## Summary
{plan overview}

## Approvals
- Architecture: APPROVED
- Tasks: APPROVED
- Test Specs: APPROVED

## Next Command
Run `/cv:build` to implement the plan

---

## On Failure

If interrupted, save progress to `session.md`:
```markdown
## Progress
- [x] Load research
- [x] Detect plan type
- [x] Architecture (approved)
- [ ] Task breakdown ← STOPPED HERE
- [ ] Test specifications

Resume: /cv:plan --resume {session-path}
```

---

## Resume

```
IF $ARGUMENTS contains --resume:
  → Load session.md
  → Find last completed phase
  → Continue from next phase
```
