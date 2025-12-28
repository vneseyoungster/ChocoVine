# Initialize New Codebase

Initialize a new project codebase: $ARGUMENTS

## Overview

This command initializes a new codebase by gathering project requirements through interactive questions, then creating the appropriate folder structure, configuration files, and documentation templates tailored to the user's tech stack and preferences.

---

## Phase 1: Create Initialization Session

### Create Session Directory
```
plans/sessions/{date}-initialize/
├── session.md         # Initialization tracking
├── answers/           # User responses
│   ├── project-info.md
│   ├── tech-stack.md
│   ├── preferences.md
│   └── architecture.md
└── generated/         # Generated configurations
    ├── structure.md   # Final project structure
    └── configs.md     # Configuration summary
```

### Session File Template
```markdown
# Session: Project Initialization

**Started:** {date}
**Project Name:** {to be determined}
**Current Phase:** 🔍 Gathering Information

## Progress
- [ ] Project information gathered
- [ ] Tech stack selected
- [ ] Code preferences defined
- [ ] Architecture decisions made
- [ ] Project structure created
- [ ] Configuration files generated
- [ ] Documentation initialized
- [ ] CLAUDE.md updated

## User Responses Summary
{to be filled during initialization}
```

---

## Phase 2: Gather Project Information

### 2.1 Basic Project Information

**Ask the user:**

```
📋 PROJECT INFORMATION

1. What is your project name?

2. Brief description of the project (1-2 sentences):

3. What type of project is this?
   - [ ] Web Application (Frontend + Backend)
   - [ ] Frontend Only (SPA/Static site)
   - [ ] Backend/API Only
   - [ ] Full-Stack Monorepo
   - [ ] Mobile Application
   - [ ] Desktop Application
   - [ ] CLI Tool
   - [ ] Library/Package
   - [ ] Microservices
   - [ ] Other: ___

4. What is the primary purpose?
   - [ ] SaaS Product
   - [ ] E-commerce
   - [ ] Content/Blog
   - [ ] Dashboard/Admin Panel
   - [ ] Internal Tool
   - [ ] Open Source Library
   - [ ] Learning/Experiment
   - [ ] Client Project
   - [ ] Other: ___
```

**Store responses:** `plans/sessions/{session}/answers/project-info.md`

---

### 2.2 Tech Stack Selection

**Ask the user:**

```
🛠️ TECH STACK SELECTION

## Programming Language
Primary language:
- [ ] TypeScript
- [ ] JavaScript
- [ ] Python
- [ ] Go
- [ ] Rust
- [ ] Java
- [ ] C#
- [ ] PHP
- [ ] Ruby
- [ ] Other: ___

## Frontend (if applicable)
Framework:
- [ ] React
- [ ] Next.js
- [ ] Vue.js
- [ ] Nuxt.js
- [ ] Angular
- [ ] Svelte/SvelteKit
- [ ] Astro
- [ ] Remix
- [ ] None/Vanilla
- [ ] Other: ___

Styling:
- [ ] Tailwind CSS
- [ ] CSS Modules
- [ ] Styled Components
- [ ] Sass/SCSS
- [ ] CSS-in-JS (Emotion, etc.)
- [ ] Plain CSS
- [ ] Other: ___

UI Components:
- [ ] shadcn/ui
- [ ] Material UI
- [ ] Chakra UI
- [ ] Ant Design
- [ ] Headless UI
- [ ] Radix UI
- [ ] None/Custom
- [ ] Other: ___

## Backend (if applicable)
Framework:
- [ ] Express.js
- [ ] Fastify
- [ ] NestJS
- [ ] Hono
- [ ] Django
- [ ] FastAPI
- [ ] Flask
- [ ] Spring Boot
- [ ] ASP.NET
- [ ] Laravel
- [ ] Ruby on Rails
- [ ] Gin (Go)
- [ ] Actix (Rust)
- [ ] None/Serverless
- [ ] Other: ___

## Database (if applicable)
Type:
- [ ] PostgreSQL
- [ ] MySQL
- [ ] MongoDB
- [ ] SQLite
- [ ] Redis
- [ ] Supabase
- [ ] Firebase
- [ ] PlanetScale
- [ ] DynamoDB
- [ ] None
- [ ] Other: ___

ORM/Query Builder:
- [ ] Prisma
- [ ] Drizzle
- [ ] TypeORM
- [ ] Sequelize
- [ ] Mongoose
- [ ] SQLAlchemy
- [ ] Django ORM
- [ ] None/Raw SQL
- [ ] Other: ___

## Authentication (if applicable)
- [ ] NextAuth.js/Auth.js
- [ ] Clerk
- [ ] Auth0
- [ ] Supabase Auth
- [ ] Firebase Auth
- [ ] Passport.js
- [ ] Custom JWT
- [ ] None
- [ ] Other: ___
```

