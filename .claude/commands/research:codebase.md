# Research Codebase

Analyze codebase for: $ARGUMENTS

## Overview

This command is **Phase 1** of the research flow. It performs comprehensive codebase research to understand existing code, patterns, and architecture before any planning or implementation.

**This phase focuses ONLY on understanding. No planning, no questions, no implementation.**

---

## Phase Flow Position

```
┌─────────────────────┐
│  /research:codebase │  ← YOU ARE HERE (Phase 1)
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  /research:feature  │  ← Phase 2 (Next)
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   /research:plan    │  ← Phase 3
└─────────────────────┘
```

---

## CRITICAL: Agent-First Research

**The main agent MUST NOT perform research directly.** All research work MUST be delegated to specialized research sub-agents to reduce context length.

### Mandatory Agent Delegation

1. **ALWAYS** invoke research sub-agents for codebase analysis
2. **NEVER** use Grep, Glob, or Read tools directly for research in the main context
3. **WAIT** for agent outputs before proceeding
4. **ONLY** read the summarized findings from agent outputs

### Why Agent-First?

- Reduces main agent context usage significantly
- Specialized agents have focused prompts for their domain
- Research artifacts are saved to disk for later reference
- Main agent only needs summaries, not raw search results

---

## Phase 1: Initialize Session

### Create Session Directory

```
plans/sessions/{date}-{task-slug}/
├── session.md        # Session tracking
├── research/         # Research findings (this phase)
├── specs/            # Requirements (Phase 2)
├── plans/            # Architecture & tasks (Phase 2)
└── reviews/          # (for validation phase)
```

### Session File Template

```markdown
# Session: {task-name}

**Started:** {date}
**Current Phase:** 🔍 Codebase Research

## Task Description
{user request}

## Research Status
- [ ] Codebase structure mapped
- [ ] Patterns identified
- [ ] Dependencies analyzed

## Phase Progress
- [x] Phase 1: Codebase Research ← Current
- [ ] Phase 2: Test Specification
- [ ] Phase 3: Architecture Planning
- [ ] Phase 4: Implementation
- [ ] Phase 5: Validation
```

---

## Phase 2: Research (Agent-Only)

### CRITICAL: Delegate ALL Research to Sub-Agents

**DO NOT perform any research directly in the main agent context.**

Use the Task tool to invoke research sub-agents. The main agent should:
1. Launch research agents IN PARALLEL using Task tool
2. Wait for agent completion
3. Read only the output summaries - do not re-research

### Agent Selection Matrix

Select appropriate researchers based on task type:

| Task Type | Primary Agent | Secondary Agent | Launch In Parallel |
|-----------|---------------|-----------------|-------------------|
| New project | codebase-explorer | pattern-researcher | Yes |
| Frontend work | frontend-researcher | pattern-researcher | Yes |
| Backend work | backend-researcher | pattern-researcher | Yes |
| Specific module | module-researcher | dependency-researcher | Yes |
| Security audit | dependency-researcher | backend-researcher | Yes |
| Refactoring | pattern-researcher | module-researcher | Yes |

### Agent Invocation Template

```
Launch Task tool with:
- subagent_type: [researcher-type]
- prompt: "Research [specific aspect] for: $ARGUMENTS

  Save findings to: plans/sessions/{session}/research/[output-file].md

  Focus on:
  - [specific research goals]
  - [patterns to identify]
  - [constraints to document]"
```

### Research Outputs

Agents will store findings in session directory:
- `plans/sessions/{session}/research/codebase-map.md`
- `plans/sessions/{session}/research/patterns.md`
- `plans/sessions/{session}/research/dependencies.md`

---

## Phase 3: Compile Findings

### After Agents Complete

Read ONLY the summary sections from agent outputs:
1. Load `research/codebase-map.md` - read summary
2. Load `research/patterns.md` - read key patterns
3. Load `research/dependencies.md` - read constraints

**DO NOT re-search or expand on agent findings. Trust the agent outputs.**

### Create Research Summary

Create `plans/sessions/{session}/research/summary.md`:

```markdown
# Research Summary: [Task Name]

## Project Overview
- Type: [webapp, library, CLI, etc.]
- Stack: [languages, frameworks]
- Size: [small/medium/large]

## Key Findings

### Codebase Structure
[Summary from codebase-map.md]

### Patterns Detected
[Summary from patterns.md]
- Naming conventions: ...
- File organization: ...
- Coding style: ...

### Dependencies & Constraints
[Summary from dependencies.md]
- Key dependencies: ...
- Version constraints: ...
- Compatibility notes: ...

### Integration Points
[Where new code will connect to existing code]

### Potential Challenges
[Identified obstacles or complexities]

## Ready for Test Specification
This research is ready for `/research:feature` to gather requirements and generate tests.
```

---

## Phase 4: Complete

### Update Session Tracking

Update `session.md`:
```markdown
**Current Phase:** Research Complete

## Research Complete
- [x] Codebase structure mapped
- [x] Patterns identified
- [x] Dependencies analyzed

## Artifacts
- research/codebase-map.md
- research/patterns.md
- research/dependencies.md
- research/summary.md

## Ready For
- `/research:feature` to gather requirements and generate test specifications
```

### Announce Completion

```
CODEBASE RESEARCH COMPLETE

Session: plans/sessions/{date}-{task}/

Research Findings:
├── research/codebase-map.md   ✓
├── research/patterns.md       ✓
├── research/dependencies.md   ✓
└── research/summary.md        ✓

Key Findings:
- [1-2 sentence summary of most important findings]

Next Step:
→ /research:feature [session-path] - Gather requirements and generate tests
```

---

## Quality Checklist

Before completing this phase:
- [ ] Session directory created
- [ ] All research agents completed
- [ ] codebase-map.md exists
- [ ] patterns.md exists
- [ ] dependencies.md exists
- [ ] summary.md compiled
- [ ] No questions asked (save for Phase 2)
- [ ] No planning done (save for Phase 2)

---

## Error Handling

### If research fails
```
Research could not complete for this task.
Gap identified: [description]
Please provide guidance or additional context.
```

### If no relevant code found
```
No existing code found related to: [task]
This appears to be a greenfield implementation.
Proceeding with minimal research findings.
```

---

## Example Usage

```
/research:codebase Add user authentication with JWT tokens

Output:
🔍 Starting Codebase Research Phase...

Creating session: plans/sessions/2024-01-15-auth/

Invoking research sub-agents...
- backend-researcher: Analyzing API structure
- pattern-researcher: Detecting authentication patterns

[Agents complete]

Research complete. Key findings:
- Express.js backend with middleware pattern
- No existing auth implementation
- bcrypt and jsonwebtoken in package.json
- Routes follow /api/v1/{resource} pattern

Session: plans/sessions/2024-01-15-auth/
├── research/codebase-map.md   ✓
├── research/patterns.md       ✓
├── research/dependencies.md   ✓
└── research/summary.md        ✓

Next: /research:feature plans/sessions/2024-01-15-auth/
```

---

## Related Commands

| Command | Purpose |
|---------|---------|
| `/research:feature` | Phase 2: Requirements & test specification |
| `/research:plan` | Phase 3: Architecture & planning |
| `/research:ui` | Standalone: Figma design research |
| `/research:docs` | Standalone: External documentation |
