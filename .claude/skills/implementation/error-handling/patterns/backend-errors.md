# Backend Error Handling Patterns

## Error Hierarchy

Create a hierarchy of error classes for different error types:

```typescript
// Base application error
export class AppError extends Error {
  public readonly isOperational: boolean;

  constructor(
    public readonly code: string,
    message: string,
    public readonly statusCode: number = 500,
    public readonly details?: unknown,
    isOperational = true
  ) {
    super(message);
    this.name = this.constructor.name;
    this.isOperational = isOperational;
    Error.captureStackTrace(this, this.constructor);
  }
}

// Client errors (4xx)
export class ClientError extends AppError {
  constructor(code: string, message: string, statusCode: number, details?: unknown) {
    super(code, message, statusCode, details, true);
  }
}

export class ValidationError extends ClientError {
  constructor(message: string, details?: unknown) {
    super('VALIDATION_ERROR', message, 400, details);
  }
}

export class UnauthorizedError extends ClientError {
  constructor(message = 'Authentication required') {
    super('UNAUTHORIZED', message, 401);
  }
}

export class ForbiddenError extends ClientError {
  constructor(message = 'Access denied') {
    super('FORBIDDEN', message, 403);
  }
}

export class NotFoundError extends ClientError {
  constructor(resource: string) {
    super('NOT_FOUND', `${resource} not found`, 404);
  }
}

export class ConflictError extends ClientError {
  constructor(message: string) {
    super('CONFLICT', message, 409);
  }
}

// Server errors (5xx)
export class ServerError extends AppError {
  constructor(message: string, details?: unknown) {
    super('INTERNAL_ERROR', message, 500, details, false);
  }
}
```

## Error Handler Middleware

### Express Example
```typescript
import { Request, Response, NextFunction } from 'express';
import { logger } from './logger';

export function errorHandler(
  err: Error,
  req: Request,
  res: Response,
  next: NextFunction
): void {
  const requestId = req.headers['x-request-id'] as string || generateId();

  // Log the error
  if (err instanceof AppError && err.isOperational) {
    logger.warn({ err, requestId }, 'Operational error');
  } else {
    logger.error({ err, requestId }, 'Unexpected error');
  }

  // Handle known application errors
  if (err instanceof AppError) {
    res.status(err.statusCode).json({
      error: {
        code: err.code,
        message: err.message,
        details: err.details,
        requestId
      }
    });
    return;
  }

  // Handle unknown errors
  res.status(500).json({
    error: {
      code: 'INTERNAL_ERROR',
      message: process.env.NODE_ENV === 'production'
        ? 'An unexpected error occurred'
        : err.message,
      requestId
    }
  });
}
```

## Async Error Handling

### Wrap Async Routes
```typescript
type AsyncHandler = (
  req: Request,
  res: Response,
  next: NextFunction
) => Promise<void>;

export function asyncHandler(fn: AsyncHandler) {
  return (req: Request, res: Response, next: NextFunction) => {
    Promise.resolve(fn(req, res, next)).catch(next);
  };
}

// Usage
router.get('/users/:id', asyncHandler(async (req, res) => {
  const user = await userService.findById(req.params.id);
  if (!user) throw new NotFoundError('User');
  res.json({ data: user });
}));
```

## Service Layer Error Handling

```typescript
class UserService {
  async findById(id: string): Promise<User> {
    const user = await this.repository.findById(id);
    if (!user) {
      throw new NotFoundError('User');
    }
    return user;
  }

  async create(data: CreateUserDto): Promise<User> {
    // Validate
    const errors = this.validate(data);
    if (errors.length > 0) {
      throw new ValidationError('Invalid user data', errors);
    }

    // Check for duplicates
    const existing = await this.repository.findByEmail(data.email);
    if (existing) {
      throw new ConflictError('User with this email already exists');
    }

    return this.repository.create(data);
  }
}
```

## Error Context

Always include helpful context:

```typescript
// Bad
throw new Error('Failed');

// Good
throw new NotFoundError('User');

// Better (with context)
throw new AppError(
  'USER_NOT_FOUND',
  `User with ID ${id} not found`,
  404,
  { userId: id, requestedBy: currentUser.id }
);
```

## Logging Best Practices

```typescript
// Use structured logging
logger.error({
  err,
  context: {
    userId: req.user?.id,
    requestId: req.headers['x-request-id'],
    path: req.path,
    method: req.method
  }
}, 'Request failed');

// Log levels
logger.debug('Detailed debugging info');    // Development only
logger.info('User logged in');              // Normal operations
logger.warn('Rate limit approaching');      // Potential issues
logger.error('Database connection failed'); // Actual errors
```

## Recovery Strategies

```typescript
async function withRetry<T>(
  fn: () => Promise<T>,
  maxRetries: number = 3,
  delay: number = 1000
): Promise<T> {
  let lastError: Error;

  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    try {
      return await fn();
    } catch (error) {
      lastError = error as Error;
      logger.warn({ attempt, maxRetries, error }, 'Retry attempt');

      if (attempt < maxRetries) {
        await sleep(delay * attempt); // Exponential backoff
      }
    }
  }

  throw lastError!;
}

// Usage
const result = await withRetry(() => externalService.call(), 3, 1000);
```
