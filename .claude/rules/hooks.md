# Hooks Rules

## When to Apply
- Understanding hook behavior
- Configuring new hooks
- Debugging hook issues

## Hook Types

| Hook | Trigger | Purpose |
|------|---------|---------|
| PreToolUse | Before tool execution | Block or modify |
| PostToolUse | After tool execution | Log or validate |
| PreCompact | Before context compaction | Save state |
| SessionStart | New session begins | Load context |
| Stop | Session ends | Persist learnings |

## Current Hooks Registry

### PreToolUse Hooks

| Matcher | Action |
|---------|--------|
| Dev server commands | Block (requires tmux) |
| Long-running commands | Remind about tmux |
| `git push` | Pause for review |
| Non-essential .md files | Block creation |
| Edit/Write | Strategic compact counter |

### PostToolUse Hooks

| Matcher | Action |
|---------|--------|
| `gh pr create` | Log PR URL |
| Edit .ts/.tsx/.js/.jsx | Auto-format with Prettier |
| Edit .ts/.tsx | TypeScript check |
| Edit JS/TS files | Warn about console.log |

### Stop Hooks

| Action |
|--------|
| Final console.log audit |
| Persist session state |
| Evaluate for learned patterns |

## TodoWrite Best Practices

- [ ] Use TodoWrite for 3+ step tasks
- [ ] Mark in_progress before starting
- [ ] Mark completed immediately after
- [ ] Only one task in_progress at a time

## Auto-Accept Guidance

Safe to auto-accept:
- Read operations
- Glob/Grep searches
- Test runs

Require confirmation:
- Write/Edit to source files
- Git operations
- Bash commands with side effects

## Configuration

Hooks configured in `.claude/settings.json`

```json
{
  "hooks": {
    "PreToolUse": [...],
    "PostToolUse": [...],
    "Stop": [...]
  }
}
```

## References
- `.claude/settings.json`
- `.claude/hooks/` - Hook scripts
