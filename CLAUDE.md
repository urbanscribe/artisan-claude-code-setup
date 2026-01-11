# Artisan's Claude Code Operating System

## NON-NEGOTIABLE PHYSICS
These are the absolute invariants that govern Artisan's Claude Code Operating System behavior. They cannot be overwritten, modified, or bypassed under any circumstances.

### Project Sovereignty
- **SOVEREIGNTY**: You are a specialist operating within a SPRINT. Your authority is limited to the files listed in PROJECT_REGISTRY.json sprints section. Your context is governed by PROJECT_REGISTRY.json foundation section.
- **STATE_SYNCHRONIZATION**: Every command MUST begin with a tool-use read of PROJECT_REGISTRY.json. All commands MUST output "OS_STATUS: Project [Name] | Sprint [ID] | Phase [Phase]" after state read.
- **AUTHORITY HIERARCHY**: Foundation > Sprint > Execution > Recovery. Lower levels cannot override higher level decisions.
- **CONTEXT BOUNDARIES**: Operations outside established boundaries are physically blocked by safety_pre_tool.py.

### Professional Discipline Physics
- **FOUNDATION GATE**: No development operations permitted until PROJECT_REGISTRY.json.foundation.complete = true
- **PLANNING COMPLETENESS**: Sprint creation blocked until all 10 planning checklist gates PASSED
- **EXECUTION BOUNDARIES**: All operations validated against sprint manifesto locked_files array
- **PROMISE ENFORCEMENT**: Ralph Wiggum loops require <promise>SANITY_CHECK_PASS</promise> to exit

### Recovery Physics
- **REGISTRY PRIORITY**: PROJECT_REGISTRY.json takes precedence over CLAUDE.md memory in all scenarios
- **GRACEFUL DEGRADATION**: System survives partial corruption with FULL/PARTIAL/MINIMAL recovery levels
- **STATE RECONSTRUCTION**: Multi-source recovery prioritizes registry > documentation > invariants

### Quality Assurance Physics
- **PLANNING QA ENFORCEMENT**: 10-gate checklist validation prevents "Victory Too Early" syndrome
- **TESTING INTEGRATION**: TDD checkpoints with database reset/drop prohibition
- **STRATEGIC LOGGING**: Surgical points only, not excessive butter-spreading
- **SESSION CONTEXT**: Unified get_db_session_context() usage throughout

### Enterprise Reliability Physics
- **ASYNC FIRST**: Use async/await throughout for proper session management
- **DEPENDENCY MANAGEMENT**: Update pyproject.toml + containers for proper integration
- **WORK IN MAIN**: No feature branches, professional workflows only
- **PERFORMANCE OPTIMIZATION**: Minimal overhead on development operations

## ABSOLUTE CONSTRAINTS

### Development Workflow
- **NO CASUAL DEVELOPMENT**: Structured foundation → planning → execution → completion only
- **PROFESSIONAL DISCIPLINE**: Invisible enforcement through blocking mechanisms and guidance
- **QUALITY GATES**: All 10 planning gates must pass before sprint execution
- **EXECUTION ISOLATION**: Sprint boundaries prevent architectural drift

### State Management
- **UNIFIED STATE**: PROJECT_REGISTRY.json is single source of truth
- **CORRUPTION RESISTANCE**: Registry survives CLAUDE.md overwrites
- **SYNCHRONIZATION**: Every command reads registry first
- **INTEGRITY**: State isolation between projects and sprints

### Error Handling
- **GRACEFUL FAILURE**: Clear error messages with resolution guidance
- **RECOVERY PRIORITY**: Registry-based restoration over memory loss
- **CONTEXT PRESERVATION**: Professional workflows survive disruptions
- **USER GUIDANCE**: Contextual help for all blocking conditions

## PROFESSIONAL OS COMMITMENT

This Professional Operating System transforms Claude Code from a basic AI assistant into an enterprise-grade development environment. Through enforced structured workflows, comprehensive quality controls, and bulletproof reliability, it prevents the #1 cause of project failure while maintaining the power and flexibility of AI assistance.

**The result**: Professional discipline is invisible yet omnipresent, enabling teams to deliver high-quality software through structured, repeatable processes that scale from individual developers to enterprise teams.
