# OWASP Top 10 Security Checklist

## Overview

The OWASP Top 10 is a standard awareness document for developers and web application security. It represents a broad consensus about the most critical security risks to web applications.

---

## A01:2021 - Broken Access Control

Access control enforces policy such that users cannot act outside of their intended permissions.

### Checklist

- [ ] Deny access by default (except for public resources)
- [ ] Implement access control mechanisms once and reuse
- [ ] Model access controls enforce record ownership
- [ ] Disable web server directory listing
- [ ] Log access control failures and alert admins
- [ ] Rate limit API and controller access
- [ ] Invalidate sessions on logout
- [ ] JWT tokens invalidated after logout

### Common Vulnerabilities

```
Vulnerability: IDOR (Insecure Direct Object Reference)
Bad:  GET /api/users/123/profile  (no ownership check)
Good: Check user.id === requestedId || user.isAdmin

Vulnerability: Missing function level access control
Bad:  /admin/users endpoint accessible to regular users
Good: @RequireRole('admin') decorator on admin routes

Vulnerability: CORS misconfiguration
Bad:  Access-Control-Allow-Origin: *
Good: Access-Control-Allow-Origin: https://trusted-domain.com
```

---

## A02:2021 - Cryptographic Failures

Failures related to cryptography which often leads to sensitive data exposure.

### Checklist

- [ ] Classify data processed/stored/transmitted
- [ ] Don't store sensitive data unnecessarily
- [ ] Encrypt all sensitive data at rest
- [ ] Use strong standard algorithms and protocols
- [ ] Encrypt all data in transit with TLS
- [ ] Disable caching for sensitive data
- [ ] Use proper key management
- [ ] Use authenticated encryption (AEAD)

### Common Vulnerabilities

```
Vulnerability: Weak password hashing
Bad:  md5(password) or sha1(password)
Good: bcrypt(password, saltRounds: 12) or argon2

Vulnerability: Sensitive data in URL
Bad:  /reset-password?token=secret123
Good: POST /reset-password with token in body

Vulnerability: Missing HTTPS
Bad:  http://api.example.com
Good: https://api.example.com with HSTS
```

---

## A03:2021 - Injection

Injection flaws occur when untrusted data is sent to an interpreter.

### Checklist

- [ ] Use parameterized queries / prepared statements
- [ ] Use positive server-side input validation
- [ ] Escape special characters
- [ ] Use LIMIT to prevent mass disclosure
- [ ] Use ORMs with parameterization
- [ ] Avoid dynamic queries with user input

### Common Vulnerabilities

```
Vulnerability: SQL Injection
Bad:  `SELECT * FROM users WHERE id = ${userId}`
Good: `SELECT * FROM users WHERE id = $1`, [userId]

Vulnerability: NoSQL Injection
Bad:  { username: req.body.username }
Good: { username: String(req.body.username) }

Vulnerability: Command Injection
Bad:  exec(`convert ${filename}`)
Good: execFile('convert', [filename])

Vulnerability: XSS (Cross-Site Scripting)
Bad:  element.innerHTML = userInput
Good: element.textContent = userInput
```

---

## A04:2021 - Insecure Design

Insecure design is a broad category representing design and architectural flaws.

### Checklist

- [ ] Establish secure development lifecycle
- [ ] Use secure design patterns
- [ ] Threat modeling for critical flows
- [ ] Integration tests for abuse cases
- [ ] Segregate tenants by design
- [ ] Limit resource consumption per user/service

### Best Practices

- Use reference architectures
- Conduct design reviews
- Create threat models for new features
- Build abuse case stories alongside user stories
- Implement defense in depth

---

## A05:2021 - Security Misconfiguration

Security misconfiguration is commonly a result of insecure default configurations.

### Checklist

- [ ] Remove/disable unused features
- [ ] Review cloud storage permissions
- [ ] Security headers configured correctly
- [ ] Error handling doesn't expose details
- [ ] Disable XML external entity processing
- [ ] Disable unnecessary HTTP methods
- [ ] Configure CORS properly

### Common Vulnerabilities

