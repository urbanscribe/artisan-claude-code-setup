# Async Patterns Sub-Rule (Tier 3)
## Purpose
Defines async/await implementation patterns, concurrency management, and performance optimization guidelines.

## ASYNC/AWAIT FUNDAMENTALS

### Async Function Definition
**CORRECT NAMING AND USAGE**:
```python
import asyncio
from typing import Optional, List, Dict, Any
import aiohttp
import asyncpg

# ✅ CORRECT: Async functions suffixed with _async for clarity
async def fetch_user_data_async(user_id: str) -> Optional[Dict[str, Any]]:
    """Fetch user data asynchronously."""
    async with aiohttp.ClientSession() as session:
        async with session.get(f'/api/users/{user_id}') as response:
            if response.status == 200:
                return await response.json()
            return None

# ✅ CORRECT: Sync wrapper for async functions
def fetch_user_data(user_id: str) -> Optional[Dict[str, Any]]:
    """Synchronous wrapper for async function."""
    return asyncio.run(fetch_user_data_async(user_id))

# ❌ AVOID: Async functions without clear naming
async def get_user(user_id: str):  # Unclear if async
    pass

# ❌ AVOID: Blocking calls in async functions
async def bad_async_function():
    import time
    time.sleep(1)  # Blocks event loop!
    return "done"
```

### Async Context Managers
**RESOURCE MANAGEMENT**:
```python
import asyncpg
from contextlib import asynccontextmanager
from typing import AsyncGenerator

@asynccontextmanager
async def get_db_connection() -> AsyncGenerator[asyncpg.Connection, None]:
    """Async context manager for database connections."""
    connection = await asyncpg.connect(
        user='user',
        password='password',
        database='database',
        host='localhost'
    )
    try:
        yield connection
    finally:
        await connection.close()

# Usage
async def get_user_count() -> int:
    async with get_db_connection() as conn:
        result = await conn.fetchval("SELECT COUNT(*) FROM users")
        return result

# Multiple connections with proper cleanup
async def transfer_data():
    async with get_db_connection() as source_conn:
        async with get_db_connection() as dest_conn:
            # Data transfer logic
            data = await source_conn.fetch("SELECT * FROM source_table")
            await dest_conn.executemany(
                "INSERT INTO dest_table VALUES ($1, $2, $3)",
                [(row['col1'], row['col2'], row['col3']) for row in data]
            )
```

## CONCURRENCY PATTERNS

### Gathering Multiple Operations
**PARALLEL EXECUTION**:
```python
import asyncio
from typing import List

async def fetch_multiple_users(user_ids: List[str]) -> List[Dict[str, Any]]:
    """Fetch multiple users in parallel."""
    # ✅ CORRECT: Use asyncio.gather for parallel execution
    tasks = [fetch_user_data_async(user_id) for user_id in user_ids]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    # Handle exceptions in results
    valid_results = []
    for result in results:
        if isinstance(result, Exception):
            # Log error and continue
            print(f"Error fetching user: {result}")
        else:
            valid_results.append(result)

    return valid_results

async def process_user_batch(user_ids: List[str]) -> Dict[str, Any]:
    """Process users with different operations in parallel."""
    async def get_profile(user_id: str):
        return await fetch_user_data_async(user_id)

    async def get_permissions(user_id: str):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'/api/users/{user_id}/permissions') as response:
                return await response.json()

    async def get_activity(user_id: str):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'/api/users/{user_id}/activity') as response:
                return await response.json()

    # Execute all operations in parallel
    profile_task = get_profile(user_ids[0])
    permissions_task = get_permissions(user_ids[0])
    activity_task = get_activity(user_ids[0])

    profile, permissions, activity = await asyncio.gather(
        profile_task, permissions_task, activity_task
    )

    return {
        'profile': profile,
        'permissions': permissions,
        'activity': activity
    }
```

