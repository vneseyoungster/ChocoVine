# Pre-Commit Quality Checklist

Use this checklist before committing any code changes.

## Automated Checks

Run these commands and ensure they pass:

```bash
# Type checking
npm run typecheck

# Linting
npm run lint

# Unit tests
npm test

# Build (catch build-time errors)
npm run build
```

## Code Quality Review

### Naming
- [ ] Variables describe their content (`userCount` not `n`)
- [ ] Functions describe their action (`validateEmail` not `check`)
- [ ] Classes describe the entity (`OrderProcessor` not `Handler`)
- [ ] Boolean variables/functions are questions (`isValid`, `hasPermission`)
- [ ] No single-letter names except in loops (`i`, `j` are acceptable)
- [ ] No abbreviations except common ones (`id`, `url`, `api`)

### Functions
- [ ] Each function does one thing
- [ ] Function is less than 20 lines (ideally)
- [ ] Has 5 or fewer parameters
- [ ] No hidden side effects
- [ ] Return type is explicit
- [ ] Pure functions where possible

### Structure
- [ ] Maximum 3 levels of nesting
- [ ] Early returns for guard clauses
- [ ] No dead code or commented-out code
- [ ] Imports are organized and minimal
- [ ] File length is reasonable (< 300 lines ideal)

### Types (TypeScript)
- [ ] No `any` types (use `unknown` if needed)
- [ ] Interfaces for object shapes
- [ ] Enums or unions for finite sets
- [ ] Generics where appropriate
- [ ] Null/undefined handled explicitly

### Error Handling
- [ ] Errors have meaningful messages
- [ ] Custom error classes for domain errors
- [ ] Errors are logged appropriately
- [ ] Async errors are caught
- [ ] User-facing messages are friendly

### Comments
- [ ] Comments explain "why", not "what"
- [ ] No obvious comments (`// increment counter`)
- [ ] TODO comments have context/ticket numbers
- [ ] JSDoc for public APIs
- [ ] No commented-out code

### Testing
- [ ] New code has tests
- [ ] Tests cover happy path
- [ ] Tests cover error cases
- [ ] Tests are readable and maintainable
- [ ] No flaky tests introduced

### Security
- [ ] No hardcoded secrets or credentials
- [ ] User input is validated
- [ ] SQL queries are parameterized
- [ ] Sensitive data is not logged
- [ ] Dependencies are from trusted sources

### Performance
- [ ] No obvious N+1 queries
- [ ] Large operations are paginated
- [ ] Expensive calculations are memoized
- [ ] No memory leaks (event listeners cleaned up)
- [ ] Assets are optimized

## Final Review

- [ ] Code follows project patterns
- [ ] Changes match the task requirements
- [ ] No scope creep beyond the task
- [ ] Commit message is descriptive
- [ ] Related documentation updated

## Quick Commands

```bash
# Full pre-commit check
npm run typecheck && npm run lint && npm test && npm run build

# Quick check (skip tests)
npm run typecheck && npm run lint

# Fix auto-fixable issues
npm run lint -- --fix
```
