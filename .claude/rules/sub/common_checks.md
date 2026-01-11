# Common Checks Sub-Rule (Tier 3)
## Purpose
Provides shared validation patterns and quality checks used across multiple rules and skills.

## CODE QUALITY PATTERNS

### Import Organization
**STANDARD STRUCTURE**:
```python
# Standard library imports
import os
import sys
from typing import Dict, List, Optional

# Third-party imports
import requests
from fastapi import FastAPI
import sqlalchemy as sa

# Local imports
from .models import User
from ..utils import helpers
```

**Validation Rules**:
- [ ] Standard library first, alphabetically sorted
- [ ] Third-party imports second, alphabetically sorted
- [ ] Local imports last, relative imports properly formatted
- [ ] No wildcard imports (from module import *)
- [ ] Import aliases follow project conventions

### Type Hint Completeness
**REQUIRED ANNOTATIONS**:
```python
def process_user(user_id: int, data: Dict[str, Any]) -> Optional[User]:
    pass

class UserService:
    def __init__(self, db: Database) -> None:
        pass

    def get_user(self, user_id: int) -> User | None:
        pass
```

**Validation Rules**:
- [ ] All function parameters typed
- [ ] All function return values typed
- [ ] Class attributes typed in __init__
- [ ] Complex types use Union, Optional, List, Dict appropriately
- [ ] Generic types properly parameterized

### Error Handling Standards
**CONSISTENT PATTERNS**:
```python
try:
    result = risky_operation()
except SpecificException as e:
    logger.error(f"Operation failed: {e}")
    raise DomainException("User-friendly message") from e
except Exception as e:
    logger.exception("Unexpected error")
    raise SystemException("System error occurred") from e
```

**Validation Rules**:
- [ ] Specific exceptions caught before generic Exception
- [ ] Custom domain exceptions defined and used
- [ ] Logging includes context and error details
- [ ] Exception chaining with 'from e' maintained
- [ ] User-friendly messages in domain exceptions

## PERFORMANCE PATTERNS

### Database Query Optimization
**EFFICIENCY CHECKS**:
```python
# GOOD: Single query with joins
users = session.query(User).join(Profile).filter(
    Profile.active == True
).all()

# AVOID: N+1 queries
users = session.query(User).all()
for user in users:  # N additional queries
    profile = user.profile
```

**Validation Rules**:
- [ ] N+1 query patterns eliminated
- [ ] Proper indexing on frequently queried columns
- [ ] Select only required columns, not entire objects
- [ ] Query result caching for repeated reads
- [ ] Connection pooling properly configured

### Memory Management
**RESOURCE EFFICIENCY**:
```python
# GOOD: Context managers for resource cleanup
with open('file.txt', 'r') as f:
    content = f.read()

# GOOD: Generator for large datasets
def process_large_file(file_path: str):
    with open(file_path, 'r') as f:
        for line in f:  # Memory efficient
            yield process_line(line)
```

**Validation Rules**:
- [ ] Files opened with context managers
- [ ] Large datasets processed with generators
- [ ] Memory-intensive operations profiled
- [ ] Object references cleared when no longer needed
- [ ] Circular references avoided

### Async/Await Discipline
**CORRECT USAGE PATTERNS**:
```python
# GOOD: Proper async function definition
async def fetch_user(user_id: int) -> User:
    async with session.begin():
        result = await session.execute(
            select(User).where(User.id == user_id)
        )
        return result.scalar_one()

# GOOD: Sync wrapper for async calls
def get_user_sync(user_id: int) -> User:
    return asyncio.run(fetch_user(user_id))
```

**Validation Rules**:
- [ ] Async functions suffixed with _async for clarity
- [ ] Async context managers used for database sessions
- [ ] Blocking calls wrapped in asyncio.run() or run_in_executor()
- [ ] Async functions called with await keyword
- [ ] Event loop management centralized

## SECURITY VALIDATION PATTERNS

### Input Sanitization
**REQUIRED CHECKS**:
```python
from pydantic import BaseModel, validator
import bleach

class UserInput(BaseModel):
    username: str
    email: str

    @validator('username')
    def sanitize_username(cls, v):
        # Remove potentially harmful characters
        return bleach.clean(v, strip=True)

    @validator('email')
    def validate_email(cls, v):
        # Email format validation
        if '@' not in v:
            raise ValueError('Invalid email format')
        return v.lower()
```

**Validation Rules**:
- [ ] All external inputs validated and sanitized
- [ ] SQL injection prevention (parameterized queries)
- [ ] XSS prevention (output encoding)
- [ ] CSRF protection implemented
- [ ] Rate limiting on sensitive endpoints

### Authentication & Authorization
**ACCESS CONTROL**:
```python
from functools import wraps
from flask import g, request, abort

def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            abort(401)

        user = validate_token(token)
        if not user:
            abort(401)

        g.user = user
        return f(*args, **kwargs)
    return decorated

def require_permission(permission: str):
    def decorator(f):
        @wraps(f)
        @require_auth
        def decorated(*args, **kwargs):
            if not g.user.has_permission(permission):
                abort(403)
            return f(*args, **kwargs)
        return decorated
    return decorator
```

