# Scope Question Templates

Templates for clarifying feature boundaries, edge cases, and data handling.

## Feature Boundaries

### Basic Scope
- "Should [feature] include [related capability], or is that separate?"
- "Does this need to work for [user type A] and [user type B], or just [one]?"
- "Is [feature] a standalone feature or part of [larger feature]?"

### Feature Depth
- "Do you need a basic version first, or the full feature right away?"
- "Should this include [advanced capability] or just [basic capability]?"
- "Is [optional enhancement] required for the first version?"

## Edge Cases

### Error Conditions
- "What should happen if [error condition]?"
- "How should the system behave when [unusual input]?"
- "Should there be a limit on [quantity/size]? If so, what?"

### Boundary Conditions
- "What's the maximum [quantity] this needs to handle?"
- "What happens when [resource] is exhausted?"
- "Should empty/null [data] be allowed?"

### User Scenarios
- "What if the user [unusual action]?"
- "Should [feature] work offline or require connection?"
- "What happens if [external service] is unavailable?"

## Data Handling

### Storage
- "Should [data] be stored permanently or temporarily?"
- "How long should [data] be retained?"
- "Should [data] be encrypted at rest?"

### Access Control
- "Who should have access to [data]?"
- "Can users see each other's [data]?"
- "Should there be role-based access for [feature]?"

### Migration
- "Should [historical data] be migrated?"
- "What format is the existing data in?"
- "Is backward compatibility required?"

## Integration Scope

### Internal Integration
- "Does this need to connect with [existing feature]?"
- "Should changes here update [related feature]?"
- "Does [feature] need to share data with [other feature]?"

### External Integration
- "Does this need to integrate with [external system]?"
- "Should [data] be exportable to [format]?"
- "Is API access required for [feature]?"

## Future Considerations

### Extensibility
- "Do you anticipate needing [future capability]?"
- "Should the design allow for [potential extension]?"
- "Is multi-[language/currency/region] support needed later?"

### Scale
- "How many [users/items] should this support initially?"
- "Do you expect significant growth in [metric]?"
- "Should we design for [scale] from the start?"

## Usage Examples

### Example 1: User Authentication Feature
```
Scope Question: "Should the login feature include social authentication
(Google, GitHub), or just email/password for now?"

Impact: Social auth requires additional OAuth setup and increases complexity.
Default: Start with email/password only.
```

### Example 2: File Upload Feature
```
Scope Question: "What's the maximum file size users should be able to upload?"

Impact: Affects storage costs, upload timeouts, and server configuration.
Default: 10MB limit.
Options: 5MB, 10MB, 50MB, No limit
```

### Example 3: Search Feature
```
Scope Question: "Should search include fuzzy matching (finding 'color'
when searching 'colour'), or exact matches only?"

Impact: Fuzzy matching requires additional search infrastructure.
Default: Exact matching only.
```
