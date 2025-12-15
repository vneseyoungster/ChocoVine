# Authentication Security Checklist

## Password Security

### Storage
- [ ] Passwords hashed using bcrypt, scrypt, or Argon2
- [ ] Salt is unique per password (automatic with bcrypt)
- [ ] Work factor is appropriate (bcrypt: 12+ rounds)
- [ ] Plain text passwords never stored or logged

### Requirements
- [ ] Minimum length: 8 characters (12+ recommended)
- [ ] No maximum length limit (or very high: 128+)
- [ ] Check against breached password lists
- [ ] Don't require arbitrary complexity rules
- [ ] Allow all printable characters and spaces

### Implementation
```typescript
// Good password hashing
import bcrypt from 'bcrypt';

async function hashPassword(password: string): Promise<string> {
  const saltRounds = 12;
  return bcrypt.hash(password, saltRounds);
}

async function verifyPassword(password: string, hash: string): Promise<boolean> {
  return bcrypt.compare(password, hash);
}

// Bad - never do this
const hash = md5(password); // Weak algorithm
const hash = sha256(password); // No salt, fast to brute force
```

---

## Session Management

### Session ID
- [ ] Generated using cryptographically secure random number generator
- [ ] Sufficient length (128+ bits of entropy)
- [ ] Session ID changes after authentication
- [ ] Session ID changes after privilege change

### Session Storage
- [ ] Session data stored server-side
- [ ] Only session ID sent to client
- [ ] Session ID in cookie, not URL
- [ ] Sessions have absolute timeout (e.g., 24 hours)
- [ ] Sessions have idle timeout (e.g., 30 minutes)

### Cookie Security
- [ ] `Secure` flag set (HTTPS only)
- [ ] `HttpOnly` flag set (no JavaScript access)
- [ ] `SameSite` attribute set (Strict or Lax)
- [ ] `Path` attribute appropriately scoped
- [ ] Cookie name doesn't reveal technology

```typescript
// Secure session cookie configuration
app.use(session({
  secret: process.env.SESSION_SECRET,
  name: 'sessionId', // Don't use default names like 'connect.sid'
  cookie: {
    secure: true,        // HTTPS only
    httpOnly: true,      // No JavaScript access
    sameSite: 'strict',  // CSRF protection
    maxAge: 24 * 60 * 60 * 1000, // 24 hours
  },
  resave: false,
  saveUninitialized: false,
}));
```

---

## Token Security (JWT)

### Token Generation
- [ ] Use strong secret key (256+ bits)
- [ ] Use asymmetric keys for distributed systems
- [ ] Include `iat` (issued at) claim
- [ ] Include `exp` (expiration) claim
- [ ] Short expiration for access tokens (15-60 minutes)
- [ ] Longer expiration for refresh tokens (days/weeks)

### Token Validation
- [ ] Verify signature on every request
- [ ] Check `exp` claim
- [ ] Validate `iss` (issuer) claim
- [ ] Validate `aud` (audience) claim
- [ ] Reject `alg: none`
- [ ] Use allowlist for algorithms

### Token Storage
- [ ] Access tokens: memory (not localStorage)
- [ ] Refresh tokens: httpOnly cookie
- [ ] Never store tokens in localStorage for sensitive apps

```typescript
// JWT configuration
import jwt from 'jsonwebtoken';

const ACCESS_TOKEN_EXPIRY = '15m';
const REFRESH_TOKEN_EXPIRY = '7d';

function generateAccessToken(userId: string): string {
  return jwt.sign(
    { sub: userId, type: 'access' },
    process.env.JWT_SECRET,
    {
      expiresIn: ACCESS_TOKEN_EXPIRY,
      algorithm: 'HS256',
      issuer: 'myapp',
      audience: 'myapp-api',
    }
  );
}

function verifyToken(token: string): JwtPayload {
  return jwt.verify(token, process.env.JWT_SECRET, {
    algorithms: ['HS256'], // Allowlist algorithms
    issuer: 'myapp',
    audience: 'myapp-api',
  });
}
```

