# Pre-Migration Checklist

Complete this checklist before running any database migration in production.

## Before Writing Migration

- [ ] Understand the current schema state
- [ ] Identify all affected tables and their sizes
- [ ] Review existing indexes and constraints
- [ ] Check for dependent views, triggers, or functions
- [ ] Understand application code dependencies

## Migration Design

- [ ] Migration has both UP and DOWN scripts
- [ ] DOWN migration is tested and works
- [ ] Migration is idempotent (can run multiple times safely)
- [ ] Large table operations use batching or CONCURRENTLY
- [ ] Transaction boundaries are appropriate
- [ ] Migration follows naming convention: `YYYYMMDDHHMMSS_description.sql`

## Risk Assessment

### Table Size Impact
| Rows | Risk | Recommendation |
|------|------|----------------|
| < 10K | Low | Standard migration |
| 10K - 1M | Medium | Test timing, consider off-peak |
| 1M - 10M | High | Use batching, maintenance window |
| > 10M | Critical | Staged migration, feature flags |

### Operation Risk
| Operation | Risk | Mitigation |
|-----------|------|------------|
| CREATE TABLE | Low | None needed |
| ADD COLUMN (nullable) | Low | None needed |
| ADD COLUMN (with default) | Medium | May lock table |
| ADD INDEX | High | Use CONCURRENTLY |
| DROP COLUMN | High | Verify no usage |
| DROP TABLE | Critical | Verify no references |
| RENAME COLUMN | Critical | Coordinate with code deploy |
| ALTER TYPE | Critical | May require data migration |

## Testing Checklist

- [ ] Tested on local database
- [ ] Tested on staging/development with production-like data
- [ ] UP migration completes successfully
- [ ] DOWN migration completes successfully
- [ ] UP → DOWN → UP cycle works
- [ ] Application works after migration
- [ ] Application works after rollback
- [ ] Performance tested (for large tables)
- [ ] Migration timing recorded

## Pre-Production Checklist

- [ ] Production database backup completed
- [ ] Backup restoration tested recently
- [ ] Team notified of maintenance window (if needed)
- [ ] Rollback plan documented
- [ ] Monitoring dashboards ready
- [ ] On-call engineer available
- [ ] Feature flags in place (if needed)

## Deployment Checklist

- [ ] Deployment order documented:
  - [ ] 1. Run migration
  - [ ] 2. Deploy application
  - OR
  - [ ] 1. Deploy application (backwards compatible)
  - [ ] 2. Run migration
  - [ ] 3. Deploy application (uses new schema)

- [ ] Communication sent to stakeholders
- [ ] Maintenance page ready (if needed)

## Post-Migration Verification

- [ ] Migration completed without errors
- [ ] Application health checks passing
- [ ] No error spikes in monitoring
- [ ] Query performance is acceptable
- [ ] Data integrity verified (spot checks)
- [ ] Dependent systems still working

## Rollback Triggers

Rollback immediately if:
- [ ] Migration fails or times out
- [ ] Application errors increase significantly
- [ ] Query performance degrades severely
- [ ] Data corruption detected
- [ ] Dependent systems fail

## Rollback Procedure

1. [ ] Notify team of rollback decision
2. [ ] Run DOWN migration
3. [ ] Verify DOWN migration completed
4. [ ] Rollback application if needed
5. [ ] Verify system health
6. [ ] Document what went wrong
7. [ ] Plan remediation

## Documentation

After successful migration:
- [ ] Update schema documentation
- [ ] Update any ERD diagrams
- [ ] Document any manual steps taken
- [ ] Record migration timing for future reference
- [ ] Archive migration ticket/PR

---

## Quick Reference: Safe vs Unsafe Operations

### Safe (Usually no issues)
```sql
CREATE TABLE ...
ALTER TABLE ADD COLUMN (nullable, no default)
CREATE INDEX CONCURRENTLY ...
```

### Requires Care
```sql
ALTER TABLE ADD COLUMN ... DEFAULT ... -- locks table
ALTER TABLE ADD CONSTRAINT ... -- may lock
CREATE INDEX ... -- locks table (use CONCURRENTLY)
```

### Dangerous (Plan carefully)
```sql
DROP TABLE ...
DROP COLUMN ...
ALTER COLUMN TYPE ...
TRUNCATE ...
```

---

## Emergency Contacts

| Role | Name | Contact |
|------|------|---------|
| DBA | [Name] | [Contact] |
| On-call | [Name] | [Contact] |
| Team Lead | [Name] | [Contact] |
