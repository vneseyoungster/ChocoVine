# Project Scan & Documentation

Scan and document codebase: $ARGUMENTS

## Overview

This command performs comprehensive codebase scanning and generates layered documentation to help developers get familiar quickly. It follows a 6-phase methodology: Understand, Structure, Essential Docs, Functions, Onboarding, and Maintain.

---

## Phase 1: Initialize Scan Session

### Create Session Directory
```
plans/sessions/{date}-project-scan/
├── session.md         # Scan tracking
├── research/          # Analysis findings
│   ├── structure.md   # Directory structure
│   ├── patterns.md    # Detected patterns
│   ├── dependencies.md # Dependency analysis
│   └── history.md     # Git history analysis
└── output/            # Generated documentation
```

### Session File Template
```markdown
# Session: Project Scan

**Started:** {date}
**Target:** {directory or description}
**Current Phase:** 📖 Understanding

## Scan Progress
- [ ] Version control analyzed
- [ ] Structure mapped
- [ ] Configuration identified
- [ ] Entry points found
- [ ] Patterns detected
- [ ] Dependencies catalogued

## Generated Documentation
- [ ] README created
- [ ] Architecture overview
- [ ] Entry points walkthrough
- [ ] Core patterns guide
- [ ] API reference (if applicable)
- [ ] Setup guide
- [ ] Gotchas documented

## Findings Summary
{to be filled during scan}
```

---

## Phase 2: Understand Before Documenting

### 2.1 Version Control Analysis

Invoke analysis to extract:
- Recent commit patterns and velocity
- Key contributors and ownership
- Branching strategy
- Focus areas

**Commands:**
```bash
git log --oneline -50
git log --all --oneline --graph | head -30
git shortlog -sn | head -10
```

**Store findings:** `plans/sessions/{session}/research/history.md`

### 2.2 Structure Analysis

Map the codebase:
- Project type detection
- Framework identification
- Directory organization
- Key file locations

**Store findings:** `plans/sessions/{session}/research/structure.md`

### 2.3 Configuration Analysis

Identify all configuration:
- Package manifests
- Environment configs
- Build/test configs
- Linter/formatter configs

### 2.4 Entry Point Analysis

Find and trace:
- Application entry points
- API route registration
- Middleware chains
- Event handlers

### 2.5 Pattern Detection

Identify recurring patterns:
- Naming conventions
- File organization strategy
- Error handling patterns
- State management
- Testing patterns

**Store findings:** `plans/sessions/{session}/research/patterns.md`

### 2.6 Dependency Analysis

Catalog dependencies:
- Direct dependencies
- Dev dependencies
- Dependency purposes
- Version constraints

**Store findings:** `plans/sessions/{session}/research/dependencies.md`

---

## Phase 3: Generate Documentation

### Documentation Priority Order

Generate in this order (most critical first):

#### 3.1 README with Setup Instructions

**Template:** `.claude/skills/documentation/project-documentation/templates/readme-template.md`

**Output:** `docs/README.md`

**Content:**
- Project overview
- Tech stack
- Quick start
- Key commands
- Project structure

**Gate:** User reviews README for accuracy

---

#### 3.2 Architecture Overview

**Template:** `.claude/skills/documentation/project-documentation/templates/architecture-template.md`

**Output:** `docs/architecture/overview.md`

**Content:**
- System context
- Component architecture
- Data flow
- Integration points
- Design decisions

---

#### 3.3 Entry Points Walkthrough

**Template:** `.claude/skills/documentation/project-documentation/templates/walkthrough-template.md`

**Output:** `docs/walkthroughs/entry-points.md`

**Content:**
- Where code execution starts
- Request flow
- Key handlers
- Initialization sequence

---

#### 3.4 Core Patterns Guide

**Output:** `docs/walkthroughs/patterns.md`

**Content:**
- Naming conventions used
- Common patterns identified
- Code organization principles
- Error handling approach

---

#### 3.5 API Reference (if applicable)

