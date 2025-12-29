# Research Documentation

Research external documentation for: $ARGUMENTS

## Overview

This command conducts comprehensive research on external documentation, libraries, frameworks, and technical topics. It uses the **docs-seeker skill** to find the latest, most relevant documentation and produces a detailed research report.

**Purpose**: Gather up-to-date information from official documentation, llms.txt sources, GitHub repositories, and community resources to inform implementation decisions.

---

## Prerequisites

Ensure the following tools are available:
- `repomix` (recommended, for repository analysis): `npm install -g repomix`
- Internet access for WebSearch and WebFetch

**Skill Reference**: `.claude/skills/repomix/SKILL.md` - See for detailed repomix usage patterns

---

## Execution Flow

### Phase 1: Parse Research Request

1. **Extract target**
   - Library/framework name
   - Specific version (if mentioned, default: latest)
   - Focus topic or question
   - Related technologies

2. **Identify scope**
   - Single library vs. multiple libraries
   - General overview vs. specific feature
   - Comparison vs. deep dive

### Phase 2: Documentation Discovery

**CRITICAL: Use docs-seeker skill workflow**

Reference: `.claude/skills/docs-seeker/SKILL.md`

#### Step 1: Try context7.com First (Priority)

For GitHub repositories:
```
Pattern: https://context7.com/{org}/{repo}/llms.txt
Examples:
- expo: https://context7.com/expo/expo/llms.txt
- react-native: https://context7.com/facebook/react-native/llms.txt
- next.js: https://context7.com/vercel/next.js/llms.txt
```

For websites:
```
Pattern: https://context7.com/websites/{normalized-domain-path}/llms.txt
```

For topic-specific searches:
```
Pattern: https://context7.com/{path}/llms.txt?topic={query}
Example: https://context7.com/expo/expo/llms.txt?topic=navigation
```

#### Step 2: Fallback to Traditional llms.txt

If context7.com fails:
```
WebSearch: "[library] llms.txt site:[docs domain]"
```

Common patterns:
- `https://docs.[library].com/llms.txt`
- `https://[library].dev/llms.txt`
- `https://[library].io/llms.txt`

#### Step 3: Repository Analysis with Repomix

**Reference**: `.claude/skills/repomix/SKILL.md`

When llms.txt is not available, use repomix to package the repository for AI analysis:

**Option A: Remote Repository (Preferred)**
```bash
# Package remote repository directly (no cloning needed)
npx repomix --remote owner/repo --style markdown -o /tmp/docs-research/library-docs.md

# For specific branch or commit
npx repomix --remote https://github.com/owner/repo/tree/main --style markdown -o /tmp/docs-research/library-docs.md
```

**Option B: Local Clone**
```bash
# Find GitHub repository
WebSearch: "[library] github repository"

# Clone and analyze
git clone --depth 1 [repo-url] /tmp/docs-research
cd /tmp/docs-research

# Package with documentation focus
repomix --include "src/**,docs/**,examples/**,*.md" --remove-comments --style markdown -o library-docs.md
```

**Repomix Options for Documentation Research:**
```bash
# Full documentation context
repomix --include "src/**,docs/**,*.md" --style markdown -o doc-context.md

# API-focused analysis
repomix --include "src/api/**,src/routes/**,src/controllers/**" --remove-comments -o api-context.xml

# Examples and guides only
repomix --include "examples/**,demos/**,docs/**" --style markdown -o examples.md
```

**Extract and analyze:**
```
Read: /tmp/docs-research/library-docs.md
Focus: README.md sections, API documentation, examples, configuration
```

#### Step 4: Research Fallback

When no structured sources exist:
- Launch multiple Researcher agents
- Search: official docs, tutorials, API references, community guides
- Aggregate findings

### Phase 3: Parallel Exploration

**Agent Distribution Guidelines:**

| URL Count | Strategy |
|-----------|----------|
| 1-3 URLs | Single Explorer agent |
| 4-10 URLs | 3-5 Explorer agents |
| 11+ URLs | 5-7 Explorer agents, prioritize |

**Launch Explorer agents simultaneously:**

```markdown
Example for 6 URLs:

Agent 1: Getting started, installation
Agent 2: Core concepts, configuration
Agent 3: API reference, examples
```

