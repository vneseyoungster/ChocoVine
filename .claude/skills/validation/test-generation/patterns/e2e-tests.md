# End-to-End (E2E) Testing Patterns

## Overview

E2E tests verify complete user flows from the user's perspective, typically through browser automation.

## Characteristics

- **Slowest**: Takes minutes
- **Most realistic**: Tests actual user experience
- **Most brittle**: Sensitive to UI changes
- **Most valuable**: Catches real-world issues

## Test Structure

### Playwright E2E Tests

```typescript
import { test, expect } from '@playwright/test';

test.describe('User Authentication', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/');
  });

  test('should allow user to sign up', async ({ page }) => {
    // Navigate to signup
    await page.click('text=Sign Up');

    // Fill form
    await page.fill('[name="email"]', 'newuser@example.com');
    await page.fill('[name="password"]', 'SecurePass123!');
    await page.fill('[name="confirmPassword"]', 'SecurePass123!');

    // Submit
    await page.click('button[type="submit"]');

    // Verify success
    await expect(page).toHaveURL('/dashboard');
    await expect(page.locator('text=Welcome')).toBeVisible();
  });

  test('should show error for invalid email', async ({ page }) => {
    await page.click('text=Sign Up');
    await page.fill('[name="email"]', 'invalid-email');
    await page.click('button[type="submit"]');

    await expect(page.locator('.error-message')).toContainText('Invalid email');
  });

  test('should allow user to login', async ({ page }) => {
    await page.click('text=Login');
    await page.fill('[name="email"]', 'existing@example.com');
    await page.fill('[name="password"]', 'password123');
    await page.click('button[type="submit"]');

    await expect(page).toHaveURL('/dashboard');
  });

  test('should allow user to logout', async ({ page }) => {
    // Login first
    await loginAs(page, 'user@example.com');

    // Logout
    await page.click('[data-testid="user-menu"]');
    await page.click('text=Logout');

    await expect(page).toHaveURL('/login');
  });
});
```

### Page Object Model

```typescript
// pages/LoginPage.ts
export class LoginPage {
  constructor(private page: Page) {}

  async goto() {
    await this.page.goto('/login');
  }

  async login(email: string, password: string) {
    await this.page.fill('[name="email"]', email);
    await this.page.fill('[name="password"]', password);
    await this.page.click('button[type="submit"]');
  }

  async getErrorMessage() {
    return this.page.locator('.error-message').textContent();
  }
}

// pages/DashboardPage.ts
export class DashboardPage {
  constructor(private page: Page) {}

  async getWelcomeMessage() {
    return this.page.locator('[data-testid="welcome"]').textContent();
  }

  async createProject(name: string) {
    await this.page.click('text=New Project');
    await this.page.fill('[name="projectName"]', name);
    await this.page.click('button[type="submit"]');
  }
}

// Usage in tests
test('user can create a project', async ({ page }) => {
  const loginPage = new LoginPage(page);
  const dashboardPage = new DashboardPage(page);

  await loginPage.goto();
  await loginPage.login('user@example.com', 'password');

  await dashboardPage.createProject('My Project');
  await expect(page.locator('text=My Project')).toBeVisible();
});
```

## Critical User Flows to Test

### Authentication Flow

```typescript
test.describe('Authentication Flow', () => {
  test('complete signup → email verification → login', async ({ page }) => {
    // Signup
    await page.goto('/signup');
    await page.fill('[name="email"]', 'new@example.com');
    await page.fill('[name="password"]', 'Password123!');
    await page.click('button[type="submit"]');

    // Check for verification message
    await expect(page.locator('text=Check your email')).toBeVisible();

    // Simulate email verification (via API or test route)
    await verifyEmail('new@example.com');

    // Login
    await page.goto('/login');
    await page.fill('[name="email"]', 'new@example.com');
    await page.fill('[name="password"]', 'Password123!');
    await page.click('button[type="submit"]');

    await expect(page).toHaveURL('/dashboard');
  });
});
```

