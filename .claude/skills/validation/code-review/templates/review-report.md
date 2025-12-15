# Code Review Report

**Date:** {date}
**Session:** {session}
**Reviewer:** code-reviewer
**Files Reviewed:** {count}

## Summary

| Category | Count |
|----------|-------|
| Critical Issues | {critical_count} |
| Warnings | {warning_count} |
| Suggestions | {suggestion_count} |

## Overall Recommendation

**Status:** {APPROVE | APPROVE_WITH_CHANGES | REQUEST_CHANGES}

{Summary statement about the overall quality and main concerns}

---

## Critical Issues

> Issues that MUST be fixed before merge

### [CRIT-1] {Issue Title}

- **File:** `{file_path}`
- **Line:** {line_number}
- **Category:** {Security | Data Loss | Breaking Change | Runtime Error}

**Issue:**
{Description of the problem}

**Current Code:**
```{language}
{problematic code snippet}
```

**Recommended Fix:**
```{language}
{fixed code snippet}
```

**Impact:**
{Why this is critical and what could happen if not fixed}

---

## Warnings

> Issues that SHOULD be fixed

### [WARN-1] {Issue Title}

- **File:** `{file_path}`
- **Line:** {line_number}
- **Category:** {Performance | Error Handling | Types | Tests}

**Issue:**
{Description of the problem}

**Recommendation:**
{How to fix or improve}

---

## Suggestions

> Nice-to-have improvements

### [SUGG-1] {Issue Title}

- **File:** `{file_path}`
- **Line:** {line_number}
- **Category:** {Naming | Refactoring | Documentation | Style}

**Suggestion:**
{Description and recommendation}

---

## Patterns Compliance

### Security
- [ ] No hardcoded secrets
- [ ] Input validation present
- [ ] Output encoding used
- [ ] Authentication verified
- [ ] Authorization checked

### Performance
- [ ] No N+1 queries
- [ ] Appropriate caching
- [ ] Efficient algorithms
- [ ] Resource cleanup

### Maintainability
- [ ] Code is readable
- [ ] Functions are focused
- [ ] Types are complete
- [ ] Tests exist
- [ ] Documentation present

### Accessibility (if frontend)
- [ ] Semantic HTML
- [ ] ARIA labels
- [ ] Keyboard navigation
- [ ] Color contrast

---

## Files Reviewed

| File | Status | Issues |
|------|--------|--------|
| `{file_path}` | {OK | ISSUES} | {issue_count} |

---

## Positive Observations

{What was done well that should be continued}

- {Positive observation 1}
- {Positive observation 2}

---

## Next Steps

1. {Action item 1 - typically fix critical issues}
2. {Action item 2 - address warnings}
3. {Action item 3 - consider suggestions}

---

## Review Metadata

- **Review Duration:** {time}
- **Commits Reviewed:** {commit_range}
- **Lines Changed:** +{additions} / -{deletions}
