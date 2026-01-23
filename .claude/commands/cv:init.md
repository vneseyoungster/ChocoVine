# Init

Initialize or scan codebase: $ARGUMENTS

---

## Step 1: Detect Mode

```
IF current directory is empty/new (no package.json, no src/, no .git):
  → MODE = NEW_PROJECT
  → Run project initialization wizard

ELSE:
  → MODE = EXISTING_PROJECT
  → Run project scan and documentation
```

---

## New Project: Initialization Wizard

**Interactive setup for new codebases.**

### Project Questions (one at a time):

**Project Info:**
- "What's the project name?"
- "What type? A) Web app B) API C) Library D) CLI E) Mobile"
- "Brief description?"

**Tech Stack:**
- "Language? A) TypeScript B) JavaScript C) Python D) Other"
- "Framework?" (options based on type)
- "Package manager? A) npm B) pnpm C) yarn"

**Preferences:**
- "Testing framework? A) Jest B) Vitest C) None for now"
- "Linting? A) ESLint B) Biome C) None"

### User Preference Questions (one at a time):

- "Primary editor? A) VS Code B) Cursor C) Zed D) Vim/Neovim E) Other"
- "Use vim keybindings? A) Yes B) No"

### Generate Structure

Based on answers, create:
```
{project}/
├── src/              # Source code
├── tests/            # Test files
├── docs/             # Documentation
├── .claude/          # Claude Code config
└── plans/            # Planning artifacts
```

### Generate Configs

- `package.json` with dependencies
- `tsconfig.json` (if TypeScript)
- `.eslintrc` or `biome.json`
- `jest.config.js` or `vitest.config.js`
- `.gitignore`

### Generate CLAUDE.md (Root)

Read template: `.claude/templates/CLAUDE.md.template`

Fill placeholders with wizard answers:
```
{PROJECT_NAME}        → project name
{PROJECT_DESCRIPTION} → description
{LANGUAGE}            → language choice
{FRAMEWORK}           → framework choice
{PACKAGE_MANAGER}     → package manager
{TESTING_FRAMEWORK}   → testing choice
{LINTING_TOOL}        → linting choice
{FILE_STRUCTURE}      → generated structure
{KEY_PATHS}           → | src/ | Source code |
{AVAILABLE_COMMANDS}  → npm run dev, npm test, etc.
{API_PATTERN}         → default ApiResponse pattern
{ERROR_HANDLING_PATTERN} → default try/catch pattern
{COMPONENT_PATTERN}   → default component structure
{ENV_VARIABLES}       → # Add your env vars here
{DEFAULT_BRANCH}      → main
{COMMIT_STYLE}        → Conventional commits
{GIT_NOTES}           → empty
{ENTRY_POINTS}        → src/index.ts or framework entry
{CORE_DEPENDENCIES}   → from package.json
{DEV_DEPENDENCIES}    → from package.json
```

Write to: `CLAUDE.md` (project root)

### Generate user-CLAUDE.md (.claude/)

Read template: `.claude/templates/user-CLAUDE.md.template`

Fill placeholders with user preferences:
```
{EDITOR}        → editor choice
{VIM_MODE}      → yes/no
{KEY_BINDINGS}  → default or vim
```

Write to: `.claude/user-CLAUDE.md`

---

## Existing Project: Scan & Document

**Analyze and document existing codebase.**

### Parallel Research

```
Task(codebase-explorer, "
  Map structure, entry points, key files.

  Find:
  - Directory structure (tree format)
  - Entry points (main files, index files)
  - Key paths and their purposes
  - Source organization pattern

  Output: plans/sessions/{date}-scan/research/structure.md
", run_in_background=true)

Task(pattern-researcher, "
  Find naming conventions, patterns, testing approach.

  Find:
  - API response patterns (with code examples)
  - Error handling patterns (with code examples)
  - Component/module patterns (with code examples)
  - Commit message style from git log
  - Code style conventions

  Output: plans/sessions/{date}-scan/research/patterns.md
", run_in_background=true)

Task(dependency-researcher, "
  Analyze dependencies and purposes.

  Find:
  - Core dependencies with purposes
  - Dev dependencies with purposes
  - Package manager used
  - Environment variables from .env.example or docs

  Output: plans/sessions/{date}-scan/research/dependencies.md
", run_in_background=true)
```

