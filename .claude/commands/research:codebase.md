# Research Codebase

Analyze codebase for: $ARGUMENTS

## Overview

This command performs comprehensive codebase research for implementation planning. It analyzes the project structure, patterns, dependencies, and relevant modules to understand how to implement a feature or fix.

---

## Phase 1: Initialize Session

### Create Session Directory
```
plans/sessions/{date}-{task-slug}/
├── session.md        # Session tracking
├── research/         # Research findings
├── specs/            # Requirements
├── plans/            # Architecture & tasks
└── reviews/          # (for validation phase)
```

### Session File Template
```markdown
# Session: {task-name}

**Started:** {date}
**Current Phase:** 🔍 Research

## Task Description
{user request}

## Research Findings
- [ ] Codebase structure mapped
- [ ] Patterns identified
- [ ] Dependencies analyzed

## Questions for User
1. {question}

## User Decisions
- {decision}

## Plan Summary
{to be filled after planning}

## Implementation Status
- [ ] {task}

## Validation Results
- [ ] Code review passed
- [ ] Tests passed
- [ ] Security audit passed
```

---

## Phase 2: Research

### Invoke Research Sub-Agents

Select appropriate researchers based on task type:

| Task Type | Primary Researcher | Secondary |
|-----------|-------------------|-----------|
| New project | codebase-explorer | pattern-researcher |
| Frontend work | frontend-researcher | pattern-researcher |
| Backend work | backend-researcher | pattern-researcher |
| Specific module | module-researcher | dependency-researcher |
| Security audit | dependency-researcher | backend-researcher |
| Refactoring | pattern-researcher | module-researcher |

### Research Outputs

Store findings in session directory:
- `plans/sessions/{session}/research/codebase-map.md`
- `plans/sessions/{session}/research/patterns.md`
- `plans/sessions/{session}/research/dependencies.md`

### Research Summary

Create handoff document with:
- Key findings
- Patterns detected
- Constraints identified
- Questions for user

---

## Phase 3: Questioning

### Load Research Context

Read all findings from research phase to inform questions.

### Invoke Requirement Analyst

Delegate to the `requirement-analyst` sub-agent with:
- Research findings summary
- Original user request
- Session context

The sub-agent will:
- Parse user intent into explicit/implicit requirements
- Identify ambiguities and gaps
- Generate prioritized questions

### Present Questions to User

Display questions grouped by priority:

**Must Answer (Blocking)**
These questions must be answered before planning can begin.

**Should Answer (Important)**
These questions improve implementation quality.

**Could Answer (Nice to Have)**
These questions help optimize the solution.

### Await User Responses

For each question:
- Record the user's answer
- Or accept the default assumption
- Note any follow-up questions

### Validate Responses

Check for:
- All blocking questions addressed
- No contradictory answers
- Technical feasibility confirmed

### Generate Requirements Document

Create `plans/sessions/{session}/specs/requirements.md`:
- Functional requirements (with IDs)
- Non-functional requirements (with IDs)
- Acceptance criteria (testable)
- Assumptions confirmed
- Out of scope items

### Confirm Requirements

Present validated requirements and ask:

> "Here are the validated requirements based on your answers. Are these accurate? Ready to proceed to planning?"

**GATE: DO NOT proceed without user confirmation**

---

## Phase 4: Architecture Planning

### Load Context

Read and analyze:
1. Requirements document
2. Research findings
3. User answers
4. Session context

### Invoke Solution Architect

Delegate to `solution-architect` sub-agent to:
- Design high-level solution architecture
- Make technology and pattern decisions
- Identify risks and mitigation strategies
- Create architecture document

**Output:** `plans/sessions/{session}/plans/architecture.md`

### Present Architecture for Review

```
📋 ARCHITECTURE REVIEW

## Key Design Decisions
[Summary of major decisions]

## Components
[List of components and responsibilities]

## Identified Risks
[Risk summary with mitigations]

## Open Questions
[Any questions needing user input]

---
Full architecture document: plans/sessions/{session}/plans/architecture.md
```

