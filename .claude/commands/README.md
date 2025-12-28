# Slash Commands

This directory contains custom slash commands for the development workflow.

## Available Commands

| Command | Purpose |
|---------|---------|
| `/initialize` | Initialize new codebase with guided setup |
| `/start` | Execute full workflow (research → execute → validate) |
| `/research` | Research codebase, ask questions, create approved plan |
| `/execute` | Execute implementation from approved plan |
| `/code-check` | Run code review, tests, security audit |
| `/quick-fix` | Quick fix for known problems (no planning phase) |
| `/project-scan` | Scan codebase and generate documentation |
| `/ui-research` | Research UI designs from Figma links |

## Usage

Slash commands are invoked by typing `/command-name` in Claude Code.

---

### `/start [feature description]`

**Recommended for most tasks.** Executes the complete workflow automatically:

1. **Research & Plan** - Analyzes codebase, asks questions, creates plan
2. **Execute** - Implements tasks with appropriate developers
3. **Validate** - Runs all quality checks

**User Interaction Points:**
- After questions generated (answers needed)
- After architecture created (approval needed)
- After plan created (approval needed)
- After validation (acknowledge results)

**Example:**
```
/start Add user authentication with JWT tokens
```

**Session Artifacts Created:**
```
plans/sessions/{date}-{slug}/
├── session.md        # Session tracking
├── research/         # Research findings
├── specs/            # Requirements
├── plans/            # Architecture & tasks
├── reviews/          # Validation reports
└── summary.md        # Final summary
```

---

### `/research [task description]`

Combines research, questioning, and planning into one phase:

1. Creates session directory structure
2. Invokes appropriate research sub-agents
3. Generates clarifying questions (prioritized)
4. Presents questions to user and records answers
5. Creates architecture design (requires approval)
6. Creates implementation plan (requires approval)

**Example:**
```
/research Add user authentication
```

**Output:**
- `plans/sessions/{session}/research/` - Research findings
- `plans/sessions/{session}/specs/requirements.md` - Requirements
- `plans/sessions/{session}/plans/architecture.md` - Architecture
- `plans/sessions/{session}/plans/implementation.md` - Task breakdown

**Quality Gates:**
- All blocking questions answered
- Architecture approval required
- Implementation plan approval required

---

### `/execute [task description]`

Executes the implementation phase:

1. Loads implementation plan from `/research` phase
2. Routes tasks to appropriate developer sub-agents
3. Executes tasks in order with verification
4. Commits after each task completion
5. Tracks progress in session file
6. Handles deviations appropriately

**Prerequisites:**
- `/research` phase completed
- Architecture and implementation plan approved

**Example:**
```
/execute Add user authentication
```

**Sub-Agent Routing:**
| Task Type | Sub-Agent |
|-----------|-----------|
| API/Backend | `backend-developer` |
| UI/Frontend | `frontend-developer` |
| Database | `database-specialist` |

**Quality Gates:**
- All tasks must complete before validation
- All verifications must pass

---

### `/code-check [task description]`

Executes the validation phase:

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
- `/execute` phase completed
- All tasks done, no pending deviations

**Example:**
```
/code-check Add user authentication
```

**Sub-Agent Invocation:**
| Check | Sub-Agent |
|-------|-----------|
| Code Review | `code-reviewer` |
| Test Execution | `test-automator` |
| Security Audit | `security-auditor` |
| Documentation | `documentation-writer` |

**Output:**
- `plans/sessions/{session}/reviews/code-review.md`
- `plans/sessions/{session}/reviews/test-report.md`
- `plans/sessions/{session}/reviews/security-audit.md`
- `plans/sessions/{session}/reviews/documentation.md`
- `plans/sessions/{session}/reviews/final-validation.md`

**Final Status:**
- READY FOR MERGE - All validations pass
- READY WITH NOTES - Warnings only
- NEEDS REMEDIATION - Failures found

---

### `/quick-fix [problem description]`

Streamlined fix workflow for known problems. Skips planning phase entirely -
main agent gathers minimal context and implements the fix directly.

**Best for:**
- Bug fixes where cause is already identified
- Typo/config corrections
- Simple refactors with clear scope
- Small code changes with known solutions

**Workflow:**
1. **Context Gathering** - Quick scan for relevant files and patterns (only if needed)
2. **Direct Fix** - Main agent implements fix directly (no sub-agents)
3. **Validation** - Self-review + run tests + auto-commit