### Git History (quick)
```bash
git log --oneline -50 > plans/sessions/{date}-scan/research/history.md
git remote -v > plans/sessions/{date}-scan/research/remote.md
git branch --show-current > plans/sessions/{date}-scan/research/branch.md
```

### Detect Project Info

```bash
# Get project name from package.json or directory
cat package.json | jq -r '.name' 2>/dev/null || basename $(pwd)

# Get description
cat package.json | jq -r '.description' 2>/dev/null || echo "No description"
```

### Wait for Research & Consolidate

After research completes, read all findings:
- `plans/sessions/{date}-scan/research/structure.md`
- `plans/sessions/{date}-scan/research/patterns.md`
- `plans/sessions/{date}-scan/research/dependencies.md`

### Generate CLAUDE.md (Root)

Read template: `.claude/templates/CLAUDE.md.template`

**Main agent fills placeholders from research findings:**

```
{PROJECT_NAME}        → from package.json or directory name
{PROJECT_DESCRIPTION} → from package.json or "Scanned project"
{LANGUAGE}            → detected from files (ts/js/py)
{FRAMEWORK}           → detected from dependencies
{PACKAGE_MANAGER}     → detected from lock file
{TESTING_FRAMEWORK}   → detected from devDependencies
{LINTING_TOOL}        → detected from devDependencies/configs
{FILE_STRUCTURE}      → from structure.md (tree format)
{KEY_PATHS}           → from structure.md (table format)
{AVAILABLE_COMMANDS}  → from package.json scripts
{API_PATTERN}         → from patterns.md (code example)
{ERROR_HANDLING_PATTERN} → from patterns.md (code example)
{COMPONENT_PATTERN}   → from patterns.md (code example)
{ENV_VARIABLES}       → from dependencies.md
{DEFAULT_BRANCH}      → from branch.md
{COMMIT_STYLE}        → from history.md analysis
{GIT_NOTES}           → from remote.md
{ENTRY_POINTS}        → from structure.md
{CORE_DEPENDENCIES}   → from dependencies.md
{DEV_DEPENDENCIES}    → from dependencies.md
```

Write to: `CLAUDE.md` (project root)

### User Preference Questions (optional)

Ask user:
- "Would you like to set up user preferences? A) Yes B) Use defaults"

IF Yes:
- "Primary editor? A) VS Code B) Cursor C) Zed D) Vim/Neovim E) Other"
- "Use vim keybindings? A) Yes B) No"

IF No (defaults):
```
{EDITOR}       → "Not specified"
{VIM_MODE}     → "No"
{KEY_BINDINGS} → "Default"
```

### Generate user-CLAUDE.md (.claude/)

Read template: `.claude/templates/user-CLAUDE.md.template`
Fill with user preferences or defaults.
Write to: `.claude/user-CLAUDE.md`

### Generate Documentation (optional)

```
Task(documentation-writer, "
  Generate documentation from research findings.

  Inputs:
  - research/structure.md
  - research/patterns.md
  - research/dependencies.md

  Outputs:
  - docs/README.md
  - docs/architecture/overview.md
  - docs/walkthroughs/entry-points.md
  - docs/setup/installation.md
")
```

---

## Completion

**New Project:**
```
PROJECT INITIALIZED

Name: {name}
Type: {type}
Stack: {language} + {framework}

Created:
- Project structure
- Configuration files
- CLAUDE.md (project root)
- .claude/user-CLAUDE.md (user preferences)

Next: Start developing or /cv:plan {feature}
```

**Existing Project:**
```
PROJECT SCANNED

Name: {name}
Type: {detected type}
Files: {count}
Framework: {detected}

Generated:
- CLAUDE.md (project root) - filled with discovered patterns
- .claude/user-CLAUDE.md (user preferences)
- plans/sessions/{date}-scan/research/ (raw findings)

Research Artifacts:
- structure.md: {summary}
- patterns.md: {summary}
- dependencies.md: {summary}

Next: /cv:plan {feature} or /cv:fix {issue}
```

---

## Template Locations

| Template | Location |
|----------|----------|
| Project CLAUDE.md | `.claude/templates/CLAUDE.md.template` |
| User preferences | `.claude/templates/user-CLAUDE.md.template` |

---

## Output Locations

| File | Location | Purpose |
|------|----------|---------|
| CLAUDE.md | Project root | Project-specific context for Claude |
| user-CLAUDE.md | .claude/ | User preferences (same across projects) |
| Research | plans/sessions/{date}-scan/research/ | Raw agent findings |
