# External Verification Sub-Rule (Tier 3)
## Purpose
Defines systematic verification protocols for external APIs, databases, and third-party services to prevent integration failures.

## EXTERNAL API VERIFICATION PROTOCOLS

### API Availability Testing
**ENDPOINT HEALTH VALIDATION**:
```python
# external_verification/api_verification.py
import aiohttp
import asyncio
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
import time

@dataclass
class APIEndpoint:
    """API endpoint specification for verification."""
    name: str
    url: str
    method: str = 'GET'
    headers: Optional[Dict[str, str]] = None
    expected_status: int = 200
    timeout: float = 30.0
    required_fields: Optional[List[str]] = None

@dataclass
class VerificationResult:
    """Result of API verification."""
    endpoint: str
    success: bool
    response_time: float
    status_code: Optional[int]
    error: Optional[str]
    response_sample: Optional[Any]

class ExternalAPIVerifier:
    """Verify external API availability and contract compliance."""

    def __init__(self, timeout: float = 30.0):
        self.timeout = timeout
        self.session: Optional[aiohttp.ClientSession] = None

    async def create_session(self):
        """Create HTTP session with proper configuration."""
        if self.session is None:
            self.session = aiohttp.ClientSession(
                timeout=aiohttp.ClientTimeout(total=self.timeout),
                connector=aiohttp.TCPConnector(limit=10)
            )

    async def close_session(self):
        """Close HTTP session."""
        if self.session:
            await self.session.close()
            self.session = None

    async def verify_endpoint(self, endpoint: APIEndpoint) -> VerificationResult:
        """Verify single API endpoint."""
        await self.create_session()
        start_time = time.time()

        try:
            async with self.session.request(
                endpoint.method,
                endpoint.url,
                headers=endpoint.headers
            ) as response:
                response_time = time.time() - start_time
                status_code = response.status

                # Check status code
                if status_code != endpoint.expected_status:
                    return VerificationResult(
                        endpoint=endpoint.name,
                        success=False,
                        response_time=response_time,
                        status_code=status_code,
                        error=f"Unexpected status code: {status_code}, expected {endpoint.expected_status}"
                    )

                # Sample response for validation
                content_type = response.headers.get('content-type', '')
                if 'application/json' in content_type:
                    response_data = await response.json()
                else:
                    response_data = await response.text()
                    response_data = response_data[:500]  # Limit text responses

                # Check required fields if specified
                if endpoint.required_fields and isinstance(response_data, dict):
                    missing_fields = [
                        field for field in endpoint.required_fields
                        if field not in response_data
                    ]
                    if missing_fields:
                        return VerificationResult(
                            endpoint=endpoint.name,
                            success=False,
                            response_time=response_time,
                            status_code=status_code,
                            error=f"Missing required fields: {missing_fields}"
                        )

                return VerificationResult(
                    endpoint=endpoint.name,
                    success=True,
                    response_time=response_time,
                    status_code=status_code,
                    response_sample=response_data
                )

        except asyncio.TimeoutError:
            response_time = time.time() - start_time
            return VerificationResult(
                endpoint=endpoint.name,
                success=False,
                response_time=response_time,
                status_code=None,
                error=f"Request timeout after {self.timeout}s"
            )
        except aiohttp.ClientError as e:
            response_time = time.time() - start_time
            return VerificationResult(
                endpoint=endpoint.name,
                success=False,
                response_time=response_time,
                status_code=None,
                error=f"Client error: {str(e)}"
            )
        except Exception as e:
            response_time = time.time() - start_time
            return VerificationResult(
                endpoint=endpoint.name,
                success=False,
                response_time=response_time,
                status_code=None,
                error=f"Unexpected error: {str(e)}"
            )

    async def verify_all_endpoints(self, endpoints: List[APIEndpoint]) -> List[VerificationResult]:
        """Verify all configured API endpoints."""
        try:
            await self.create_session()
            tasks = [self.verify_endpoint(endpoint) for endpoint in endpoints]
            results = await asyncio.gather(*tasks, return_exceptions=True)

            # Handle exceptions in results
            processed_results = []
            for i, result in enumerate(results):
                if isinstance(result, Exception):
                    processed_results.append(VerificationResult(
                        endpoint=endpoints[i].name,
                        success=False,
                        response_time=0.0,
                        status_code=None,
                        error=f"Verification failed: {str(result)}"
                    ))
                else:
                    processed_results.append(result)

            return processed_results
        finally:
            await self.close_session()
```

