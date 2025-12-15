# API Documentation

## Overview

Brief description of the API and its purpose.

**Base URL:** `https://api.example.com/v1`

**Authentication:** Bearer token in Authorization header

## Authentication

All API requests require authentication using a Bearer token.

```bash
curl -H "Authorization: Bearer YOUR_API_KEY" \
  https://api.example.com/v1/resource
```

### Getting an API Key

1. Log in to the dashboard
2. Navigate to Settings > API Keys
3. Click "Generate New Key"
4. Copy and securely store your key

## Rate Limiting

- **Rate limit:** 1000 requests per minute
- **Headers:**
  - `X-RateLimit-Limit`: Request limit
  - `X-RateLimit-Remaining`: Remaining requests
  - `X-RateLimit-Reset`: Reset timestamp

## Common Response Formats

### Success Response

```json
{
  "success": true,
  "data": {
    // Response data
  }
}
```

### Error Response

```json
{
  "success": false,
  "error": {
    "code": "ERROR_CODE",
    "message": "Human-readable error message",
    "details": {
      // Additional error context
    }
  }
}
```

### Pagination

```json
{
  "success": true,
  "data": [...],
  "pagination": {
    "page": 1,
    "perPage": 20,
    "total": 100,
    "totalPages": 5
  }
}
```

---

## Endpoints

### Resource Name

#### List Resources

```
GET /resources
```

Retrieve a paginated list of resources.

**Query Parameters:**

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `page` | integer | Page number | 1 |
| `perPage` | integer | Items per page (max 100) | 20 |
| `sort` | string | Sort field | `createdAt` |
| `order` | string | Sort order (`asc`, `desc`) | `desc` |
| `filter` | string | Filter by status | - |

**Response:**

```json
{
  "success": true,
  "data": [
    {
      "id": "res_123",
      "name": "Resource Name",
      "status": "active",
      "createdAt": "2024-01-15T10:30:00Z",
      "updatedAt": "2024-01-15T10:30:00Z"
    }
  ],
  "pagination": {
    "page": 1,
    "perPage": 20,
    "total": 50,
    "totalPages": 3
  }
}
```

**Example:**

```bash
curl -X GET "https://api.example.com/v1/resources?page=1&perPage=10" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

---

#### Get Resource

```
GET /resources/:id
```

Retrieve a single resource by ID.

**Path Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `id` | string | Resource ID |

**Response:**

```json
{
  "success": true,
  "data": {
    "id": "res_123",
    "name": "Resource Name",
    "description": "Detailed description",
    "status": "active",
    "metadata": {
      "key": "value"
    },
    "createdAt": "2024-01-15T10:30:00Z",
    "updatedAt": "2024-01-15T10:30:00Z"
  }
}
```

**Errors:**

| Code | Description |
|------|-------------|
| 404 | Resource not found |

**Example:**

```bash
curl -X GET "https://api.example.com/v1/resources/res_123" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

---

#### Create Resource

```
POST /resources
```

Create a new resource.

**Request Body:**

| Field | Type | Description | Required |
|-------|------|-------------|----------|
| `name` | string | Resource name (1-100 chars) | Yes |
| `description` | string | Resource description | No |
| `metadata` | object | Custom metadata | No |

**Request:**

```json
{
  "name": "New Resource",
  "description": "Description of the resource",
  "metadata": {
    "key": "value"
  }
}
```

**Response:** `201 Created`

```json
{
  "success": true,
  "data": {
    "id": "res_456",
    "name": "New Resource",
    "description": "Description of the resource",
    "status": "active",
    "metadata": {
      "key": "value"
    },
    "createdAt": "2024-01-15T12:00:00Z",
    "updatedAt": "2024-01-15T12:00:00Z"
  }
}
```

**Errors:**

| Code | Description |
|------|-------------|
| 400 | Validation error |
| 409 | Resource already exists |

**Example:**

```bash
curl -X POST "https://api.example.com/v1/resources" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"name": "New Resource"}'
```

---

#### Update Resource

```
PATCH /resources/:id
```

Update an existing resource (partial update).

**Path Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `id` | string | Resource ID |

**Request Body:**

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Resource name |
| `description` | string | Resource description |
| `status` | string | Status (`active`, `inactive`) |
| `metadata` | object | Custom metadata |

**Response:** `200 OK`

```json
{
  "success": true,
  "data": {
    "id": "res_123",
    "name": "Updated Name",
    // ... updated fields
  }
}
```

**Errors:**

| Code | Description |
|------|-------------|
| 400 | Validation error |
| 404 | Resource not found |

---

#### Delete Resource

```
DELETE /resources/:id
```

Delete a resource.

**Path Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `id` | string | Resource ID |

**Response:** `204 No Content`

**Errors:**

| Code | Description |
|------|-------------|
| 404 | Resource not found |
| 409 | Resource cannot be deleted (has dependencies) |

---

## Error Codes

| Code | HTTP Status | Description |
|------|-------------|-------------|
| `VALIDATION_ERROR` | 400 | Invalid request data |
| `UNAUTHORIZED` | 401 | Invalid or missing API key |
| `FORBIDDEN` | 403 | Insufficient permissions |
| `NOT_FOUND` | 404 | Resource not found |
| `CONFLICT` | 409 | Resource conflict |
| `RATE_LIMITED` | 429 | Too many requests |
| `INTERNAL_ERROR` | 500 | Server error |

## Webhooks

### Event Types

| Event | Description |
|-------|-------------|
| `resource.created` | Resource was created |
| `resource.updated` | Resource was updated |
| `resource.deleted` | Resource was deleted |

### Webhook Payload

```json
{
  "id": "evt_789",
  "type": "resource.created",
  "timestamp": "2024-01-15T12:00:00Z",
  "data": {
    "id": "res_123",
    "name": "Resource Name"
  }
}
```

### Verifying Webhooks

Verify the `X-Webhook-Signature` header using HMAC-SHA256.

```typescript
import crypto from 'crypto';

function verifyWebhook(payload: string, signature: string, secret: string): boolean {
  const expected = crypto
    .createHmac('sha256', secret)
    .update(payload)
    .digest('hex');

  return crypto.timingSafeEqual(
    Buffer.from(signature),
    Buffer.from(expected)
  );
}
```

## SDKs

- [JavaScript/TypeScript](https://github.com/example/sdk-js)
- [Python](https://github.com/example/sdk-python)
- [Go](https://github.com/example/sdk-go)

## Changelog

See [API Changelog](./changelog.md) for version history.
