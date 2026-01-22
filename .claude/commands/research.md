# Research

Research topic: $ARGUMENTS

---

## Step 1: Auto-Detect Type

```
IF $ARGUMENTS contains Figma URL (figma.com/file or figma.com/design):
  → TYPE = UI
  → Route to UI Research

ELSE IF $ARGUMENTS mentions library/framework/docs/API:
  → TYPE = DOCS
  → Route to Documentation Research

ELSE:
  → TYPE = ANALYZE
  → Route to Topic Analysis
```

---

## UI Research (Figma)

**Prerequisites:** FIGMA_ACCESS_TOKEN, GEMINI_API_KEY

**Execute:**
```bash
# Export design
python .claude/skills/figma-analyzer/scripts/figma_export.py \
  --url "{figma-url}" \
  --output plans/research/ui/{slug}/assets/design.png

# Analyze with Gemini (NOT Claude vision)
python .claude/skills/ai-multimodal/scripts/gemini_batch_process.py \
  --files plans/research/ui/{slug}/assets/design.png \
  --task analyze \
  --prompt "Analyze UI: layout, components, colors, typography, spacing" \
  --output plans/research/ui/{slug}/analysis.md
```

**Output:**
```
plans/research/ui/{slug}/
├── assets/design.png
├── analysis.md
├── design-tokens.md
├── components.md
└── generated-styles.css
```

---

## Documentation Research

**Use docs-seeker skill for:**
- llms.txt via context7.com
- GitHub repos via Repomix
- Official documentation

**Execute:**
```
Task(general-purpose, "
  Research: $ARGUMENTS

  Search:
  1. llms.txt (context7.com/llms-full.txt)
  2. GitHub repos (use repomix skill)
  3. Official docs

  Output: plans/research/docs/{slug}/report.md
")
```

**Output:**
```
plans/research/docs/{slug}/
├── report.md
├── sources.md
└── code-examples.md
```

---

## Topic Analysis

**Use for:**
- Concept exploration
- Trade-off analysis
- Decision documentation

**Execute:**
```
Task(general-purpose, "
  Analyze topic: $ARGUMENTS

  Structure:
  1. Overview - What is this?
  2. Key Concepts - Core ideas
  3. Trade-offs - Pros/cons
  4. Use Cases - When to use
  5. Examples - Practical applications
  6. Recommendations - Best practices

  Output: plans/research/topics/{slug}.md
")
```

**Output:** `plans/research/topics/{slug}.md`

---

## Completion

```
RESEARCH COMPLETE

Type: {UI|DOCS|ANALYZE}
Topic: {description}

Output: {output-path}

Summary:
{key findings}

Next Steps:
- {recommendations}
```

---

## Force Mode

Override auto-detection:
```
/research --ui {figma-url}
/research --docs {library/topic}
/research --analyze {topic}
```