### Authentication Testing
**CREDENTIAL VALIDATION**:
```python
# external_verification/auth_verification.py
import aiohttp
import asyncio
from typing import Dict, Optional, List
from dataclasses import dataclass

@dataclass
class AuthConfig:
    """Authentication configuration for external service."""
    service_name: str
    auth_type: str  # 'bearer', 'basic', 'api_key', 'oauth2'
    token_url: Optional[str] = None
    client_id: Optional[str] = None
    client_secret: Optional[str] = None
    api_key: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None

@dataclass
class AuthResult:
    """Result of authentication verification."""
    service: str
    success: bool
    token_valid: bool = False
    error: Optional[str] = None
    expires_in: Optional[int] = None

class AuthVerifier:
    """Verify external service authentication."""

    async def verify_bearer_token(self, config: AuthConfig, test_url: str) -> AuthResult:
        """Verify bearer token authentication."""
        headers = {'Authorization': f'Bearer {config.api_key}'}

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(test_url, headers=headers) as response:
                    if response.status == 401:
                        return AuthResult(
                            service=config.service_name,
                            success=False,
                            token_valid=False,
                            error="Invalid or expired token"
                        )
                    elif response.status == 403:
                        return AuthResult(
                            service=config.service_name,
                            success=False,
                            token_valid=True,
                            error="Token valid but insufficient permissions"
                        )
                    elif response.status < 400:
                        return AuthResult(
                            service=config.service_name,
                            success=True,
                            token_valid=True
                        )
                    else:
                        return AuthResult(
                            service=config.service_name,
                            success=False,
                            error=f"Unexpected response: {response.status}"
                        )
        except Exception as e:
            return AuthResult(
                service=config.service_name,
                success=False,
                error=f"Authentication check failed: {str(e)}"
            )

    async def verify_oauth2_flow(self, config: AuthConfig) -> AuthResult:
        """Verify OAuth2 token acquisition and validation."""
        if not config.token_url or not config.client_id or not config.client_secret:
            return AuthResult(
                service=config.service_name,
                success=False,
                error="OAuth2 configuration incomplete"
            )

        # OAuth2 client credentials flow
        auth_data = {
            'grant_type': 'client_credentials',
            'client_id': config.client_id,
            'client_secret': config.client_secret
        }

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(config.token_url, data=auth_data) as response:
                    if response.status != 200:
                        return AuthResult(
                            service=config.service_name,
                            success=False,
                            error=f"Token request failed: {response.status}"
                        )

                    token_data = await response.json()
                    access_token = token_data.get('access_token')
                    expires_in = token_data.get('expires_in')

                    if not access_token:
                        return AuthResult(
                            service=config.service_name,
                            success=False,
                            error="No access token in response"
                        )

                    return AuthResult(
                        service=config.service_name,
                        success=True,
                        token_valid=True,
                        expires_in=expires_in
                    )
        except Exception as e:
            return AuthResult(
                service=config.service_name,
                success=False,
                error=f"OAuth2 flow failed: {str(e)}"
            )
```

## DATABASE VERIFICATION PROTOCOLS

