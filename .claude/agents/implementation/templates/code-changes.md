# Code Changes Template

Output to: `{session}/code-changes/{task-slug}.md`

## Template

```markdown
# {task-name}

## Purpose

[1-2 sentences from implementation plan - why this change exists]

## Changes

### `{file-path}`

**Summary:** [What this file does in the codebase]

| Lines | Action | Description |
|-------|--------|-------------|
| {n}-{m} | {Add|Modify|Remove} | {What to change} |

**Pattern:** Follow `{similar-file}:{lines}`

---

[Repeat for each file]

---

## Verification

`{verification commands}`
```

## Rules

- One file per task: `{task-slug}.md`
- Task slug: lowercase, hyphenated (e.g., "add-user-auth")
- Include ALL files that need modification
- Always include file summary (what it does)
- Always include pattern reference when available
- Keep descriptions concise but complete
