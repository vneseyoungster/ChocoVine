# Data Validation Security Checklist

## Input Validation Principles

### General Rules
- [ ] Validate on the server (never trust client validation)
- [ ] Validate type, length, format, and range
- [ ] Use allowlists over denylists
- [ ] Reject invalid input (don't sanitize and accept)
- [ ] Validate early (at API boundary)

### Validation Strategy
```
User Input
    ↓
Type Validation (string, number, boolean)
    ↓
Format Validation (email, URL, phone)
    ↓
Range Validation (min/max, allowed values)
    ↓
Business Rule Validation
    ↓
Sanitization (only if necessary)
    ↓
Use in Application
```

---

## Type Validation

### String Inputs
- [ ] Maximum length enforced
- [ ] Encoding validated (UTF-8)
- [ ] Null bytes rejected
- [ ] Control characters handled

```typescript
import { z } from 'zod';

const userInputSchema = z.object({
  name: z.string()
    .min(1, 'Name is required')
    .max(100, 'Name too long')
    .trim(),
  email: z.string()
    .email('Invalid email format')
    .max(255),
  age: z.number()
    .int('Age must be a whole number')
    .min(0, 'Age cannot be negative')
    .max(150, 'Invalid age'),
});
```

### Numeric Inputs
- [ ] Type is actually a number
- [ ] Within acceptable range
- [ ] No special values (Infinity, NaN)
- [ ] Precision appropriate for use case

```typescript
const numericSchema = z.object({
  quantity: z.number()
    .int()
    .min(1)
    .max(1000),
  price: z.number()
    .positive()
    .finite()
    .multipleOf(0.01), // Currency precision
});
```

### Boolean Inputs
- [ ] Actual boolean type
- [ ] Not truthy/falsy string

```typescript
// Bad - truthy string
const isAdmin = req.body.isAdmin; // Could be "false" (truthy!)

// Good - explicit boolean
const isAdmin = req.body.isAdmin === true;
```

### Array Inputs
- [ ] Maximum length enforced
- [ ] Each element validated
- [ ] No duplicate handling if required

```typescript
const arraySchema = z.array(z.string().max(100))
  .max(100, 'Too many items')
  .nonempty('At least one item required');
```

---

## Format Validation

### Email
```typescript
const emailSchema = z.string()
  .email()
  .max(255)
  .toLowerCase()
  .trim();

// Or with custom regex for stricter validation
const strictEmailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
```

### URL
```typescript
const urlSchema = z.string()
  .url()
  .refine((url) => {
    const parsed = new URL(url);
    return ['http:', 'https:'].includes(parsed.protocol);
  }, 'Only HTTP(S) URLs allowed');
```

### Phone Number
```typescript
import { parsePhoneNumber, isValidPhoneNumber } from 'libphonenumber-js';

const phoneSchema = z.string().refine(
  (val) => isValidPhoneNumber(val),
  'Invalid phone number'
);
```

### UUID
```typescript
const uuidSchema = z.string().uuid();

// Or regex
const UUID_REGEX = /^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i;
```

### Date/Time
```typescript
const dateSchema = z.string()
  .datetime() // ISO 8601 format
  .or(z.date());

// With range
const birthDateSchema = z.coerce.date()
  .min(new Date('1900-01-01'), 'Too old')
  .max(new Date(), 'Cannot be in future');
```

---

## Dangerous Patterns

### Path Traversal
```typescript
// Bad - allows ../../../etc/passwd
const filePath = `uploads/${req.params.filename}`;

// Good - validate and sanitize
import path from 'path';

function getSafeFilePath(filename: string, baseDir: string): string {
  // Remove path components
  const safeName = path.basename(filename);

  // Resolve full path
  const fullPath = path.resolve(baseDir, safeName);

  // Ensure still within base directory
  if (!fullPath.startsWith(path.resolve(baseDir))) {
    throw new Error('Invalid file path');
  }

  return fullPath;
}
```

### SQL Injection
```typescript
// Bad - string concatenation
const query = `SELECT * FROM users WHERE id = '${userId}'`;

// Good - parameterized query
const query = 'SELECT * FROM users WHERE id = $1';
const result = await db.query(query, [userId]);

// Good - ORM with parameter binding
const user = await User.findOne({ where: { id: userId } });
```

### XSS Prevention
```typescript
// Bad - direct HTML insertion
element.innerHTML = userInput;

// Good - text content (automatically escaped)
element.textContent = userInput;

// Good - template with auto-escaping (React, Vue, etc.)
<div>{userInput}</div>

// If HTML needed, use allowlist sanitizer
import DOMPurify from 'dompurify';
element.innerHTML = DOMPurify.sanitize(userInput, {
  ALLOWED_TAGS: ['b', 'i', 'em', 'strong', 'p'],
});
```

### Command Injection
```typescript
// Bad - shell command with user input
exec(`convert ${filename} output.png`);

// Good - use array arguments (no shell)
execFile('convert', [filename, 'output.png']);

// Better - avoid shell commands entirely
import sharp from 'sharp';
await sharp(filename).png().toFile('output.png');
```

---

## File Upload Validation

### File Type
- [ ] Validate MIME type from file header (not extension)
- [ ] Use allowlist of accepted types
- [ ] Reject executable files
- [ ] Check file signature (magic bytes)

```typescript
import fileType from 'file-type';

async function validateUpload(buffer: Buffer): Promise<boolean> {
  const type = await fileType.fromBuffer(buffer);

  const allowedTypes = ['image/jpeg', 'image/png', 'image/gif'];

  if (!type || !allowedTypes.includes(type.mime)) {
    throw new Error('Invalid file type');
  }

  return true;
}
```

### File Size
- [ ] Maximum size enforced before processing
- [ ] Limits appropriate for file type
- [ ] Memory usage monitored

```typescript
app.use(express.json({ limit: '100kb' }));

const upload = multer({
  limits: {
    fileSize: 5 * 1024 * 1024, // 5MB
    files: 5, // Maximum 5 files
  },
});
```

### File Name
- [ ] Sanitize filename
- [ ] Generate new filename (don't use original)
- [ ] No path components allowed

```typescript
import crypto from 'crypto';
import path from 'path';

function generateSafeFilename(originalName: string): string {
  const ext = path.extname(originalName).toLowerCase();
  const allowedExtensions = ['.jpg', '.jpeg', '.png', '.gif'];

  if (!allowedExtensions.includes(ext)) {
    throw new Error('Invalid file extension');
  }

  const randomName = crypto.randomBytes(16).toString('hex');
  return `${randomName}${ext}`;
}
```

---

## JSON Validation

### Structure
- [ ] Validate against schema
- [ ] Reject unknown properties (strict mode)
- [ ] Limit nesting depth
- [ ] Limit payload size

```typescript
const requestSchema = z.object({
  user: z.object({
    name: z.string(),
    email: z.string().email(),
  }),
  items: z.array(z.object({
    id: z.string().uuid(),
    quantity: z.number().int().positive(),
  })).max(100),
}).strict(); // Reject unknown properties

// Size limit at middleware level
app.use(express.json({ limit: '100kb' }));
```

### Parsing Safety
```typescript
// Limit JSON parsing depth (custom parser or library)
const MAX_DEPTH = 10;

function parseJSONSafely(json: string, maxDepth = MAX_DEPTH): unknown {
  let depth = 0;

  return JSON.parse(json, (key, value) => {
    if (typeof value === 'object' && value !== null) {
      depth++;
      if (depth > maxDepth) {
        throw new Error('JSON nesting too deep');
      }
    }
    return value;
  });
}
```

---

## Validation Libraries

### Recommended
- **Zod** - TypeScript-first schema validation
- **Yup** - JavaScript schema validation
- **Joi** - Powerful validation library
- **class-validator** - Decorator-based validation

### Example with Zod
```typescript
import { z } from 'zod';

const createUserSchema = z.object({
  email: z.string().email().max(255),
  password: z.string().min(8).max(100),
  name: z.string().min(1).max(100).optional(),
  role: z.enum(['user', 'admin']).default('user'),
});

type CreateUserInput = z.infer<typeof createUserSchema>;

async function createUser(input: unknown) {
  const validated = createUserSchema.parse(input);
  // validated is now type-safe CreateUserInput
}
```
