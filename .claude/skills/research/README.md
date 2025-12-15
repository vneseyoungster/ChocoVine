# Research Skills

This directory contains skill definitions that support the Research (R) phase of the RQPIV workflow.

## Available Skills

| Skill | Purpose | Used By |
|-------|---------|---------|
| `codebase-mapping` | Generate structured codebase maps | codebase-explorer, module-researcher |
| `dependency-analysis` | Audit dependencies for security/updates | dependency-researcher |
| `pattern-detection` | Detect code patterns and conventions | pattern-researcher |

## Directory Structure

```
research/
├── codebase-mapping/
│   ├── SKILL.md           # Skill definition
│   └── templates/
│       └── structure-report.md
├── dependency-analysis/
│   ├── SKILL.md           # Skill definition
│   ├── templates/
│   │   └── dep-report.md
│   └── scripts/
│       └── audit-deps.sh
└── pattern-detection/
    ├── SKILL.md           # Skill definition
    └── patterns/
        ├── naming-conventions.md
        ├── error-handling.md
        └── testing-patterns.md
```

## Skill File Format

Each skill uses Markdown with YAML frontmatter:

```markdown
---
name: skill-name
description: What this skill does and when to use it
---

# Skill Name

[Skill documentation, templates, and processes]
```

## Output Locations

| Skill | Output Location |
|-------|-----------------|
| codebase-mapping | `docs/research/codebase-map-{date}.md` |
| dependency-analysis | `docs/research/dependency-audit-{date}.md` |
| pattern-detection | `docs/research/patterns-{date}.md` |

## Adding New Skills

1. Create a new directory with the skill name
2. Add `SKILL.md` with required frontmatter
3. Add any templates, scripts, or reference materials
4. Update this README with the new skill
