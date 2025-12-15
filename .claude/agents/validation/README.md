# Validation Sub-Agents

This directory contains sub-agents for the **Validation (V)** phase of the RQPIV workflow.

## Purpose

Validation sub-agents enforce quality gates by reviewing code, running tests, auditing security, and updating documentation before changes can be merged.

## Available Agents

| Agent | Model | Purpose |
|-------|-------|---------|
| `code-reviewer` | inherit | Review code quality, security, and maintainability |
| `test-automator` | sonnet | Write and run tests, report coverage |
| `security-auditor` | sonnet | OWASP compliance, vulnerability scanning |
| `documentation-writer` | haiku | Update READMEs, API docs, changelogs |

## Agent Selection Guide

### code-reviewer
Use when:
- After any code implementation
- Before committing changes
- For code quality assessment

### test-automator
Use when:
- After implementing new features
- When test coverage is needed
- To verify existing tests pass

### security-auditor
Use when:
- After security-sensitive implementations
- For regular security reviews
- Before deploying to production

### documentation-writer
Use when:
- After successful implementation
- When APIs have changed
- For changelog updates

## Validation Workflow

```
Implementation Complete
         │
         ▼
    code-reviewer ──► Review Report
         │
         ▼ (if passed)
    test-automator ──► Test Report
         │
         ▼ (if passed)
   security-auditor ──► Security Report
         │
         ▼ (if passed)
documentation-writer ──► Doc Updates
         │
         ▼
   Final Validation Report
```

## Quality Gates

| Gate | Requirement |
|------|-------------|
| Code Review | No critical issues |
| Tests | All tests pass, coverage targets met |
| Security | No critical/high vulnerabilities |
| Documentation | Docs updated for changes |

## Output Artifacts

All validation reports are stored in `docs/reviews/`:
- `code-review-{session}.md`
- `test-report-{session}.md`
- `security-audit-{session}.md`
- `documentation-{session}.md`
- `final-validation-{session}.md`
