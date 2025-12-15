# Pull Request Template

Use this template when creating pull requests.

## Template

```markdown
## Description

[Provide a brief description of the changes in this PR]

## Type of Change

- [ ] Feature (new functionality)
- [ ] Bug fix (non-breaking fix)
- [ ] Refactor (code improvement without feature change)
- [ ] Documentation (docs only)
- [ ] Test (test additions or fixes)
- [ ] Chore (maintenance, dependencies)
- [ ] Breaking change (fix or feature that breaks existing functionality)

## Related Issues

- Closes #[issue_number]
- Related to #[issue_number]

## Changes Made

- [List specific changes]
- [Be concise but complete]
- [Group related changes]

## Testing

### How to Test

1. [Step-by-step testing instructions]
2. [Include any setup required]
3. [Specify expected outcomes]

### Test Coverage

- [ ] Unit tests added/updated
- [ ] Integration tests added/updated
- [ ] E2E tests added/updated (if applicable)
- [ ] Manual testing completed

## Screenshots (if applicable)

[Add screenshots for UI changes]

| Before | After |
|--------|-------|
| [image] | [image] |

## Checklist

### Code Quality
- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] No unnecessary comments or debug code
- [ ] Error handling implemented

### Testing
- [ ] All tests pass locally
- [ ] New code has adequate test coverage
- [ ] Edge cases considered

### Documentation
- [ ] README updated (if needed)
- [ ] API documentation updated (if needed)
- [ ] Inline comments added where necessary
- [ ] Changelog updated (if needed)

### Security
- [ ] No sensitive data exposed
- [ ] Input validation implemented
- [ ] Authentication/authorization checked

## Deployment Notes

[Any special deployment considerations or migrations required]

## Additional Context

[Any additional information reviewers should know]
```

## Example: Feature PR

```markdown
## Description

Implement JWT token refresh functionality to maintain user sessions without requiring re-login.

## Type of Change

- [x] Feature (new functionality)
- [ ] Bug fix
- [ ] Refactor
- [ ] Documentation
- [ ] Test
- [ ] Chore
- [ ] Breaking change

## Related Issues

- Closes #123
- Related to #100 (auth improvements epic)

## Changes Made

- Add `/auth/refresh` endpoint for token refresh
- Implement refresh token rotation for security
- Add token blacklist for revoked tokens
- Update auth middleware to handle expired tokens

## Testing

### How to Test

1. Login to get initial tokens
2. Wait for access token to expire (or manually expire it)
3. Make authenticated request - should auto-refresh
4. Verify new tokens are returned
5. Test logout invalidates refresh token

### Test Coverage

- [x] Unit tests added/updated
- [x] Integration tests added/updated
- [ ] E2E tests added/updated
- [x] Manual testing completed

## Checklist

### Code Quality
- [x] Code follows project style guidelines
- [x] Self-review completed
- [x] No unnecessary comments or debug code
- [x] Error handling implemented

### Testing
- [x] All tests pass locally
- [x] New code has adequate test coverage
- [x] Edge cases considered

### Documentation
- [x] README updated
- [x] API documentation updated
- [x] Inline comments added where necessary
- [ ] Changelog updated

### Security
- [x] No sensitive data exposed
- [x] Input validation implemented
- [x] Authentication/authorization checked

## Deployment Notes

- Run migration: `npm run migrate`
- Update environment variable: `REFRESH_TOKEN_SECRET`

## Additional Context

Token refresh follows RFC 6749 OAuth 2.0 spec. Refresh tokens are rotated on each use to prevent replay attacks.
```

## Tips for Good PRs

### Do
- Keep PRs focused on a single concern
- Write descriptive titles
- Include context for reviewers
- Respond to feedback promptly
- Add screenshots for UI changes

### Don't
- Don't create massive PRs (aim for < 400 lines)
- Don't mix refactoring with features
- Don't leave failing tests
- Don't forget to update docs
