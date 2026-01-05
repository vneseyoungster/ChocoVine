# Topic Analysis & Documentation

Analyze topic: $ARGUMENTS

## Overview

Performs deep analysis of abstract topics, concepts, or technologies through multi-agent research and brainstorming. Produces comprehensive documentation with Mermaid diagrams, converted to a styled standalone HTML report.

**Input:** Topic/concept description (not file paths)
**Output:** Styled HTML report in `report/index.html`

---

## Execution

Follow the skill guide at:
`.claude/skills/documentation/topic-analysis/topic-analysis.md`

Use templates from:
- `.claude/skills/documentation/topic-analysis/templates/analysis-template.md`
- `.claude/skills/documentation/topic-analysis/templates/html-template.html`

---

## Quick Reference

### Phase Flow

```
INITIALIZE → RESEARCH → BRAINSTORM → DOCUMENT → CONVERT → COMPLETE
```

### Session Structure

```
plans/sessions/{date}-analyze-{topic-slug}/
├── session.md
├── research/
├── docs/
└── report/
    └── index.html
```

### Quality Gates

| Phase | Gate |
|-------|------|
| Initialize | Session directory created |
| Research | All agents completed |
| Brainstorm | User confirms direction |
| Document | Markdown with diagrams exists |
| Convert | HTML renders correctly |
| Complete | All files saved |

---

## Related Commands

| Command | Purpose |
|---------|---------|
| `/research:docs` | Research external documentation only |
| `/research:codebase` | Analyze existing code (not topics) |
| `/project-scan` | Generate documentation for a codebase |