### E-Commerce Checkout Flow

```typescript
test.describe('Checkout Flow', () => {
  test('browse → add to cart → checkout → confirm', async ({ page }) => {
    // Browse products
    await page.goto('/products');
    await page.click('[data-testid="product-1"]');

    // Add to cart
    await page.click('text=Add to Cart');
    await expect(page.locator('[data-testid="cart-count"]')).toHaveText('1');

    // Go to cart
    await page.click('[data-testid="cart-icon"]');
    await expect(page.locator('[data-testid="cart-item"]')).toHaveCount(1);

    // Checkout
    await page.click('text=Checkout');

    // Fill shipping
    await page.fill('[name="address"]', '123 Test St');
    await page.fill('[name="city"]', 'Test City');
    await page.fill('[name="zip"]', '12345');
    await page.click('text=Continue');

    // Fill payment
    await page.fill('[name="cardNumber"]', '4242424242424242');
    await page.fill('[name="expiry"]', '12/25');
    await page.fill('[name="cvc"]', '123');

    // Place order
    await page.click('text=Place Order');

    // Confirm
    await expect(page.locator('text=Order Confirmed')).toBeVisible();
    await expect(page.locator('[data-testid="order-number"]')).toBeVisible();
  });
});
```

## Visual Testing

```typescript
test('homepage should match snapshot', async ({ page }) => {
  await page.goto('/');
  await expect(page).toHaveScreenshot('homepage.png');
});

test('dashboard should match snapshot', async ({ page }) => {
  await loginAs(page, 'user@example.com');
  await page.goto('/dashboard');

  // Wait for dynamic content
  await page.waitForSelector('[data-testid="dashboard-loaded"]');

  await expect(page).toHaveScreenshot('dashboard.png', {
    mask: [page.locator('[data-testid="timestamp"]')], // Mask dynamic content
  });
});
```

## Test Configuration

```typescript
// playwright.config.ts
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './e2e',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 1 : undefined,

  use: {
    baseURL: 'http://localhost:3000',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
  },

  projects: [
    { name: 'chromium', use: { ...devices['Desktop Chrome'] } },
    { name: 'firefox', use: { ...devices['Desktop Firefox'] } },
    { name: 'webkit', use: { ...devices['Desktop Safari'] } },
    { name: 'mobile', use: { ...devices['iPhone 12'] } },
  ],

  webServer: {
    command: 'npm run dev',
    url: 'http://localhost:3000',
    reuseExistingServer: !process.env.CI,
  },
});
```

## Best Practices

### Use Data Attributes

```html
<!-- Good - stable selectors -->
<button data-testid="submit-btn">Submit</button>
<input data-testid="email-input" name="email" />

<!-- Avoid - brittle selectors -->
<button class="btn-primary">Submit</button>
```

### Handle Async Operations

```typescript
// Wait for element
await page.waitForSelector('[data-testid="loaded"]');

// Wait for network idle
await page.waitForLoadState('networkidle');

// Wait for specific request
await page.waitForResponse('**/api/users');

// Wait for timeout (last resort)
await page.waitForTimeout(1000);
```

### Test Data Management

```typescript
test.beforeEach(async ({ request }) => {
  // Reset database via API
  await request.post('/api/test/reset');

  // Seed test data
  await request.post('/api/test/seed', {
    data: { scenario: 'basic-user' },
  });
});
```

### Avoid Flaky Tests

```typescript
// Bad - timing dependent
await page.click('button');
await page.waitForTimeout(500);
expect(await page.locator('.result').textContent()).toBe('Done');

// Good - wait for condition
await page.click('button');
await expect(page.locator('.result')).toHaveText('Done');
```

## When to Use E2E vs Other Tests

| Scenario | Test Type |
|----------|-----------|
| Business logic | Unit |
| API contracts | Integration |
| Database queries | Integration |
| Critical user flows | E2E |
| Edge cases | Unit/Integration |
| Visual regression | E2E |
| Performance | Dedicated perf tests |
