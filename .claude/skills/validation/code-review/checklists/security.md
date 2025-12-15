# Security Review Checklist

## Authentication

### Password Handling
- [ ] Passwords are hashed using bcrypt/argon2 (not MD5/SHA1)
- [ ] Password complexity requirements enforced
- [ ] Password reset flow is secure
- [ ] No passwords in logs or error messages

### Session Management
- [ ] Sessions expire after inactivity
- [ ] Session tokens are cryptographically random
- [ ] Sessions invalidated on logout
- [ ] Secure and HttpOnly cookie flags set

### Token Security
- [ ] JWTs have appropriate expiration
- [ ] Tokens stored securely (not localStorage for sensitive data)
- [ ] Refresh token rotation implemented
- [ ] Token revocation supported

## Authorization

### Access Control
- [ ] All endpoints require authentication (unless public)
- [ ] Authorization checks on all protected resources
- [ ] Deny by default principle applied
- [ ] Role-based access properly implemented

### Data Access
- [ ] Users can only access their own data
- [ ] Admin functions properly restricted
- [ ] No IDOR (Insecure Direct Object Reference) vulnerabilities
- [ ] Tenant isolation enforced (multi-tenant apps)

## Input Validation

### General Input
- [ ] All user input is validated
- [ ] Input length limits enforced
- [ ] Input type validation done
- [ ] Whitelist validation preferred over blacklist

### File Uploads
- [ ] File type validation (not just extension)
- [ ] File size limits enforced
- [ ] Files stored outside web root
- [ ] Malware scanning for uploads

## Output Encoding

### XSS Prevention
- [ ] All output HTML-encoded
- [ ] Context-appropriate encoding used
- [ ] User content sanitized before display
- [ ] Content-Security-Policy header set

### Response Headers
- [ ] X-Content-Type-Options: nosniff
- [ ] X-Frame-Options configured
- [ ] X-XSS-Protection enabled
- [ ] Referrer-Policy set

## Database Security

### Query Safety
- [ ] Parameterized queries used (no string concatenation)
- [ ] ORM used properly to prevent injection
- [ ] No raw SQL with user input
- [ ] Database errors don't leak sensitive info

### Data Protection
- [ ] Sensitive data encrypted at rest
- [ ] PII properly handled
- [ ] Database credentials not in code
- [ ] Backup encryption enabled

## Secrets Management

### Credential Storage
- [ ] No hardcoded secrets in code
- [ ] Environment variables for configuration
- [ ] Secrets in secure vault/service
- [ ] API keys properly scoped

### Code Repository
- [ ] .gitignore includes sensitive files
- [ ] No secrets in commit history
- [ ] Pre-commit hooks for secret detection
- [ ] Environment-specific configs separated

## API Security

### Request Validation
- [ ] Rate limiting implemented
- [ ] Request size limits set
- [ ] CORS properly configured
- [ ] API versioning in place

### Response Security
- [ ] Sensitive data not in URLs
- [ ] Error messages don't leak info
- [ ] Appropriate HTTP status codes
- [ ] No stack traces in production

## Logging & Monitoring

### Security Logging
- [ ] Authentication events logged
- [ ] Authorization failures logged
- [ ] Suspicious activity detected
- [ ] Logs don't contain sensitive data

### Incident Response
- [ ] Alerting configured
- [ ] Log retention policy defined
- [ ] Audit trail maintained
- [ ] Breach notification process exists

## Critical Patterns to Flag

### Immediate Action Required
```
Pattern: hardcoded credentials
Example: const password = "admin123"
Action: Remove immediately, rotate credential

Pattern: SQL injection vulnerability
Example: `SELECT * FROM users WHERE id = ${userId}`
Action: Use parameterized query

Pattern: XSS vulnerability
Example: innerHTML = userInput
Action: Use textContent or sanitize

Pattern: Missing authentication
Example: Public endpoint exposing sensitive data
Action: Add authentication middleware
```
