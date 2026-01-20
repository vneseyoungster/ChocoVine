# Dependency Sorting Reference

How to order phases so independent ones come first.

---

## The Core Algorithm

```
1. Build dependency graph
2. Calculate depth for each component
3. Sort: lowest depth first
4. Within same depth: foundational types first
```

---

## Step-by-Step Process

### Step 1: List Components

From architecture, extract all components:
```
- Config (environment, constants)
- Types (interfaces, schemas)
- Models (entities, validation)
- Services (business logic)
- Controllers (API routes)
- UI Components (frontend)
- Integration (E2E, hooks)
```

### Step 2: Build Dependency Matrix

For each component, list what it imports:

| Component | Imports |
|-----------|---------|
| Config | (nothing) |
| Types | (nothing) |
| Models | Types |
| Services | Models, Config |
| Controllers | Services, Models |
| UI Components | Services, Models, Types |
| Integration | Controllers, UI, Services |

### Step 3: Calculate Depth

**Depth = longest path to a component with no dependencies**

| Component | Depth | Calculation |
|-----------|-------|-------------|
| Config | 0 | No dependencies |
| Types | 0 | No dependencies |
| Models | 1 | Types (0) + 1 |
| Services | 2 | Models (1) + 1 |
| Controllers | 3 | Services (2) + 1 |
| UI Components | 3 | Services (2) + 1 |
| Integration | 4 | Controllers (3) + 1 |

### Step 4: Sort by Depth

```
Phase 1: Config, Types        (depth 0)
Phase 2: Models               (depth 1)
Phase 3: Services             (depth 2)
Phase 4: Controllers, UI      (depth 3)
Phase 5: Integration          (depth 4)
```

---

## Tiebreaker Rules

When components have same depth, order by:

1. **Configuration** first (env, constants)
2. **Types/Interfaces** second
3. **Data models** third
4. **Services** fourth
5. **Controllers/Routes** fifth
6. **UI Components** sixth
7. **Integration/E2E** last

---

## Quick Decision Tree

```
Is it configuration or types?
├── Yes → Phase 1 (top)
└── No → Does it have dependencies?
    ├── No → Phase 1-2 (top)
    └── Yes → How many?
        ├── 1-2 dependencies → Phase 2-3 (middle)
        └── 3+ dependencies → Phase 4+ (bottom)
```

---

## Common Patterns

### Web Application

```
Phase 1: Config, Types, Utils          # 0 deps
Phase 2: Database Models               # Types only
Phase 3: Services, Repositories        # Models
Phase 4: Controllers, Middleware       # Services
Phase 5: Frontend Components           # Services, Types
Phase 6: Integration, E2E              # Everything
```

### React Frontend

```
Phase 1: Types, Constants, Theme       # 0 deps
Phase 2: Hooks, Utils                  # Types only
Phase 3: Components (atoms)            # Theme, Types
Phase 4: Components (molecules)        # Atoms
Phase 5: Components (organisms)        # Molecules
Phase 6: Pages, Routes                 # Organisms
Phase 7: Integration Tests             # Everything
```

### API Service

```
Phase 1: Config, Types                 # 0 deps
Phase 2: Database, Models              # Config
Phase 3: Services                      # Models
Phase 4: Routes, Middleware            # Services
Phase 5: Integration, E2E              # Routes
```

---

## Parallel Execution Groups

Phases with same depth can run in parallel:

```
Parallel Group 1: Phase 1 (Config + Types)
Parallel Group 2: Phase 2 (Models)
Parallel Group 3: Phase 3 (Services)
Parallel Group 4: Phase 4 (Controllers) + Phase 5 (UI)
Sequential: Phase 6 (Integration) - must wait for all
```

---

## Red Flags

| Pattern | Problem | Fix |
|---------|---------|-----|
| Integration at top | Wrong order | Move to bottom |
| UI before services | Missing deps | Reorder |
| Circular deps | Architecture issue | Refactor |
| Everything in one phase | Too coupled | Split more |

---

## Example: Auth Feature

**Components identified:**
- JWT Config
- User types
- User model
- Auth service
- Auth controller
- Login UI
- Auth tests

**Dependency analysis:**
```
JWT Config     → (nothing)           depth: 0
User types     → (nothing)           depth: 0
User model     → User types          depth: 1
Auth service   → User model, Config  depth: 2
Auth controller→ Auth service        depth: 3
Login UI       → Auth service        depth: 3
Auth tests     → Controller, UI      depth: 4
```

**Final order:**
```
Phase 1: JWT Config, User Types     # Independent
Phase 2: User Model                 # Needs types
Phase 3: Auth Service               # Needs model
Phase 4: Auth Controller, Login UI  # Needs service
Phase 5: Auth Integration Tests     # Needs everything
```

---

## Checklist

Before finalizing phase order:
- [ ] All depth-0 components are in Phase 1
- [ ] No phase depends on a later phase
- [ ] Integration/E2E is always last
- [ ] Parallel groups are identified
- [ ] No circular dependencies
