# YAGNI - You Aren't Gonna Need It

> Always implement things when you actually need them, never when you just foresee that you need them.

## Core Concept
Don't add functionality until it's necessary. Speculative features add complexity, maintenance burden, and often go unused.

## Guidelines

### Implement Only What's Needed Now

**Over-engineered (Bad):**
```typescript
interface UserRepositoryOptions {
  cache?: boolean;
  cacheTimeout?: number;
  retryCount?: number;
  retryDelay?: number;
  logging?: boolean;
  metrics?: boolean;
  circuitBreaker?: boolean;
  // ... 20 more options for "future needs"
}

class UserRepository {
  constructor(options: UserRepositoryOptions = {}) {
    // Complex initialization for features we might never use
  }
}
```

**Just Enough (Good):**
```typescript
class UserRepository {
  async findById(id: string): Promise<User | null> {
    return this.db.users.findUnique({ where: { id } });
  }

  async save(user: User): Promise<void> {
    await this.db.users.upsert({
      where: { id: user.id },
      update: user,
      create: user
    });
  }
}
// Add caching, retries, etc. when actually needed
```

### No Speculative Generalization

**Speculative (Bad):**
```typescript
// "We might need other notification types later"
interface NotificationStrategy {
  send(message: string, recipient: string): Promise<void>;
}

class EmailNotification implements NotificationStrategy { /* ... */ }
class SMSNotification implements NotificationStrategy { /* ... */ }
class PushNotification implements NotificationStrategy { /* ... */ }
class SlackNotification implements NotificationStrategy { /* ... */ }

class NotificationService {
  constructor(private strategies: NotificationStrategy[]) {}
  // Complex routing logic for strategies we don't use yet
}
```

**Practical (Good):**
```typescript
// We only need email right now
class EmailService {
  async sendEmail(to: string, subject: string, body: string): Promise<void> {
    await this.mailer.send({ to, subject, body });
  }
}
// Add other notification types when requirements demand them
```

### Add Complexity When Required

**Timeline:**
1. **Day 1**: Simple function works
2. **Month 3**: New requirement - add one parameter
3. **Month 6**: Pattern emerges - now extract abstraction

**Not:**
1. **Day 1**: Build complex abstraction for hypothetical future

### Avoid "Just In Case" Code

**Just In Case (Bad):**
```typescript
class User {
  id: string;
  email: string;
  name: string;

  // "Just in case we need these later"
  middleName?: string;
  suffix?: string;
  alternateEmail?: string;
  phoneNumbers?: string[];
  socialLinks?: Record<string, string>;
  preferences?: Record<string, unknown>;
  metadata?: Record<string, unknown>;
  legacyId?: string;
  externalIds?: Record<string, string>;
}
```

**Required Only (Good):**
```typescript
class User {
  id: string;
  email: string;
  name: string;
  // Add fields when requirements specify them
}
```

## When YAGNI Doesn't Apply

### Security
Always implement security measures:
```typescript
// Don't skip validation "because it's internal"
function updateUser(id: string, data: unknown) {
  const validated = validateUserUpdate(data); // Always validate
  // ...
}
```

### Data Integrity
Protect data from the start:
```typescript
// Use proper types and constraints
await db.users.create({
  data: {
    email: email.toLowerCase(), // Normalize early
    // ...
  }
});
```

### Core Architecture Decisions
Some decisions are hard to change later:
- Database schema basics
- API versioning strategy
- Authentication mechanism

## Cost of YAGNI Violations

| Problem | Cost |
|---------|------|
| Unused code | Maintenance burden |
| Extra complexity | Slower development |
| Premature abstraction | Wrong abstraction |
| Over-engineering | Technical debt |
| Feature creep | Delayed delivery |

## Questions to Ask

Before adding features:
1. Is this in the current requirements?
2. Do we have a concrete use case?
3. What's the cost of adding this later vs now?
4. Am I building for a real need or a hypothetical one?

## Checklist
- [ ] Is this feature in the current sprint/requirements?
- [ ] Do we have a user story for this?
- [ ] Are we building to spec, not speculation?
- [ ] Can this be added later without significant refactoring?
- [ ] Am I avoiding "wouldn't it be cool if..." features?