### Phase 4: Information Synthesis

1. **Aggregate findings** from all agents
2. **Cross-reference** information for consistency
3. **Verify** against official sources
4. **Organize** by topic and relevance
5. **Identify gaps** and note limitations

### Phase 5: Generate Research Report

Create session directory and report:

```
plans/research/docs/{date}-{topic-slug}/
├── README.md              # Overview and summary
├── sources.md             # All sources consulted
├── findings.md            # Detailed findings
├── comparison.md          # (if multiple libraries compared)
├── recommendations.md     # Implementation recommendations
├── references/            # Downloaded documentation
└── repomix/               # Repository packages (when using repomix)
    ├── {library}-full.md  # Full repository package
    ├── {library}-api.xml  # API-focused package
    └── {library}-docs.md  # Documentation-focused package
```

---

## Output Format

### Main Report (README.md)

```markdown
# Documentation Research: {Topic}

**Research Date:** {date}
**Target:** {library/framework/topic}
**Version:** {version or "latest"}

## Executive Summary
[2-3 sentence overview of key findings]

## Discovery Method
- Primary source: [llms.txt / Repository (via Repomix) / Research]
- URLs consulted: [count]
- Agents deployed: [count]
- Repomix packages: [list if used, e.g., "library-docs.md (12,450 tokens)"]

## Key Findings

### Overview
[What is this library/framework and what problem does it solve]

### Installation & Setup
[How to install and configure]

### Core Concepts
[Fundamental concepts developers need to understand]

### Common Patterns
[Typical usage patterns with examples]

### API Reference Summary
[Key APIs and their purposes]

### Integration Notes
[How it integrates with related technologies]

## Code Examples

### Basic Usage
\`\`\`javascript
// Example code
\`\`\`

### Advanced Pattern
\`\`\`javascript
// Example code
\`\`\`

## Compatibility & Requirements

| Requirement | Version |
|-------------|---------|
| Node.js | >= X.X |
| React | >= X.X |
| ... | ... |

## Known Issues & Limitations
[Documented issues, gotchas, and limitations]

## Recommendations
[Recommendations for implementation based on research]

## Additional Resources
- [Official docs](url)
- [GitHub repository](url)
- [Community examples](url)

## Research Notes
- [Any caveats about information freshness]
- [Gaps in available documentation]
- [Conflicting information encountered]

---
Generated by Research Documentation workflow using docs-seeker skill.
```

---

## Version Handling

**Latest (default):**
- Search without version specifier
- Use current documentation paths
- Note current version in report

**Specific version:**
- Include version in search: `[library] v[version] llms.txt`
- Check versioned paths: `/v[version]/llms.txt`
- For repositories: checkout specific tag/branch
- Clearly indicate version in all findings

---

## Quality Gates

Before completing research:
- [ ] Primary source identified and documented
- [ ] Core documentation retrieved
- [ ] Installation instructions found
- [ ] Basic usage examples included
- [ ] Version requirements documented
- [ ] Known issues noted
- [ ] All sources attributed
- [ ] Freshness verified (latest docs)
- [ ] Repomix packages stored (if used) with token counts noted
- [ ] No sensitive data in repomix output (security check passed)

---

## Error Handling

| Error | Resolution |
|-------|------------|
| llms.txt not found | Try repomix repository analysis → Research fallback |
| Repository not accessible | Check if private → Search alternatives |
| Outdated documentation | Note version → Search for updates |
| Conflicting information | Prioritize official → Note conflicts |
| Rate limited | Wait and retry → Use cached content |
| Repomix output too large | Add `--include` patterns to filter relevant files |
| Repomix timeout | Use `--include` to reduce scope, exclude node_modules |
| Repomix security warning | Review flagged files → Add to `.repomixignore` if false positive |
| Repomix not installed | Run `npm install -g repomix` or use `npx repomix` |

---

## Example Usage

### Basic Library Research
```bash
/research:docs How to use Expo with React Native

# Output: Comprehensive guide on Expo + React Native integration
# - Installation steps
# - Project setup
# - Common patterns
# - Navigation integration
# - Build and deployment
```

