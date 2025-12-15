# Research Sub-Agents

This directory contains sub-agent definitions for the Research (R) phase of the RQPIV workflow.

## Available Sub-Agents

| Agent | Model | Purpose |
|-------|-------|---------|
| `codebase-explorer` | haiku | Fast codebase structure mapping |
| `module-researcher` | sonnet | Deep module/component analysis |
| `frontend-researcher` | sonnet | Frontend architecture analysis |
| `backend-researcher` | sonnet | Backend architecture analysis |
| `dependency-researcher` | haiku | Package/security auditing |
| `pattern-researcher` | sonnet | Code pattern/convention detection |

## Usage

These sub-agents are invoked automatically during the Research phase of the RQPIV workflow, or can be called directly using the Task tool.

### Selection Guide

| Task Type | Primary Agent | Secondary Agent |
|-----------|---------------|-----------------|
| New project | codebase-explorer | pattern-researcher |
| Frontend changes | frontend-researcher | pattern-researcher |
| Backend changes | backend-researcher | pattern-researcher |
| Module modification | module-researcher | dependency-researcher |
| Security review | dependency-researcher | backend-researcher |
| Refactoring | pattern-researcher | module-researcher |

## File Format

Each sub-agent file uses Markdown with YAML frontmatter:

```markdown
---
name: agent-name
description: What this agent does and when to use it
tools: Tool1, Tool2, Tool3
model: haiku|sonnet|opus
---

# Agent Name

[Agent instructions and protocols]
```

## Adding New Research Agents

1. Create a new `.md` file in this directory
2. Add required frontmatter (name, description, tools, model)
3. Define the agent's responsibilities and protocols
4. Update the CLAUDE.md file to include the new agent
