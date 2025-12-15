# REST API Conventions

## Resource Naming

### Use Nouns, Not Verbs
```
Good: GET /users
Bad:  GET /getUsers

Good: POST /orders
Bad:  POST /createOrder
```

### Use Plural Nouns
```
Good: /users, /products, /orders
Bad:  /user, /product, /order
```

### Use Kebab-Case for Multi-Word Resources
```
Good: /order-items, /user-profiles
Bad:  /orderItems, /user_profiles
```

## URL Structure

### Collection and Item Pattern
```
/resources          # Collection
/resources/:id      # Single item
```

### Nested Resources (Use Sparingly)
```
/users/:id/orders           # Orders for a user
/users/:id/orders/:orderId  # Specific order for a user
```

Limit nesting to 2 levels. For deeper relationships, use query parameters:
```
# Instead of: /users/:id/orders/:orderId/items/:itemId
# Use: /order-items?orderId=123
```

### Query Parameters
```
# Filtering
GET /users?status=active&role=admin

# Sorting
GET /users?sort=createdAt:desc

# Pagination
GET /users?page=2&limit=20

# Field selection
GET /users?fields=id,name,email
```

## HTTP Methods in Detail

### GET - Retrieve
```typescript
// List
GET /users
Response: 200 OK
{
  "data": [...],
  "pagination": { "page": 1, "total": 100 }
}

// Single item
GET /users/123
Response: 200 OK
{
  "data": { "id": "123", "name": "John" }
}

// Not found
GET /users/999
Response: 404 Not Found
```

### POST - Create
```typescript
POST /users
Body: { "name": "John", "email": "john@example.com" }

Response: 201 Created
Location: /users/123
{
  "data": { "id": "123", "name": "John", ... }
}
```

### PUT - Replace
```typescript
PUT /users/123
Body: { "name": "John Updated", "email": "john@example.com" }

Response: 200 OK
{
  "data": { "id": "123", "name": "John Updated", ... }
}
```

### PATCH - Partial Update
```typescript
PATCH /users/123
Body: { "name": "John Updated" }

Response: 200 OK
{
  "data": { "id": "123", "name": "John Updated", ... }
}
```

### DELETE - Remove
```typescript
DELETE /users/123

Response: 204 No Content
// No body
```

## Headers

### Request Headers
```
Content-Type: application/json
Accept: application/json
Authorization: Bearer <token>
```

### Response Headers
```
Content-Type: application/json
X-Request-Id: <uuid>
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 99
```

## Idempotency

Idempotent methods can be called multiple times with the same result:
- GET: Yes (always safe)
- PUT: Yes (same input = same state)
- DELETE: Yes (deleting twice = still deleted)
- POST: No (creates new resource each time)
- PATCH: Depends on implementation

For non-idempotent operations, consider:
```
POST /payments
Idempotency-Key: <client-generated-uuid>
```

## Caching

Use appropriate cache headers:
```
# Can be cached
Cache-Control: public, max-age=3600

# Cannot be cached
Cache-Control: no-store

# Must revalidate
Cache-Control: no-cache
ETag: "abc123"
```
