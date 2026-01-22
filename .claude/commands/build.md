# Build

Build feature from plan: $ARGUMENTS

---

## Step 1: Load Plan

```
IF $ARGUMENTS contains session path (plans/sessions/...):
  → Load from specified path

ELSE IF $ARGUMENTS contains --no-plan:
  → Skip to direct implementation (user provides guidance)

ELSE:
  → Find latest session: plans/sessions/*/plans/implementation.md
```

**Summarize plan:**
```
Task(summarize-agent, "
  Summarize: {session}/plans/implementation.md

  Extract:
  - Task list with dependencies
  - File paths and operations
  - Test mappings per task
  - Verification commands
")
```

---

## Step 2: Execute Tasks

**For each task in plan:**

### 2a. Find Code Locations

```
Task(full-stack-developer, "
  Task: {task-description}
  Patterns: {session}/research/patterns.md

  Find exact code locations. Do NOT implement.
  Output: {session}/code-changes/{task-slug}.md
")
```

### 2b. Implement Changes

1. **Read** the changes doc for file summary
2. **Read** target source file at documented lines
3. **Apply** changes using Edit tool, following patterns
4. **Verify** after each change:
   ```bash
   npm run typecheck && npm run lint
   ```

### 2c. Run Mapped Tests

```bash
npm test -- --testNamePattern="{test-ids-for-this-task}"
```

**If tests pass:** Mark task complete, commit.
**If tests fail:** Debug and fix before proceeding.

### 2d. Commit

```bash
git add {changed-files}
git commit -m "{task-description}"
```

---

## Step 3: Validate

After all tasks complete:

**Run full test suite:**
```bash
npm test
```

**If any failures:** Return to Step 2, fix issues.

**Run code review:**
```
Task(code-reviewer, "
  Review changes for: {feature}
  Session: {session-path}
  Output: {session}/reviews/code-review.md
")
```

**Run security audit (if applicable):**
```
Task(security-auditor, "
  Audit changes for: {feature}
  Session: {session-path}
  Output: {session}/reviews/security-audit.md
")
```

---

## Step 4: Review Summary

```
Task(review-generator, "
  Generate implementation review.
  Session: {session-path}
  Output: {session}/reviews/implementation-review.md
")
```

**Present to user:**
```
BUILD COMPLETE

Session: {session-path}

## Tasks
- Completed: {N}/{N}
- Commits: {M}

## Tests
- Total: {X}
- Passing: {X}
- Coverage: {Y}%

## Reviews
- Code Review: {PASS|WARNINGS|ISSUES}
- Security: {PASS|WARNINGS|N/A}

## Files Changed
{list of files}

## Next Steps
- {recommendations}
```

---

## Direct Mode (--no-plan)

When invoked without a plan:

1. **Gather minimal context:**
   ```
   Task(codebase-explorer, "Quick scan for: $ARGUMENTS")
   ```

2. **Implement directly** based on user guidance

3. **Validate:**
   ```bash
   npm test && npm run typecheck && npm run lint
   ```

4. **Self-review** changes before commit

---

## On Failure

If task fails:

```
Task {N} failed: {error}

Options:
1. Retry with different approach
2. Skip and continue (mark incomplete)
3. Abort and save progress

Progress saved to: {session}/session.md
Resume: /build --resume {session-path}
```

Save completed tasks to session.md for resume.

---

## Completion Criteria

- [ ] All tasks from plan completed
- [ ] All mapped tests passing
- [ ] Full test suite passing
- [ ] Build succeeds
- [ ] Lint passes
- [ ] Code review complete
- [ ] Security audit complete (if applicable)
