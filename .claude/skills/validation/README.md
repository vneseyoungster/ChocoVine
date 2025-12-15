# Validation Skills

This directory contains skills for the **Validation (V)** phase of the RQPIV workflow.

## Purpose

Validation skills provide templates, checklists, patterns, and automation scripts to ensure thorough code review, testing, security auditing, and documentation during the validation phase.

## Available Skills

| Skill | Purpose | Used By |
|-------|---------|---------|
| `code-review` | Code quality, security, performance checklists | code-reviewer |
| `test-generation` | Test patterns and templates | test-automator |
| `security-scan` | OWASP checklists and security automation | security-auditor |
| `documentation` | Documentation templates and generation | documentation-writer |

## Skill Structure

Each skill follows this structure:

```
skill-name/
├── SKILL.md           # Main skill definition
├── checklists/        # Review checklists (if applicable)
├── patterns/          # Code patterns and examples
├── templates/         # Output templates
└── scripts/           # Automation scripts
```

## Skill Details

### code-review

**Files:**
- `SKILL.md` - Review process and guidelines
- `checklists/security.md` - Security review checklist
- `checklists/performance.md` - Performance review checklist
- `checklists/maintainability.md` - Code quality checklist
- `checklists/accessibility.md` - A11y checklist for frontend
- `templates/review-report.md` - Review report template

**Usage:** Auto-activated when reviewing code changes

### test-generation

**Files:**
- `SKILL.md` - Testing guidelines and coverage targets
- `patterns/unit-tests.md` - Unit testing patterns
- `patterns/integration-tests.md` - Integration testing patterns
- `patterns/e2e-tests.md` - End-to-end testing patterns
- `templates/test-template.ts` - Test file template

**Usage:** Auto-activated when generating tests

### security-scan

**Files:**
- `SKILL.md` - Security scanning guidelines
- `checklists/owasp-top-10.md` - OWASP Top 10 checklist
- `checklists/auth-security.md` - Authentication security checklist
- `checklists/data-validation.md` - Input validation checklist
- `scripts/security-scan.sh` - Automated security scan script

**Usage:** Auto-activated for security audits

### documentation

**Files:**
- `SKILL.md` - Documentation standards
- `templates/readme-template.md` - README template
- `templates/api-doc-template.md` - API documentation template
- `templates/changelog-template.md` - Changelog template
- `scripts/generate-docs.py` - Documentation generation script

**Usage:** Auto-activated when updating documentation

## How Skills Are Used

1. **Sub-agent invokes skill** - When a validation sub-agent runs, it loads its associated skill
2. **Skill provides context** - Checklists, patterns, and templates guide the work
3. **Automation runs** - Scripts execute automated checks
4. **Output follows templates** - Reports use consistent formats

## Integration with Validation Phase

```
/phase-validate
       │
       ├──► code-reviewer + code-review skill
       │         │
       │         └──► docs/reviews/code-review-{session}.md
       │
       ├──► test-automator + test-generation skill
       │         │
       │         └──► docs/reviews/test-report-{session}.md
       │
       ├──► security-auditor + security-scan skill
       │         │
       │         └──► docs/reviews/security-audit-{session}.md
       │
       └──► documentation-writer + documentation skill
                 │
                 └──► docs/reviews/documentation-{session}.md
```

## Creating Custom Skills

To create a new validation skill:

1. Create directory: `.claude/skills/validation/skill-name/`
2. Create `SKILL.md` with frontmatter:
   ```yaml
   ---
   name: skill-name
   description: What this skill does
   ---
   ```
3. Add checklists, patterns, templates as needed
4. Reference in sub-agent's `skills` field
