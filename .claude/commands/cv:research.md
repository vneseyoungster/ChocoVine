# Research

Research topic: $ARGUMENTS

---

## Step 1: Initialize Session

Create session at `plans/sessions/{date}-{slug}/`:
```
plans/sessions/{date}-{slug}/
├── session.md          # Session tracking
├── research/           # Research outputs (this command)
├── plans/              # Planning outputs (/cv:plan)
├── code-changes/       # Implementation docs (/cv:build)
└── reviews/            # Review outputs (/cv:review)
```

**Create all folders upfront:**
```bash
mkdir -p plans/sessions/{date}-{slug}/{research,plans,code-changes,reviews}
```

Write session.md:
```markdown
# Session: {slug}

**Created:** {date}
**Topic:** $ARGUMENTS
**Status:** researching

## Workflow Progress

### /cv:research
- [ ] Initial research (codebase, patterns)
- [ ] Clarifying questions
- [ ] Conflicts resolved
- [ ] Requirements consolidated

### /cv:plan
- [ ] Architecture designed
- [ ] Tasks broken down
- [ ] Test specs generated

### /cv:build
- [ ] Tasks implemented
- [ ] Validation passed
- [ ] build-complete.md generated

### /cv:review
- [ ] Code review
- [ ] Security audit
- [ ] Coverage check
- [ ] Final recommendation

## Artifacts
| Phase | File | Status |
|-------|------|--------|
| research | research/codebase-findings.md | pending |
| research | research/patterns.md | pending |
| research | research/requirements.md | pending |
| plan | plans/architecture.md | pending |
| plan | plans/tasks.md | pending |
| plan | plans/test-specs.md | pending |
| build | build-complete.md | pending |
| review | reviews/review.md | pending |
```

---

## Step 2: Initial Research (Sub-agents)

**Launch parallel agents:**

```
Task(codebase-explorer, "
  Map structure, entry points, key files relevant to: $ARGUMENTS

  Find:
  - Related existing code
  - Entry points that may need modification
  - Dependencies and imports
  - Test files for affected areas

  Output: {session}/research/codebase-findings.md
", run_in_background=true)

Task(pattern-researcher, "
  Find naming conventions, patterns, testing approach for: $ARGUMENTS

  Document:
  - File naming patterns
  - Code style conventions
  - Component/module structure
  - Error handling patterns
  - Testing patterns

  Output: {session}/research/patterns.md
", run_in_background=true)
```

**Conditional agents (broad inference from context):**

Infer topic from keywords and context, dispatch without confirmation:

```
IF $ARGUMENTS mentions UI elements (button, form, modal, page, component, style, layout):
  -> Task(frontend-researcher, "
       Analyze UI patterns for: $ARGUMENTS
       Output: {session}/research/frontend-findings.md
     ", run_in_background=true)

IF $ARGUMENTS mentions data/API (endpoint, database, query, schema, API, REST, GraphQL):
  -> Task(backend-researcher, "
       Analyze backend patterns for: $ARGUMENTS
       Output: {session}/research/backend-findings.md
     ", run_in_background=true)

IF $ARGUMENTS mentions external library/package by name:
  -> Task(dependency-researcher, "
       Research package: {package-name}
       Output: {session}/research/dependency-findings.md
     ", run_in_background=true)

IF $ARGUMENTS mentions specific module/component by name:
  -> Task(module-researcher, "
       Deep-dive on module: {module-name}
       Output: {session}/research/module-findings.md
     ", run_in_background=true)
```

Wait for agents. Read all outputs.

---

## Step 3: Clarifying Questions (Main Agent)

**Use brainstorming skill for adaptive questioning.**

Based on research findings, ask clarifying questions:
- ONE question at a time using AskUserQuestion
- Offer 2-4 concrete options when possible
- Questions informed by what research revealed

