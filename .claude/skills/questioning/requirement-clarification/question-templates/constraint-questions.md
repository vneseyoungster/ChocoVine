# Constraint Question Templates

Templates for clarifying timeline, budget, team, and operational constraints.

## Timeline Constraints

### Deadlines
- "Is there a deadline for this feature?"
- "Is this blocking other work?"
- "Can this be released incrementally or must it be all-at-once?"

### Prioritization
- "What's the priority relative to [other work]?"
- "Can this wait until after [milestone]?"
- "Is a partial solution acceptable initially?"

### Dependencies
- "Is this blocked by any other work?"
- "Does anything depend on this being complete?"
- "Are there external dependencies (APIs, services)?"

## Resource Constraints

### Team
- "Who will maintain this after implementation?"
- "Is there specific expertise required?"
- "Should this be documented for handoff?"

### Infrastructure
- "Should this run on existing infrastructure?"
- "Are there hosting/deployment preferences?"
- "Is there a budget for new services?"

### Technical Debt
- "Is there existing code that should be refactored alongside this?"
- "Are there known issues that affect this area?"
- "Should this address any tech debt?"

## User Constraints

### Target Users
- "Who will be using this feature?"
- "What's the technical level of the users?"
- "Is accessibility (a11y) compliance required?"

### Usage Patterns
- "How often will this feature be used?"
- "Is this a critical path feature?"
- "Are there peak usage times?"

### User Experience
- "Should this match existing UX patterns?"
- "Are there specific design requirements?"
- "Is user documentation needed?"

## Operational Constraints

### Monitoring
- "Should this include monitoring/alerting?"
- "What metrics should be tracked?"
- "Is there a logging standard to follow?"

### Maintenance
- "How should updates be handled?"
- "Is zero-downtime deployment required?"
- "Should this support feature flags?"

### Compliance
- "Are there regulatory requirements?"
- "Is audit logging required?"
- "Are there data retention policies?"

## Compatibility Constraints

### Backward Compatibility
- "Must this maintain backward compatibility?"
- "Can we deprecate [old feature]?"
- "Is data migration acceptable?"

### Forward Compatibility
- "Should the design anticipate [future need]?"
- "Is versioning required?"
- "Should we design for extensibility?"

### Integration Compatibility
- "Must this work with [existing system]?"
- "Are there API contract requirements?"
- "Should this follow existing patterns?"

## Usage Examples

### Example 1: Timeline Constraint
```
Constraint Question: "Is there a deadline for this feature, or can it be
released when ready?"

Impact: Hard deadlines may require scope reduction or increased risk.
Options:
- Flexible (release when ready)
- Soft deadline ([date], can slip if needed)
- Hard deadline ([date], must ship)
Default: Flexible - prioritize quality over speed.
```

### Example 2: User Constraint
```
Constraint Question: "Who will be the primary users of this feature -
internal team, power users, or general public?"

Impact: Determines UX complexity, error handling detail, and documentation needs.
Options:
- Internal team (can be technical, minimal docs)
- Power users (some technical knowledge)
- General public (must be intuitive, full docs)
Default: Assume general public (safest).
```

### Example 3: Compatibility Constraint
```
Constraint Question: "Can we introduce breaking changes to [API/data format],
or must we maintain backward compatibility?"

Impact: Maintaining compatibility adds complexity but avoids disruption.
Options:
- Breaking changes OK (simpler, requires coordination)
- Maintain compatibility (more complex, safer)
- Deprecation period (middle ground)
Default: Maintain compatibility with deprecation warnings.
```

### Example 4: Operational Constraint
```
Constraint Question: "Should this feature be behind a feature flag for
gradual rollout?"

Impact: Feature flags add complexity but reduce risk of widespread issues.
Options:
- No flag (simpler, higher risk)
- Flag for initial release (can disable quickly)
- Permanent flag (full control)
Default: Feature flag for initial release, remove after stable.
```
