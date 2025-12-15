# Performance Review Checklist

## Database Performance

### Query Optimization
- [ ] No N+1 query patterns (use eager loading)
- [ ] Appropriate indexes exist for queries
- [ ] EXPLAIN/EXPLAIN ANALYZE reviewed for slow queries
- [ ] Pagination implemented for large result sets
- [ ] Avoid SELECT * (select only needed columns)

### Connection Management
- [ ] Connection pooling configured
- [ ] Connections properly closed/returned
- [ ] Transaction scope minimized
- [ ] Appropriate timeout settings

### Data Fetching
- [ ] Batch operations used where possible
- [ ] Lazy loading for heavy relations
- [ ] Query results cached when appropriate
- [ ] No duplicate queries in request

## API Performance

### Response Time
- [ ] Async operations for I/O-bound tasks
- [ ] Background jobs for heavy processing
- [ ] Timeouts configured for external calls
- [ ] Circuit breakers for failing services

### Payload Optimization
- [ ] Response size minimized
- [ ] Compression enabled (gzip/brotli)
- [ ] Unnecessary fields excluded
- [ ] Pagination for list endpoints

### Caching Strategy
- [ ] HTTP cache headers set appropriately
- [ ] CDN used for static assets
- [ ] Application-level caching implemented
- [ ] Cache invalidation strategy defined

## Frontend Performance

### Bundle Size
- [ ] Code splitting implemented
- [ ] Tree shaking enabled
- [ ] Dynamic imports for large modules
- [ ] Bundle analyzer reviewed

### Rendering
- [ ] Unnecessary re-renders avoided
- [ ] Memoization used appropriately
- [ ] Virtual scrolling for long lists
- [ ] Lazy loading for off-screen content

### Assets
- [ ] Images optimized and properly sized
- [ ] Modern image formats used (WebP, AVIF)
- [ ] Critical CSS inlined
- [ ] Fonts optimized and preloaded

### Network
- [ ] Requests minimized/batched
- [ ] Prefetching for predictable navigation
- [ ] Service worker for offline/caching
- [ ] HTTP/2 or HTTP/3 utilized

## Memory Management

### Resource Cleanup
- [ ] Event listeners removed on cleanup
- [ ] Subscriptions unsubscribed
- [ ] Timers/intervals cleared
- [ ] Large objects dereferenced

### Memory Leaks
- [ ] No closures holding large objects
- [ ] WeakMap/WeakSet used where appropriate
- [ ] Circular references avoided
- [ ] Object pools for frequent allocations

## Algorithm Efficiency

### Complexity
- [ ] O(n²) or worse algorithms justified
- [ ] Appropriate data structures used
- [ ] Early termination where possible
- [ ] Divide and conquer for large data

### Data Structures
- [ ] Map/Set for frequent lookups (not Array.find)
- [ ] Appropriate collection types
- [ ] Immutable structures where beneficial
- [ ] Pre-computed values for repeated calculations

## Concurrency

### Parallelization
- [ ] Independent operations parallelized
- [ ] Promise.all for concurrent requests
- [ ] Web Workers for CPU-intensive tasks
- [ ] Thread pool sizing appropriate

### Race Conditions
- [ ] Proper synchronization implemented
- [ ] Atomic operations where needed
- [ ] Optimistic locking considered
- [ ] Deadlock prevention

## Performance Anti-Patterns

### Backend
```
Issue: N+1 Query
Bad:  users.map(u => u.getPosts())  // N+1 queries
Good: User.findAll({ include: [Post] })  // 1 query with eager loading

Issue: Missing Index
Bad:  WHERE email = ?  // Full table scan on large table
Good: CREATE INDEX idx_users_email ON users(email)

Issue: Synchronous I/O
Bad:  fs.readFileSync() in request handler
Good: await fs.promises.readFile()
```

### Frontend
```
Issue: Unnecessary Re-render
Bad:  <List items={items.map(i => ({...i}))} />  // New array on each render
Good: const memoizedItems = useMemo(() => items.map(...), [items])

Issue: Large Bundle Import
Bad:  import _ from 'lodash'  // Imports entire library
Good: import debounce from 'lodash/debounce'  // Tree-shakeable

Issue: Layout Thrashing
Bad:  elements.forEach(e => { e.style.width = e.offsetWidth + 'px' })
Good: const widths = elements.map(e => e.offsetWidth); elements.forEach((e, i) => e.style.width = widths[i] + 'px')
```

## Performance Testing

### Metrics to Track
- [ ] Time to First Byte (TTFB)
- [ ] First Contentful Paint (FCP)
- [ ] Largest Contentful Paint (LCP)
- [ ] Time to Interactive (TTI)
- [ ] Cumulative Layout Shift (CLS)

### Load Testing
- [ ] Expected load tested
- [ ] Peak load tested
- [ ] Failure scenarios tested
- [ ] Performance regression tests exist
