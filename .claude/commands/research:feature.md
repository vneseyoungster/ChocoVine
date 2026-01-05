# Research Feature (Requirements Gathering)

Gather requirements for: $ARGUMENTS

## Overview

This command is **Phase 2** of the research flow. It uses collaborative dialogue to understand the feature, then outputs a formal requirements document.

**Input:** User's feature description + codebase research
**Output:** `specs/requirements.md`

**Prerequisite:** `/research:codebase` should be completed first (or will be auto-invoked).

---

## Phase Flow Position

```
┌─────────────────────┐
│  /research:codebase │  ← Phase 1 (Codebase understanding)
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  /research:feature  │  ← YOU ARE HERE (Requirements)
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   /research:spec    │  ← Phase 3 (Test specification)
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   /generate:tests   │  ← Phase 4 (Test files)
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   /research:plan    │  ← Phase 5 (Implementation plan)
└─────────────────────┘
```

---

## Phase 1: Verify Prerequisites

### Parse Arguments

```
IF $ARGUMENTS contains session path (plans/sessions/...):
  → Mode = FROM_SESSION
  → Load session from specified path
  → Verify research phase completed

ELSE IF $ARGUMENTS is task description:
  → Mode = FRESH_START
  → Check if research exists for this task
  → IF no research: Auto-invoke /research:codebase first
```

### GATE: Verify Codebase Research Complete

Before proceeding, verify:
- [ ] Session directory exists: `plans/sessions/{date}-{task}/`
- [ ] Research findings exist: `research/codebase-map.md`
- [ ] Patterns documented: `research/patterns.md`

**If research missing:**
```
Codebase research not found. Invoking Phase 1 first...
→ /research:codebase $ARGUMENTS
```

---

## Phase 2: Load Research Context

### Summarize Research First

**Use summarize-agent to compress research findings before loading.**

```
Task(summarize-agent, "Summarize: plans/sessions/{session}/research/")
```

This returns a consolidated summary for context-efficient processing.

### Context Summary

Compile key findings for questioning:
- Project type and stack
- Existing patterns to follow
- Integration points identified
- Constraints and limitations

---

## Phase 3: Collaborative Dialogue

### Use Brainstorming Skill

Apply the `brainstorming` skill principles:

1. **One question at a time** - Never overwhelm
2. **Multiple choice preferred** - Offer concrete options
3. **Lead with recommendation** - Explain your reasoning
4. **Incremental validation** - 200-300 word chunks
5. **Explore alternatives** - 2-3 approaches before settling
6. **YAGNI ruthlessly** - Challenge unnecessary features

### Dialogue Flow

```
1. UNDERSTAND THE IDEA
   - "What problem does this solve?"
   - "Who will use this feature?"
   - "What does success look like?"

2. EXPLORE CONSTRAINTS
   - "What systems does this integrate with?"
   - "Any performance requirements?"
   - "What's v1 scope vs future?"

3. PROPOSE APPROACHES
   - Present 2-3 options with trade-offs
   - Lead with recommendation
   - Get user's choice

4. VALIDATE UNDERSTANDING
   - Summarize in sections
   - Confirm each before moving on
```

### Question Prioritization

**Must Answer (Blocking)**
Questions that fundamentally shape the feature.

**Should Answer (Important)**
Questions that improve quality but have sensible defaults.

**Could Answer (Nice to Have)**
Edge cases and polish - can use defaults.

---

## Phase 4: Generate Requirements Document

### Create Requirements File

Create `plans/sessions/{session}/specs/requirements.md`:

```markdown
# Requirements: [Feature Name]

**Session:** {session-id}
**Created:** {date}
**Status:** Draft | Validated | Approved

---

## Summary

[2-3 sentence description of what we're building and why]

---

## Functional Requirements

### REQ-1: [Requirement Name]
**Priority:** P1 (Must Have) | P2 (Should Have) | P3 (Nice to Have)
**Description:** [What the system should do]
**Acceptance Criteria:**
- [ ] [Testable criterion 1]
- [ ] [Testable criterion 2]

### REQ-2: [Requirement Name]
...

---

## Non-Functional Requirements

### NFR-1: [Requirement Name]
**Category:** Performance | Security | Usability | Reliability
**Description:** [Constraint or quality attribute]
**Metric:** [How to measure]

---

## Assumptions

| ID | Assumption | Confirmed By |
|----|------------|--------------|
| A1 | [Assumption] | User / Default |

---

## Out of Scope

- [Explicitly excluded item 1]
- [Explicitly excluded item 2]

---

## Open Questions

| ID | Question | Status |
|----|----------|--------|
| Q1 | [Unresolved question] | Open / Answered |

---

## Decisions Made

| ID | Decision | Rationale |
|----|----------|-----------|
| D1 | [Choice made] | [Why] |
```

---

## Phase 5: Confirm & Complete

### Present Requirements Summary

```
REQUIREMENTS CAPTURED

Feature: [Name]
Session: plans/sessions/{date}-{task}/

## Summary
[Brief description]

## Requirements
- Functional: [N] requirements
- Non-Functional: [N] requirements

## Key Decisions
- [Decision 1]
- [Decision 2]

## Out of Scope
- [Item 1]
- [Item 2]

---
Full document: plans/sessions/{session}/specs/requirements.md

Do you approve these requirements?
```

**GATE: User must approve before proceeding**

### Update Session Tracking

Update `session.md`:
```markdown
**Current Phase:** Requirements Complete

## Requirements
- Documented in: specs/requirements.md
- Status: Approved
- Functional: [N]
- Non-Functional: [N]

## Ready For
- `/research:spec` to generate test specification
```

### Announce Completion

```
REQUIREMENTS COMPLETE

Session: plans/sessions/{date}-{task}/
├── research/          ✓ (from Phase 1)
└── specs/
    └── requirements.md ✓

Next Steps:
→ /research:spec [session-path] - Generate test specification
→ /research:plan [session-path] - Skip to implementation planning
```

---

## Quality Gates

### Before Completion
- [ ] Codebase research exists
- [ ] Brainstorming dialogue completed
- [ ] All blocking questions answered
- [ ] Requirements document created
- [ ] User approved requirements

### Requirements Quality
- [ ] Each requirement is testable
- [ ] Priorities assigned (P1/P2/P3)
- [ ] Assumptions documented
- [ ] Out of scope defined
- [ ] No ambiguous language ("should", "might", "could")

---

## Error Handling

### Research not found
```
Codebase research not found.
Running research phase first...
→ Invoking /research:codebase
```

### User skips blocking questions
```
The following questions must be answered before proceeding:
1. [Question]

Please provide an answer or accept the default assumption.
```

### User rejects requirements
```
Requirements not approved.
What would you like to change?
[Return to dialogue phase]
```

---

## Example Usage

### From Fresh Start
```
/research:feature Add user authentication with JWT tokens

→ No research found, invoking /research:codebase first...
→ Research complete
→ Entering brainstorming dialogue...
→ [Collaborative Q&A with user]
→ Requirements captured in specs/requirements.md
→ User approves
→ Ready for /research:spec
```

### From Existing Session
```
/research:feature plans/sessions/2024-01-15-auth/

→ Loading research findings...
→ Entering brainstorming dialogue...
→ [Collaborative Q&A with user]
→ Requirements captured
→ Ready for /research:spec
```

---

## Related Commands

| Command | Purpose |
|---------|---------|
| `/research:codebase` | Phase 1: Codebase understanding |
| `/research:spec` | Phase 3: Test specification |
| `/generate:tests` | Phase 4: Test file generation |
| `/research:plan` | Phase 5: Implementation planning |
