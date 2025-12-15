# Commit Message Conventions

## Format

```
<type>(<scope>): <subject>

[optional body]

[optional footer]
```

### Header (Required)
- **type**: Category of change (see types below)
- **scope**: Module/component affected (optional but recommended)
- **subject**: Short description in imperative mood

### Body (Optional)
- Explain what and why, not how
- Use bullet points for multiple changes
- Wrap at 72 characters

### Footer (Optional)
- Reference issues: `Closes #123`, `Fixes #456`
- Breaking changes: `BREAKING CHANGE: description`
- Co-authors: `Co-authored-by: Name <email>`

## Types

| Type | Description | Example |
|------|-------------|---------|
| `feat` | New feature | `feat(auth): add OAuth2 login` |
| `fix` | Bug fix | `fix(cart): correct total calculation` |
| `refactor` | Code change without feature/fix | `refactor(api): simplify error handling` |
| `docs` | Documentation only | `docs(readme): update installation steps` |
| `test` | Add/modify tests | `test(user): add registration tests` |
| `chore` | Maintenance tasks | `chore(deps): update dependencies` |
| `perf` | Performance improvement | `perf(query): optimize user lookup` |
| `style` | Formatting, whitespace | `style(lint): fix indentation` |
| `ci` | CI/CD changes | `ci(github): add test workflow` |
| `build` | Build system changes | `build(webpack): update config` |
| `revert` | Revert previous commit | `revert: feat(auth): add OAuth2 login` |

## Examples

### Simple Feature
```
feat(user): add email verification

Implement email verification flow for new user registration.
```

### Bug Fix with Issue Reference
```
fix(checkout): prevent double submission

Add loading state to prevent multiple form submissions
during checkout process.

Fixes #234
```

### Refactoring
```
refactor(api): extract validation logic

- Move validation to separate module
- Add reusable validation helpers
- Update affected endpoints
```

### Breaking Change
```
feat(api): change response format to JSON:API

BREAKING CHANGE: API responses now follow JSON:API spec.
Clients need to update response parsing.

Migration guide: docs/migration/v2.md
```

### Multiple Co-authors
```
feat(dashboard): add analytics widget

Implement real-time analytics widget with charts.

Co-authored-by: Alice <alice@example.com>
Co-authored-by: Bob <bob@example.com>
```

## Subject Line Guidelines

### Do
- Use imperative mood: "add feature" not "added feature"
- Keep under 50 characters
- Start with lowercase
- No period at the end

### Don't
- Don't describe the code changes (that's what the diff is for)
- Don't include ticket numbers in subject (use footer)
- Don't use vague terms like "update" or "fix stuff"

## Scope Suggestions

Common scopes by project area:
- **Frontend**: `ui`, `components`, `styles`, `hooks`
- **Backend**: `api`, `auth`, `db`, `services`
- **Infrastructure**: `ci`, `docker`, `k8s`, `terraform`
- **Documentation**: `readme`, `api-docs`, `changelog`
