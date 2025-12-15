# Shared Skills

This directory contains skills that are used across multiple RQPIV phases.

## Overview

Shared skills provide common functionality that benefits all phases of the development workflow. Unlike phase-specific skills, these are designed for cross-cutting concerns.

## Available Skills

### git-workflow

| Attribute | Value |
|-----------|-------|
| Location | `git-workflow/` |
| Used By | All implementation and validation sub-agents |

**Purpose:** Ensure consistent git practices across all phases.

**Contents:**
- `SKILL.md` - Main skill definition
- `conventions/commit-messages.md` - Commit message format
- `conventions/branch-naming.md` - Branch naming conventions
- `conventions/pr-template.md` - Pull request template

**Key Features:**
- Commit message conventions (type, scope, subject)
- Branch naming patterns
- PR template with checklist
- Quality guidelines

### context-preservation

| Attribute | Value |
|-----------|-------|
| Location | `context-preservation/` |
| Used By | workflow-orchestrator, all sub-agents |

**Purpose:** Maintain context continuity across phases and sessions.

**Contents:**
- `SKILL.md` - Main skill definition
- `templates/handoff-template.md` - Phase transition handoff format
- `templates/progress-summary.md` - Work progress tracking
- `templates/session-resume.md` - Resume interrupted sessions

**Key Features:**
- Structured phase handoffs
- Progress tracking templates
- Session state preservation
- Resume instructions

## Usage

### In Sub-Agents

Sub-agents reference shared skills in their frontmatter:

```markdown
---
name: backend-developer
skills: clean-code, api-design, git-workflow
---
```

### During Workflow

1. **Git Workflow** is auto-activated during:
   - Commit creation
   - Branch operations
   - PR preparation

2. **Context Preservation** is used during:
   - Phase transitions (R→Q, Q→P, P→I, I→V)
   - Work interruptions
   - Session resumption

## Directory Structure

```
shared/
├── README.md                          # This file
├── git-workflow/
│   ├── SKILL.md                       # Skill definition
│   └── conventions/
│       ├── commit-messages.md         # Commit format
│       ├── branch-naming.md           # Branch naming
│       └── pr-template.md             # PR template
└── context-preservation/
    ├── SKILL.md                       # Skill definition
    └── templates/
        ├── handoff-template.md        # Phase handoff
        ├── progress-summary.md        # Progress tracking
        └── session-resume.md          # Resume template
```

## Best Practices

### For Git Workflow
- Always use conventional commit format
- Follow branch naming conventions
- Complete PR checklist before submitting
- Keep commits atomic and meaningful

### For Context Preservation
- Create handoffs at every phase transition
- Update progress summaries frequently
- Document decisions with rationale
- Include file paths for artifacts

## Adding New Shared Skills

When adding a new shared skill:

1. Create directory under `shared/`
2. Add `SKILL.md` with frontmatter
3. Include supporting templates/scripts
4. Update this README
5. Reference in relevant sub-agents
