# Execute Questioning Phase

Transition to questioning phase for: $ARGUMENTS

## Prerequisites Check

Before proceeding, verify:
- [ ] Research phase completed
- [ ] Research findings in `docs/research/`
- [ ] Session tracking file exists in `docs/sessions/`

If prerequisites not met, prompt user to complete research phase first.

## Execution Steps

### 1. Load Research Context

Read all findings for current session:
```
docs/research/codebase-map-*.md
docs/research/patterns-*.md
docs/research/dependency-audit-*.md
docs/research/*-analysis-*.md
```

Summarize key findings relevant to the task.

### 2. Invoke Requirement Analyst

Delegate to the `requirement-analyst` sub-agent with:
- Research findings summary
- Original user request
- Session context

The sub-agent will:
- Parse user intent into explicit/implicit requirements
- Identify ambiguities and gaps
- Generate prioritized questions

### 3. Generate Questions Document

Create `docs/specs/questions-{session}.md` with:
- Questions grouped by priority
- Impact statement for each
- Default assumptions

### 4. Present Questions to User

Display questions grouped by priority:

**Must Answer (Blocking)**
These questions must be answered before planning can begin.

**Should Answer (Important)**
These questions improve implementation quality.

**Could Answer (Nice to Have)**
These questions help optimize the solution.

### 5. Await User Responses

For each question:
- Record the user's answer
- Or accept the default assumption
- Note any follow-up questions

### 6. Validate Responses

Check for:
- All blocking questions addressed
- No contradictory answers
- Technical feasibility confirmed

Run validation:
```bash
python .claude/skills/questioning/requirement-clarification/scripts/validate-requirements.py {session-id}
```

### 7. Generate Requirements Document

After answers received, create `docs/specs/requirements-{session}.md`:
- Functional requirements (with IDs)
- Non-functional requirements (with IDs)
- Acceptance criteria (testable)
- Assumptions confirmed
- Out of scope items

### 8. Confirm with User

Present the validated requirements and ask:

> "Here are the validated requirements based on your answers:
>
> [Requirements Summary]
>
> Are these requirements accurate? Ready to proceed to planning?"

## Quality Gate

**DO NOT proceed to planning phase without:**
- [ ] All blocking questions answered
- [ ] Requirements document created
- [ ] User explicitly confirms requirements
- [ ] No unresolved contradictions

## Phase Transition

Upon user confirmation:
1. Update session file: `Current Phase: Planning`
2. Store requirements in `docs/specs/requirements-{session}.md`
3. Announce: "Requirements confirmed. Ready for `/phase-plan`"

## Output Locations

| Artifact | Path |
|----------|------|
| Parsed Intent | `docs/specs/parsed-intent-{session}.md` |
| Questions | `docs/specs/questions-{session}.md` |
| Requirements | `docs/specs/requirements-{session}.md` |

## Error Handling

### If research not found
```
Research findings not found for this session.
Please run `/rqpiv-start {task}` first, or ensure research files
exist in docs/research/.
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

## Example Usage

```
/phase-question add user authentication

Output:
Entering Questioning Phase for: add user authentication

Loading research findings...
Found:
- Codebase structure mapped
- Existing auth patterns identified
- Dependencies analyzed

Generating clarifying questions...

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