### Semaphore for Rate Limiting
**CONCURRENCY CONTROL**:
```python
import asyncio
from typing import List, Dict, Any

class RateLimitedAPIClient:
    """API client with rate limiting."""

    def __init__(self, max_concurrent: int = 10):
        self.semaphore = asyncio.Semaphore(max_concurrent)

    async def api_call(self, endpoint: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Make rate-limited API call."""
        async with self.semaphore:
            async with aiohttp.ClientSession() as session:
                async with session.post(endpoint, json=data) as response:
                    return await response.json()

async def process_batch_with_rate_limit(
    items: List[Dict[str, Any]],
    batch_size: int = 10
) -> List[Dict[str, Any]]:
    """Process items with rate limiting."""
    client = RateLimitedAPIClient(max_concurrent=5)

    # Process in batches to avoid overwhelming the system
    results = []
    for i in range(0, len(items), batch_size):
        batch = items[i:i + batch_size]

        # Process batch concurrently but rate-limited
        batch_tasks = [
            client.api_call('/api/process', item)
            for item in batch
        ]
        batch_results = await asyncio.gather(*batch_tasks)
        results.extend(batch_results)

        # Small delay between batches
        await asyncio.sleep(0.1)

    return results
```

### Task Groups and Cancellation
**STRUCTURED CONCURRENCY**:
```python
import asyncio
from asyncio import TaskGroup
from typing import List, Optional

async def process_with_timeout(
    user_ids: List[str],
    timeout_seconds: float = 30.0
) -> List[Optional[Dict[str, Any]]]:
    """Process users with timeout and proper cancellation."""
    async def fetch_with_timeout(user_id: str) -> Optional[Dict[str, Any]]:
        try:
            return await asyncio.wait_for(
                fetch_user_data_async(user_id),
                timeout=timeout_seconds
            )
        except asyncio.TimeoutError:
            print(f"Timeout fetching user {user_id}")
            return None

    # Use TaskGroup for structured concurrency (Python 3.11+)
    try:
        async with asyncio.TaskGroup() as tg:
            tasks = [
                tg.create_task(fetch_with_timeout(user_id))
                for user_id in user_ids
            ]
    except Exception as e:
        print(f"Task group failed: {e}")
        # Cancel remaining tasks
        for task in tasks:
            if not task.done():
                task.cancel()
        raise

    # Wait for all tasks to complete
    results = await asyncio.gather(*tasks, return_exceptions=True)
    return [
        result if not isinstance(result, Exception) else None
        for result in results
    ]

async def coordinated_shutdown():
    """Demonstrate proper task cancellation."""
    async def worker(name: str, duration: float):
        try:
            await asyncio.sleep(duration)
            print(f"Worker {name} completed")
        except asyncio.CancelledError:
            print(f"Worker {name} was cancelled")
            raise

    # Create tasks
    task1 = asyncio.create_task(worker("A", 10))
    task2 = asyncio.create_task(worker("B", 5))

    # Wait for first to complete, then cancel others
    done, pending = await asyncio.wait(
        [task1, task2],
        return_when=asyncio.FIRST_COMPLETED
    )

    # Cancel pending tasks
    for task in pending:
        task.cancel()

    # Wait for cancellation to complete
    await asyncio.gather(*pending, return_exceptions=True)
```

## DATABASE ASYNC PATTERNS

### Connection Pool Management
**EFFICIENT CONNECTION HANDLING**:
```python
import asyncpg
from typing import AsyncGenerator, Optional
import os

class DatabaseManager:
    """Async database connection manager."""

    def __init__(self):
        self._pool: Optional[asyncpg.Pool] = None

    async def get_pool(self) -> asyncpg.Pool:
        """Get or create connection pool."""
        if self._pool is None:
            self._pool = await asyncpg.create_pool(
                user=os.getenv('DB_USER'),
                password=os.getenv('DB_PASSWORD'),
                database=os.getenv('DB_NAME'),
                host=os.getenv('DB_HOST'),
                min_size=5,      # Minimum connections
                max_size=20,     # Maximum connections
                command_timeout=60
            )
        return self._pool

    async def close(self):
        """Close connection pool."""
        if self._pool:
            await self._pool.close()
            self._pool = None

    @asynccontextmanager
    async def get_connection(self) -> AsyncGenerator[asyncpg.Connection, None]:
        """Get database connection from pool."""
        pool = await self.get_pool()
        async with pool.acquire() as conn:
            yield conn

# Global database manager
db_manager = DatabaseManager()

async def get_user_count() -> int:
    """Get user count with pooled connection."""
    async with db_manager.get_connection() as conn:
        return await conn.fetchval("SELECT COUNT(*) FROM users")

async def create_user(user_data: Dict[str, Any]) -> int:
    """Create user with transaction."""
    async with db_manager.get_connection() as conn:
        async with conn.transaction():
            user_id = await conn.fetchval("""
                INSERT INTO users (username, email, created_at)
                VALUES ($1, $2, $3)
                RETURNING id
            """, user_data['username'], user_data['email'], datetime.utcnow())

            # Additional operations in same transaction
            await conn.execute("""
                INSERT INTO user_profiles (user_id, bio)
                VALUES ($1, $2)
            """, user_id, user_data.get('bio', ''))

            return user_id
```

