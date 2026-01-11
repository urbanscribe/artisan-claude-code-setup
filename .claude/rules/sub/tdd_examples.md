# TDD Examples Sub-Rule (Tier 3)
## Purpose
Provides concrete test structure examples and TDD implementation patterns for consistent testing practices.

## UNIT TEST PATTERNS

### Basic Unit Test Structure
**STANDARD FORMAT**:
```python
# tests/test_user_service.py
import pytest
from unittest.mock import Mock, patch
from app.services.user_service import UserService
from app.models.user import User


class TestUserService:
    """Test cases for UserService following TDD principles."""

    def setup_method(self):
        """Set up test fixtures before each test."""
        self.service = UserService()
        self.mock_db = Mock()
        self.service.db = self.mock_db

    def test_create_user_success(self):
        """Test successful user creation."""
        # Arrange
        user_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'securepass123'
        }
        expected_user = User(id=1, **user_data)

        self.mock_db.add.return_value = None
        self.mock_db.commit.return_value = None
        self.mock_db.refresh.return_value = expected_user

        # Act
        result = self.service.create_user(user_data)

        # Assert
        assert result.id == 1
        assert result.username == 'testuser'
        assert result.email == 'test@example.com'
        self.mock_db.add.assert_called_once()
        self.mock_db.commit.assert_called_once()

    def test_create_user_duplicate_username(self):
        """Test user creation with duplicate username fails."""
        # Arrange
        user_data = {'username': 'existing', 'email': 'test@example.com'}

        from app.errors import ValidationError
        self.mock_db.add.side_effect = ValidationError("Username already exists")

        # Act & Assert
        with pytest.raises(ValidationError, match="Username already exists"):
            self.service.create_user(user_data)

        self.mock_db.rollback.assert_called_once()

    def test_get_user_by_id_found(self):
        """Test retrieving existing user by ID."""
        # Arrange
        user_id = 123
        expected_user = User(id=user_id, username='testuser')

        self.mock_db.query.return_value.get.return_value = expected_user

        # Act
        result = self.service.get_user_by_id(user_id)

        # Assert
        assert result == expected_user
        self.mock_db.query.assert_called_once()

    def test_get_user_by_id_not_found(self):
        """Test retrieving non-existent user returns None."""
        # Arrange
        user_id = 999
        self.mock_db.query.return_value.get.return_value = None

        # Act
        result = self.service.get_user_by_id(user_id)

        # Assert
        assert result is None
```

### TDD Cycle Demonstration
**RED-GREEN-REFACTOR PATTERN**:
```python
# Step 1: RED - Write failing test first
def test_calculate_total_with_tax(self):
    """Calculate total with tax - initially fails."""
    service = PricingService()
    items = [Item(price=10.00, taxable=True)]

    # This will fail initially - no implementation yet
    result = service.calculate_total(items)

    assert result == 10.75  # 10.00 + 7.5% tax

# Step 2: GREEN - Minimal implementation to pass
def calculate_total(self, items: List[Item]) -> Decimal:
    """Calculate total with minimal tax implementation."""
    subtotal = sum(item.price for item in items)
    # Hard-coded tax rate - will refactor later
    return subtotal * Decimal('1.075')

# Step 3: REFACTOR - Improve implementation while maintaining tests
TAX_RATE = Decimal('0.075')

def calculate_total(self, items: List[Item]) -> Decimal:
    """Calculate total with proper tax implementation."""
    subtotal = sum(item.price for item in items)
    taxable_amount = sum(
        item.price for item in items
        if item.taxable
    )
    tax = taxable_amount * TAX_RATE
    return subtotal + tax
```

## INTEGRATION TEST PATTERNS

