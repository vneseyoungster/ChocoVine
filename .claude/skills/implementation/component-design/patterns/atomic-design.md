# Atomic Design Pattern

Atomic Design is a methodology for creating design systems with five distinct levels.

## The Five Levels

### 1. Atoms
The smallest, indivisible UI elements.

**Examples:**
- Button
- Input
- Label
- Icon
- Badge
- Avatar

**Characteristics:**
- Cannot be broken down further
- No dependencies on other components
- Highly reusable
- Often map to HTML elements

```tsx
// atoms/Button.tsx
interface ButtonProps {
  variant?: 'primary' | 'secondary';
  size?: 'sm' | 'md' | 'lg';
  children: React.ReactNode;
  onClick?: () => void;
}

export function Button({ variant = 'primary', size = 'md', children, onClick }: ButtonProps) {
  return (
    <button className={`btn btn-${variant} btn-${size}`} onClick={onClick}>
      {children}
    </button>
  );
}
```

### 2. Molecules
Simple groups of atoms functioning together as a unit.

**Examples:**
- FormField (Label + Input + Error)
- SearchBox (Input + Button)
- MenuItem (Icon + Text)
- Card Header (Avatar + Name + Badge)

**Characteristics:**
- Combination of 2-4 atoms
- Single, simple function
- Reusable across different contexts

```tsx
// molecules/FormField.tsx
interface FormFieldProps {
  label: string;
  name: string;
  error?: string;
  children: React.ReactNode;
}

export function FormField({ label, name, error, children }: FormFieldProps) {
  return (
    <div className="form-field">
      <Label htmlFor={name}>{label}</Label>
      {children}
      {error && <ErrorText>{error}</ErrorText>}
    </div>
  );
}
```

### 3. Organisms
Complex UI sections composed of molecules and/or atoms.

**Examples:**
- Header (Logo + Navigation + UserMenu)
- LoginForm (multiple FormFields + Button)
- ProductCard (Image + Title + Price + Button)
- CommentSection (CommentForm + CommentList)

**Characteristics:**
- Self-contained sections of UI
- May have local state
- Can be context-specific
- May include business logic

```tsx
// organisms/LoginForm.tsx
export function LoginForm({ onSubmit }: LoginFormProps) {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  return (
    <form onSubmit={handleSubmit}>
      <FormField label="Email" name="email">
        <Input type="email" value={email} onChange={e => setEmail(e.target.value)} />
      </FormField>
      <FormField label="Password" name="password">
        <Input type="password" value={password} onChange={e => setPassword(e.target.value)} />
      </FormField>
      <Button type="submit">Login</Button>
    </form>
  );
}
```

### 4. Templates
Page-level layouts that define structure without specific content.

**Examples:**
- DashboardLayout
- AuthLayout
- SettingsLayout
- TwoColumnLayout

**Characteristics:**
- Define page structure
- Accept children/slots for content
- No specific content of their own
- Handle responsive layout

```tsx
// templates/DashboardLayout.tsx
interface DashboardLayoutProps {
  sidebar: React.ReactNode;
  header: React.ReactNode;
  children: React.ReactNode;
}

export function DashboardLayout({ sidebar, header, children }: DashboardLayoutProps) {
  return (
    <div className="dashboard-layout">
      <aside className="sidebar">{sidebar}</aside>
      <div className="main">
        <header className="header">{header}</header>
        <main className="content">{children}</main>
      </div>
    </div>
  );
}
```

### 5. Pages
Specific instances of templates with real content.

**Examples:**
- HomePage
- UserProfilePage
- SettingsPage
- CheckoutPage

**Characteristics:**
- Combine templates with real data
- Handle data fetching
- Manage page-level state
- Connect to routes

```tsx
// pages/DashboardPage.tsx
export function DashboardPage() {
  const { user } = useUser();
  const { data: stats } = useStats();

  return (
    <DashboardLayout
      sidebar={<DashboardNav user={user} />}
      header={<DashboardHeader title="Dashboard" />}
    >
      <StatsGrid stats={stats} />
      <RecentActivity />
    </DashboardLayout>
  );
}
```

## Directory Structure

```
src/
├── components/
│   ├── atoms/
│   │   ├── Button/
│   │   ├── Input/
│   │   └── ...
│   ├── molecules/
│   │   ├── FormField/
│   │   ├── SearchBox/
│   │   └── ...
│   ├── organisms/
│   │   ├── Header/
│   │   ├── LoginForm/
│   │   └── ...
│   └── templates/
│       ├── DashboardLayout/
│       └── ...
└── pages/
    ├── Dashboard/
    └── ...
```

## When to Use Each Level

| Need | Use |
|------|-----|
| Basic UI element | Atom |
| Simple combination | Molecule |
| Complex section | Organism |
| Page structure | Template |
| Specific page | Page |
