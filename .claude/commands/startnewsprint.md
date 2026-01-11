# /startnewsprint - Sprint Execution Manifesto & Boundary Establishment

## Purpose
Validate sprint readiness, generate immutable execution manifesto, and establish professional sprint boundaries. This creates the "Execution Manifesto" that prevents "Loss of Intent" between planning and execution phases.

## Workflow
1. **MANDATORY STATE SYNC**: Read PROJECT_REGISTRY.json → Output OS_STATUS
2. **Foundation Validation**: Confirm foundation.complete = true
3. **Active Sprint Check**: Warn if unfinished sprint exists
4. **COMPREHENSIVE PLANNING CHECKLIST VALIDATION**: Block if planning_checklist.completed ≠ true
5. **Execution Manifesto Generation**: Create immutable token with sprint scope
6. **Sprint State Initialization**: Update PROJECT_REGISTRY.json sprints.active
7. **APPROVE_MANIFESTO Gate**: Human verification required

## Planning Checklist Enforcement
**CRITICAL BLOCKING MECHANISM**: Cannot proceed without complete planning validation

```
🚫 SPRINT BLOCKED: Planning checklist incomplete
Return to /startsprintplanning to complete quality gates

Current Status:
❌ Goals Clarity: PENDING
❌ Code Location: PENDING
❌ Architecture: PENDING
❌ Testing: PENDING
✅ All Gates: INCOMPLETE
```

**Validation Logic**:
- Read PROJECT_REGISTRY.json planning_checklist.completed
- If false, display detailed status report of incomplete gates
- Block sprint creation until ALL 10 quality gates show "passed"
- No bypass available - must return to /startsprintplanning

## Execution Manifesto Implementation
**Immutable Token**: Single non-editable Markdown block summarizing complete sprint scope

**Manifesto Structure**:
```
# EXECUTION MANIFESTO - [SPRINT_ID]
# Immutable Sprint Boundary Definition

## Sprint Scope
**ID**: [Generated sprint ID: YYYY-MM-DD_plan_XXX_sprint_title]
**Status**: ACTIVE | BOUNDARY_LOCKED
**Created**: [Timestamp]
**Planning Complete**: ✅ ALL_QUALITY_GATES_PASSED

## Execution Boundaries (LOCKED)
**Locked Files**: Complete enumeration of all files within sprint scope
- [file1.py] - [purpose]
- [file2.py] - [purpose]
- [file3.md] - [purpose]

**Nonsense-Prevention Rubric**:
- Data Validation: Must check for N/A, NaN, null, undefined values
- Business Logic: Flag impossible values (negative stock prices, 0.00% volatility)
- UI State: Confirm meaningful data display, not placeholder content
- Sanity Checks: Visual proof required before Victory Declaration

**Phase Transition Lock**: Prevents "Loss of Intent" between planning and execution
**Human Verification**: APPROVE_MANIFESTO required before execution begins

## Quality Gates Status
✅ Goals Clarity | ✅ Code Location | ✅ Architecture | ✅ Testing
✅ Duplication Elimination | ✅ Step-by-Step | ✅ Strategic Logging
✅ Dependency Management | ✅ UI-First Design | ✅ Decisions

---
MANIFESTO APPROVAL: ____________________ Date: _____________
```

## Sprint State Initialization
**PROJECT_REGISTRY.json Updates**:
```json
{
  "sprints": {
    "active": {
      "id": "2026-01-10_plan_002_user_auth",
      "phase": "execution",
      "status": "manifesto_locked",
      "plan_path": "documentation/plans/2026-01-10_plan_002_user_auth.md",
      "manifesto_locked": true,
      "locked_files": ["src/auth.py", "tests/test_auth.py", "docs/auth.md"],
      "created": "2026-01-10T14:30:00Z",
      "iteration": 0,
      "max_iterations": 1000
    }
  }
}
```

## Required Skills
- **sprint-planning-specialist**: Validates planning completeness and generates manifesto
- Model: default (standard operations)
- Context: fork (isolated sprint initialization)
- Permissions: read, write (registry updates), run_terminal_cmd (validation)

## Error Handling
- **Foundation Incomplete**: "⚠️ Cannot start sprint - foundation not established"
- **Planning Incomplete**: "🚫 SPRINT BLOCKED: Planning checklist incomplete. Return to /startsprintplanning"
- **Active Sprint Exists**: "⚠️ Sprint [ID] already active. Complete with /endsprint or abandon first"
- **Manifesto Rejected**: "❌ Manifesto not approved. Sprint creation cancelled"

## Integration
- **Blocks Execution**: /implement validates active sprint exists with manifesto_locked = true
- **Safety Enforcement**: safety_pre_tool.py checks file operations against locked_files array
- **Professional Workflow**: Enforces planning → manifesto → execution sequence
- **State Management**: Updates PROJECT_REGISTRY.json with complete sprint metadata

## Professional Discipline
This command physically prevents development until comprehensive planning is complete and boundaries are established. No more unstructured sprint jumping - every execution begins with clear, approved scope and boundaries.

## User Guidance Output
**MANDATORY STATE SYNC**: Read PROJECT_REGISTRY.json → Display OS_STATUS

**Post-Manifesto Approval Guidance**:
```
🎯 EXECUTION MANIFESTO LOCKED
✅ Sprint [ID] established
✅ Manifesto boundaries locked
✅ File scope: [X] files protected
✅ Iteration limit: 10 (safety bound)

🎯 NEXT STEPS
1. Run /implement to begin Ralph Wiggum execution
2. Use /projectstatus to monitor sprint progress
3. Execute within established boundaries only

💡 PROFESSIONAL DISCIPLINE: Manifesto prevents "Loss of Intent" between planning and execution
⚠️  WARNING: All operations now validated against sprint boundaries
```

**Error Guidance** (Planning Incomplete):
```
🚫 SPRINT BLOCKED
Planning checklist incomplete: [X]/10 gates passed

❌ INCOMPLETE GATES:
- [List of failed gates]

🎯 RESOLUTION PATH
1. Run /startsprintplanning to complete quality gates
2. Use /projectstatus --checklist to view detailed status
3. Complete all 10 gates before retrying /startnewsprint

💡 PROFESSIONAL TIP: Quality gates prevent execution failures
```

**Guidance Logic**:
- Display after successful manifesto approval
- Show sprint boundaries and constraints clearly
- Provide immediate execution guidance
- Include boundary enforcement warnings
- Offer clear resolution paths for blocked states
- Reinforce professional discipline benefits
