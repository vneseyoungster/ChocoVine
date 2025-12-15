# Specifications & Requirements

This directory stores outputs from the Questioning (Q) phase of the RQPIV workflow.

## Contents

| Artifact Type | Filename Pattern | Purpose |
|---------------|------------------|---------|
| Parsed intent | `parsed-intent-{session}.md` | Structured user requirements |
| Questions | `questions-{session}.md` | Clarifying questions for user |
| Requirements | `requirements-{session}.md` | Validated requirements document |

## Purpose

These artifacts capture:

1. **User Intent**: What the user actually wants to achieve
2. **Clarifications**: Questions asked and answers received
3. **Requirements**: Final validated requirements ready for planning
4. **Assumptions**: Documented assumptions made during analysis

## Workflow

1. **Parse Intent**: Extract explicit and implicit requirements from user request
2. **Generate Questions**: Create prioritized clarifying questions
3. **Collect Answers**: Record user responses
4. **Validate Requirements**: Create final requirements document

## Document Templates

### Parsed Intent
```markdown
# Parsed Requirements: [Feature]

## User Statement
> [original request]

## Extracted Requirements
| ID | Requirement | Source | Confidence |
|----|-------------|--------|------------|
| FR-1 | ... | Explicit | High |
```

### Questions
```markdown
# Clarifying Questions

## Must Answer (Blocking)
1. [Question]
   - Impact: [why this matters]
   - Default: [assumption if not answered]
```

### Requirements
```markdown
# Validated Requirements: [Feature]

## Functional Requirements
...

## Non-Functional Requirements
...

## Acceptance Criteria
- [ ] Given/When/Then...
```

## Quality Gate

Requirements must be:
- [ ] Confirmed by user
- [ ] Free of contradictions
- [ ] Technically feasible
- [ ] Specific and testable
