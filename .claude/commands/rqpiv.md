# Execute Full RQPIV Workflow

Run complete RQPIV workflow for: $ARGUMENTS

## Overview

This command orchestrates the full Research → Question → Plan → Implement → Validate workflow for a feature request. It coordinates all sub-agents and ensures quality gates are enforced.

## Execution

### 1. Initialize Session

Create session directory structure:
```
docs/sessions/{date}-{slug}/
├── session.md        # Session tracking
├── research/         # Research artifacts
├── specs/            # Requirements
├── plans/            # Architecture & tasks
├── reviews/          # Validation reports
└── summary.md        # Final summary (created at end)
```

Initialize session tracking file with:
- Feature description
- Current phase (Research)
- Start timestamp
- Phase progress table

### 2. Research Phase (R)

**Invoke:** Research sub-agents based on task type

**Sub-agents to consider:**
- `codebase-explorer` - Always run first for new/unfamiliar projects
- `module-researcher` - For specific module analysis
- `frontend-researcher` - For UI/frontend tasks
- `backend-researcher` - For API/backend tasks
- `dependency-researcher` - For package-related tasks
- `pattern-researcher` - For convention-sensitive tasks

**Gate:** Research findings documented in `docs/sessions/{session}/research/`

**Handoff:** Create research summary with:
- Key findings
- Patterns detected
- Constraints identified
- Questions for user

### 3. Questioning Phase (Q)

**Invoke:** `/phase-question`

**Process:**
1. Review research findings
2. Generate clarifying questions
3. Present questions to user (grouped by priority)
4. Await user answers
5. Validate requirements

**Gate:** User confirmed requirements

**User Interaction Point:** PAUSE and present questions. Wait for answers.

### 4. Planning Phase (P)

**Invoke:** `/phase-plan`

**Process:**
1. Invoke `solution-architect` for architecture design
2. Present architecture for approval
3. **PAUSE** - Await architecture approval
4. Invoke `task-planner` for task breakdown
5. Present implementation plan
6. **PAUSE** - Await plan approval

**Gates:**
- Architecture approved by user
- Implementation plan approved by user

**User Interaction Points:**
- After architecture design
- After task breakdown

### 5. Implementation Phase (I)

**Invoke:** `/phase-implement`

**Process:**
1. Load approved implementation plan
2. For each task:
   - Route to appropriate developer sub-agent
   - Execute task
   - Run verification
   - Commit changes
   - Update progress
3. Handle any deviations
4. Complete all tasks

**Sub-agent routing:**
| Task Type | Sub-Agent |
|-----------|-----------|
| API/Backend | backend-developer |
| UI/Frontend | frontend-developer |
| Database | database-specialist |

**Gate:** All tasks completed, code builds

### 6. Validation Phase (V)

**Invoke:** `/phase-validate`

**Process:**
1. Run code review (code-reviewer)
2. If critical issues: STOP, fix, restart
3. Run tests (test-automator)
4. If tests fail: STOP, fix, restart
5. Run security audit (security-auditor)
6. If critical vulnerabilities: STOP, fix, restart
7. Update documentation (documentation-writer)
8. Generate final validation report

**Gate:** All validations pass

### 7. Completion

Generate final summary:
- What was built
- Key decisions made
- Files changed
- Validation results
- Known limitations
- Follow-up items

Update session status to COMPLETE.

Present results to user.

## User Interaction Points

Throughout the workflow, pause for user input at:

| Phase | Interaction | Required |
|-------|-------------|----------|
| Q | Answer questions | Yes |
| P | Approve architecture | Yes |
| P | Approve implementation plan | Yes |
| V | Acknowledge results | Yes |

## Abort Handling

If user requests abort:
1. Save current state to session.md
2. Document last completed action
3. Create resume instructions in session directory
4. Provide command to resume later

## Resume Handling

If resuming interrupted session:
1. Load session.md to determine state
2. Identify last completed phase
3. Verify artifacts exist
4. Continue from appropriate point
5. Ask user to confirm resume point

## Phase Indicators

Use these indicators in session tracking:
- 🔍 Research
- ❓ Questioning
- 📋 Planning
- 🔨 Implementation
- ✅ Validation
- ✓ Complete

## Error Handling

| Error Type | Action |
|------------|--------|
| Research fails | Document gap, ask user for guidance |
| User declines plan | Revise based on feedback |
| Implementation fails | Document issue, attempt recovery |
| Validation fails | Return to implementation, fix issues |
| Critical blocker | Pause workflow, escalate to user |

## Session Artifacts

All workflow artifacts are preserved:

| Artifact | Location |
|----------|----------|
| Session tracking | `docs/sessions/{session}/session.md` |
| Research findings | `docs/sessions/{session}/research/` |
| Requirements | `docs/sessions/{session}/specs/` |
| Architecture | `docs/sessions/{session}/plans/` |
| Implementation plan | `docs/sessions/{session}/plans/` |
| Review reports | `docs/sessions/{session}/reviews/` |
| Final summary | `docs/sessions/{session}/summary.md` |
