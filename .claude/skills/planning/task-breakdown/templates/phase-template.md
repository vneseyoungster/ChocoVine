# Phase Template

Use this template for each phase file in `plans/phases/`.

---

# Phase [N]: [Phase Name]

**Dependencies:** None | Phase [X], [Y]
**Can Start:** Immediately | After Phase [X] completes
**Estimated Tasks:** [N]
**Risk Level:** Low | Medium | High

---

## Objective

[One sentence describing what this phase accomplishes independently]

---

## Entry Criteria

Before starting this phase:
- [ ] [Prerequisite 1 - what must exist/be true]
- [ ] [Prerequisite 2 - if any dependencies, they are complete]

---

## Tasks

### Task [N.1]: [Task Name]

**Priority:** P1 | P2 | P3
**Size:** XS | S | M | L
**Dependencies:** None | Task [N.X]

**Description:**
[What needs to be done]

**File Operations:**

| Action | File | Details |
|--------|------|---------|
| CREATE | `path/to/file` | [Purpose, pattern] |
| MODIFY | `path/to/file` | Lines [X-Y], [change] |

**Current State:**
```[language]
// File: path/to/file
// Lines: X-Y
[existing code]
```

**Expected State:**
```[language]
// After implementation
[expected code]
```

**Verification:**
```bash
npm run typecheck
npm run lint
npm test -- [pattern]
```

**Commit:**
```
[type]([scope]): [description]

[body]
```

---

### Task [N.2]: [Task Name]

[Repeat format for each task]

---

## Exit Criteria

This phase is complete when:
- [ ] All [N] tasks completed
- [ ] All verification commands pass
- [ ] No regressions in existing functionality
- [ ] Phase can be merged independently

---

## Phase Verification

```bash
# Run all phase-specific tests
npm test -- --testPathPattern=[phase-pattern]

# Type check affected files
npm run typecheck

# Lint affected files
npm run lint -- [files]

# Build verification (if applicable)
npm run build
```

---

## Rollback Plan

If this phase needs to be reverted:
1. [Specific rollback step]
2. [Files to restore]
3. [Verification after rollback]

---

## Notes

- [Any important considerations]
- [Known limitations]
- [Future improvements deferred]

---

# Example: Filled Phase Template

## Phase 2: Core Models

**Dependencies:** None
**Can Start:** Immediately
**Estimated Tasks:** 3
**Risk Level:** Low

---

## Objective

Create TypeScript models and validation schemas for User, Product, and Order entities.

---

## Entry Criteria

Before starting this phase:
- [ ] TypeScript is configured in project
- [ ] Zod or validation library is installed

---

## Tasks

### Task 2.1: Create User Model

**Priority:** P1
**Size:** S
**Dependencies:** None

**Description:**
Create User entity with validation schema following existing patterns.

**File Operations:**

| Action | File | Details |
|--------|------|---------|
| CREATE | `src/models/user.model.ts` | New model file |
| MODIFY | `src/models/index.ts` | Line 3, add export |

**Current State:**
```typescript
// File: src/models/index.ts
// Lines: 1-2
export { BaseModel } from './base.model';
```

**Expected State:**
```typescript
// After implementation
export { BaseModel } from './base.model';
export { User, UserSchema } from './user.model';
```

**Verification:**
```bash
npm run typecheck
npm test -- user.model
```

**Commit:**
```
feat(models): add User model with validation

- Create User entity with id, email, name
- Add Zod schema for runtime validation
- Export from models index
```

---

### Task 2.2: Create Product Model

**Priority:** P1
**Size:** S
**Dependencies:** None

[Similar format...]

---

### Task 2.3: Create Order Model

**Priority:** P2
**Size:** M
**Dependencies:** Task 2.1, 2.2 (soft - uses User and Product types)

[Similar format...]

---

## Exit Criteria

This phase is complete when:
- [ ] All 3 tasks completed
- [ ] All models export from index
- [ ] Type check passes
- [ ] Unit tests pass
- [ ] Models can be imported by other phases

---

## Phase Verification

```bash
npm test -- --testPathPattern=models
npm run typecheck
npm run lint -- src/models/
```

---

## Rollback Plan

If this phase needs to be reverted:
1. Delete `src/models/user.model.ts`, `product.model.ts`, `order.model.ts`
2. Restore `src/models/index.ts` to original
3. Run `npm run typecheck` to verify no broken imports

---

## Notes

- Models are designed to be independent of database layer
- Validation schemas can be used in both frontend and backend
- Order model has soft dependency on User/Product but works with IDs only
