# Execute Implementation Phase

Execute implementation plan for: $ARGUMENTS

## Prerequisites Check
- [ ] Planning phase completed
- [ ] Architecture approved
- [ ] Implementation plan approved
- [ ] Plan document in `docs/plans/`

## Execution Steps

1. **Load Implementation Plan**
   Read: `docs/plans/implementation-{session}.md`

2. **Switch to Auto-Accept Mode**
   Enter Shift+Tab to enable auto-accept

3. **Execute Tasks In Order**
   For each task:
   a. Invoke appropriate developer sub-agent
   b. Implement per task specification
   c. Run task verification
   d. Log completion

4. **Quality Checks Per Task**
   After each task:
   ```bash
   npm run typecheck
   npm run lint
   ```

5. **Commit After Each Task**
   Using commit message from plan:
   ```bash
   git add -A
   git commit -m "[message from plan]"
   ```

6. **Track Progress**
   Update session file with:
   - Tasks completed
   - Tasks remaining
   - Any deviations

7. **Transition to Validation**
   After all tasks:
   - Summarize changes made
   - List files modified
   - Prepare for validation phase

## Sub-Agent Routing

| Task Type | Sub-Agent |
|-----------|-----------|
| API/Backend | backend-developer |
| UI/Frontend | frontend-developer |
| Database | database-specialist |
| Mixed | Route to primary concern |

## Sub-Agent Invocation

### Backend Tasks
```
Invoke backend-developer sub-agent with:
- Task details from implementation plan
- Reference to clean-code, api-design, error-handling skills
- Verification commands to run
```

### Frontend Tasks
```
Invoke frontend-developer sub-agent with:
- Task details from implementation plan
- Reference to clean-code, component-design skills
- Accessibility requirements
- Verification commands to run
```

### Database Tasks
```
Invoke database-specialist sub-agent with:
- Task details from implementation plan
- Reference to clean-code, migration skills
- Pre-migration checklist requirements
- Verification commands to run
```

## Task Execution Protocol

For each task in the implementation plan:

### 1. Read Task Details
- File operations (CREATE, MODIFY, DELETE)
- Current state (if MODIFY)
- Expected outcome
- Dependencies on other tasks

### 2. Check Patterns
Before implementing, review:
- `docs/research/patterns-*.md` for coding conventions
- Similar implementations in codebase
- Skill references for best practices

### 3. Implement
Follow the specified implementation notes:
- Use patterns from research
- Follow existing error handling approach
- Match logging conventions

### 4. Verify
Run verification commands from task:
```bash
# Example verification
npm run typecheck
npm run lint
npm test -- [specific test file]
```

### 5. Self-Review
Before marking complete:
- [ ] Code follows project patterns
- [ ] All types defined (if TypeScript)
- [ ] Errors handled appropriately
- [ ] No lint/type errors
- [ ] Tests pass

### 6. Commit
Use commit message from task:
```bash
git add [specific files]
git commit -m "[commit message from plan]"
```

### 7. Update Progress
Mark task as complete in session tracking

## Deviation Handling

If plan cannot be followed exactly:

### Minor Deviations
(Different variable name, slight refactoring)
1. Document deviation in task notes
2. Explain rationale
3. Continue with implementation

### Significant Deviations
(Different approach, additional files, scope change)
1. STOP implementation
2. Document the issue
3. Present options to user
4. Get approval before continuing
5. Update plan document if approved

### Blocking Issues
(Missing dependency, conflicting code, unclear requirement)
1. STOP implementation
2. Document the blocker
3. Identify what's needed to proceed
4. Ask user for guidance
5. Do NOT make assumptions

## Progress Tracking

Update `docs/sessions/{session}/session.md` after each task:

```markdown
## Implementation Progress

### Completed Tasks
- [x] Task 1.1: Create user model ✓
- [x] Task 1.2: Add validation ✓

### In Progress
- [ ] Task 1.3: Create API endpoint

### Remaining
- [ ] Task 2.1: Add tests
- [ ] Task 2.2: Update documentation

### Deviations
- Task 1.2: Used Zod instead of Joi (approved)

### Issues
- None currently
```

## Quality Gates

Before marking implementation complete:
- [ ] All tasks executed
- [ ] All verifications passed
- [ ] All commits created
- [ ] No outstanding deviations
- [ ] Session file updated

## Gate: All tasks must complete before validation

Do NOT proceed to validation phase until:
1. Every task in the plan is completed
2. All verification commands pass
3. All commits are created
4. Progress tracking is updated
5. User confirms implementation is complete

## Transition to Validation

After all tasks complete:

1. **Summarize Implementation**
   ```markdown
   ## Implementation Summary
   - Tasks completed: X of Y
   - Files created: [list]
   - Files modified: [list]
   - Commits: [list of commit hashes]
   ```

2. **Prepare for Validation**
   - List all files that need review
   - Identify test coverage needs
   - Note any security-sensitive changes

3. **Notify User**
   "Implementation phase complete. Ready for validation?"

4. **Await Confirmation**
   Do NOT auto-transition to validation
