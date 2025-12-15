# Error Handling Patterns

## Common Approaches

### 1. Custom Error Classes

```typescript
// TypeScript/JavaScript
class AppError extends Error {
  constructor(
    public code: string,
    message: string,
    public statusCode: number = 500,
    public details?: unknown
  ) {
    super(message);
    this.name = 'AppError';
  }
}

class ValidationError extends AppError {
  constructor(message: string, details?: unknown) {
    super('VALIDATION_ERROR', message, 400, details);
  }
}

class NotFoundError extends AppError {
  constructor(resource: string) {
    super('NOT_FOUND', `${resource} not found`, 404);
  }
}

class UnauthorizedError extends AppError {
  constructor(message = 'Unauthorized') {
    super('UNAUTHORIZED', message, 401);
  }
}
```

### 2. Result Pattern (No Exceptions)

```typescript
// TypeScript
type Result<T, E = Error> =
  | { success: true; data: T }
  | { success: false; error: E };

function parseUser(data: unknown): Result<User, ValidationError> {
  if (!isValidUser(data)) {
    return { success: false, error: new ValidationError('Invalid user data') };
  }
  return { success: true, data: data as User };
}

// Usage
const result = parseUser(input);
if (result.success) {
  console.log(result.data);
} else {
  console.error(result.error);
}
```

### 3. Try-Catch Wrapper

```typescript
// Async function wrapper
async function tryCatch<T>(
  fn: () => Promise<T>
): Promise<[T, null] | [null, Error]> {
  try {
    const result = await fn();
    return [result, null];
  } catch (error) {
    return [null, error as Error];
  }
}

// Usage
const [user, error] = await tryCatch(() => getUserById(id));
if (error) {
  // Handle error
}
```

## Middleware Pattern (Express/Fastify)

```typescript
// Error handling middleware
function errorHandler(
  err: Error,
  req: Request,
  res: Response,
  next: NextFunction
) {
  logger.error(err);

  if (err instanceof AppError) {
    return res.status(err.statusCode).json({
      error: {
        code: err.code,
        message: err.message,
        details: err.details
      }
    });
  }

  return res.status(500).json({
    error: {
      code: 'INTERNAL_ERROR',
      message: 'An unexpected error occurred'
    }
  });
}
```

## Frontend Error Boundaries (React)

```tsx
class ErrorBoundary extends React.Component {
  state = { hasError: false, error: null };

  static getDerivedStateFromError(error: Error) {
    return { hasError: true, error };
  }

  componentDidCatch(error: Error, errorInfo: React.ErrorInfo) {
    logErrorToService(error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return <ErrorFallback error={this.state.error} />;
    }
    return this.props.children;
  }
}
```

## Logging Patterns

```typescript
// Structured logging
interface LogContext {
  userId?: string;
  requestId?: string;
  action?: string;
  [key: string]: unknown;
}

function logError(error: Error, context: LogContext = {}) {
  logger.error({
    message: error.message,
    stack: error.stack,
    code: error instanceof AppError ? error.code : 'UNKNOWN',
    ...context
  });
}
```

## Detection Queries

### Find Custom Error Classes
```bash
grep -r "extends Error" src/
grep -r "class.*Error" src/
```

### Find Try-Catch Blocks
```bash
grep -r "try {" src/ | wc -l
grep -r "catch\s*(" src/ | head -10
```

### Find Error Middleware
```bash
grep -r "errorHandler" src/
grep -r "err.*req.*res.*next" src/
```
