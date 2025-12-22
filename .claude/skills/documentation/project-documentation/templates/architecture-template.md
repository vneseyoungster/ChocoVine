# Architecture Template

Use this template to document system architecture for scanned projects.

---

```markdown
# Architecture Overview

## System Context

{High-level description of what the system does and its place in the ecosystem}

### System Boundaries

```
┌─────────────────────────────────────────────────────────┐
│                    External Systems                      │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐                 │
│  │ {Ext 1} │  │ {Ext 2} │  │ {Ext 3} │                 │
│  └────┬────┘  └────┬────┘  └────┬────┘                 │
│       │            │            │                       │
│       ▼            ▼            ▼                       │
│  ┌─────────────────────────────────────────────────┐   │
│  │              {System Name}                       │   │
│  │  ┌─────────┐  ┌─────────┐  ┌─────────┐         │   │
│  │  │ {Comp1} │──│ {Comp2} │──│ {Comp3} │         │   │
│  │  └─────────┘  └─────────┘  └─────────┘         │   │
│  └─────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

## Architecture Style

**Style:** {Monolith / Microservices / Serverless / Hybrid}

**Key Characteristics:**
- {Characteristic 1}
- {Characteristic 2}
- {Characteristic 3}

## Component Architecture

### Component Overview

| Component | Responsibility | Technology | Location |
|-----------|---------------|------------|----------|
| {Component 1} | {What it does} | {Tech} | `{path/}` |
| {Component 2} | {What it does} | {Tech} | `{path/}` |
| {Component 3} | {What it does} | {Tech} | `{path/}` |

### Component Details

#### {Component 1}

**Purpose:** {Detailed description}

**Key Files:**
- `{file1.ts}` - {Description}
- `{file2.ts}` - {Description}

**Dependencies:**
- Depends on: {Component 2}
- Depended by: {Component 3}

**Interfaces:**
```typescript
interface {ComponentInterface} {
  {method}({params}): {ReturnType}
}
```

## Data Architecture

### Data Flow

```
{User/Client}
      │
      ▼
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   {Layer1}  │ ──► │   {Layer2}  │ ──► │   {Layer3}  │
│  {Purpose}  │     │  {Purpose}  │     │  {Purpose}  │
└─────────────┘     └─────────────┘     └─────────────┘
      │                   │                   │
      ▼                   ▼                   ▼
┌─────────────────────────────────────────────────────┐
│                    Data Store                        │
│  {Database Type} - {Database Name}                  │
└─────────────────────────────────────────────────────┘
```

### Data Models

**Core Entities:**
- `{Entity1}` - {Description}
- `{Entity2}` - {Description}
- `{Entity3}` - {Description}

See: `{path/to/schema}` for detailed schema

## Integration Points

### External APIs

| API | Purpose | Auth Method | Docs |
|-----|---------|-------------|------|
| {API 1} | {Purpose} | {OAuth/Key} | {link} |
| {API 2} | {Purpose} | {OAuth/Key} | {link} |

### Internal APIs

| Endpoint Pattern | Handler | Purpose |
|-----------------|---------|---------|
| `{/api/v1/*}` | `{handler}` | {Purpose} |

## Security Architecture

### Authentication

- **Method:** {JWT / Session / OAuth}
- **Implementation:** `{path/to/auth}`
- **Token Storage:** {Where tokens stored}

### Authorization

- **Model:** {RBAC / ABAC / Custom}
- **Roles:** {List of roles}
- **Implementation:** `{path/to/authz}`

## Deployment Architecture

### Environments

| Environment | Purpose | URL |
|-------------|---------|-----|
| Development | Local dev | `localhost:{port}` |
| Staging | Pre-prod testing | `{staging-url}` |
| Production | Live | `{prod-url}` |

### Infrastructure

```
┌─────────────────────────────────────────┐
│            {Cloud Provider}              │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐ │
│  │{Service}│  │{Service}│  │{Service}│ │
│  └─────────┘  └─────────┘  └─────────┘ │
└─────────────────────────────────────────┘
```

## Design Decisions

### ADR-001: {Decision Title}

**Status:** {Accepted / Superseded / Deprecated}
**Date:** {Date}

**Context:** {Why decision was needed}

**Decision:** {What was decided}

**Consequences:**
- {Positive consequence}
- {Negative consequence}
- {Trade-off}

## Known Constraints

1. **{Constraint 1}:** {Description and impact}
2. **{Constraint 2}:** {Description and impact}

## Future Considerations

- {Planned improvement 1}
- {Planned improvement 2}
```

---

## Template Usage Notes

- Use ASCII diagrams for portability
- Link to actual code files when referencing
- Keep diagrams simple and focused
- Update when architecture changes
- Include rationale for decisions
