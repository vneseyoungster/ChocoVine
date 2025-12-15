# Product Requirements Document (PRD)
# RQPIV Workflow System for Claude Code

**Version:** 1.0  
**Date:** December 14, 2025  
**Author:** [Your Name]  
**Status:** Draft  

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Problem Statement](#2-problem-statement)
3. [Product Vision & Goals](#3-product-vision--goals)
4. [Target Users](#4-target-users)
5. [System Architecture Overview](#5-system-architecture-overview)
6. [Development Phases](#6-development-phases)
   - [Phase 1: Foundation & Research Infrastructure](#phase-1-foundation--research-infrastructure)
   - [Phase 2: Questioning & Requirement Analysis](#phase-2-questioning--requirement-analysis)
   - [Phase 3: Planning Infrastructure](#phase-3-planning-infrastructure)
   - [Phase 4: Implementation Framework](#phase-4-implementation-framework)
   - [Phase 5: Validation & Quality Gates](#phase-5-validation--quality-gates)
   - [Phase 6: Orchestration & Integration](#phase-6-orchestration--integration)
7. [Technical Requirements](#7-technical-requirements)
8. [Success Metrics](#8-success-metrics)
9. [Risks & Mitigations](#9-risks--mitigations)
10. [Appendices](#10-appendices)

---

## 1. Executive Summary

### 1.1 Product Overview

The **RQPIV Workflow System** is a comprehensive context-engineering framework for Claude Code that implements a structured development methodology through specialized sub-agents and skills. The system transforms Claude Code's main agent into a pure orchestrator that delegates all research, analysis, planning, implementation, and validation tasks to specialized sub-agents operating in isolated context windows.

### 1.2 Key Value Proposition

- **Context Preservation**: Prevents context window pollution by isolating tasks to sub-agents
- **Quality Assurance**: Enforces mandatory phases with quality gates
- **Consistency**: Standardizes development workflows across teams
- **Scalability**: Works for both new and large existing codebases
- **Non-Developer Friendly**: Structured questioning phase helps non-technical users articulate requirements

### 1.3 RQPIV Methodology

| Phase | Name | Purpose |
|-------|------|---------|
| **R** | Research | Gather codebase context via specialized researcher sub-agents |
| **Q** | Questioning | Clarify requirements through structured inquiry |
| **P** | Planning | Create detailed, executable implementation plans |
| **I** | Implementation | Execute plans following clean architecture principles |
| **V** | Validation | Verify quality, security, tests, and documentation |

---

## 2. Problem Statement

### 2.1 Current Challenges

1. **Context Window Exhaustion**: In complex tasks, the main agent's context fills rapidly with research data, leaving insufficient space for implementation reasoning.

2. **Inconsistent Quality**: Without enforced phases, agents may skip research or validation, leading to suboptimal solutions.

3. **Requirement Ambiguity**: Non-developer users struggle to articulate technical requirements, leading to implementation misalignment.

4. **Lost Institutional Knowledge**: Research findings and architectural decisions are not preserved for future sessions.

5. **Code Quality Variance**: Without standardized skills, code quality depends on prompt quality.

### 2.2 Impact

- Extended development cycles due to rework
- Technical debt accumulation
- Frustrated non-technical stakeholders
- Inconsistent codebase quality
- Wasted tokens on repeated research

---

## 3. Product Vision & Goals

### 3.1 Vision Statement

> Create an intelligent development orchestration system where Claude Code's main agent acts as a skilled project manager, delegating specialized tasks to expert sub-agents while maintaining a clean, focused context for high-level decision making.

### 3.2 Primary Goals

| Goal | Description | Success Indicator |
|------|-------------|-------------------|
| **G1** | Reduce main agent context usage by 60% | Measure context utilization before/after |
| **G2** | Enforce mandatory RQPIV phases | 100% workflow compliance |
| **G3** | Improve code quality consistency | Static analysis score improvement |
| **G4** | Enable non-developers to use effectively | User satisfaction surveys |
| **G5** | Preserve research across sessions | Research artifacts stored and reusable |

### 3.3 Non-Goals (Out of Scope)

- Integration with external project management tools (Jira, Linear)
- Custom model training or fine-tuning
- Multi-repository orchestration (single repo focus)
- Real-time collaboration features

---

## 4. Target Users

### 4.1 Primary Users

| User Type | Description | Key Needs |
|-----------|-------------|-----------|
| **Solo Developers** | Individual developers on personal/professional projects | Efficient workflow, quality enforcement |
| **Development Teams** | Teams sharing Claude Code workflows | Consistency, knowledge sharing |
| **Non-Technical Users** | Product managers, founders, designers | Guided requirement specification |
| **Enterprise Developers** | Developers in regulated environments | Audit trails, quality gates |

### 4.2 User Stories

**US-1**: As a developer, I want the agent to research the codebase before making changes, so that implementations follow existing patterns.

**US-2**: As a non-technical user, I want the agent to ask me clarifying questions, so that my requirements are accurately understood.

**US-3**: As a team lead, I want all code changes to pass through validation, so that quality standards are maintained.

**US-4**: As a developer, I want research findings preserved, so that I don't repeat investigations in future sessions.

**US-5**: As an enterprise developer, I want mandatory security reviews, so that compliance requirements are met.

---

## 5. System Architecture Overview

### 5.1 Component Hierarchy

```
┌─────────────────────────────────────────────────────────────────┐
│                     MAIN AGENT (Orchestrator)                    │
│                    - Receives user requests                      │
│                    - Delegates to sub-agents                     │
│                    - Maintains minimal context                   │
│                    - Makes phase transition decisions            │
└─────────────────────────────────────────────────────────────────┘
                                │
        ┌───────────────────────┼───────────────────────┐
        ▼                       ▼                       ▼
┌───────────────┐     ┌───────────────┐     ┌───────────────┐
│   RESEARCH    │     │   PLANNING    │     │IMPLEMENTATION │
│  SUB-AGENTS   │     │  SUB-AGENTS   │     │  SUB-AGENTS   │
│               │     │               │     │               │
│ - Explorers   │     │ - Architect   │     │ - Developers  │
│ - Researchers │     │ - Planner     │     │ - Specialists │
│ - Analysts    │     │               │     │               │
└───────────────┘     └───────────────┘     └───────────────┘
        │                       │                       │
        └───────────────────────┼───────────────────────┘
                                │
                    ┌───────────────────┐
                    │    VALIDATION     │
                    │    SUB-AGENTS     │
                    │                   │
                    │ - Code Reviewer   │
                    │ - Test Automator  │
                    │ - Security Audit  │
                    │ - Doc Writer      │
                    └───────────────────┘
                                │
        ┌───────────────────────┼───────────────────────┐
        ▼                       ▼                       ▼
┌───────────────┐     ┌───────────────┐     ┌───────────────┐
│    SKILLS     │     │   ARTIFACTS   │     │    HOOKS      │
│               │     │               │     │               │
│ Model-invoked │     │ docs/research │     │ Pre/Post exec │
│ capabilities  │     │ docs/plans    │     │ Quality gates │
│               │     │ docs/specs    │     │               │
└───────────────┘     └───────────────┘     └───────────────┘
```

### 5.2 Data Flow

```
User Request
     │
     ▼
┌─────────────────┐
│  R: RESEARCH    │──▶ Findings stored in docs/research/
└─────────────────┘
     │
     ▼
┌─────────────────┐
│  Q: QUESTIONING │──▶ Validated requirements in docs/specs/
└─────────────────┘
     │
     ▼
┌─────────────────┐
│  P: PLANNING    │──▶ Implementation plan in docs/plans/
└─────────────────┘
     │
     ▼
┌─────────────────┐
│ I: IMPLEMENT    │──▶ Code changes with git commits
└─────────────────┘
     │
     ▼
┌─────────────────┐
│  V: VALIDATION  │──▶ Review reports, test results, docs
└─────────────────┘
     │
     ▼
  Complete ✓
```

### 5.3 File Structure

```
project-root/
├── .claude/
│   ├── agents/                    # Sub-agent definitions
│   │   ├── research/
│   │   │   ├── codebase-explorer.md
│   │   │   ├── module-researcher.md
│   │   │   ├── frontend-researcher.md
│   │   │   ├── backend-researcher.md
│   │   │   ├── dependency-researcher.md
│   │   │   └── pattern-researcher.md
│   │   ├── questioning/
│   │   │   └── requirement-analyst.md
│   │   ├── planning/
│   │   │   ├── solution-architect.md
│   │   │   └── task-planner.md
│   │   ├── implementation/
│   │   │   ├── backend-developer.md
│   │   │   ├── frontend-developer.md
│   │   │   └── database-specialist.md
│   │   ├── validation/
│   │   │   ├── code-reviewer.md
│   │   │   ├── test-automator.md
│   │   │   ├── security-auditor.md
│   │   │   └── documentation-writer.md
│   │   └── orchestration/
│   │       └── workflow-orchestrator.md
│   │
│   ├── skills/                    # Skill definitions
│   │   ├── research/
│   │   │   ├── codebase-mapping/
│   │   │   ├── dependency-analysis/
│   │   │   └── pattern-detection/
│   │   ├── questioning/
│   │   │   ├── requirement-clarification/
│   │   │   └── user-intent-parser/
│   │   ├── planning/
│   │   │   ├── architecture-planning/
│   │   │   └── task-breakdown/
│   │   ├── implementation/
│   │   │   ├── clean-code/
│   │   │   ├── api-design/
│   │   │   ├── component-design/
│   │   │   ├── error-handling/
│   │   │   └── migration/
│   │   ├── validation/
│   │   │   ├── code-review/
│   │   │   ├── test-generation/
│   │   │   ├── security-scan/
│   │   │   └── documentation/
│   │   └── shared/
│   │       ├── git-workflow/
│   │       └── context-preservation/
│   │
│   ├── commands/                  # Slash commands
│   │   ├── rqpiv-start.md
│   │   ├── phase-research.md
│   │   ├── phase-question.md
│   │   ├── phase-plan.md
│   │   ├── phase-implement.md
│   │   └── phase-validate.md
│   │
│   └── hooks/                     # Event hooks
│       ├── pre-phase-transition.sh
│       └── post-implementation.sh
│
├── docs/                          # Generated artifacts
│   ├── research/
│   ├── specs/
│   ├── plans/
│   └── reviews/
│
└── CLAUDE.md                      # Project context file
```

---

## 6. Development Phases

---

## Phase 1: Foundation & Research Infrastructure

**Duration:** 2-3 weeks
**Priority:** Critical
**Dependencies:** None
**Status:** ✅ COMPLETED (December 14, 2025)  

### 1.1 Objectives

- Establish project structure and conventions
- Implement core research sub-agents
- Create foundational skills for research phase
- Set up artifact storage patterns

### 1.2 Deliverables

#### 1.2.1 Project Structure Setup

**Task 1.2.1.1: Create Directory Structure**
```
.claude/
├── agents/
│   └── research/
├── skills/
│   └── research/
├── commands/
└── hooks/
docs/
├── research/
├── specs/
├── plans/
└── reviews/
```

**Acceptance Criteria:**
- [ ] All directories created
- [ ] .gitkeep files added where needed
- [ ] README.md in each major directory explaining purpose

#### 1.2.2 Research Sub-Agents

**Sub-Agent: `codebase-explorer`**

| Attribute | Value |
|-----------|-------|
| File | `.claude/agents/research/codebase-explorer.md` |
| Model | `haiku` |
| Tools | `Read, Glob, Grep, Bash` |
| Purpose | Fast, lightweight codebase structure mapping |

**Specification:**
```markdown
---
name: codebase-explorer
description: PROACTIVELY explore and map codebase structure. Use immediately 
  when understanding project architecture, directory layout, or file organization 
  is needed. Fast, read-only exploration.
tools: Read, Glob, Grep, Bash
model: haiku
---

# Codebase Explorer

You are a fast, efficient codebase exploration specialist. Your role is to 
quickly map and understand project structure without deep analysis.

## Primary Responsibilities
1. Map directory structure and organization
2. Identify key configuration files
3. Detect project type and framework
4. List main entry points and important files

## Exploration Protocol
1. Run `ls -la` and `tree -L 2` for structure overview
2. Check for common config files (package.json, pyproject.toml, etc.)
3. Identify src/, lib/, tests/ directories
4. Note any monorepo or workspace patterns

## Output Format
Return a structured report with:
- Project type (Node.js, Python, etc.)
- Framework detected (React, FastAPI, etc.)
- Directory structure summary
- Key files identified
- Recommended next researchers to invoke

## Constraints
- Read-only operations only
- Maximum 30 seconds per exploration
- Return concise, actionable summaries
- Do not analyze code logic, only structure
```

**Acceptance Criteria:**
- [ ] Sub-agent file created with correct frontmatter
- [ ] Correctly identifies project type for Node.js, Python, Go projects
- [ ] Returns structured output within 30 seconds
- [ ] Does not attempt write operations

---

**Sub-Agent: `module-researcher`**

| Attribute | Value |
|-----------|-------|
| File | `.claude/agents/research/module-researcher.md` |
| Model | `sonnet` |
| Tools | `Read, Glob, Grep, Bash` |
| Purpose | Deep analysis of specific modules and components |

**Specification:**
```markdown
---
name: module-researcher
description: Deep-dive research on specific modules, classes, or components. 
  MUST BE USED for understanding existing implementations before making changes.
  Analyzes dependencies, interfaces, and patterns.
tools: Read, Glob, Grep, Bash
model: sonnet
---

# Module Researcher

You are a deep-dive code analysis specialist. Your role is to thoroughly 
understand specific modules, their dependencies, and how they fit into 
the broader system.

## Primary Responsibilities
1. Analyze module structure and organization
2. Map internal and external dependencies
3. Document public interfaces and contracts
4. Identify patterns and conventions used
5. Assess modification risk and impact

## Research Protocol
1. Read main module files completely
2. Trace imports and dependencies
3. Identify exported interfaces
4. Check for tests and documentation
5. Note coding patterns and conventions

## Output Format
Provide detailed report including:

### Module Overview
- Purpose and responsibility
- File locations

### Dependencies
- Internal dependencies (same project)
- External dependencies (packages)
- Dependency direction (who depends on this)

### Public Interface
- Exported functions/classes
- Type signatures
- Expected inputs/outputs

### Patterns Observed
- Design patterns used
- Naming conventions
- Error handling approach

### Modification Risk Assessment
- High/Medium/Low risk areas
- Potential impact of changes
- Recommended approach

## Constraints
- Read-only operations
- Focus on requested module scope
- Maximum 2 minutes per module
- Reference specific file paths and line numbers
```

**Acceptance Criteria:**
- [ ] Accurately maps module dependencies
- [ ] Identifies public interfaces correctly
- [ ] Provides risk assessment
- [ ] Includes specific file paths and line numbers
- [ ] Completes within 2 minutes

---

**Sub-Agent: `frontend-researcher`**

| Attribute | Value |
|-----------|-------|
| File | `.claude/agents/research/frontend-researcher.md` |
| Model | `sonnet` |
| Tools | `Read, Glob, Grep, Bash` |
| Purpose | Frontend-specific architecture analysis |

**Specification:**
```markdown
---
name: frontend-researcher
description: Research frontend architecture including React/Vue/Angular patterns, 
  state management, component hierarchy, and styling approaches. Use for any 
  UI/UX related analysis or before frontend modifications.
tools: Read, Glob, Grep, Bash
model: sonnet
---

# Frontend Researcher

You are a frontend architecture specialist with deep expertise in modern 
JavaScript frameworks, state management, and UI patterns.

## Primary Responsibilities
1. Analyze component hierarchy and organization
2. Map state management patterns (Redux, Zustand, Context, etc.)
3. Document routing structure
4. Identify styling approach (CSS modules, Tailwind, styled-components)
5. Check for design system usage

## Research Protocol
1. Identify frontend framework and version
2. Map component directory structure
3. Trace state management flow
4. Document routing configuration
5. Analyze build configuration

## Framework-Specific Checks

### React
- Check for hooks vs class components
- Identify context providers
- Note code-splitting patterns
- Check for SSR/SSG (Next.js, Remix)

### Vue
- Check for Composition API vs Options API
- Identify Vuex/Pinia usage
- Note Vue Router configuration

### Angular
- Check module organization
- Identify services and DI patterns
- Note lazy loading configuration

## Output Format
### Framework & Version
- Framework: [name]
- Version: [version]
- Meta-framework: [Next.js/Nuxt/etc. if applicable]

### Component Architecture
- Organization pattern (atomic, feature-based, etc.)
- Component tree overview
- Shared component library

### State Management
- Solution used
- Store structure
- Data flow patterns

### Styling Approach
- CSS solution
- Design tokens/theme
- Responsive strategy

### Build & Bundle
- Bundler (Vite, Webpack, etc.)
- Key optimizations
- Environment handling

### Recommendations
- Patterns to follow
- Areas of concern
- Suggested improvements
```

**Acceptance Criteria:**
- [ ] Correctly identifies React, Vue, and Angular projects
- [ ] Maps component hierarchy accurately
- [ ] Identifies state management solution
- [ ] Documents styling approach
- [ ] Provides actionable recommendations

---

**Sub-Agent: `backend-researcher`**

| Attribute | Value |
|-----------|-------|
| File | `.claude/agents/research/backend-researcher.md` |
| Model | `sonnet` |
| Tools | `Read, Glob, Grep, Bash` |
| Purpose | Backend architecture analysis |

**Specification:**
```markdown
---
name: backend-researcher
description: Research backend architecture including APIs, database schemas, 
  authentication flows, and service patterns. Use for server-side analysis 
  or before backend modifications.
tools: Read, Glob, Grep, Bash
model: sonnet
---

# Backend Researcher

You are a backend architecture specialist with expertise in APIs, databases,
authentication, and distributed systems.

## Primary Responsibilities
1. Map API endpoints and routes
2. Analyze database schemas and relationships
3. Document authentication and authorization flows
4. Identify service boundaries and patterns
5. Check for middleware and interceptors

## Research Protocol
1. Identify backend framework and version
2. Map route definitions
3. Analyze data models and schemas
4. Trace authentication flow
5. Document middleware chain

## Framework-Specific Checks

### Node.js (Express/Fastify/NestJS)
- Route organization
- Middleware stack
- Controller patterns
- Service layer structure

### Python (FastAPI/Django/Flask)
- Route decorators
- Dependency injection
- ORM usage (SQLAlchemy, Django ORM)
- Async patterns

### Go (Gin/Echo/Fiber)
- Handler organization
- Middleware chain
- Repository patterns

## Output Format
### Framework & Version
- Framework: [name]
- Version: [version]
- Runtime: [Node.js/Python/Go version]

### API Architecture
- Route organization pattern
- API versioning approach
- Request/response handling
- Error handling patterns

### Data Layer
- Database(s) used
- ORM/Query builder
- Schema overview
- Migration approach

### Authentication & Authorization
- Auth mechanism (JWT, sessions, OAuth)
- Permission model
- Protected routes pattern

### Service Architecture
- Service boundaries
- Inter-service communication
- External integrations

### Recommendations
- Patterns to follow
- Security concerns
- Performance considerations
```

**Acceptance Criteria:**
- [ ] Correctly identifies backend framework
- [ ] Maps API routes accurately
- [ ] Documents authentication flow
- [ ] Identifies database and ORM
- [ ] Provides security recommendations

---

**Sub-Agent: `dependency-researcher`**

| Attribute | Value |
|-----------|-------|
| File | `.claude/agents/research/dependency-researcher.md` |
| Model | `haiku` |
| Tools | `Read, Bash, Grep` |
| Purpose | Package and dependency analysis |

**Specification:**
```markdown
---
name: dependency-researcher
description: Analyze project dependencies, versions, security vulnerabilities, 
  and upgrade paths. Use when modifying packages, checking security, or 
  planning upgrades.
tools: Read, Bash, Grep
model: haiku
---

# Dependency Researcher

You are a dependency management specialist focused on security, compatibility,
and upgrade planning.

## Primary Responsibilities
1. Audit current dependencies and versions
2. Identify security vulnerabilities
3. Check for outdated packages
4. Analyze dependency tree
5. Recommend upgrade paths

## Research Protocol
1. Read package manifest (package.json, requirements.txt, go.mod)
2. Check lock file for exact versions
3. Run audit commands if available
4. Identify major version gaps
5. Check for deprecated packages

## Package Manager Commands

### npm/yarn/pnpm
- `npm audit` / `yarn audit`
- `npm outdated` / `yarn outdated`
- `npm ls --depth=0`

### pip
- `pip list --outdated`
- `pip-audit` (if installed)
- `pip show [package]`

### Go
- `go list -m all`
- `go mod graph`
- `govulncheck` (if installed)

## Output Format
### Dependency Summary
- Total dependencies: [count]
- Direct dependencies: [count]
- Dev dependencies: [count]

### Security Issues
| Package | Severity | Vulnerability | Fix Version |
|---------|----------|---------------|-------------|
| ...     | ...      | ...           | ...         |

### Outdated Packages
| Package | Current | Latest | Type |
|---------|---------|--------|------|
| ...     | ...     | ...    | ...  |

### Upgrade Recommendations
- Safe upgrades (patch/minor)
- Breaking changes (major)
- Deprecated packages to replace

### Dependency Conflicts
- Any version conflicts detected
- Resolution recommendations
```

**Acceptance Criteria:**
- [ ] Correctly reads package manifests for Node.js, Python, Go
- [ ] Runs appropriate audit commands
- [ ] Identifies security vulnerabilities
- [ ] Lists outdated packages with versions
- [ ] Provides upgrade recommendations

---

**Sub-Agent: `pattern-researcher`**

| Attribute | Value |
|-----------|-------|
| File | `.claude/agents/research/pattern-researcher.md` |
| Model | `sonnet` |
| Tools | `Read, Glob, Grep` |
| Purpose | Pattern and convention detection |

**Specification:**
```markdown
---
name: pattern-researcher
description: Identify existing code patterns, naming conventions, and 
  architectural decisions in the codebase. Use to maintain consistency 
  when adding new code.
tools: Read, Glob, Grep
model: sonnet
---

# Pattern Researcher

You are a code consistency specialist focused on identifying and documenting
patterns and conventions used throughout a codebase.

## Primary Responsibilities
1. Identify naming conventions
2. Document coding patterns
3. Detect architectural decisions
4. Find testing patterns
5. Note documentation standards

## Research Protocol
1. Sample multiple files across directories
2. Compare similar components/modules
3. Check for style configuration files
4. Analyze test file patterns
5. Review existing documentation format

## Patterns to Detect

### Naming Conventions
- File naming (kebab-case, camelCase, PascalCase)
- Variable naming
- Function/method naming
- Class naming
- Constant naming

### Code Patterns
- Error handling approach
- Logging patterns
- Configuration management
- Dependency injection
- Factory patterns
- Repository patterns

### File Organization
- Directory structure philosophy
- Index file usage
- Barrel exports
- Feature-based vs layer-based

### Testing Patterns
- Test file location (co-located, separate)
- Test naming conventions
- Mocking approaches
- Fixture patterns

### Documentation
- JSDoc/docstring style
- README patterns
- Inline comment style

## Output Format
### Naming Conventions
| Element | Convention | Example |
|---------|------------|---------|
| Files   | ...        | ...     |
| Functions | ...      | ...     |
| Classes | ...        | ...     |

### Code Patterns
- Error Handling: [description with example]
- Logging: [description with example]
- Config: [description with example]

### Architecture Decisions
- [Decision]: [Rationale if discoverable]

### Testing Conventions
- Location: [pattern]
- Naming: [pattern]
- Structure: [pattern]

### Documentation Style
- [Format with example]

### Consistency Issues Found
- [Any inconsistencies detected]
```

**Acceptance Criteria:**
- [ ] Identifies naming conventions correctly
- [ ] Documents error handling patterns
- [ ] Detects testing conventions
- [ ] Notes any inconsistencies
- [ ] Provides usable examples

---

#### 1.2.3 Research Skills

**Skill: `codebase-mapping-skill`**

| Attribute | Value |
|-----------|-------|
| Location | `.claude/skills/research/codebase-mapping/` |
| Files | `SKILL.md`, `templates/structure-report.md` |
| Used By | `codebase-explorer`, `module-researcher` |

**SKILL.md:**
```markdown
---
name: codebase-mapping
description: Generate structured codebase maps with dependency graphs, file 
  relationships, and architectural patterns. Use when exploring unfamiliar 
  codebases or documenting project structure.
---

# Codebase Mapping Skill

## Purpose
Produce consistent, structured documentation of codebase organization.

## When to Use
- Starting work on unfamiliar project
- Onboarding new team members
- Documenting architecture decisions
- Before major refactoring

## Output Template
Use the template in [templates/structure-report.md](templates/structure-report.md)

## Mapping Process

### Step 1: Project Identification
Identify project type from configuration files:
- `package.json` → Node.js
- `pyproject.toml` / `setup.py` → Python
- `go.mod` → Go
- `Cargo.toml` → Rust
- `pom.xml` / `build.gradle` → Java

### Step 2: Structure Analysis
Map directories to their purposes:
- `src/` or `lib/` → Source code
- `tests/` or `__tests__/` → Test files
- `docs/` → Documentation
- `scripts/` → Build/utility scripts
- `config/` → Configuration files

### Step 3: Dependency Graph
Create simplified dependency visualization:
```
Entry Point
├── Core Module A
│   ├── Utility 1
│   └── Utility 2
├── Core Module B
│   └── External Lib
└── Shared Components
```

### Step 4: Key Files
Identify and document:
- Entry points (main.ts, index.js, app.py)
- Configuration (tsconfig, eslint, etc.)
- Environment handling
- Build configuration

## Storage Location
Save output to: `docs/research/codebase-map-{date}.md`
```

**templates/structure-report.md:**
```markdown
# Codebase Structure Report

**Generated:** {date}
**Project:** {project_name}
**Type:** {project_type}

## Quick Reference

| Aspect | Value |
|--------|-------|
| Language | {language} |
| Framework | {framework} |
| Package Manager | {package_manager} |
| Test Framework | {test_framework} |

## Directory Structure

```
{tree_output}
```

## Key Files

| File | Purpose |
|------|---------|
| {file} | {purpose} |

## Module Map

{dependency_diagram}

## Entry Points

1. **{entry_point}**: {description}

## Configuration Files

| File | Purpose |
|------|---------|
| {config_file} | {purpose} |

## Recommendations

- {recommendation_1}
- {recommendation_2}
```

**Acceptance Criteria:**
- [ ] SKILL.md has valid frontmatter
- [ ] Template produces readable output
- [ ] Output saved to correct location
- [ ] Works for Node.js, Python, Go projects

---

**Skill: `dependency-analysis-skill`**

| Attribute | Value |
|-----------|-------|
| Location | `.claude/skills/research/dependency-analysis/` |
| Files | `SKILL.md`, `scripts/audit-deps.sh`, `templates/dep-report.md` |
| Used By | `dependency-researcher` |

**SKILL.md:**
```markdown
---
name: dependency-analysis
description: Analyze project dependencies for security vulnerabilities, outdated 
  packages, and upgrade paths. Use when auditing dependencies or planning upgrades.
---

# Dependency Analysis Skill

## Purpose
Systematic analysis of project dependencies for security and maintenance.

## When to Use
- Security audits
- Before adding new dependencies
- Planning version upgrades
- Regular maintenance checks

## Analysis Process

### Step 1: Identify Package Manager
Detect from files:
- `package-lock.json` / `yarn.lock` / `pnpm-lock.yaml` → Node.js
- `requirements.txt` / `Pipfile.lock` / `poetry.lock` → Python
- `go.sum` → Go

### Step 2: Run Security Audit
Execute appropriate command:
```bash
# Node.js
npm audit --json || yarn audit --json

# Python (if pip-audit installed)
pip-audit --format json

# Go
govulncheck ./...
```

### Step 3: Check Outdated
```bash
# Node.js
npm outdated --json

# Python
pip list --outdated --format json

# Go
go list -u -m all
```

### Step 4: Analyze Results
Categorize findings:
- **Critical**: Security vulnerabilities with known exploits
- **High**: Security issues or major version behind
- **Medium**: Minor version behind or deprecated
- **Low**: Patch version behind

## Output Format
Use [templates/dep-report.md](templates/dep-report.md)

## Storage Location
Save to: `docs/research/dependency-audit-{date}.md`
```

**Acceptance Criteria:**
- [ ] Correctly identifies package manager
- [ ] Runs appropriate audit commands
- [ ] Categorizes findings by severity
- [ ] Generates structured report

---

**Skill: `pattern-detection-skill`**

| Attribute | Value |
|-----------|-------|
| Location | `.claude/skills/research/pattern-detection/` |
| Files | `SKILL.md`, `patterns/*.md` |
| Used By | `pattern-researcher`, `module-researcher` |

**SKILL.md:**
```markdown
---
name: pattern-detection
description: Detect and document existing code patterns in a codebase. Use to 
  maintain consistency with established conventions when writing new code.
---

# Pattern Detection Skill

## Purpose
Identify and document patterns for consistency enforcement.

## Pattern Categories

### 1. Naming Conventions
Reference: [patterns/naming-conventions.md](patterns/naming-conventions.md)

Detection method:
- Sample 10+ files across different directories
- Extract function/class/variable names
- Identify dominant patterns

### 2. Error Handling
Reference: [patterns/error-handling.md](patterns/error-handling.md)

Detection method:
- Search for try/catch blocks
- Find custom error classes
- Check for error middleware

### 3. Testing Patterns
Reference: [patterns/testing-patterns.md](patterns/testing-patterns.md)

Detection method:
- Locate test files
- Analyze test structure
- Identify mocking approach

## Consistency Scoring

Rate codebase consistency:
- **High (90%+)**: Strong patterns, few deviations
- **Medium (70-89%)**: Clear patterns with some variation
- **Low (<70%)**: Inconsistent, needs standardization

## Output Format
Create patterns document with:
1. Detected patterns with examples
2. Consistency score per category
3. Deviation examples
4. Recommendations for standardization

## Storage Location
Save to: `docs/research/patterns-{date}.md`
```

**Acceptance Criteria:**
- [ ] Detects naming conventions accurately
- [ ] Identifies error handling patterns
- [ ] Documents testing conventions
- [ ] Provides consistency score
- [ ] Includes concrete examples

---

#### 1.2.4 Foundation Slash Commands

**Command: `/rqpiv-start`**

| Attribute | Value |
|-----------|-------|
| File | `.claude/commands/rqpiv-start.md` |
| Purpose | Initialize RQPIV workflow for a new task |

```markdown
# Start RQPIV Workflow

Initialize the RQPIV workflow for: $ARGUMENTS

## Workflow Steps

1. **Create Session Directory**
   Create `docs/sessions/{date}-{task-slug}/` for this workflow session

2. **Enter Plan Mode**
   Switch to plan mode (Shift+Tab×2) for research phase

3. **Invoke Research Phase**
   Delegate to research sub-agents:
   - codebase-explorer (if unfamiliar with project)
   - Relevant specialist researcher based on task type

4. **Await Research Completion**
   Store findings in session directory

5. **Transition to Questioning**
   Generate clarifying questions based on research

6. **DO NOT PROCEED** without user confirmation

## Session Tracking
Create `docs/sessions/{date}-{task-slug}/session.md` with:
- Task description
- Current phase
- Findings summary
- Pending questions
- User decisions

## Phase Indicators
- 🔍 Research
- ❓ Questioning  
- 📋 Planning
- 🔨 Implementation
- ✅ Validation
```

**Acceptance Criteria:**
- [ ] Creates session directory structure
- [ ] Enters plan mode
- [ ] Invokes appropriate researchers
- [ ] Creates session tracking file
- [ ] Does not proceed without confirmation

---

#### 1.2.5 CLAUDE.md Foundation

Create project-level CLAUDE.md with RQPIV workflow instructions:

```markdown
# Project Context for Claude Code

## RQPIV Workflow

This project uses the RQPIV (Research, Question, Plan, Implement, Validate) 
workflow system. Follow these phases strictly.

### Phase Requirements

1. **Research (R)**: ALWAYS delegate to researcher sub-agents before making changes
2. **Question (Q)**: ALWAYS ask clarifying questions before planning
3. **Plan (P)**: Create detailed plans with file paths and line numbers
4. **Implement (I)**: Follow the approved plan exactly
5. **Validate (V)**: Run code review and tests before committing

### Sub-Agent Usage

- Use `codebase-explorer` for initial project understanding
- Use specialist researchers for deep analysis
- NEVER do research in main context - always delegate

### Artifact Storage

- Research findings: `docs/research/`
- Requirements: `docs/specs/`
- Plans: `docs/plans/`
- Reviews: `docs/reviews/`

### Quality Gates

- No implementation without approved plan
- No commit without passing validation
- All changes must follow detected patterns

## Project-Specific Information

[To be filled based on actual project]
```

**Acceptance Criteria:**
- [x] CLAUDE.md created at project root
- [x] Contains RQPIV workflow instructions
- [x] Documents artifact storage locations
- [x] Defines quality gates

---

### 1.3 Phase 1 Testing Requirements

| Test Case | Description | Expected Result |
|-----------|-------------|-----------------|
| TC-1.1 | Invoke codebase-explorer on Node.js project | Returns structure in <30s |
| TC-1.2 | Invoke module-researcher on specific module | Returns dependencies and interfaces |
| TC-1.3 | Invoke frontend-researcher on React project | Identifies React version and patterns |
| TC-1.4 | Invoke backend-researcher on Express API | Maps routes and middleware |
| TC-1.5 | Invoke dependency-researcher | Lists vulnerabilities and outdated packages |
| TC-1.6 | Invoke pattern-researcher | Documents naming and coding conventions |
| TC-1.7 | Run /rqpiv-start command | Creates session and invokes researchers |
| TC-1.8 | Verify context isolation | Main agent context not polluted by research |

### 1.4 Phase 1 Success Criteria

- [x] All 6 research sub-agents implemented and tested
- [x] All 3 research skills implemented with templates
- [x] `/rqpiv-start` command functional
- [x] CLAUDE.md foundation in place
- [x] Research artifacts storing correctly
- [x] Context isolation verified

---

## Phase 2: Questioning & Requirement Analysis

**Duration:** 1-2 weeks
**Priority:** High
**Dependencies:** Phase 1 complete
**Status:** COMPLETED (December 14, 2025)

### 2.1 Objectives

- Implement requirement-analyst sub-agent
- Create questioning skills with templates
- Build structured question generation
- Establish requirement validation gates

### 2.2 Deliverables

#### 2.2.1 Questioning Sub-Agent

**Sub-Agent: `requirement-analyst`**

| Attribute | Value |
|-----------|-------|
| File | `.claude/agents/questioning/requirement-analyst.md` |
| Model | `opus` |
| Tools | `Read, Write` |
| Purpose | Analyze research and generate clarifying questions |

**Specification:**
```markdown
---
name: requirement-analyst
description: Analyze research findings and generate clarifying questions for 
  users. MUST BE USED before planning phase. Ensures requirements are complete, 
  unambiguous, and validated before implementation begins.
tools: Read, Write
model: opus
---

# Requirement Analyst

You are a senior business analyst and requirements engineer. Your role is to 
bridge the gap between user intent and technical specification.

## Primary Responsibilities
1. Analyze research findings for requirement implications
2. Identify ambiguities and gaps in user requests
3. Generate targeted clarifying questions
4. Validate requirements are implementable
5. Create structured requirement documents

## Analysis Protocol

### Step 1: Review Research
Read all findings in `docs/research/` for current session:
- Codebase structure
- Existing patterns
- Technical constraints
- Dependencies

### Step 2: Parse User Intent
From original request, identify:
- Explicit requirements (stated directly)
- Implicit requirements (assumed/expected)
- Ambiguous requirements (unclear)
- Missing requirements (gaps)

### Step 3: Generate Questions
For each ambiguity or gap, create:
- Clear, specific question
- Why it matters (impact)
- Default assumption if not answered
- Options where applicable

### Step 4: Validate Technical Feasibility
Cross-reference with research to flag:
- Conflicts with existing architecture
- Missing dependencies
- Breaking changes required
- Performance implications

## Question Categories

### Scope Questions
- Feature boundaries
- Edge cases
- Error scenarios
- Future extensibility

### Technical Questions
- Technology preferences
- Performance requirements
- Security requirements
- Integration points

### UX Questions
- User flows
- Error messaging
- Loading states
- Accessibility needs

### Priority Questions
- Must-have vs nice-to-have
- Deadline constraints
- Phasing possibilities

## Output Format

### Questions Document
Save to: `docs/specs/questions-{session}.md`

```
# Clarifying Questions

## Must Answer (Blocking)
1. [Question]
   - Impact: [why this matters]
   - Default: [assumption if not answered]

## Should Answer (Important)
1. [Question]
   - Impact: [why this matters]
   - Options: [A, B, C]

## Could Answer (Nice to Have)
1. [Question]
   - Context: [additional info]
```

### Validated Requirements
After answers received, create: `docs/specs/requirements-{session}.md`

## Constraints
- Maximum 10 blocking questions
- Questions must be answerable by non-technical users
- Include defaults for all questions
- Never proceed to planning without user confirmation
```

**Acceptance Criteria:**
- [ ] Reviews research findings before generating questions
- [ ] Categorizes questions by priority
- [ ] Provides default assumptions
- [ ] Questions are non-technical friendly
- [ ] Creates structured requirements document after answers

---

#### 2.2.2 Questioning Skills

**Skill: `requirement-clarification-skill`**

| Attribute | Value |
|-----------|-------|
| Location | `.claude/skills/questioning/requirement-clarification/` |
| Files | `SKILL.md`, `question-templates/*.md`, `scripts/validate-requirements.py` |
| Used By | `requirement-analyst` |

**SKILL.md:**
```markdown
---
name: requirement-clarification
description: Generate clarifying questions from research findings. MUST be used 
  before planning phase. Validates requirements are complete and unambiguous 
  before technical work begins.
---

# Requirement Clarification Skill

## Purpose
Transform ambiguous user requests into clear, implementable requirements.

## Question Templates

### For Scope Clarification
See [question-templates/scope-questions.md](question-templates/scope-questions.md)

Common patterns:
- "Should [feature] also handle [edge case]?"
- "When [condition], what should happen?"
- "Is [assumption] correct, or do you need [alternative]?"

### For Technical Decisions
See [question-templates/technical-questions.md](question-templates/technical-questions.md)

Common patterns:
- "Do you have a preference between [A] and [B] for [purpose]?"
- "Should this integrate with [existing system]?"
- "What level of [performance/security] is required?"

### For Constraints
See [question-templates/constraint-questions.md](question-templates/constraint-questions.md)

Common patterns:
- "Is there a deadline for this?"
- "Are there any [technology/approach] restrictions?"
- "Who will be using this feature?"

## Question Quality Checklist

Each question must be:
- [ ] Specific (not vague)
- [ ] Answerable (user has the information)
- [ ] Impactful (answer affects implementation)
- [ ] Non-technical (accessible language)
- [ ] Defaultable (has fallback assumption)

## Validation Script

Run `scripts/validate-requirements.py` to check:
- All blocking questions answered
- No contradictory requirements
- Technical feasibility confirmed

## Output Location
- Questions: `docs/specs/questions-{session}.md`
- Requirements: `docs/specs/requirements-{session}.md`
```

**question-templates/scope-questions.md:**
```markdown
# Scope Question Templates

## Feature Boundaries
- "Should [feature] include [related capability], or is that separate?"
- "Does this need to work for [user type A] and [user type B], or just [one]?"

## Edge Cases
- "What should happen if [error condition]?"
- "How should the system behave when [unusual input]?"
- "Should there be a limit on [quantity/size]? If so, what?"

## Data Handling
- "Should [data] be stored permanently or temporarily?"
- "Who should have access to [data]?"
- "Should [historical data] be migrated?"

## Integration Scope
- "Does this need to connect with [external system]?"
- "Should changes here update [related feature]?"
```

**question-templates/technical-questions.md:**
```markdown
# Technical Question Templates

## Architecture Decisions
- "Should this be a new [module/service] or extend [existing one]?"
- "Do you prefer [sync/async] processing for this?"

## Performance
- "How many [users/requests/items] should this handle?"
- "Is real-time response critical, or is [N seconds] acceptable?"

## Security
- "Who should be able to [action]? (roles/permissions)"
- "Does [data] contain sensitive information requiring encryption?"

## Technology
- "Is there a preferred [library/framework] for this?"
- "Should this support [browser/platform]?"
```

**Acceptance Criteria:**
- [ ] Question templates cover scope, technical, and constraints
- [ ] Questions follow quality checklist
- [ ] Validation script functional
- [ ] Output stored in correct location

---

**Skill: `user-intent-parser-skill`**

| Attribute | Value |
|-----------|-------|
| Location | `.claude/skills/questioning/user-intent-parser/` |
| Files | `SKILL.md`, `templates/parsed-intent.md` |
| Used By | `requirement-analyst` |

**SKILL.md:**
```markdown
---
name: user-intent-parser
description: Parse user requirements into structured format with explicit 
  assumptions, constraints, and acceptance criteria. Use when initial 
  requirements are ambiguous or informal.
---

# User Intent Parser Skill

## Purpose
Convert informal user requests into structured requirement format.

## Parsing Process

### Step 1: Extract Explicit Statements
Identify what user directly stated:
- Actions (verbs): create, update, delete, show, etc.
- Objects (nouns): user, product, order, etc.
- Conditions (when/if): triggers, prerequisites
- Outcomes (so that): expected results

### Step 2: Identify Implicit Requirements
What's assumed but not stated:
- Authentication required?
- Error handling expectations
- Performance expectations
- Platform/device support

### Step 3: Flag Ambiguities
Mark unclear items:
- Vague terms ("fast", "good", "easy")
- Missing specifics (quantities, limits)
- Unclear scope (boundaries)

### Step 4: Generate Structured Format
Use [templates/parsed-intent.md](templates/parsed-intent.md)

## Output Format

### Parsed Intent Document

```markdown
# Parsed Requirements: [Feature Name]

## User Statement (Original)
> [exact user request]

## Extracted Requirements

### Functional Requirements
| ID | Requirement | Source | Confidence |
|----|-------------|--------|------------|
| FR-1 | [requirement] | Explicit | High |
| FR-2 | [requirement] | Implicit | Medium |

### Non-Functional Requirements
| ID | Requirement | Source | Confidence |
|----|-------------|--------|------------|
| NFR-1 | [requirement] | Implicit | Low |

## Assumptions Made
1. [Assumption] - [Rationale]

## Ambiguities Requiring Clarification
1. [Ambiguity] - [Question to ask]

## Acceptance Criteria (Draft)
- [ ] Given [context], when [action], then [result]
```

## Storage Location
Save to: `docs/specs/parsed-intent-{session}.md`
```

**Acceptance Criteria:**
- [ ] Correctly extracts explicit requirements
- [ ] Identifies implicit requirements
- [ ] Flags ambiguities with questions
- [ ] Generates structured output
- [ ] Assigns confidence levels

---

#### 2.2.3 Questioning Slash Command

**Command: `/phase-question`**

| Attribute | Value |
|-----------|-------|
| File | `.claude/commands/phase-question.md` |
| Purpose | Execute questioning phase of RQPIV |

```markdown
# Execute Questioning Phase

Transition to questioning phase for: $ARGUMENTS

## Prerequisites Check
- [ ] Research phase completed
- [ ] Research findings in `docs/research/`
- [ ] Session tracking file exists

## Execution Steps

1. **Load Research Context**
   Read all files in current session's research directory

2. **Invoke Requirement Analyst**
   Use requirement-analyst sub-agent with:
   - Research findings
   - Original user request
   - Session context

3. **Generate Questions**
   - Parse user intent
   - Identify gaps and ambiguities
   - Create prioritized question list

4. **Present Questions to User**
   Display questions grouped by priority:
   - 🔴 Must Answer (blocking)
   - 🟡 Should Answer (important)
   - 🟢 Could Answer (nice to have)

5. **Await User Responses**
   - Record answers
   - Validate completeness
   - Resolve contradictions

6. **Generate Requirements Document**
   After answers received:
   - Create validated requirements
   - Include acceptance criteria
   - Store in `docs/specs/`

7. **Confirm Readiness**
   Ask user: "Are these requirements accurate? Ready to proceed to planning?"

## Gate: DO NOT proceed to planning without explicit user confirmation
```

**Acceptance Criteria:**
- [ ] Checks research prerequisites
- [ ] Invokes requirement-analyst correctly
- [ ] Presents questions by priority
- [ ] Records user answers
- [ ] Generates requirements document
- [ ] Requires explicit confirmation

---

### 2.3 Phase 2 Testing Requirements

| Test Case | Description | Expected Result |
|-----------|-------------|-----------------|
| TC-2.1 | Parse ambiguous user request | Extracts explicit/implicit requirements |
| TC-2.2 | Generate questions from research | Produces categorized question list |
| TC-2.3 | Questions are non-technical | Readable by non-developers |
| TC-2.4 | Default assumptions provided | All questions have fallbacks |
| TC-2.5 | Requirements validation | Contradictions flagged |
| TC-2.6 | Gate enforcement | Cannot proceed without confirmation |

### 2.4 Phase 2 Success Criteria

- [x] requirement-analyst sub-agent implemented
- [x] Both questioning skills implemented
- [x] `/phase-question` command functional
- [x] Question templates comprehensive
- [x] Requirement documents generating correctly
- [x] Gate preventing premature planning enforced

---

## Phase 3: Planning Infrastructure

**Duration:** 2-3 weeks
**Priority:** High
**Dependencies:** Phase 2 complete
**Status:** ✅ COMPLETED (December 15, 2025)

### 3.1 Objectives

- Implement planning sub-agents
- Create planning skills with templates
- Build detailed task breakdown system
- Establish plan approval gates

### 3.2 Deliverables

#### 3.2.1 Planning Sub-Agents

**Sub-Agent: `solution-architect`**

| Attribute | Value |
|-----------|-------|
| File | `.claude/agents/planning/solution-architect.md` |
| Model | `opus` |
| Tools | `Read, Write, Glob, Grep` |
| Purpose | High-level architecture and design decisions |

**Specification:**
```markdown
---
name: solution-architect
description: Create detailed architecture plans and design decisions based on 
  validated requirements. Use for significant feature implementations, 
  refactoring, or system design.
tools: Read, Write, Glob, Grep
model: opus
---

# Solution Architect

You are a senior software architect responsible for system design and 
architectural decisions.

## Primary Responsibilities
1. Design high-level solution architecture
2. Make technology and pattern decisions
3. Identify risks and mitigation strategies
4. Create architecture decision records
5. Define interfaces and contracts

## Architecture Process

### Step 1: Review Inputs
Read and analyze:
- Validated requirements (`docs/specs/requirements-*.md`)
- Research findings (`docs/research/`)
- Existing architecture (from codebase research)

### Step 2: Identify Options
For each major decision:
- List viable approaches (minimum 2)
- Pros and cons of each
- Alignment with existing patterns
- Impact on future development

### Step 3: Make Decisions
For each decision:
- Select recommended approach
- Document rationale
- Note trade-offs accepted

### Step 4: Design Solution
Create architecture document:
- Component diagram
- Data flow
- Interface definitions
- Integration points

### Step 5: Risk Assessment
Identify:
- Technical risks
- Timeline risks
- Integration risks
- Mitigation strategies

## Output Format

### Architecture Document
Save to: `docs/plans/architecture-{session}.md`

```markdown
# Architecture: [Feature Name]

## Overview
[High-level description]

## Design Decisions

### Decision 1: [Topic]
**Options Considered:**
1. [Option A]: [description]
2. [Option B]: [description]

**Selected:** [Option]
**Rationale:** [Why this option]
**Trade-offs:** [What we're accepting]

## Component Design

### [Component Name]
- **Responsibility:** [what it does]
- **Location:** [file path]
- **Interfaces:** [public API]
- **Dependencies:** [what it needs]

## Data Flow
[Diagram or description]

## Integration Points
| System | Direction | Protocol | Data |
|--------|-----------|----------|------|
| [name] | In/Out    | [type]   | [format] |

## Risk Assessment
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| [risk] | H/M/L | H/M/L | [strategy] |

## Open Questions
- [Questions for team/user]
```

## Constraints
- Maximum 5 major decisions per document
- Each decision must have rationale
- Risk assessment required for all plans
- Must reference existing patterns from research
```

**Acceptance Criteria:**
- [ ] Reviews requirements and research before designing
- [ ] Documents multiple options for decisions
- [ ] Provides clear rationale for selections
- [ ] Identifies and assesses risks
- [ ] Creates structured architecture document

---

**Sub-Agent: `task-planner`**

| Attribute | Value |
|-----------|-------|
| File | `.claude/agents/planning/task-planner.md` |
| Model | `sonnet` |
| Tools | `Read, Write, Glob, Grep` |
| Purpose | Detailed task breakdown with implementation specifics |

**Specification:**
```markdown
---
name: task-planner
description: Break down architectural plans into specific, actionable tasks 
  with exact file paths, line numbers, and verification steps. Creates 
  execution-ready implementation plans.
tools: Read, Write, Glob, Grep
model: sonnet
---

# Task Planner

You are a technical project planner who creates detailed, executable task lists.

## Primary Responsibilities
1. Break architecture into atomic tasks
2. Identify exact files and locations
3. Define verification for each task
4. Establish task dependencies
5. Estimate complexity

## Planning Process

### Step 1: Review Architecture
Read:
- Architecture document (`docs/plans/architecture-*.md`)
- Research findings (patterns, structure)
- Existing code in affected areas

### Step 2: Identify All Changes
For each component:
- New files to create
- Existing files to modify
- Files to delete/move
- Configuration changes
- Test requirements

### Step 3: Create Atomic Tasks
Each task should be:
- Completable in one Claude Code session
- Independently verifiable
- Clear in scope

### Step 4: Add Implementation Details
For each task:
- Exact file paths
- Specific line ranges for modifications
- Code patterns to follow
- Verification commands

### Step 5: Establish Order
- Identify dependencies
- Create execution order
- Note parallelizable tasks

## Output Format

### Implementation Plan
Save to: `docs/plans/implementation-{session}.md`

```markdown
# Implementation Plan: [Feature Name]

## Summary
- **Total Tasks:** [N]
- **Estimated Effort:** [time]
- **Risk Level:** [High/Medium/Low]

## Requirements Reference
[Link to requirements doc]

## Current State
[Brief description of existing state]

## Expected Outcome
[What success looks like]

---

## Phase 1: [Phase Name]

### Task 1.1: [Task Name]
**Priority:** P1 (Critical) | P2 (High) | P3 (Medium)

**Description:**
[What needs to be done]

**File Operations:**
| Action | File | Details |
|--------|------|---------|
| CREATE | `src/services/auth.ts` | New service file |
| MODIFY | `src/routes/index.ts` | Lines 45-60, add route |
| DELETE | `src/old/legacy.ts` | Remove deprecated |

**Implementation Notes:**
- Follow pattern in `src/services/user.ts`
- Use existing error handling from `src/utils/errors.ts`

**Verification:**
```bash
npm run typecheck
npm test -- auth.test.ts
```

**Commit Message:**
```
feat(auth): implement JWT token service

- Add token generation and validation
- Integrate with user service
- Add unit tests
```

**Dependencies:** None | Task 1.2

---

### Task 1.2: [Next Task]
...

---

## Validation Checklist
- [ ] All new files created
- [ ] All modifications complete
- [ ] Tests pass
- [ ] Type check passes
- [ ] Lint passes
- [ ] Manual verification done
```

## Constraints
- Tasks must be atomic (one concern each)
- All file paths must be absolute
- Verification must be automatable
- Commit messages must follow conventions
```

**Acceptance Criteria:**
- [ ] Breaks architecture into atomic tasks
- [ ] Includes exact file paths and line ranges
- [ ] Provides verification commands
- [ ] Defines task dependencies
- [ ] Creates git commit messages

---

#### 3.2.2 Planning Skills

**Skill: `architecture-planning-skill`**

| Attribute | Value |
|-----------|-------|
| Location | `.claude/skills/planning/architecture-planning/` |
| Files | `SKILL.md`, `templates/*.md`, `patterns/*.md` |
| Used By | `solution-architect` |

**SKILL.md:**
```markdown
---
name: architecture-planning
description: Create detailed architecture plans with decision records and risk 
  assessments. Use when planning significant features or system changes.
---

# Architecture Planning Skill

## Purpose
Produce consistent, thorough architecture documentation.

## Templates
- [templates/architecture-doc.md](templates/architecture-doc.md) - Main structure
- [templates/decision-record.md](templates/decision-record.md) - ADR format
- [templates/risk-assessment.md](templates/risk-assessment.md) - Risk matrix

## Pattern Library
Reference established patterns:
- [patterns/microservices.md](patterns/microservices.md)
- [patterns/monolith.md](patterns/monolith.md)
- [patterns/serverless.md](patterns/serverless.md)

## Decision Framework

### When to Create ADR
- Technology choice (database, framework)
- Architectural pattern (monolith vs microservice)
- Integration approach (sync vs async)
- Security model changes

### ADR Format (Lightweight)
```markdown
# ADR-[N]: [Title]
**Status:** Proposed | Accepted | Deprecated
**Date:** [YYYY-MM-DD]

## Context
[Why decision needed]

## Decision
[What we decided]

## Consequences
[What follows from this]
```

## Risk Assessment Matrix

| Probability ↓ / Impact → | Low | Medium | High |
|---------------------------|-----|--------|------|
| High | Medium | High | Critical |
| Medium | Low | Medium | High |
| Low | Low | Low | Medium |

## Quality Checklist
- [ ] All major decisions documented
- [ ] Options considered for each decision
- [ ] Rationale provided
- [ ] Risks identified
- [ ] Mitigation strategies defined
- [ ] Aligns with existing patterns
```

**Acceptance Criteria:**
- [ ] Templates produce consistent output
- [ ] Decision records follow ADR format
- [ ] Risk matrix applied correctly
- [ ] Pattern library referenced appropriately

---

**Skill: `task-breakdown-skill`**

| Attribute | Value |
|-----------|-------|
| Location | `.claude/skills/planning/task-breakdown/` |
| Files | `SKILL.md`, `templates/task-template.md`, `scripts/generate-tasks.py` |
| Used By | `task-planner` |

**SKILL.md:**
```markdown
---
name: task-breakdown
description: Break down high-level plans into specific tasks with file paths, 
  line numbers, and verification steps. Creates execution-ready implementation 
  plans.
---

# Task Breakdown Skill

## Purpose
Transform architecture plans into atomic, executable tasks.

## Task Template
Use [templates/task-template.md](templates/task-template.md)

## Task Criteria

### Atomic Tasks Must Be:
1. **Single-concern**: One logical change
2. **Verifiable**: Can confirm completion
3. **Bounded**: Clear start and end
4. **Estimated**: Rough time/complexity
5. **Ordered**: Dependencies clear

### Task Size Guidelines
| Size | Description | Typical Duration |
|------|-------------|------------------|
| XS | Single line change | < 5 min |
| S | Single function | 5-15 min |
| M | Single file | 15-30 min |
| L | Multiple files, one concern | 30-60 min |
| XL | Split into smaller tasks | > 60 min |

## File Operation Types

### CREATE
- New file from scratch
- Include full path
- Note template/pattern to follow

### MODIFY
- Changes to existing file
- Include line range
- Describe before/after

### DELETE
- Remove file/code
- Confirm no dependencies
- Note cleanup required

### MOVE
- Relocate file
- Update imports
- Keep git history

## Verification Approaches

| Type | Command | Use Case |
|------|---------|----------|
| Type Check | `npm run typecheck` | TypeScript changes |
| Lint | `npm run lint` | Style compliance |
| Unit Test | `npm test -- [file]` | Logic verification |
| E2E Test | `npm run e2e` | Integration |
| Manual | [Instructions] | UI/UX changes |

## Dependency Types
- **Hard**: Must complete before next
- **Soft**: Should complete, but can proceed
- **None**: Independent

## Output Quality
- [ ] All tasks have verification
- [ ] File paths are absolute
- [ ] Line numbers included where relevant
- [ ] Commit message for each task
- [ ] Dependencies clearly marked
```

**templates/task-template.md:**
```markdown
### Task [N.M]: [Task Name]

**Priority:** P1 | P2 | P3  
**Size:** XS | S | M | L  
**Dependencies:** [Task IDs or "None"]

#### Description
[Clear description of what needs to be done]

#### File Operations
| Action | File Path | Details |
|--------|-----------|---------|
| [ACTION] | `[full/path/to/file]` | [specifics] |

#### Current State
```[language]
// Location: [file:lines]
[existing code snippet if modifying]
```

#### Expected State
```[language]
// After implementation
[expected code snippet]
```

#### Implementation Notes
- [Pattern to follow]
- [Gotchas to avoid]
- [Related files to check]

#### Verification
```bash
[verification commands]
```

#### Commit
```
[type](scope): [description]

[body if needed]
```
```

**Acceptance Criteria:**
- [ ] Tasks are appropriately sized
- [ ] All file operations specified
- [ ] Current and expected state shown
- [ ] Verification commands provided
- [ ] Commit messages included

---

#### 3.2.3 Planning Slash Command

**Command: `/phase-plan`**

| Attribute | Value |
|-----------|-------|
| File | `.claude/commands/phase-plan.md` |
| Purpose | Execute planning phase of RQPIV |

```markdown
# Execute Planning Phase

Transition to planning phase for: $ARGUMENTS

## Prerequisites Check
- [ ] Research phase completed
- [ ] Questioning phase completed
- [ ] Requirements validated and confirmed
- [ ] Requirements document in `docs/specs/`

## Execution Steps

1. **Load Context**
   Read:
   - Requirements document
   - Research findings
   - User answers from questioning

2. **Architecture Planning**
   Invoke solution-architect sub-agent:
   - Design high-level solution
   - Make technology decisions
   - Assess risks
   - Create architecture document

3. **User Review (Architecture)**
   Present architecture for approval:
   - Key decisions made
   - Risks identified
   - Open questions

4. **Await Architecture Approval**
   DO NOT proceed without explicit approval

5. **Task Breakdown**
   After approval, invoke task-planner:
   - Create atomic tasks
   - Add file paths and line numbers
   - Define verification steps
   - Establish order and dependencies

6. **Present Implementation Plan**
   Show user:
   - Total tasks
   - Estimated effort
   - Execution order
   - Risk areas

7. **Final Plan Approval**
   Ask: "Ready to proceed with implementation?"

## Gate: DO NOT proceed to implementation without plan approval

## Outputs
- `docs/plans/architecture-{session}.md`
- `docs/plans/implementation-{session}.md`
```

**Acceptance Criteria:**
- [ ] Checks all prerequisites
- [ ] Invokes architect then planner in sequence
- [ ] Requires architecture approval before task breakdown
- [ ] Creates both architecture and implementation documents
- [ ] Requires final approval before implementation

---

### 3.3 Phase 3 Testing Requirements

| Test Case | Description | Expected Result |
|-----------|-------------|-----------------|
| TC-3.1 | Architecture document generation | Complete architecture with decisions |
| TC-3.2 | Decision records created | ADR format followed |
| TC-3.3 | Risk assessment included | Matrix applied correctly |
| TC-3.4 | Task breakdown from architecture | Atomic tasks with details |
| TC-3.5 | File paths accuracy | All paths are valid |
| TC-3.6 | Verification commands | Commands are executable |
| TC-3.7 | Approval gates | Cannot proceed without approval |

### 3.4 Phase 3 Success Criteria

- [x] solution-architect sub-agent implemented
- [x] task-planner sub-agent implemented
- [x] Architecture planning skill implemented
- [x] Task breakdown skill implemented
- [x] `/phase-plan` command functional
- [x] Approval gates enforced
- [x] Plan documents comprehensive and usable

---

## Phase 4: Implementation Framework

**Duration:** 3-4 weeks
**Priority:** High
**Dependencies:** Phase 3 complete
**Status:** ✅ COMPLETED (December 15, 2025)

### 4.1 Objectives

- Implement developer sub-agents
- Create implementation skills
- Build quality enforcement hooks
- Establish implementation workflow

### 4.2 Deliverables

#### 4.2.1 Implementation Sub-Agents

**Sub-Agent: `backend-developer`**

| Attribute | Value |
|-----------|-------|
| File | `.claude/agents/implementation/backend-developer.md` |
| Model | `sonnet` |
| Tools | `Read, Write, Edit, Bash, Grep, Glob` |
| Skills | `clean-code`, `api-design`, `error-handling` |

**Specification:**
```markdown
---
name: backend-developer
description: Implement backend code following clean architecture and SOLID 
  principles. Use for API development, database operations, and server-side 
  logic implementation.
tools: Read, Write, Edit, Bash, Grep, Glob
model: sonnet
skills: clean-code, api-design, error-handling
---

# Backend Developer

You are a senior backend developer specializing in clean architecture,
API design, and maintainable code.

## Primary Responsibilities
1. Implement backend features per plan
2. Follow clean architecture principles
3. Write clean, testable code
4. Handle errors appropriately
5. Document public interfaces

## Implementation Protocol

### Step 1: Review Task
Read assigned task from implementation plan:
- File operations required
- Current state
- Expected outcome
- Verification steps

### Step 2: Check Patterns
Review existing patterns from research:
- Similar implementations
- Error handling approach
- Logging conventions
- Type patterns

### Step 3: Implement
Follow this order:
1. Types/interfaces first
2. Core logic
3. Error handling
4. Logging
5. Documentation

### Step 4: Verify
Run verification commands:
```bash
npm run typecheck
npm run lint
npm test -- [relevant tests]
```

### Step 5: Self-Review
Before marking complete:
- [ ] Code follows project patterns
- [ ] All types defined
- [ ] Errors handled
- [ ] Logs added
- [ ] JSDoc for public APIs

## Code Quality Rules

### SOLID Principles
- **S**ingle Responsibility: One reason to change
- **O**pen/Closed: Extend, don't modify
- **L**iskov Substitution: Subtypes substitutable
- **I**nterface Segregation: Small, focused interfaces
- **D**ependency Inversion: Depend on abstractions

### Clean Code
- Meaningful names
- Small functions (< 20 lines ideal)
- One level of abstraction per function
- No magic numbers/strings
- Comments explain why, not what

### Error Handling
- Use custom error classes
- Include error context
- Log with appropriate level
- Return meaningful messages

## Output
- Implemented code
- Updated tests (if scope includes)
- Verification results
- Notes for code reviewer

## Constraints
- Follow plan exactly (no scope creep)
- Match existing patterns
- All code must pass verification
- Document any deviations with rationale
```

**Acceptance Criteria:**
- [x] Implements tasks per plan
- [x] Follows SOLID principles
- [x] Matches existing patterns
- [x] Runs verification successfully
- [x] Documents deviations

---

**Sub-Agent: `frontend-developer`**

| Attribute | Value |
|-----------|-------|
| File | `.claude/agents/implementation/frontend-developer.md` |
| Model | `sonnet` |
| Tools | `Read, Write, Edit, Bash, Grep, Glob` |
| Skills | `clean-code`, `component-design`, `accessibility` |

**Specification:**
```markdown
---
name: frontend-developer
description: Implement frontend code following component best practices and 
  accessibility standards. Use for UI components, state management, and 
  client-side logic.
tools: Read, Write, Edit, Bash, Grep, Glob
model: sonnet
skills: clean-code, component-design, accessibility
---

# Frontend Developer

You are a senior frontend developer specializing in component architecture,
state management, and accessible UI development.

## Primary Responsibilities
1. Implement UI components per plan
2. Follow component best practices
3. Ensure accessibility compliance
4. Write testable component code
5. Optimize performance

## Implementation Protocol

### Step 1: Review Task
Read assigned task:
- Component requirements
- State management needs
- Styling approach
- Accessibility requirements

### Step 2: Check Patterns
Review existing patterns:
- Component structure
- State management approach
- Styling conventions
- Testing patterns

### Step 3: Implement
Follow this order:
1. Types/props interface
2. Component structure
3. State/hooks
4. Event handlers
5. Styling
6. Tests

### Step 4: Verify
```bash
npm run typecheck
npm run lint
npm test -- [component tests]
npm run build # Check for build errors
```

### Step 5: Self-Review
- [ ] Accessible (ARIA, keyboard nav)
- [ ] Responsive
- [ ] Props typed and documented
- [ ] Loading/error states handled
- [ ] Tests cover main scenarios

## Component Best Practices

### Structure
- Presentational vs container separation
- Custom hooks for logic reuse
- Composition over inheritance
- Props for customization

### State Management
- Local state when possible
- Lift state only when needed
- Derived state, not duplicated
- Memoize expensive calculations

### Accessibility
- Semantic HTML
- ARIA labels where needed
- Keyboard navigation
- Focus management
- Color contrast

### Performance
- Lazy load heavy components
- Memoize appropriately
- Avoid unnecessary re-renders
- Optimize images

## Constraints
- Follow plan exactly
- Match existing component patterns
- All code must be accessible
- Must pass all verification steps
```

**Acceptance Criteria:**
- [x] Implements components per plan
- [x] Follows existing patterns
- [x] Accessibility requirements met
- [x] All verification passes
- [x] Tests included

---

**Sub-Agent: `database-specialist`**

| Attribute | Value |
|-----------|-------|
| File | `.claude/agents/implementation/database-specialist.md` |
| Model | `sonnet` |
| Tools | `Read, Write, Edit, Bash, Grep` |
| Skills | `clean-code`, `migration` |

**Specification:**
```markdown
---
name: database-specialist
description: Implement database schemas, migrations, and queries. Use for all 
  database-related implementations including schema changes, query optimization,
  and data migrations.
tools: Read, Write, Edit, Bash, Grep
model: sonnet
skills: clean-code, migration
---

# Database Specialist

You are a senior database engineer specializing in schema design, migrations,
and query optimization.

## Primary Responsibilities
1. Design and implement schemas
2. Create reversible migrations
3. Optimize queries
4. Ensure data integrity
5. Document data models

## Implementation Protocol

### Step 1: Review Requirements
- Data entities needed
- Relationships
- Constraints
- Performance requirements

### Step 2: Schema Design
- Normalize appropriately
- Define indexes
- Set constraints
- Plan for growth

### Step 3: Migration Creation
Always create reversible migrations:
```sql
-- UP
CREATE TABLE ...

-- DOWN
DROP TABLE ...
```

### Step 4: Verify
```bash
npm run migrate:status
npm run migrate:up
npm run migrate:down
npm run migrate:up # Verify reversibility
npm test -- database
```

## Migration Best Practices

### Safety
- Always have down migration
- Test on copy of production data
- Handle existing data
- Consider timeout for large tables

### Naming
```
YYYYMMDDHHMMSS_descriptive_name.sql
20251214120000_create_users_table.sql
20251214120100_add_email_index.sql
```

### Order
1. Create tables
2. Add columns
3. Create indexes
4. Add constraints
5. Migrate data

### Rollback Plan
- Document manual steps if needed
- Test rollback procedure
- Have data backup strategy

## Query Optimization
- Use EXPLAIN ANALYZE
- Index frequently queried columns
- Avoid N+1 queries
- Use appropriate join types
- Consider pagination

## Constraints
- All migrations must be reversible
- No destructive changes without explicit approval
- Must pass all database tests
- Document breaking changes
```

**Acceptance Criteria:**
- [x] Schemas properly normalized
- [x] Migrations are reversible
- [x] Indexes created appropriately
- [x] Verification passes
- [x] Breaking changes documented

---

#### 4.2.2 Implementation Skills

**Skill: `clean-code-skill`**

| Attribute | Value |
|-----------|-------|
| Location | `.claude/skills/implementation/clean-code/` |
| Files | `SKILL.md`, `principles/*.md`, `checklists/pre-commit.md` |
| Used By | ALL implementation sub-agents |

**SKILL.md:**
```markdown
---
name: clean-code
description: Enforce SOLID, DRY, KISS principles during implementation. 
  Auto-activated when writing or modifying code.
---

# Clean Code Skill

## Purpose
Ensure all code follows clean code principles.

## Core Principles

### SOLID
Reference: [principles/solid.md](principles/solid.md)

### DRY (Don't Repeat Yourself)
Reference: [principles/dry.md](principles/dry.md)
- Extract common logic to functions
- Use constants for magic values
- Create shared utilities

### KISS (Keep It Simple, Stupid)
Reference: [principles/kiss.md](principles/kiss.md)
- Favor readability over cleverness
- One thing per function
- Obvious over implicit

### YAGNI (You Aren't Gonna Need It)
Reference: [principles/yagni.md](principles/yagni.md)
- Implement only what's needed now
- No speculative generalization
- Add complexity when required

## Code Quality Checklist
Use before committing: [checklists/pre-commit.md](checklists/pre-commit.md)

### Naming
- [ ] Variables describe content
- [ ] Functions describe action
- [ ] Classes describe entity
- [ ] No abbreviations (except common ones)

### Functions
- [ ] Single responsibility
- [ ] < 20 lines preferred
- [ ] < 5 parameters
- [ ] No side effects where possible

### Comments
- [ ] Explain why, not what
- [ ] Update when code changes
- [ ] Remove commented-out code

### Error Handling
- [ ] Specific error types
- [ ] Meaningful messages
- [ ] Proper logging
- [ ] Recovery or fail gracefully

## Auto-Checks
When implementing, verify:
```bash
npm run lint
npm run typecheck
```
```

**principles/solid.md:**
```markdown
# SOLID Principles

## S - Single Responsibility Principle
> A class should have only one reason to change.

**Good:**
```typescript
class UserRepository {
  findById(id: string): User {}
  save(user: User): void {}
}

class UserValidator {
  validate(user: User): ValidationResult {}
}
```

**Bad:**
```typescript
class User {
  findById(id: string): User {}
  validate(): ValidationResult {}
  sendEmail(): void {}
  formatForDisplay(): string {}
}
```

## O - Open/Closed Principle
> Open for extension, closed for modification.

**Good:**
```typescript
interface PaymentProcessor {
  process(amount: number): void;
}

class StripeProcessor implements PaymentProcessor {}
class PayPalProcessor implements PaymentProcessor {}
```

**Bad:**
```typescript
class PaymentProcessor {
  process(amount: number, type: 'stripe' | 'paypal') {
    if (type === 'stripe') { ... }
    else if (type === 'paypal') { ... }
  }
}
```

## L - Liskov Substitution Principle
> Subtypes must be substitutable for their base types.

## I - Interface Segregation Principle
> Clients shouldn't depend on interfaces they don't use.

## D - Dependency Inversion Principle
> Depend on abstractions, not concretions.
```

**Acceptance Criteria:**
- [x] SOLID principles documented with examples
- [x] DRY, KISS, YAGNI documented
- [x] Pre-commit checklist comprehensive
- [x] Auto-check commands included

---

**Skill: `api-design-skill`**

| Attribute | Value |
|-----------|-------|
| Location | `.claude/skills/implementation/api-design/` |
| Files | `SKILL.md`, `standards/*.md`, `templates/endpoint-doc.md` |
| Used By | `backend-developer` |

**SKILL.md:**
```markdown
---
name: api-design
description: Design RESTful APIs following conventions with proper error 
  handling, versioning, and documentation. Use when creating or modifying 
  API endpoints.
---

# API Design Skill

## Purpose
Create consistent, well-designed APIs.

## REST Conventions
Reference: [standards/rest-conventions.md](standards/rest-conventions.md)

### HTTP Methods
| Method | Use Case | Idempotent |
|--------|----------|------------|
| GET | Retrieve resource | Yes |
| POST | Create resource | No |
| PUT | Replace resource | Yes |
| PATCH | Partial update | No |
| DELETE | Remove resource | Yes |

### URL Patterns
```
GET    /users           # List users
GET    /users/:id       # Get user
POST   /users           # Create user
PUT    /users/:id       # Replace user
PATCH  /users/:id       # Update user
DELETE /users/:id       # Delete user

GET    /users/:id/posts # Nested resource
```

### Response Status Codes
| Code | Meaning | Use When |
|------|---------|----------|
| 200 | OK | Successful GET, PUT, PATCH |
| 201 | Created | Successful POST |
| 204 | No Content | Successful DELETE |
| 400 | Bad Request | Validation error |
| 401 | Unauthorized | Auth required |
| 403 | Forbidden | Auth insufficient |
| 404 | Not Found | Resource doesn't exist |
| 422 | Unprocessable | Business rule violation |
| 500 | Server Error | Unexpected error |

## Error Response Format
Reference: [standards/error-responses.md](standards/error-responses.md)

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Validation failed",
    "details": [
      {
        "field": "email",
        "message": "Invalid email format"
      }
    ]
  }
}
```

## Versioning
Reference: [standards/versioning.md](standards/versioning.md)

Options:
- URL: `/api/v1/users`
- Header: `Accept: application/vnd.api.v1+json`

Recommendation: URL versioning for simplicity

## Endpoint Documentation
Use template: [templates/endpoint-doc.md](templates/endpoint-doc.md)
```

**Acceptance Criteria:**
- [x] REST conventions documented
- [x] Error response format standardized
- [x] Versioning strategy defined
- [x] Endpoint documentation template provided

---

**Skill: `component-design-skill`**

| Attribute | Value |
|-----------|-------|
| Location | `.claude/skills/implementation/component-design/` |
| Files | `SKILL.md`, `patterns/*.md`, `templates/component-template.tsx` |
| Used By | `frontend-developer` |

**SKILL.md:**
```markdown
---
name: component-design
description: Design React/Vue components following atomic design and composition 
  patterns. Use when creating UI components.
---

# Component Design Skill

## Purpose
Create consistent, reusable UI components.

## Atomic Design
Reference: [patterns/atomic-design.md](patterns/atomic-design.md)

### Hierarchy
1. **Atoms**: Basic elements (Button, Input, Label)
2. **Molecules**: Simple groups (FormField, SearchBox)
3. **Organisms**: Complex sections (Header, Form, Card)
4. **Templates**: Page layouts
5. **Pages**: Specific instances

## Component Patterns
Reference: [patterns/composition.md](patterns/composition.md)

### Compound Components
```tsx
<Select>
  <Select.Trigger />
  <Select.Content>
    <Select.Item value="1">Option 1</Select.Item>
  </Select.Content>
</Select>
```

### Render Props
```tsx
<DataFetcher url="/api/users">
  {({ data, loading }) => (
    loading ? <Spinner /> : <UserList users={data} />
  )}
</DataFetcher>
```

### Custom Hooks
```tsx
function useUser(id: string) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  // ...
  return { user, loading, error };
}
```

## Props Interface
```tsx
interface ButtonProps {
  /** Visual variant of the button */
  variant?: 'primary' | 'secondary' | 'ghost';
  /** Size of the button */
  size?: 'sm' | 'md' | 'lg';
  /** Whether button is disabled */
  disabled?: boolean;
  /** Click handler */
  onClick?: () => void;
  /** Button content */
  children: React.ReactNode;
}
```

## Component Template
Use: [templates/component-template.tsx](templates/component-template.tsx)

## State Management
Reference: [patterns/state-management.md](patterns/state-management.md)

### Decision Tree
1. UI-only state → `useState`
2. Complex local state → `useReducer`
3. Shared between siblings → Lift to parent
4. Shared across app → Context or global store
5. Server state → React Query/SWR
```

**Acceptance Criteria:**
- [x] Atomic design levels documented
- [x] Composition patterns explained
- [x] Props interface pattern defined
- [x] State management guidelines clear
- [x] Component template provided

---

**Skill: `error-handling-skill`**

| Attribute | Value |
|-----------|-------|
| Location | `.claude/skills/implementation/error-handling/` |
| Files | `SKILL.md`, `patterns/*.md`, `templates/error-class.ts` |
| Used By | `backend-developer`, `frontend-developer` |

**SKILL.md:**
```markdown
---
name: error-handling
description: Implement consistent error handling across the application. 
  Use when adding try-catch blocks, error boundaries, or custom error classes.
---

# Error Handling Skill

## Purpose
Ensure consistent, informative error handling.

## Backend Error Handling
Reference: [patterns/backend-errors.md](patterns/backend-errors.md)

### Custom Error Classes
```typescript
// templates/error-class.ts
export class AppError extends Error {
  constructor(
    public code: string,
    message: string,
    public statusCode: number = 500,
    public details?: unknown
  ) {
    super(message);
    this.name = 'AppError';
  }
}

export class ValidationError extends AppError {
  constructor(message: string, details?: unknown) {
    super('VALIDATION_ERROR', message, 400, details);
  }
}

export class NotFoundError extends AppError {
  constructor(resource: string) {
    super('NOT_FOUND', `${resource} not found`, 404);
  }
}
```

### Error Handler Middleware
```typescript
function errorHandler(err, req, res, next) {
  logger.error(err);
  
  if (err instanceof AppError) {
    return res.status(err.statusCode).json({
      error: {
        code: err.code,
        message: err.message,
        details: err.details
      }
    });
  }
  
  return res.status(500).json({
    error: {
      code: 'INTERNAL_ERROR',
      message: 'An unexpected error occurred'
    }
  });
}
```

## Frontend Error Handling
Reference: [patterns/frontend-errors.md](patterns/frontend-errors.md)

### Error Boundaries
```tsx
class ErrorBoundary extends React.Component {
  state = { hasError: false };
  
  static getDerivedStateFromError() {
    return { hasError: true };
  }
  
  componentDidCatch(error, info) {
    logError(error, info);
  }
  
  render() {
    if (this.state.hasError) {
      return <ErrorFallback onReset={() => this.setState({ hasError: false })} />;
    }
    return this.props.children;
  }
}
```

### Async Error Handling
```typescript
async function fetchWithError<T>(url: string): Promise<T> {
  const response = await fetch(url);
  
  if (!response.ok) {
    const error = await response.json();
    throw new ApiError(error.code, error.message);
  }
  
  return response.json();
}
```

## Logging Guidelines
| Level | Use For |
|-------|---------|
| error | Exceptions, failures |
| warn | Recoverable issues |
| info | Important events |
| debug | Development info |
```

**Acceptance Criteria:**
- [x] Custom error classes defined
- [x] Backend middleware pattern provided
- [x] Frontend error boundaries explained
- [x] Logging guidelines clear

---

**Skill: `migration-skill`**

| Attribute | Value |
|-----------|-------|
| Location | `.claude/skills/implementation/migration/` |
| Files | `SKILL.md`, `templates/migration-template.sql`, `checklists/pre-migration.md` |
| Used By | `database-specialist` |

**SKILL.md:**
```markdown
---
name: migration
description: Create reversible database migrations with rollback scripts. 
  Use when modifying database schemas.
---

# Migration Skill

## Purpose
Create safe, reversible database migrations.

## Migration Template
Use: [templates/migration-template.sql](templates/migration-template.sql)

```sql
-- Migration: [description]
-- Created: [date]
-- Author: [name]

-- ==================== UP ====================
BEGIN;

-- Your migration here
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email VARCHAR(255) NOT NULL UNIQUE,
  created_at TIMESTAMP DEFAULT NOW()
);

COMMIT;

-- ==================== DOWN ====================
BEGIN;

DROP TABLE IF EXISTS users;

COMMIT;
```

## Pre-Migration Checklist
Use: [checklists/pre-migration.md](checklists/pre-migration.md)

- [ ] Down migration works
- [ ] Tested on production-like data
- [ ] Performance impact assessed
- [ ] Backup plan documented
- [ ] Deployment timing considered

## Migration Types

### Safe Migrations
- Add table
- Add nullable column
- Add index (CONCURRENTLY)
- Add foreign key (without validation)

### Risky Migrations
- Drop table (verify no references)
- Drop column (verify no usage)
- Rename column (may break app)
- Change column type (may lose data)

### Dangerous Migrations
- Truncate table
- Drop database
- Remove constraints

## Large Table Migrations
For tables with >1M rows:
1. Create new structure
2. Backfill in batches
3. Add constraints
4. Switch over
5. Clean up old structure

## Rollback Strategy
- Test down migration before running up
- Document manual rollback steps
- Have production backup
- Consider feature flags for code changes
```

**Acceptance Criteria:**
- [x] Migration template provided
- [x] Pre-migration checklist comprehensive
- [x] Migration types categorized by risk
- [x] Large table strategy documented

---

#### 4.2.3 Implementation Slash Command

**Command: `/phase-implement`**

| Attribute | Value |
|-----------|-------|
| File | `.claude/commands/phase-implement.md` |
| Purpose | Execute implementation phase of RQPIV |

```markdown
# Execute Implementation Phase

Execute implementation plan for: $ARGUMENTS

## Prerequisites Check
- [ ] Planning phase completed
- [ ] Architecture approved
- [ ] Implementation plan approved
- [ ] Plan document in `docs/plans/`

## Execution Steps

1. **Load Implementation Plan**
   Read: `docs/plans/implementation-{session}.md`

2. **Switch to Auto-Accept Mode**
   Enter Shift+Tab to enable auto-accept

3. **Execute Tasks In Order**
   For each task:
   a. Invoke appropriate developer sub-agent
   b. Implement per task specification
   c. Run task verification
   d. Log completion

4. **Quality Checks Per Task**
   After each task:
   ```bash
   npm run typecheck
   npm run lint
   ```

5. **Commit After Each Task**
   Using commit message from plan:
   ```bash
   git add -A
   git commit -m "[message from plan]"
   ```

6. **Track Progress**
   Update session file with:
   - Tasks completed
   - Tasks remaining
   - Any deviations

7. **Transition to Validation**
   After all tasks:
   - Summarize changes made
   - List files modified
   - Prepare for validation phase

## Sub-Agent Routing

| Task Type | Sub-Agent |
|-----------|-----------|
| API/Backend | backend-developer |
| UI/Frontend | frontend-developer |
| Database | database-specialist |
| Mixed | Route to primary concern |

## Deviation Handling
If plan cannot be followed exactly:
1. Document deviation
2. Explain rationale
3. Get approval if significant
4. Update plan document

## Gate: All tasks must complete before validation
```

**Acceptance Criteria:**
- [x] Loads and follows implementation plan
- [x] Routes to correct developer sub-agents
- [x] Runs verification after each task
- [x] Commits after each task
- [x] Tracks progress in session file
- [x] Handles deviations appropriately

---

### 4.3 Phase 4 Testing Requirements

| Test Case | Description | Expected Result |
|-----------|-------------|-----------------|
| TC-4.1 | Backend task implementation | Follows SOLID, passes verification |
| TC-4.2 | Frontend task implementation | Accessible, follows patterns |
| TC-4.3 | Database migration | Reversible, passes tests |
| TC-4.4 | Clean code enforcement | Checklist items verified |
| TC-4.5 | Task routing | Correct sub-agent selected |
| TC-4.6 | Commit per task | Git history shows task commits |
| TC-4.7 | Deviation handling | Documented and approved |

### 4.4 Phase 4 Success Criteria

- [x] All 3 developer sub-agents implemented
- [x] All 5 implementation skills implemented
- [x] `/phase-implement` command functional
- [x] Quality checks running after each task
- [x] Commits created per task
- [x] Deviation handling working

---

## Phase 5: Validation & Quality Gates

**Duration:** 2-3 weeks
**Priority:** High
**Dependencies:** Phase 4 complete
**Status:** ✅ COMPLETED (December 15, 2025)  

### 5.1 Objectives

- Implement validation sub-agents
- Create validation skills
- Build automated quality gates
- Establish validation workflow

### 5.2 Deliverables

#### 5.2.1 Validation Sub-Agents

**Sub-Agent: `code-reviewer`**

| Attribute | Value |
|-----------|-------|
| File | `.claude/agents/validation/code-reviewer.md` |
| Model | `inherit` |
| Tools | `Read, Grep, Glob, Bash` |
| Skills | `code-review` |

**Specification:**
```markdown
---
name: code-reviewer
description: PROACTIVELY review code after any implementation. Expert in code 
  quality, security, and maintainability. MUST BE USED after writing or 
  modifying code.
tools: Read, Grep, Glob, Bash
model: inherit
skills: code-review
---

# Code Reviewer

You are a senior code reviewer focused on quality, security, and maintainability.

## Primary Responsibilities
1. Review all code changes
2. Identify quality issues
3. Check security concerns
4. Verify pattern compliance
5. Suggest improvements

## Review Protocol

### Step 1: Gather Changes
```bash
git diff HEAD~[N]..HEAD
git log --oneline -[N]
```

### Step 2: Review Each File
For each changed file:
- Read full context
- Check against patterns
- Verify error handling
- Check types

### Step 3: Categorize Issues

#### Critical (Must Fix)
- Security vulnerabilities
- Data loss risks
- Breaking changes
- Runtime errors

#### Warning (Should Fix)
- Performance issues
- Code smell
- Missing error handling
- Inadequate types

#### Suggestion (Consider)
- Naming improvements
- Refactoring opportunities
- Documentation gaps
- Test coverage

### Step 4: Create Report
Save to: `docs/reviews/code-review-{session}.md`

```markdown
# Code Review Report

**Date:** [date]
**Reviewer:** code-reviewer
**Files Reviewed:** [count]

## Summary
- Critical Issues: [count]
- Warnings: [count]
- Suggestions: [count]

## Critical Issues
### [Issue 1]
- **File:** [path]
- **Line:** [number]
- **Issue:** [description]
- **Fix:** [recommendation]

## Warnings
...

## Suggestions
...

## Patterns Compliance
- [ ] Naming conventions followed
- [ ] Error handling consistent
- [ ] Types complete
- [ ] Tests adequate

## Recommendation
[APPROVE | APPROVE WITH CHANGES | REQUEST CHANGES]
```

## Gate
- Critical issues: MUST be fixed
- Warnings: SHOULD be fixed
- Cannot proceed to commit with critical issues
```

**Acceptance Criteria:**
- [x] Reviews all changed files
- [x] Categorizes issues by severity
- [x] Generates structured report
- [x] Enforces critical issue resolution
- [x] Provides actionable recommendations

---

**Sub-Agent: `test-automator`**

| Attribute | Value |
|-----------|-------|
| File | `.claude/agents/validation/test-automator.md` |
| Model | `sonnet` |
| Tools | `Read, Write, Edit, Bash, Grep, Glob` |
| Skills | `test-generation` |

**Specification:**
```markdown
---
name: test-automator
description: Write and run tests for implemented code. Use PROACTIVELY after 
  implementations to ensure test coverage. Creates unit, integration, and 
  e2e tests as needed.
tools: Read, Write, Edit, Bash, Grep, Glob
model: sonnet
skills: test-generation
---

# Test Automator

You are a senior QA engineer specializing in test automation.

## Primary Responsibilities
1. Analyze code for test needs
2. Write comprehensive tests
3. Run test suite
4. Report coverage
5. Identify gaps

## Testing Protocol

### Step 1: Identify Test Needs
Review changed code:
- New functions → Unit tests
- API endpoints → Integration tests
- UI components → Component tests
- User flows → E2E tests

### Step 2: Check Existing Tests
- Are there existing tests?
- Do they cover new code?
- Do they still pass?

### Step 3: Write Missing Tests
Follow project test patterns:
- File naming convention
- Test structure
- Mocking approach
- Assertion style

### Step 4: Run Tests
```bash
npm test -- --coverage
npm run test:e2e # if applicable
```

### Step 5: Generate Report
Save to: `docs/reviews/test-report-{session}.md`

```markdown
# Test Report

**Date:** [date]
**Total Tests:** [count]
**Passed:** [count]
**Failed:** [count]

## Coverage Summary
| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| Lines | [%] | 80% | [✓/✗] |
| Functions | [%] | 80% | [✓/✗] |
| Branches | [%] | 70% | [✓/✗] |

## New Tests Added
- [test file]: [count] tests

## Failing Tests
### [Test Name]
- **File:** [path]
- **Error:** [message]
- **Cause:** [analysis]

## Coverage Gaps
- [file/function]: [reason not covered]

## Recommendation
[PASS | NEEDS WORK]
```

## Test Types

### Unit Tests
- Single function/method
- Mocked dependencies
- Fast execution
- Cover edge cases

### Integration Tests
- Multiple components
- Real dependencies
- API testing
- Database testing

### E2E Tests
- Full user flows
- Browser automation
- Critical paths only
- Slower execution
```

**Acceptance Criteria:**
- [x] Identifies test gaps
- [x] Writes tests following patterns
- [x] Generates coverage report
- [x] Identifies failing tests
- [x] Provides coverage recommendations

---

**Sub-Agent: `security-auditor`**

| Attribute | Value |
|-----------|-------|
| File | `.claude/agents/validation/security-auditor.md` |
| Model | `sonnet` |
| Tools | `Read, Grep, Glob, Bash` |
| Skills | `security-scan` |

**Specification:**
```markdown
---
name: security-auditor
description: Audit code for security vulnerabilities, OWASP compliance, and 
  secure coding practices. Use for security-sensitive implementations or 
  regular security reviews.
tools: Read, Grep, Glob, Bash
model: sonnet
skills: security-scan
---

# Security Auditor

You are a security specialist focused on application security.

## Primary Responsibilities
1. Identify security vulnerabilities
2. Check OWASP Top 10
3. Verify authentication/authorization
4. Audit data handling
5. Review dependencies

## Security Audit Protocol

### Step 1: Dependency Audit
```bash
npm audit
# or equivalent for other package managers
```

### Step 2: Code Analysis
Check for:
- SQL injection
- XSS vulnerabilities
- CSRF issues
- Authentication flaws
- Authorization bypasses
- Sensitive data exposure

### Step 3: OWASP Top 10 Check
Reference checklist for each item:
1. Injection
2. Broken Authentication
3. Sensitive Data Exposure
4. XML External Entities
5. Broken Access Control
6. Security Misconfiguration
7. Cross-Site Scripting
8. Insecure Deserialization
9. Using Components with Known Vulnerabilities
10. Insufficient Logging & Monitoring

### Step 4: Authentication Review
- Password handling
- Session management
- Token security
- MFA implementation

### Step 5: Generate Report
Save to: `docs/reviews/security-audit-{session}.md`

```markdown
# Security Audit Report

**Date:** [date]
**Scope:** [files/features reviewed]

## Vulnerability Summary
| Severity | Count |
|----------|-------|
| Critical | [N] |
| High | [N] |
| Medium | [N] |
| Low | [N] |

## Critical Vulnerabilities
### [Vuln-1]
- **Type:** [category]
- **Location:** [file:line]
- **Description:** [details]
- **Impact:** [potential damage]
- **Remediation:** [how to fix]

## OWASP Compliance
| Category | Status | Notes |
|----------|--------|-------|
| Injection | [✓/✗] | [notes] |
| ... | ... | ... |

## Dependency Vulnerabilities
[output from npm audit or equivalent]

## Recommendations
1. [Priority action 1]
2. [Priority action 2]

## Recommendation
[SECURE | NEEDS REMEDIATION]
```

## Gate
- Critical/High vulnerabilities: MUST be fixed
- Medium vulnerabilities: SHOULD be fixed
- Cannot deploy with critical vulnerabilities
```

**Acceptance Criteria:**
- [x] Runs dependency audit
- [x] Checks OWASP Top 10
- [x] Reviews authentication
- [x] Generates comprehensive report
- [x] Enforces remediation for critical issues

---

**Sub-Agent: `documentation-writer`**

| Attribute | Value |
|-----------|-------|
| File | `.claude/agents/validation/documentation-writer.md` |
| Model | `haiku` |
| Tools | `Read, Write, Edit, Grep, Glob` |
| Skills | `documentation` |

**Specification:**
```markdown
---
name: documentation-writer
description: Generate and update documentation for implemented features. 
  Use after successful implementation and testing to ensure documentation 
  is current.
tools: Read, Write, Edit, Grep, Glob
model: haiku
skills: documentation
---

# Documentation Writer

You are a technical writer focused on clear, accurate documentation.

## Primary Responsibilities
1. Update README files
2. Document APIs
3. Write inline comments
4. Create changelogs
5. Update user guides

## Documentation Protocol

### Step 1: Identify Documentation Needs
Based on changes:
- New features → README update
- New APIs → API documentation
- New components → Component docs
- Breaking changes → Migration guide

### Step 2: Review Existing Docs
- What exists?
- What's outdated?
- What's missing?

### Step 3: Update Documentation

#### README Updates
- New features section
- Updated installation
- New examples

#### API Documentation
- Endpoint descriptions
- Request/response examples
- Error codes

#### Code Comments
- JSDoc for public APIs
- Inline comments for complex logic
- TODO for known limitations

#### Changelog
```markdown
## [Version] - [Date]

### Added
- [New feature]

### Changed
- [Modification]

### Fixed
- [Bug fix]

### Deprecated
- [Deprecation]
```

### Step 4: Verify Documentation
- Code examples work
- Links are valid
- Formatting correct

### Step 5: Create Report
Save to: `docs/reviews/documentation-{session}.md`

```markdown
# Documentation Update Report

**Date:** [date]

## Files Updated
- [file]: [changes]

## New Documentation
- [file]: [description]

## Verification
- [ ] Code examples tested
- [ ] Links validated
- [ ] Spelling checked

## Remaining Gaps
- [gap 1]
```
```

**Acceptance Criteria:**
- [x] Updates relevant documentation
- [x] Follows existing documentation patterns
- [x] Verifies code examples work
- [x] Creates changelog entries
- [x] Reports documentation gaps

---

#### 5.2.2 Validation Skills

**Skill: `code-review-skill`**

| Attribute | Value |
|-----------|-------|
| Location | `.claude/skills/validation/code-review/` |
| Files | `SKILL.md`, `checklists/*.md`, `templates/review-report.md` |
| Used By | `code-reviewer` |

**SKILL.md:**
```markdown
---
name: code-review
description: Review code for quality, security, performance, and maintainability. 
  Auto-activate after code modifications.
---

# Code Review Skill

## Purpose
Ensure consistent, thorough code reviews.

## Review Checklists

### Security Checklist
Reference: [checklists/security.md](checklists/security.md)
- [ ] No hardcoded secrets
- [ ] Input validation present
- [ ] Output encoding used
- [ ] Authentication verified
- [ ] Authorization checked

### Performance Checklist
Reference: [checklists/performance.md](checklists/performance.md)
- [ ] No N+1 queries
- [ ] Appropriate caching
- [ ] Efficient algorithms
- [ ] Resource cleanup
- [ ] Pagination implemented

### Maintainability Checklist
Reference: [checklists/maintainability.md](checklists/maintainability.md)
- [ ] Code is readable
- [ ] Functions are focused
- [ ] Types are complete
- [ ] Tests exist
- [ ] Documentation present

### Accessibility Checklist (Frontend)
Reference: [checklists/accessibility.md](checklists/accessibility.md)
- [ ] Semantic HTML
- [ ] ARIA labels
- [ ] Keyboard navigation
- [ ] Color contrast
- [ ] Focus management

## Issue Severity Guidelines

### Critical
- Security vulnerabilities
- Data loss potential
- Production breaking
- Compliance violations

### Warning
- Performance issues
- Missing error handling
- Incomplete types
- Missing tests

### Suggestion
- Naming improvements
- Refactoring opportunities
- Documentation gaps
- Style consistency

## Report Template
Use: [templates/review-report.md](templates/review-report.md)
```

**Acceptance Criteria:**
- [x] All checklists comprehensive
- [x] Severity guidelines clear
- [x] Report template usable
- [x] Categories cover key areas

---

**Skill: `test-generation-skill`**

| Attribute | Value |
|-----------|-------|
| Location | `.claude/skills/validation/test-generation/` |
| Files | `SKILL.md`, `patterns/*.md`, `templates/test-template.ts` |
| Used By | `test-automator` |

**SKILL.md:**
```markdown
---
name: test-generation
description: Generate comprehensive tests following project testing patterns. 
  Use after implementing features.
---

# Test Generation Skill

## Purpose
Create consistent, comprehensive tests.

## Test Patterns

### Unit Test Pattern
Reference: [patterns/unit-tests.md](patterns/unit-tests.md)

```typescript
// templates/test-template.ts
describe('[Unit Under Test]', () => {
  describe('[method/function]', () => {
    it('should [expected behavior] when [condition]', () => {
      // Arrange
      const input = ...;
      const expected = ...;
      
      // Act
      const result = functionUnderTest(input);
      
      // Assert
      expect(result).toEqual(expected);
    });
    
    it('should throw [error] when [invalid condition]', () => {
      // Arrange
      const invalidInput = ...;
      
      // Act & Assert
      expect(() => functionUnderTest(invalidInput))
        .toThrow(ExpectedError);
    });
  });
});
```

### Integration Test Pattern
Reference: [patterns/integration-tests.md](patterns/integration-tests.md)

### E2E Test Pattern
Reference: [patterns/e2e-tests.md](patterns/e2e-tests.md)

## Coverage Targets
| Type | Lines | Functions | Branches |
|------|-------|-----------|----------|
| Unit | 80% | 80% | 70% |
| Integration | 60% | 60% | 50% |
| E2E | Critical paths | - | - |

## Test Naming Convention
```
[should/does] [expected behavior] [when/given] [condition]
```

Examples:
- `should return user when valid ID provided`
- `should throw NotFoundError when user does not exist`
- `should disable button when form is invalid`

## What to Test
- Happy path (normal operation)
- Edge cases (boundaries)
- Error cases (exceptions)
- State transitions
```

**Acceptance Criteria:**
- [x] Test patterns documented
- [x] Coverage targets defined
- [x] Naming convention clear
- [x] Templates provided

---

**Skill: `security-scan-skill`**

| Attribute | Value |
|-----------|-------|
| Location | `.claude/skills/validation/security-scan/` |
| Files | `SKILL.md`, `checklists/*.md`, `scripts/security-scan.sh` |
| Used By | `security-auditor` |

**SKILL.md:**
```markdown
---
name: security-scan
description: Scan code for OWASP vulnerabilities and security issues. 
  Use for security-sensitive implementations.
---

# Security Scan Skill

## Purpose
Identify and prevent security vulnerabilities.

## OWASP Top 10 Checklist
Reference: [checklists/owasp-top-10.md](checklists/owasp-top-10.md)

### A01: Broken Access Control
- [ ] Authorization on all endpoints
- [ ] Deny by default
- [ ] Rate limiting implemented
- [ ] CORS properly configured

### A02: Cryptographic Failures
- [ ] Data encrypted in transit (HTTPS)
- [ ] Sensitive data encrypted at rest
- [ ] Strong algorithms used
- [ ] Keys properly managed

### A03: Injection
- [ ] Parameterized queries
- [ ] Input validation
- [ ] Output encoding
- [ ] No eval() with user input

[Continue for all 10...]

## Authentication Checklist
Reference: [checklists/auth-security.md](checklists/auth-security.md)
- [ ] Passwords hashed (bcrypt/argon2)
- [ ] Session properly managed
- [ ] Tokens securely stored
- [ ] Logout invalidates session

## Data Validation Checklist
Reference: [checklists/data-validation.md](checklists/data-validation.md)
- [ ] All input validated
- [ ] Type checking enforced
- [ ] Size limits set
- [ ] Format validation done

## Automated Scan Script
Run: `scripts/security-scan.sh`

```bash
#!/bin/bash
# Run dependency audit
npm audit

# Run static analysis (if available)
npx eslint --plugin security .

# Check for secrets
npx secretlint .
```
```

**Acceptance Criteria:**
- [x] OWASP Top 10 checklist complete
- [x] Authentication checklist comprehensive
- [x] Automated scan script functional
- [x] Data validation covered

---

**Skill: `documentation-skill`**

| Attribute | Value |
|-----------|-------|
| Location | `.claude/skills/validation/documentation/` |
| Files | `SKILL.md`, `templates/*.md`, `scripts/generate-docs.py` |
| Used By | `documentation-writer` |

**SKILL.md:**
```markdown
---
name: documentation
description: Generate and update documentation from code. 
  Use after successful implementation.
---

# Documentation Skill

## Purpose
Maintain accurate, helpful documentation.

## Templates

### README Template
Reference: [templates/readme-template.md](templates/readme-template.md)

```markdown
# Project Name

Brief description of the project.

## Features

- Feature 1
- Feature 2

## Installation

```bash
npm install
```

## Usage

```javascript
// Example code
```

## API Reference

[Link to API docs]

## Contributing

[Link to contributing guide]

## License

[License type]
```

### API Documentation Template
Reference: [templates/api-doc-template.md](templates/api-doc-template.md)

### Changelog Template
Reference: [templates/changelog-template.md](templates/changelog-template.md)

## JSDoc Standards
```typescript
/**
 * Brief description of what the function does.
 * 
 * @param {string} name - Description of name parameter
 * @param {Options} options - Description of options
 * @returns {Result} Description of return value
 * @throws {ValidationError} When validation fails
 * @example
 * const result = myFunction('test', { flag: true });
 */
function myFunction(name: string, options: Options): Result {
  // ...
}
```

## Documentation Checklist
- [ ] README up to date
- [ ] API endpoints documented
- [ ] Code examples work
- [ ] Changelog updated
- [ ] JSDoc on public APIs
```

**Acceptance Criteria:**
- [x] Templates cover key documentation types
- [x] JSDoc standards defined
- [x] Documentation checklist complete
- [x] Examples provided

---

#### 5.2.3 Validation Slash Command

**Command: `/phase-validate`**

| Attribute | Value |
|-----------|-------|
| File | `.claude/commands/phase-validate.md` |
| Purpose | Execute validation phase of RQPIV |

```markdown
# Execute Validation Phase

Run validation for: $ARGUMENTS

## Prerequisites Check
- [ ] Implementation phase completed
- [ ] All tasks marked complete
- [ ] No pending deviations

## Execution Steps

1. **Run Code Review**
   Invoke code-reviewer sub-agent:
   - Review all changes
   - Generate review report
   - Identify issues by severity

2. **Check for Critical Issues**
   If critical issues found:
   - STOP validation
   - Return to implementation
   - Fix critical issues
   - Restart validation

3. **Run Tests**
   Invoke test-automator sub-agent:
   - Run existing tests
   - Generate new tests if needed
   - Generate coverage report

4. **Check Test Results**
   If tests fail:
   - STOP validation
   - Return to implementation
   - Fix failing tests
   - Restart validation

5. **Run Security Audit**
   Invoke security-auditor sub-agent:
   - Check OWASP compliance
   - Audit dependencies
   - Generate security report

6. **Check Security Results**
   If critical vulnerabilities:
   - STOP validation
   - Return to implementation
   - Fix vulnerabilities
   - Restart validation

7. **Update Documentation**
   Invoke documentation-writer sub-agent:
   - Update README if needed
   - Document new APIs
   - Update changelog

8. **Generate Final Report**
   Combine all validation reports:
   - Code review summary
   - Test coverage summary
   - Security audit summary
   - Documentation status

9. **Determine Final Status**
   - All validations pass → READY FOR MERGE
   - Warnings only → READY WITH NOTES
   - Failures → NEEDS REMEDIATION

## Outputs
- `docs/reviews/code-review-{session}.md`
- `docs/reviews/test-report-{session}.md`
- `docs/reviews/security-audit-{session}.md`
- `docs/reviews/documentation-{session}.md`
- `docs/reviews/final-validation-{session}.md`

## Gate: Cannot merge without passing validation
```

**Acceptance Criteria:**
- [x] Invokes all validation sub-agents
- [x] Stops on critical issues
- [x] Generates all reports
- [x] Produces final validation status
- [x] Enforces merge gate

---

### 5.3 Phase 5 Testing Requirements

| Test Case | Description | Expected Result |
|-----------|-------------|-----------------|
| TC-5.1 | Code review execution | Report with categorized issues |
| TC-5.2 | Critical issue handling | Validation stops, returns to impl |
| TC-5.3 | Test automation | Tests run, coverage reported |
| TC-5.4 | Security audit | OWASP checklist completed |
| TC-5.5 | Documentation update | Docs updated for changes |
| TC-5.6 | Final report generation | Combined validation report |
| TC-5.7 | Merge gate enforcement | Cannot proceed with failures |

### 5.4 Phase 5 Success Criteria

- [x] All 4 validation sub-agents implemented
- [x] All 4 validation skills implemented
- [x] `/phase-validate` command functional
- [x] Validation reports generating correctly
- [x] Merge gate enforced
- [x] Integration with implementation phase working

---

## Phase 6: Orchestration & Integration

**Duration:** 2-3 weeks  
**Priority:** High  
**Dependencies:** Phases 1-5 complete  

### 6.1 Objectives

- Implement orchestration sub-agent
- Create shared/cross-phase skills
- Build end-to-end workflow integration
- Establish session management
- Create comprehensive documentation

### 6.2 Deliverables

#### 6.2.1 Orchestration Sub-Agent

**Sub-Agent: `workflow-orchestrator`**

| Attribute | Value |
|-----------|-------|
| File | `.claude/agents/orchestration/workflow-orchestrator.md` |
| Model | `opus` |
| Tools | `Read, Write, Bash` |
| Skills | `context-preservation` |

**Specification:**
```markdown
---
name: workflow-orchestrator
description: Coordinate multi-phase RQPIV workflows. Use for complex features 
  requiring multiple sub-agents across all phases. Manages transitions, 
  handoffs, and session state.
tools: Read, Write, Bash
model: opus
skills: context-preservation
---

# Workflow Orchestrator

You are a senior engineering manager orchestrating complex development workflows.

## Primary Responsibilities
1. Manage RQPIV phase transitions
2. Coordinate sub-agent handoffs
3. Track session state and progress
4. Ensure quality gates are enforced
5. Generate executive summaries

## Orchestration Protocol

### Session Initialization
Create session structure:
```
docs/sessions/{date}-{slug}/
├── session.md        # Session tracking
├── research/         # Research artifacts
├── specs/            # Requirements
├── plans/            # Architecture & tasks
├── reviews/          # Validation reports
└── summary.md        # Final summary
```

### Phase Transitions

#### R → Q Transition
Prerequisites:
- [ ] All relevant research complete
- [ ] Findings documented
- [ ] No blocking gaps

Handoff:
- Create research summary
- Identify key constraints
- List open questions

#### Q → P Transition
Prerequisites:
- [ ] All blocking questions answered
- [ ] Requirements validated
- [ ] User confirmed

Handoff:
- Finalize requirements document
- Note user decisions
- Flag constraints for architect

#### P → I Transition
Prerequisites:
- [ ] Architecture approved
- [ ] Implementation plan approved
- [ ] No blocking issues

Handoff:
- Finalize task list
- Confirm execution order
- Note dependencies

#### I → V Transition
Prerequisites:
- [ ] All tasks complete
- [ ] Deviations documented
- [ ] Ready for validation

Handoff:
- List all changes
- Note deviations
- Flag risk areas

### Progress Tracking
Maintain in `session.md`:
```markdown
# Session: [name]

## Status: [PHASE]

## Progress
| Phase | Status | Started | Completed |
|-------|--------|---------|-----------|
| Research | ✓ | [time] | [time] |
| Question | ✓ | [time] | [time] |
| Plan | ● | [time] | - |
| Implement | ○ | - | - |
| Validate | ○ | - | - |

## Decisions Made
- [Decision 1]: [outcome]

## Issues Encountered
- [Issue 1]: [resolution]

## Next Actions
- [Action 1]
```

### Final Summary
After validation, create `summary.md`:
```markdown
# Feature Summary: [name]

## What Was Built
[Description]

## Key Decisions
[List with rationale]

## Files Changed
[List with brief description]

## Validation Results
[Summary of reviews]

## Known Limitations
[Any deferred items]

## Follow-up Items
[Future improvements]
```
```

**Acceptance Criteria:**
- [ ] Creates session structure
- [ ] Manages phase transitions
- [ ] Enforces prerequisites
- [ ] Tracks progress
- [ ] Generates final summary

---

#### 6.2.2 Shared Skills

**Skill: `git-workflow-skill`**

| Attribute | Value |
|-----------|-------|
| Location | `.claude/skills/shared/git-workflow/` |
| Files | `SKILL.md`, `conventions/*.md` |
| Used By | ALL implementation and validation sub-agents |

**SKILL.md:**
```markdown
---
name: git-workflow
description: Follow git conventions for commits, branches, and PRs. 
  Auto-activated during git operations.
---

# Git Workflow Skill

## Purpose
Ensure consistent git practices across all phases.

## Commit Message Convention
Reference: [conventions/commit-messages.md](conventions/commit-messages.md)

### Format
```
<type>(<scope>): <subject>

[optional body]

[optional footer]
```

### Types
| Type | Use For |
|------|---------|
| feat | New feature |
| fix | Bug fix |
| refactor | Code restructuring |
| docs | Documentation |
| test | Test changes |
| chore | Maintenance |

### Examples
```
feat(auth): implement JWT token refresh

- Add refresh token endpoint
- Update token validation logic
- Add integration tests

Closes #123
```

## Branch Naming
Reference: [conventions/branch-naming.md](conventions/branch-naming.md)

Format: `<type>/<ticket>-<description>`

Examples:
- `feat/AUTH-123-jwt-refresh`
- `fix/BUG-456-login-error`
- `refactor/TECH-789-user-service`

## PR Template
Reference: [conventions/pr-template.md](conventions/pr-template.md)

```markdown
## Description
[What does this PR do?]

## Type of Change
- [ ] Feature
- [ ] Bug fix
- [ ] Refactor
- [ ] Documentation

## Testing
[How was this tested?]

## Checklist
- [ ] Code follows project style
- [ ] Tests pass
- [ ] Documentation updated
```
```

**Acceptance Criteria:**
- [ ] Commit message format defined
- [ ] Branch naming convention clear
- [ ] PR template comprehensive
- [ ] Examples provided

---

**Skill: `context-preservation-skill`**

| Attribute | Value |
|-----------|-------|
| Location | `.claude/skills/shared/context-preservation/` |
| Files | `SKILL.md`, `templates/*.md` |
| Used By | `workflow-orchestrator`, ALL sub-agents |

**SKILL.md:**
```markdown
---
name: context-preservation
description: Generate structured handoff summaries between workflow phases. 
  Use when transitioning between RQPIV phases.
---

# Context Preservation Skill

## Purpose
Maintain context continuity across phases and sessions.

## Handoff Template
Reference: [templates/handoff-template.md](templates/handoff-template.md)

```markdown
# Phase Handoff: [From Phase] → [To Phase]

## Summary
[Brief description of what was accomplished]

## Key Findings/Decisions
1. [Finding/Decision 1]
2. [Finding/Decision 2]

## Artifacts Created
- [File 1]: [Description]
- [File 2]: [Description]

## Open Items
- [Item 1]: [Status]

## Recommendations for Next Phase
- [Recommendation 1]

## Context for Next Agent
[Specific information the next phase needs]
```

## Progress Summary Template
Reference: [templates/progress-summary.md](templates/progress-summary.md)

```markdown
# Progress Summary

## Completed
- [X] [Task 1]
- [X] [Task 2]

## In Progress
- [ ] [Task 3] - [Status]

## Blocked
- [ ] [Task 4] - [Blocker]

## Next Steps
1. [Step 1]
2. [Step 2]
```

## Session Resume Template
Reference: [templates/session-resume.md](templates/session-resume.md)

For resuming interrupted sessions:
```markdown
# Session Resume: [session-id]

## Last Known State
- Phase: [phase]
- Last Action: [action]
- Time: [timestamp]

## Context to Reload
- [File 1]
- [File 2]

## Continue From
[Instruction for resuming]
```
```

**Acceptance Criteria:**
- [ ] Handoff template comprehensive
- [ ] Progress summary clear
- [ ] Session resume enables continuation
- [ ] Templates are usable

---

#### 6.2.3 Master Slash Command

**Command: `/rqpiv`**

| Attribute | Value |
|-----------|-------|
| File | `.claude/commands/rqpiv.md` |
| Purpose | Execute full RQPIV workflow |

```markdown
# Execute Full RQPIV Workflow

Run complete RQPIV workflow for: $ARGUMENTS

## Overview
This command orchestrates the full Research → Question → Plan → Implement → 
Validate workflow for a feature request.

## Execution

### 1. Initialize Session
- Create session directory
- Initialize tracking file
- Enter Plan Mode

### 2. Research Phase
- Invoke /phase-research
- Await completion
- Verify findings stored

### 3. Questioning Phase
- Invoke /phase-question
- Present questions to user
- Await answers
- Validate requirements

### 4. Planning Phase
- Invoke /phase-plan
- Present architecture for approval
- Present tasks for approval
- Await plan approval

### 5. Implementation Phase
- Switch to Auto-Accept Mode
- Invoke /phase-implement
- Execute all tasks
- Track progress

### 6. Validation Phase
- Invoke /phase-validate
- Run all validations
- Handle any failures
- Generate final report

### 7. Completion
- Generate final summary
- Update session status
- Present results to user

## User Interactions
Throughout the workflow, pause for user input at:
- After questions generated (answers needed)
- After architecture created (approval needed)
- After plan created (approval needed)
- After validation (acknowledge results)

## Abort Handling
If user requests abort:
- Save current state
- Create resume instructions
- Clean up gracefully

## Resume Handling
If resuming interrupted session:
- Load session state
- Identify last completed phase
- Continue from next phase
```

**Acceptance Criteria:**
- [ ] Orchestrates full workflow
- [ ] Pauses for user input appropriately
- [ ] Handles abort gracefully
- [ ] Supports session resume
- [ ] Generates comprehensive reports

---

#### 6.2.4 Enhanced CLAUDE.md

Final CLAUDE.md with full RQPIV integration:

```markdown
# Project Context for Claude Code

## RQPIV Workflow System

This project uses the RQPIV (Research, Question, Plan, Implement, Validate) 
workflow system for all development tasks.

### Quick Start
```
/rqpiv [feature description]
```

### Manual Phase Execution
```
/rqpiv-start [task]      # Initialize workflow
/phase-research          # Research phase
/phase-question          # Questioning phase
/phase-plan              # Planning phase
/phase-implement         # Implementation phase
/phase-validate          # Validation phase
```

## Sub-Agent Reference

### Research Agents
| Agent | Purpose | Model |
|-------|---------|-------|
| codebase-explorer | Project structure | haiku |
| module-researcher | Deep module analysis | sonnet |
| frontend-researcher | Frontend architecture | sonnet |
| backend-researcher | Backend architecture | sonnet |
| dependency-researcher | Package analysis | haiku |
| pattern-researcher | Convention detection | sonnet |

### Planning Agents
| Agent | Purpose | Model |
|-------|---------|-------|
| requirement-analyst | Requirement validation | opus |
| solution-architect | Architecture design | opus |
| task-planner | Task breakdown | sonnet |

### Implementation Agents
| Agent | Purpose | Model |
|-------|---------|-------|
| backend-developer | Server-side code | sonnet |
| frontend-developer | Client-side code | sonnet |
| database-specialist | Database operations | sonnet |

### Validation Agents
| Agent | Purpose | Model |
|-------|---------|-------|
| code-reviewer | Code quality | inherit |
| test-automator | Test creation | sonnet |
| security-auditor | Security review | sonnet |
| documentation-writer | Documentation | haiku |

### Orchestration
| Agent | Purpose | Model |
|-------|---------|-------|
| workflow-orchestrator | Phase coordination | opus |

## Artifact Locations

| Type | Location |
|------|----------|
| Research findings | docs/research/ |
| Requirements | docs/specs/ |
| Architecture | docs/plans/ |
| Implementation plans | docs/plans/ |
| Review reports | docs/reviews/ |
| Session data | docs/sessions/ |

## Quality Gates

### Research → Question
- All research artifacts created
- No blocking gaps

### Question → Plan
- All blocking questions answered
- Requirements document approved

### Plan → Implement
- Architecture approved
- Implementation plan approved

### Implement → Validate
- All tasks completed
- Deviations documented

### Validate → Complete
- Code review passed (no critical issues)
- Tests passed
- Security audit passed (no critical vulnerabilities)
- Documentation updated

## Project-Specific Information

### Tech Stack
[Define your stack]

### Code Conventions
[Reference patterns detected or define]

### Build Commands
```bash
npm install        # Install dependencies
npm run dev        # Start development
npm run build      # Build for production
npm test           # Run tests
npm run lint       # Run linting
```

### Environment Setup
[Environment-specific instructions]
```

---

### 6.3 Phase 6 Testing Requirements

| Test Case | Description | Expected Result |
|-----------|-------------|-----------------|
| TC-6.1 | Full workflow execution | All phases complete successfully |
| TC-6.2 | Phase transition handoffs | Context preserved correctly |
| TC-6.3 | Session tracking | Progress accurately recorded |
| TC-6.4 | Session resume | Can continue interrupted workflow |
| TC-6.5 | Final summary generation | Comprehensive summary created |
| TC-6.6 | Git workflow compliance | Commits follow conventions |
| TC-6.7 | Integration test | End-to-end workflow on sample project |

### 6.4 Phase 6 Success Criteria

- [ ] Orchestrator sub-agent implemented
- [ ] Shared skills implemented
- [ ] `/rqpiv` master command functional
- [ ] Session management working
- [ ] Context preservation verified
- [ ] Full CLAUDE.md completed
- [ ] End-to-end workflow tested

---

## 7. Technical Requirements

### 7.1 Claude Code Requirements

| Requirement | Specification |
|-------------|---------------|
| Claude Code Version | 1.0.124 or later |
| Sub-agent Support | Required |
| Skills Support | Required |
| Plan Mode | Required |
| Auto-Accept Mode | Required |

### 7.2 Project Structure Requirements

| Directory | Purpose | Required |
|-----------|---------|----------|
| `.claude/agents/` | Sub-agent definitions | Yes |
| `.claude/skills/` | Skill definitions | Yes |
| `.claude/commands/` | Slash commands | Yes |
| `.claude/hooks/` | Event hooks | Optional |
| `docs/` | Generated artifacts | Yes |

### 7.3 Model Requirements

| Model | Use Cases | Cost Tier |
|-------|-----------|-----------|
| haiku | Fast research, documentation | Low |
| sonnet | Implementation, detailed analysis | Medium |
| opus | Architecture, complex reasoning | High |
| inherit | Match main session | Variable |

### 7.4 Tool Requirements

| Tool | Used By | Purpose |
|------|---------|---------|
| Read | All | Read files |
| Write | Implementation, Planning | Create files |
| Edit | Implementation | Modify files |
| Bash | All | Execute commands |
| Glob | Research | Find files |
| Grep | Research | Search content |

---

## 8. Success Metrics

### 8.1 Efficiency Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Context utilization reduction | 60% | Compare before/after |
| Research reuse rate | 80% | Research artifacts used in planning |
| Task completion rate | 95% | Tasks completed per plan |

### 8.2 Quality Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Code review pass rate | 90% | First-pass approval |
| Test coverage | 80% | Line coverage |
| Security audit pass rate | 95% | No critical issues |

### 8.3 User Experience Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Question clarity score | 4/5 | User rating |
| Plan accuracy | 90% | Plan vs actual |
| Documentation completeness | 95% | Checklist completion |

---

## 9. Risks & Mitigations

### 9.1 Technical Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Sub-agent context limits | Medium | High | Implement chunking strategy |
| Model inconsistency | Low | Medium | Use explicit model selection |
| Tool permission issues | Medium | Medium | Pre-configure permissions |

### 9.2 Process Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Phase skip attempts | Medium | High | Enforce gates in commands |
| User impatience | High | Medium | Show progress, estimate time |
| Scope creep | Medium | Medium | Strict plan adherence |

### 9.3 Adoption Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Learning curve | High | Medium | Comprehensive documentation |
| Workflow overhead | Medium | Medium | Optimize for common cases |
| Team resistance | Low | High | Demonstrate value early |

---

## 10. Appendices

### Appendix A: Sub-Agent Summary Table

| Agent | Phase | Model | Tools | Skills |
|-------|-------|-------|-------|--------|
| codebase-explorer | R | haiku | Read, Glob, Grep, Bash | codebase-mapping |
| module-researcher | R | sonnet | Read, Glob, Grep, Bash | codebase-mapping, pattern-detection |
| frontend-researcher | R | sonnet | Read, Glob, Grep, Bash | codebase-mapping |
| backend-researcher | R | sonnet | Read, Glob, Grep, Bash | codebase-mapping |
| dependency-researcher | R | haiku | Read, Bash, Grep | dependency-analysis |
| pattern-researcher | R | sonnet | Read, Glob, Grep | pattern-detection |
| requirement-analyst | Q | opus | Read, Write | requirement-clarification, user-intent-parser |
| solution-architect | P | opus | Read, Write, Glob, Grep | architecture-planning |
| task-planner | P | sonnet | Read, Write, Glob, Grep | task-breakdown |
| backend-developer | I | sonnet | Read, Write, Edit, Bash, Grep, Glob | clean-code, api-design, error-handling |
| frontend-developer | I | sonnet | Read, Write, Edit, Bash, Grep, Glob | clean-code, component-design, accessibility |
| database-specialist | I | sonnet | Read, Write, Edit, Bash, Grep | clean-code, migration |
| code-reviewer | V | inherit | Read, Grep, Glob, Bash | code-review |
| test-automator | V | sonnet | Read, Write, Edit, Bash, Grep, Glob | test-generation |
| security-auditor | V | sonnet | Read, Grep, Glob, Bash | security-scan |
| documentation-writer | V | haiku | Read, Write, Edit, Grep, Glob | documentation |
| workflow-orchestrator | All | opus | Read, Write, Bash | context-preservation |

### Appendix B: Skills Summary Table

| Skill | Phase | Used By |
|-------|-------|---------|
| codebase-mapping | R | codebase-explorer, module-researcher |
| dependency-analysis | R | dependency-researcher |
| pattern-detection | R | pattern-researcher, module-researcher |
| requirement-clarification | Q | requirement-analyst |
| user-intent-parser | Q | requirement-analyst |
| architecture-planning | P | solution-architect |
| task-breakdown | P | task-planner |
| clean-code | I | All developers |
| api-design | I | backend-developer |
| component-design | I | frontend-developer |
| error-handling | I | backend-developer, frontend-developer |
| migration | I | database-specialist |
| code-review | V | code-reviewer |
| test-generation | V | test-automator |
| security-scan | V | security-auditor |
| documentation | V | documentation-writer |
| git-workflow | Shared | All implementation/validation agents |
| context-preservation | Shared | workflow-orchestrator, all agents |

### Appendix C: Slash Commands Summary

| Command | Purpose | Phase |
|---------|---------|-------|
| /rqpiv | Full workflow execution | All |
| /rqpiv-start | Initialize session | Start |
| /phase-research | Execute research | R |
| /phase-question | Execute questioning | Q |
| /phase-plan | Execute planning | P |
| /phase-implement | Execute implementation | I |
| /phase-validate | Execute validation | V |

### Appendix D: Development Timeline

| Phase | Duration | Dependencies | Priority |
|-------|----------|--------------|----------|
| Phase 1: Foundation | 2-3 weeks | None | Critical |
| Phase 2: Questioning | 1-2 weeks | Phase 1 | High |
| Phase 3: Planning | 2-3 weeks | Phase 2 | High |
| Phase 4: Implementation | 3-4 weeks | Phase 3 | High |
| Phase 5: Validation | 2-3 weeks | Phase 4 | High |
| Phase 6: Orchestration | 2-3 weeks | Phases 1-5 | High |
| **Total** | **12-18 weeks** | | |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-12-14 | [Author] | Initial draft |

---

*End of PRD*
