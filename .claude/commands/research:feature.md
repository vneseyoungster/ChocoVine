# Research Feature (Test-First)

Generate failing tests for: $ARGUMENTS

## Overview

This command generates **executable failing tests** before implementation, enforcing TDD principles. Tests define what the feature SHOULD do, not what code currently does.

**Philosophy:** Writing tests first forces you to think about edge cases, inputs, and outputs before you're mentally committed to an implementation.

---

## Phase 1: Initialize & Detect Mode

### Parse Arguments

```
IF $ARGUMENTS contains ".md" file path:
  → Mode = EXISTING_PLAN
  → Load plan from specified path

ELSE IF $ARGUMENTS is empty AND active session has implementation.md:
  → Ask user: "Found implementation plan. Generate tests from it? (y/n)"
  → IF yes: Mode = EXISTING_PLAN
  → IF no: Mode = FRESH_START

ELSE:
  → Mode = FRESH_START
  → Feature description = $ARGUMENTS
```

### Create/Use Session Directory

**For FRESH_START:**
```
plans/sessions/{date}-{feature-slug}/
├── session.md
├── research/
│   └── test-patterns.md
├── specs/
│   └── test-specification.md
└── tests/
    └── (list of generated test files)
```

**For EXISTING_PLAN:**
Use existing session directory from the plan.

---

## Phase 2: Research Test Patterns

### Invoke Pattern Researcher (Test Focus)

Delegate to `pattern-researcher` sub-agent to detect:
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

## Phase 3: Generate Test Specification

### FRESH_START Mode

**Step 3.1: Brainstorm Feature Behavior**

Use `brainstorming` skill:
- Ask ONE question at a time
- Explore expected behaviors
- Identify edge cases and error conditions
- Clarify inputs and outputs

**Step 3.2: Map Requirements to Test Cases**

For each behavior identified:
- Create describe block (component/function)
- Create it/test blocks (specific behaviors)
- Include edge cases and error scenarios

### EXISTING_PLAN Mode

**Step 3.1: Read Implementation Plan**

Load `plans/sessions/{session}/plans/implementation.md`

**Step 3.2: Extract Testable Items**

For each task in the plan:
- Extract "Verification" criteria
- Convert to test cases
- Identify acceptance criteria

### Both Modes: Design Test Structure

Create test specification document:

```markdown
# Test Specification: [Feature Name]

## Test Suite: [Component/Module]

### Describe: [Function/Behavior]

| Test Case | Input | Expected Output | Priority |
|-----------|-------|-----------------|----------|
| it should... | ... | ... | P1 |

### Edge Cases

| Case | Expected Behavior |
|------|-------------------|
| Empty input | ... |
| Invalid type | ... |
| Boundary value | ... |

### Error Scenarios

| Scenario | Expected Error |
|----------|----------------|
| ... | ... |
```

### Present Specification for Approval

```
TEST SPECIFICATION REVIEW

## Summary
- Total Tests: [N]
- Test Files: [N]
- Framework: [detected]

## Test Cases
[List of test cases by priority]

## Edge Cases Covered
[List]

## Gaps (if any)
[Requirements not covered]

---
Do you approve this test specification?
```

**GATE: User must approve before generating test files**

---

## Phase 4: Write Failing Tests

### Invoke Test Spec Generator

Delegate to `test-spec-generator` sub-agent with:
- Approved test specification
- Test framework (from Phase 2)
- Project conventions
- TDD skill reference

### Create Test Files

Follow detected conventions:
- File naming (*.test.ts, *.spec.js, test_*.py)
- Directory structure (co-located, __tests__, tests/)
- Import style

### Test File Template

```typescript
describe('[Component/Feature]', () => {
  describe('[function/method]', () => {
    it('should [expected behavior]', () => {
      // Arrange
      const input = /* test data */;

      // Act
      const result = functionUnderTest(input);

      // Assert
      expect(result).toBe(/* expected */);
    });

    it('should handle [edge case]', () => {
      // TODO: Implement [component] to make this pass
      expect(/* ... */).toBe(/* ... */);
    });
  });
});
```