**Template:** `.claude/skills/documentation/project-documentation/templates/api-reference-template.md`

**Output:** `docs/api/endpoints.md` or `docs/api/functions.md`

**Content:**
- Endpoint documentation
- Function signatures
- Types/interfaces
- Examples

---

#### 3.6 Setup Guide

**Template:** `.claude/skills/documentation/project-documentation/templates/setup-guide-template.md`

**Output:** `docs/setup/installation.md`

**Content:**
- Prerequisites
- Installation steps
- Configuration
- Troubleshooting

---

#### 3.7 Gotchas & Edge Cases

**Output:** `docs/onboarding/gotchas.md`

**Content:**
- Common pitfalls
- Non-obvious behaviors
- Environment gotchas
- Tips for newcomers

---

## Phase 4: Review & Finalize

### Present Findings Summary

```
📊 PROJECT SCAN COMPLETE

## Project Profile
- Type: {project type}
- Framework: {framework}
- Language: {language}
- Size: {file count} files, {loc} LOC

## Documentation Generated
1. ✅ README - docs/README.md
2. ✅ Architecture - docs/architecture/overview.md
3. ✅ Entry Points - docs/walkthroughs/entry-points.md
4. ✅ Patterns - docs/walkthroughs/patterns.md
5. ✅ API Reference - docs/api/endpoints.md
6. ✅ Setup Guide - docs/setup/installation.md
7. ✅ Gotchas - docs/onboarding/gotchas.md

## Key Findings
- {Finding 1}
- {Finding 2}
- {Finding 3}

## Recommendations
- {Recommendation 1}
- {Recommendation 2}

## Documentation Gaps
- {Area needing manual documentation}
```

### Gate: User Review

Ask user:
> "Documentation has been generated. Please review the files and let me know if any sections need refinement or additional detail."

---

## Phase 5: Documentation Structure

Final documentation layout:
```
docs/
├── README.md                    # Project overview (root)
├── architecture/
│   ├── overview.md              # System architecture
│   ├── components.md            # Component details
│   └── diagrams/                # Architecture diagrams
├── walkthroughs/
│   ├── entry-points.md          # Where code starts
│   ├── data-flow.md             # How data moves
│   └── patterns.md              # Recurring patterns
├── api/
│   ├── endpoints.md             # API documentation
│   └── functions.md             # Key functions
├── setup/
│   ├── installation.md          # Setup guide
│   ├── configuration.md         # Config options
│   └── troubleshooting.md       # Common issues
└── onboarding/
    ├── quickstart.md            # Quick start guide
    ├── tutorials/               # Hands-on tutorials
    └── gotchas.md               # Edge cases & tips
```

---

## Skill Reference

**Primary Skill:** `project-documentation`
**Location:** `.claude/skills/documentation/project-documentation/SKILL.md`

**Templates:**
- `templates/readme-template.md`
- `templates/architecture-template.md`
- `templates/walkthrough-template.md`
- `templates/api-reference-template.md`
- `templates/setup-guide-template.md`

**References:**
- `references/function-documentation.md`

---

## Error Handling

### If codebase is too large
```
Codebase exceeds typical analysis scope.
Focusing on core directories: {list}
Additional areas can be documented incrementally.
```

### If patterns unclear
```
Unable to definitively identify patterns in: {area}
Documenting observations. Manual review recommended.
```

### If entry points not found
```
Standard entry points not detected.
Please specify the main entry point for this project.
```

---

## Example Usage

```
/project-scan
/project-scan ./src
/project-scan Focus on API documentation
```

---

## Phase Indicators

- 📖 Understanding (analyzing codebase)
- 📝 Documenting (generating docs)
- 🔍 Reviewing (quality check)
- ✅ Complete (all docs generated)

---

## Completion

On completion:
1. Update session status to COMPLETE
2. List all generated documentation files
3. Summarize key findings
4. Note areas needing manual documentation
5. Provide next steps for documentation maintenance
