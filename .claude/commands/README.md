# Slash Commands

This directory contains custom slash commands for the development workflow.

## Available Commands

| Command | Purpose |
|---------|---------|
| `/initialize` | Initialize new codebase with guided setup |
| `/start` | Execute full workflow (research → execute → validate) |
| `/research` | Router to specialized research modes |
| `/research:codebase` | Phase 1: Analyze codebase for patterns & structure |
| `/research:feature` | Phase 2: Requirements & test specifications (TDD) |
| `/research:plan` | Phase 3: Architecture & implementation planning |
| `/research:ui` | Research UI designs from Figma links |
| `/research:docs` | Research external documentation & libraries |
| `/execute` | Execute implementation from approved plan |
| `/code-check` | Run code review, tests, security audit |
| `/quick-fix` | Quick fix for known problems (no planning phase) |
| `/project-scan` | Scan codebase and generate documentation |

## Usage

Slash commands are invoked by typing `/command-name` in Claude Code.

---

## Research Flow

The research phase follows a sequential 3-phase flow for implementation tasks (TDD approach):

```
┌─────────────────────┐
│  /research:codebase │  ← Phase 1: Understand existing code & patterns
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  /research:feature  │  ← Phase 2: Requirements & test specification (TDD)
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   /research:plan    │  ← Phase 3: Architecture & implementation planning
└─────────────────────┘
```

**Standalone modes** (not part of sequential flow):
- `/research:ui` - Figma design research
- `/research:docs` - External documentation research

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

**Router command** that directs to specialized research modes based on context:

| Detected | Routes To |
|----------|-----------|
| Figma URL | `/research:ui` |
| Library/framework keywords | `/research:docs` |
| Session/plan path | Appropriate next phase |
| Implementation task | `/research:codebase` |

**Example:**
```
/research Add user authentication
```

---

### `/research:codebase [task description]`

**Phase 1: Codebase Research** - Analyzes existing code to understand patterns and structure.

**What It Does:**
1. Creates session directory structure
2. Invokes research sub-agents in parallel
3. Maps project structure and conventions
4. Identifies integration points
5. Documents patterns and dependencies

**Example:**
```
/research:codebase Add user authentication with JWT tokens
```

**Output:**
```
plans/sessions/{date}-{task}/
├── session.md
└── research/
    ├── codebase-map.md
    ├── patterns.md
    ├── dependencies.md
    └── summary.md
```

**Next Step:** `/research:feature [session-path]`

---

### `/research:feature [task description]` or `/research:feature [session-path]`

**Phase 2: Requirements & Test Specification (TDD)** - Gathers requirements and generates failing tests.

**Prerequisites:** `/research:codebase` completed (auto-invokes if missing)

**What It Does:**
1. Loads codebase research findings
2. Engages in brainstorming dialogue with user
3. Generates clarifying questions (prioritized)
4. Creates requirements document
5. Detects test framework and conventions
6. Maps requirements to test cases
7. Generates executable failing test files
8. Verifies tests fail correctly (not syntax errors)

**Example:**
```
# Fresh start (auto-runs Phase 1 first)
/research:feature Add user authentication

# From existing session
/research:feature plans/sessions/2024-01-15-auth/
```

**Output:**
```
plans/sessions/{date}-{task}/
├── research/
│   └── test-patterns.md
├── specs/
│   ├── requirements.md
│   └── test-specification.md
└── (test files in project's test directory)
```

**Quality Gates:**
- All blocking questions answered
- Requirements approved by user
- Test specification approved by user
- All test files created
- Tests fail correctly (missing implementation, not errors)

**Next Step:** `/research:plan [session-path]`

---

### `/research:plan [task description]` or `/research:plan [session-path]`

**Phase 3: Architecture & Planning** - Creates architecture and implementation plan to make tests pass.

**Prerequisites:** `/research:feature` completed (auto-invokes if missing)

**What It Does:**
1. Loads test specification and requirements
2. Designs architecture to satisfy tests
3. Maps components to test suites
4. Creates implementation plan with explicit test mappings
5. Each task references which tests it will make pass

**Example:**
```
# Fresh start (auto-runs Phase 1 & 2 first)
/research:plan Add user authentication

# From existing session
/research:plan plans/sessions/2024-01-15-auth/
```

**Output:**
```
plans/sessions/{date}-{task}/
└── plans/
    ├── architecture.md
    └── implementation.md  (with test mappings)
```

**Quality Gates:**
- Test specification exists
- Architecture approval required
- Implementation plan approval required
- Each task maps to specific test IDs

**Next Step:** `/execute [session-path]`

---

### `/research:ui [figma-url]`

**Standalone: UI Design Research** - Analyzes Figma designs for implementation.

**What It Does:**
1. Fetches design from Figma API
2. Analyzes visually with Gemini vision
3. Extracts colors, typography, spacing
4. Documents component specifications
5. Generates implementation guide

**Example:**
```
/research:ui https://www.figma.com/file/xxx/Design-File
/research:ui https://www.figma.com/design/xxx/Dashboard
```

**Output:**
```
plans/research/ui/{design-name}/
├── overview.md
├── components/
├── styles/
└── implementation.md
```

---

### `/research:docs [topic]`

**Standalone: Documentation Research** - Researches external libraries and documentation.

**What It Does:**
1. Searches llms.txt via context7.com
2. Analyzes GitHub repositories
3. Aggregates documentation
4. Produces comprehensive report

**Example:**
```
/research:docs How to use Expo with React Native
/research:docs Compare Zustand vs Jotai for state management
```

**Output:**
```
plans/research/docs/{date}-{topic}/
└── research-report.md
```

---

### `/execute [task description]`

Executes the implementation phase:

1. Loads implementation plan from research phase
2. Routes tasks to appropriate developer sub-agents
3. Executes tasks in order with verification
4. Commits after each task completion
5. Tracks progress in session file
6. Handles deviations appropriately

**Prerequisites:**
- Research phase completed (any of the 3 phases)
- Architecture and implementation plan approved

**Example:**
```
/execute Add user authentication
/execute plans/sessions/2024-01-15-auth/
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

## Workflow Summary

### Full Workflow (Recommended)
```
/start [description]
  └── Handles everything automatically
```

### Manual Sequential Flow (TDD)
```
/research:codebase [task]    → Phase 1: Understand code
       ↓
/research:feature [session]  → Phase 2: Requirements & failing tests
       ↓
/research:plan [session]     → Phase 3: Plan to make tests pass
       ↓
/execute [session]           → Implement (make tests pass)
       ↓
/code-check [session]        → Validate
```

### Quick Path (Skip Planning)
```
/research:codebase [task]    → Phase 1: Understand code
       ↓
/research:feature [session]  → Phase 2: Requirements & tests
       ↓
/execute [session]           → Implement directly
       ↓
/code-check [session]        → Validate
```

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
