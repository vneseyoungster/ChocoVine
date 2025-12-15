# Planning Sub-Agents

This directory contains sub-agent definitions for the **Planning (P)** phase of the RQPIV workflow.

## Overview

The planning phase transforms validated requirements into executable implementation plans through two specialized sub-agents working in sequence.

## Sub-Agents

### 1. Solution Architect (`solution-architect.md`)

| Attribute | Value |
|-----------|-------|
| Model | `opus` |
| Tools | Read, Write, Glob, Grep |
| Input | Requirements from `docs/specs/`, Research from `docs/research/` |
| Output | `docs/plans/architecture-{session}.md` |

**Purpose:** Creates high-level architecture plans with design decisions, component design, and risk assessment.

**When to Use:**
- Significant feature implementations
- System refactoring
- New module design
- Technology decisions

**Key Outputs:**
- Design decisions with options considered
- Component responsibilities and interfaces
- Data flow diagrams
- Risk assessment matrix
- Integration points

---

### 2. Task Planner (`task-planner.md`)

| Attribute | Value |
|-----------|-------|
| Model | `sonnet` |
| Tools | Read, Write, Glob, Grep |
| Input | Architecture from `docs/plans/architecture-*.md` |
| Output | `docs/plans/implementation-{session}.md` |

**Purpose:** Breaks down architecture into atomic, executable tasks with exact file paths, line numbers, and verification steps.

**When to Use:**
- After architecture is approved
- Converting design to implementation steps
- Creating detailed task lists

**Key Outputs:**
- Atomic tasks with file operations
- Exact file paths and line ranges
- Verification commands
- Commit messages
- Task dependencies

---

## Workflow

```
Requirements (docs/specs/)
        │
        ▼
┌─────────────────────┐
│  solution-architect │  ◄── Creates architecture
└─────────────────────┘
        │
        ▼
Architecture Document (docs/plans/architecture-*.md)
        │
        ▼
    [User Approval]     ◄── GATE: Must approve before proceeding
        │
        ▼
┌─────────────────────┐
│    task-planner     │  ◄── Creates implementation plan
└─────────────────────┘
        │
        ▼
Implementation Plan (docs/plans/implementation-*.md)
        │
        ▼
    [User Approval]     ◄── GATE: Must approve before implementing
        │
        ▼
    Implementation Phase
```

## Usage Examples

### Invoking Solution Architect
```
Use the solution-architect sub-agent to design the authentication system
based on the validated requirements in docs/specs/requirements-auth.md
```

### Invoking Task Planner
```
Use the task-planner sub-agent to break down the approved architecture
in docs/plans/architecture-auth.md into implementation tasks
```

## Quality Gates

1. **Architecture Approval**: User must explicitly approve architecture before task breakdown
2. **Plan Approval**: User must approve implementation plan before coding begins

## Related Skills

- `architecture-planning` - Templates and patterns for architecture documents
- `task-breakdown` - Task templates and verification approaches

## Output Locations

| Document | Location |
|----------|----------|
| Architecture | `docs/plans/architecture-{session}.md` |
| Implementation Plan | `docs/plans/implementation-{session}.md` |
| Decision Records | `docs/plans/adr-{number}-{title}.md` |
