# Generate Tests

Generate failing test files for: $ARGUMENTS

## Overview

This command is **Phase 4** of the research flow. It takes an approved test specification and generates actual test files that fail (as expected in TDD).

**Input:** `specs/test-specification.md` (from `/research:spec`)
**Output:** Actual test files in the project

**Prerequisite:** `/research:spec` must be completed with approved specification.

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
│   /research:spec    │  ← Phase 3 (Test Spec)
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│   /generate:tests   │  ← YOU ARE HERE (Test Files)
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
  → Verify test specification exists and is approved

ELSE:
  → Error: Session path required
```

### GATE: Verify Test Specification Complete

Before proceeding, verify:
- [ ] Session directory exists
- [ ] `specs/test-specification.md` exists
- [ ] Specification status is "Approved"
- [ ] `research/test-patterns.md` exists

**If specification missing or not approved:**
```
Test specification not found or not approved.
Please complete /research:spec first.
```

---

## Phase 2: Load Context

### Load Test Specification

Read the approved specification:
- Test cases with IDs
- Expected inputs/outputs
- Edge cases
- Error scenarios
- File structure plan

### Load Test Patterns

Read detected conventions:
- Framework (jest/vitest/mocha/pytest)
- File naming (*.test.ts, *.spec.js, test_*.py)
- Directory structure
- Import style
- Assertion style

---

## Phase 3: Generate Test Files

### Invoke Test Spec Generator Agent

Delegate to `test-spec-generator` sub-agent with:
- Approved test specification
- Test framework conventions
- Project patterns
- TDD skill reference

### Test File Template (TypeScript/Jest)

```typescript
/**
 * Test Suite: [Component/Feature]
 * Generated from: plans/sessions/{session}/specs/test-specification.md
 *
 * TDD: These tests define EXPECTED behavior before implementation.
 * All tests should FAIL initially - passing means implementation complete.
 */

import { functionUnderTest } from '../path/to/module';

describe('[Component/Feature]', () => {
  describe('[function/method]', () => {
    // REQ-1: [Requirement description]

    // T1: Happy path
    it('should [expected behavior]', () => {
      // Arrange
      const input = /* test data from spec */;

      // Act
      const result = functionUnderTest(input);

      // Assert
      expect(result).toBe(/* expected from spec */);
    });

    // E1: Edge case - empty input
    it('should handle empty input', () => {
      const result = functionUnderTest([]);
      expect(result).toEqual([]);
    });

    // ERR1: Error scenario
    it('should throw when [error condition]', () => {
      expect(() => functionUnderTest(invalidInput))
        .toThrow(ExpectedError);
    });
  });
});
```

### Test File Template (Python/pytest)

```python
"""
Test Suite: [Component/Feature]
Generated from: plans/sessions/{session}/specs/test-specification.md

TDD: These tests define EXPECTED behavior before implementation.
All tests should FAIL initially - passing means implementation complete.
"""

import pytest
from module import function_under_test


class TestFeature:
    """REQ-1: [Requirement description]"""

    # T1: Happy path
    def test_should_expected_behavior(self):
        # Arrange
        input_data = ...  # from spec

        # Act
        result = function_under_test(input_data)

        # Assert
        assert result == expected  # from spec

    # E1: Edge case
    def test_should_handle_empty_input(self):
        result = function_under_test([])
        assert result == []

    # ERR1: Error scenario
    def test_should_raise_when_error_condition(self):
        with pytest.raises(ExpectedError):
            function_under_test(invalid_input)
```

### File Generation Rules

1. **Follow project conventions** - Use detected patterns
2. **Include traceability** - Reference requirement IDs in comments
3. **AAA pattern** - Arrange, Act, Assert
4. **One assertion per test** - Keep tests atomic
5. **Descriptive names** - `it('should X when Y')`

---

## Phase 4: Verify Tests Fail Correctly

### Run Test Suite

```bash
# JavaScript/TypeScript
npm test -- [test-file] --no-coverage

