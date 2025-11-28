---
name: generate-tests
description: Generate comprehensive unit tests for the selected code following project testing standards
agent: agent
tools:
  - search
  - createFile
  - usages
---

# Generate Unit Tests

Generate comprehensive unit tests for the provided code following the project's testing standards.

## Context

**Source File:** ${file}

**Code to Test:**
```
${selection}
```

## Instructions

Follow the testing standards defined in:
- [Testing Standards](../instructions/testing-standards.instructions.md)

### Analysis Phase

1. **Identify the code type:**
   - Function/method
   - Class
   - Module/component
   - API endpoint

2. **Determine what to test:**
   - All public functions and methods
   - Input validation
   - Return values and output
   - Error handling and edge cases
   - Side effects (if any)

3. **Identify dependencies to mock:**
   - External API calls
   - Database operations
   - File system access
   - Third-party libraries

### Test Generation Requirements

1. **File Location:**
   - Place test file adjacent to source file
   - Use naming convention: `{filename}.test.{ext}` or `test_{filename}.py`

2. **Test Structure:**
   - Use describe/it blocks (JS/TS) or TestClass/test_ methods (Python)
   - Follow Arrange-Act-Assert pattern
   - Group related tests logically

3. **Coverage Goals:**
   - Happy path scenarios
   - Edge cases (null, undefined, empty, boundary values)
   - Error conditions and exceptions
   - Async behavior (if applicable)

4. **Test Cases to Include:**
   - Input validation tests
   - Expected output tests
   - Error handling tests
   - Boundary condition tests
   - Integration point tests (mocked)

### Output Format

Generate a complete test file with:

```
// File: {test-file-path}

// 1. Imports (testing framework, mocks, source code)
// 2. Mock setup (if needed)
// 3. Test suites organized by function/method
// 4. Individual test cases following naming conventions
```

### Framework Detection

- **TypeScript/JavaScript:** Use Jest or Vitest based on project config
- **Python:** Use pytest
- **React Components:** Use React Testing Library
- **API Endpoints:** Use supertest or httpx

### Example Output Structure

For a TypeScript function:

```typescript
import { describe, it, expect, beforeEach, jest } from '@jest/globals';
import { functionName } from './source-file';

describe('functionName', () => {
  describe('when given valid input', () => {
    it('should return expected result', () => {
      // Arrange
      const input = createValidInput();
      
      // Act
      const result = functionName(input);
      
      // Assert
      expect(result).toEqual(expectedOutput);
    });
  });

  describe('when given invalid input', () => {
    it('should throw ValidationError', () => {
      expect(() => functionName(null)).toThrow(ValidationError);
    });
  });

  describe('edge cases', () => {
    it('should handle empty array', () => { /* ... */ });
    it('should handle maximum values', () => { /* ... */ });
  });
});
```

## Task

1. Analyze the provided code to understand its purpose and behavior
2. Identify all testable scenarios (happy paths, edge cases, errors)
3. Generate a complete test file with comprehensive coverage
4. Include appropriate mocks for any external dependencies
5. Add clear comments explaining complex test scenarios

Create the test file at the appropriate location following project conventions.
