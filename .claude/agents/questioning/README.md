# Questioning Sub-Agents

This directory contains sub-agents for the **Questioning (Q)** phase of the RQPIV workflow.

## Purpose

Questioning sub-agents analyze research findings and user requests to generate clarifying questions, parse user intent, and create validated requirement documents.

## Available Agents

| Agent | Model | Purpose |
|-------|-------|---------|
| `requirement-analyst` | opus | Analyze research, generate questions, validate requirements |

## Agent Selection Guide

| Scenario | Agent to Use |
|----------|--------------|
| After research phase completion | requirement-analyst |
| Ambiguous user requirements | requirement-analyst |
| Non-technical user requests | requirement-analyst |
| Complex feature planning | requirement-analyst |

## Usage

These agents are invoked via the Claude Code Task tool:

```
Task tool with subagent_type: "requirement-analyst"
```

Or automatically through the `/phase-question` slash command.

## Output Locations

| Output Type | Location |
|-------------|----------|
| Parsed Intent | `docs/specs/parsed-intent-{session}.md` |
| Questions | `docs/specs/questions-{session}.md` |
| Requirements | `docs/specs/requirements-{session}.md` |

## Quality Gates

Before transitioning to Planning phase:
- [ ] All blocking questions answered
- [ ] No contradictory requirements
- [ ] Technical feasibility confirmed
- [ ] User has explicitly confirmed requirements

## Adding New Agents

1. Create a new `.md` file in this directory
2. Include YAML frontmatter with: name, description, tools, model
3. Define responsibilities, protocol, output format, and constraints
4. Update this README with the new agent
