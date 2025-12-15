# Questioning Skills

This directory contains skills for the **Questioning (Q)** phase of the RQPIV workflow.

## Purpose

These skills help transform ambiguous user requests into clear, implementable requirements through structured question generation and intent parsing.

## Available Skills

| Skill | Purpose |
|-------|---------|
| `requirement-clarification` | Generate structured clarifying questions |
| `user-intent-parser` | Parse user requests into structured requirements |

## Directory Structure

```
questioning/
├── README.md
├── requirement-clarification/
│   ├── SKILL.md
│   ├── question-templates/
│   │   ├── scope-questions.md
│   │   ├── technical-questions.md
│   │   └── constraint-questions.md
│   └── scripts/
│       └── validate-requirements.py
└── user-intent-parser/
    ├── SKILL.md
    └── templates/
        └── parsed-intent.md
```

## Output Locations

| Artifact | Location |
|----------|----------|
| Parsed Intent | `docs/specs/parsed-intent-{session}.md` |
| Questions | `docs/specs/questions-{session}.md` |
| Requirements | `docs/specs/requirements-{session}.md` |

## Skill Usage

Skills are automatically invoked by the `requirement-analyst` sub-agent during the questioning phase.

### Manual Invocation

```bash
# Validate requirements document
python .claude/skills/questioning/requirement-clarification/scripts/validate-requirements.py <session-id>
```

## Quality Criteria

### Questions Must Be:
- Specific (not vague)
- Answerable (user has the information)
- Impactful (answer affects implementation)
- Non-technical (accessible language)
- Defaultable (has fallback assumption)

### Requirements Must Be:
- Complete (all blocking questions answered)
- Consistent (no contradictions)
- Feasible (technically possible)
- Specific (measurable acceptance criteria)

## Adding New Skills

1. Create a new directory under `questioning/`
2. Add `SKILL.md` with YAML frontmatter (name, description)
3. Add supporting templates and scripts
4. Update this README
