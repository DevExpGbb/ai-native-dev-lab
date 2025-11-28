---
applyTo: "**/*.test.{js,ts,jsx,tsx,py}"
---

# Testing Standards

This document defines the testing standards and best practices for all test files in this project. Follow these guidelines to ensure consistent, maintainable, and effective tests.

## Core Testing Principles

### 1. Test Structure (Arrange-Act-Assert)

Every test should follow the AAA pattern for clarity and consistency:

```typescript
it('should calculate total with tax', () => {
  // Arrange - Set up test data and preconditions
  const cart = new ShoppingCart();
  cart.addItem({ name: 'Widget', price: 100 });
  const taxRate = 0.08;

  // Act - Execute the code under test
  const total = cart.calculateTotal(taxRate);

  // Assert - Verify the expected outcome
  expect(total).toBe(108);
});
```

### 2. Describe Block Organization

Organize tests using nested describe blocks that mirror the code structure:

```typescript
describe('ShoppingCart', () => {
  describe('addItem', () => {
    it('should add item to empty cart', () => { /* ... */ });
    it('should increment quantity for existing item', () => { /* ... */ });
  });

  describe('calculateTotal', () => {
    it('should return 0 for empty cart', () => { /* ... */ });
    it('should sum all item prices', () => { /* ... */ });
    it('should apply tax rate correctly', () => { /* ... */ });
  });
});
```

## Naming Conventions

### Test File Naming

- **JavaScript/TypeScript**: `{filename}.test.ts` or `{filename}.spec.ts`
- **Python**: `test_{filename}.py`
- Place test files adjacent to source files or in a parallel `tests/` directory

### Test Case Naming

Use descriptive names that explain the scenario and expected outcome:

```typescript
// ✅ Good - Clear scenario and expectation
it('should throw ValidationError when email format is invalid', () => {});
it('should return empty array when no users match filter', () => {});
it('should retry request up to 3 times on network failure', () => {});

// ❌ Bad - Vague or implementation-focused
it('works', () => {});
it('test email', () => {});
it('calls the function', () => {});
```

### Pattern Templates

Follow these naming patterns:

- `should {expected behavior} when {condition}`
- `should {expected behavior} given {precondition}`
- `should not {behavior} if {condition}`

## Coverage Requirements

### Minimum Coverage Targets

| Metric     | Minimum | Target |
|------------|---------|--------|
| Statements | 80%     | 90%    |
| Branches   | 75%     | 85%    |
| Functions  | 80%     | 90%    |
| Lines      | 80%     | 90%    |

### What to Cover

- ✅ All public functions and methods
- ✅ All conditional branches (if/else, switch cases)
- ✅ Error handling paths
- ✅ Edge cases (null, undefined, empty, boundary values)
- ✅ Integration points with external systems

### What NOT to Cover

- ❌ Third-party library code
- ❌ Simple getters/setters without logic
- ❌ Configuration files
- ❌ Type definitions

## Mocking and Isolation

### Isolation Principles

1. **Unit tests should be isolated** - Mock all external dependencies
2. **Test one thing at a time** - Each test should verify a single behavior
3. **Avoid shared state** - Reset mocks and state between tests

### Mocking Best Practices

```typescript
// ✅ Good - Mock at the boundary
const mockUserRepository = {
  findById: jest.fn(),
  save: jest.fn(),
};

const userService = new UserService(mockUserRepository);

// ✅ Good - Clear mock setup per test
beforeEach(() => {
  jest.clearAllMocks();
});

it('should return user when found', async () => {
  mockUserRepository.findById.mockResolvedValue({ id: 1, name: 'Alice' });
  
  const user = await userService.getUser(1);
  
  expect(user.name).toBe('Alice');
  expect(mockUserRepository.findById).toHaveBeenCalledWith(1);
});
```

### What to Mock

- ✅ Database connections and queries
- ✅ HTTP/API calls
- ✅ File system operations
- ✅ Time-dependent functions (Date, timers)
- ✅ Random number generation
- ✅ External service clients

### What NOT to Mock

- ❌ The code under test
- ❌ Simple utility functions without side effects
- ❌ Data transformation logic

## Test Data Management

### Use Factory Functions

```typescript
// ✅ Good - Factory function for test data
const createUser = (overrides = {}) => ({
  id: 1,
  name: 'Test User',
  email: 'test@example.com',
  createdAt: new Date('2024-01-01'),
  ...overrides,
});

it('should format user display name', () => {
  const user = createUser({ name: 'Alice Smith' });
  expect(formatDisplayName(user)).toBe('Alice S.');
});
```

