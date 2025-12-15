# API Versioning Standards

## Versioning Strategies

### 1. URL Path Versioning (Recommended)

```
https://api.example.com/v1/users
https://api.example.com/v2/users
```

**Pros:**
- Simple and explicit
- Easy to understand and implement
- Works with all clients
- Easy to route/cache

**Cons:**
- URLs change between versions
- Breaking change for clients on upgrade

### 2. Header Versioning

```
GET /users
Accept: application/vnd.api.v1+json
```

**Pros:**
- URLs stay clean
- More "pure" REST approach

**Cons:**
- Harder to test/debug
- Not visible in URLs
- Requires header support in clients

### 3. Query Parameter Versioning

```
GET /users?version=1
```

**Pros:**
- Easy to implement
- Visible in URL

**Cons:**
- Can be confused with regular parameters
- Less standard

## Recommended Approach: URL Path Versioning

```typescript
// Express example
app.use('/v1', v1Router);
app.use('/v2', v2Router);

// Route structure
/api/v1/users
/api/v1/orders
/api/v2/users  // New version with breaking changes
```

## When to Version

### Major Version (v1 → v2)
Create a new version when:
- Removing fields from responses
- Changing field types
- Renaming fields
- Changing error formats
- Removing endpoints
- Changing authentication

### Minor Changes (No New Version)
Don't version when:
- Adding new optional fields
- Adding new endpoints
- Adding new optional parameters
- Bug fixes that don't change contracts

## Version Lifecycle

```
v1 (Current)     → Active development and support
v2 (Beta)        → New features, may change
v0 (Deprecated)  → Bug fixes only, sunset planned
```

### Deprecation Process

1. **Announce deprecation** (minimum 6 months notice)
2. **Add deprecation headers**:
   ```
   Deprecation: true
   Sunset: Sat, 01 Jan 2025 00:00:00 GMT
   Link: <https://api.example.com/v2/users>; rel="successor-version"
   ```
3. **Log usage** for migration tracking
4. **Provide migration guide**
5. **Set sunset date** and enforce

## Implementation Example

### Router Structure
```
src/
├── api/
│   ├── v1/
│   │   ├── routes/
│   │   ├── controllers/
│   │   └── index.ts
│   ├── v2/
│   │   ├── routes/
│   │   ├── controllers/
│   │   └── index.ts
│   └── shared/          # Shared services/utilities
```

### Version Router
```typescript
// api/index.ts
import { Router } from 'express';
import v1Router from './v1';
import v2Router from './v2';

const router = Router();

router.use('/v1', v1Router);
router.use('/v2', v2Router);

// Redirect root to current version
router.get('/', (req, res) => {
  res.redirect('/v2');
});

export default router;
```

### Shared Code Between Versions
```typescript
// api/shared/services/user.service.ts
export class UserService {
  async findById(id: string): Promise<User> {
    // Shared business logic
  }
}

// api/v1/controllers/user.controller.ts
export class UserControllerV1 {
  constructor(private userService: UserService) {}

  async getUser(req: Request, res: Response) {
    const user = await this.userService.findById(req.params.id);
    res.json(this.toV1Response(user)); // Version-specific format
  }
}

// api/v2/controllers/user.controller.ts
export class UserControllerV2 {
  constructor(private userService: UserService) {}

  async getUser(req: Request, res: Response) {
    const user = await this.userService.findById(req.params.id);
    res.json(this.toV2Response(user)); // New format
  }
}
```

## Documentation

Each version should have:
- OpenAPI/Swagger spec
- Changelog from previous version
- Migration guide
- Sunset date (if deprecated)

```yaml
# openapi.yaml
openapi: 3.0.0
info:
  title: My API
  version: '2.0'
  description: |
    ## Version 2.0 Changes
    - Added `metadata` field to User response
    - Deprecated `legacy_id` field (removed in v3)
    - New `/users/search` endpoint
```
