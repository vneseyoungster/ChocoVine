# Dependency Audit Report

**Generated:** {date}
**Project:** {project_name}
**Package Manager:** {package_manager}

## Summary

| Metric | Count |
|--------|-------|
| Total Dependencies | {total} |
| Direct Dependencies | {direct} |
| Dev Dependencies | {dev} |
| Security Issues | {security_count} |
| Outdated Packages | {outdated_count} |

## Security Vulnerabilities

### Critical
| Package | Vulnerability | Severity | Fix Version |
|---------|---------------|----------|-------------|
| {package} | {vuln_id} | Critical | {fix_version} |

### High
| Package | Vulnerability | Severity | Fix Version |
|---------|---------------|----------|-------------|
| {package} | {vuln_id} | High | {fix_version} |

### Medium/Low
| Package | Vulnerability | Severity | Fix Version |
|---------|---------------|----------|-------------|
| {package} | {vuln_id} | {severity} | {fix_version} |

## Outdated Packages

### Major Updates Available
| Package | Current | Latest | Breaking Changes |
|---------|---------|--------|------------------|
| {package} | {current} | {latest} | {notes} |

### Minor/Patch Updates
| Package | Current | Latest |
|---------|---------|--------|
| {package} | {current} | {latest} |

## Deprecated Packages
| Package | Replacement | Notes |
|---------|-------------|-------|
| {package} | {replacement} | {notes} |

## Recommendations

### Immediate Actions (Critical)
1. {action_1}

### Short-term (High Priority)
1. {action_2}

### Long-term (Maintenance)
1. {action_3}

## Dependency Tree Issues
- {conflict_or_issue}
