# Serverless Architecture Pattern

## Overview

Serverless architecture is an event-driven approach where the cloud provider manages server infrastructure, automatically scaling and billing based on actual usage rather than pre-provisioned capacity.

## When to Use

**Good Fit:**
- Event-driven workloads
- Variable or unpredictable traffic
- Cost optimization for sporadic usage
- Rapid development and deployment
- Stateless operations
- Background processing tasks

**Poor Fit:**
- Long-running processes
- Applications requiring persistent connections
- Workloads with predictable, constant load
- Latency-sensitive applications (cold start issues)
- Complex orchestration requirements

## Key Characteristics

| Aspect | Description |
|--------|-------------|
| Infrastructure | Fully managed by provider |
| Scaling | Automatic, pay-per-execution |
| State | Stateless functions |
| Execution | Event-triggered |
| Billing | Per invocation/duration |

## Architecture Components

```
Events/Triggers
       │
       ▼
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  API Gateway │     │  Event Bus   │     │   Schedule   │
└──────┬───────┘     └──────┬───────┘     └──────┬───────┘
       │                    │                    │
       └────────────────────┼────────────────────┘
                            │
                            ▼
              ┌─────────────────────────┐
              │    Function Runtime     │
              │  ┌───────┐ ┌───────┐   │
              │  │ Fn A  │ │ Fn B  │   │
              │  └───────┘ └───────┘   │
              │  ┌───────┐ ┌───────┐   │
              │  │ Fn C  │ │ Fn D  │   │
              │  └───────┘ └───────┘   │
              └─────────────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
        ▼                   ▼                   ▼
┌───────────────┐  ┌───────────────┐  ┌───────────────┐
│   Database    │  │    Storage    │  │External APIs  │
│  (DynamoDB)   │  │     (S3)      │  │               │
└───────────────┘  └───────────────┘  └───────────────┘
```

## Common Platforms

| Provider | Functions | API Gateway | Events |
|----------|-----------|-------------|--------|
| AWS | Lambda | API Gateway | EventBridge |
| Azure | Functions | API Management | Event Grid |
| GCP | Cloud Functions | Cloud Endpoints | Eventarc |
| Cloudflare | Workers | Built-in | Queues |

## Function Patterns

### Single-Purpose Functions
Each function does one thing well:
```
┌─────────────┐
│ HTTP Event  │
└──────┬──────┘
       ▼
┌─────────────┐     ┌─────────────┐
│ Validate    │────▶│   Save      │
│ Input       │     │   Data      │
└─────────────┘     └─────────────┘
```

### Function Chaining
Functions trigger other functions:
```
Upload → Process → Validate → Store → Notify
```

### Fan-Out Pattern
One event triggers multiple functions:
```
         ┌──▶ Send Email
Event ───┼──▶ Update DB
         └──▶ Log Analytics
```

## Common Triggers

| Trigger Type | Use Case | Example |
|--------------|----------|---------|
| HTTP | API endpoints | REST API |
| Queue | Background jobs | Order processing |
| Schedule | Cron jobs | Daily reports |
| Storage | File processing | Image resize |
| Database | Change streams | Sync data |

## State Management

### Stateless Design
- Each invocation is independent
- No shared memory between invocations

### External State Stores
- **DynamoDB/Cosmos DB**: Key-value, fast
- **Redis/ElastiCache**: Caching, sessions
- **S3/Blob Storage**: Large files, artifacts

### Step Functions/Durable Functions
For complex workflows requiring state:
```
Start → Step 1 → [Wait] → Step 2 → [Decision] → Step 3 → End
```

## Advantages

- No server management
- Automatic scaling
- Pay-per-use pricing
- Built-in high availability
- Reduced operational overhead
- Fast time to market
- Natural microservices boundaries

## Challenges

- **Cold Starts**: Initial invocation latency
- **Vendor Lock-in**: Platform-specific features
- **Debugging**: Distributed tracing complexity
- **Testing**: Local development challenges
- **Timeouts**: Execution time limits
- **Statelessness**: External state required
- **Cost Unpredictability**: Spiky usage

## Cold Start Mitigation

1. **Provisioned Concurrency**: Pre-warm instances
2. **Smaller Functions**: Faster initialization
3. **Language Choice**: Go/Rust > Python/Node > Java
4. **Keep Warm**: Periodic pings
5. **Optimize Dependencies**: Minimize packages

## Best Practices

### Function Design
- Single responsibility
- Small, focused functions
- Minimal dependencies
- Fast initialization
- Idempotent operations

### Error Handling
```javascript
// Retry-safe function
exports.handler = async (event) => {
  const idempotencyKey = event.id;

  // Check if already processed
  if (await isProcessed(idempotencyKey)) {
    return { statusCode: 200, body: 'Already processed' };
  }

  try {
    const result = await processEvent(event);
    await markProcessed(idempotencyKey);
    return { statusCode: 200, body: result };
  } catch (error) {
    // Don't mark as processed - allow retry
    throw error;
  }
};
```

### Project Structure
```
functions/
├── api/
│   ├── users/
│   │   ├── create.js
│   │   ├── get.js
│   │   └── update.js
│   └── orders/
├── events/
│   ├── order-created.js
│   └── user-registered.js
├── scheduled/
│   └── daily-report.js
└── shared/
    ├── utils/
    └── middleware/
```

## Implementation Checklist

- [ ] Define function boundaries
- [ ] Choose trigger types
- [ ] Design state management
- [ ] Plan error handling and retries
- [ ] Set up monitoring and tracing
- [ ] Configure cold start mitigation
- [ ] Implement idempotency
- [ ] Set appropriate timeouts
- [ ] Plan local development workflow
- [ ] Define deployment pipeline

## References

- [AWS Lambda Best Practices](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html)
- [Serverless Framework](https://www.serverless.com/)
- [Martin Fowler - Serverless Architectures](https://martinfowler.com/articles/serverless.html)
