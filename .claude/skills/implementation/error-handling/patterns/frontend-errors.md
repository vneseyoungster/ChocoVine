# Frontend Error Handling Patterns

## Error Boundaries

### Basic Error Boundary
```tsx
import React, { Component, ErrorInfo, ReactNode } from 'react';

interface Props {
  children: ReactNode;
  fallback?: ReactNode;
  onError?: (error: Error, errorInfo: ErrorInfo) => void;
}

interface State {
  hasError: boolean;
  error: Error | null;
}

export class ErrorBoundary extends Component<Props, State> {
  state: State = {
    hasError: false,
    error: null
  };

  static getDerivedStateFromError(error: Error): State {
    return { hasError: true, error };
  }

  componentDidCatch(error: Error, errorInfo: ErrorInfo): void {
    // Log to error reporting service
    console.error('Error caught by boundary:', error, errorInfo);
    this.props.onError?.(error, errorInfo);
  }

  render(): ReactNode {
    if (this.state.hasError) {
      return this.props.fallback || <DefaultErrorFallback />;
    }

    return this.props.children;
  }
}

// Usage
<ErrorBoundary
  fallback={<ErrorPage />}
  onError={(error) => reportError(error)}
>
  <App />
</ErrorBoundary>
```

### Resettable Error Boundary
```tsx
interface ResettableProps extends Props {
  resetKeys?: unknown[];
}

export class ResettableErrorBoundary extends Component<ResettableProps, State> {
  state: State = { hasError: false, error: null };

  static getDerivedStateFromError(error: Error): State {
    return { hasError: true, error };
  }

  componentDidUpdate(prevProps: ResettableProps): void {
    if (this.state.hasError && this.props.resetKeys) {
      const hasChanged = this.props.resetKeys.some(
        (key, idx) => key !== prevProps.resetKeys?.[idx]
      );
      if (hasChanged) {
        this.reset();
      }
    }
  }

  reset = (): void => {
    this.setState({ hasError: false, error: null });
  };

  render(): ReactNode {
    if (this.state.hasError) {
      return (
        <ErrorFallback
          error={this.state.error!}
          onReset={this.reset}
        />
      );
    }
    return this.props.children;
  }
}
```

## API Error Handling

### Custom Error Class
```typescript
export class ApiError extends Error {
  constructor(
    public code: string,
    message: string,
    public status: number,
    public details?: unknown
  ) {
    super(message);
    this.name = 'ApiError';
  }

  static fromResponse(response: Response, body: any): ApiError {
    return new ApiError(
      body.error?.code || 'UNKNOWN_ERROR',
      body.error?.message || 'An error occurred',
      response.status,
      body.error?.details
    );
  }
}
```

### Fetch Wrapper
```typescript
async function apiFetch<T>(
  url: string,
  options?: RequestInit
): Promise<T> {
  try {
    const response = await fetch(url, {
      ...options,
      headers: {
        'Content-Type': 'application/json',
        ...options?.headers
      }
    });

    const body = await response.json();

    if (!response.ok) {
      throw ApiError.fromResponse(response, body);
    }

    return body.data;
  } catch (error) {
    if (error instanceof ApiError) {
      throw error;
    }

    // Network error
    throw new ApiError(
      'NETWORK_ERROR',
      'Unable to connect to server',
      0
    );
  }
}
```

### React Query Error Handling
```tsx
import { useQuery, useMutation } from '@tanstack/react-query';

function UserProfile({ userId }: { userId: string }) {
  const { data, error, isLoading, refetch } = useQuery({
    queryKey: ['user', userId],
    queryFn: () => apiFetch<User>(`/api/users/${userId}`),
    retry: (failureCount, error) => {
      // Don't retry on 4xx errors
      if (error instanceof ApiError && error.status < 500) {
        return false;
      }
      return failureCount < 3;
    }
  });

  if (isLoading) return <Spinner />;

  if (error) {
    return (
      <ErrorMessage
        error={error as ApiError}
        onRetry={refetch}
      />
    );
  }

  return <UserCard user={data!} />;
}
```

## Form Error Handling

```tsx
interface FormErrors {
  [field: string]: string | undefined;
}

function LoginForm() {
  const [errors, setErrors] = useState<FormErrors>({});
  const [submitError, setSubmitError] = useState<string | null>(null);

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    setErrors({});
    setSubmitError(null);

    try {
      await login(email, password);
    } catch (error) {
      if (error instanceof ApiError) {
        if (error.code === 'VALIDATION_ERROR' && error.details) {
          // Field-level errors
          const fieldErrors: FormErrors = {};
          (error.details as any[]).forEach(d => {
            fieldErrors[d.field] = d.message;
          });
          setErrors(fieldErrors);
        } else {
          // Form-level error
          setSubmitError(error.message);
        }
      } else {
        setSubmitError('An unexpected error occurred');
      }
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      {submitError && <Alert type="error">{submitError}</Alert>}

      <FormField
        label="Email"
        name="email"
        error={errors.email}
      >
        <Input type="email" name="email" />
      </FormField>

      <Button type="submit">Login</Button>
    </form>
  );
}
```

## Toast Notifications

```typescript
// Toast service
const toast = {
  success: (message: string) => { /* ... */ },
  error: (message: string) => { /* ... */ },
  warning: (message: string) => { /* ... */ }
};

// Use with mutations
const mutation = useMutation({
  mutationFn: createUser,
  onSuccess: () => {
    toast.success('User created successfully');
  },
  onError: (error) => {
    if (error instanceof ApiError) {
      toast.error(error.message);
    } else {
      toast.error('An unexpected error occurred');
    }
  }
});
```

## Global Error Handler

```typescript
// Catch unhandled promise rejections
window.addEventListener('unhandledrejection', (event) => {
  console.error('Unhandled promise rejection:', event.reason);
  reportError(event.reason);
});

// Catch global errors
window.addEventListener('error', (event) => {
  console.error('Global error:', event.error);
  reportError(event.error);
});
```

## Error Reporting

```typescript
function reportError(error: Error, context?: Record<string, unknown>): void {
  // Send to error tracking service (Sentry, etc.)
  console.error('Reporting error:', {
    name: error.name,
    message: error.message,
    stack: error.stack,
    ...context
  });

  // Example with Sentry
  // Sentry.captureException(error, { extra: context });
}
```