### API Endpoint Testing
**END-TO-END VALIDATION**:
```python
# tests/integration/test_user_api.py
import pytest
import json
from app import create_app


class TestUserAPI:
    """Integration tests for user API endpoints."""

    def setup_method(self):
        """Set up test client and database."""
        self.app = create_app('testing')
        self.client = self.app.test_client()
        with self.app.app_context():
            # Set up test database
            pass

    def test_create_user_api_success(self):
        """Test successful user creation via API."""
        # Arrange
        user_data = {
            'username': 'apiuser',
            'email': 'api@example.com',
            'password': 'securepass123'
        }

        # Act
        response = self.client.post(
            '/api/users',
            data=json.dumps(user_data),
            content_type='application/json'
        )

        # Assert
        assert response.status_code == 201
        data = json.loads(response.data)
        assert data['username'] == 'apiuser'
        assert data['email'] == 'api@example.com'
        assert 'id' in data
        assert 'password' not in data  # Should not return password

    def test_get_user_api_not_found(self):
        """Test retrieving non-existent user via API."""
        # Act
        response = self.client.get('/api/users/999')

        # Assert
        assert response.status_code == 404
        data = json.loads(response.data)
        assert 'error' in data
        assert 'not found' in data['error'].lower()

    def test_user_list_pagination(self):
        """Test user list with pagination."""
        # Arrange - create multiple users
        users = []
        for i in range(5):
            user_data = {
                'username': f'user{i}',
                'email': f'user{i}@example.com',
                'password': 'pass123'
            }
            response = self.client.post(
                '/api/users',
                data=json.dumps(user_data),
                content_type='application/json'
            )
            users.append(json.loads(response.data))

        # Act - request paginated results
        response = self.client.get('/api/users?page=1&per_page=2')

        # Assert
        assert response.status_code == 200
        data = json.loads(response.data)
        assert len(data['users']) == 2
        assert data['pagination']['total'] == 5
        assert data['pagination']['page'] == 1
        assert data['pagination']['per_page'] == 2
```

## UI TESTING PATTERNS

### Component Testing with Testing Library
**REACT COMPONENT EXAMPLE**:
```javascript
// tests/components/test_UserProfile.test.js
import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import '@testing-library/jest-dom';
import UserProfile from '../../src/components/UserProfile';


describe('UserProfile Component', () => {
  const mockUser = {
    id: 1,
    username: 'testuser',
    email: 'test@example.com',
    profile: {
      firstName: 'Test',
      lastName: 'User',
      bio: 'A test user'
    }
  };

  const mockOnUpdate = jest.fn();

  beforeEach(() => {
    mockOnUpdate.mockClear();
  });

  test('renders user information correctly', () => {
    // Arrange
    render(<UserProfile user={mockUser} onUpdate={mockOnUpdate} />);

    // Assert
    expect(screen.getByText('testuser')).toBeInTheDocument();
    expect(screen.getByText('test@example.com')).toBeInTheDocument();
    expect(screen.getByText('Test User')).toBeInTheDocument();
    expect(screen.getByText('A test user')).toBeInTheDocument();
  });

  test('allows editing profile information', async () => {
    // Arrange
    render(<UserProfile user={mockUser} onUpdate={mockOnUpdate} />);

    // Act
    const editButton = screen.getByRole('button', { name: /edit/i });
    fireEvent.click(editButton);

    const firstNameInput = screen.getByLabelText(/first name/i);
    fireEvent.change(firstNameInput, { target: { value: 'Updated' } });

    const saveButton = screen.getByRole('button', { name: /save/i });
    fireEvent.click(saveButton);

    // Assert
    await waitFor(() => {
      expect(mockOnUpdate).toHaveBeenCalledWith({
        ...mockUser,
        profile: {
          ...mockUser.profile,
          firstName: 'Updated'
        }
      });
    });
  });

  test('validates email format', async () => {
    // Arrange
    render(<UserProfile user={mockUser} onUpdate={mockOnUpdate} />);

    // Act
    const editButton = screen.getByRole('button', { name: /edit/i });
    fireEvent.click(editButton);

    const emailInput = screen.getByLabelText(/email/i);
    fireEvent.change(emailInput, { target: { value: 'invalid-email' } });

    const saveButton = screen.getByRole('button', { name: /save/i });
    fireEvent.click(saveButton);

    // Assert
    await waitFor(() => {
      expect(screen.getByText(/invalid email format/i)).toBeInTheDocument();
    });
    expect(mockOnUpdate).not.toHaveBeenCalled();
  });
});
```

