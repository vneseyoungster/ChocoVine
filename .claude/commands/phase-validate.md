# Execute Validation Phase

Run validation for: $ARGUMENTS

## Prerequisites Check
- [ ] Implementation phase completed
- [ ] All tasks marked complete
- [ ] No pending deviations

## Execution Steps

1. **Run Code Review**
   Invoke code-reviewer sub-agent:
   - Review all changes
   - Generate review report
   - Identify issues by severity

2. **Check for Critical Issues**
   If critical issues found:
   - STOP validation
   - Return to implementation
   - Fix critical issues
   - Restart validation

3. **Run Tests**
   Invoke test-automator sub-agent:
   - Run existing tests
   - Generate new tests if needed
   - Generate coverage report

4. **Check Test Results**
   If tests fail:
   - STOP validation
   - Return to implementation
   - Fix failing tests
   - Restart validation

5. **Run Security Audit**
   Invoke security-auditor sub-agent:
   - Check OWASP compliance
   - Audit dependencies
   - Generate security report

6. **Check Security Results**
   If critical vulnerabilities:
   - STOP validation
   - Return to implementation
   - Fix vulnerabilities
   - Restart validation

7. **Update Documentation**
   Invoke documentation-writer sub-agent:
   - Update README if needed
   - Document new APIs
   - Update changelog

8. **Generate Final Report**
   Combine all validation reports:
   - Code review summary
   - Test coverage summary
   - Security audit summary
   - Documentation status

9. **Determine Final Status**
   - All validations pass → READY FOR MERGE
   - Warnings only → READY WITH NOTES
   - Failures → NEEDS REMEDIATION

## Sub-Agent Invocation

### Code Review
```
Invoke code-reviewer with:
- Files changed in implementation
- Detected patterns from research
- Project-specific conventions
```

### Test Automation
```
Invoke test-automator with:
- New/modified code paths
- Existing test patterns
- Coverage targets (80% lines, 80% functions, 70% branches)
```

### Security Audit
```
Invoke security-auditor with:
- Changed files for code analysis
- Dependency manifest for audit
- OWASP checklist reference
```

### Documentation
```
Invoke documentation-writer with:
- List of changes made
- New public APIs
- Breaking changes (if any)
```

## Outputs

All validation reports stored in `docs/reviews/`:

| Report | File |
|--------|------|
| Code Review | `code-review-{session}.md` |
| Test Report | `test-report-{session}.md` |
| Security Audit | `security-audit-{session}.md` |
| Documentation | `documentation-{session}.md` |
| Final Report | `final-validation-{session}.md` |

## Final Validation Report Template

```markdown
# Validation Report: {session}

**Date:** {date}
**Status:** {PASS | PASS_WITH_WARNINGS | FAIL}

## Summary

| Check | Status | Issues |
|-------|--------|--------|
| Code Review | {status} | {count} |
| Tests | {status} | {count} |
| Security | {status} | {count} |
| Documentation | {status} | {count} |

## Code Review
- Critical: {count}
- Warnings: {count}
- Suggestions: {count}
- [Full Report](code-review-{session}.md)

## Test Results
- Tests Run: {count}
- Passed: {count}
- Failed: {count}
- Coverage: {percent}%
- [Full Report](test-report-{session}.md)

## Security Audit
- Critical: {count}
- High: {count}
- Medium: {count}
- Low: {count}
- [Full Report](security-audit-{session}.md)

## Documentation
- Files Updated: {count}
- Gaps Identified: {count}
- [Full Report](documentation-{session}.md)

## Recommendation

{READY FOR MERGE | NEEDS REMEDIATION}

### Required Actions
1. {action if needed}

### Notes
- {any warnings or observations}
```

## Quality Gates

| Gate | Criteria | Action if Failed |
|------|----------|------------------|
| Code Review | No critical issues | Return to implementation |
| Tests | All pass, coverage met | Fix failing tests |
| Security | No critical/high vulnerabilities | Fix vulnerabilities |
| Documentation | Docs updated | Update documentation |

## Gate: Cannot merge without passing validation
