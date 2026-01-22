# Performance Rules

## When to Apply
- Choosing model for tasks
- Managing context window
- Complex problem solving

## Requirements

### Model Selection

| Model | Use For | Cost |
|-------|---------|------|
| **Haiku** | Simple tasks, quick answers | $ |
| **Sonnet** | Most coding tasks | $$ |
| **Opus** | Complex architecture, difficult bugs | $$$ |

**Guidelines:**
- [ ] Start with Haiku for simple queries
- [ ] Use Sonnet for standard implementation
- [ ] Escalate to Opus for complex reasoning
- [ ] Specify `model` parameter in Task tool

### Context Window Management

- [ ] Use summarize-agent for large content
- [ ] Compact context at phase transitions
- [ ] Avoid loading entire files when sections suffice
- [ ] Use Glob/Grep before Read for large codebases

**Compaction Triggers:**
- After 50+ tool calls
- Before major phase change (research → implementation)
- When context feels "stale"

### Ultrathink + Plan Mode

For complex tasks requiring deep reasoning:

1. **Enter Plan Mode** - Use EnterPlanMode tool
2. **Think deeply** - "think harder" or "ultrathink"
3. **Explore thoroughly** - Use research agents
4. **Design approach** - Write to plan file
5. **Exit with plan** - Use ExitPlanMode for approval

### Sequential Thinking

For multi-stage problems:
- Break into discrete steps
- Validate each step before proceeding
- Use sequential-thinking skill for complex analysis

## References
- sequential-thinking skill
- EnterPlanMode / ExitPlanMode tools
- summarize-agent
