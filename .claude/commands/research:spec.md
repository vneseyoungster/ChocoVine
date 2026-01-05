# Research Spec (Test Specification)

Generate test specification for: $ARGUMENTS

## Overview

This command is **Phase 3** of the research flow. It takes approved requirements and generates a detailed test specification document.

**Input:** `specs/requirements.md` (from `/research:feature`)
**Output:** `specs/test-specification.md`

**Prerequisite:** `/research:feature` must be completed with approved requirements.

---

## Phase Flow Position

```
┌─────────────────────┐
│  /research:codebase │  ← Phase 1
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│  /research:feature  │  ← Phase 2 (Requirements)
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│   /research:spec    │  ← YOU ARE HERE (Test Spec)
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│   /generate:tests   │  ← Phase 4 (Test Files)
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│   /research:plan    │  ← Phase 5 (Implementation)
└─────────────────────┘
```

---

## Phase 1: Verify Prerequisites

### Parse Arguments

```
IF $ARGUMENTS contains session path (plans/sessions/...):
  → Load session from specified path
  → Verify requirements exist and are approved

ELSE:
  → Error: Session path required
```

### GATE: Verify Requirements Complete

Before proceeding, verify:
- [ ] Session directory exists
- [ ] `specs/requirements.md` exists
- [ ] Requirements status is "Approved"

**If requirements missing or not approved:**
```
Requirements not found or not approved.
Please complete /research:feature first.
```

---

## Phase 2: Load Context

### Summarize Requirements

Use summarize-agent for context efficiency:

```
Task(summarize-agent, "Summarize: plans/sessions/{session}/specs/requirements.md")
```

### Load Test Patterns

Invoke `pattern-researcher` sub-agent to detect:
- Test framework (jest, vitest, mocha, pytest)
- Test file naming convention
- Test directory structure
- Assertion style
- Mocking approach

**Detection Strategy:**
| Detection | Framework |
|-----------|-----------|
| `jest` in package.json | Jest |
| `vitest.config.*` exists | Vitest |
| `pytest.ini` or `conftest.py` | pytest |
| `mocha` in package.json | Mocha |

**Output:** `plans/sessions/{session}/research/test-patterns.md`

---

## Phase 3: Map Requirements to Tests

### For Each Requirement

Transform requirements into test cases:

```markdown
## Requirement: [REQ-ID] [Requirement Name]

### Happy Path Tests
| ID | Test Case | Input | Expected Output |
|----|-----------|-------|-----------------|
| T1 | it should... | ... | ... |

### Edge Cases
| ID | Case | Expected Behavior |
|----|------|-------------------|
| E1 | Empty input | ... |
| E2 | Invalid type | ... |

### Error Scenarios
| ID | Scenario | Expected Error |
|----|----------|----------------|
| ERR1 | ... | ... |
```

### Edge Case Categories

Consider these for each requirement:
- **Boundary values** - min, max, zero, negative
- **Empty states** - null, undefined, empty string, empty array
- **Type errors** - wrong types, missing properties
- **Async failures** - timeouts, network errors
- **Permission errors** - unauthorized, forbidden
- **State conflicts** - concurrent operations, stale data

---

## Phase 4: Generate Test Specification

### Create Specification Document

Create `plans/sessions/{session}/specs/test-specification.md`:

```markdown
# Test Specification: [Feature Name]

**Session:** {session-id}
**Generated:** {date}
**Source:** specs/requirements.md
**Test Framework:** {detected}
**Status:** Draft | Approved

---

## Summary

- **Total Test Cases:** [N]
- **Test Files Needed:** [N]
- **Coverage Areas:** [list]

---

## Test Suite: [Component/Module]

### Describe: [Function/Behavior]

#### Happy Path Tests
| ID | Test Case | Input | Expected | Priority |
|----|-----------|-------|----------|----------|
| T1 | it should... | ... | ... | P1 |
| T2 | it should... | ... | ... | P1 |

#### Edge Cases
| ID | Case | Expected Behavior | Priority |
|----|------|-------------------|----------|
| E1 | Empty input | Returns empty array | P2 |
| E2 | Invalid type | Throws TypeError | P2 |

#### Error Scenarios
| ID | Scenario | Expected Error | Priority |
|----|----------|----------------|----------|
| ERR1 | Network failure | Throws NetworkError | P1 |

---

## Requirement Traceability Matrix

| Requirement ID | Test IDs | Coverage |
|----------------|----------|----------|
| REQ-1 | T1, T2, E1 | Full |
| REQ-2 | T3, T4, ERR1 | Full |
| REQ-3 | T5 | Partial - needs E3 |

---

## Test File Structure

```
[project-test-dir]/
├── [component].test.[ext]     # N tests
├── [component2].test.[ext]    # M tests
└── ...
```

---

## Mocking Strategy

### External Dependencies
| Dependency | Mock Strategy |
|------------|---------------|
| Database | In-memory / Mock client |
| API | MSW / nock |
| File system | memfs / mock-fs |

### Internal Dependencies
| Module | Mock Strategy |
|--------|---------------|
| ... | ... |

---

## Test Data Requirements

### Fixtures Needed
- [Fixture 1]: [description]
- [Fixture 2]: [description]

### Test Database State
- [Initial state requirements]
```

---

## Phase 5: Review & Approve

### Present Specification Summary

```
TEST SPECIFICATION REVIEW

Feature: [Name]
Session: plans/sessions/{date}-{task}/

## Summary
- Total Tests: [N]
- Test Files: [N]
- Framework: [detected]

## Test Coverage
- [Component 1]: X tests (Y edge cases)
- [Component 2]: Z tests (W edge cases)

## Requirement Coverage
- REQ-1: ✓ Full coverage
- REQ-2: ✓ Full coverage
- REQ-3: ⚠ Partial (missing edge case)

## Gaps Identified
[If any requirements lack coverage]

---
Full specification: specs/test-specification.md

Do you approve this test specification?
```

**GATE: User must approve before generating test files**

### Handle Feedback

If user requests changes:
- Update specification
- Re-present for approval

---

## Phase 6: Complete

### Update Session Tracking

Update `session.md`:
```markdown
**Current Phase:** Test Specification Complete

## Test Specification
- Documented in: specs/test-specification.md
- Status: Approved
- Total Tests: [N]
- Test Files: [N]

## Ready For
- `/generate:tests` to create test files
```

### Announce Completion

```
TEST SPECIFICATION COMPLETE

Session: plans/sessions/{date}-{task}/
├── research/                    ✓
├── specs/
│   ├── requirements.md          ✓
│   └── test-specification.md    ✓ (NEW)

Specification: [N] tests across [M] files

Next Steps:
→ /generate:tests [session-path] - Create failing test files
→ /research:plan [session-path] - Skip to implementation planning
```

---

## Quality Gates

### Before Approval
- [ ] Requirements document exists and is approved
- [ ] Test framework identified
- [ ] All requirements have test cases
- [ ] Edge cases identified for each requirement
- [ ] Error scenarios documented
- [ ] Traceability matrix complete

### Specification Quality
- [ ] Each test case is atomic (tests one thing)
- [ ] Expected outcomes are specific and measurable
- [ ] No duplicate test cases
- [ ] Priorities assigned (P1/P2/P3)
- [ ] Test file structure defined

---

## Error Handling

### Requirements not found
```
Requirements document not found.
Please complete /research:feature first.
→ /research:feature [description]
```

### Requirements not approved
```
Requirements exist but not approved.
Please review and approve requirements first.
→ /research:feature [session-path]
```

### Test framework not detected
```
Could not detect test framework.
Please specify: jest | vitest | mocha | pytest | other
```

---

## Example Usage

```
/research:spec plans/sessions/2024-01-15-auth/

→ Loading requirements from specs/requirements.md...
→ Found 5 functional requirements
→ Detecting test framework... Jest
→ Generating test specification...
→ Mapping requirements to test cases...
→ Identifying edge cases...
→ Creating traceability matrix...
→ [Presents specification for approval]
→ User approves
→ Ready for /generate:tests
```

---

## Related Commands

| Command | Purpose |
|---------|---------|
| `/research:feature` | Phase 2: Requirements gathering |
| `/generate:tests` | Phase 4: Test file generation |
| `/research:plan` | Phase 5: Implementation planning |
