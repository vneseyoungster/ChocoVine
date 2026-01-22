# Security Rules

## When to Apply
- Authentication/authorization code
- Data handling and storage
- API endpoint implementation
- User input processing

## Requirements

### Mandatory Checklist

- [ ] No secrets in code (use env vars)
- [ ] Input validation on all endpoints
- [ ] Output encoding for user content
- [ ] SQL parameterization (no string concat)
- [ ] HTTPS only for external calls
- [ ] Authentication on protected routes
- [ ] Rate limiting on public endpoints
- [ ] CORS configured correctly

### Secret Management

```typescript
// BAD
const apiKey = "sk-1234567890";

// GOOD
const apiKey = process.env.API_KEY;
if (!apiKey) throw new Error('API_KEY required');
```

### Input Validation

```typescript
// Always validate and sanitize
const input = sanitize(req.body.userInput);
const validated = schema.parse(input);
```

### SQL Safety

```typescript
// BAD - SQL Injection vulnerable
db.query(`SELECT * FROM users WHERE id = ${userId}`);

// GOOD - Parameterized
db.query('SELECT * FROM users WHERE id = ?', [userId]);
```

## Security Response Protocol

When vulnerability found:
1. **STOP** - Do not commit
2. **FIX** - Remediate immediately
3. **AUDIT** - Check for similar issues
4. **DOCUMENT** - Log the finding

## References
- `.claude/agents/validation/security-auditor.md`
- `.claude/skills/validation/security-scan/`
- `.claude/skills/validation/security-scan/checklists/owasp-top-10.md`
