# DRY - Don't Repeat Yourself

> Every piece of knowledge must have a single, unambiguous, authoritative representation within a system.

## Core Concept
DRY is about knowledge duplication, not just code duplication. Sometimes similar-looking code represents different knowledge and should NOT be merged.

## When to Apply DRY

### Extract Common Logic

**Before (Repeated):**
```typescript
function calculateOrderTotal(items: OrderItem[]): number {
  let total = 0;
  for (const item of items) {
    total += item.price * item.quantity;
  }
  return total * 1.1; // Add 10% tax
}

function calculateCartTotal(items: CartItem[]): number {
  let total = 0;
  for (const item of items) {
    total += item.price * item.quantity;
  }
  return total * 1.1; // Add 10% tax
}
```

**After (DRY):**
```typescript
interface Priceable {
  price: number;
  quantity: number;
}

function calculateTotal<T extends Priceable>(items: T[], taxRate = 0.1): number {
  const subtotal = items.reduce((sum, item) => sum + item.price * item.quantity, 0);
  return subtotal * (1 + taxRate);
}
```

### Use Constants for Magic Values

**Before:**
```typescript
if (user.role === 'admin') { /* ... */ }
if (user.role === 'admin') { /* ... */ }
if (retries > 3) { /* ... */ }
```

**After:**
```typescript
const ROLES = {
  ADMIN: 'admin',
  USER: 'user',
  GUEST: 'guest'
} as const;

const MAX_RETRIES = 3;

if (user.role === ROLES.ADMIN) { /* ... */ }
if (retries > MAX_RETRIES) { /* ... */ }
```

### Create Shared Utilities

**Before:**
```typescript
// In file1.ts
const formattedDate = `${date.getFullYear()}-${String(date.getMonth() + 1).padStart(2, '0')}-${String(date.getDate()).padStart(2, '0')}`;

// In file2.ts
const formattedDate = `${date.getFullYear()}-${String(date.getMonth() + 1).padStart(2, '0')}-${String(date.getDate()).padStart(2, '0')}`;
```

**After:**
```typescript
// utils/date.ts
export function formatDate(date: Date): string {
  return date.toISOString().split('T')[0];
}

// file1.ts & file2.ts
import { formatDate } from './utils/date';
const formattedDate = formatDate(date);
```

## When NOT to Apply DRY

### Accidental Duplication
When code looks similar but represents different concepts:

```typescript
// These look similar but serve different purposes
function validateUsername(username: string): boolean {
  return username.length >= 3 && username.length <= 20;
}

function validateProductCode(code: string): boolean {
  return code.length >= 3 && code.length <= 20;
}
// Keep separate - validation rules may evolve differently
```

### Premature Abstraction
Don't extract until you see the pattern 3+ times:

```typescript
// Don't create abstractions for hypothetical future needs
// Wait for actual duplication before extracting
```

## Rule of Three
Extract when you see duplication **three times**:
1. First time: Just write it
2. Second time: Note the duplication
3. Third time: Extract and refactor

## Checklist
- [ ] Are there repeated code blocks doing the same thing?
- [ ] Are magic numbers/strings used in multiple places?
- [ ] Is business logic duplicated across files?
- [ ] Are validation rules defined in multiple locations?
- [ ] Is the same data transformation repeated?
