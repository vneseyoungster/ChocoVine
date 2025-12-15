# Hooks

This directory contains event hooks for the RQPIV workflow system.

## Purpose

Hooks are shell scripts that execute in response to specific events during the Claude Code workflow. They enable:

- Quality gate enforcement
- Automated checks before/after actions
- Custom workflow automation

## Planned Hooks (Future Phases)

| Hook | Trigger | Purpose |
|------|---------|---------|
| `pre-phase-transition.sh` | Before phase change | Verify prerequisites are met |
| `post-implementation.sh` | After code changes | Run linting, type checking |
| `pre-commit.sh` | Before git commit | Enforce code quality |

## Hook File Format

Hooks are executable shell scripts:

```bash
#!/bin/bash
# Hook: hook-name
# Trigger: when this hook runs
# Purpose: what this hook does

# Hook logic here
exit 0  # 0 = success, non-zero = block action
```

## Return Codes

| Code | Meaning |
|------|---------|
| 0 | Success - proceed with action |
| 1+ | Failure - block action and show error |

## Adding New Hooks

1. Create a new `.sh` file with descriptive name
2. Make it executable: `chmod +x hook-name.sh`
3. Return appropriate exit code
4. Document the hook in this README

## Configuration

Hooks can be configured in Claude Code settings. See Claude Code documentation for details on:

- Hook trigger events
- Environment variables available
- Timeout settings