**Store responses:** `plans/sessions/{session}/answers/tech-stack.md`

---

### 2.3 Development Preferences

**Ask the user:**

```
⚙️ DEVELOPMENT PREFERENCES

## Package Manager
- [ ] npm
- [ ] yarn
- [ ] pnpm
- [ ] bun

## Code Quality
Linting:
- [ ] ESLint
- [ ] Biome
- [ ] Standard
- [ ] None

Formatting:
- [ ] Prettier
- [ ] Biome
- [ ] EditorConfig only
- [ ] None

Type Checking:
- [ ] TypeScript (strict)
- [ ] TypeScript (loose)
- [ ] JSDoc types
- [ ] None

## Testing
Unit Testing:
- [ ] Jest
- [ ] Vitest
- [ ] Mocha
- [ ] pytest
- [ ] None

E2E Testing:
- [ ] Playwright
- [ ] Cypress
- [ ] Selenium
- [ ] None

## Git Workflow
Branching Strategy:
- [ ] GitFlow (main/develop/feature)
- [ ] GitHub Flow (main/feature)
- [ ] Trunk-Based
- [ ] Custom

Commit Style:
- [ ] Conventional Commits
- [ ] Gitmoji
- [ ] Free-form
- [ ] Custom

## CI/CD (if applicable)
- [ ] GitHub Actions
- [ ] GitLab CI
- [ ] CircleCI
- [ ] Jenkins
- [ ] Vercel
- [ ] Netlify
- [ ] None yet
- [ ] Other: ___

## Deployment Target (if applicable)
- [ ] Vercel
- [ ] Netlify
- [ ] AWS
- [ ] Google Cloud
- [ ] Azure
- [ ] DigitalOcean
- [ ] Railway
- [ ] Fly.io
- [ ] Docker/Kubernetes
- [ ] Self-hosted
- [ ] Not decided
- [ ] Other: ___
```

**Store responses:** `plans/sessions/{session}/answers/preferences.md`

---

### 2.4 Architecture Preferences

**Ask the user:**

```
🏗️ ARCHITECTURE PREFERENCES

## Code Organization
Project Structure:
- [ ] Feature-based (by domain/feature)
- [ ] Layer-based (controllers/services/repos)
- [ ] Hybrid
- [ ] Monorepo (multiple packages)
- [ ] Not sure (recommend based on project type)

## State Management (Frontend)
- [ ] React Context
- [ ] Redux/Redux Toolkit
- [ ] Zustand
- [ ] Jotai
- [ ] Recoil
- [ ] MobX
- [ ] TanStack Query only
- [ ] None/Props drilling
- [ ] Not applicable
- [ ] Other: ___

## API Style (Backend)
- [ ] REST
- [ ] GraphQL
- [ ] tRPC
- [ ] gRPC
- [ ] Hybrid
- [ ] Not applicable

## Error Handling
- [ ] Centralized error handler
- [ ] Per-route/function
- [ ] Result types (Rust-style)
- [ ] Not sure (recommend)

## Logging
- [ ] Winston
- [ ] Pino
- [ ] Morgan
- [ ] Console only
- [ ] Cloud logging service
- [ ] Not sure (recommend)
- [ ] Other: ___

## Environment Management
- [ ] dotenv (.env files)
- [ ] Environment variables only
- [ ] Config service (Vault, etc.)
- [ ] Not sure (recommend)

## Documentation Preferences
- [ ] JSDoc/TSDoc comments
- [ ] Markdown docs
- [ ] Storybook (for components)
- [ ] OpenAPI/Swagger (for APIs)
- [ ] Minimal
- [ ] All of the above
```

