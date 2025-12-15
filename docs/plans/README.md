# Plans & Architecture

This directory stores outputs from the Planning (P) phase of the RQPIV workflow.

## Contents

| Artifact Type | Filename Pattern | Purpose |
|---------------|------------------|---------|
| Architecture | `architecture-{session}.md` | High-level design decisions |
| Implementation | `implementation-{session}.md` | Detailed task breakdown |
| ADRs | `adr-{number}-{title}.md` | Architecture Decision Records |

## Purpose

These artifacts provide:

1. **Design Documentation**: How the solution will be architected
2. **Decision Records**: Why certain choices were made
3. **Task Plans**: Specific implementation steps with file paths
4. **Risk Assessment**: Identified risks and mitigation strategies

## Document Types

### Architecture Document

Contains:
- Solution overview
- Component design
- Data flow diagrams
- Integration points
- Design decisions with rationale
- Risk assessment

### Implementation Plan

Contains:
- Task breakdown with priorities
- File operations (CREATE/MODIFY/DELETE)
- Specific line numbers for modifications
- Verification commands
- Git commit messages
- Task dependencies

### Architecture Decision Records (ADRs)

Format:
```markdown
# ADR-N: Title

**Status:** Proposed | Accepted | Deprecated
**Date:** YYYY-MM-DD

## Context
[Why decision needed]

## Decision
[What we decided]

## Consequences
[What follows]
```

## Workflow

1. **Review Requirements**: Read validated requirements from `docs/specs/`
2. **Design Architecture**: Create high-level solution design
3. **User Approval**: Get architecture sign-off
4. **Task Breakdown**: Create detailed implementation tasks
5. **Final Approval**: Get implementation plan sign-off

## Quality Gate

Plans must be:
- [ ] Aligned with requirements
- [ ] Approved by user
- [ ] Include specific file paths
- [ ] Have verification steps
- [ ] Address identified risks
