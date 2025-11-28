---
applyTo: "**/*.md"
---

# Documentation Standards

These standards define how all documentation should be written, structured, and formatted across the project.

## Core Principles

1. **Clarity First**: Write for developers who are new to the codebase
2. **Consistency**: Follow established patterns throughout all documentation
3. **Completeness**: Include all necessary information without being verbose
4. **Currency**: Keep documentation up-to-date with code changes

## Document Structure

### Required Sections

Every documentation file MUST include:

1. **Title** (H1): Clear, descriptive name
2. **Overview**: 2-3 sentence summary of what this document covers
3. **Table of Contents**: For documents longer than 3 sections
4. **Main Content**: Organized with proper heading hierarchy
5. **Examples**: Practical code examples where applicable

### Heading Hierarchy

```markdown
# Title (H1) - Only one per document
## Major Section (H2)
### Subsection (H3)
#### Detail Section (H4) - Use sparingly
```

## Writing Style

### Voice and Tone

- Use **active voice**: "The function returns a value" not "A value is returned"
- Use **second person**: "You can configure..." not "Users can configure..."
- Be **direct**: "Run the command" not "You should run the command"
- Stay **professional** but approachable

### Technical Writing Guidelines

- Define acronyms on first use: "Application Programming Interface (API)"
- Use consistent terminology throughout
- Avoid jargon unless necessary for the audience
- Include context for code references

### Sentence Structure

- Keep sentences under 25 words when possible
- One idea per sentence
- Use bullet points for lists of 3+ items
- Use numbered lists for sequential steps

## Code Examples

### Formatting Standards

Always use fenced code blocks with language specification:

```typescript
// Good: Language specified, includes context
function calculateTotal(items: Item[]): number {
  return items.reduce((sum, item) => sum + item.price, 0);
}
```

### Code Example Requirements

1. **Runnable**: Examples should work when copied
2. **Complete**: Include necessary imports and context
3. **Commented**: Add inline comments for complex logic
4. **Realistic**: Use meaningful variable names and realistic data

### Bad vs Good Examples

❌ **Bad Example**:
```javascript
function f(x) {
  return x.map(i => i.a + i.b);
}
```

✅ **Good Example**:
```javascript
/**
 * Calculates the total price for each order line item.
 * @param orderItems - Array of order items with unitPrice and quantity
 * @returns Array of calculated totals
 */
function calculateLineTotals(orderItems) {
  return orderItems.map(item => item.unitPrice * item.quantity);
}
```

## API Documentation

### Function Documentation Format

```typescript
/**
 * Brief description of what the function does.
 *
 * @description Longer description if needed, explaining the purpose
 * and any important behavior details.
 *
 * @param paramName - Description of the parameter
 * @param optionalParam - Description (optional, defaults to X)
 * @returns Description of return value
 * @throws {ErrorType} When this error condition occurs
 *
 * @example
 * // Example usage with expected output
 * const result = functionName('input');
 * console.log(result); // 'expected output'
 */
```

### Class Documentation Format

```typescript
/**
 * Brief description of the class purpose.
 *
 * @description Detailed explanation of the class responsibility,
 * when to use it, and any important patterns.
 *
 * @example
 * const instance = new ClassName(config);
 * instance.doSomething();
 */
```

## File Organization

### README Files

Every directory should have a README.md with:

1. **Purpose**: What this directory contains
2. **Contents**: Brief description of key files
3. **Usage**: How to use or navigate the contents
4. **Related**: Links to related documentation

### Documentation File Naming

- Use kebab-case: `api-reference.md`, `getting-started.md`
- Be descriptive: `user-authentication.md` not `auth.md`
- Group related docs: `api/`, `guides/`, `tutorials/`

## Markdown Formatting

### Links

- Use descriptive link text: write `[API Reference]` not `[click here]`
- Use relative paths for internal links
- Check links are valid before committing

### Tables

Use tables for structured data:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | `string` | Yes | Unique identifier |
| `name` | `string` | No | Display name |

### Callouts and Emphasis

Use blockquotes for important notes:

> **Note**: Important information the reader should know.

> **Warning**: Critical information about potential issues.

> **Tip**: Helpful suggestions for better usage.

## Maintenance

### Review Checklist

Before submitting documentation:

- [ ] Spelling and grammar checked
- [ ] All code examples tested
- [ ] Links verified
- [ ] Consistent formatting applied
- [ ] Table of contents updated (if applicable)
- [ ] Related documents cross-referenced

### Version Considerations

- Note version-specific behavior
- Mark deprecated features clearly
- Include migration guides for breaking changes