**Store responses:** `plans/sessions/{session}/answers/architecture.md`

---

## Phase 3: Generate Project Structure

Based on user responses, generate appropriate structure.

### 3.1 Create Base Directories

**For Web Application (Full-Stack):**
```
{project-name}/
├── src/
│   ├── app/              # Next.js app router OR main app
│   ├── components/       # Reusable UI components
│   │   ├── ui/          # Base UI components
│   │   └── features/    # Feature-specific components
│   ├── lib/             # Utility functions
│   ├── hooks/           # Custom React hooks
│   ├── services/        # API services
│   ├── stores/          # State management
│   ├── types/           # TypeScript types
│   └── styles/          # Global styles
├── server/              # Backend code (if separate)
│   ├── api/            # API routes
│   ├── services/       # Business logic
│   ├── models/         # Data models
│   └── middleware/     # Express/Fastify middleware
├── prisma/              # Database schema (if Prisma)
├── tests/               # Test files
│   ├── unit/
│   ├── integration/
│   └── e2e/
├── docs/                # Documentation
├── scripts/             # Build/deploy scripts
├── .claude/             # Claude Code configuration
│   ├── commands/       # Slash commands
│   ├── agents/         # Agent definitions
│   └── skills/         # Custom skills
└── plans/               # Planning artifacts
```

**For Backend/API Only:**
```
{project-name}/
├── src/
│   ├── api/             # Route handlers
│   │   └── v1/         # API versioning
│   ├── services/        # Business logic
│   ├── models/          # Data models
│   ├── middleware/      # Middleware
│   ├── utils/           # Utilities
│   ├── types/           # TypeScript types
│   └── config/          # Configuration
├── prisma/              # Database (if applicable)
├── tests/
├── docs/
├── scripts/
├── .claude/
└── plans/
```

**For Frontend Only:**
```
{project-name}/
├── src/
│   ├── app/             # Pages/routes
│   ├── components/
│   │   ├── ui/
│   │   ├── layout/
│   │   └── features/
│   ├── hooks/
│   ├── lib/
│   ├── services/        # API clients
│   ├── stores/
│   ├── types/
│   └── styles/
├── public/              # Static assets
├── tests/
├── docs/
├── .claude/
└── plans/
```

**For Library/Package:**
```
{project-name}/
├── src/
│   ├── index.ts         # Main export
│   ├── core/            # Core functionality
│   ├── utils/           # Utilities
│   └── types/           # Type definitions
├── tests/
├── docs/
├── examples/            # Usage examples
├── .claude/
└── plans/
```

**For CLI Tool:**
```
{project-name}/
├── src/
│   ├── index.ts         # Entry point
│   ├── commands/        # CLI commands
│   ├── lib/             # Core logic
│   ├── utils/           # Utilities
│   └── types/
├── tests/
├── docs/
├── .claude/
└── plans/
```

---

### 3.2 Generate Configuration Files

Based on tech stack selection, generate:

**Package.json:**
- Project name, description
- Scripts for dev, build, test, lint
- Dependencies based on selections

**TypeScript Config (if TypeScript):**
- Strict mode based on preference
- Path aliases
- Target based on runtime

**ESLint/Biome Config:**
- Rules based on framework
- Integration with Prettier/TypeScript

**Prettier Config (if selected):**
- Tab width, semicolons, quotes
- Framework-specific settings

**Git Configuration:**
- .gitignore based on tech stack
- Commit hooks (if conventional commits)

**Environment Template:**
- .env.example with common variables
- Documentation for each variable

**Docker (if applicable):**
- Dockerfile
- docker-compose.yml

---

### 3.3 Generate Claude Configuration

**Update CLAUDE.md:**
```markdown
## Project-Specific Information

### Tech Stack
- Language: {selected language}
- Framework: {selected framework}
- Database: {selected database}
- Testing: {selected test framework}

### Key Directories
- Source code: src/
- Tests: tests/
- Configuration: config/ or root
- Documentation: docs/

### Build Commands
{generated based on package manager and framework}

### Code Conventions
- {based on architecture preferences}
- Follow existing codebase conventions
- Use git-workflow skill for commits and branches

### Environment Setup
{generated based on tech stack}
```

