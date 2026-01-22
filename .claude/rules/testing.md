# Testing Rules

## When to Apply
- After implementing any feature
- After fixing bugs
- Before marking task complete

## Requirements

### Coverage Minimum

- [ ] 80% code coverage minimum
- [ ] 100% coverage for critical paths
- [ ] No untested error handlers

### Test Types

| Type | Scope | When |
|------|-------|------|
| Unit | Single function/component | Always |
| Integration | Module interactions | API endpoints, DB |
| E2E | Full user flows | Critical paths |

### TDD Workflow

```
RED → GREEN → IMPROVE → VERIFY
```

1. **RED**: Write failing test first
2. **GREEN**: Minimum code to pass
3. **IMPROVE**: Refactor while green
4. **VERIFY**: Run full suite

### Test Structure

```typescript
describe('ComponentName', () => {
  describe('methodName', () => {
    it('should [expected behavior] when [condition]', () => {
      // Arrange
      // Act
      // Assert
    });
  });
});
```

## Verification Commands

```bash
# Run all tests
npm test

# With coverage
npm test -- --coverage

# Specific pattern
npm test -- --testNamePattern="UserAuth"
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Flaky tests | Add proper async/await, mock timers |
| Slow tests | Mock external dependencies |
| Coverage gaps | Check branch coverage, edge cases |

## References
- `.claude/agents/validation/test-automator.md`
- `.claude/skills/validation/test-generation/`
- test-driven-development skill
