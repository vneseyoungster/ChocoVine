# Refactoring Agents

Agents specialized for safe code refactoring and cleanup.

## Available Agents

| Agent | Purpose | Tools |
|-------|---------|-------|
| [refactor-cleaner](refactor-cleaner.md) | Dead code cleanup, duplicate consolidation | Read, Edit, Bash, Grep, Glob |

## Usage

These agents are invoked by the `/refactor` command. They can also be called directly:

```
Task(refactor-cleaner, "
  Analyze codebase for dead code.
  Output: docs/reports/dead-code-analysis.md
")
```

## Workflow Integration

```
/refactor clean → refactor-cleaner agent → Analysis → User approval → Safe removal
```

## Safety Principles

1. **Never delete without tests** - Always verify tests pass before and after
2. **Categorize by risk** - SAFE, CAUTION, DANGER levels
3. **User approval gates** - No automatic deletion of risky items
4. **Atomic commits** - One logical change per commit
5. **Rollback ready** - Immediate revert on test failure
