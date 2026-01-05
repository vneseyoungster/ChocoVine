# Research Feature (Test Specification)

Generate test specifications for: $ARGUMENTS

## Overview

This command is **Phase 2** of the research flow. It gathers requirements through collaborative dialogue, then generates **executable failing tests** that define expected behavior before any implementation.

**Prerequisite:** `/research:codebase` must be completed first (or will be auto-invoked).

**Philosophy:** Writing tests first forces you to think about edge cases, inputs, and outputs before you're mentally committed to an implementation. Tests define SHOULD behavior, not IS behavior.

---

## Phase Flow Position

```
┌─────────────────────┐
│  /research:codebase │  ← Phase 1 (REQUIRED FIRST)
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  /research:feature  │  ← YOU ARE HERE (Phase 2)
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   /research:plan    │  ← Phase 3 (Next)
└─────────────────────┘
```

---

## Phase 0: Verify Prerequisites

### Parse Arguments

```
IF $ARGUMENTS contains session path (plans/sessions/...):
  → Mode = FROM_SESSION
  → Load session from specified path
  → Verify research phase completed

ELSE IF $ARGUMENTS is task description:
  → Mode = FRESH_START
  → Check if research exists for this task
  → IF no research: Auto-invoke /research:codebase first
```

### GATE: Verify Codebase Research Complete

Before proceeding, verify:
- [ ] Session directory exists: `plans/sessions/{date}-{task}/`
- [ ] Research findings exist: `research/codebase-map.md`
- [ ] Patterns documented: `research/patterns.md`

**If research missing:**
```
Codebase research not found. Invoking Phase 1 first...
→ /research:codebase $ARGUMENTS
```

---

## Phase 1: Load Research Context

### Summarize Research First

**CRITICAL: Use summarize-agent to compress research findings before loading into context.**

```
Invoke summarize-agent with:
- plans/sessions/{session}/research/

This returns a consolidated summary of:
- codebase-map.md
- patterns.md
- dependencies.md

Use this summary for planning instead of reading full files.
Only read full files if specific details are missing from summary.
```

**Invocation:**
```
Task(summarize-agent, "Summarize: plans/sessions/{session}/research/")
```

### Read Research Findings (If Needed)

Load specific research artifacts only if summary lacks detail:
1. `research/codebase-map.md` - Project structure
2. `research/patterns.md` - Code patterns and conventions
3. `research/dependencies.md` - Dependencies and constraints

### Create Context Summary

Compile key findings for questioning:
- Project type and stack
- Existing patterns to follow
- Integration points identified
- Constraints and limitations

---

## Phase 2: Questioning (Brainstorming-First)

### Invoke Requirement Analyst

Delegate to `requirement-analyst` sub-agent with:
- Research findings summary
- Original user request
- Session context

**The sub-agent uses the `brainstorming` skill FIRST:**
- Engages in collaborative dialogue with user
- Asks ONE question at a time (never overwhelming)
- Prefers multiple choice questions when possible
- Proposes 2-3 different approaches with trade-offs
- Leads with recommendation and reasoning
- Presents ideas in 200-300 word sections, validating each

### Brainstorming Dialogue Flow

```
1. Understand purpose, constraints, success criteria
   ↓
2. Explore 2-3 approaches with trade-offs
   ↓
3. Present recommendation with reasoning
   ↓
4. Validate incrementally (200-300 word sections)
   ↓
5. Generate formal questions for remaining gaps
```

### Present Questions to User

Display questions grouped by priority:

**Must Answer (Blocking)**
These questions must be answered before proceeding.

**Should Answer (Important)**
These questions improve test coverage quality.

**Could Answer (Nice to Have)**
These questions help identify edge cases.

### Await User Responses

For each question:
- Record the user's answer
- Or accept the default assumption
- Note any follow-up questions

### Generate Requirements Document

Create `plans/sessions/{session}/specs/requirements.md`:
- Functional requirements (with IDs)
- Non-functional requirements (with IDs)
- Acceptance criteria (testable)
- Assumptions confirmed
- Out of scope items

### Confirm Requirements

Present validated requirements and ask:

> "Here are the validated requirements based on your answers. Are these accurate? Ready to proceed to test specification?"

**GATE: DO NOT proceed without user confirmation**

---

## Phase 3: Research Test Patterns

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

## Phase 4: Generate Test Specification

### Map Requirements to Test Cases

For each requirement from the requirements document:

```markdown
## Requirement: [REQ-ID] [Requirement Name]

### Test Cases
| Test Case | Input | Expected Output | Priority |
|-----------|-------|-----------------|----------|
| it should... | ... | ... | P1 |

### Edge Cases
| Case | Expected Behavior |
|------|-------------------|
| Empty input | ... |
| Invalid type | ... |

### Error Scenarios
| Scenario | Expected Error |
|----------|----------------|
| ... | ... |
```

### Brainstorm Additional Scenarios

Use `brainstorming` skill to explore:
- What happens with edge cases?
- What error conditions could occur?
- What are the acceptance criteria boundaries?

### Create Test Specification Document

Create `plans/sessions/{session}/specs/test-specification.md`:

