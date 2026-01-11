# Architecture Basics Sub-Rule (Tier 3)
## Purpose
Establishes foundational architectural patterns and domain-driven design principles for consistent system structure.

## DOMAIN-DRIVEN DESIGN FOUNDATIONS

### Bounded Contexts
**CONTEXT DEFINITION AND ISOLATION**:
```python
# Domain contexts define clear boundaries
# Each context has its own language and rules

# User Management Context
class UserManagementContext:
    """Handles user registration, authentication, and profiles."""

    def register_user(self, username: str, email: str) -> User:
        # User-specific business logic
        pass

    def authenticate_user(self, credentials: LoginCredentials) -> AuthToken:
        # Authentication-specific logic
        pass

# Order Processing Context
class OrderProcessingContext:
    """Handles order creation, payment processing, and fulfillment."""

    def create_order(self, items: List[OrderItem], customer: Customer) -> Order:
        # Order-specific business logic
        pass

    def process_payment(self, order: Order, payment_method: PaymentMethod) -> PaymentResult:
        # Payment-specific logic
        pass
```

**CONTEXT MAPPING PATTERNS**:
- **Shared Kernel**: Common domain concepts shared between contexts
- **Customer-Supplier**: One context supplies services to another
- **Conformist**: One context adapts to another's interface
- **Anti-Corruption Layer**: Translation layer between contexts

### Entities and Value Objects
**ENTITY DEFINITIONS**:
```python
from dataclasses import dataclass
from typing import List
import uuid
from datetime import datetime

@dataclass
class User:  # Entity - has identity and lifecycle
    id: uuid.UUID
    username: str
    email: str
    created_at: datetime
    updated_at: datetime

    def update_profile(self, new_email: str) -> None:
        """Business logic for profile updates."""
        if not self._is_valid_email(new_email):
            raise ValueError("Invalid email format")

        self.email = new_email
        self.updated_at = datetime.utcnow()

    def _is_valid_email(self, email: str) -> bool:
        """Domain validation logic."""
        return '@' in email and '.' in email.split('@')[1]

@dataclass(frozen=True)
class Money:  # Value Object - immutable, no identity
    amount: Decimal
    currency: str

    def add(self, other: 'Money') -> 'Money':
        if self.currency != other.currency:
            raise ValueError("Cannot add different currencies")

        return Money(self.amount + other.amount, self.currency)

    def multiply(self, factor: Decimal) -> 'Money':
        return Money(self.amount * factor, self.currency)
```

**VALUE OBJECT CHARACTERISTICS**:
- **Immutability**: Cannot be changed after creation
- **Equality by Value**: Two instances are equal if all attributes match
- **No Identity**: No unique identifier separate from attributes
- **Self-Validating**: Constructor validates business rules

### Aggregates and Aggregate Roots
**AGGREGATE PATTERNS**:
```python
from typing import List, Optional
from dataclasses import dataclass, field

@dataclass
class OrderItem:  # Part of Order aggregate
    product_id: uuid.UUID
    quantity: int
    unit_price: Money

    @property
    def total_price(self) -> Money:
        return self.unit_price.multiply(Decimal(self.quantity))

@dataclass
class Order:  # Aggregate Root
    id: uuid.UUID
    customer_id: uuid.UUID
    items: List[OrderItem] = field(default_factory=list)
    status: OrderStatus = OrderStatus.PENDING
    created_at: datetime = field(default_factory=datetime.utcnow)

    def add_item(self, product_id: uuid.UUID, quantity: int, unit_price: Money) -> None:
        """Business logic for adding items."""
        if self.status != OrderStatus.PENDING:
            raise OrderModificationError("Cannot modify non-pending order")

        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        # Check for existing item
        existing_item = next(
            (item for item in self.items if item.product_id == product_id),
            None
        )

        if existing_item:
            # Update quantity
            existing_item.quantity += quantity
        else:
            # Add new item
            self.items.append(OrderItem(product_id, quantity, unit_price))

    def calculate_total(self) -> Money:
        """Aggregate-level calculation."""
        return sum((item.total_price for item in self.items), Money(0, 'USD'))

    def confirm(self) -> None:
        """State transition with business rules."""
        if not self.items:
            raise OrderConfirmationError("Cannot confirm empty order")

        if self.calculate_total().amount <= 0:
            raise OrderConfirmationError("Invalid order total")

        self.status = OrderStatus.CONFIRMED
```

