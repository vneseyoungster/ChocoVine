# Task Template

Use this template for tasks within phase files.

---

## Task [Phase.Number]: [Task Name]

**Priority:** P1 | P2 | P3
**Size:** XS | S | M | L
**Dependencies:** None | Task [X.Y]

---

### Description

[What needs to be done - include "why" if not obvious]

---

### File Operations

| Action | File | Details |
|--------|------|---------|
| CREATE | `path/to/file` | [Purpose, pattern to follow] |
| MODIFY | `path/to/file` | Lines [X-Y], [change description] |
| DELETE | `path/to/file` | [Reason, dependency check] |
| MOVE | `from` → `to` | [Import updates needed] |

---

### Current State
*(For MODIFY - show existing code)*

```[language]
// File: path/to/file
// Lines: X-Y
[existing code]
```

---

### Expected State

```[language]
// After implementation
[expected code]
```

---

### Implementation Notes

**Pattern:** Follow `path/to/similar/file`
**Key points:**
- [Important detail]
- [Gotcha to avoid]

---

### Verification

```bash
npm run typecheck
npm run lint
npm test -- [pattern]
```

---

### Commit

```
[type]([scope]): [description]

[body]
```

---

### Success Criteria

- [ ] [Specific criterion]
- [ ] Verification passes
- [ ] Follows project patterns

---

## Size Guidelines

| Size | Scope | Example |
|------|-------|---------|
| **XS** | Single line | Typo, constant |
| **S** | Single function | Add one function |
| **M** | Single file | Multiple functions |
| **L** | 2-4 files | Feature spanning files |
| **XL** | Split required | Too large |

**Rule:** No XL tasks. Split them.

---

## Quick Example

### Task 1.2: Add Auth Middleware

**Priority:** P1
**Size:** S
**Dependencies:** Task 1.1

---

### Description

Create authentication middleware that validates JWT tokens on protected routes.

---

### File Operations

| Action | File | Details |
|--------|------|---------|
| CREATE | `src/middleware/auth.ts` | New middleware |
| MODIFY | `src/middleware/index.ts` | Line 5, add export |

---

### Current State

```typescript
// File: src/middleware/index.ts
// Lines: 1-4
export { errorHandler } from './error';
export { logger } from './logger';
```

---

### Expected State

```typescript
// After implementation
export { errorHandler } from './error';
export { logger } from './logger';
export { authMiddleware } from './auth';
```

---

### Implementation Notes

**Pattern:** Follow `src/middleware/logger.ts`
**Key points:**
- Use AuthService from Task 1.1
- Return 401 for invalid tokens
- Pass user to request context

---

### Verification

```bash
npm run typecheck
npm test -- auth.middleware
```

---

### Commit

```
feat(auth): add JWT authentication middleware

- Validate tokens on protected routes
- Attach user to request context
- Return 401 for invalid/missing tokens
```

---

### Success Criteria

- [ ] Middleware validates tokens
- [ ] Invalid tokens return 401
- [ ] Valid tokens pass user to route
- [ ] Tests pass
