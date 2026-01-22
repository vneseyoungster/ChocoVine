# Start

Run full workflow: $ARGUMENTS

---

## Entry Check

```
IF no package.json AND no src/ AND no .git:
  → "New project detected. Run /init first?"
  → If yes: /init

ELSE IF no CLAUDE.md:
  → "Codebase not documented. Run /init to scan?"
  → If yes: /init
```

---

## Workflow

**Execute in sequence:**

```
Step 1: /plan $ARGUMENTS
        ↓ (wait for approval at each gate)

Step 2: /build {session-path}
        ↓ (wait for completion)

Done: Present summary
```

---

## Flow Diagram

```
┌─────────┐     ┌───────┐     ┌─────────┐
│  /init  │ ──▶ │ /plan │ ──▶ │ /build  │
└─────────┘     └───────┘     └─────────┘
(if needed)     (4 phases)    (4 phases)
                 - Scan        - Read
                 - Reqs        - Implement
                 - Tests       - Validate
                 - Arch        - Review
```

---

## Abort/Resume

```
IF user aborts:
  → Save progress to session.md
  → Show resume command

Resume: /start --resume {session-path}
```

---

## Completion

```
WORKFLOW COMPLETE

Session: {session-path}

Summary:
- Requirements: {N} functional, {M} non-functional
- Tests: {X} generated, all passing
- Tasks: {Y} completed
- Files: {Z} changed

Validation:
- Tests: PASS
- Typecheck: PASS
- Lint: PASS
- Review: PASS

Commits: {list}
```
