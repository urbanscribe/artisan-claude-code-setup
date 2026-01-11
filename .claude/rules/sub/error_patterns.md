# Error Patterns Sub-Rule (Tier 3)
## Purpose
Defines comprehensive error handling, exception management, and failure recovery patterns for robust system reliability.

## EXCEPTION HIERARCHY DESIGN

### Base Exception Classes
**DOMAIN-SPECIFIC EXCEPTIONS**:
```python
from abc import ABC
from typing import Dict, Any, Optional

class DomainException(Exception, ABC):
    """Base class for all domain-specific exceptions."""

    def __init__(self, message: str, code: str = None, details: Dict[str, Any] = None):
        super().__init__(message)
        self.code = code or self.__class__.__name__
        self.details = details or {}

    def to_dict(self) -> Dict[str, Any]:
        """Convert exception to dictionary for API responses."""
        return {
            'error': self.code,
            'message': str(self),
            'details': self.details
        }

class BusinessRuleViolation(DomainException):
    """Exceptions for business rule violations."""
    pass

class ValidationError(BusinessRuleViolation):
    """Data validation failures."""
    pass

class AuthorizationError(DomainException):
    """Access control violations."""
    pass

class ResourceNotFoundError(DomainException):
    """Requested resource does not exist."""
    def __init__(self, resource_type: str, resource_id: str):
        super().__init__(
            f"{resource_type} with id '{resource_id}' not found",
            code="RESOURCE_NOT_FOUND",
            details={'resource_type': resource_type, 'resource_id': resource_id}
        )

class OperationNotAllowedError(DomainException):
    """Operation not permitted in current state."""
    pass
```

### Infrastructure Exceptions
**SYSTEM-LEVEL EXCEPTIONS**:
```python
class InfrastructureException(Exception, ABC):
    """Base class for infrastructure-related exceptions."""
    pass

class DatabaseException(InfrastructureException):
    """Database operation failures."""
    def __init__(self, operation: str, details: str = None):
        super().__init__(f"Database {operation} failed: {details}")
        self.operation = operation

class ExternalServiceException(InfrastructureException):
    """External API or service failures."""
    def __init__(self, service: str, operation: str, status_code: int = None):
        message = f"External service '{service}' {operation} failed"
        if status_code:
            message += f" (HTTP {status_code})"
        super().__init__(message)
        self.service = service
        self.status_code = status_code

class ConfigurationException(InfrastructureException):
    """Configuration-related errors."""
    pass
```

## ERROR HANDLING PATTERNS

### Try-Except-Finally Blocks
**STRUCTURED ERROR HANDLING**:
```python
from contextlib import contextmanager
from typing import Generator, TypeVar, Callable
import logging

logger = logging.getLogger(__name__)
T = TypeVar('T')

@contextmanager
def error_context(operation: str, context: Dict[str, Any] = None) -> Generator[None, None, None]:
    """Context manager for consistent error handling."""
    try:
        yield
    except DomainException:
        # Re-raise domain exceptions unchanged
        raise
    except InfrastructureException as e:
        # Log infrastructure issues and convert to domain exception
        logger.error(f"Infrastructure error in {operation}: {e}", extra=context)
        raise SystemException(f"System error during {operation}") from e
    except Exception as e:
        # Unexpected errors - log and convert
        logger.exception(f"Unexpected error in {operation}", extra=context)
        raise SystemException(f"Unexpected error during {operation}") from e

def with_error_handling(operation: str, context: Dict[str, Any] = None):
    """Decorator for consistent error handling."""
    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        def wrapper(*args, **kwargs) -> T:
            with error_context(operation, context):
                return func(*args, **kwargs)
        return wrapper
    return decorator

# Usage examples
class UserService:
    @with_error_handling("user_creation", lambda: {"user_id": "new"})
    def create_user(self, username: str, email: str) -> User:
        """Create user with comprehensive error handling."""
        if not username:
            raise ValidationError("Username is required")

        try:
            # Database operation with specific error handling
            with error_context("database_user_creation"):
                user = User(username=username, email=email)
                self.db.add(user)
                self.db.commit()
                return user
        except IntegrityError:
            self.db.rollback()
            raise BusinessRuleViolation(f"Username '{username}' already exists")
        except Exception:
            self.db.rollback()
            raise

    def update_user(self, user_id: str, updates: Dict[str, Any]) -> User:
        """Update user with proper error context."""
        with error_context("user_update", {"user_id": user_id, "updates": list(updates.keys())}):
            user = self.get_user_by_id(user_id)
            if not user:
                raise ResourceNotFoundError("User", user_id)

            # Apply updates with validation
            for field, value in updates.items():
                if field == 'email':
                    user.update_email(value)
                elif field == 'username':
                    user.update_username(value)
                else:
                    raise ValidationError(f"Unknown field: {field}")

            self.db.commit()
            return user
```

