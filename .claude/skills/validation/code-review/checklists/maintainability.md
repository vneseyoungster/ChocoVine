# Maintainability Review Checklist

## Code Readability

### Naming
- [ ] Variables describe their content
- [ ] Functions describe their action
- [ ] Classes describe their entity/responsibility
- [ ] No single-letter names (except loops/lambdas)
- [ ] Consistent naming conventions (camelCase, PascalCase, etc.)
- [ ] Abbreviations avoided or widely understood

### Structure
- [ ] Functions are focused (single responsibility)
- [ ] Functions are < 20 lines (ideal), < 50 lines (acceptable)
- [ ] Nesting depth <= 3 levels
- [ ] Early returns used to reduce nesting
- [ ] Guard clauses at function start

### Formatting
- [ ] Consistent indentation
- [ ] Appropriate whitespace
- [ ] Line length reasonable (< 100-120 chars)
- [ ] Logical grouping of related code

## Code Organization

### File Structure
- [ ] One concern per file
- [ ] Logical directory organization
- [ ] Related files co-located
- [ ] Index files for clean imports

### Module Design
- [ ] Clear module boundaries
- [ ] Minimal public API surface
- [ ] Dependencies flow in one direction
- [ ] Circular dependencies avoided

### Separation of Concerns
- [ ] Business logic separated from I/O
- [ ] UI separated from data fetching
- [ ] Configuration externalized
- [ ] Cross-cutting concerns isolated

## Type Safety

### TypeScript/Type Annotations
- [ ] All function parameters typed
- [ ] Return types specified
- [ ] No `any` types (or justified)
- [ ] Interfaces for complex objects
- [ ] Generics used appropriately

### Null Safety
- [ ] Optional chaining used
- [ ] Nullish coalescing used
- [ ] Null checks before access
- [ ] Default values provided

## Error Handling

### Exception Handling
- [ ] Errors caught at appropriate level
- [ ] Specific error types used
- [ ] Error messages are helpful
- [ ] Original error preserved (cause)

### Recovery & Fallbacks
- [ ] Graceful degradation implemented
- [ ] Retry logic where appropriate
- [ ] Fallback values for non-critical failures
- [ ] User-friendly error messages

## Documentation

### Code Comments
- [ ] Complex logic explained (why, not what)
- [ ] Public APIs have JSDoc/docstrings
- [ ] TODO/FIXME items tracked
- [ ] No commented-out code

### External Documentation
- [ ] README up to date
- [ ] API documentation exists
- [ ] Architecture decisions documented
- [ ] Setup instructions accurate

## Testing

### Test Coverage
- [ ] Critical paths tested
- [ ] Edge cases covered
- [ ] Error scenarios tested
- [ ] Integration points tested

### Test Quality
- [ ] Tests are readable
- [ ] Tests are maintainable
- [ ] Tests are deterministic
- [ ] Test names describe behavior

## SOLID Principles

### Single Responsibility
- [ ] Classes have one reason to change
- [ ] Functions do one thing
- [ ] Modules have clear purpose

### Open/Closed
- [ ] Extensible without modification
- [ ] Plugin/strategy patterns used
- [ ] Behavior customizable via config

### Liskov Substitution
- [ ] Subtypes are substitutable
- [ ] Contracts preserved in inheritance
- [ ] No surprises in overrides

### Interface Segregation
- [ ] Interfaces are focused
- [ ] No unused interface methods
- [ ] Role interfaces preferred

### Dependency Inversion
- [ ] Depend on abstractions
- [ ] High-level modules don't depend on low-level
- [ ] Dependency injection used

## Code Smells to Flag

### Complexity
```
Issue: Long Method
Sign: Function > 50 lines
Action: Extract smaller functions

Issue: Large Class
Sign: Class with > 10 methods or 500 lines
Action: Split responsibilities

Issue: Deep Nesting
Sign: > 3 levels of indentation
Action: Use early returns, extract functions
```

### Duplication
```
Issue: Copy-Paste Code
Sign: Similar code blocks in multiple places
Action: Extract shared function/component

Issue: Parallel Inheritance
Sign: Similar class hierarchies
Action: Use composition or shared base
```

### Coupling
```
Issue: Feature Envy
Sign: Method uses more from another class than its own
Action: Move method to appropriate class

Issue: Shotgun Surgery
Sign: One change requires many file edits
Action: Consolidate related logic
```

## Refactoring Triggers

### When to Refactor
- Same code copied 3+ times
- Function exceeds size limits
- Class takes too many dependencies
- Tests are hard to write
- Bug found in duplicated code

### When Not to Refactor
- Code is working and stable
- No tests to verify behavior
- Deadline pressure (note for later)
- Optimization without measurement
