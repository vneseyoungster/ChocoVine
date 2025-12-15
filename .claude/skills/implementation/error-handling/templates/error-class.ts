/**
 * Custom Error Classes Template
 *
 * Copy and adapt these error classes for your application.
 */

// ============================================================================
// Base Application Error
// ============================================================================

/**
 * Base error class for all application errors.
 *
 * @example
 * ```typescript
 * throw new AppError('CUSTOM_ERROR', 'Something went wrong', 500, { detail: 'value' });
 * ```
 */
export class AppError extends Error {
  /**
   * Whether this error is operational (expected) vs programming error
   */
  public readonly isOperational: boolean;

  constructor(
    /** Error code for programmatic handling */
    public readonly code: string,
    /** Human-readable error message */
    message: string,
    /** HTTP status code */
    public readonly statusCode: number = 500,
    /** Additional error details */
    public readonly details?: unknown,
    /** Whether this is an expected operational error */
    isOperational = true
  ) {
    super(message);
    this.name = this.constructor.name;
    this.isOperational = isOperational;
    Error.captureStackTrace(this, this.constructor);
  }

  /**
   * Convert error to JSON for API responses
   */
  toJSON(): Record<string, unknown> {
    return {
      code: this.code,
      message: this.message,
      details: this.details,
    };
  }
}

// ============================================================================
// Client Errors (4xx)
// ============================================================================

/**
 * Validation error (400 Bad Request)
 *
 * @example
 * ```typescript
 * throw new ValidationError('Invalid input', [
 *   { field: 'email', message: 'Invalid email format' }
 * ]);
 * ```
 */
export class ValidationError extends AppError {
  constructor(message: string, details?: unknown) {
    super('VALIDATION_ERROR', message, 400, details);
  }
}

/**
 * Authentication error (401 Unauthorized)
 *
 * @example
 * ```typescript
 * throw new UnauthorizedError('Invalid or expired token');
 * ```
 */
export class UnauthorizedError extends AppError {
  constructor(message = 'Authentication required') {
    super('UNAUTHORIZED', message, 401);
  }
}

/**
 * Authorization error (403 Forbidden)
 *
 * @example
 * ```typescript
 * throw new ForbiddenError('You do not have permission to access this resource');
 * ```
 */
export class ForbiddenError extends AppError {
  constructor(message = 'Access denied') {
    super('FORBIDDEN', message, 403);
  }
}

/**
 * Resource not found error (404 Not Found)
 *
 * @example
 * ```typescript
 * throw new NotFoundError('User');
 * // Results in: "User not found"
 * ```
 */
export class NotFoundError extends AppError {
  constructor(resource: string) {
    super('NOT_FOUND', `${resource} not found`, 404);
  }
}

/**
 * Conflict error (409 Conflict)
 *
 * @example
 * ```typescript
 * throw new ConflictError('User with this email already exists');
 * ```
 */
export class ConflictError extends AppError {
  constructor(message: string) {
    super('CONFLICT', message, 409);
  }
}

/**
 * Business rule violation (422 Unprocessable Entity)
 *
 * @example
 * ```typescript
 * throw new BusinessRuleError('Cannot delete user with active orders');
 * ```
 */
export class BusinessRuleError extends AppError {
  constructor(message: string, details?: unknown) {
    super('BUSINESS_RULE_VIOLATION', message, 422, details);
  }
}

/**
 * Rate limit exceeded (429 Too Many Requests)
 *
 * @example
 * ```typescript
 * throw new RateLimitError('Too many requests', { retryAfter: 60 });
 * ```
 */
export class RateLimitError extends AppError {
  constructor(message = 'Too many requests', details?: { retryAfter?: number }) {
    super('RATE_LIMITED', message, 429, details);
  }
}

// ============================================================================
// Server Errors (5xx)
// ============================================================================

/**
 * Internal server error (500)
 * Used for unexpected errors
 *
 * @example
 * ```typescript
 * throw new InternalError('Database connection failed');
 * ```
 */
export class InternalError extends AppError {
  constructor(message: string, details?: unknown) {
    super('INTERNAL_ERROR', message, 500, details, false);
  }
}

/**
 * Service unavailable error (503)
 *
 * @example
 * ```typescript
 * throw new ServiceUnavailableError('Database is currently unavailable');
 * ```
 */
export class ServiceUnavailableError extends AppError {
  constructor(message = 'Service temporarily unavailable') {
    super('SERVICE_UNAVAILABLE', message, 503);
  }
}

// ============================================================================
// Frontend-specific Errors
// ============================================================================

/**
 * API error for frontend use
 *
 * @example
 * ```typescript
 * const error = ApiError.fromResponse(response, body);
 * ```
 */
export class ApiError extends Error {
  constructor(
    public readonly code: string,
    message: string,
    public readonly status: number,
    public readonly details?: unknown
  ) {
    super(message);
    this.name = 'ApiError';
  }

  /**
   * Create ApiError from fetch response
   */
  static fromResponse(response: Response, body: any): ApiError {
    return new ApiError(
      body.error?.code || 'UNKNOWN_ERROR',
      body.error?.message || 'An error occurred',
      response.status,
      body.error?.details
    );
  }

  /**
   * Check if error is a network error
   */
  get isNetworkError(): boolean {
    return this.status === 0;
  }

  /**
   * Check if error is a client error (4xx)
   */
  get isClientError(): boolean {
    return this.status >= 400 && this.status < 500;
  }

  /**
   * Check if error is a server error (5xx)
   */
  get isServerError(): boolean {
    return this.status >= 500;
  }
}

// ============================================================================
// Type Guards
// ============================================================================

/**
 * Check if an error is an AppError
 */
export function isAppError(error: unknown): error is AppError {
  return error instanceof AppError;
}

/**
 * Check if an error is an ApiError
 */
export function isApiError(error: unknown): error is ApiError {
  return error instanceof ApiError;
}

/**
 * Check if an error is operational (expected)
 */
export function isOperationalError(error: unknown): boolean {
  if (error instanceof AppError) {
    return error.isOperational;
  }
  return false;
}