**Create .claude/settings.local.json:**
```json
{
  "project": {
    "name": "{project-name}",
    "type": "{project-type}",
    "language": "{primary-language}",
    "framework": "{main-framework}"
  }
}
```

---

## Phase 4: Initialize Documentation

### Create Initial Documentation Structure

```
docs/
├── README.md                    # Project overview
├── architecture/
│   └── decisions/              # Architecture Decision Records
│       └── 001-initial-setup.md
├── setup/
│   ├── installation.md         # Setup instructions
│   ├── configuration.md        # Config guide
│   └── development.md          # Dev workflow
├── api/                        # API docs (if applicable)
├── guides/                     # Developer guides
└── contributing.md             # Contribution guide
```

### Generate Initial README
```markdown
# {Project Name}

{Project description}

## Tech Stack

- **Language:** {language}
- **Framework:** {framework}
- **Database:** {database}
- **Testing:** {test framework}

## Quick Start

### Prerequisites
{based on tech stack}

### Installation
{based on package manager}

### Development
{based on framework}

## Project Structure
{generated structure overview}

## Scripts
{available npm/yarn/pnpm scripts}

## Documentation
- [Architecture](./docs/architecture/)
- [Setup Guide](./docs/setup/)
- [API Reference](./docs/api/)

## Contributing
See [CONTRIBUTING.md](./docs/contributing.md)

## License
{to be specified}
```

---

## Phase 5: Final Setup

### 5.1 Initialize Git Repository (if not exists)
```bash
git init
git add .
git commit -m "Initial project setup"
```

### 5.2 Install Dependencies
Based on package manager preference:
```bash
npm install    # or yarn/pnpm/bun
```

### 5.3 Verify Setup
- Run linting
- Run type checking
- Run test suite (should have placeholder test)
- Start development server

---

## Phase 6: Present Summary

```
✅ PROJECT INITIALIZED SUCCESSFULLY

## Project Profile
- Name: {project-name}
- Type: {project-type}
- Language: {language}
- Framework: {framework}

## Created Structure
{list of created directories}

## Generated Files
- [ ] package.json
- [ ] tsconfig.json (if TypeScript)
- [ ] .eslintrc / biome.json
- [ ] .prettierrc (if Prettier)
- [ ] .gitignore
- [ ] .env.example
- [ ] CLAUDE.md (updated)
- [ ] README.md

## Next Steps
1. Review generated configuration files
2. Update .env with your values
3. Run `{package-manager} install`
4. Start development with `{package-manager} run dev`
5. Use `/research` to plan your first feature

## Recommendations
- {based on project type and tech stack}
```

---

## Error Handling

### If project already initialized
```
⚠️ Project appears to already be initialized.
Detected: package.json, existing src/ directory

Options:
1. Proceed anyway (will merge/update configurations)
2. Cancel and use /project-scan instead
3. Reset and start fresh (destructive)

What would you like to do?
```

### If conflicting selections
```
⚠️ Potential conflict detected:
- Selected: {option A}
- Selected: {option B}
- Issue: {explanation}

Recommendation: {suggested resolution}
Proceed anyway? (y/n)
```

### If unknown framework/tool
```
ℹ️ Custom selection: {user input}
I'll create a generic structure. You may need to:
- Adjust configurations manually
- Add framework-specific files
- Update build scripts
```

---

## Example Usage

```
/initialize
/initialize my-awesome-app
/initialize Create a Next.js e-commerce app
/initialize Set up a Python FastAPI backend
```

---

## Phase Indicators

- 🔍 Gathering Information
- 📝 Generating Structure
- ⚙️ Creating Configurations
- 📚 Initializing Documentation
- ✅ Complete

---

## Completion Checklist

On completion:
1. All user questions answered and stored
2. Project structure created
3. Configuration files generated
4. CLAUDE.md updated with project specifics
5. Initial documentation created
6. Git initialized (if requested)
7. Summary presented to user
8. Next steps provided