**Example:**
```
/quick-fix Fix the null pointer exception in UserService.getProfile()
```

**Key Differences from Full Workflow:**
| Aspect | Full RQPIV | Quick Fix |
|--------|-----------|-----------|
| Research | Full analysis | Minimal context |
| Questions | Comprehensive | Only if unclear |
| Planning | Full architecture | None |
| Implementation | Sub-agents | Main agent |
| Validation | Full suite | Self-review + tests |
| Session | Creates docs | No session |

**Sub-Agent Usage (Optional):**
| Agent | When Used |
|-------|-----------|
| `codebase-explorer` | Only if file locations unclear |
| `pattern-researcher` | Only if coding patterns unclear |

**Complexity Warning:**
If fix touches 3+ files, a warning is shown but user decides whether to proceed
or switch to `/research` + `/execute` workflow.

**Auto-Commit:**
Changes are automatically committed if tests pass and self-review is clean.

---

### `/initialize [project-name]`

Interactive project initialization wizard that guides users through setting up a new codebase.

**What It Does:**
1. **Gathers Information** - Asks comprehensive questions about project type, tech stack, and preferences
2. **Generates Structure** - Creates appropriate directory structure based on project type
3. **Creates Configurations** - Generates config files (package.json, tsconfig, eslint, etc.)
4. **Initializes Documentation** - Sets up docs/ structure with initial files
5. **Updates CLAUDE.md** - Populates project-specific information

**Question Categories:**
- **Project Info** - Name, description, type (web app, API, library, CLI, etc.)
- **Tech Stack** - Language, frontend/backend frameworks, database, auth
- **Preferences** - Package manager, linting, testing, CI/CD, deployment
- **Architecture** - Code organization, state management, API style

**Example:**
```
/initialize
/initialize my-awesome-app
/initialize Create a Next.js e-commerce platform
```

**Session Artifacts Created:**
```
plans/sessions/{date}-initialize/
├── session.md         # Initialization tracking
├── answers/           # User responses by category
└── generated/         # Configuration summaries
```

**Generated Project Structure (varies by type):**
```
{project-name}/
├── src/              # Source code
├── tests/            # Test files
├── docs/             # Documentation
├── .claude/          # Claude Code configuration
└── plans/            # Planning artifacts
```

---

### `/project-scan [target]`

Comprehensive codebase scanner that generates layered documentation for developer onboarding.

**What It Does:**
1. **Analyzes Codebase** - Version control, structure, configurations, entry points
2. **Detects Patterns** - Naming conventions, error handling, state management
3. **Catalogs Dependencies** - Direct/dev dependencies with purposes
4. **Generates Documentation** - README, architecture, walkthroughs, API docs

**Example:**
```
/project-scan
/project-scan ./src
/project-scan Focus on API documentation
```

**Session Artifacts Created:**
```
plans/sessions/{date}-project-scan/
├── session.md         # Scan tracking
├── research/          # Analysis findings
└── output/            # Generated documentation
```

**Generated Documentation:**
```
docs/
├── README.md                    # Project overview
├── architecture/overview.md     # System architecture
├── walkthroughs/               # Entry points, data flow, patterns
├── api/                        # API reference
├── setup/                      # Installation & configuration
└── onboarding/gotchas.md       # Edge cases & tips
```

---

### `/ui-research [figma-url]`

Analyzes Figma designs using the Gemini vision API to extract implementation-ready specifications.

**What It Does:**
1. **Fetches Design** - Uses Figma API to retrieve design frames/components
2. **Analyzes Visually** - Uses Gemini vision to understand layout and components
3. **Extracts Specs** - Colors, typography, spacing, component hierarchy
4. **Generates Guide** - Implementation-ready documentation

**Example:**
```
/ui-research https://www.figma.com/file/xxx/Design-File
/ui-research https://www.figma.com/design/xxx/Dashboard
```

**Output:**
```
plans/research/ui/{design-name}/
├── overview.md        # Design overview
├── components/        # Component specifications
├── styles/           # Color, typography, spacing
└── implementation.md  # Implementation guide
```

**Prerequisites:**
- Figma API token configured
- Gemini API access

---

## Command File Format

Each command is a Markdown file named after the command (without `/`):

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
