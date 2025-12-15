# State Management Patterns

## Decision Tree

Use this flowchart to decide where to manage state:

```
Is this state used by only one component?
├── YES → useState in that component
└── NO → Is it used by parent and children?
    ├── YES → useState in parent, pass down
    └── NO → Is it used by siblings?
        ├── YES → Lift to common ancestor
        └── NO → Is it used across the app?
            ├── YES (UI state) → Context or global store
            └── YES (server state) → React Query/SWR
```

## 1. Local State (useState)

For UI state used by a single component.

```tsx
function Counter() {
  const [count, setCount] = useState(0);
  return (
    <button onClick={() => setCount(c => c + 1)}>
      Count: {count}
    </button>
  );
}
```

**Use for:**
- Form inputs
- Toggle states
- Local UI state

## 2. Complex Local State (useReducer)

For complex state logic with multiple sub-values.

```tsx
type State = { count: number; step: number };
type Action =
  | { type: 'increment' }
  | { type: 'decrement' }
  | { type: 'setStep'; payload: number };

function reducer(state: State, action: Action): State {
  switch (action.type) {
    case 'increment':
      return { ...state, count: state.count + state.step };
    case 'decrement':
      return { ...state, count: state.count - state.step };
    case 'setStep':
      return { ...state, step: action.payload };
  }
}

function Counter() {
  const [state, dispatch] = useReducer(reducer, { count: 0, step: 1 });
  // ...
}
```

**Use for:**
- Multiple related state values
- Complex state transitions
- When next state depends on previous

## 3. Lifted State

Share state between siblings by lifting to parent.

```tsx
function Parent() {
  const [selected, setSelected] = useState<string | null>(null);

  return (
    <div>
      <ItemList items={items} selected={selected} onSelect={setSelected} />
      <ItemDetail itemId={selected} />
    </div>
  );
}
```

**Use for:**
- Sibling communication
- Parent-child sync

## 4. Context (Global UI State)

For state needed across many components.

```tsx
// ThemeContext.tsx
const ThemeContext = createContext<ThemeContextValue | null>(null);

export function ThemeProvider({ children }: { children: React.ReactNode }) {
  const [theme, setTheme] = useState<'light' | 'dark'>('light');

  const toggle = useCallback(() => {
    setTheme(t => t === 'light' ? 'dark' : 'light');
  }, []);

  return (
    <ThemeContext.Provider value={{ theme, toggle }}>
      {children}
    </ThemeContext.Provider>
  );
}

export function useTheme() {
  const context = useContext(ThemeContext);
  if (!context) throw new Error('useTheme must be within ThemeProvider');
  return context;
}

// Usage anywhere in app
function ThemeToggle() {
  const { theme, toggle } = useTheme();
  return <button onClick={toggle}>{theme}</button>;
}
```

**Use for:**
- Theme
- Locale/i18n
- Authentication state
- Feature flags

**Avoid for:**
- Frequently changing data (causes re-renders)
- Server state (use React Query instead)

## 5. Server State (React Query / SWR)

For data from external sources.

```tsx
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';

function UserList() {
  const { data: users, isLoading, error } = useQuery({
    queryKey: ['users'],
    queryFn: () => fetch('/api/users').then(r => r.json())
  });

  if (isLoading) return <Spinner />;
  if (error) return <Error />;
  return <ul>{users.map(u => <li key={u.id}>{u.name}</li>)}</ul>;
}

function CreateUser() {
  const queryClient = useQueryClient();
  const mutation = useMutation({
    mutationFn: (data: NewUser) =>
      fetch('/api/users', { method: 'POST', body: JSON.stringify(data) }),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['users'] });
    }
  });
  // ...
}
```

**Use for:**
- API data
- Any external data source
- Data that needs caching/revalidation

**Benefits:**
- Automatic caching
- Background refetching
- Optimistic updates
- Error retry

## 6. Global Store (Zustand / Redux)

For complex global state beyond Context.

```tsx
// With Zustand
import { create } from 'zustand';

interface CartStore {
  items: CartItem[];
  addItem: (item: CartItem) => void;
  removeItem: (id: string) => void;
  clear: () => void;
}

const useCartStore = create<CartStore>((set) => ({
  items: [],
  addItem: (item) => set((state) => ({ items: [...state.items, item] })),
  removeItem: (id) => set((state) => ({
    items: state.items.filter(i => i.id !== id)
  })),
  clear: () => set({ items: [] })
}));

// Usage
function Cart() {
  const { items, removeItem } = useCartStore();
  // ...
}
```

**Use for:**
- Complex app-wide state
- State with complex update logic
- When Context re-renders are problematic

## Summary Table

| State Type | Solution | Example |
|------------|----------|---------|
| Single component | useState | Form input |
| Complex local | useReducer | Multi-step form |
| Parent-child | Lifted state | List + Detail |
| App-wide UI | Context | Theme, Auth |
| Server data | React Query | API data |
| Complex global | Zustand/Redux | Shopping cart |
