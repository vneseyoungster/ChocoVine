# Hooks

This directory contains event hooks for Claude Code workflow automation.

## Overview

Hooks are shell scripts that execute in response to specific Claude Code events. They enable:
- Quality gate enforcement
- Automated checks before/after actions
- Session persistence and memory
- Code quality automation

## Active Hooks

All hooks are configured in `../.claude/settings.json` using **inline scripts** for portability. The external scripts in this directory serve as reference implementations.

### Hook Events

| Event | Hooks | Description |
|-------|-------|-------------|
| **PreToolUse** | 5 hooks | Before tool execution |
| **PostToolUse** | 4 hooks | After tool execution |
| **PreCompact** | 1 hook | Before context compaction |
| **SessionStart** | 1 hook | When session begins |
| **Stop** | 3 hooks | When session ends |

### PreToolUse Hooks

| Hook | Trigger | Action |
|------|---------|--------|
| Dev server blocker | `npm/pnpm/yarn/bun run dev` | Blocks unless in tmux |
| Tmux reminder | Long-running commands | Suggests tmux usage |
| Git push review | `git push` | Pauses for review |
| Doc file blocker | `.md/.txt` file creation | Blocks random docs |
| Strategic compact | Edit/Write tools | Suggests compaction |

### PostToolUse Hooks

| Hook | Trigger | Action |
|------|---------|--------|
| PR logger | `gh pr create` | Logs PR URL |
| Prettier | JS/TS file edits | Auto-formats |
| TypeScript check | TS file edits | Runs `tsc --noEmit` |
| console.log warner | JS/TS file edits | Warns about debug logs |

### Session Management Hooks

| Hook | Event | Action |
|------|-------|--------|
| Pre-compact | PreCompact | Saves state before summarization |
| Session start | SessionStart | Loads previous context |
| Session end | Stop | Persists session state |
| Continuous learning | Stop | Evaluates for patterns |

## Directory Structure

```
hooks/
├── README.md                    # This file
├── memory-persistence/          # Session persistence hooks
│   ├── pre-compact.sh          # State before compaction
│   ├── session-start.sh        # Load previous context
│   └── session-end.sh          # Save session state
└── strategic-compact/           # Compaction management
    └── suggest-compact.sh      # Suggest manual compaction
```

## Data Storage

Hooks store data in user home directory:

| Path | Purpose |
|------|---------|
| `~/.claude/sessions/` | Session files and compaction logs |
| `~/.claude/skills/learned/` | Extracted patterns from sessions |

## Configuration

Hooks are configured in `.claude/settings.json`:

```json
{
  "hooks": {
    "PreToolUse": [...],
    "PostToolUse": [...],
    "PreCompact": [...],
    "SessionStart": [...],
    "Stop": [...]
  }
}
```

## Return Codes

| Code | Meaning |
|------|---------|
| 0 | Success - proceed with action |
| 1+ | Failure - block action and show error |

## Customization

To modify hooks:

1. Edit `.claude/settings.json` for inline hooks
2. Or modify scripts in this directory and update settings to reference them

### Using External Scripts

To use external scripts instead of inline:

```json
{
  "hooks": [{
    "type": "command",
    "command": "~/.claude/hooks/memory-persistence/pre-compact.sh"
  }]
}
```

Note: External scripts must be in `~/.claude/` (user home) to be accessible.

## Making Scripts Executable

```bash
chmod +x .claude/hooks/**/*.sh
chmod +x .claude/skills/continuous-learning/*.sh
```
