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
  Find code locations for task:

  Session: {session-path}
  Task: {task-description}

  Research Context:
  - Patterns: {session}/research/patterns.md
  - Architecture: {session}/plans/architecture.md

  Return:
  - Files to modify with line numbers
  - Patterns to follow
  - Proposed changes (description only)
  - Verification commands
")
```

### Collect Findings Report

The sub-agent returns:
- `Files to Modify` - Exact file:line locations
- `Patterns Found` - Existing code patterns to follow
- `Proposed Changes` - Description of what needs to change
- `Verification Commands` - How to test

---

## Step 3: Execute Implementation

**Main agent implements based on findings.**

### Implementation Steps

For each item in Findings Report:

1. **Read** the target file
2. **Apply** changes using Edit tool
3. **Follow** patterns identified by sub-agent
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
│     - Locate files and lines                    │
│     - Document patterns                         │
│     - Describe changes needed                   │
└──────────────────────┬──────────────────────────┘
                       ▼
┌─────────────────────────────────────────────────┐
│  3. EXECUTE (main agent)                        │
│     - Apply changes using Edit tool             │
│     - Follow identified patterns                │
│     - Run verification                          │
│     - Commit changes                            │
└──────────────────────┬──────────────────────────┘
                       ▼
┌─────────────────────────────────────────────────┐
│  4. REPEAT steps 2-3 for all tasks              │
└──────────────────────┬──────────────────────────┘
                       ▼
┌─────────────────────────────────────────────────┐
│  5. REVIEW (via review-generator)               │
│     - Scan all changes                          │
│     - Generate review document                  │
└──────────────────────┬──────────────────────────┘
                       ▼
┌─────────────────────────────────────────────────┐
│  6. COMPLETE                                    │
│     → /code-check {session-path}                │
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
