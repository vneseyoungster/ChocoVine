# Project Scan & Documentation

Scan and document codebase: $ARGUMENTS

## Overview

This command performs comprehensive codebase scanning and generates layered documentation to help developers get familiar quickly. It uses parallel sub-agents for maximum efficiency.

---

## Phase 1: Initialize Scan Session

### Create Session Directory

```
plans/sessions/{date}-project-scan/
├── session.md         # Scan tracking
├── research/          # Analysis findings (populated by agents)
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

## Phase 2: Parallel Research (Sub-Agent Delegation)

**Launch all research agents in parallel using a single message with multiple Task calls:**

### Agent 1: Codebase Explorer

```
Task(codebase-explorer, "
Explore and map the codebase structure:
- Project type detection (frontend/backend/fullstack/library)
- Framework identification
- Directory organization and conventions
- Key file locations (entry points, configs, tests)
- Application entry points and initialization flow

Output findings to: plans/sessions/{session}/research/structure.md
", run_in_background=true)
```

### Agent 2: Pattern Researcher

```
Task(pattern-researcher, "
Identify code patterns and conventions:
- Naming conventions (files, functions, variables)
- File organization strategy
- Error handling patterns
- State management approach
- Testing patterns and structure
- Common abstractions and utilities

Output findings to: plans/sessions/{session}/research/patterns.md
", run_in_background=true)
```

### Agent 3: Dependency Researcher

```
Task(dependency-researcher, "
Analyze project dependencies:
- Direct dependencies and their purposes
- Dev dependencies
- Version constraints and compatibility
- Security vulnerabilities (if detectable)
- Dependency graph overview

Output findings to: plans/sessions/{session}/research/dependencies.md
", run_in_background=true)
```

### Agent 4: Git History Analysis (Bash)

Run directly (fast operation):
```bash
git log --oneline -50 > plans/sessions/{session}/research/history.md
git log --all --oneline --graph | head -30 >> plans/sessions/{session}/research/history.md
git shortlog -sn | head -10 >> plans/sessions/{session}/research/history.md
```

### Wait for Agents

```
TaskOutput(agent1_id, block=true)
TaskOutput(agent2_id, block=true)
TaskOutput(agent3_id, block=true)
```

---

## Phase 3: Generate Documentation (Sub-Agent Delegation)

**After research completes, invoke documentation-writer agent:**

```
Task(documentation-writer, "
Generate comprehensive project documentation using research findings.

Input files:
- plans/sessions/{session}/research/structure.md
- plans/sessions/{session}/research/patterns.md
- plans/sessions/{session}/research/dependencies.md
- plans/sessions/{session}/research/history.md

Generate the following documentation in priority order:

1. **README** → docs/README.md
   - Project overview, tech stack, quick start, key commands, structure

2. **Architecture Overview** → docs/architecture/overview.md
   - System context, component architecture, data flow, design decisions

3. **Entry Points Walkthrough** → docs/walkthroughs/entry-points.md
   - Where code execution starts, request flow, key handlers

4. **Patterns Guide** → docs/walkthroughs/patterns.md
   - Naming conventions, common patterns, code organization principles

5. **API Reference** → docs/api/endpoints.md (if applicable)
   - Endpoint documentation, function signatures, types, examples

6. **Setup Guide** → docs/setup/installation.md
   - Prerequisites, installation steps, configuration, troubleshooting

7. **Gotchas** → docs/onboarding/gotchas.md
   - Common pitfalls, non-obvious behaviors, tips for newcomers

Use templates from: .claude/skills/documentation/project-documentation/templates/
")
```

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

## Sub-Agent Reference

| Phase | Agent | Purpose |
|-------|-------|---------|
| 2 | `codebase-explorer` | Map structure, detect project type, find entry points |
| 2 | `pattern-researcher` | Identify conventions, patterns, testing approach |
| 2 | `dependency-researcher` | Catalog dependencies, versions, purposes |
| 3 | `documentation-writer` | Generate all documentation from research findings |

**Execution Strategy:**
- Phase 2 agents run **in parallel** (background)
- Phase 3 agent runs **after** Phase 2 completes
- Total agents: 4 (3 parallel + 1 sequential)

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

### If agent fails
```
Agent {name} failed: {error}
Retrying with reduced scope...
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

- 📖 Understanding (research agents running)
- 📝 Documenting (documentation agent running)
- 🔍 Reviewing (quality check)
- ✅ Complete (all docs generated)

---

## Completion

On completion:
1. Update session status to COMPLETE
2. List all generated documentation files
3. Summarize key findings from agent outputs
4. Note areas needing manual documentation
5. Provide next steps for documentation maintenance
