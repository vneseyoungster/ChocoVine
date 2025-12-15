# Architecture: [Feature/System Name]

**Session:** {session-id}
**Created:** {date}
**Author:** Claude Code (solution-architect)
**Status:** Proposed | Approved | Implemented

---

## Overview

[High-level description of the solution. What problem does it solve? What is the approach?]

---

## Design Decisions

### Decision 1: [Decision Topic]

**Context:**
[Why is this decision needed?]

**Options Considered:**

1. **[Option A]**: [Brief description]
   - **Pros:**
     - [Advantage 1]
     - [Advantage 2]
   - **Cons:**
     - [Disadvantage 1]
     - [Disadvantage 2]

2. **[Option B]**: [Brief description]
   - **Pros:**
     - [Advantage 1]
     - [Advantage 2]
   - **Cons:**
     - [Disadvantage 1]
     - [Disadvantage 2]

**Selected:** [Option Name]

**Rationale:**
[Why this option was chosen over others]

**Trade-offs Accepted:**
[What we're giving up by this choice]

---

### Decision 2: [Decision Topic]

[Repeat format for each major decision]

---

## Component Design

### [Component Name]

| Attribute | Value |
|-----------|-------|
| **Responsibility** | [What this component does] |
| **Location** | `[file/directory path]` |
| **Dependencies** | [What it needs] |

**Public Interface:**
```[language]
// Key exports/APIs
[interface or function signatures]
```

**Internal Structure:**
- [Key internal elements]
- [Data structures]

---

### [Component Name]

[Repeat for each component]

---

## Data Flow

```
[ASCII diagram showing data flow between components]

Example:
User Request
     │
     ▼
┌─────────────┐
│   Router    │
└─────────────┘
     │
     ▼
┌─────────────┐     ┌─────────────┐
│ Controller  │────▶│   Service   │
└─────────────┘     └─────────────┘
                          │
                          ▼
                    ┌─────────────┐
                    │  Database   │
                    └─────────────┘
```

---

## Integration Points

| System | Direction | Protocol | Data Format | Notes |
|--------|-----------|----------|-------------|-------|
| [External System] | Inbound/Outbound | REST/GraphQL/gRPC | JSON/XML | [Additional notes] |

---

## Risk Assessment

| # | Risk | Probability | Impact | Risk Level | Mitigation |
|---|------|-------------|--------|------------|------------|
| 1 | [Risk description] | High/Medium/Low | High/Medium/Low | Critical/High/Medium/Low | [Mitigation strategy] |
| 2 | [Risk description] | High/Medium/Low | High/Medium/Low | Critical/High/Medium/Low | [Mitigation strategy] |

---

## Security Considerations

- [ ] Authentication requirements addressed
- [ ] Authorization model defined
- [ ] Data encryption needs identified
- [ ] Input validation planned
- [ ] Audit logging considered

**Security Notes:**
[Any specific security considerations for this architecture]

---

## Performance Requirements

| Metric | Requirement | Notes |
|--------|-------------|-------|
| Response Time | [e.g., < 200ms] | [Context] |
| Throughput | [e.g., 1000 req/s] | [Context] |
| Availability | [e.g., 99.9%] | [Context] |

---

## Open Questions

- [ ] [Question requiring team/user input]
- [ ] [Question requiring team/user input]

---

## Dependencies

### External Dependencies
- [Library/Service]: [Version] - [Purpose]

### Internal Dependencies
- [Module/Component]: [Purpose]

---

## Next Steps

1. [ ] Review and approve architecture
2. [ ] Create detailed implementation plan
3. [ ] [Additional steps]

---

## Appendix

### Related Documents
- Requirements: `docs/specs/requirements-{session}.md`
- Research: `docs/research/[relevant files]`

### Glossary
| Term | Definition |
|------|------------|
| [Term] | [Definition] |
