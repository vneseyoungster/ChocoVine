# Coding Style Rules

## When to Apply
- All code changes (Edit, Write tools)
- Code review validation
- New file creation

## Requirements

### Immutability (CRITICAL)

- [ ] Never mutate function parameters
- [ ] Use spread/Object.assign for object updates
- [ ] Use map/filter/reduce over for-loops with mutation

```typescript
// BAD
function process(items: Item[]) {
  items.push(newItem);  // Mutates input!
  return items;
}

// GOOD
function process(items: Item[]): Item[] {
  return [...items, newItem];
}
```

### File Organization

- [ ] Target: 200-400 lines per file
- [ ] Maximum: 800 lines (refactor if exceeded)
- [ ] One component/class per file
- [ ] Related utilities in same directory

### Error Handling

- [ ] Use typed errors with context
- [ ] Never swallow errors silently
- [ ] Log at appropriate levels

```typescript
// GOOD
throw new ValidationError('Invalid email format', {
  field: 'email',
  value: input
});
```

### Input Validation

- [ ] Validate at system boundaries
- [ ] Use zod for schema validation

```typescript
const userSchema = z.object({
  email: z.string().email(),
  age: z.number().min(0).max(150)
});
```

## Code Quality Checklist

Before committing:
- [ ] No console.log statements
- [ ] No commented-out code
- [ ] No magic numbers (use constants)
- [ ] Types explicit, no `any`
- [ ] Functions < 50 lines
- [ ] Descriptive variable names

## References
- `.claude/skills/implementation/clean-code/`
- `.claude/skills/implementation/error-handling/`