### Connection Testing
**DATABASE AVAILABILITY**:
```python
# external_verification/database_verification.py
import asyncpg
import aiomysql
import aiosqlite
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from abc import ABC, abstractmethod
import time

@dataclass
class DatabaseConfig:
    """Database connection configuration."""
    type: str  # 'postgresql', 'mysql', 'sqlite'
    host: Optional[str] = None
    port: Optional[int] = None
    database: str = ''
    username: Optional[str] = None
    password: Optional[str] = None
    connection_string: Optional[str] = None

@dataclass
class DatabaseResult:
    """Result of database verification."""
    database: str
    success: bool
    connection_time: float
    error: Optional[str] = None
    schema_version: Optional[str] = None
    table_count: Optional[int] = None

class DatabaseVerifier(ABC):
    """Abstract base class for database verification."""

    @abstractmethod
    async def verify_connection(self, config: DatabaseConfig) -> DatabaseResult:
        """Verify database connection and basic functionality."""
        pass

    @abstractmethod
    async def verify_schema(self, config: DatabaseConfig) -> DatabaseResult:
        """Verify database schema integrity."""
        pass

class PostgreSQLVerifier(DatabaseVerifier):
    """PostgreSQL database verification."""

    async def verify_connection(self, config: DatabaseConfig) -> DatabaseResult:
        """Verify PostgreSQL connection."""
        start_time = time.time()

        try:
            connection = await asyncpg.connect(
                user=config.username,
                password=config.password,
                database=config.database,
                host=config.host,
                port=config.port,
                timeout=10
            )

            # Test basic query
            result = await connection.fetchval("SELECT version()")
            connection_time = time.time() - start_time

            await connection.close()

            return DatabaseResult(
                database=config.database,
                success=True,
                connection_time=connection_time,
                schema_version=result.split()[1] if result else None
            )

        except Exception as e:
            connection_time = time.time() - start_time
            return DatabaseResult(
                database=config.database,
                success=False,
                connection_time=connection_time,
                error=f"PostgreSQL connection failed: {str(e)}"
            )

    async def verify_schema(self, config: DatabaseConfig) -> DatabaseResult:
        """Verify PostgreSQL schema."""
        try:
            connection = await asyncpg.connect(
                user=config.username,
                password=config.password,
                database=config.database,
                host=config.host,
                port=config.port
            )

            # Get table count
            table_count = await connection.fetchval("""
                SELECT count(*)
                FROM information_schema.tables
                WHERE table_schema = 'public'
            """)

            # Check for required tables (customize as needed)
            required_tables = ['users', 'sessions']  # Example
            existing_tables = await connection.fetch("""
                SELECT table_name
                FROM information_schema.tables
                WHERE table_schema = 'public'
                AND table_name = ANY($1)
            """, required_tables)

            existing_table_names = [row['table_name'] for row in existing_tables]
            missing_tables = set(required_tables) - set(existing_table_names)

            await connection.close()

            if missing_tables:
                return DatabaseResult(
                    database=config.database,
                    success=False,
                    connection_time=0.0,
                    error=f"Missing required tables: {missing_tables}",
                    table_count=table_count
                )

            return DatabaseResult(
                database=config.database,
                success=True,
                connection_time=0.0,
                table_count=table_count
            )

        except Exception as e:
            return DatabaseResult(
                database=config.database,
                success=False,
                connection_time=0.0,
                error=f"Schema verification failed: {str(e)}"
            )
```

### Schema Validation
**STRUCTURE VERIFICATION**:
```python
# external_verification/schema_validator.py
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
import asyncpg

@dataclass
class TableSchema:
    """Expected table schema."""
    name: str
    columns: Dict[str, str]  # column_name -> data_type
    primary_key: List[str]
    indexes: Optional[Dict[str, List[str]]] = None  # index_name -> columns

@dataclass
class SchemaValidationResult:
    """Result of schema validation."""
    table: str
    valid: bool
    issues: List[str]
    recommendations: List[str]

class SchemaValidator:
    """Validate database schema against expected structure."""

    async def validate_schema(
        self,
        connection: asyncpg.Connection,
        expected_schema: List[TableSchema]
    ) -> List[SchemaValidationResult]:
        """Validate database schema."""
        results = []

        for table_schema in expected_schema:
            issues = []
            recommendations = []

            # Check if table exists
            table_exists = await connection.fetchval("""
                SELECT EXISTS (
                    SELECT 1 FROM information_schema.tables
                    WHERE table_schema = 'public'
                    AND table_name = $1
                )
            """, table_schema.name)

            if not table_exists:
                issues.append(f"Table '{table_schema.name}' does not exist")
                recommendations.append(f"Create table '{table_schema.name}' with defined schema")
                results.append(SchemaValidationResult(
                    table=table_schema.name,
                    valid=False,
                    issues=issues,
                    recommendations=recommendations
                ))
                continue

            # Validate columns
            columns = await connection.fetch("""
                SELECT column_name, data_type, is_nullable
                FROM information_schema.columns
                WHERE table_schema = 'public'
                AND table_name = $1
                ORDER BY ordinal_position
            """, table_schema.name)

            existing_columns = {col['column_name']: col['data_type'] for col in columns}

            # Check expected columns exist with correct types
            for col_name, expected_type in table_schema.columns.items():
                if col_name not in existing_columns:
                    issues.append(f"Column '{col_name}' missing from table '{table_schema.name}'")
                    recommendations.append(f"Add column '{col_name}' {expected_type} to table '{table_schema.name}'")
                elif existing_columns[col_name] != expected_type:
                    issues.append(f"Column '{col_name}' has type {existing_columns[col_name]}, expected {expected_type}")
                    recommendations.append(f"Alter column '{col_name}' type to {expected_type}")

            # Check primary key
            pk_columns = await connection.fetch("""
                SELECT a.attname
                FROM pg_index i
                JOIN pg_attribute a ON a.attrelid = i.indrelid AND a.attnum = ANY(i.indkey)
                WHERE i.indrelid = $1::regclass
                AND i.indisprimary
            """, table_schema.name)

            existing_pk = [row['attname'] for row in pk_columns]
            if set(existing_pk) != set(table_schema.primary_key):
                issues.append(f"Primary key mismatch: expected {table_schema.primary_key}, got {existing_pk}")
                recommendations.append(f"Recreate primary key with columns: {table_schema.primary_key}")

            # Check indexes (simplified)
            if table_schema.indexes:
                for index_name, index_columns in table_schema.indexes.items():
                    index_exists = await connection.fetchval("""
                        SELECT EXISTS (
                            SELECT 1 FROM pg_indexes
                            WHERE tablename = $1
                            AND indexname = $2
                        )
                    """, table_schema.name, index_name)

                    if not index_exists:
                        issues.append(f"Index '{index_name}' missing on table '{table_schema.name}'")
                        recommendations.append(f"Create index '{index_name}' on columns {index_columns}")

            results.append(SchemaValidationResult(
                table=table_schema.name,
                valid=len(issues) == 0,
                issues=issues,
                recommendations=recommendations
            ))

        return results
```

