# Slash Commands

This directory contains custom slash commands for the RQPIV workflow system.

## Available Commands

| Command | Phase | Purpose |
|---------|-------|---------|
| `/rqpiv` | All | Execute full RQPIV workflow (recommended) |
| `/rqpiv-start` | All | Initialize a new RQPIV workflow session |
| `/phase-question` | Q | Execute questioning phase |
| `/phase-plan` | P | Execute planning phase |
| `/phase-implement` | I | Execute implementation phase |
| `/phase-validate` | V | Execute validation phase |

## Usage

Slash commands are invoked by typing `/command-name` in Claude Code.

### `/rqpiv [feature description]`

**Recommended for most tasks.** Executes the complete RQPIV workflow automatically:

1. **Initialize** - Creates session directory and tracking
2. **Research** - Invokes appropriate research sub-agents
3. **Question** - Generates and presents clarifying questions
4. **Plan** - Creates architecture and implementation plan
5. **Implement** - Executes tasks with appropriate developers
6. **Validate** - Runs all quality checks

**User Interaction Points:**
- After questions generated (answers needed)
- After architecture created (approval needed)
- After plan created (approval needed)
- After validation (acknowledge results)

**Example:**
```
/rqpiv Add user authentication with JWT tokens
```

**Session Artifacts Created:**
```
docs/sessions/{date}-{slug}/
├── session.md        # Session tracking
├── research/         # Research findings
├── specs/            # Requirements
├── plans/            # Architecture & tasks
├── reviews/          # Validation reports
└── summary.md        # Final summary
```

**Best For:**
- New features
- Complex changes
- Unfamiliar codebases
- Quality-critical work

---

### `/rqpiv-start [task description]`

Initializes a complete RQPIV workflow session:

1. Creates session directory structure
2. Enters plan mode for research
3. Invokes appropriate research sub-agents
4. Sets up session tracking
5. Prepares for questioning phase

**Example:**
```
/rqpiv-start Add user authentication with JWT tokens
```

### `/phase-question [task description]`

Executes the questioning phase of the RQPIV workflow:

1. Loads research findings from previous phase
2. Invokes requirement-analyst sub-agent
3. Generates clarifying questions (prioritized)
4. Presents questions to user
5. Records answers and validates
6. Creates requirements document
7. Requires explicit user confirmation

**Example:**
```
/phase-question Add user authentication
```

**Output:**
- `docs/specs/parsed-intent-{session}.md`
- `docs/specs/questions-{session}.md`
- `docs/specs/requirements-{session}.md`

### `/phase-plan [task description]`

Executes the planning phase of the RQPIV workflow:

1. Loads research findings and validated requirements
2. Invokes solution-architect sub-agent for high-level design
3. Presents architecture for user approval
4. After approval, invokes task-planner sub-agent
5. Creates detailed implementation plan with file paths
6. Requires explicit user approval before implementation

**Prerequisites:**
- Research phase completed (findings in `docs/research/`)
- Questioning phase completed (requirements in `docs/specs/`)

**Example:**
```
/phase-plan Add user authentication
```

**Output:**
- `docs/plans/architecture-{session}.md` - High-level design
- `docs/plans/implementation-{session}.md` - Detailed task breakdown

**Quality Gates:**
- Architecture approval required before task breakdown
- Implementation plan approval required before coding

### `/phase-implement [task description]`

Executes the implementation phase of the RQPIV workflow:

1. Loads implementation plan from previous phase
2. Routes tasks to appropriate developer sub-agents
3. Executes tasks in order with verification
4. Commits after each task completion
5. Tracks progress in session file
6. Handles deviations appropriately
7. Prepares for validation phase

**Prerequisites:**
- Planning phase completed (plan in `docs/plans/`)
- Architecture and implementation plan approved

**Example:**
```
/phase-implement Add user authentication
```

**Sub-Agent Routing:**
| Task Type | Sub-Agent |
|-----------|-----------|
| API/Backend | `backend-developer` |
| UI/Frontend | `frontend-developer` |
| Database | `database-specialist` |

**Output:**
- Implemented code changes
- Git commits per task
- Updated session tracking

**Quality Gates:**
- All tasks must complete before validation
- All verifications must pass

### `/phase-validate [task description]`

Executes the validation phase of the RQPIV workflow:

1. Invokes code-reviewer sub-agent for code review
2. Checks for critical issues (stops if found)
3. Invokes test-automator sub-agent for test execution
4. Checks test results (stops if failing)
5. Invokes security-auditor sub-agent for security audit
6. Checks for vulnerabilities (stops if critical)
7. Invokes documentation-writer sub-agent for doc updates
8. Generates final validation report
9. Determines merge readiness

**Prerequisites:**
- Implementation phase completed (all tasks done)
- No pending deviations

**Example:**
```
/phase-validate Add user authentication
```

**Sub-Agent Invocation:**
| Check | Sub-Agent |
|-------|-----------|
| Code Review | `code-reviewer` |
| Test Execution | `test-automator` |
| Security Audit | `security-auditor` |
| Documentation | `documentation-writer` |

**Output:**
- `docs/reviews/code-review-{session}.md`
- `docs/reviews/test-report-{session}.md`
- `docs/reviews/security-audit-{session}.md`
- `docs/reviews/documentation-{session}.md`
- `docs/reviews/final-validation-{session}.md`

**Quality Gates:**
- No critical code review issues
- All tests pass, coverage targets met
- No critical/high security vulnerabilities
- Documentation updated for changes

**Final Status:**
- READY FOR MERGE - All validations pass
- READY WITH NOTES - Warnings only
- NEEDS REMEDIATION - Failures found

## Command File Format

Each command is a Markdown file with the command name (without `/`):

```markdown
# Command Title

Description of what the command does: $ARGUMENTS

## Steps
1. Step one
2. Step two
...
```

The `$ARGUMENTS` placeholder is replaced with any text following the command.

## Adding New Commands

1. Create a new `.md` file named after the command (e.g., `my-command.md`)
2. The command will be available as `/my-command`
3. Use `$ARGUMENTS` to capture user input
4. Document the command in this README
