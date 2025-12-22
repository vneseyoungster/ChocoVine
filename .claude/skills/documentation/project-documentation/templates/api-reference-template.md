# API Reference Template

Use this template to document APIs, functions, and modules.

---

```markdown
# API Reference: {Module/Service Name}

## Overview

{Brief description of what this API/module does}

**Base URL:** `{base-url}` (for HTTP APIs)
**Import:** `{import statement}` (for modules)

## Authentication

{Skip for internal modules}

**Method:** {Bearer Token / API Key / OAuth}

**Header:** `Authorization: Bearer {token}`

**Example:**
```bash
curl -H "Authorization: Bearer YOUR_TOKEN" {base-url}/endpoint
```

## Endpoints / Functions

### {Endpoint/Function Name}

{Brief description}

**HTTP APIs:**
```
{METHOD} {/path/:param}
```

**Functions:**
```{language}
function {name}({params}): {ReturnType}
```

#### Parameters

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `{param1}` | `{type}` | Yes | - | {Description} |
| `{param2}` | `{type}` | No | `{default}` | {Description} |

#### Request Body (HTTP)

```json
{
  "{field1}": "{type} - {description}",
  "{field2}": "{type} - {description}"
}
```

#### Response / Return Value

**Success (200/return):**
```json
{
  "{field1}": "{example}",
  "{field2}": "{example}"
}
```

**TypeScript Type:**
```typescript
interface {ResponseType} {
  {field1}: {type}
  {field2}: {type}
}
```

#### Errors

| Code/Error | Condition | Response/Message |
|------------|-----------|------------------|
| `400` / `ValidationError` | {When} | `{message}` |
| `404` / `NotFoundError` | {When} | `{message}` |
| `500` / `InternalError` | {When} | `{message}` |

#### Example

**Request/Call:**
```{language}
// Example usage
{code example}
```

**Response/Result:**
```json
{example response}
```

---

### {Next Endpoint/Function}

{Repeat structure above}

---

## Types

### {TypeName}

```typescript
interface {TypeName} {
  /**
   * {Field description}
   */
  {field1}: {type}

  /**
   * {Field description}
   * @default {defaultValue}
   */
  {field2}?: {type}
}
```

**Usage:**
```typescript
const example: {TypeName} = {
  {field1}: {value},
  {field2}: {value}
}
```

---

## Constants

| Constant | Value | Description |
|----------|-------|-------------|
| `{CONST_1}` | `{value}` | {Description} |
| `{CONST_2}` | `{value}` | {Description} |

## Error Codes

| Code | Name | Description | Resolution |
|------|------|-------------|------------|
| `{E001}` | `{ErrorName}` | {When thrown} | {How to fix} |
| `{E002}` | `{ErrorName}` | {When thrown} | {How to fix} |

## Rate Limits

{For HTTP APIs}

| Tier | Requests/Min | Requests/Day |
|------|--------------|--------------|
| Free | {limit} | {limit} |
| Pro | {limit} | {limit} |

## Pagination

{For list endpoints}

**Query Parameters:**
- `page`: Page number (default: 1)
- `limit`: Items per page (default: 20, max: 100)

**Response Headers:**
- `X-Total-Count`: Total items
- `X-Page-Count`: Total pages

**Example:**
```
GET /items?page=2&limit=50
```

## Versioning

**Current Version:** {v1}
**Deprecation Policy:** {policy}

| Version | Status | End of Life |
|---------|--------|-------------|
| v2 | Current | - |
| v1 | Deprecated | {date} |

## SDK Examples

### {Language 1}

```{language}
{SDK usage example}
```

### {Language 2}

```{language}
{SDK usage example}
```

## Webhooks

{If applicable}

### {Event Name}

**Trigger:** {When this webhook fires}

**Payload:**
```json
{
  "event": "{event_name}",
  "data": {
    "{field}": "{value}"
  }
}
```

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| {1.1.0} | {Date} | {Change description} |
| {1.0.0} | {Date} | Initial release |
```

---

## Template Usage Notes

- Include runnable examples
- Document all error cases
- Use consistent type notation
- Include both request and response examples
- Document optional parameters and defaults
- Keep examples realistic and tested
