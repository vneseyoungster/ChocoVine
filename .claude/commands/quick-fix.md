# Quick Fix

Quick fix for: $ARGUMENTS

## Overview

Streamlined fix workflow for known problems. Gathers minimal context,
implements fix directly, and validates. No planning phase - main agent
performs the fix directly.

**Best for:** Bug fixes, typo corrections, config changes, simple refactors
where the problem and solution are already known.

**For bugs:** Uses `systematic-debugging` skill to ensure root cause is found
before attempting fixes.

---

## Phase 1: Context Gathering

### Step 1.1: Understand the Problem

Parse $ARGUMENTS to identify:
- Affected files/modules
- Type of fix (bug, typo, config, refactor)
- Expected outcome

### Step 1.2: Bug Fix Path - Systematic Debugging (REQUIRED for bugs)

**If fix type is "bug" or involves unexpected behavior:**

**INVOKE the `systematic-debugging` skill BEFORE attempting any fix.**

The systematic debugging process follows four phases:

```
Phase 1: Root Cause Investigation (REQUIRED FIRST)
├── Read error messages carefully (full stack traces)
├── Reproduce consistently (exact steps)
├── Check recent changes (git diff, commits)
├── Gather evidence in multi-component systems
└── Trace data flow to find source

Phase 2: Pattern Analysis
├── Find working examples in codebase
├── Compare against references
├── Identify differences
└── Understand dependencies

Phase 3: Hypothesis and Testing
├── Form single hypothesis ("I think X because Y")
├── Test minimally (smallest possible change)
├── Verify before continuing
└── If wrong, form NEW hypothesis (don't pile fixes)

Phase 4: Implementation
├── Create failing test case
├── Implement single fix
├── Verify fix
└── If 3+ fixes failed → STOP, question architecture
```

**CRITICAL: No fixes without root cause investigation first.**

Red flags that mean STOP and follow the process:
- "Quick fix for now, investigate later"
- "Just try changing X and see if it works"
- "It's probably X, let me fix that"
- "I don't fully understand but this might work"
- Proposing solutions before tracing data flow
- Each fix reveals new problem in different place

### Step 1.3: Gather Context (Research Phase)

**Invoke research agents in parallel based on what's unclear:**

| Condition | Agent | Purpose |
|-----------|-------|---------|
| File locations unclear | `codebase-explorer` (haiku) | Quick scan for relevant file paths |
| Coding patterns unclear | `pattern-researcher` (haiku) | Identify conventions in affected area |
| Dependencies/imports unclear | `module-researcher` (haiku) | Trace module relationships |
| External API/library involved | `backend-researcher` (haiku) | Understand integration points |

**Agent invocation pattern:**

```
Task(agent-type, model: haiku, prompt: "
  Target: [specific area related to problem]
  Scope: Quick scan for fix context only
  Output: Concise findings (file paths, patterns, dependencies)
")
```

**Run agents in parallel** when multiple conditions apply to minimize latency.

### Step 1.4: Summarize Research Findings

**ALWAYS invoke `summarize-agent` after research completes:**

```
Task(summarize-agent, model: haiku, prompt: "
  Summarize findings from research agents for quick-fix context:
  - Problem: $ARGUMENTS
  - Research outputs: [agent results]

  Extract only:
  1. Exact file paths to modify
  2. Key patterns to follow
  3. Critical dependencies
  4. Any gotchas or constraints

  Keep under 500 tokens.
")
```

**Benefits:**
- ~70% context reduction
- Consolidated view of all research
- Only essential details for the fix

### Step 1.5: Read Affected Files

Using summarized findings:
- Read only the files identified as needing changes
- Focus on specific sections (use line ranges if large files)
- Understand current implementation at change locations
- Skip files that are reference-only (already summarized)

---

## Phase 2: Direct Fix

### Step 2.1: Complexity Check

If fix touches 3+ files, show warning:

> "This fix affects X files. Consider using `/research` + `/execute` for complex changes. Continue anyway? (y/n)"

- If user confirms, proceed with quick-fix
- If user declines, suggest the full workflow and stop

### Step 2.2: For Bug Fixes - Create Failing Test First

**If this is a bug fix and root cause was identified in Step 1.2:**

