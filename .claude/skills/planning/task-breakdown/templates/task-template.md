# Task Template

Use this template for each task in an implementation plan.

---

## Task [Phase.Number]: [Task Name]

**Priority:** P1 (Critical) | P2 (High) | P3 (Medium) | P4 (Low)
**Size:** XS | S | M | L
**Dependencies:** None | Task [X.Y] (hard/soft)

---

### Description

[Clear description of what needs to be done. Include the "why" if not obvious.]

---

### File Operations

| Action | File Path | Details |
|--------|-----------|---------|
| CREATE | `[full/path/to/new/file]` | [Purpose, pattern to follow] |
| MODIFY | `[full/path/to/file]` | Lines [X-Y], [what changes] |
| DELETE | `[full/path/to/file]` | [Reason, dependency check] |
| MOVE | `[from]` → `[to]` | [Update imports] |

---

### Current State
*(For MODIFY operations - show what exists now)*

```[language]
// File: [path/to/file]
// Lines: [start-end]

[existing code that will be changed]
```

---

### Expected State
*(Show what the code should look like after implementation)*

```[language]
// File: [path/to/file]
// After implementation

[expected code after changes]
```

---

### Implementation Notes

**Pattern Reference:**
- Follow pattern in `[path/to/similar/implementation]`

**Key Considerations:**
- [Important detail 1]
- [Important detail 2]

**Gotchas to Avoid:**
- [Common mistake to avoid]

**Related Files:**
- `[path/to/related/file]` - [why it's relevant]

---

### Verification

```bash
# Type check
[type check command]

# Lint
[lint command]

# Test
[test command]

# Build (if applicable)
[build command]
```

**Manual Verification:**
- [ ] [Manual check if needed]

---

### Commit

```
[type]([scope]): [description]

[body - what was done and why]

[footer - closes issues, breaking changes]
```

---

### Success Criteria

- [ ] [Specific criterion 1]
- [ ] [Specific criterion 2]
- [ ] All verification commands pass
- [ ] Code follows project patterns

---

## Example: Filled Template

### Task 1.1: Create Authentication Service

**Priority:** P1 (Critical)
**Size:** M
**Dependencies:** None

---

### Description

Create a new authentication service that handles JWT token generation and validation. This is the foundation for the auth system and will be used by controllers and middleware.

---

### File Operations

| Action | File Path | Details |
|--------|-----------|---------|
| CREATE | `src/services/auth.service.ts` | New service, follow UserService pattern |
| MODIFY | `src/services/index.ts` | Line 5, add export |

---

### Current State

```typescript
// File: src/services/index.ts
// Lines: 1-6

export { UserService } from './user.service';
export { ProductService } from './product.service';
export { OrderService } from './order.service';
```

---

### Expected State

```typescript
// File: src/services/index.ts
// After implementation

export { UserService } from './user.service';
export { ProductService } from './product.service';
export { OrderService } from './order.service';
export { AuthService } from './auth.service';
```

```typescript
// File: src/services/auth.service.ts
// New file

import { Injectable } from '@nestjs/common';
import { JwtService } from '@nestjs/jwt';
import { User } from '../entities/user.entity';

@Injectable()
export class AuthService {
  constructor(private jwtService: JwtService) {}

  generateToken(user: User): string {
    const payload = { sub: user.id, email: user.email };
    return this.jwtService.sign(payload);
  }

  validateToken(token: string): TokenPayload | null {
    try {
      return this.jwtService.verify(token);
    } catch {
      return null;
    }
  }
}
```

---

### Implementation Notes

**Pattern Reference:**
- Follow pattern in `src/services/user.service.ts`

**Key Considerations:**
- Use environment variables for JWT secret
- Token expiry should be configurable
- Include user ID and email in token payload

**Gotchas to Avoid:**
- Don't store sensitive data in token payload
- Remember to handle token expiration gracefully

**Related Files:**
- `src/config/jwt.config.ts` - JWT configuration
- `src/middleware/auth.middleware.ts` - Will use this service

---

### Verification

```bash
# Type check
npm run typecheck

# Lint
npm run lint -- src/services/auth.service.ts

# Test
npm test -- --testPathPattern=auth.service

# Build
npm run build
```

**Manual Verification:**
- [ ] Service can be imported in other files
- [ ] No circular dependencies

---

### Commit

```
feat(auth): implement JWT authentication service

- Add AuthService with token generation and validation
- Configure JWT with environment-based secret
- Export from services index

Part of authentication system implementation
```

---

### Success Criteria

- [ ] AuthService class is exported
- [ ] generateToken returns valid JWT
- [ ] validateToken correctly verifies tokens
- [ ] All verification commands pass
- [ ] Code follows project patterns
