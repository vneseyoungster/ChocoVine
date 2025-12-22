# Documentation Agents

Agents for codebase scanning, analysis, and documentation generation.

## Available Agents

### project-scanner

**Purpose:** Comprehensive codebase scanner and documentation generator

**Model:** sonnet

**Skills:** project-documentation

**Use when:**
- First-time codebase documentation
- Generating onboarding materials
- Creating architecture overviews
- Documenting patterns and conventions

**Outputs:**
- README documentation
- Architecture overview
- Code walkthroughs
- API reference
- Setup guides
- Onboarding materials

## Related Command

**Command:** `/project-scan`
**Location:** `.claude/commands/project-scan.md`

## Documentation Methodology

Follows the 6-phase layered documentation approach:

1. **Understand** - Explore codebase before documenting
2. **Structure** - Create high/mid/low level documentation
3. **Essential Docs** - Generate core documents
4. **Functions** - Document with intent (WHY not WHAT)
5. **Onboarding** - Create self-paced learning materials
6. **Maintain** - Keep documentation versioned

## Documentation Priority

1. README with setup (get developers running)
2. Architecture overview (big picture)
3. Entry points (where code starts)
4. Core patterns (recurring approaches)
5. Key functions/modules (purpose & examples)
6. Edge cases & gotchas (avoid pitfalls)