### Result Pattern for Operations
**EXPLICIT SUCCESS/FAILURE HANDLING**:
```python
from typing import Union, Generic, TypeVar
from dataclasses import dataclass

T = TypeVar('T')
E = TypeVar('E', bound=Exception)

@dataclass
class Success(Generic[T]):
    """Successful operation result."""
    value: T
    metadata: Dict[str, Any] = None

    def is_success(self) -> bool:
        return True

    def is_failure(self) -> bool:
        return False

@dataclass
class Failure(Generic[E]):
    """Failed operation result."""
    error: E
    metadata: Dict[str, Any] = None

    def is_success(self) -> bool:
        return False

    def is_failure(self) -> bool:
        return True

Result = Union[Success[T], Failure[E]]

def safe_divide(a: float, b: float) -> Result[float, ZeroDivisionError]:
    """Safe division returning Result pattern."""
    if b == 0:
        return Failure(ZeroDivisionError("Division by zero"))
    return Success(a / b)

# Usage with pattern matching (Python 3.10+)
def handle_calculation():
    result = safe_divide(10, 0)

    match result:
        case Success(value):
            print(f"Result: {value}")
        case Failure(error):
            print(f"Error: {error}")

# Usage with explicit checking
def handle_calculation_legacy():
    result = safe_divide(10, 2)

    if result.is_success():
        print(f"Result: {result.value}")
    else:
        print(f"Error: {result.error}")
```

## ERROR RECOVERY PATTERNS

### Retry Mechanisms
**INTELLIGENT RETRY LOGIC**:
```python
import asyncio
import random
from typing import Callable, TypeVar, Awaitable
from datetime import datetime, timedelta

T = TypeVar('T')

class RetryConfig:
    def __init__(
        self,
        max_attempts: int = 3,
        base_delay: float = 1.0,
        max_delay: float = 60.0,
        backoff_factor: float = 2.0,
        jitter: bool = True
    ):
        self.max_attempts = max_attempts
        self.base_delay = base_delay
        self.max_delay = max_delay
        self.backoff_factor = backoff_factor
        self.jitter = jitter

async def retry_async(
    func: Callable[[], Awaitable[T]],
    config: RetryConfig,
    retryable_exceptions: tuple = (Exception,)
) -> T:
    """Retry async function with exponential backoff."""
    last_exception = None

    for attempt in range(config.max_attempts):
        try:
            return await func()
        except retryable_exceptions as e:
            last_exception = e

            if attempt == config.max_attempts - 1:
                # Last attempt failed
                break

            # Calculate delay with exponential backoff
            delay = min(
                config.base_delay * (config.backoff_factor ** attempt),
                config.max_delay
            )

            # Add jitter to prevent thundering herd
            if config.jitter:
                delay *= (0.5 + random.random() * 0.5)

            await asyncio.sleep(delay)

    raise last_exception

# Usage
async def unreliable_api_call():
    async def _call():
        # Simulate API call that might fail
        if random.random() < 0.7:  # 70% failure rate
            raise ExternalServiceException("api", "call", 500)
        return {"data": "success"}

    config = RetryConfig(max_attempts=3, base_delay=1.0)
    return await retry_async(_call, config, (ExternalServiceException,))
```

### Circuit Breaker Pattern
**FAILURE PREVENTION**:
```python
from enum import Enum
from datetime import datetime, timedelta
import asyncio

class CircuitState(Enum):
    CLOSED = "closed"      # Normal operation
    OPEN = "open"         # Failing, requests blocked
    HALF_OPEN = "half_open"  # Testing recovery

class CircuitBreaker:
    def __init__(
        self,
        failure_threshold: int = 5,
        recovery_timeout: int = 60,
        success_threshold: int = 3
    ):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.success_threshold = success_threshold

        self.state = CircuitState.CLOSED
        self.failure_count = 0
        self.success_count = 0
        self.last_failure_time = None

    async def call(self, func: Callable[[], Awaitable[T]]) -> T:
        """Execute function through circuit breaker."""
        if self.state == CircuitState.OPEN:
            if self._should_attempt_reset():
                self.state = CircuitState.HALF_OPEN
            else:
                raise CircuitBreakerOpenException("Circuit breaker is open")

        try:
            result = await func()
            self._on_success()
            return result
        except Exception as e:
            self._on_failure()
            raise e

    def _should_attempt_reset(self) -> bool:
        """Check if enough time has passed to attempt recovery."""
        if self.last_failure_time is None:
            return True

        elapsed = datetime.utcnow() - self.last_failure_time
        return elapsed.total_seconds() >= self.recovery_timeout

    def _on_success(self):
        """Handle successful call."""
        self.failure_count = 0

        if self.state == CircuitState.HALF_OPEN:
            self.success_count += 1
            if self.success_count >= self.success_threshold:
                self._reset()

    def _on_failure(self):
        """Handle failed call."""
        self.failure_count += 1
        self.last_failure_time = datetime.utcnow()
        self.success_count = 0

        if self.failure_count >= self.failure_threshold:
            self.state = CircuitState.OPEN

    def _reset(self):
        """Reset circuit breaker to normal operation."""
        self.state = CircuitState.CLOSED
        self.failure_count = 0
        self.success_count = 0

# Usage
circuit_breaker = CircuitBreaker()

async def call_external_service():
    async def _call():
        # External service call
        return await external_api.request()

    return await circuit_breaker.call(_call)
```

## ERROR LOGGING PATTERNS

