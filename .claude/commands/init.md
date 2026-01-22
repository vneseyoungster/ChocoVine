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

### Questions (one at a time):

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

### Generate CLAUDE.md

Minimal context file for Claude:
```markdown
# Project Context

## Overview
- **Name:** {name}
- **Type:** {type}
- **Description:** {description}

## Tech Stack
- **Language:** {language}
- **Framework:** {framework}

## Commands
{generated commands}

## Key Paths
{generated paths}
```

---

## Existing Project: Scan & Document

**Analyze and document existing codebase.**

### Parallel Research

```
Task(codebase-explorer, "
  Map structure, entry points, key files
  Output: plans/sessions/{date}-scan/research/structure.md
", run_in_background=true)

Task(pattern-researcher, "
  Find naming conventions, patterns, testing approach
  Output: plans/sessions/{date}-scan/research/patterns.md
", run_in_background=true)

Task(dependency-researcher, "
  Analyze dependencies and purposes
  Output: plans/sessions/{date}-scan/research/dependencies.md
", run_in_background=true)
```

### Git History (quick)
```bash
git log --oneline -50 > plans/sessions/{date}-scan/research/history.md
```

### Generate Documentation

After research completes:
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

### Generate CLAUDE.md

Create minimal context file in project root with:
- Project type and tech stack
- Key paths
- Available commands
- Architecture notes
- Important conventions

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
- CLAUDE.md

Next: Start developing or /plan {feature}
```

**Existing Project:**
```
PROJECT SCANNED

Type: {detected type}
Files: {count}
Framework: {detected}

Generated:
- docs/README.md
- docs/architecture/overview.md
- CLAUDE.md

Next: /plan {feature} or /fix {issue}
```