---

## Multi-Factor Authentication (MFA)

### Implementation
- [ ] Offer MFA as an option (required for sensitive apps)
- [ ] Support multiple MFA methods (TOTP, SMS backup)
- [ ] TOTP preferred over SMS
- [ ] Recovery codes generated and stored securely
- [ ] Rate limit MFA attempts

### TOTP Setup
```typescript
import speakeasy from 'speakeasy';
import qrcode from 'qrcode';

function generateTotpSecret(userEmail: string) {
  const secret = speakeasy.generateSecret({
    name: `MyApp (${userEmail})`,
    issuer: 'MyApp',
  });

  return {
    secret: secret.base32,
    qrCodeUrl: secret.otpauth_url,
  };
}

function verifyTotp(secret: string, token: string): boolean {
  return speakeasy.totp.verify({
    secret,
    encoding: 'base32',
    token,
    window: 1, // Allow 1 step tolerance
  });
}
```

---

## Login Security

### Brute Force Protection
- [ ] Rate limit login attempts per account
- [ ] Rate limit login attempts per IP
- [ ] Implement exponential backoff
- [ ] Account lockout after N failures (temporary)
- [ ] CAPTCHA after N failures

### Login Response
- [ ] Same response for invalid username and password
- [ ] No user enumeration via error messages
- [ ] No timing differences between valid/invalid users

```typescript
// Anti-enumeration login response
async function login(email: string, password: string) {
  const user = await findUserByEmail(email);

  // Always hash even if user doesn't exist (prevent timing attack)
  const fakeHash = '$2b$12$fake.hash.for.timing.attack.prevention';
  const hashToCheck = user?.passwordHash || fakeHash;

  const isValid = await bcrypt.compare(password, hashToCheck);

  if (!user || !isValid) {
    // Same error regardless of which failed
    throw new AuthError('Invalid email or password');
  }

  return createSession(user);
}
```

---

## Password Reset

### Flow Security
- [ ] Rate limit reset requests
- [ ] Use secure random tokens (128+ bits)
- [ ] Tokens expire quickly (1 hour max)
- [ ] One-time use tokens
- [ ] Invalidate existing tokens on new request
- [ ] Same response for valid/invalid emails

### Implementation
```typescript
async function requestPasswordReset(email: string) {
  const user = await findUserByEmail(email);

  // Always return success (prevent enumeration)
  if (!user) return;

  // Invalidate existing reset tokens
  await invalidateResetTokens(user.id);

  // Generate secure token
  const token = crypto.randomBytes(32).toString('hex');
  const expiry = new Date(Date.now() + 60 * 60 * 1000); // 1 hour

  await saveResetToken({
    userId: user.id,
    tokenHash: await bcrypt.hash(token, 10),
    expiresAt: expiry,
  });

  await sendResetEmail(email, token);
}
```

---

## Logout

### Requirements
- [ ] Session invalidated server-side
- [ ] Session cookie cleared
- [ ] JWT refresh token revoked
- [ ] Clear client-side storage
- [ ] Redirect to login page

```typescript
async function logout(sessionId: string, refreshToken: string) {
  // Invalidate session
  await deleteSession(sessionId);

  // Revoke refresh token (add to blacklist or delete)
  await revokeRefreshToken(refreshToken);

  // Clear cookies
  res.clearCookie('sessionId');
  res.clearCookie('refreshToken');

  res.redirect('/login');
}
```

---

## Security Headers

```typescript
// Security headers for auth pages
app.use((req, res, next) => {
  res.set({
    'Strict-Transport-Security': 'max-age=31536000; includeSubDomains',
    'X-Content-Type-Options': 'nosniff',
    'X-Frame-Options': 'DENY',
    'X-XSS-Protection': '1; mode=block',
    'Cache-Control': 'no-store, no-cache, must-revalidate, proxy-revalidate',
    'Pragma': 'no-cache',
    'Expires': '0',
  });
  next();
});
```
