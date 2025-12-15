# Orchestration Sub-Agents

This directory contains sub-agent definitions for workflow orchestration and coordination.

## Overview

Orchestration agents coordinate multi-phase RQPIV workflows, managing transitions between phases and ensuring quality gates are enforced.

## Available Agents

### workflow-orchestrator

| Attribute | Value |
|-----------|-------|
| Model | opus |
| Tools | Read, Write, Bash |
| Skills | context-preservation |

**Purpose:** Coordinate complex development workflows across all RQPIV phases.

**Use When:**
- Running full RQPIV workflow via `/rqpiv` command
- Managing multi-session projects
- Coordinating multiple sub-agents
- Tracking complex feature development

**Key Capabilities:**
- Phase transition management
- Session state tracking
- Quality gate enforcement
- Sub-agent coordination
- Progress reporting
- Summary generation

## Session Management

The orchestrator creates and maintains session directories:

```
docs/sessions/{date}-{slug}/
├── session.md        # Session tracking file
├── research/         # Research artifacts
├── specs/            # Requirements documents
├── plans/            # Architecture and implementation plans
├── reviews/          # Validation reports
└── summary.md        # Final feature summary
```

## Phase Transitions

The orchestrator enforces quality gates between phases:

| Transition | Gate Requirements |
|------------|-------------------|
| R → Q | Research artifacts complete, no gaps |
| Q → P | Questions answered, requirements confirmed |
| P → I | Architecture and plan approved |
| I → V | All tasks complete, deviations documented |
| V → Done | All validations passed |

## Usage Example

```
# Full workflow orchestration
/rqpiv implement user authentication

# The orchestrator will:
# 1. Initialize session
# 2. Coordinate research sub-agents
# 3. Manage questioning phase
# 4. Guide planning phase
# 5. Oversee implementation
# 6. Ensure validation completes
# 7. Generate final summary
```

## Integration with Other Phases

The orchestrator delegates to phase-specific sub-agents:

- **Research:** codebase-explorer, module-researcher, etc.
- **Questioning:** requirement-analyst
- **Planning:** solution-architect, task-planner
- **Implementation:** backend-developer, frontend-developer, database-specialist
- **Validation:** code-reviewer, test-automator, security-auditor, documentation-writer

## Best Practices

1. **Always use for complex features** - The orchestrator ensures nothing is missed
2. **Trust the quality gates** - Don't skip phases even if they seem unnecessary
3. **Review session summaries** - They capture decisions and rationale
4. **Resume interrupted sessions** - The orchestrator maintains state for continuation
