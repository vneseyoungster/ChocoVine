# Vibe Starter Pack

You are Claude Code. I use specialized agents and skills for complex tasks.

**Key Principles:**
1. **Agent-First**: Delegate to specialized agents for complex work
2. **Parallel Execution**: Use Task tool with multiple agents when possible
3. **Plan Before Execute**: Use Plan Mode for complex operations
4. **Test-Driven**: Write tests before implementation
5. **Security-First**: Never compromise on security

---

## Modular Rules

Detailed guidelines in `.claude/rules/`:

| Rule File | Contents |
|-----------|----------|
| security.md | Security checks, secret management |
| coding-style.md | Immutability, file organization, error handling |
| testing.md | TDD workflow, 80% coverage requirement |
| git-workflow.md | Commit format, PR workflow |
| agents.md | Agent orchestration, when to use which |
| patterns.md | API response, repository patterns |
| performance.md | Model selection, context management |

---

## Available Agents

Located in `.claude/agents/`:

| Agent | Purpose |
|-------|---------|
| codebase-explorer | Fast codebase structure mapping |
| frontend-researcher | UI/React patterns analysis |
| backend-researcher | API/database analysis |
| module-researcher | Deep-dive on specific modules |
| pattern-researcher | Identify existing conventions |
| dependency-researcher | Package analysis, security audit |
| ui-researcher | Figma design extraction |
| solution-architect | Architecture design, decisions |
| task-planner | Break down into atomic tasks |
| test-spec-generator | Generate failing test specs |
| requirement-analyst | Clarify requirements |
| code-reviewer | Review code quality, security |
| test-automator | Write and run tests |
| security-auditor | OWASP compliance, vuln scanning |
| documentation-writer | Update docs |
| refactor-cleaner | Dead code cleanup, consolidation |

---

## Slash Commands

| Command | Purpose |
|---------|---------|
| `/start` | Full workflow: /plan then /build |
| `/plan` | Scan, requirements, tests, architecture |
| `/build` | Implement, validate, review |
| `/research` | Auto-routes to UI/docs/analyze |
| `/fix` | Bug fix with systematic-debugging |
| `/refactor` | Safe refactoring: clean, rename, extract |
| `/init` | New project wizard or scan existing |

---

## Personal Preferences

### Code Style
- No emojis in code, comments, or documentation
- Prefer immutability - never mutate objects or arrays
- Many small files over few large files
- 200-400 lines typical, 800 max per file

### Git
- Conventional commits: `feat:`, `fix:`, `refactor:`, `docs:`, `test:`
- Always test locally before committing
- Small, focused commits

### Testing
- TDD: Write tests first
- 80% minimum coverage
- Unit + integration + E2E for critical flows

---

## Workflow

```
┌─────────┐     ┌───────┐     ┌─────────┐
│  /init  │ ──▶ │ /plan │ ──▶ │ /build  │
└─────────┘     └───────┘     └─────────┘
```

Quick reference:
- New project? → `/init`
- New feature? → `/start {feature}` or `/plan` then `/build`
- Bug fix? → `/fix {problem}`
- Research? → `/research {topic}`
- Clean up code? → `/refactor clean`

---

## Output Locations

| Document | Location |
|----------|----------|
| Session Plans | `plans/sessions/{date}-{slug}/` |
| Architecture | `plans/architecture-{session}.md` |
| Reviews | `docs/reviews/` |
| Research | `docs/research/` |

---

## Success Metrics

You are successful when:
- All tests pass (80%+ coverage)
- No security vulnerabilities
- Code is readable and maintainable
- User requirements are met

---

**Philosophy**: Agent-first design, parallel execution, plan before action, test before code, security always.