```markdown
# Test Specification: [Feature Name]

**Generated:** {date}
**Source:** specs/requirements.md
**Test Framework:** {detected}

## Summary
- Total Test Cases: [N]
- Test Files to Create: [N]
- Coverage Areas: [list]

## Test Suite: [Component/Module]

### Describe: [Function/Behavior]

#### Test Cases
| ID | Test Case | Input | Expected | Priority |
|----|-----------|-------|----------|----------|
| T1 | it should... | ... | ... | P1 |
| T2 | it should... | ... | ... | P1 |

#### Edge Cases
| ID | Case | Expected Behavior |
|----|------|-------------------|
| E1 | Empty input | Returns empty array |
| E2 | Invalid type | Throws TypeError |

#### Error Scenarios
| ID | Scenario | Expected Error |
|----|----------|----------------|
| ERR1 | Network failure | Throws NetworkError |

## Requirement Traceability

| Requirement ID | Test IDs | Coverage |
|----------------|----------|----------|
| REQ-1 | T1, T2, E1 | Full |
| REQ-2 | T3, T4, ERR1 | Full |
```

### Present Specification for Approval

```
TEST SPECIFICATION REVIEW

## Summary
- Total Tests: [N]
- Test Files: [N]
- Framework: [detected]

## Test Coverage
- [Component 1]: X tests
- [Component 2]: Y tests

## Edge Cases Covered
[List by category]

## Gaps (if any)
[Requirements not covered]

---
Full specification: plans/sessions/{session}/specs/test-specification.md

Do you approve this test specification?
```

**GATE: User must approve before generating test files**

---

## Phase 5: Write Failing Tests

### Invoke Test Spec Generator

Delegate to `test-spec-generator` sub-agent with:
- Approved test specification
- Test framework (from Phase 3)
- Project conventions
- TDD skill reference

### Create Test Files

Follow detected conventions:
- File naming (*.test.ts, *.spec.js, test_*.py)
- Directory structure (co-located, __tests__, tests/)
- Import style

### Test File Template

```typescript
/**
 * Test Suite: [Component/Feature]
 * Generated from: plans/sessions/{session}/specs/test-specification.md
 *
 * These tests define EXPECTED behavior before implementation.
 * All tests should FAIL initially - passing means implementation is complete.
 */

describe('[Component/Feature]', () => {
  describe('[function/method]', () => {
    // From REQ-1: [Requirement description]
    it('should [expected behavior] (T1)', () => {
      // Arrange
      const input = /* test data */;

      // Act
      const result = functionUnderTest(input);

      // Assert
      expect(result).toBe(/* expected */);
    });

    // Edge case: E1
    it('should handle [edge case]', () => {
      expect(/* ... */).toBe(/* ... */);
    });

    // Error scenario: ERR1
    it('should throw when [error condition]', () => {
      expect(() => functionUnderTest(invalidInput))
        .toThrow(ExpectedError);
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

## Phase 6: Complete

### Update Session Tracking

Update `session.md`:
```markdown
**Current Phase:** Test Specification Complete

## Requirements
- Documented in: specs/requirements.md

## Test Specification
- Documented in: specs/test-specification.md

## Test Files Generated
- [list of files]

## Test Summary
- Total Tests: [N]
- All tests currently FAILING (expected)

## Ready For
- `/research:plan` to create implementation plan
```

### Announce Completion

```
TEST SPECIFICATION COMPLETE

Requirements gathered and tests generated.

Session: plans/sessions/{date}-{task}/
├── specs/requirements.md       ✓
├── specs/test-specification.md ✓
└── [test files]                ✓

Generated: {N} failing tests in {M} files

Test Files:
- [file1] (X tests)
- [file2] (Y tests)

All tests are failing as expected (no implementation yet).

Next Steps:
→ /research:plan [session-path] - Create implementation plan to make tests pass
→ /execute [session-path] - Skip planning, implement directly (not recommended)
```

---

## Quality Gates

### Before Test Generation
- [ ] Codebase research complete
- [ ] User questions answered
- [ ] Requirements document created
- [ ] Requirements approved by user
- [ ] Test framework identified
- [ ] Test conventions documented
- [ ] Test specification approved by user

### After Test Generation
- [ ] All test files created
- [ ] Tests run without syntax errors
- [ ] Tests FAIL (not pass, not error)
- [ ] Failure reason is "missing implementation"
- [ ] Tests map to requirements

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

### Research not found
```
Codebase research not found.
Running research phase first...
→ Invoking /research:codebase
```

### Tests pass immediately
```
WARNING: Test passed immediately!
This means you're testing existing behavior, not new behavior.
Revise test to assert on MISSING functionality.
```

### User skips blocking questions
```
The following blocking questions must be answered before proceeding:
1. [Question]
2. [Question]

Please provide answers or accept the default assumptions.
```

---

## Example Usage

### From Fresh Start
```
/research:feature Add user authentication with JWT tokens

→ No research found, invoking /research:codebase first...
→ Research complete
→ Entering questioning phase...
→ [Brainstorming dialogue with user]
→ Requirements captured in specs/requirements.md
→ Generating test specification...
→ [User approves specification]
→ Creating test files:
  - src/auth/__tests__/login.test.ts (8 tests)
  - src/auth/__tests__/token.test.ts (7 tests)
→ Verifying all tests fail correctly ✓
→ Ready for /research:plan
```

### From Existing Session
```
/research:feature plans/sessions/2024-01-15-auth/

→ Loading research findings...
→ Found: codebase-map.md, patterns.md
→ Entering questioning phase...
→ [Brainstorming dialogue with user]
→ Requirements captured
→ Test specification generated
→ Test files created
→ Ready for /research:plan
```

---

## Related Commands

| Command | Purpose |
|---------|---------|
| `/research:codebase` | Phase 1: Codebase research |
| `/research:plan` | Phase 3: Implementation planning |
| `/execute` | Implementation phase |
| `/code-check` | Validation phase |