## MOCK IMPLEMENTATION STRATEGIES

### Development Mocks
**TESTING WITHOUT EXTERNAL DEPENDENCIES**:
```python
# external_verification/mock_services.py
from typing import Dict, Any, Optional, List
import json
import os

class MockExternalService:
    """Mock external service for development and testing."""

    def __init__(self, service_name: str):
        self.service_name = service_name
        self.mock_data_file = f"mock_data/{service_name}.json"
        self._load_mock_data()

    def _load_mock_data(self):
        """Load mock data from file."""
        if os.path.exists(self.mock_data_file):
            with open(self.mock_data_file, 'r') as f:
                self.mock_data = json.load(f)
        else:
            self.mock_data = self._get_default_mock_data()

    def _get_default_mock_data(self) -> Dict[str, Any]:
        """Get default mock data structure."""
        return {
            "users": [
                {"id": 1, "name": "Mock User 1", "email": "user1@mock.com"},
                {"id": 2, "name": "Mock User 2", "email": "user2@mock.com"}
            ],
            "products": [
                {"id": 1, "name": "Mock Product", "price": 29.99}
            ]
        }

    async def get_users(self) -> List[Dict[str, Any]]:
        """Mock user retrieval."""
        # Simulate API delay
        await asyncio.sleep(0.1)
        return self.mock_data.get("users", [])

    async def get_user(self, user_id: int) -> Optional[Dict[str, Any]]:
        """Mock single user retrieval."""
        await asyncio.sleep(0.05)
        users = self.mock_data.get("users", [])
        return next((user for user in users if user["id"] == user_id), None)

    async def create_user(self, user_data: Dict[str, Any]) -> Dict[str, Any]:
        """Mock user creation."""
        await asyncio.sleep(0.1)
        new_user = {
            "id": len(self.mock_data["users"]) + 1,
            **user_data
        }
        self.mock_data["users"].append(new_user)
        self._save_mock_data()
        return new_user

    def _save_mock_data(self):
        """Save mock data to file."""
        os.makedirs(os.path.dirname(self.mock_data_file), exist_ok=True)
        with open(self.mock_data_file, 'w') as f:
            json.dump(self.mock_data, f, indent=2)

# Environment-based service selection
def get_external_service(service_name: str):
    """Get external service instance based on environment."""
    if os.getenv('USE_MOCK_SERVICES', 'false').lower() == 'true':
        return MockExternalService(service_name)
    else:
        # Return real service implementation
        if service_name == 'user_api':
            return RealUserAPI()
        elif service_name == 'payment_service':
            return RealPaymentService()
        else:
            raise ValueError(f"Unknown service: {service_name}")
```

This external verification sub-rule establishes comprehensive protocols for validating external API and database dependencies, ensuring system reliability through proactive testing and mock fallbacks. The verification patterns prevent integration failures and provide robust fallback mechanisms for development and testing environments.```
<xai:function_call name="write">
<parameter name="file_path">claude_code/setup/.claude/rules/sub/polish_checklist.md