Use `test-driven-development` skill to:
1. Write a failing test that reproduces the bug
2. Verify the test fails for the expected reason
3. Then proceed to implement the fix

This ensures:
- Bug is reproducible
- Fix is verifiable
- Regression is prevented

### Step 2.3: Implement Fix

**Main agent performs the fix directly:**

- Make minimal changes to solve the problem
- Follow patterns identified in context gathering
- Do not over-engineer or add unrelated changes
- Do not delegate to implementation sub-agents
- **For bugs:** ONE fix at a time, verify before trying another

### Step 2.4: Quality Check

After changes:
- Run typecheck (if applicable): `npm run typecheck` or equivalent
- Run lint (if applicable): `npm run lint` or equivalent
- Fix any introduced errors immediately

---

## Phase 3: Validation (Lightweight)

### Step 3.1: Self-Review

Main agent reviews changes:
- [ ] Fix addresses the stated problem
- [ ] No unintended side effects
- [ ] Code follows existing patterns
- [ ] No security issues introduced

### Step 3.2: Run Tests

- Run tests related to changed files (if exist)
- Report test results
- If tests fail, report failures and ask user how to proceed

### Step 3.3: Auto-Commit

If all checks pass:
- Stage changes
- Auto-commit with descriptive message: `fix: [brief description]`
- No user confirmation needed

---

## Output

Report to user:
- Files modified
- Changes summary
- Test results (if any)
- Commit hash

---

## Error Handling

### If problem is unclear

Ask user for clarification before proceeding. Do not guess.

### If fix touches many files (3+)

Show warning but let user decide (see Step 2.1).

### If tests fail

Report failures and ask user:
- Proceed without tests passing?
- Attempt to fix the failing tests?
- Abort the quick-fix?

### If typecheck/lint fails

Attempt to fix the errors. If unable to resolve, report to user and ask how to proceed.

### If bug fix fails (3+ attempts)

**From systematic-debugging skill:**

If 3+ fix attempts have failed, STOP and question the architecture:
- Each fix revealing new problems in different places indicates architectural issues
- Discuss with user before attempting more fixes
- Consider using `/research` + `/execute` for proper restructuring

---

## Skills & Agents Reference

| Skill/Agent | When to Use | Path/Type |
|-------------|-------------|-----------|
| `systematic-debugging` | **REQUIRED** for any bug, test failure, or unexpected behavior | `.claude/skills/systematic-debugging/SKILL.md` |
| `test-driven-development` | For creating failing test before fix (bug fixes) | `.claude/skills/test-driven-development/SKILL.md` |
| `summarize-agent` | **REQUIRED** after research phase to consolidate findings | Sub-agent (haiku) |
| `codebase-explorer` | When file locations are unclear | Sub-agent (haiku) |
| `pattern-researcher` | When coding patterns are unclear | Sub-agent (haiku) |
| `module-researcher` | When dependencies/imports are unclear | Sub-agent (haiku) |
| `backend-researcher` | When external API/library is involved | Sub-agent (haiku) |

### systematic-debugging Key Principles

```
NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST
```

Four phases (must complete in order):
1. **Root Cause Investigation** - Read errors, reproduce, check changes, trace data flow
2. **Pattern Analysis** - Find working examples, compare, identify differences
3. **Hypothesis Testing** - Form theory, test minimally, verify
4. **Implementation** - Create test, fix, verify

### test-driven-development Key Principles

```
NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST
```

Red-Green-Refactor cycle:
1. **RED** - Write failing test
2. **Verify RED** - Watch it fail for expected reason
3. **GREEN** - Write minimal code to pass
4. **Verify GREEN** - All tests pass
5. **REFACTOR** - Clean up while staying green

### summarize-agent Key Principles

```
CONSOLIDATE BEFORE CONSUMING CONTEXT
```

Research → Summarize → Act workflow:
1. **RESEARCH** - Run relevant agents in parallel (haiku for speed)
2. **SUMMARIZE** - Consolidate findings via summarize-agent
3. **ACT** - Use summary for targeted file reads and fixes

Benefits:
- ~70% context reduction
- Prevents reading unnecessary files
- Consolidates multi-agent findings into single actionable summary
