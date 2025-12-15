# SOLID Principles

## S - Single Responsibility Principle
> A class should have only one reason to change.

**Good:**
```typescript
class UserRepository {
  findById(id: string): User {}
  save(user: User): void {}
}

class UserValidator {
  validate(user: User): ValidationResult {}
}
```

**Bad:**
```typescript
class User {
  findById(id: string): User {}
  validate(): ValidationResult {}
  sendEmail(): void {}
  formatForDisplay(): string {}
}
```

## O - Open/Closed Principle
> Open for extension, closed for modification.

**Good:**
```typescript
interface PaymentProcessor {
  process(amount: number): void;
}

class StripeProcessor implements PaymentProcessor {
  process(amount: number): void {
    // Stripe-specific implementation
  }
}

class PayPalProcessor implements PaymentProcessor {
  process(amount: number): void {
    // PayPal-specific implementation
  }
}
```

**Bad:**
```typescript
class PaymentProcessor {
  process(amount: number, type: 'stripe' | 'paypal') {
    if (type === 'stripe') { /* ... */ }
    else if (type === 'paypal') { /* ... */ }
    // Need to modify this class for every new payment type
  }
}
```

## L - Liskov Substitution Principle
> Subtypes must be substitutable for their base types.

**Good:**
```typescript
class Bird {
  move(): void {
    console.log('Moving');
  }
}

class Sparrow extends Bird {
  move(): void {
    console.log('Flying');
  }
}

class Penguin extends Bird {
  move(): void {
    console.log('Walking');
  }
}
```

**Bad:**
```typescript
class Bird {
  fly(): void {
    console.log('Flying');
  }
}

class Penguin extends Bird {
  fly(): void {
    throw new Error("Penguins can't fly!"); // Violates LSP
  }
}
```

## I - Interface Segregation Principle
> Clients shouldn't depend on interfaces they don't use.

**Good:**
```typescript
interface Readable {
  read(): string;
}

interface Writable {
  write(data: string): void;
}

interface ReadWritable extends Readable, Writable {}

class FileReader implements Readable {
  read(): string { /* ... */ }
}

class FileWriter implements Writable {
  write(data: string): void { /* ... */ }
}
```

**Bad:**
```typescript
interface FileOperations {
  read(): string;
  write(data: string): void;
  delete(): void;
  rename(name: string): void;
}

// Forced to implement methods it doesn't need
class ReadOnlyFile implements FileOperations {
  read(): string { /* ... */ }
  write(data: string): void { throw new Error('Read only'); }
  delete(): void { throw new Error('Read only'); }
  rename(name: string): void { throw new Error('Read only'); }
}
```

## D - Dependency Inversion Principle
> Depend on abstractions, not concretions.

**Good:**
```typescript
interface Logger {
  log(message: string): void;
}

class ConsoleLogger implements Logger {
  log(message: string): void {
    console.log(message);
  }
}

class FileLogger implements Logger {
  log(message: string): void {
    // Write to file
  }
}

class UserService {
  constructor(private logger: Logger) {}

  createUser(data: UserData): User {
    this.logger.log('Creating user...');
    // ...
  }
}

// Can inject any logger implementation
const service = new UserService(new ConsoleLogger());
```

**Bad:**
```typescript
class UserService {
  private logger = new ConsoleLogger(); // Tightly coupled

  createUser(data: UserData): User {
    this.logger.log('Creating user...');
    // Can't easily switch logger implementation
  }
}
```
