# Endpoint Documentation Template

Use this template to document each API endpoint.

---

## [METHOD] /path/to/endpoint

Brief description of what this endpoint does.

### Authentication
- Required: Yes/No
- Type: Bearer Token / API Key / None

### Authorization
- Required roles: `admin`, `user`
- Required scopes: `read:users`, `write:users`

### Request

#### URL Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | The user's unique identifier |

#### Query Parameters
| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `page` | integer | No | 1 | Page number for pagination |
| `limit` | integer | No | 20 | Items per page (max: 100) |
| `sort` | string | No | `createdAt:desc` | Sort order |

#### Request Body
```json
{
  "name": "string (required, 1-100 chars)",
  "email": "string (required, valid email)",
  "role": "string (optional, enum: admin|user)"
}
```

#### Example Request
```bash
curl -X POST https://api.example.com/v1/users \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john@example.com",
    "role": "user"
  }'
```

### Response

#### Success Response
**Code:** 201 Created

**Headers:**
```
Location: /v1/users/123
```

**Body:**
```json
{
  "data": {
    "id": "123",
    "name": "John Doe",
    "email": "john@example.com",
    "role": "user",
    "createdAt": "2024-01-15T10:30:00Z",
    "updatedAt": "2024-01-15T10:30:00Z"
  }
}
```

#### Error Responses

**400 Bad Request** - Validation Error
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Request validation failed",
    "details": [
      {
        "field": "email",
        "message": "Invalid email format"
      }
    ]
  }
}
```

**401 Unauthorized** - Missing/Invalid Token
```json
{
  "error": {
    "code": "UNAUTHORIZED",
    "message": "Authentication required"
  }
}
```

**403 Forbidden** - Insufficient Permissions
```json
{
  "error": {
    "code": "FORBIDDEN",
    "message": "You don't have permission to create users"
  }
}
```

**409 Conflict** - Duplicate Resource
```json
{
  "error": {
    "code": "ALREADY_EXISTS",
    "message": "A user with this email already exists"
  }
}
```

### Rate Limiting
- Limit: 100 requests per minute
- Headers: `X-RateLimit-Limit`, `X-RateLimit-Remaining`

### Notes
- Any additional implementation details
- Known limitations
- Related endpoints

### Changelog
| Version | Date | Changes |
|---------|------|---------|
| v2.0 | 2024-01-15 | Added `role` field |
| v1.0 | 2024-01-01 | Initial release |

---

# Example: GET /v1/users/:id

Retrieve a single user by their unique identifier.

### Authentication
- Required: Yes
- Type: Bearer Token

### Authorization
- Required roles: `admin`, `user` (own profile only)

### Request

#### URL Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | The user's unique identifier (UUID) |

#### Example Request
```bash
curl https://api.example.com/v1/users/550e8400-e29b-41d4-a716-446655440000 \
  -H "Authorization: Bearer <token>"
```

### Response

#### Success Response (200 OK)
```json
{
  "data": {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "name": "John Doe",
    "email": "john@example.com",
    "role": "user",
    "avatarUrl": "https://example.com/avatars/john.jpg",
    "createdAt": "2024-01-15T10:30:00Z",
    "updatedAt": "2024-01-15T10:30:00Z"
  }
}
```

#### Error Response (404 Not Found)
```json
{
  "error": {
    "code": "NOT_FOUND",
    "message": "User not found"
  }
}
```
