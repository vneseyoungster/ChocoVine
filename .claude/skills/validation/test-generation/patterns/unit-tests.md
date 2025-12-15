# Unit Testing Patterns

## Overview

Unit tests verify individual functions, methods, or classes in isolation from their dependencies.

## Characteristics

- **Fast**: Execute in milliseconds
- **Isolated**: No external dependencies
- **Deterministic**: Same result every time
- **Focused**: One concern per test

## Structure Pattern

### Basic Test Structure

```typescript
import { describe, it, expect, beforeEach, afterEach } from 'vitest';
import { Calculator } from './calculator';

describe('Calculator', () => {
  let calculator: Calculator;

  beforeEach(() => {
    calculator = new Calculator();
  });

  afterEach(() => {
    // Cleanup if needed
  });

  describe('add', () => {
    it('should return sum of two positive numbers', () => {
      expect(calculator.add(2, 3)).toBe(5);
    });

    it('should handle negative numbers', () => {
      expect(calculator.add(-2, 3)).toBe(1);
    });

    it('should handle zero', () => {
      expect(calculator.add(0, 5)).toBe(5);
    });
  });
});
```

## Testing Patterns

### Testing Pure Functions

```typescript
// Function under test
function formatCurrency(amount: number, currency: string): string {
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency,
  }).format(amount);
}

// Tests
describe('formatCurrency', () => {
  it('should format USD correctly', () => {
    expect(formatCurrency(1234.56, 'USD')).toBe('$1,234.56');
  });

  it('should handle zero', () => {
    expect(formatCurrency(0, 'USD')).toBe('$0.00');
  });

  it('should handle negative amounts', () => {
    expect(formatCurrency(-50, 'USD')).toBe('-$50.00');
  });
});
```

### Testing with Mocks

```typescript
import { vi } from 'vitest';

describe('UserService', () => {
  it('should create user and send welcome email', async () => {
    // Arrange
    const mockRepository = {
      save: vi.fn().mockResolvedValue({ id: '123', email: 'test@example.com' }),
    };
    const mockEmailService = {
      sendWelcome: vi.fn().mockResolvedValue(undefined),
    };
    const service = new UserService(mockRepository, mockEmailService);

    // Act
    const user = await service.createUser({ email: 'test@example.com' });

    // Assert
    expect(user.id).toBe('123');
    expect(mockRepository.save).toHaveBeenCalledWith({ email: 'test@example.com' });
    expect(mockEmailService.sendWelcome).toHaveBeenCalledWith('test@example.com');
  });
});
```

### Testing Async Code

```typescript
describe('AsyncService', () => {
  it('should resolve with data', async () => {
    const result = await asyncFunction();
    expect(result).toEqual(expectedData);
  });

  it('should reject with error', async () => {
    await expect(asyncFunctionThatFails()).rejects.toThrow('Expected error');
  });

  it('should handle promises with then', () => {
    return asyncFunction().then((result) => {
      expect(result).toEqual(expectedData);
    });
  });
});
```

### Testing Errors

```typescript
describe('validateEmail', () => {
  it('should throw ValidationError for invalid email', () => {
    expect(() => validateEmail('invalid')).toThrow(ValidationError);
  });

  it('should throw with specific message', () => {
    expect(() => validateEmail('invalid')).toThrow('Invalid email format');
  });

  it('should not throw for valid email', () => {
    expect(() => validateEmail('test@example.com')).not.toThrow();
  });
});
```

### Parameterized Tests

```typescript
describe('isValidEmail', () => {
  const validEmails = [
    'test@example.com',
    'user.name@domain.co.uk',
    'user+tag@example.org',
  ];

  const invalidEmails = [
    'invalid',
    '@example.com',
    'test@',
    'test @example.com',
  ];

  it.each(validEmails)('should return true for valid email: %s', (email) => {
    expect(isValidEmail(email)).toBe(true);
  });

  it.each(invalidEmails)('should return false for invalid email: %s', (email) => {
    expect(isValidEmail(email)).toBe(false);
  });
});
```

## Test Data Factories

```typescript
// factories/user.ts
export function createTestUser(overrides: Partial<User> = {}): User {
  return {
    id: 'test-id',
    email: 'test@example.com',
    name: 'Test User',
    createdAt: new Date('2024-01-01'),
    ...overrides,
  };
}

// Usage in tests
it('should update user email', () => {
  const user = createTestUser({ email: 'old@example.com' });
  const updated = updateEmail(user, 'new@example.com');
  expect(updated.email).toBe('new@example.com');
});
```

## Common Assertions

```typescript
// Equality
expect(value).toBe(expected);           // Strict equality
expect(value).toEqual(expected);        // Deep equality
expect(value).toStrictEqual(expected);  // Deep + type equality

// Truthiness
expect(value).toBeTruthy();
expect(value).toBeFalsy();
expect(value).toBeNull();
expect(value).toBeUndefined();
expect(value).toBeDefined();

// Numbers
expect(value).toBeGreaterThan(3);
expect(value).toBeGreaterThanOrEqual(3);
expect(value).toBeLessThan(5);
expect(value).toBeCloseTo(0.3, 5);

// Strings
expect(value).toMatch(/pattern/);
expect(value).toContain('substring');

// Arrays
expect(array).toContain(item);
expect(array).toHaveLength(3);
expect(array).toContainEqual({ id: 1 });

// Objects
expect(object).toHaveProperty('key');
expect(object).toHaveProperty('key', value);
expect(object).toMatchObject({ partial: 'match' });

// Functions
expect(fn).toHaveBeenCalled();
expect(fn).toHaveBeenCalledWith(arg1, arg2);
expect(fn).toHaveBeenCalledTimes(3);
```

## Anti-Patterns to Avoid

### Testing Implementation Details

```typescript
// Bad - tests internal state
it('should set internal flag', () => {
  component.click();
  expect(component._internalFlag).toBe(true);
});

// Good - tests behavior
it('should show success message after click', () => {
  component.click();
  expect(component.message).toBe('Success');
});
```

### Multiple Assertions Without Context

```typescript
// Bad - unclear what's being tested
it('should work', () => {
  expect(result.id).toBeDefined();
  expect(result.name).toBe('test');
  expect(result.status).toBe('active');
  expect(result.createdAt).toBeDefined();
});

// Good - grouped by concern
describe('created user', () => {
  it('should have an id', () => {});
  it('should have the provided name', () => {});
  it('should have active status', () => {});
  it('should have a creation timestamp', () => {});
});
```

### Non-Deterministic Tests

```typescript
// Bad - depends on current time
it('should be recent', () => {
  const user = createUser();
  expect(user.createdAt.getTime()).toBeCloseTo(Date.now(), -3);
});

// Good - mock the time
it('should set creation date', () => {
  vi.setSystemTime(new Date('2024-01-01'));
  const user = createUser();
  expect(user.createdAt).toEqual(new Date('2024-01-01'));
  vi.useRealTimers();
});
```