### Specific Feature Research
```bash
/research:docs Better Auth authentication library setup with Next.js

# Output: Focused guide on Better Auth + Next.js
# - Configuration
# - Providers setup
# - Session handling
# - Protected routes
```

### Version-Specific Research
```bash
/research:docs React Query v5 migration guide

# Output: Migration-focused documentation
# - Breaking changes from v4
# - New features in v5
# - Migration steps
# - Updated patterns
```

### Comparison Research
```bash
/research:docs Compare Prisma vs Drizzle ORM for PostgreSQL

# Output: Side-by-side comparison
# - Feature comparison
# - Performance considerations
# - Developer experience
# - Recommendations
```

### Repository-Based Research (with Repomix)
```bash
/research:docs Analyze zustand state management library

# Workflow:
# 1. Try context7.com/pmndrs/zustand/llms.txt first
# 2. If unavailable, use repomix:
#    npx repomix --remote pmndrs/zustand --style markdown -o zustand-docs.md
# 3. Analyze packaged repository for:
#    - API surface and exports
#    - Usage patterns from examples/
#    - Integration guides from docs/
#    - TypeScript types and interfaces
```

### Multi-Library Comparison (with Repomix)
```bash
/research:docs Compare TanStack Query vs SWR for data fetching

# Workflow:
# 1. Package both libraries:
#    npx repomix --remote TanStack/query --include "packages/react-query/**,docs/**" -o tanstack-query.md
#    npx repomix --remote vercel/swr --include "src/**,*.md" -o swr.md
# 2. Analyze both outputs for:
#    - API design differences
#    - Feature parity
#    - Bundle size considerations
#    - TypeScript support
```

---

## Constraints

1. **Latest information** - Always prioritize up-to-date documentation
2. **Official sources** - Prefer official docs over community content
3. **Attribution** - Always cite sources
4. **Verification** - Cross-reference claims when possible
5. **Scope awareness** - Stay focused on user's question
6. **Version clarity** - Always note version being documented

---

## Skills Used

### docs-seeker
**Purpose**: Documentation discovery and analysis
**Location**: `.claude/skills/docs-seeker/SKILL.md`
**Workflows**: `.claude/skills/docs-seeker/WORKFLOWS.md`

**Key strategies:**
- llms.txt-first approach via context7.com
- Repository analysis via Repomix
- Parallel exploration with Explorer agents
- Research fallback with Researcher agents

### repomix
**Purpose**: Package repositories into AI-friendly format for analysis
**Location**: `.claude/skills/repomix/SKILL.md`
**References**:
- `.claude/skills/repomix/references/configuration.md` - Configuration options
- `.claude/skills/repomix/references/usage-patterns.md` - Common usage patterns

**Key capabilities:**
- Remote repository packaging without cloning: `npx repomix --remote owner/repo`
- Multiple output formats: XML, Markdown, JSON, Plain text
- Smart filtering with include/exclude patterns
- Comment removal for cleaner output
- Token counting for LLM context management
- Security checks for sensitive data detection

**Common patterns for documentation research:**
```bash
# Quick library evaluation
npx repomix --remote owner/library --style markdown -o library-eval.md

# Documentation-focused packaging
repomix --include "src/**,docs/**,*.md" --style markdown -o doc-context.md

# API reference extraction
repomix --include "src/api/**,src/routes/**" --remove-comments -o api-context.xml

# Compare two libraries
npx repomix --remote owner/lib-a --style xml -o lib-a.xml
npx repomix --remote owner/lib-b --style xml -o lib-b.xml
```

---

## Phase Indicator

- 📚 Research Documentation

---

## Completion

When research is complete:

```
✅ Documentation Research Complete

Session: plans/research/docs/{session}/

Files Generated:
- README.md - Research summary and findings
- sources.md - All consulted sources
- findings.md - Detailed documentation
- recommendations.md - Implementation guidance

Key Findings:
- [Summary point 1]
- [Summary point 2]
- [Summary point 3]

Next: Use these findings for /research:codebase or /start to plan implementation.
```

---

## Related Commands

- `/research:codebase` - Research codebase for implementation
- `/research:ui` - Research UI designs from Figma
- `/execute` - Implement the approved plan
- `/start` - Full workflow from research to validation