### Verify Tests Fail Correctly

Run test suite:
```bash
npm test -- [test-file]
```

Verify:
- Tests fail (not error/skip)
- Failure is due to missing implementation (not syntax error)
- No import or type errors

**If tests pass:** STOP - Test is not testing the right thing. Revise test.
**If tests error:** Fix error, then verify correct failure.

---

## Phase 5: Complete

### Save Test Specification

Create `plans/sessions/{session}/specs/test-specification.md`:
```markdown
# Test Specification: [Feature]

**Generated:** {date}
**Mode:** Fresh Start | From Existing Plan
**Test Framework:** {framework}

## Summary
- Total Tests: {count}
- Test Files Created: {list}

## Test Mapping

### [Requirement/Task ID]
- `it should...` in `file.test.ts:15`
- `it should...` in `file.test.ts:25`

## Edge Cases Covered
| Category | Count |
|----------|-------|
| Input validation | ... |
| Error handling | ... |

## Next Steps
1. Run `/execute` to implement features
2. Watch tests turn green one at a time
```

### Update Session Tracking

Update `session.md`:
```markdown
**Current Phase:** Test Specification Complete

## Test Files Generated
- [list of files]

## Ready For
- `/execute` to implement and make tests pass
```

### Announce Completion

```
TEST SPECIFICATION COMPLETE

Generated: {N} failing tests in {M} files

Test Files:
- [file1] (X tests)
- [file2] (Y tests)

All tests are failing as expected (no implementation yet).

Next: Run `/execute` to implement the feature.
Each passing test = progress toward completion.
```

---

## Quality Gates

### Before Test Generation
- [ ] Mode detected (fresh/existing)
- [ ] Test framework identified
- [ ] Test conventions documented
- [ ] Test specification approved by user

### After Test Generation
- [ ] All test files created
- [ ] Tests run without syntax errors
- [ ] Tests FAIL (not pass, not error)
- [ ] Failure reason is "missing implementation"

---

## TDD Skill Integration

This command enforces TDD principles from `.claude/skills/test-driven-development/SKILL.md`:

**Core Philosophy:**
- NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST
- Tests define SHOULD behavior, not IS behavior
- Watch each test fail before implementing

**Anti-Patterns to Avoid:**
From `.claude/skills/test-driven-development/testing-anti-patterns.md`:
- Don't test mock behavior instead of real code
- Don't add test-only methods to production classes
- Don't write incomplete mocks
- Don't add tests as afterthought

---

## Error Handling

### No test framework detected
```
Could not detect test framework.
Please specify: jest | vitest | mocha | pytest | other
```

### Existing plan not found
```
Plan file not found at: [path]
Switching to fresh start mode.
```

### Tests pass immediately
```
WARNING: Test passed immediately!
This means you're testing existing behavior, not new behavior.
Revise test to assert on MISSING functionality.
```

---

## Example Usage

### Fresh Start
```
/research:feature Add user authentication with JWT

→ Detects: vitest framework, __tests__ directory
→ Brainstorms: login behavior, token validation, edge cases
→ Generates test specification
→ Creates failing tests:
  - src/auth/__tests__/login.test.ts
  - src/auth/__tests__/token.test.ts
  - src/auth/__tests__/middleware.test.ts
→ Verifies all tests fail correctly
→ Ready for /execute
```

### From Existing Plan
```
/research:feature plans/sessions/2024-01-15-auth/plans/implementation.md

→ Reads implementation plan (15 tasks)
→ Extracts verification criteria
→ Generates test specification (22 test cases)
→ Creates failing tests mapped to each task
→ Ready for /execute
```

---

## Related Commands

- `/research:codebase` - Full research + planning (no tests)
- `/execute` - Implement and make tests pass
- `/code-check` - Validate implementation