```
Vulnerability: Default credentials
Action: Change all default passwords immediately

Vulnerability: Directory listing enabled
Action: Disable in web server configuration

Vulnerability: Verbose errors in production
Bad:  { error: stack_trace }
Good: { error: "An error occurred", reference: "ERR-123" }

Vulnerability: Missing security headers
Required: X-Content-Type-Options, X-Frame-Options, CSP
```

---

## A06:2021 - Vulnerable and Outdated Components

Components with known vulnerabilities undermine application defenses.

### Checklist

- [ ] Remove unused dependencies
- [ ] Continuously inventory component versions
- [ ] Monitor CVE and NVD for vulnerabilities
- [ ] Use only official sources over HTTPS
- [ ] Prefer signed packages
- [ ] Monitor unmaintained libraries
- [ ] Implement virtual patching if needed

### Commands

```bash
# Node.js
npm audit
npm audit fix
npm outdated

# Python
pip-audit
safety check
pip list --outdated

# Go
govulncheck ./...
go list -m -u all
```

---

## A07:2021 - Identification and Authentication Failures

Confirmation of user identity and session management is critical.

### Checklist

- [ ] Implement multi-factor authentication
- [ ] Don't ship with default credentials
- [ ] Implement weak password checks
- [ ] Harden registration and credential recovery
- [ ] Limit failed login attempts
- [ ] Use secure session management
- [ ] Generate new session ID on login

### Common Vulnerabilities

```
Vulnerability: Credential stuffing
Mitigation: Rate limiting, CAPTCHA, MFA

Vulnerability: Session fixation
Action: Regenerate session ID after authentication

Vulnerability: Brute force attacks
Action: Account lockout after N failed attempts

Vulnerability: Insecure password storage
Bad:  plaintext or MD5/SHA1
Good: bcrypt, scrypt, or Argon2
```

---

## A08:2021 - Software and Data Integrity Failures

Failures relating to code and infrastructure without integrity verification.

### Checklist

- [ ] Use digital signatures to verify software
- [ ] Ensure libraries are from trusted repositories
- [ ] Use software composition analysis tools
- [ ] Review code and config changes
- [ ] Ensure CI/CD pipeline has proper access controls
- [ ] Unsigned/unencrypted data not sent to untrusted clients

### Common Vulnerabilities

```
Vulnerability: Unverified CDN resources
Bad:  <script src="https://cdn.example.com/lib.js">
Good: <script src="..." integrity="sha384-..." crossorigin="anonymous">

Vulnerability: Insecure deserialization
Action: Don't deserialize untrusted data, use allow-lists
```

---

## A09:2021 - Security Logging and Monitoring Failures

Without logging and monitoring, breaches cannot be detected.

### Checklist

- [ ] Log login, access control, and validation failures
- [ ] Log with sufficient context
- [ ] Ensure logs are in a consumable format
- [ ] Log data is encoded to prevent injection
- [ ] High-value transactions have audit trail
- [ ] Establish effective monitoring and alerting
- [ ] Incident response and recovery plan exists

### What to Log

```
Authentication: login success/failure, logout, password reset
Authorization: access denied, privilege escalation attempts
Input validation: blocked requests, suspicious patterns
Application errors: exceptions, crashes
System events: startup/shutdown, configuration changes
```

---

## A10:2021 - Server-Side Request Forgery (SSRF)

SSRF flaws occur when a web application fetches a remote resource without validating the user-supplied URL.

### Checklist

- [ ] Sanitize and validate all user-supplied URLs
- [ ] Use allowlist of permitted destinations
- [ ] Disable HTTP redirects
- [ ] Don't send raw responses to clients
- [ ] Segment remote resource access functionality
- [ ] Block requests to internal services (169.254.x.x, 10.x.x.x)

### Common Vulnerabilities

```
Vulnerability: Internal service access
Bad:  fetch(userProvidedUrl)
Good: Validate URL against allowlist of external domains

Vulnerability: Cloud metadata access
Block: http://169.254.169.254/latest/meta-data/

Vulnerability: File protocol
Block: file://, gopher://, dict://
```