**AGGREGATE RULES**:
- **Consistency Boundaries**: All changes within aggregate are atomic
- **External Access**: Only through aggregate root
- **Size Limits**: Keep aggregates small for performance
- **Transactional Consistency**: Aggregate changes are atomic

## LAYERED ARCHITECTURE PATTERNS

### Presentation Layer
**API AND INTERFACE PATTERNS**:
```python
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Data Transfer Objects
class CreateUserRequest(BaseModel):
    username: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: str
    username: str
    email: str
    created_at: str

# Dependency injection for use cases
def get_user_service() -> UserService:
    # In real app, this would use proper DI container
    return UserService()

@app.post("/users", response_model=UserResponse)
async def create_user(
    request: CreateUserRequest,
    user_service: UserService = Depends(get_user_service)
):
    """Presentation layer - thin API translation."""
    try:
        # Translate to domain objects
        command = CreateUserCommand(
            username=request.username,
            email=request.email,
            password=request.password
        )

        # Execute business logic
        user = await user_service.create_user(command)

        # Translate to response
        return UserResponse(
            id=str(user.id),
            username=user.username,
            email=user.email,
            created_at=user.created_at.isoformat()
        )

    except UserAlreadyExistsError:
        raise HTTPException(status_code=409, detail="Username already exists")
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=str(e))
```

### Application Layer
**USE CASE COORDINATION**:
```python
from typing import Protocol
from abc import ABC, abstractmethod

# Application Services (Use Cases)
class CreateUserUseCase:
    def __init__(self, user_repository: UserRepository, domain_events: DomainEventPublisher):
        self.user_repository = user_repository
        self.domain_events = domain_events

    async def execute(self, command: CreateUserCommand) -> User:
        """Application service coordinates domain logic."""

        # Validate command
        if not command.username or len(command.username) < 3:
            raise ValidationError("Username must be at least 3 characters")

        # Check business rules
        existing_user = await self.user_repository.get_by_username(command.username)
        if existing_user:
            raise UserAlreadyExistsError(f"Username {command.username} already exists")

        # Create domain entity
        user = User.create(
            username=command.username,
            email=command.email,
            password=command.password
        )

        # Persist
        await self.user_repository.save(user)

        # Publish domain events
        await self.domain_events.publish(UserCreatedEvent(user.id))

        return user

# Command objects
@dataclass
class CreateUserCommand:
    username: str
    email: str
    password: str
```

### Domain Layer
**BUSINESS LOGIC CORE**:
```python
from dataclasses import dataclass
from typing import List
import hashlib
from datetime import datetime

# Domain Events
@dataclass
class DomainEvent:
    occurred_at: datetime

@dataclass
class UserCreatedEvent(DomainEvent):
    user_id: uuid.UUID

# Domain Services (when logic doesn't belong to entities)
class PasswordHasher:
    @staticmethod
    def hash_password(password: str) -> str:
        """Domain service for password hashing."""
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def verify_password(password: str, hashed: str) -> bool:
        """Domain service for password verification."""
        return PasswordHasher.hash_password(password) == hashed

# Entity with domain logic
@dataclass
class User:
    id: uuid.UUID
    username: str
    email: str
    password_hash: str
    created_at: datetime
    _domain_events: List[DomainEvent] = field(default_factory=list)

    @classmethod
    def create(cls, username: str, email: str, password: str) -> 'User':
        """Factory method with business rules."""
        if not username or len(username.strip()) < 3:
            raise ValidationError("Username must be at least 3 characters")

        if '@' not in email:
            raise ValidationError("Invalid email format")

        return cls(
            id=uuid.uuid4(),
            username=username.strip(),
            email=email.lower().strip(),
            password_hash=PasswordHasher.hash_password(password),
            created_at=datetime.utcnow()
        )

    def change_password(self, old_password: str, new_password: str) -> None:
        """Domain logic for password changes."""
        if not PasswordHasher.verify_password(old_password, self.password_hash):
            raise AuthenticationError("Invalid current password")

        if len(new_password) < 8:
            raise ValidationError("New password must be at least 8 characters")

        self.password_hash = PasswordHasher.hash_password(new_password)
        self._domain_events.append(PasswordChangedEvent(self.id))

    def get_domain_events(self) -> List[DomainEvent]:
        """Get and clear domain events."""
        events = self._domain_events.copy()
        self._domain_events.clear()
        return events
```

