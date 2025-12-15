# API Error Response Standards

## Standard Error Format

All API errors should follow this structure:

```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Human-readable message",
    "details": [],
    "requestId": "req_abc123"
  }
}
```

## Error Codes

Use uppercase snake_case for error codes:

### Authentication Errors (401)
| Code | Description |
|------|-------------|
| `UNAUTHORIZED` | No authentication provided |
| `INVALID_TOKEN` | Token is malformed or expired |
| `TOKEN_EXPIRED` | Token has expired |

### Authorization Errors (403)
| Code | Description |
|------|-------------|
| `FORBIDDEN` | User lacks permission |
| `INSUFFICIENT_SCOPE` | Token lacks required scope |
| `ACCOUNT_SUSPENDED` | Account is suspended |

### Validation Errors (400)
| Code | Description |
|------|-------------|
| `VALIDATION_ERROR` | Input validation failed |
| `INVALID_FORMAT` | Data format is incorrect |
| `MISSING_FIELD` | Required field is missing |

### Resource Errors (404, 409, 422)
| Code | Description |
|------|-------------|
| `NOT_FOUND` | Resource doesn't exist |
| `ALREADY_EXISTS` | Resource already exists |
| `CONFLICT` | Resource state conflict |
| `BUSINESS_RULE_VIOLATION` | Business rule prevents action |

### Server Errors (500, 503)
| Code | Description |
|------|-------------|
| `INTERNAL_ERROR` | Unexpected server error |
| `SERVICE_UNAVAILABLE` | Service temporarily down |
| `RATE_LIMITED` | Too many requests |

## Validation Error Details

For validation errors, include field-level details:

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Validation failed",
    "details": [
      {
        "field": "email",
        "code": "INVALID_FORMAT",
        "message": "Invalid email format"
      },
      {
        "field": "password",
        "code": "TOO_SHORT",
        "message": "Password must be at least 8 characters"
      }
    ]
  }
}
```

## Error Response Examples

### 400 Bad Request
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
    ],
    "requestId": "req_abc123"
  }
}
```

### 401 Unauthorized
```json
{
  "error": {
    "code": "INVALID_TOKEN",
    "message": "The provided token is invalid or expired",
    "requestId": "req_abc123"
  }
}
```

### 403 Forbidden
```json
{
  "error": {
    "code": "FORBIDDEN",
    "message": "You don't have permission to access this resource",
    "requestId": "req_abc123"
  }
}
```

### 404 Not Found
```json
{
  "error": {
    "code": "NOT_FOUND",
    "message": "User not found",
    "requestId": "req_abc123"
  }
}
```

### 422 Unprocessable Entity
```json
{
  "error": {
    "code": "BUSINESS_RULE_VIOLATION",
    "message": "Cannot delete user with active orders",
    "details": [
      {
        "rule": "active_orders_check",
        "message": "User has 3 active orders"
      }
    ],
    "requestId": "req_abc123"
  }
}
```

### 500 Internal Server Error
```json
{
  "error": {
    "code": "INTERNAL_ERROR",
    "message": "An unexpected error occurred",
    "requestId": "req_abc123"
  }
}
```

## Implementation

### TypeScript Error Classes
```typescript
export class ApiError extends Error {
  constructor(
    public code: string,
    message: string,
    public statusCode: number,
    public details?: unknown[]
  ) {
    super(message);
  }

  toJSON() {
    return {
      error: {
        code: this.code,
        message: this.message,
        details: this.details
      }
    };
  }
}
```

### Error Handler Middleware
```typescript
function errorHandler(err: Error, req: Request, res: Response, next: NextFunction) {
  const requestId = req.headers['x-request-id'] || generateId();

  if (err instanceof ApiError) {
    return res.status(err.statusCode).json({
      error: {
        code: err.code,
        message: err.message,
        details: err.details,
        requestId
      }
    });
  }

  // Log unexpected errors
  logger.error({ err, requestId }, 'Unexpected error');

  return res.status(500).json({
    error: {
      code: 'INTERNAL_ERROR',
      message: 'An unexpected error occurred',
      requestId
    }
  });
}
```

## Best Practices

1. **Always include requestId** for debugging
2. **Use appropriate status codes** (don't use 200 for errors)
3. **Keep messages user-friendly** (no stack traces)
4. **Include field-level details** for validation errors
5. **Log server errors** with full context
6. **Document all error codes** in API documentation
