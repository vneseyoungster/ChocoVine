# Function Documentation Guidelines

Best practices for documenting functions, methods, and code segments.

## Core Principles

### 1. Document Intent, Not Implementation

**Bad (restating code):**
```typescript
/**
 * Loops through users and filters by age
 */
function getAdultUsers(users: User[]): User[] {
  return users.filter(u => u.age >= 18)
}
```

**Good (explaining why):**
```typescript
/**
 * Filters users to only those eligible for age-restricted content.
 * Uses legal adult age threshold (18) for compliance.
 */
function getAdultUsers(users: User[]): User[] {
  return users.filter(u => u.age >= 18)
}
```

### 2. Document Decisions and Trade-offs

When code makes non-obvious choices:
```typescript
/**
 * Processes payment using retry with exponential backoff.
 *
 * Uses 3 retries because payment provider recommends this for
 * transient failures. Exponential backoff prevents rate limiting.
 *
 * Trade-off: Slower failure detection vs. higher success rate.
 */
async function processPayment(order: Order): Promise<Receipt> {
  // ...
}
```

### 3. Document Edge Cases and Constraints

```typescript
/**
 * Calculates discount for cart items.
 *
 * @param items - Cart items. Empty array returns 0.
 * @param code - Optional promo code. Case-insensitive.
 * @returns Discount amount (always positive, capped at cart total)
 *
 * @throws {InvalidCodeError} If code is malformed (not expired codes)
 *
 * Note: Does not stack with member discounts. Use getMemberDiscount()
 * first, then apply whichever is greater.
 */
function calculateDiscount(items: CartItem[], code?: string): number
```

## Documentation Patterns by Language

### TypeScript/JavaScript (JSDoc)

```typescript
/**
 * Brief description of function purpose.
 *
 * Detailed explanation if needed. Can be multiple paragraphs.
 * Explain business context, algorithm choices, or constraints.
 *
 * @param name - Description. Include valid values/ranges.
 * @param options - Configuration object:
 *   - `timeout` - Max wait time in ms (default: 5000)
 *   - `retries` - Retry attempts (default: 3)
 * @returns Description of return value
 * @throws {ErrorType} When and why this error occurs
 *
 * @example
 * const result = myFunction('test', { timeout: 3000 })
 * // => { success: true, data: {...} }
 *
 * @see {@link RelatedFunction} for related functionality
 * @since 1.2.0
 * @deprecated Use newFunction instead. Removal in v3.0.
 */
```

### Python (Docstrings)

```python
def calculate_risk_score(transactions: list[Transaction],
                         threshold: float = 0.7) -> RiskAssessment:
    """
    Calculate fraud risk score from transaction history.

    Uses ML model trained on historical fraud cases. Higher scores
    indicate higher risk. Threshold of 0.7 is recommended for
    balanced precision/recall based on A/B testing.

    Args:
        transactions: Recent transactions (minimum 10 required
            for accurate scoring). Older transactions are weighted
            less heavily.
        threshold: Risk threshold for flagging (0.0-1.0).
            Default 0.7 balances false positives vs. missed fraud.

    Returns:
        RiskAssessment with:
        - score: Float 0.0-1.0 (higher = more risk)
        - factors: List of contributing risk factors
        - recommendation: 'approve', 'review', or 'decline'

    Raises:
        InsufficientDataError: If less than 10 transactions provided.
        ModelNotLoadedError: If ML model fails to initialize.

    Example:
        >>> txns = fetch_recent_transactions(user_id, limit=100)
        >>> assessment = calculate_risk_score(txns)
        >>> if assessment.score > 0.9:
        ...     trigger_manual_review(user_id)

    Note:
        Model is retrained weekly. Score interpretation may shift
        slightly between versions. Always use recommendation field.
    """
```

### Go

```go
// ProcessOrder handles the complete order fulfillment lifecycle.
//
// This function orchestrates inventory check, payment processing,
// and shipping label generation. It uses two-phase commit to
// ensure inventory and payment stay synchronized.
//
// The timeout parameter controls the maximum time for payment
// processing. Recommended: 30s for credit cards, 60s for bank
// transfers.
//
// Returns ErrInsufficientInventory if any item is out of stock.
// Returns ErrPaymentFailed if payment cannot be processed.
// Returns ErrShippingUnavailable if address is not serviceable.
//
// Example:
//
//	order := &Order{Items: items, Address: addr}
//	receipt, err := ProcessOrder(ctx, order, 30*time.Second)
//	if err != nil {
//	    log.Printf("Order failed: %v", err)
//	    return
//	}
//	sendConfirmation(receipt)
func ProcessOrder(ctx context.Context, order *Order, timeout time.Duration) (*Receipt, error)
```

## When to Document

### Always Document

- Public APIs and exported functions
- Complex algorithms (especially non-obvious ones)
- Business logic with domain-specific rules
- Functions with non-obvious side effects
- Deprecated code (with migration path)
- Functions with unusual parameter constraints

### Skip Documentation When

- Function name is self-documenting: `getUserById(id)`
- Implementation is obvious: `isEmpty(arr) => arr.length === 0`
- Private helper with clear name: `formatCurrency(amount)`
- Test functions (name should describe what's being tested)

## Inline Comments

Use for explaining WHY, not WHAT:

```typescript
// BAD: Restating code
// Loop through users
for (const user of users) {

// GOOD: Explaining non-obvious decision
// Process oldest users first to prioritize long-term customers
users.sort((a, b) => a.createdAt - b.createdAt)
for (const user of users) {
```

## Common Anti-Patterns

### 1. Outdated Documentation

```typescript
/**
 * Sends email notification
 * @deprecated This now sends SMS too (but comment not updated)
 */
function notifyUser(user: User) {
  sendEmail(user.email)  // Original
  sendSMS(user.phone)    // Added later, doc not updated
}
```

### 2. Over-Documentation

```typescript
/**
 * Adds two numbers together.
 *
 * This function takes the first number parameter and adds it
 * to the second number parameter using the + operator and then
 * returns the result of that addition.
 *
 * @param a - The first number to add
 * @param b - The second number to add
 * @returns The sum of a and b
 */
function add(a: number, b: number): number {
  return a + b
}
// Just use: add(a: number, b: number): number - self-documenting
```

### 3. Placeholder Documentation

```typescript
/**
 * TODO: Add documentation
 * @param data - data
 * @returns result
 */
function processData(data: any): any {
  // Complex business logic here
}
// Either document properly or don't document at all
```

## Documentation Maintenance

1. **Update with code changes** - Stale docs are worse than none
2. **Review in PRs** - Check doc accuracy with code review
3. **Use examples** - Keep examples working with tests
4. **Link related docs** - Use @see and cross-references
5. **Version notes** - Use @since and @deprecated appropriately
