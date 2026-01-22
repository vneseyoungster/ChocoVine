# Fix

Fix problem: $ARGUMENTS

---

## Step 1: Classify Problem

```
IF $ARGUMENTS describes a bug/error/failure:
  → Use systematic-debugging skill

ELSE IF $ARGUMENTS requires reasoning/analysis:
  → Use sequential-thinking skill

ELSE:
  → Direct fix (gather context → implement → verify)
```

---

## Systematic Debugging

**Invoke skill:**
```
/systematic-debugging $ARGUMENTS
```

The skill handles:
1. Reproduce the issue
2. Gather evidence (logs, errors, state)
3. Form hypotheses
4. Test hypotheses systematically
5. Implement fix
6. Verify fix

---

## Sequential Thinking

**Invoke skill:**
```
/sequential-thinking $ARGUMENTS
```

The skill handles:
1. Break down the problem
2. Analyze step by step
3. Consider alternatives
4. Revise approach if needed
5. Reach conclusion

---

## Direct Fix

For simple/known problems:

**1. Gather minimal context:**
```
Task(codebase-explorer, "
  Quick scan for files related to: $ARGUMENTS
", model=haiku)
```

**2. Implement fix directly**

**3. Verify:**
```bash
npm test && npm run typecheck && npm run lint
```

**4. Self-review changes**

**5. Commit if tests pass:**
```bash
git add -A && git commit -m "fix: {description}"
```

---

## Complexity Warning

```
IF fix touches 3+ files:
  → Warning: "This may need more planning. Continue or switch to /plan?"
  → User decides
```

---

## Completion

```
FIX COMPLETE

Problem: {description}
Approach: {debugging|thinking|direct}

Changes:
- {file1}: {change}
- {file2}: {change}

Verification:
- Tests: PASS
- Typecheck: PASS
- Lint: PASS

Committed: {commit-hash}
```
