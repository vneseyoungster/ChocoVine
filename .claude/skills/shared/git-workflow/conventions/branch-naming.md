# Branch Naming Conventions

## Format

```
<type>/<ticket>-<description>
```

Or without ticket:
```
<type>/<description>
```

## Branch Types

| Type | Purpose | Example |
|------|---------|---------|
| `feat` | New feature | `feat/AUTH-123-oauth-login` |
| `fix` | Bug fix | `fix/BUG-456-cart-total` |
| `refactor` | Code restructuring | `refactor/TECH-789-user-service` |
| `docs` | Documentation | `docs/update-api-docs` |
| `test` | Test additions | `test/add-checkout-tests` |
| `chore` | Maintenance | `chore/update-dependencies` |
| `hotfix` | Urgent production fix | `hotfix/critical-auth-bug` |
| `release` | Release preparation | `release/v2.1.0` |
| `experiment` | Experimental work | `experiment/new-caching-strategy` |

## Description Guidelines

### Do
- Use lowercase
- Use hyphens to separate words
- Keep it short but descriptive
- Include ticket number when available

### Don't
- Don't use spaces or underscores
- Don't use special characters
- Don't make it too long (aim for < 50 chars total)
- Don't use vague names like `fix-bug` or `update`

## Examples

### With Ticket Numbers
```
feat/AUTH-123-jwt-refresh-token
fix/BUG-456-login-redirect-loop
refactor/TECH-789-extract-validation
docs/DOC-101-api-authentication
```

### Without Ticket Numbers
```
feat/user-profile-avatar
fix/checkout-shipping-calculation
refactor/simplify-error-handling
chore/upgrade-node-version
```

### Special Branches
```
release/v2.0.0
hotfix/security-vulnerability
experiment/graphql-migration
```

## Protected Branches

These branches typically have special protections:

| Branch | Purpose | Protection |
|--------|---------|------------|
| `main` | Production code | No direct push, require PR |
| `develop` | Integration branch | No direct push, require PR |
| `release/*` | Release preparation | No direct push |

## Workflow Examples

### Feature Development
```bash
# Create feature branch
git checkout -b feat/AUTH-123-oauth-login

# Work on feature...
git commit -m "feat(auth): add OAuth2 provider config"
git commit -m "feat(auth): implement OAuth callback"

# Push and create PR
git push -u origin feat/AUTH-123-oauth-login
```

### Bug Fix
```bash
# Create fix branch
git checkout -b fix/BUG-456-cart-total

# Fix the bug
git commit -m "fix(cart): correct discount calculation"

# Push and create PR
git push -u origin fix/BUG-456-cart-total
```

### Hotfix (Urgent)
```bash
# Create hotfix from main
git checkout main
git checkout -b hotfix/critical-auth-bug

# Apply fix
git commit -m "fix(auth): patch session vulnerability"

# Push immediately
git push -u origin hotfix/critical-auth-bug
```

## Branch Cleanup

After merge, delete feature branches:
```bash
# Delete local branch
git branch -d feat/AUTH-123-oauth-login

# Delete remote branch
git push origin --delete feat/AUTH-123-oauth-login
```
