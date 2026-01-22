# Code Patterns Rules

## When to Apply
- Creating new APIs
- Building React components
- Implementing data access

## Requirements

### API Response Format

```typescript
interface ApiResponse<T> {
  success: boolean;
  data?: T;
  error?: {
    code: string;
    message: string;
    details?: Record<string, unknown>;
  };
  meta?: {
    pagination?: {
      page: number;
      limit: number;
      total: number;
    };
  };
}
```

- [ ] All API responses follow this format
- [ ] Error codes are documented
- [ ] Pagination included for lists

### Custom Hooks Pattern

```typescript
function useResource<T>(resourceId: string) {
  const [data, setData] = useState<T | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<Error | null>(null);

  useEffect(() => {
    fetchResource(resourceId)
      .then(setData)
      .catch(setError)
      .finally(() => setLoading(false));
  }, [resourceId]);

  return { data, loading, error };
}
```

- [ ] Return object with data, loading, error
- [ ] Handle cleanup in useEffect
- [ ] Memoize callbacks with useCallback

### Repository Pattern

```typescript
interface Repository<T> {
  findById(id: string): Promise<T | null>;
  findAll(filter?: Partial<T>): Promise<T[]>;
  create(data: Omit<T, 'id'>): Promise<T>;
  update(id: string, data: Partial<T>): Promise<T>;
  delete(id: string): Promise<void>;
}
```

- [ ] Abstract data access behind interface
- [ ] Keep business logic out of repositories
- [ ] Use dependency injection

### Component Structure

```
ComponentName/
├── index.ts           # Export
├── ComponentName.tsx  # Component
├── ComponentName.test.tsx
├── ComponentName.styles.ts
└── types.ts           # Local types
```

## References
- `.claude/skills/implementation/api-design/`
- `.claude/skills/implementation/component-design/`
- `.claude/skills/implementation/component-design/patterns/`
