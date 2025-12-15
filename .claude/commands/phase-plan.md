# Execute Planning Phase

Transition to planning phase for: $ARGUMENTS

## Prerequisites Check

Before starting planning, verify:
- [ ] Research phase completed (findings in `docs/research/`)
- [ ] Questioning phase completed
- [ ] Requirements validated and confirmed by user
- [ ] Requirements document exists in `docs/specs/`

**If prerequisites are not met:** STOP and notify user which phase needs completion.

---

## Execution Steps

### Step 1: Load Context

Read and analyze:
1. **Requirements document:** `docs/specs/requirements-*.md`
2. **Research findings:** `docs/research/`
3. **User answers:** From questioning phase
4. **Session context:** Current workflow session

Summarize key inputs before proceeding.

---

### Step 2: Architecture Planning

Invoke the `solution-architect` sub-agent to:
- Design high-level solution architecture
- Make technology and pattern decisions
- Identify risks and mitigation strategies
- Create architecture document

**Output:** `docs/plans/architecture-{session}.md`

---

### Step 3: Present Architecture for Review

Display to user:

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
Full architecture document: docs/plans/architecture-{session}.md
```

---

### Step 4: Architecture Approval Gate

**🚫 GATE: DO NOT proceed without explicit user approval**

Ask user:
> "Please review the architecture above. Do you approve this design, or do you have changes/questions?"

**If approved:** Proceed to Step 5
**If changes needed:** Update architecture and return to Step 3
**If questions:** Answer questions and return to Step 3

---

### Step 5: Task Breakdown

After architecture approval, invoke the `task-planner` sub-agent to:
- Break architecture into atomic tasks
- Add exact file paths and line numbers
- Define verification for each task
- Establish dependencies and order

**Output:** `docs/plans/implementation-{session}.md`

---

### Step 6: Present Implementation Plan

Display to user:

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

## Estimated Verification Commands
[Key commands that will be run]

---
Full implementation plan: docs/plans/implementation-{session}.md
```

---

### Step 7: Plan Approval Gate

**🚫 GATE: DO NOT proceed to implementation without explicit approval**

Ask user:
> "Please review the implementation plan above. Ready to proceed with implementation?"

**If approved:** Planning phase complete. Ready for implementation phase.
**If changes needed:** Update plan and return to Step 6

---

## Phase Outputs

| Document | Location | Status |
|----------|----------|--------|
| Architecture | `docs/plans/architecture-{session}.md` | Required |
| Implementation Plan | `docs/plans/implementation-{session}.md` | Required |
| ADRs (if any) | `docs/plans/adr-*.md` | Optional |

---

## Quality Checklist

Before completing planning phase:
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
1. Update session tracking with planning status
2. Archive planning artifacts
3. Confirm ready for implementation phase

**Next phase:** Implementation (`/phase-implement` when available)

---

## Indicators

- 🔍 Research (complete)
- ❓ Questioning (complete)
- 📋 **Planning (current)**
- 🔨 Implementation (next)
- ✅ Validation (pending)