### Transaction Management
**ACID COMPLIANCE**:
```python
async def transfer_funds(
    from_account: int,
    to_account: int,
    amount: Decimal
) -> bool:
    """Transfer funds between accounts with proper transaction handling."""
    async with db_manager.get_connection() as conn:
        async with conn.transaction():
            # Check sender balance
            sender_balance = await conn.fetchval("""
                SELECT balance FROM accounts
                WHERE id = $1 FOR UPDATE
            """, from_account)

            if sender_balance < amount:
                raise InsufficientFundsError("Insufficient funds")

            # Check receiver exists
            receiver_exists = await conn.fetchval("""
                SELECT EXISTS(SELECT 1 FROM accounts WHERE id = $1)
            """, to_account)

            if not receiver_exists:
                raise AccountNotFoundError(f"Account {to_account} not found")

            # Perform transfer
            await conn.execute("""
                UPDATE accounts SET balance = balance - $1
                WHERE id = $2
            """, amount, from_account)

            await conn.execute("""
                UPDATE accounts SET balance = balance + $1
                WHERE id = $2
            """, amount, to_account)

            # Log transaction
            await conn.execute("""
                INSERT INTO transactions (from_account, to_account, amount, timestamp)
                VALUES ($1, $2, $3, $4)
            """, from_account, to_account, amount, datetime.utcnow())

            return True
```

## ASYNC WEB FRAMEWORK PATTERNS

### FastAPI Async Handlers
**REQUEST HANDLING**:
```python
from fastapi import FastAPI, BackgroundTasks, HTTPException
from typing import List, Dict, Any
import asyncio

app = FastAPI()

@app.get("/users/{user_id}")
async def get_user(user_id: str) -> Dict[str, Any]:
    """Async FastAPI endpoint."""
    # Parallel data fetching
    user_task = fetch_user_data_async(user_id)
    permissions_task = fetch_user_permissions_async(user_id)
    activity_task = fetch_user_activity_async(user_id)

    user, permissions, activity = await asyncio.gather(
        user_task, permissions_task, activity_task
    )

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        'user': user,
        'permissions': permissions,
        'activity': activity
    }

@app.post("/users/batch")
async def create_users_batch(users: List[Dict[str, Any]], background_tasks: BackgroundTasks):
    """Batch user creation with background processing."""
    # Validate all users first
    validation_errors = []
    for i, user_data in enumerate(users):
        try:
            validate_user_data(user_data)
        except ValidationError as e:
            validation_errors.append(f"User {i}: {e}")

    if validation_errors:
        raise HTTPException(status_code=400, detail=validation_errors)

    # Start background processing
    background_tasks.add_task(process_user_batch_async, users)

    return {"message": "Batch processing started", "count": len(users)}

async def process_user_batch_async(users: List[Dict[str, Any]]):
    """Background batch processing."""
    semaphore = asyncio.Semaphore(5)  # Limit concurrent operations

    async def create_single_user(user_data: Dict[str, Any]):
        async with semaphore:
            return await create_user_async(user_data)

    # Process in parallel with rate limiting
    tasks = [create_single_user(user) for user in users]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    # Handle results
    success_count = sum(1 for r in results if not isinstance(r, Exception))
    error_count = len(results) - success_count

    print(f"Batch complete: {success_count} success, {error_count} errors")
```

