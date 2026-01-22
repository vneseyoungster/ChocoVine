# Agent Usage Rules

## When to Apply
- Multi-step tasks requiring specialized expertise
- Research, analysis, or validation tasks
- Tasks matching agent descriptions

## Available Agents

| Category | Agent | Purpose |
|----------|-------|---------|
| **Research** | codebase-explorer | Map project structure |
| | frontend-researcher | UI/React patterns |
| | backend-researcher | API/database analysis |
| | module-researcher | Deep-dive on specific modules |
| | pattern-researcher | Identify existing conventions |
| | dependency-researcher | Package analysis |
| | ui-researcher | Figma design extraction |
| **Questioning** | requirement-analyst | Clarify requirements |
| **Planning** | solution-architect | Architecture design |
| | task-planner | Break down into tasks |
| | test-spec-generator | Generate test specs |
| **Validation** | code-reviewer | Review code quality |
| | test-automator | Write and run tests |
| | security-auditor | Security scanning |
| | documentation-writer | Update docs |
| **Refactoring** | refactor-cleaner | Dead code cleanup, consolidation |
| **Documentation** | project-scanner | Generate project docs |
| **Implementation** | full-stack-developer | Find code locations |
| **Utility** | review-generator | Create review summaries |
| | summarize-agent | Compress content |

## Requirements

- [ ] Use agents immediately when task matches description
- [ ] No prompt confirmation needed - just invoke
- [ ] Launch independent agents in parallel
- [ ] Use `subagent_type` parameter correctly

## Parallel Execution

```
Task(codebase-explorer, "...") | Task(pattern-researcher, "...")
```

Launch multiple agents in single message for independent tasks.

## Multi-Perspective Analysis

For complex decisions, get multiple viewpoints:
```
Task(frontend-researcher) + Task(backend-researcher) + Task(security-auditor)
```

## References
- `.claude/agents/` - Agent definitions
- Task tool documentation
