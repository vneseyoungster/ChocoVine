# Review

Review changes: $ARGUMENTS

---

## Step 1: Load Session

```
IF $ARGUMENTS contains session path (plans/sessions/...):
  -> Load from specified path

ELSE IF $ARGUMENTS contains --uncommitted:
  -> Review current working tree changes only

ELSE:
  -> Find latest session: plans/sessions/*/build-complete.md
```

IF no session found:
  -> Prompt user with AskUserQuestion:
    "No build session found. How would you like to proceed?"
    A) Review current uncommitted changes
    B) Specify a session path
    C) Cancel review

**Gather changes:**
```bash
# If session exists, diff from session start
git diff {session-start-commit}..HEAD

# If uncommitted only
git diff HEAD
```

Read session context:
- {session}/build-complete.md (changes summary)
- {session}/plans/tasks.md (what was planned)

---

## Step 2: Launch Validation Agents

**Execute in parallel:**

```
Task(code-reviewer, "
  Review changes for quality, patterns, maintainability.

  Session: {session-path}
  Changes: {git diff summary}
  Patterns: {session}/research/patterns.md

  Check:
  - Code style consistency
  - Error handling
  - Naming conventions
  - SOLID principles
  - No commented code or console.log

  Output: {session}/reviews/code-review.md

  Return: APPROVE | APPROVE WITH CHANGES | REQUEST CHANGES
  Include: List of issues with file:line references
", run_in_background=true)

Task(security-auditor, "
  Audit changes for security vulnerabilities.

  Session: {session-path}
  Changes: {git diff summary}

  Check:
  - OWASP Top 10
  - Input validation
  - SQL injection
  - XSS vulnerabilities
  - Secrets in code
  - Authentication/authorization

  Output: {session}/reviews/security-audit.md

  Return: APPROVE | APPROVE WITH CHANGES | REQUEST CHANGES
  Include: List of vulnerabilities with severity
", run_in_background=true)

Task(test-automator, "
  Check test coverage for changed files.

  Coverage threshold: 80% minimum (HARD GATE)

  Run:
  npm test -- --coverage --changedSince={session-start-commit}

  Output: {session}/reviews/coverage-report.md

  Return:
  - Coverage percentage per file
  - Overall coverage percentage
  - PASS if >= 80%, FAIL if < 80%
  Include: Uncovered lines list
", run_in_background=true)
```

Wait for all agents to complete.
Read outputs from:
- {session}/reviews/code-review.md
- {session}/reviews/security-audit.md
- {session}/reviews/coverage-report.md

---

## Step 3: Consolidate Results

**Parse agent outputs:**
```
code_result = parse({session}/reviews/code-review.md)
security_result = parse({session}/reviews/security-audit.md)
coverage_result = parse({session}/reviews/coverage-report.md)
```

**Recommendation Logic (Most Severe Wins):**
```
IF security_result.recommendation == REQUEST CHANGES:
  -> recommendation = REQUEST CHANGES
  -> reason = "Security vulnerabilities found"

ELSE IF coverage_result.percentage < 80:
  -> recommendation = REQUEST CHANGES
  -> reason = "Coverage below 80% threshold"

ELSE IF code_result.recommendation == REQUEST CHANGES:
  -> recommendation = REQUEST CHANGES
  -> reason = "Code quality issues"

ELSE IF any result == APPROVE WITH CHANGES:
  -> recommendation = APPROVE WITH CHANGES
  -> reason = "Minor issues to address"

ELSE:
  -> recommendation = APPROVE
  -> reason = "All checks passed"
```

**Generate consolidated review:**
Write to: {session}/reviews/review.md

```markdown
# Review Summary

Session: {session-path}
Date: {date}
Recommendation: {recommendation}

## Results

| Category | Status | Issues | Details |
|----------|--------|--------|---------|
| Code Quality | {PASS/WARN/FAIL} | {count} | code-review.md |
| Security | {PASS/WARN/FAIL} | {count} | security-audit.md |
| Coverage | {percent}% | {PASS/FAIL} | coverage-report.md |

## Issues Summary

### Critical (Must Fix)
{list from all reports}

### Warnings (Should Fix)
{list from all reports}

### Suggestions (Nice to Have)
{list from all reports}

## Recommendation
{recommendation}: {reason}
```

---

## Completion

```
REVIEW COMPLETE

Session: {session-path}

## Recommendation
{APPROVE|APPROVE WITH CHANGES|REQUEST CHANGES}

Reason: {reason}

## Summary
| Category | Status | Issues |
|----------|--------|--------|
| Code Quality | {PASS|WARN|FAIL} | {count} |
| Security | {PASS|WARN|FAIL} | {count} |
| Coverage | {percent}% | {PASS if >=80%, FAIL if <80%} |

## Reports Generated
- {session}/reviews/code-review.md
- {session}/reviews/security-audit.md
- {session}/reviews/coverage-report.md
- {session}/reviews/review.md (consolidated)

## Next Steps
IF APPROVE:
  -> Ready to merge. Run: git push

IF APPROVE WITH CHANGES:
  -> Fix minor issues listed in review.md
  -> Run /cv:review again after fixes

IF REQUEST CHANGES:
  -> Address critical issues first
  -> Re-run /cv:build if significant changes needed
  -> Run /cv:review again after fixes
```

---

## On Failure

```
REVIEW FAILED

Error: {description}

Options:
1. Retry review: /cv:review {session-path}
2. Skip failing validator: /cv:review --skip={validator}
3. Review partial results in {session}/reviews/
4. Cancel and fix issues manually

Progress saved to: {session}/reviews/
```
