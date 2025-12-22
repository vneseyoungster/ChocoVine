# Walkthrough Template

Use this template to create code walkthroughs and pattern documentation.

---

```markdown
# {Feature/Flow} Walkthrough

## Overview

{1-2 sentences explaining what this walkthrough covers}

**Audience:** {Who should read this}
**Prerequisites:** {What reader should know}
**Time:** {Estimated reading time}

## Entry Points

The code execution starts at:

| Entry Point | File | Purpose |
|-------------|------|---------|
| {Entry 1} | `{path/file.ts:line}` | {When this is triggered} |
| {Entry 2} | `{path/file.ts:line}` | {When this is triggered} |

## Flow Diagram

```
{Trigger}
    │
    ▼
┌─────────────────┐
│  {Step 1}       │  ← {file.ts:line}
│  {Description}  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  {Step 2}       │  ← {file.ts:line}
│  {Description}  │
└────────┬────────┘
         │
    ┌────┴────┐
    ▼         ▼
┌───────┐ ┌───────┐
│{Path1}│ │{Path2}│
└───────┘ └───────┘
```

## Step-by-Step Walkthrough

### Step 1: {Step Name}

**Location:** `{path/to/file.ts:line-range}`

**What happens:**
{Description of what the code does at this step}

**Key code:**
```{language}
// {file.ts:line}
{relevant code snippet}
```

**Why:**
{Explanation of business logic or design decision}

**Next:** Proceeds to Step 2 when {condition}

---

### Step 2: {Step Name}

**Location:** `{path/to/file.ts:line-range}`

**What happens:**
{Description}

**Key code:**
```{language}
// {file.ts:line}
{relevant code snippet}
```

**Decision point:**
- If {condition A}: goes to {Step 3a}
- If {condition B}: goes to {Step 3b}
- Otherwise: {default behavior}

---

### Step 3a: {Success Path}

**Location:** `{path/to/file.ts:line-range}`

{Continue walkthrough...}

---

### Step 3b: {Error Path}

**Location:** `{path/to/file.ts:line-range}`

{Continue walkthrough...}

## Key Patterns

### Pattern: {Pattern Name}

**Used in:** `{file1.ts}`, `{file2.ts}`, `{file3.ts}`

**Description:**
{What this pattern does and why it's used}

**Example:**
```{language}
// Example from {file.ts:line}
{code example}
```

**When to use:**
- {Use case 1}
- {Use case 2}

**Anti-patterns to avoid:**
- {What NOT to do}

## Data Transformations

| Stage | Data Shape | Example |
|-------|------------|---------|
| Input | `{Type}` | `{example}` |
| After Step 1 | `{Type}` | `{example}` |
| After Step 2 | `{Type}` | `{example}` |
| Output | `{Type}` | `{example}` |

## Error Handling

| Error Type | Thrown At | Handled At | User Message |
|------------|-----------|------------|--------------|
| `{Error1}` | `{file:line}` | `{file:line}` | {Message} |
| `{Error2}` | `{file:line}` | `{file:line}` | {Message} |

## Testing This Flow

**Relevant tests:** `{path/to/tests/}`

**Test scenarios:**
1. {Happy path test}
2. {Edge case test}
3. {Error case test}

**Running tests:**
```bash
{test command} {test file pattern}
```

## Common Modifications

### Adding {Feature}

1. Modify `{file1.ts}` to {change}
2. Update `{file2.ts}` to {change}
3. Add tests in `{test-file.ts}`

### Changing {Behavior}

1. {Step 1}
2. {Step 2}
3. {Step 3}

## Gotchas

- **{Gotcha 1}:** {What trips people up and how to avoid}
- **{Gotcha 2}:** {What trips people up and how to avoid}

## Related Documentation

- [{Related Doc 1}]({link})
- [{Related Doc 2}]({link})
```

---

## Template Usage Notes

- Link to actual file:line references
- Include real code snippets (keep them short)
- Explain WHY, not just what
- Highlight decision points clearly
- Include error paths, not just happy paths
- Reference related tests
