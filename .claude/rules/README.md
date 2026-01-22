# Rules

Governance guidelines for Claude Code in this project.

## Available Rules

| Rule | Purpose | Priority |
|------|---------|----------|
| [agents.md](agents.md) | Agent usage and delegation | HIGH |
| [coding-style.md](coding-style.md) | Code quality standards | CRITICAL |
| [testing.md](testing.md) | Test requirements | HIGH |
| [security.md](security.md) | Security checklist | CRITICAL |
| [git-workflow.md](git-workflow.md) | Commit and PR standards | MEDIUM |
| [performance.md](performance.md) | Model and context management | MEDIUM |
| [patterns.md](patterns.md) | Code patterns and templates | HIGH |
| [hooks.md](hooks.md) | Hook configuration | LOW |

## Rule Format

Each rule file uses this structure:

```markdown
# Rule Name

## When to Apply
[Conditions for rule activation]

## Requirements
[Mandatory items - checklist format]

## Examples
[Good/bad examples]

## References
[Links to skills, agents, or external docs]
```

## Adding New Rules

1. Create `rule-name.md` in this folder
2. Follow the format above
3. Add entry to this README table
4. Set appropriate priority (CRITICAL/HIGH/MEDIUM/LOW)