### Avoid Magic Values

```typescript
// ✅ Good - Named constants explain intent
const VALID_EMAIL = 'user@example.com';
const INVALID_EMAIL = 'not-an-email';
const MAX_RETRY_ATTEMPTS = 3;

// ❌ Bad - Magic values without context
expect(result).toBe(3);
expect(email).toMatch('test@test.com');
```

## Async Testing

### Handle Promises Correctly

```typescript
// ✅ Good - Return the promise or use async/await
it('should fetch user data', async () => {
  const user = await userService.fetchUser(1);
  expect(user.name).toBe('Alice');
});

// ✅ Good - Test rejection
it('should throw when user not found', async () => {
  await expect(userService.fetchUser(999))
    .rejects
    .toThrow('User not found');
});
```

### Use Proper Timeout Handling

```typescript
// ✅ Good - Use fake timers for time-dependent tests
beforeEach(() => {
  jest.useFakeTimers();
});

afterEach(() => {
  jest.useRealTimers();
});

it('should timeout after 5 seconds', () => {
  const callback = jest.fn();
  startTimeout(callback);
  
  jest.advanceTimersByTime(5000);
  
  expect(callback).toHaveBeenCalledWith('timeout');
});
```

## Error Testing

### Test Error Conditions Explicitly

```typescript
describe('error handling', () => {
  it('should throw ValidationError for invalid input', () => {
    expect(() => validateEmail('')).toThrow(ValidationError);
  });

  it('should include field name in error message', () => {
    expect(() => validateEmail('')).toThrow('email is required');
  });

  it('should handle network errors gracefully', async () => {
    mockApi.get.mockRejectedValue(new NetworkError('Connection failed'));
    
    const result = await fetchWithRetry('/users');
    
    expect(result.error).toBe('Unable to connect. Please try again.');
  });
});
```

## Python-Specific Guidelines

### Use pytest Conventions

```python
# ✅ Good - pytest style
import pytest
from mymodule import calculate_tax

class TestCalculateTax:
    def test_calculates_standard_rate(self):
        result = calculate_tax(100, rate=0.08)
        assert result == 8.0

    def test_raises_for_negative_amount(self):
        with pytest.raises(ValueError, match="Amount must be positive"):
            calculate_tax(-100, rate=0.08)

    @pytest.fixture
    def sample_invoice(self):
        return Invoice(amount=100, tax_rate=0.08)

    def test_invoice_total(self, sample_invoice):
        assert sample_invoice.total == 108.0
```

### Use Fixtures for Setup

```python
@pytest.fixture
def mock_database(mocker):
    return mocker.patch('mymodule.database.connect')

@pytest.fixture
def user_service(mock_database):
    return UserService(database=mock_database)

def test_creates_user(user_service, mock_database):
    user_service.create_user("alice@example.com")
    mock_database.insert.assert_called_once()
```

## Anti-Patterns to Avoid

### ❌ Testing Implementation Details

```typescript
// ❌ Bad - Tests internal state
it('should set _isLoading to true', () => {
  component.fetchData();
  expect(component._isLoading).toBe(true);
});

// ✅ Good - Tests observable behavior
it('should show loading spinner while fetching', () => {
  component.fetchData();
  expect(screen.getByRole('progressbar')).toBeVisible();
});
```

### ❌ Interdependent Tests

```typescript
// ❌ Bad - Test B depends on Test A's side effects
it('A: should create user', () => { /* creates user */ });
it('B: should find created user', () => { /* finds user from A */ });

// ✅ Good - Each test is independent
it('should find existing user', () => {
  const user = createUser({ id: 1 }); // Arrange in each test
  const found = findUser(1);
  expect(found).toEqual(user);
});
```

### ❌ Overly Complex Setup

If your test setup is longer than the test itself, consider:
- Breaking the code into smaller, more testable units
- Using factory functions or fixtures
- Refactoring the production code for better testability

## Checklist for Every Test

- [ ] Follows AAA pattern (Arrange-Act-Assert)
- [ ] Has a descriptive name explaining scenario and expectation
- [ ] Tests one specific behavior
- [ ] Is isolated from other tests
- [ ] Cleans up after itself
- [ ] Runs quickly (< 100ms for unit tests)
- [ ] Doesn't depend on external systems
- [ ] Has clear assertions with good error messages
