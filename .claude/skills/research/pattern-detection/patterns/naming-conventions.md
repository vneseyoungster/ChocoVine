# Naming Convention Patterns

## File Naming

### JavaScript/TypeScript
| Pattern | Example | Use Case |
|---------|---------|----------|
| kebab-case | `user-service.ts` | Most common, recommended |
| camelCase | `userService.ts` | Sometimes used |
| PascalCase | `UserService.ts` | React components, classes |

### Python
| Pattern | Example | Use Case |
|---------|---------|----------|
| snake_case | `user_service.py` | Standard Python convention |
| lowercase | `userservice.py` | Simple modules |

### Go
| Pattern | Example | Use Case |
|---------|---------|----------|
| lowercase | `userservice.go` | Standard Go convention |
| snake_case | `user_service.go` | Multi-word files |

## Variable Naming

### Constants
```javascript
// JavaScript/TypeScript
const MAX_RETRIES = 3;
const API_BASE_URL = '/api/v1';

// Python
MAX_RETRIES = 3
API_BASE_URL = '/api/v1'

// Go
const MaxRetries = 3
const apiBaseURL = "/api/v1"
```

### Variables
```javascript
// JavaScript/TypeScript
const userName = 'John';
const isActive = true;
const itemCount = 5;

// Python
user_name = 'John'
is_active = True
item_count = 5

// Go
userName := "John"
isActive := true
itemCount := 5
```

## Function Naming

### Actions
```javascript
// Verb + Noun pattern
getUserById(id)
createUser(data)
updateUserProfile(id, data)
deleteUser(id)
```

### Boolean Functions
```javascript
// is/has/can/should prefix
isValidEmail(email)
hasPermission(user, action)
canAccessResource(user, resource)
shouldRefreshToken(token)
```

### Event Handlers
```javascript
// on/handle prefix
onUserClick()
handleSubmit()
onInputChange()
handleError()
```

## Class/Type Naming

### Classes
```javascript
// PascalCase
class UserService {}
class AuthenticationManager {}
class DatabaseConnection {}
```

### Interfaces/Types
```typescript
// I-prefix (optional) or plain PascalCase
interface IUserRepository {}
interface UserRepository {}
type UserResponse = {}
type CreateUserDTO = {}
```

### Enums
```typescript
// PascalCase with SCREAMING_SNAKE values
enum UserStatus {
  ACTIVE = 'ACTIVE',
  INACTIVE = 'INACTIVE',
  PENDING = 'PENDING'
}
```

## Detection Queries

### Find File Naming Pattern
```bash
# List all source files
find src -type f -name "*.ts" -o -name "*.js" | head -20
```

### Find Variable Patterns
```bash
# Search for const declarations
grep -r "const [A-Z_]*\s*=" src/ | head -10
```

### Find Function Patterns
```bash
# Search for function declarations
grep -r "function\s\+\w\+" src/ | head -10
```