### Architecture Approval Gate

**🚫 GATE: DO NOT proceed without explicit user approval**

Ask user:
> "Please review the architecture above. Do you approve this design, or do you have changes/questions?"

**If approved:** Proceed to task breakdown
**If changes needed:** Update architecture and present again
**If questions:** Answer questions and present again

---

## Phase 5: Task Breakdown

### Invoke Task Planner

After architecture approval, delegate to `task-planner` sub-agent to:
- Break architecture into atomic tasks
- Add exact file paths and line numbers
- Define verification for each task
- Establish dependencies and order

**Output:** `plans/sessions/{session}/plans/implementation.md`

### Present Implementation Plan

```
📝 IMPLEMENTATION PLAN

## Summary
- Total Tasks: [N]
- Phases: [N]
- Risk Level: [High/Medium/Low]

## Phase Breakdown
[Phase 1: N tasks]
[Phase 2: N tasks]
...

## Critical Path
[List of P1 tasks that must complete first]

## Verification Commands
[Key commands that will be run]

---
Full implementation plan: plans/sessions/{session}/plans/implementation.md
```

### Plan Approval Gate

**🚫 GATE: DO NOT proceed to implementation without explicit approval**

Ask user:
> "Please review the implementation plan above. Ready to proceed with implementation?"

**If approved:** Research phase complete. Ready for `/execute`
**If changes needed:** Update plan and present again

---

## Quality Checklist

Before completing this phase:
- [ ] Session directory created
- [ ] Research findings documented
- [ ] All blocking questions answered
- [ ] Requirements document created
- [ ] Architecture document addresses all requirements
- [ ] All major decisions have documented rationale
- [ ] Risks identified with mitigations
- [ ] Tasks are atomic and verifiable
- [ ] File paths and line numbers specified
- [ ] Dependencies clearly marked
- [ ] Verification commands included
- [ ] User has approved both architecture and plan

---

## Phase Transition

**On completion:**
1. Update session tracking with status
2. Archive all artifacts
3. Announce: "Codebase research & planning complete. Ready for `/execute`"

---

## Phase Indicators

- 🔍 Research (in progress)
- ❓ Questioning (in progress)
- 📋 Planning (in progress)
- 🔨 Implementation (next: `/execute`)
- ✅ Validation (pending: `/code-check`)

---

## Error Handling

### If research fails
```
Research could not complete for this task.
Gap identified: [description]
Please provide guidance or additional context.
```

### If user skips blocking questions
```
The following blocking questions must be answered before planning:
1. [Question]
2. [Question]

Please provide answers or accept the default assumptions.
```

### If contradictions detected
```
Potential contradictions found in your requirements:
- [Contradiction 1]
- [Contradiction 2]

Please clarify which approach you prefer.
```

---

## Example Usage

```
/research:codebase Add user authentication with JWT tokens

Output:
🔍 Starting Codebase Research Phase...

Invoking research sub-agents...
- backend-researcher: Analyzing API structure
- pattern-researcher: Detecting authentication patterns

Research complete. Key findings:
- Express.js backend with middleware pattern
- No existing auth implementation
- bcrypt and jsonwebtoken available in dependencies

❓ Entering Questioning Phase...

**Must Answer (Blocking)**

Q1: Should authentication use JWT tokens or session-based cookies?
- Impact: Affects security model and state management
- Default: JWT tokens (stateless, better for APIs)

Q2: Which OAuth providers should be supported?
- Impact: Determines third-party integrations needed
- Options: Google, GitHub, Microsoft, None
- Default: None (email/password only)

**Should Answer (Important)**

Q3: Should failed login attempts be rate-limited?
- Impact: Security hardening
- Default: Yes, 5 attempts per 15 minutes

Please answer these questions to proceed with planning.
```

---

## Related Commands

- `/research:ui` - Research UI designs from Figma
- `/research:docs` - Research external documentation and libraries
- `/execute` - Implement the approved plan
- `/code-check` - Validate implementation