### Structured Error Logging
**COMPREHENSIVE ERROR CONTEXT**:
```python
import logging
import json
from typing import Dict, Any, Optional

class ErrorLogger:
    """Structured error logging with context."""

    def __init__(self, logger_name: str):
        self.logger = logging.getLogger(logger_name)

    def log_error(
        self,
        error: Exception,
        operation: str,
        context: Dict[str, Any] = None,
        user_id: str = None,
        request_id: str = None
    ):
        """Log error with comprehensive context."""
        error_context = {
            'operation': operation,
            'error_type': type(error).__name__,
            'error_message': str(error),
            'user_id': user_id,
            'request_id': request_id,
            'timestamp': datetime.utcnow().isoformat(),
            **(context or {})
        }

        # Add stack trace for unexpected errors
        if not isinstance(error, DomainException):
            error_context['stack_trace'] = self._format_stack_trace(error)

        self.logger.error(
            f"Error in {operation}: {error}",
            extra=error_context,
            exc_info=True
        )

    def _format_stack_trace(self, error: Exception) -> str:
        """Format stack trace for logging."""
        import traceback
        return ''.join(traceback.format_exception(type(error), error, error.__traceback__))

# Usage
error_logger = ErrorLogger(__name__)

try:
    user_service.create_user(username="", email="invalid")
except ValidationError as e:
    error_logger.log_error(
        e,
        "user_creation",
        context={'username': "", 'email': "invalid"},
        user_id=None,
        request_id="req-123"
    )
    raise
```

### Error Metrics and Monitoring
**ERROR TRACKING AND ALERTING**:
```python
from collections import defaultdict, deque
from datetime import datetime, timedelta
import threading

class ErrorMetrics:
    """Track error patterns and trigger alerts."""

    def __init__(self, alert_threshold: int = 10, time_window: int = 300):
        self.alert_threshold = alert_threshold
        self.time_window = time_window  # seconds

        self.errors = defaultdict(lambda: deque(maxlen=1000))
        self.lock = threading.Lock()

    def record_error(self, error_type: str, operation: str):
        """Record an error occurrence."""
        with self.lock:
            timestamp = datetime.utcnow()
            self.errors[error_type].append({
                'timestamp': timestamp,
                'operation': operation
            })

            # Check for alert condition
            recent_errors = [
                e for e in self.errors[error_type]
                if (timestamp - e['timestamp']).total_seconds() < self.time_window
            ]

            if len(recent_errors) >= self.alert_threshold:
                self._trigger_alert(error_type, len(recent_errors))

    def _trigger_alert(self, error_type: str, count: int):
        """Trigger alert for excessive errors."""
        alert_logger = logging.getLogger('error_alerts')
        alert_logger.warning(
            f"Error threshold exceeded for {error_type}: {count} errors in {self.time_window}s"
        )

# Global error metrics
error_metrics = ErrorMetrics()

# Integration with error handling
def handle_with_metrics(operation: str):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                error_metrics.record_error(type(e).__name__, operation)
                raise
        return wrapper
    return decorator
```

## ERROR RESPONSE PATTERNS

### API Error Responses
**CONSISTENT ERROR FORMATS**:
```python
from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
from typing import Dict, Any

def create_error_response(
    status_code: int,
    error_code: str,
    message: str,
    details: Dict[str, Any] = None
) -> JSONResponse:
    """Create consistent error response."""
    return JSONResponse(
        status_code=status_code,
        content={
            'error': {
                'code': error_code,
                'message': message,
                'details': details or {},
                'timestamp': datetime.utcnow().isoformat()
            }
        }
    )

# Exception handlers
def domain_exception_handler(request: Request, exc: DomainException):
    """Handle domain exceptions."""
    status_map = {
        ValidationError: 400,
        AuthorizationError: 403,
        ResourceNotFoundError: 404,
        OperationNotAllowedError: 409,
        BusinessRuleViolation: 422
    }

    status_code = status_map.get(type(exc), 500)
    return create_error_response(
        status_code,
        exc.code,
        str(exc),
        exc.details
    )

def infrastructure_exception_handler(request: Request, exc: InfrastructureException):
    """Handle infrastructure exceptions."""
    # Log infrastructure errors
    logger.error(f"Infrastructure error: {exc}", exc_info=True)

    return create_error_response(
        503,
        'INFRASTRUCTURE_ERROR',
        'Service temporarily unavailable',
        {'retry_after': 60}
    )

def unexpected_exception_handler(request: Request, exc: Exception):
    """Handle unexpected exceptions."""
    # Log with full context
    logger.exception(f"Unexpected error: {exc}")

    return create_error_response(
        500,
        'INTERNAL_ERROR',
        'An unexpected error occurred',
        {'request_id': getattr(request.state, 'request_id', None)}
    )
```

This comprehensive error patterns rule establishes standardized approaches for exception handling, recovery mechanisms, logging, and API responses, ensuring robust and maintainable error management across the entire system. The patterns promote consistency, observability, and reliability in error scenarios.```
</xai:function_call name="write">
<parameter name="file_path">claude_code/setup/.claude/rules/sub/async_patterns.md
