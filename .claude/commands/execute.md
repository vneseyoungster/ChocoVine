# Execute Implementation

Execute implementation plan for: $ARGUMENTS

---

## Step 1: Load Implementation Plan

### Locate Plan

```
IF $ARGUMENTS contains plan path (plans/sessions/.../plans/implementation.md):
  → Use specified plan path

ELSE IF $ARGUMENTS contains session path (plans/sessions/...):
  → Use: {session}/plans/implementation.md

ELSE:
  → Find latest session: plans/sessions/*/plans/implementation.md
  → Use most recent by date
```

### Summarize Plan

**Use summarize-agent to reduce context usage:**

```
Task(summarize-agent, "
  Summarize: {plan-path}

  Focus on:
  - Task list with dependencies
  - File paths and operations
  - Verification commands
  - Session context path
")
```

Extract from summary:
- Ordered task list
- Dependencies between tasks
- Session path for context

---

## Step 2: For Each Task - Code Finding

**DO NOT implement anything yet. Find code locations first.**

### Invoke Full-Stack Developer

For each task, invoke the code finder:

```
Task(full-stack-developer, "
  Session: {session-path}
  Task: {task-description}

  Context:
  - Patterns: {session}/research/patterns.md
  - Architecture: {session}/plans/architecture.md

  Output to: {session}/code-changes/{task-slug}.md
")
```

### Collect Findings

The sub-agent writes to `{session}/code-changes/{task-slug}.md`:

```markdown
# {task-name}

## Purpose
[Why this change - from implementation plan]

## Changes

### `{file-path}`
**Summary:** [What this file does]

| Lines | Action | Description |
|-------|--------|-------------|
| {n}-{m} | {Add|Modify|Remove} | {What to change} |

**Pattern:** Follow `{similar-file}:{lines}`

## Verification
`{commands}`
```

---

## Step 3: Execute Implementation

**Main agent implements based on code-changes documentation.**

### Implementation Steps

For each file in `{session}/code-changes/{task-slug}.md`:

1. **Read** the changes doc for file summary and locations
2. **Read** the target source file at documented lines
3. **Apply** changes using Edit tool, following referenced patterns
4. **Verify** after each change:
   ```bash
   npm run typecheck
   npm run lint
   ```

### Commit After Logical Units

After completing a related group of changes:

```bash
git add {changed-files}
git commit -m "{descriptive-message}"
```

### If Implementation Issue

```
Encountered issue implementing: {task}
Error: {error-details}

Option
1. Retry with different approach

```

---

## Step 4: Repeat for All Tasks

```
FOR each task in plan:
  1. Invoke full-stack-developer (findings)
  2. Execute implementation
  3. Verify changes
  4. Commit if successful

UNTIL all tasks complete
```

### Handle Dependencies

- Tasks with no dependencies: Can be batched
- Tasks with dependencies: Wait for predecessors
- Track completed tasks for dependency resolution

---

## Step 5: Generate Review

**After all tasks complete, invoke review-generator:**

```
Task(review-generator, "
  Generate implementation review for:

  Session: {session-path}
  Plan: {plan-path}

  Output to: {session}/reviews/implementation-review.md
")
```

The review-generator will:
- Scan all changes made
- Compare against original plan
- Run verification commands
- Generate structured review document

---

## Step 6: Announce Completion

```
IMPLEMENTATION COMPLETE

Session: {session-path}
Tasks: {completed}/{total}

Review: plans/sessions/{session}/reviews/implementation-review.md

Next: /code-check {session-path}
```

---

## Workflow Summary

```
┌─────────────────────────────────────────────────┐
│  1. LOAD PLAN (via summarize-agent)             │
└──────────────────────┬──────────────────────────┘
                       ▼
┌─────────────────────────────────────────────────┐
│  2. FIND CODE (via full-stack-developer)        │
│     → Write to: {session}/code-changes/{task}.md│
└──────────────────────┬──────────────────────────┘
                       ▼
┌─────────────────────────────────────────────────┐
│  3. EXECUTE (main agent)                        │
│     - Read changes doc                          │
│     - Apply changes, follow patterns            │
│     - Verify and commit                         │
└──────────────────────┬──────────────────────────┘
                       ▼
┌─────────────────────────────────────────────────┐
│  4. REPEAT steps 2-3 for all tasks              │
└──────────────────────┬──────────────────────────┘
                       ▼
┌─────────────────────────────────────────────────┐
│  5. REVIEW (via review-generator)               │
└──────────────────────┬──────────────────────────┘
                       ▼
┌─────────────────────────────────────────────────┐
│  6. COMPLETE → /code-check {session-path}       │
└─────────────────────────────────────────────────┘
```

---

## Related Commands

| Command | Purpose |
|---------|---------|
| `/research:codebase` | Phase 1: Codebase research |
| `/research:plan` | Phase 2: Architecture & planning |
| `/research:feature` | Phase 3: Test specification |
| `/code-check` | Validation phase |