### E2E Testing with Playwright
**FULL USER JOURNEY**:
```javascript
// tests/e2e/test_user_registration.spec.js
const { test, expect } = require('@playwright/test');

test.describe('User Registration Flow', () => {
  test('successful user registration and login', async ({ page }) => {
    // Navigate to registration page
    await page.goto('/register');

    // Fill registration form
    await page.fill('[data-testid="username"]', 'e2euser');
    await page.fill('[data-testid="email"]', 'e2e@example.com');
    await page.fill('[data-testid="password"]', 'SecurePass123!');
    await page.fill('[data-testid="confirm-password"]', 'SecurePass123!');

    // Submit form
    await page.click('[data-testid="register-button"]');

    // Verify success message
    await expect(page.locator('[data-testid="success-message"]')).toBeVisible();
    await expect(page.locator('[data-testid="success-message"]')).toContainText('Registration successful');

    // Verify redirect to login or automatic login
    await expect(page).toHaveURL(/\/dashboard|\/login/);

    // If redirected to login, complete login
    if (page.url().includes('/login')) {
      await page.fill('[data-testid="username"]', 'e2euser');
      await page.fill('[data-testid="password"]', 'SecurePass123!');
      await page.click('[data-testid="login-button"]');

      await expect(page).toHaveURL('/dashboard');
    }

    // Verify user is logged in
    await expect(page.locator('[data-testid="user-menu"]')).toContainText('e2euser');
  });

  test('registration validation errors', async ({ page }) => {
    // Navigate to registration page
    await page.goto('/register');

    // Try to submit empty form
    await page.click('[data-testid="register-button"]');

    // Verify validation errors
    await expect(page.locator('[data-testid="username-error"]')).toBeVisible();
    await expect(page.locator('[data-testid="username-error"]')).toContainText('Username is required');

    await expect(page.locator('[data-testid="email-error"]')).toBeVisible();
    await expect(page.locator('[data-testid="email-error"]')).toContainText('Email is required');

    await expect(page.locator('[data-testid="password-error"]')).toBeVisible();
    await expect(page.locator('[data-testid="password-error"]')).toContainText('Password is required');

    // Fill form with invalid data
    await page.fill('[data-testid="username"]', 'us');
    await page.fill('[data-testid="email"]', 'invalid-email');
    await page.fill('[data-testid="password"]', '123');

    // Submit and verify field-specific errors
    await page.click('[data-testid="register-button"]');

    await expect(page.locator('[data-testid="username-error"]')).toContainText('at least 3 characters');
    await expect(page.locator('[data-testid="email-error"]')).toContainText('valid email');
    await expect(page.locator('[data-testid="password-error"]')).toContainText('at least 8 characters');
  });
});
```

## PERFORMANCE TEST PATTERNS

### Load Testing with Artillery
**API LOAD TESTING**:
```yaml
# tests/performance/user_api_load.yml
config:
  target: 'http://localhost:3000'
  phases:
    - duration: 60
      arrivalRate: 5
      name: "Warm up phase"
    - duration: 120
      arrivalRate: 5
      rampTo: 50
      name: "Ramp up load"
    - duration: 60
      arrivalRate: 50
      name: "Sustained load"

scenarios:
  - name: "User registration flow"
    weight: 30
    flow:
      - post:
          url: "/api/users"
          json:
            username: "loadtest{{ $randomInt }}"
            email: "loadtest{{ $randomInt }}@example.com"
            password: "SecurePass123!"
          expect:
            - statusCode: 201

  - name: "User login flow"
    weight: 40
    flow:
      - post:
          url: "/api/auth/login"
          json:
            username: "existinguser"
            email: "existing@example.com"
            password: "SecurePass123!"
          expect:
            - statusCode: 200
          capture:
            json: "$.access_token"
            as: "token"

  - name: "Get user profile"
    weight: 30
    flow:
      - get:
          url: "/api/users/profile"
          headers:
            Authorization: "Bearer {{ token }}"
          expect:
            - statusCode: 200
            - hasProperty: "username"
```

### Database Performance Testing
**QUERY PERFORMANCE VALIDATION**:
```python
# tests/performance/test_database_performance.py
import pytest
import time
from app.database import get_db_session


class TestDatabasePerformance:
    """Performance tests for database operations."""

    def test_user_query_performance(self, benchmark):
        """Test user query performance under load."""
        def query_users():
            with get_db_session() as session:
                return session.query(User).limit(100).all()

        # Benchmark the query
        result = benchmark(query_users)

        # Assert performance requirements
        assert benchmark.stats.mean < 0.1  # Less than 100ms average
        assert len(result) == 100

    def test_bulk_insert_performance(self, benchmark):
        """Test bulk user insertion performance."""
        def bulk_insert():
            users = []
            for i in range(100):
                users.append(User(
                    username=f'perf_test_{i}',
                    email=f'perf_test_{i}@example.com',
                    password='testpass123'
                ))

            with get_db_session() as session:
                session.bulk_save_objects(users)
                session.commit()

        # Benchmark the bulk insert
        benchmark(bulk_insert)

        # Verify data was inserted
        with get_db_session() as session:
            count = session.query(User).filter(
                User.username.like('perf_test_%')
            ).count()

        assert count == 100

    def test_concurrent_user_access(self):
        """Test database performance under concurrent load."""
        import threading

        results = []
        errors = []

        def worker(worker_id):
            try:
                with get_db_session() as session:
                    start_time = time.time()
                    user = session.query(User).filter_by(id=worker_id).first()
                    query_time = time.time() - start_time

                    results.append({
                        'worker': worker_id,
                        'query_time': query_time,
                        'success': user is not None
                    })
            except Exception as e:
                errors.append(f"Worker {worker_id}: {e}")

        # Start concurrent workers
        threads = []
        for i in range(10):
            thread = threading.Thread(target=worker, args=(i+1,))
            threads.append(thread)
            thread.start()

        # Wait for all threads to complete
        for thread in threads:
            thread.join()

        # Assert performance requirements
        assert len(errors) == 0, f"Errors occurred: {errors}"
        assert len(results) == 10

        avg_query_time = sum(r['query_time'] for r in results) / len(results)
        assert avg_query_time < 0.05  # Less than 50ms average under concurrent load

        assert all(r['success'] for r in results), "Some queries failed"
```

