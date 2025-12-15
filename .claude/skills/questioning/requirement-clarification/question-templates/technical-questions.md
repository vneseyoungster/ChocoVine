# Technical Question Templates

Templates for clarifying architecture, performance, security, and technology decisions.

## Architecture Decisions

### Component Design
- "Should this be a new [module/service] or extend [existing one]?"
- "Do you prefer [sync/async] processing for this?"
- "Should this follow [pattern A] or [pattern B]?"

### Data Architecture
- "Should [data] live in [existing database] or a new one?"
- "Is [caching layer] needed for this feature?"
- "Should we use [SQL/NoSQL] for [data type]?"

### Integration Architecture
- "Should this be a REST API, GraphQL, or something else?"
- "Do you need real-time updates (WebSockets) or polling is fine?"
- "Should this be a separate microservice or part of the main app?"

## Performance Requirements

### Response Time
- "How many [users/requests/items] should this handle?"
- "Is real-time response critical, or is [N seconds] acceptable?"
- "What's the acceptable latency for [operation]?"

### Throughput
- "How many concurrent users should this support?"
- "What's the expected peak load?"
- "Should this auto-scale based on demand?"

### Resource Constraints
- "Is there a memory/CPU budget for this feature?"
- "Should this run on [specific infrastructure]?"
- "Are there cost constraints for [cloud resources]?"

## Security Requirements

### Authentication
- "Who should be able to [action]? (roles/permissions)"
- "Should this require authentication or allow anonymous access?"
- "Is multi-factor authentication required?"

### Data Protection
- "Does [data] contain sensitive information requiring encryption?"
- "Are there compliance requirements (GDPR, HIPAA, etc.)?"
- "Should [data] be anonymized in logs?"

### Access Control
- "Should users only see their own [data] or shared [data]?"
- "Are admin-level overrides needed?"
- "Should actions be audited?"

## Technology Preferences

### Libraries/Frameworks
- "Is there a preferred [library/framework] for this?"
- "Should we use [existing dependency] or add [new one]?"
- "Any libraries we should avoid?"

### Platform Support
- "Should this support [browser/platform]?"
- "Is mobile responsiveness required?"
- "What's the minimum supported version of [browser/OS]?"

### Development Standards
- "Should we add types/schemas for this?"
- "Is test coverage required? What percentage?"
- "Should this include API documentation?"

## Error Handling

### User-Facing Errors
- "How detailed should error messages be?"
- "Should errors be logged or shown to users?"
- "Is error recovery/retry needed?"

### System Errors
- "Should failures trigger alerts?"
- "Is automatic recovery required?"
- "How should partial failures be handled?"

## Usage Examples

### Example 1: Data Processing Feature
```
Technical Question: "Do you prefer synchronous processing (user waits for result)
or asynchronous (user gets notified when done)?"

Impact: Async requires queue infrastructure but handles large files better.
Options:
- Sync (simpler, good for small data)
- Async (scales better, more complex)
Default: Sync for files under 10MB, async for larger.
```

### Example 2: API Design
```
Technical Question: "Should the API use pagination for listing [items],
and if so, cursor-based or offset-based?"

Impact: Cursor-based is more efficient for large datasets but more complex.
Options:
- No pagination (if small dataset)
- Offset-based (simpler, potential performance issues)
- Cursor-based (efficient, more complex)
Default: Offset-based with 100 item limit.
```

### Example 3: Caching Strategy
```
Technical Question: "Should [frequently accessed data] be cached?
If so, for how long?"

Impact: Caching improves performance but adds complexity and stale data risk.
Options:
- No caching (always fresh, slower)
- Short TTL (1-5 min, good balance)
- Long TTL (1+ hour, fastest, stale risk)
Default: 5-minute cache TTL.
```
