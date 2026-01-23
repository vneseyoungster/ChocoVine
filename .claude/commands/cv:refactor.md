# Refactor

Safely refactor codebase: $ARGUMENTS

---

## Step 1: Classify Refactor Type

```
IF $ARGUMENTS contains "clean" OR "dead code" OR "unused":
  → Dead Code Cleanup (Step 2)

ELSE IF $ARGUMENTS contains "rename" OR "move":
  → Symbol Refactor (Step 3)

ELSE IF $ARGUMENTS contains "extract" OR "split":
  → Extract Refactor (Step 4)

ELSE:
  → General Refactor (Step 5)
```

---

## Step 2: Dead Code Cleanup

### 2a. Analyze

```
Task(refactor-cleaner, "
  Analyze codebase for dead code.
  Output: docs/reports/dead-code-analysis.md
")
```

The agent will run detection tools, categorize findings by severity, and verify with grep.

### 2b. User Approval Gate

Present the agent's findings grouped by severity:
- **SAFE** - Can be removed with approval
- **CAUTION** - Needs manual review
- **DANGER** - Do not auto-remove

**GATE:** User must approve before any deletions.

### 2c. Execute Removals

```
Task(refactor-cleaner, "
  Remove approved items from dead code analysis.
  Follow safe removal protocol (test before/after each deletion).
  Update docs/DELETION_LOG.md with changes.
")
```

---

## Step 3: Symbol Refactor (Rename/Move)

### 3a. Gather Context

```
Task(codebase-explorer, "
  Find all references to: $ARGUMENTS
  Include: imports, exports, usages, tests
  Output: .reports/symbol-references.md
")
```

### 3b. Plan Changes

**Present plan:**
```
RENAME/MOVE PLAN

Symbol: {name}
References: {N} files

Changes:
1. {file}:{line} - {change}
2. {file}:{line} - {change}
...

Proceed? [Yes/No]
```

### 3c. Execute with Verification

**For each change:**
1. Apply change
2. Run typecheck: `npm run typecheck`
3. If fails, rollback and stop
4. Continue to next

**Final verification:**
```bash
npm test && npm run typecheck && npm run lint
```

---

## Step 4: Extract Refactor

### 4a. Analyze Target

```
Task(module-researcher, "
  Analyze: $ARGUMENTS

  Identify:
  - Code to extract
  - Dependencies
  - Dependents
  - Suggested extraction boundary

  Output: .reports/extraction-analysis.md
")
```

### 4b. Design Extraction

**Present plan:**
```
EXTRACTION PLAN

Source: {file}:{lines}
Target: {new-file-or-location}

New module will contain:
- {function/class}
- {dependencies}

Imports to update: {N} files

Proceed? [Yes/No]
```

### 4c. Execute Extraction

1. Create new file with extracted code
2. Update imports in source
3. Update all dependents
4. Verify: `npm run typecheck`
5. Run tests: `npm test`

---

## Step 5: General Refactor

### 5a. Understand Scope

```
Task(pattern-researcher, "
  Analyze refactoring scope: $ARGUMENTS

  Identify:
  - Current patterns
  - Proposed changes
  - Impact assessment

  Output: .reports/refactor-scope.md
")
```

### 5b. Plan with User

**Ask clarifying questions:**
- What's the goal of this refactor?
- What should remain unchanged?
- Any patterns to follow?

### 5c. Execute Incrementally

**For each change:**
1. Small, atomic edit
2. Typecheck after each
3. Test after each file
4. Commit after each logical unit

---

## Verification (All Types)

**Final checks:**
```bash
npm run typecheck && npm run lint && npm test
```

**If all pass:**
```
Task(code-reviewer, "
  Review refactoring changes.
  Focus: Did refactor maintain behavior? Any regressions?
  Output: docs/reports/refactor-review.md
")
```

---

## Completion

```
REFACTOR COMPLETE

Type: {dead-code|rename|extract|general}
Scope: $ARGUMENTS

Changes:
- Files modified: {N}
- Files deleted: {M}
- Files created: {P}

Verification:
- Tests: PASS ({X} passing)
- Typecheck: PASS
- Lint: PASS

Commits: {list}

Report: docs/reports/{report-file}.md
```

---

## On Failure

```
REFACTOR FAILED

Step: {step}
Error: {error}

Rollback applied: {yes/no}
Changes preserved: {list of committed changes}

Options:
1. Resume from failed step
2. Abort (all uncommitted changes reverted)
```

Save state for resume: `.reports/refactor-state.json`

---

## Safety Rules

1. **Never delete without tests** - Always run test suite before and after
2. **Atomic commits** - One logical change per commit
3. **Rollback on failure** - Immediately revert if tests break
4. **User approval for CAUTION/DANGER** - Never auto-delete risky items
5. **Preserve behavior** - Refactor must not change functionality

---

## References

| Resource | Location |
|----------|----------|
| refactor-cleaner agent | `.claude/agents/refactoring/refactor-cleaner.md` |
| Deletion log | `docs/DELETION_LOG.md` |
| Analysis reports | `docs/reports/dead-code-analysis.md` |
| State file | `.reports/refactor-state.json` |
