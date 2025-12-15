# Component Composition Patterns

## 1. Compound Components

Create components that work together as a family, sharing implicit state.

### Example: Select Component
```tsx
const SelectContext = createContext<SelectContextValue | null>(null);

function Select({ children, value, onChange }: SelectProps) {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <SelectContext.Provider value={{ value, onChange, isOpen, setIsOpen }}>
      <div className="select">{children}</div>
    </SelectContext.Provider>
  );
}

function Trigger({ children }: { children: React.ReactNode }) {
  const { isOpen, setIsOpen } = useSelectContext();
  return (
    <button onClick={() => setIsOpen(!isOpen)}>
      {children}
    </button>
  );
}

function Content({ children }: { children: React.ReactNode }) {
  const { isOpen } = useSelectContext();
  if (!isOpen) return null;
  return <div className="select-content">{children}</div>;
}

function Item({ value, children }: ItemProps) {
  const { onChange, setIsOpen } = useSelectContext();
  return (
    <div onClick={() => { onChange(value); setIsOpen(false); }}>
      {children}
    </div>
  );
}

// Attach sub-components
Select.Trigger = Trigger;
Select.Content = Content;
Select.Item = Item;

// Usage
<Select value={selected} onChange={setSelected}>
  <Select.Trigger>Choose option</Select.Trigger>
  <Select.Content>
    <Select.Item value="a">Option A</Select.Item>
    <Select.Item value="b">Option B</Select.Item>
  </Select.Content>
</Select>
```

### When to Use
- Multi-part components (modals, dropdowns, tabs)
- Flexible child composition needed
- Shared state between related components

## 2. Render Props

Pass a function as children to control rendering.

### Example: Data Fetcher
```tsx
interface FetcherProps<T> {
  url: string;
  children: (state: { data: T | null; loading: boolean; error: Error | null }) => React.ReactNode;
}

function Fetcher<T>({ url, children }: FetcherProps<T>) {
  const [data, setData] = useState<T | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<Error | null>(null);

  useEffect(() => {
    fetch(url)
      .then(res => res.json())
      .then(setData)
      .catch(setError)
      .finally(() => setLoading(false));
  }, [url]);

  return <>{children({ data, loading, error })}</>;
}

// Usage
<Fetcher<User[]> url="/api/users">
  {({ data, loading, error }) => {
    if (loading) return <Spinner />;
    if (error) return <Error message={error.message} />;
    return <UserList users={data!} />;
  }}
</Fetcher>
```

### When to Use
- Sharing behavior without prescribing UI
- Flexible rendering control needed
- Cross-cutting concerns (auth, loading, error states)

## 3. Higher-Order Components (HOC)

Wrap components to enhance with additional behavior.

### Example: withAuth HOC
```tsx
function withAuth<P extends object>(Component: React.ComponentType<P>) {
  return function AuthenticatedComponent(props: P) {
    const { user, loading } = useAuth();

    if (loading) return <Spinner />;
    if (!user) return <Navigate to="/login" />;

    return <Component {...props} />;
  };
}

// Usage
const ProtectedDashboard = withAuth(Dashboard);
```

### When to Use
- Adding behavior to multiple components
- Cross-cutting concerns
- Legacy codebases (prefer hooks in new code)

## 4. Custom Hooks

Extract reusable logic into hooks.

### Example: useForm Hook
```tsx
function useForm<T extends Record<string, any>>(initialValues: T) {
  const [values, setValues] = useState(initialValues);
  const [errors, setErrors] = useState<Partial<Record<keyof T, string>>>({});
  const [touched, setTouched] = useState<Partial<Record<keyof T, boolean>>>({});

  const handleChange = (name: keyof T) => (e: React.ChangeEvent<HTMLInputElement>) => {
    setValues(prev => ({ ...prev, [name]: e.target.value }));
  };

  const handleBlur = (name: keyof T) => () => {
    setTouched(prev => ({ ...prev, [name]: true }));
  };

  const reset = () => {
    setValues(initialValues);
    setErrors({});
    setTouched({});
  };

  return { values, errors, touched, handleChange, handleBlur, setErrors, reset };
}

// Usage
function LoginForm() {
  const { values, handleChange, handleBlur } = useForm({ email: '', password: '' });

  return (
    <form>
      <input
        value={values.email}
        onChange={handleChange('email')}
        onBlur={handleBlur('email')}
      />
    </form>
  );
}
```

### When to Use
- Sharing stateful logic
- Complex state management
- Side effects

## 5. Slots Pattern

Named children for flexible layouts.

### Example: Card with Slots
```tsx
interface CardProps {
  header?: React.ReactNode;
  footer?: React.ReactNode;
  children: React.ReactNode;
}

function Card({ header, footer, children }: CardProps) {
  return (
    <div className="card">
      {header && <div className="card-header">{header}</div>}
      <div className="card-body">{children}</div>
      {footer && <div className="card-footer">{footer}</div>}
    </div>
  );
}

// Usage
<Card
  header={<h2>Title</h2>}
  footer={<Button>Action</Button>}
>
  <p>Content goes here</p>
</Card>
```

## Pattern Selection Guide

| Scenario | Pattern |
|----------|---------|
| Multi-part related components | Compound Components |
| Flexible rendering control | Render Props |
| Adding behavior to components | HOC (or hooks) |
| Sharing stateful logic | Custom Hooks |
| Flexible layouts | Slots |