**Validation Rules**:
- [ ] Authentication required for protected endpoints
- [ ] Authorization checks based on user roles/permissions
- [ ] Session management secure and timeout-configured
- [ ] Password policies enforced
- [ ] Multi-factor authentication available

## DOCUMENTATION STANDARDS

### Code Documentation
**REQUIRED ELEMENTS**:
```python
def calculate_total(items: List[Item]) -> Decimal:
    """
    Calculate the total cost of a list of items including tax.

    This function iterates through all items, sums their base prices,
    applies the appropriate tax rate based on item categories,
    and returns the final total as a Decimal for precision.

    Args:
        items: List of Item objects to total. Each item must have
               a price attribute (Decimal) and category (str).

    Returns:
        The total cost including tax as a Decimal.

    Raises:
        ValueError: If any item has invalid price or category.
        EmptyListError: If items list is empty.

    Example:
        >>> items = [Item(price=10.00, category='book')]
        >>> calculate_total(items)
        Decimal('10.75')
    """
    pass
```

**Validation Rules**:
- [ ] All public functions documented with docstrings
- [ ] Parameters and return values described
- [ ] Exceptions documented
- [ ] Usage examples provided
- [ ] Complex logic explained

### API Documentation
**OPENAPI COMPLIANCE**:
```yaml
paths:
  /users/{userId}:
    get:
      summary: Get user by ID
      parameters:
        - name: userId
          in: path
          required: true
          schema:
            type: integer
      responses:
        '200':
          description: User found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
        '404':
          description: User not found
```

**Validation Rules**:
- [ ] All endpoints documented in OpenAPI format
- [ ] Request/response schemas defined
- [ ] Error responses documented
- [ ] Authentication requirements specified
- [ ] Rate limiting documented

## LOGGING PATTERNS

### Structured Logging
**CONSISTENT FORMAT**:
```python
import logging
import json

logger = logging.getLogger(__name__)

def process_payment(user_id: int, amount: Decimal):
    logger.info(
        "Processing payment",
        extra={
            'user_id': user_id,
            'amount': str(amount),  # Convert for JSON serialization
            'operation': 'payment_processing',
            'correlation_id': get_correlation_id()
        }
    )

    try:
        # Process payment logic
        result = payment_gateway.charge(amount)
        logger.info(
            "Payment successful",
            extra={
                'user_id': user_id,
                'transaction_id': result.transaction_id,
                'amount': str(amount),
                'status': 'success'
            }
        )
        return result
    except PaymentError as e:
        logger.error(
            "Payment failed",
            exc_info=True,
            extra={
                'user_id': user_id,
                'amount': str(amount),
                'error_code': e.code,
                'status': 'failed'
            }
        )
        raise
```

**Validation Rules**:
- [ ] Structured logging with consistent key names
- [ ] Correlation IDs for request tracing
- [ ] Appropriate log levels (DEBUG, INFO, WARNING, ERROR)
- [ ] Sensitive data not logged
- [ ] Exception information included in error logs
- [ ] Performance impact minimized

## TESTING PATTERNS

### Unit Test Structure
**STANDARD FORMAT**:
```python
import pytest
from unittest.mock import Mock, patch

class TestUserService:
    def setup_method(self):
        self.service = UserService()

    def test_get_user_success(self):
        # Arrange
        user_id = 123
        expected_user = User(id=user_id, name="Test User")

        with patch.object(self.service.db, 'query') as mock_query:
            mock_query.return_value.get.return_value = expected_user

            # Act
            result = self.service.get_user(user_id)

            # Assert
            assert result == expected_user
            mock_query.assert_called_once()

    def test_get_user_not_found(self):
        # Arrange
        user_id = 999

        with patch.object(self.service.db, 'query') as mock_query:
            mock_query.return_value.get.return_value = None

            # Act & Assert
            with pytest.raises(UserNotFoundError):
                self.service.get_user(user_id)
```

**Validation Rules**:
- [ ] Test class names prefixed with 'Test'
- [ ] Test method names descriptive and prefixed with 'test_'
- [ ] Arrange-Act-Assert pattern followed
- [ ] Mocks used appropriately for external dependencies
- [ ] Edge cases and error conditions tested
- [ ] Test isolation maintained

### Integration Test Standards
**END-TO-END VALIDATION**:
```python
def test_user_registration_flow(client, db_session):
    # Test complete user registration workflow
    user_data = {
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'securepassword123'
    }

    # Register user
    response = client.post('/api/users/register', json=user_data)
    assert response.status_code == 201

    # Verify user created in database
    user = db_session.query(User).filter_by(username='testuser').first()
    assert user is not None
    assert user.email == 'test@example.com'

    # Test login
    login_data = {
        'username': 'testuser',
        'password': 'securepassword123'
    }
    response = client.post('/api/auth/login', json=login_data)
    assert response.status_code == 200

    # Verify token received
    data = response.get_json()
    assert 'access_token' in data
```

**Validation Rules**:
- [ ] Database state properly initialized and cleaned up
- [ ] API endpoints tested with realistic data
- [ ] Authentication and authorization tested
- [ ] Error conditions and edge cases covered
- [ ] Test data isolated from production data