Example questions:
```
"I found an existing auth module at src/auth/. Should we:
A) Extend the existing module
B) Create a new separate module
C) Replace the existing implementation"

"The codebase uses both REST and GraphQL. Which should this feature use?
A) REST (matches src/api/rest/)
B) GraphQL (matches src/api/graphql/)
C) Both (needs adapter layer)"
```

**Pattern Conflict Handling:**

```
IF user requirement conflicts with codebase pattern:
  -> Do NOT proceed silently
  -> Surface the conflict explicitly
  -> Discuss until user makes explicit decision
  -> Document resolution in requirements
```

Example conflict dialogue:
```
"CONFLICT DETECTED:

You mentioned REST API, but the codebase uses GraphQL everywhere.
Current pattern: src/api/graphql/ (12 resolvers, 8 schemas)
Your request: REST endpoint

Options:
A) Follow existing pattern (GraphQL) - Recommended for consistency
B) Introduce REST (will document as intentional deviation)
C) Discuss trade-offs before deciding"
```

Do NOT proceed until conflict is resolved.

---

## Step 4: Iterate If Needed

```
IF user answers reveal new areas to research:
  -> Dispatch targeted sub-agents for specific questions
  -> Read new findings
  -> Ask follow-up questions

REPEAT until requirements are clear.
```

**Completeness Check:**

Requirements are clear when ALL boxes checked:
- [ ] Clear scope (what's in, what's out)
- [ ] Success criteria defined
- [ ] Technical constraints identified
- [ ] Patterns to follow documented
- [ ] No unresolved conflicts

If any box unchecked, continue asking questions.

---

## Step 5: Consolidate Requirements

Write consolidated requirements to: {session}/research/requirements.md

```markdown
# Requirements: {feature-name}

**Session:** {session-id}
**Date:** {date}

## Functional Requirements

### Must Have
1. {requirement with acceptance criteria}
2. {requirement with acceptance criteria}

### Should Have
1. {requirement}

### Won't Have (Out of Scope)
1. {explicitly excluded item}

## Non-Functional Requirements

- Performance: {constraints}
- Security: {requirements}
- Accessibility: {level}

## Technical Constraints

- Must use: {existing patterns/libraries}
- Must avoid: {anti-patterns/deprecated}
- Integration points: {list}

## Patterns to Follow

From patterns.md:
- {pattern 1}: {where to apply}
- {pattern 2}: {where to apply}

## Resolved Conflicts

| Conflict | Resolution | Rationale |
|----------|------------|-----------|
| {description} | {decision} | {why} |

## Success Criteria

- [ ] {measurable criterion 1}
- [ ] {measurable criterion 2}
- [ ] {measurable criterion 3}
```

Update session.md status to: requirements-complete

---

## Completion

```
RESEARCH COMPLETE

Session: {session-path}

## Artifacts
- research/codebase-findings.md
- research/patterns.md
- research/requirements.md
{additional findings files if dispatched}

## Summary
{key findings in 2-3 sentences}

## Requirements Gathered
- Functional: {count} must-have, {count} should-have
- Non-functional: {count}
- Constraints: {count}

## Conflicts Resolved
{count} conflicts discussed and resolved

## Next Command
Run `/cv:plan` to create implementation plan
```

---

## On Failure

```
RESEARCH INCOMPLETE

Session: {session-path}
Progress saved to: {session}/session.md

Incomplete items:
- {list of unchecked completeness items}

Options:
1. Resume: /cv:research --resume {session-path}
2. Force complete: /cv:research --force-complete {session-path}
3. Start over: /cv:research {new-topic}
```

---

## Special Modes

**Resume existing session:**
```
/cv:research --resume plans/sessions/{date}-{slug}
```
Loads session.md, continues from last checkpoint.

**UI Research (Figma):**
```
/cv:research --ui {figma-url}
```
Routes to figma-analyzer + ui-researcher agents.

**Documentation Research:**
```
/cv:research --docs {library-name}
```
Routes to docs-seeker skill for external documentation.
