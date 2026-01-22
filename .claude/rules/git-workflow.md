# Git Workflow Rules

## When to Apply
- Creating commits
- Opening pull requests
- Branch management

## Requirements

### Commit Message Format

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation only
- `style`: Formatting, no code change
- `refactor`: Code restructure
- `test`: Adding tests
- `chore`: Maintenance

**Example:**
```
feat(auth): add OAuth2 login support

- Add Google OAuth provider
- Store tokens securely
- Add logout functionality

Closes #123
```

### PR Workflow

- [ ] Branch from main/dev
- [ ] Keep PRs focused (< 400 lines ideal)
- [ ] Write clear description
- [ ] Link related issues
- [ ] Request appropriate reviewers
- [ ] Pass CI checks before merge

### Feature Implementation Flow

```
1. Create branch: git checkout -b feat/feature-name
2. Implement with atomic commits
3. Push and create PR
4. Address review feedback
5. Squash merge when approved
```

### Branch Naming

```
feat/add-user-auth
fix/login-redirect-bug
refactor/api-response-format
docs/api-documentation
```

## Pre-commit Checks

```bash
npm run lint && npm run typecheck && npm test
```

## References
- `.claude/skills/shared/git-workflow/`
- `.claude/skills/shared/git-workflow/conventions/commit-messages.md`
- `.claude/skills/shared/git-workflow/conventions/pr-template.md`
