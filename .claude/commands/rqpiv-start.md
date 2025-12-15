# Start RQPIV Workflow

Initialize the RQPIV workflow for: $ARGUMENTS

## Workflow Steps

1. **Create Session Directory**
   Create `docs/sessions/{date}-{task-slug}/` for this workflow session

2. **Enter Plan Mode**
   Switch to plan mode (Shift+Tab×2) for research phase

3. **Invoke Research Phase**
   Delegate to research sub-agents:
   - codebase-explorer (if unfamiliar with project)
   - Relevant specialist researcher based on task type

4. **Await Research Completion**
   Store findings in session directory

5. **Transition to Questioning**
   Generate clarifying questions based on research

6. **DO NOT PROCEED** without user confirmation

## Session Tracking
Create `docs/sessions/{date}-{task-slug}/session.md` with:
- Task description
- Current phase
- Findings summary
- Pending questions
- User decisions

## Phase Indicators
- 🔍 Research
- ❓ Questioning
- 📋 Planning
- 🔨 Implementation
- ✅ Validation

## Research Sub-Agent Selection Guide

| Task Type | Primary Researcher | Secondary |
|-----------|-------------------|-----------|
| New project | codebase-explorer | pattern-researcher |
| Frontend work | frontend-researcher | pattern-researcher |
| Backend work | backend-researcher | pattern-researcher |
| Specific module | module-researcher | dependency-researcher |
| Security audit | dependency-researcher | backend-researcher |
| Refactoring | pattern-researcher | module-researcher |

## Session File Template

```markdown
# RQPIV Session: {task-name}

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
{to be filled after planning phase}

## Implementation Status
- [ ] {task}

## Validation Results
- [ ] Code review passed
- [ ] Tests passed
- [ ] Security audit passed
```