### Background Task Management
**LONG-RUNNING OPERATIONS**:
```python
from fastapi import BackgroundTasks
import asyncio
from typing import Dict, Any
import uuid

# Task storage (in production, use Redis/database)
active_tasks: Dict[str, Dict[str, Any]] = {}

async def long_running_operation(task_id: str, data: Dict[str, Any]):
    """Simulate long-running async operation."""
    try:
        # Update task status
        active_tasks[task_id]['status'] = 'running'

        # Simulate work with progress updates
        for i in range(10):
            await asyncio.sleep(1)  # Simulate async work
            active_tasks[task_id]['progress'] = (i + 1) * 10

        # Complete task
        active_tasks[task_id]['status'] = 'completed'
        active_tasks[task_id]['result'] = {'processed': len(data), 'timestamp': datetime.utcnow()}

    except Exception as e:
        active_tasks[task_id]['status'] = 'failed'
        active_tasks[task_id]['error'] = str(e)

@app.post("/jobs/{job_type}")
async def start_job(job_type: str, data: Dict[str, Any], background_tasks: BackgroundTasks):
    """Start background job."""
    task_id = str(uuid.uuid4())

    # Initialize task
    active_tasks[task_id] = {
        'id': task_id,
        'type': job_type,
        'status': 'pending',
        'progress': 0,
        'created_at': datetime.utcnow()
    }

    # Start background task
    background_tasks.add_task(long_running_operation, task_id, data)

    return {"task_id": task_id, "status": "started"}

@app.get("/jobs/{task_id}")
async def get_job_status(task_id: str):
    """Get job status."""
    if task_id not in active_tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    return active_tasks[task_id]
```

## PERFORMANCE OPTIMIZATION

### Connection Reuse
**PERSISTENT CONNECTIONS**:
```python
import aiohttp
from typing import Optional

class HTTPClientManager:
    """Reusable HTTP client with connection pooling."""

    def __init__(self):
        self._session: Optional[aiohttp.ClientSession] = None

    async def get_session(self) -> aiohttp.ClientSession:
        """Get or create client session."""
        if self._session is None or self._session.closed:
            self._session = aiohttp.ClientSession(
                connector=aiohttp.TCPConnector(
                    limit=100,          # Connection pool size
                    limit_per_host=10,  # Per-host limit
                    ttl_dns_cache=300,  # DNS cache TTL
                    use_dns_cache=True
                ),
                timeout=aiohttp.ClientTimeout(total=30)
            )
        return self._session

    async def close(self):
        """Close client session."""
        if self._session and not self._session.closed:
            await self._session.close()

# Global HTTP client manager
http_client = HTTPClientManager()

async def fetch_multiple_apis(urls: List[str]) -> List[Dict[str, Any]]:
    """Fetch from multiple APIs with connection reuse."""
    session = await http_client.get_session()

    async def fetch_url(url: str) -> Dict[str, Any]:
        async with session.get(url) as response:
            return await response.json()

    # Execute in parallel with shared connection pool
    tasks = [fetch_url(url) for url in urls]
    results = await asyncio.gather(*tasks)
    return results
```

### Memory-Efficient Streaming
**LARGE DATA HANDLING**:
```python
import aiofiles
from typing import AsyncGenerator

async def process_large_file_async(file_path: str) -> AsyncGenerator[str, None]:
    """Process large file asynchronously with memory efficiency."""
    async with aiofiles.open(file_path, 'r') as file:
        async for line in file:
            # Process line without loading entire file
            processed_line = await process_line_async(line.strip())
            yield processed_line

async def stream_file_to_client(file_path: str):
    """Stream large file to client without loading in memory."""
    async def generate():
        async for processed_line in process_large_file_async(file_path):
            yield f"{processed_line}\n"
            await asyncio.sleep(0)  # Allow other tasks to run

    return StreamingResponse(generate(), media_type="text/plain")

async def batch_process_with_memory_limit(
    items: List[Dict[str, Any]],
    batch_size: int = 100,
    max_memory_mb: int = 100
) -> List[Dict[str, Any]]:
    """Process items in batches to control memory usage."""
    results = []

    for i in range(0, len(items), batch_size):
        batch = items[i:i + batch_size]

        # Process batch
        batch_tasks = [process_item_async(item) for item in batch]
        batch_results = await asyncio.gather(*batch_tasks)

        results.extend(batch_results)

        # Memory check (simplified)
        if len(results) % 1000 == 0:
            # Force garbage collection if needed
            import gc
            gc.collect()
            await asyncio.sleep(0.01)  # Small yield

    return results
```

This comprehensive async patterns rule establishes clear guidelines for async/await usage, concurrency management, database operations, and performance optimization, ensuring efficient and maintainable asynchronous code throughout the system. The patterns promote proper resource management, error handling, and scalability in async contexts.```
</xai:function_call name="write">
<parameter name="file_path">claude_code/setup/.claude/rules/sub/doc_revision_rules.md
