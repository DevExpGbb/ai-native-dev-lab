---
name: generate-docs
description: Generate comprehensive documentation for code files, functions, or modules
agent: agent
tools:
  - search
  - usages
  - fetch
  - edit/createFile
  - search/codebase
---

# Generate Documentation

Generate comprehensive, standards-compliant documentation for the specified code.

## Context

Use the documentation standards defined in:
- [Documentation Standards](../instructions/documentation-standards.instructions.md)

## Input

### Target Code
${file}

### Specific Selection (if any)
${selection}

## Task

Analyze the provided code and generate appropriate documentation following these steps:

### 1. Code Analysis

First, understand the code by identifying:
- **Purpose**: What problem does this code solve?
- **Public API**: What functions, classes, or methods are exported?
- **Dependencies**: What does this code depend on?
- **Complexity**: Are there complex algorithms or patterns that need explanation?

### 2. Documentation Type Selection

Based on the code, determine what documentation to create:

| Code Type | Documentation Output |
|-----------|---------------------|
| Single function | JSDoc/TSDoc comments + usage example |
| Class/Module | API reference document |
| Feature/Component | Guide with examples |
| Utility library | Reference + cookbook |

### 3. Documentation Generation

Generate documentation that includes:

#### For Functions/Methods
```typescript
/**
 * [Brief description - one line]
 *
 * [Detailed description - when to use, important behavior]
 *
 * @param paramName - [Description with type info if not in signature]
 * @returns [Description of return value]
 * @throws {ErrorType} [When this error occurs]
 *
 * @example
 * [Practical usage example]
 */
```

#### For Classes/Modules
Create a markdown document with:
1. Overview section
2. Installation/Import instructions
3. API Reference (all public members)
4. Usage Examples
5. Error Handling
6. Related Resources

#### For Components
Include:
1. Component purpose
2. Props/Configuration options
3. Usage examples
4. Styling information
5. Accessibility notes

## Output Format

### Inline Documentation
Add directly to the source file using appropriate comment format:
- TypeScript/JavaScript: JSDoc (`/** */`)
- Python: Docstrings (`"""`)
- Other: Language-appropriate format

### External Documentation
Create markdown files in the appropriate location:
- API docs: `docs/api/[module-name].md`
- Guides: `docs/guides/[topic].md`
- README: Same directory as the code

## Quality Checklist

Ensure generated documentation:
- [ ] Follows the documentation standards
- [ ] Uses active voice and clear language
- [ ] Includes working code examples
- [ ] Covers error cases and edge conditions
- [ ] Has proper formatting and structure
- [ ] Links to related documentation

## Example Output

For a utility function, generate:

```typescript
/**
 * Formats a date string according to the specified locale and options.
 *
 * Handles timezone conversion automatically and provides sensible defaults
 * for common formatting scenarios. Invalid dates return a fallback string.
 *
 * @param date - The date to format (Date object, timestamp, or ISO string)
 * @param options - Formatting options
 * @param options.locale - BCP 47 locale string (default: 'en-US')
 * @param options.format - Predefined format: 'short', 'long', 'relative'
 * @returns Formatted date string, or 'Invalid Date' if parsing fails
 *
 * @example
 * // Basic usage
 * formatDate(new Date()); // "Nov 28, 2025"
 *
 * @example
 * // With options
 * formatDate('2025-11-28', { locale: 'de-DE', format: 'long' });
 * // "28. November 2025"
 */
export function formatDate(
  date: Date | number | string,
  options?: FormatOptions
): string {
  // Implementation
}
```