### Infrastructure Layer
**EXTERNAL CONCERNS**:
```python
from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
from typing import Optional

Base = declarative_base()

# Repository implementation
class SqlUserRepository:
    def __init__(self, session_factory):
        self.session_factory = session_factory

    async def save(self, user: User) -> None:
        """Infrastructure implementation of domain interface."""
        async with self.session_factory() as session:
            # Convert domain entity to persistence model
            db_user = DbUser(
                id=user.id,
                username=user.username,
                email=user.email,
                password_hash=user.password_hash,
                created_at=user.created_at
            )
            session.add(db_user)
            await session.commit()

    async def get_by_username(self, username: str) -> Optional[User]:
        """Infrastructure implementation."""
        async with self.session_factory() as session:
            db_user = await session.execute(
                select(DbUser).where(DbUser.username == username)
            )
            db_user = db_user.scalar_one_or_none()

            if db_user:
                return User(
                    id=db_user.id,
                    username=db_user.username,
                    email=db_user.email,
                    password_hash=db_user.password_hash,
                    created_at=db_user.created_at
                )
            return None

# Persistence model
class DbUser(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, nullable=False)
    password_hash = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
```

## ARCHITECTURAL PRINCIPLES

### Dependency Inversion
**DEPENDENCY DIRECTION**:
```python
# High-level modules should not depend on low-level modules
# Both should depend on abstractions

from abc import ABC, abstractmethod

# Abstractions (interfaces)
class UserRepository(ABC):
    @abstractmethod
    async def save(self, user: User) -> None:
        pass

    @abstractmethod
    async def get_by_username(self, username: str) -> Optional[User]:
        pass

# High-level module depends on abstraction
class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository  # Depends on interface

# Low-level module implements abstraction
class SqlUserRepository(UserRepository):
    # Implementation details...
    pass

# Dependency injection at composition root
def create_user_service() -> UserService:
    repository = SqlUserRepository(create_session_factory())
    return UserService(repository)
```

### Single Responsibility Principle
**FOCUSED COMPONENTS**:
```python
# ❌ VIOLATION - Multiple responsibilities
class UserManager:
    def create_user(self, data): pass
    def send_welcome_email(self, user): pass
    def calculate_user_stats(self): pass
    def generate_user_report(self): pass

# ✅ COMPLIANT - Single responsibilities
class UserService:  # User business logic
    def create_user(self, data): pass

class EmailService:  # Email communication
    def send_welcome_email(self, user): pass

class UserAnalyticsService:  # Analytics calculations
    def calculate_user_stats(self): pass

class ReportService:  # Report generation
    def generate_user_report(self): pass
```

### Open-Closed Principle
**EXTENSIBLE DESIGN**:
```python
# Open for extension, closed for modification

from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: Money, method: PaymentMethod) -> PaymentResult:
        pass

# Existing implementation
class StripePaymentProcessor(PaymentProcessor):
    def process_payment(self, amount: Money, method: PaymentMethod) -> PaymentResult:
        # Stripe-specific logic
        pass

# New payment method - extension without modification
class PayPalPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount: Money, method: PaymentMethod) -> PaymentResult:
        # PayPal-specific logic
        pass

# Usage - no changes needed
class OrderService:
    def __init__(self, payment_processors: Dict[str, PaymentProcessor]):
        self.payment_processors = payment_processors

    def process_order_payment(self, order: Order) -> PaymentResult:
        processor = self.payment_processors[order.payment_method.type]
        return processor.process_payment(order.total, order.payment_method)
```

This establishes the foundational architectural patterns that all development must follow, ensuring consistency, maintainability, and adherence to domain-driven design principles across the entire system. The patterns provide clear guidelines for organizing code, managing dependencies, and implementing business logic in a scalable and testable manner.```
</xai:function_call name="write">
<parameter name="file_path">claude_code/setup/.claude/rules/sub/error_patterns.md
