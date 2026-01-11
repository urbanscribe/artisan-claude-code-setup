# Core Operational Rules
## Purpose
Holds all procedural "how-to" guidance moved from CLAUDE.md during the Great Stripping.

## Testing Requirements
- **TDD as gatekeeper** - Tests first, then implementation
- Tests in `/tests/` subfolders only
- Real data testing only - no mocks or destructive operations

## Code Quality Standards
- **Async preferred** - Use async/await patterns
- Type hints required for all parameters and return values
- Strategic logging only - not excessive
- Surgical changes - minimal, targeted edits

## Worktree Ownership
- Each worktree = one feature namespace
- Agents may only modify files inside that namespace unless explicitly approved

## Architectural Documentation
- **Source of Truth**: `/documentation/main/` contains authoritative architectural documents
- **Consistency First**: All features must align with established architecture patterns