## TEST ORGANIZATION PATTERNS

### Test Data Management
**FIXTURE STRATEGIES**:
```python
# tests/conftest.py
import pytest
from app.database import get_db_session, create_tables
from app.models import User, Product


@pytest.fixture(scope="session")
def db_session():
    """Create test database session."""
    # Set up test database
    create_tables()

    with get_db_session() as session:
        yield session

        # Clean up after tests
        session.rollback()


@pytest.fixture
def test_user(db_session):
    """Create a test user."""
    user = User(
        username='testuser',
        email='test@example.com',
        password='hashedpassword'
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)

    yield user

    # Clean up
    db_session.delete(user)
    db_session.commit()


@pytest.fixture
def authenticated_client(test_user):
    """Create authenticated test client."""
    from app import create_app

    app = create_app('testing')
    client = app.test_client()

    # Simulate login
    with client:
        # Set authentication context
        pass

    return client
```

### Test Categories and Markers
**TEST CLASSIFICATION**:
```python
# tests/test_user_management.py
import pytest


class TestUserCreation:
    """Tests for user creation functionality."""

    @pytest.mark.smoke
    def test_create_valid_user(self, db_session):
        """Smoke test for basic user creation."""
        pass

    @pytest.mark.unit
    def test_username_validation(self):
        """Unit test for username validation rules."""
        pass

    @pytest.mark.integration
    def test_user_creation_with_profile(self, db_session):
        """Integration test for user with profile creation."""
        pass

    @pytest.mark.slow
    def test_bulk_user_creation(self, db_session):
        """Slow test for bulk user operations."""
        pass


@pytest.mark.security
class TestUserSecurity:
    """Security tests for user operations."""

    def test_password_hashing(self):
        """Test that passwords are properly hashed."""
        pass

    def test_sql_injection_prevention(self, client):
        """Test SQL injection attack prevention."""
        pass

    def test_authorization_enforcement(self, client):
        """Test that authorization rules are enforced."""
        pass


# Custom markers for different test types
def pytest_configure(config):
    config.addinivalue_line("markers", "smoke: quick smoke tests")
    config.addinivalue_line("markers", "unit: unit tests")
    config.addinivalue_line("markers", "integration: integration tests")
    config.addinivalue_line("markers", "security: security tests")
    config.addinivalue_line("markers", "slow: slow-running tests")
```

## CONTINUOUS INTEGRATION PATTERNS

### GitHub Actions Test Workflow
**CI/CD INTEGRATION**:
```yaml
# .github/workflows/test.yml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.8, 3.9, "3.10", "3.11"]

    steps:
    - uses: actions/checkout@v3

    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install -r requirements-dev.txt

    - name: Run linting
      run: |
        flake8 app/ tests/
        black --check app/ tests/
        isort --check-only app/ tests/

    - name: Run unit tests
      run: |
        pytest tests/unit/ -v --cov=app --cov-report=xml

    - name: Run integration tests
      run: |
        pytest tests/integration/ -v --cov=app --cov-append --cov-report=xml

    - name: Run UI tests
      run: |
        pytest tests/ui/ -v
      env:
        DISPLAY: :99

    - name: Upload coverage reports
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml

  performance:
    runs-on: ubuntu-latest
    needs: test

    steps:
    - uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'

    - name: Install dependencies
      run: |
        pip install -r requirements.txt
        pip install -r requirements-dev.txt

    - name: Run performance tests
      run: |
        pytest tests/performance/ -v --benchmark-only

  security:
    runs-on: ubuntu-latest
    needs: test

    steps:
    - uses: actions/checkout@v3

    - name: Run security scans
      run: |
        safety check
        bandit -r app/
```

This provides comprehensive TDD examples covering unit tests, integration tests, UI tests, performance tests, and CI/CD integration patterns. The examples demonstrate proper test structure, mocking strategies, and quality practices for maintainable test suites.```

