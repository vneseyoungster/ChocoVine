# Integration Testing Patterns

## Overview

Integration tests verify that multiple components work together correctly, including interaction with databases, APIs, and external services.

## Characteristics

- **Slower**: Takes seconds to minutes
- **Less isolated**: Tests real interactions
- **More realistic**: Catches integration bugs
- **Database/API involved**: Tests actual connections

## Test Structure

### API Integration Tests

```typescript
import { describe, it, expect, beforeAll, afterAll } from 'vitest';
import request from 'supertest';
import { app } from '../app';
import { db } from '../database';

describe('User API', () => {
  beforeAll(async () => {
    await db.connect();
    await db.migrate();
  });

  afterAll(async () => {
    await db.close();
  });

  beforeEach(async () => {
    await db.truncate(['users']);
  });

  describe('POST /api/users', () => {
    it('should create a new user', async () => {
      const response = await request(app)
        .post('/api/users')
        .send({ email: 'test@example.com', name: 'Test User' })
        .expect(201);

      expect(response.body).toMatchObject({
        id: expect.any(String),
        email: 'test@example.com',
        name: 'Test User',
      });
    });

    it('should return 400 for invalid email', async () => {
      const response = await request(app)
        .post('/api/users')
        .send({ email: 'invalid', name: 'Test' })
        .expect(400);

      expect(response.body.error.code).toBe('VALIDATION_ERROR');
    });

    it('should return 409 for duplicate email', async () => {
      // Create first user
      await request(app)
        .post('/api/users')
        .send({ email: 'test@example.com', name: 'First' });

      // Attempt duplicate
      const response = await request(app)
        .post('/api/users')
        .send({ email: 'test@example.com', name: 'Second' })
        .expect(409);

      expect(response.body.error.code).toBe('DUPLICATE_EMAIL');
    });
  });

  describe('GET /api/users/:id', () => {
    it('should return user by id', async () => {
      // Create user first
      const createResponse = await request(app)
        .post('/api/users')
        .send({ email: 'test@example.com', name: 'Test' });

      const userId = createResponse.body.id;

      // Fetch user
      const response = await request(app)
        .get(`/api/users/${userId}`)
        .expect(200);

      expect(response.body.id).toBe(userId);
    });

    it('should return 404 for non-existent user', async () => {
      await request(app)
        .get('/api/users/non-existent-id')
        .expect(404);
    });
  });
});
```

### Database Integration Tests

```typescript
describe('UserRepository', () => {
  let repository: UserRepository;

  beforeAll(async () => {
    await db.connect();
  });

  afterAll(async () => {
    await db.close();
  });

  beforeEach(async () => {
    await db.truncate(['users']);
    repository = new UserRepository(db);
  });

  describe('findById', () => {
    it('should return user when exists', async () => {
      // Insert test data
      const inserted = await repository.create({
        email: 'test@example.com',
        name: 'Test',
      });

      // Query
      const found = await repository.findById(inserted.id);

      expect(found).toMatchObject({
        id: inserted.id,
        email: 'test@example.com',
      });
    });

    it('should return null when not exists', async () => {
      const found = await repository.findById('non-existent');
      expect(found).toBeNull();
    });
  });

  describe('transactions', () => {
    it('should rollback on error', async () => {
      await expect(
        repository.transferCredits('user1', 'user2', 100)
      ).rejects.toThrow();

      // Verify no changes
      const user1 = await repository.findById('user1');
      expect(user1.credits).toBe(50); // Original amount
    });
  });
});
```

### External Service Integration

```typescript
describe('PaymentService Integration', () => {
  let paymentService: PaymentService;

  beforeAll(() => {
    // Use test/sandbox API keys
    paymentService = new PaymentService({
      apiKey: process.env.STRIPE_TEST_KEY,
      environment: 'test',
    });
  });

  it('should create a payment intent', async () => {
    const intent = await paymentService.createPaymentIntent({
      amount: 1000,
      currency: 'usd',
    });

    expect(intent.id).toMatch(/^pi_/);
    expect(intent.amount).toBe(1000);
    expect(intent.status).toBe('requires_payment_method');
  });

  it('should handle declined cards', async () => {
    await expect(
      paymentService.charge({
        amount: 1000,
        card: 'tok_chargeDeclined',
      })
    ).rejects.toThrow('Card declined');
  });
});
```

## Test Database Setup

### Using Test Containers

```typescript
import { PostgreSqlContainer } from '@testcontainers/postgresql';

let container: StartedPostgreSqlContainer;

beforeAll(async () => {
  container = await new PostgreSqlContainer()
    .withDatabase('test')
    .start();

  process.env.DATABASE_URL = container.getConnectionUri();
  await db.connect();
  await db.migrate();
}, 60000); // Higher timeout for container startup

afterAll(async () => {
  await db.close();
  await container.stop();
});
```

### Using In-Memory Database

```typescript
beforeAll(async () => {
  await db.connect(':memory:');
  await db.migrate();
});
```

### Test Data Seeding

```typescript
async function seedTestData() {
  await db.users.createMany([
    { id: 'user-1', email: 'user1@test.com', role: 'admin' },
    { id: 'user-2', email: 'user2@test.com', role: 'user' },
  ]);

  await db.posts.createMany([
    { id: 'post-1', authorId: 'user-1', title: 'Test Post' },
  ]);
}

beforeEach(async () => {
  await db.truncateAll();
  await seedTestData();
});
```

## Best Practices

### Test Isolation

```typescript
// Each test should start with clean state
beforeEach(async () => {
  await db.truncate(['users', 'posts', 'comments']);
});

// Tests should not depend on order
it('should work independently', async () => {
  // Set up all required data within the test
  const user = await createUser();
  const post = await createPost(user.id);

  // Test behavior
  const result = await getPostWithAuthor(post.id);
  expect(result.author.id).toBe(user.id);
});
```

### Realistic Test Data

```typescript
// Use factories that create realistic data
const user = await createTestUser({
  email: 'realistic@example.com',
  createdAt: subDays(new Date(), 30),
});

// Test with edge case data
const userWithLongName = await createTestUser({
  name: 'A'.repeat(100),
});
```

### Cleanup Resources

```typescript
afterEach(async () => {
  // Clean up any created resources
  await cleanupTestFiles();
  await db.truncate(['test_uploads']);
});

afterAll(async () => {
  // Close connections
  await db.close();
  await redis.quit();
});
```

## Common Integration Points

### API + Database

- Test full request/response cycle
- Verify data persisted correctly
- Test transactions and rollbacks

### API + External Services

- Use sandbox/test environments
- Test webhook handling
- Test error scenarios

### Message Queues

- Test message publishing
- Test consumer handling
- Test dead letter queues

### Caching

- Test cache hits/misses
- Test cache invalidation
- Test cache consistency
