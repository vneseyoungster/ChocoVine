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
  → Find latest session: plans/sessions/*/plans/tasks.md
```

**Summarize plan:**
```
Task(summarize-agent, "
  Summarize: {session}/plans/tasks.md

  Extract:
  - Task list with dependencies
  - File paths and operations
  - Test mappings per task
  - Acceptance criteria
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
4. **Inline validation after each file:**
   ```bash
   npm run lint -- {changed-file}
   npm run typecheck
   ```
   - IF validation fails → fix before proceeding
5. Mark task complete

### 2c. Commit (optional per task)

```bash
git add {changed-files}
git commit -m "{task-description}"
```

### 2d. Repeat

Continue to next task. Do NOT run tests automatically.

---

## Step 3: Final Validation

After all tasks complete:

**Run full compile/build check:**
```bash
npm run build
```

**Run lint and typecheck:**
```bash
npm run lint && npm run typecheck
```

**IF build fails:** Fix before proceeding.

**Do NOT run tests automatically.** User runs tests manually.

---

## Step 4: Generate Build Summary

Write to: `{session}/build-complete.md`

```markdown
# Build Complete: {feature}

**Session:** {session-id}
**Completed:** {date}

## Summary
{what was built}

## Changes Made
| File | Change Type | Description |
|------|-------------|-------------|
| {path} | {add/modify/delete} | {brief description} |

## Validation Status
- Lint: PASSED
- TypeCheck: PASSED
- Build: PASSED
- Tests: NOT RUN (manual)

## Manual Testing Instructions

**Prerequisites:**
{any setup needed - e.g., start dev server, seed database}

**Test Steps:**
1. {specific action}
   - Navigate to: {URL or location}
   - Action: {click, enter, etc.}
   - Expected: {specific result}

2. {specific action}
   - Navigate to: {URL or location}
   - Action: {click, enter, etc.}
   - Expected: {specific result}

{continue for all testable scenarios from requirements}

**Edge Cases to Verify:**
- {edge case 1}: {how to test, expected result}
- {edge case 2}: {how to test, expected result}

## Next Command
Run `/cv:review` after manual testing
```

---

## Completion

```
BUILD COMPLETE

Session: {session-path}

## Tasks
- Completed: {N}/{N}
- Commits: {M}

## Validation
- Lint: PASSED
- TypeCheck: PASSED
- Build: PASSED

## Files Changed
{list}

## Build Summary
{session}/build-complete.md

## Next Steps
1. Run tests manually: `npm test`
2. Follow manual testing instructions in build-complete.md
3. Run `/cv:review` when testing complete
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
   npm run build && npm run typecheck && npm run lint
   ```

4. **Generate build-complete.md** with manual test instructions

5. Point user to `/cv:review` when done

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
Resume: /cv:build --resume {session-path}
```

Save completed tasks to session.md for resume.

---

## Completion Criteria

- [ ] All tasks from plan completed
- [ ] Build succeeds
- [ ] Lint passes
- [ ] TypeCheck passes
- [ ] build-complete.md generated with manual test instructions
- [ ] User directed to run `/cv:review`
