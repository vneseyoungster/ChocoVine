# KISS - Keep It Simple, Stupid

> Simplicity should be a key goal in design, and unnecessary complexity should be avoided.

## Core Concept
The simplest solution that works is usually the best. Complexity is the enemy of maintainability.

## Guidelines

### Favor Readability Over Cleverness

**Clever (Bad):**
```typescript
const result = arr.reduce((a, c) => (a[c] = (a[c] || 0) + 1, a), {});
```

**Simple (Good):**
```typescript
const counts: Record<string, number> = {};
for (const item of arr) {
  counts[item] = (counts[item] || 0) + 1;
}
```

### One Thing Per Function

**Complex (Bad):**
```typescript
function processUser(userData: unknown) {
  // Validate
  if (!userData || typeof userData !== 'object') {
    throw new Error('Invalid');
  }
  const { name, email } = userData as any;
  if (!name || !email) {
    throw new Error('Missing fields');
  }
  if (!email.includes('@')) {
    throw new Error('Invalid email');
  }

  // Transform
  const user = {
    name: name.trim(),
    email: email.toLowerCase(),
    createdAt: new Date()
  };

  // Save
  database.users.insert(user);

  // Notify
  emailService.send(email, 'Welcome!');

  return user;
}
```

**Simple (Good):**
```typescript
function validateUserData(data: unknown): UserInput {
  // Single responsibility: validation
}

function createUser(input: UserInput): User {
  // Single responsibility: creation
}

function saveUser(user: User): void {
  // Single responsibility: persistence
}

function sendWelcomeEmail(user: User): void {
  // Single responsibility: notification
}

// Compose simply
const input = validateUserData(userData);
const user = createUser(input);
saveUser(user);
sendWelcomeEmail(user);
```

### Choose Obvious Over Implicit

**Implicit (Bad):**
```typescript
// What does 86400000 mean?
setTimeout(callback, 86400000);

// What does the second parameter do?
formatDate(date, true);
```

**Obvious (Good):**
```typescript
const ONE_DAY_MS = 24 * 60 * 60 * 1000;
setTimeout(callback, ONE_DAY_MS);

// Use named parameters or options object
formatDate(date, { includeTime: true });
```

### Avoid Deep Nesting

**Deeply Nested (Bad):**
```typescript
function processOrder(order: Order) {
  if (order) {
    if (order.items) {
      if (order.items.length > 0) {
        if (order.customer) {
          if (order.customer.verified) {
            // Finally do something
          }
        }
      }
    }
  }
}
```

**Flat (Good):**
```typescript
function processOrder(order: Order) {
  if (!order) return;
  if (!order.items?.length) return;
  if (!order.customer?.verified) return;

  // Do something
}
```

### Use Standard Solutions

**Custom (Bad):**
```typescript
// Custom date parsing
function parseDate(str: string) {
  const parts = str.split('-');
  return new Date(+parts[0], +parts[1] - 1, +parts[2]);
}
```

**Standard (Good):**
```typescript
// Use built-in or well-tested libraries
const date = new Date(str);
// or
import { parseISO } from 'date-fns';
const date = parseISO(str);
```

## Complexity Indicators

Watch for these signs:
- [ ] Functions longer than 20 lines
- [ ] More than 3 levels of nesting
- [ ] More than 5 parameters
- [ ] Complex conditionals (multiple &&, ||)
- [ ] Need to write comments explaining how code works

## Simplification Strategies

1. **Extract Method**: Break large functions into smaller ones
2. **Early Return**: Eliminate nesting with guard clauses
3. **Replace Conditional with Polymorphism**: Use objects instead of switch/if
4. **Use Built-in Functions**: Array methods, string methods, etc.
5. **Decompose Conditional**: Extract complex conditions to named variables

## Checklist
- [ ] Can someone understand this code in 30 seconds?
- [ ] Is there a simpler way to achieve the same result?
- [ ] Am I using language/framework features appropriately?
- [ ] Have I avoided premature optimization?
- [ ] Is the code self-documenting?