# Python
pytest [test-file] -v
```

### Verification Criteria

| Result | Meaning | Action |
|--------|---------|--------|
| Tests FAIL | Correct - missing implementation | Proceed |
| Tests PASS | Wrong - testing existing behavior | Revise test |
| Tests ERROR | Syntax/import issue | Fix and re-run |
| Tests SKIP | Missing setup | Add setup and re-run |

### Handle Issues

**If tests pass immediately:**
```
WARNING: Test passed immediately!
This means you're testing existing behavior, not new behavior.
Revising test to assert on MISSING functionality...
```

**If tests error:**
```
Test file has errors:
- [error details]
Fixing...
```

---

## Phase 5: Complete

### Update Session Tracking

Update `session.md`:
```markdown
**Current Phase:** Test Files Generated

## Test Files
- [file1.test.ts] - X tests
- [file2.test.ts] - Y tests

## Test Summary
- Total Tests: [N]
- Status: All FAILING (expected - no implementation yet)
- Framework: [detected]

## Ready For
- `/research:plan` to create implementation plan
- `/execute` to implement directly
```

### Announce Completion

```
TEST FILES GENERATED

Session: plans/sessions/{date}-{task}/
├── research/                    ✓
├── specs/
│   ├── requirements.md          ✓
│   └── test-specification.md    ✓
└── [test files created]         ✓

Generated Files:
- src/__tests__/auth.test.ts (8 tests) ✓ FAILING
- src/__tests__/token.test.ts (6 tests) ✓ FAILING

Total: 14 tests, all failing as expected

Next Steps:
→ /research:plan [session-path] - Create implementation plan
→ /execute [session-path] - Implement to make tests pass
```

---

## Quality Gates

### Before Completion
- [ ] Test specification exists and is approved
- [ ] All test files created
- [ ] Tests run without syntax errors
- [ ] Tests FAIL (not pass, not error)
- [ ] Failure reason is "missing implementation"
- [ ] Tests map to requirements (traceability)

### Test Quality
- [ ] Each test is atomic
- [ ] Uses AAA pattern
- [ ] Descriptive test names
- [ ] Requirement IDs in comments
- [ ] Follows project conventions

---

## TDD Principles Enforced

From `.claude/skills/test-driven-development/SKILL.md`:

**Core Rules:**
- NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST
- Tests define SHOULD behavior, not IS behavior
- Watch each test fail before implementing

**Anti-Patterns to Avoid:**
- Don't test mock behavior instead of real code
- Don't add test-only methods to production classes
- Don't write incomplete mocks
- Don't add tests as afterthought

---

## Error Handling

### Specification not found
```
Test specification not found.
Please complete /research:spec first.
→ /research:spec [session-path]
```

### Specification not approved
```
Test specification exists but not approved.
Please review and approve specification.
→ /research:spec [session-path]
```

### Test framework not detected
```
Could not detect test framework.
Please specify: jest | vitest | mocha | pytest | other
```

### Tests pass immediately
```
WARNING: Tests should FAIL before implementation!
Test [test-name] passed immediately.
This indicates testing existing behavior.
Revising to test MISSING functionality...
```

---

## Example Usage

```
/generate:tests plans/sessions/2024-01-15-auth/

→ Loading test specification...
→ Found 14 test cases across 2 files
→ Detecting test patterns... Jest, TypeScript
→ Generating test files...
  - Creating src/__tests__/auth.test.ts
  - Creating src/__tests__/token.test.ts
→ Running tests to verify failures...
→ Results: 14 tests, 14 failed (expected)
→ All tests failing due to missing implementation ✓
→ Ready for implementation
```

---

## Related Commands

| Command | Purpose |
|---------|---------|
| `/research:spec` | Phase 3: Test specification |
| `/research:plan` | Phase 5: Implementation planning |
| `/execute` | Implementation phase |
