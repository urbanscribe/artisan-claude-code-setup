# Project Discovery Rule (Tier 2)
## Purpose
Forces Planner to ingest authoritative architectural context before any planning decisions.

## Mandatory Execution Protocol
**BEFORE ANY PLANNING**: Execute grep or read on entire /documentation/main/ folder.

**ARCHITECTURAL INGESTION REQUIRED**:
- Read keygoals.md for objectives and success conditions
- Read architecture.md for patterns and constraints
- Read proposedarchitecture.md for current design decisions
- Read any domain-specific architectural documents

**ENFORCEMENT**: Planner cannot issue INITIAL_PLAN_COMPLETE until ingestion confirmed.

## Why This Matters
Prevents architectural hallucinations by grounding planning in project-specific reality rather than generic knowledge.

## Integration
- Loaded automatically by /implement command at Gate A
- Referenced in Planner prompt as "MANDATORY INITIAL ACTION"
