# Testing Patterns

## Test File Organization

### Co-located Tests
```
src/
├── services/
│   ├── user.service.ts
│   └── user.service.test.ts
├── components/
│   ├── Button.tsx
│   └── Button.test.tsx
```

### Separate Test Directory
```
src/
├── services/
│   └── user.service.ts
tests/
├── services/
│   └── user.service.test.ts
```

### __tests__ Directory (Jest Default)
```
src/
├── services/
│   ├── __tests__/
│   │   └── user.service.test.ts
│   └── user.service.ts
```

## Test Naming Conventions

### describe/it Pattern
```typescript
describe('UserService', () => {
  describe('createUser', () => {
    it('should create a new user with valid data', () => {});
    it('should throw ValidationError for invalid email', () => {});
    it('should hash password before saving', () => {});
  });
});
```

### Naming Formula
```
should [expected behavior] when [condition]
```

Examples:
- `should return user when valid ID provided`
- `should throw NotFoundError when user does not exist`
- `should send email when user registered`

## Test Structure (AAA Pattern)

```typescript
it('should calculate total price with discount', () => {
  // Arrange
  const items = [
    { price: 100, quantity: 2 },
    { price: 50, quantity: 1 }
  ];
  const discount = 0.1;

  // Act
  const result = calculateTotal(items, discount);

  // Assert
  expect(result).toBe(225); // (200 + 50) * 0.9
});
```

## Mocking Patterns

### Manual Mocks
```typescript
const mockUserRepository = {
  findById: jest.fn(),
  create: jest.fn(),
  update: jest.fn(),
  delete: jest.fn()
};
```

### Jest Mock Functions
```typescript
jest.mock('../services/user.service');
const mockedUserService = UserService as jest.Mocked<typeof UserService>;
mockedUserService.getUser.mockResolvedValue({ id: '1', name: 'Test' });
```

### Dependency Injection
```typescript
describe('UserController', () => {
  let controller: UserController;
  let mockService: jest.Mocked<UserService>;

  beforeEach(() => {
    mockService = {
      getUser: jest.fn(),
      createUser: jest.fn()
    } as any;
    controller = new UserController(mockService);
  });
});
```

## Fixture Patterns

### Factory Functions
```typescript
function createTestUser(overrides: Partial<User> = {}): User {
  return {
    id: 'test-id',
    name: 'Test User',
    email: 'test@example.com',
    createdAt: new Date(),
    ...overrides
  };
}
```

### Fixture Files
```typescript
// fixtures/users.ts
export const validUser = {
  id: '1',
  name: 'John Doe',
  email: 'john@example.com'
};

export const invalidUser = {
  id: '',
  name: '',
  email: 'not-an-email'
};
```

## Async Testing

```typescript
// Using async/await
it('should fetch user data', async () => {
  const user = await userService.getUser('1');
  expect(user.name).toBe('John');
});

// Testing rejections
it('should throw on invalid ID', async () => {
  await expect(userService.getUser('invalid'))
    .rejects
    .toThrow(NotFoundError);
});
```

## Detection Queries

### Find Test Files
```bash
find . -name "*.test.ts" -o -name "*.spec.ts" | head -20
```

### Find Test Framework
```bash
grep -l "jest\|mocha\|vitest" package.json
```

### Find Mocking Patterns
```bash
grep -r "jest.mock\|jest.fn\|vi.mock" tests/ | head -10
```

### Count Test Coverage
```bash
grep -r "describe\|it\|test(" tests/ | wc -l
```
