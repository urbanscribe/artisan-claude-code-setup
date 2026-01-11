# /endsprint - Professional Sprint Completion with Cleanup & Documentation

## Purpose
Execute professional sprint completion with human acceptance, orphaned code detection, documentation updates, and postmortem generation. This ensures sprint learnings are captured and repository hygiene is maintained.

## Workflow
1. **MANDATORY STATE SYNC**: Read PROJECT_REGISTRY.json → Output OS_STATUS
2. **Active Sprint Validation**: Confirm sprint exists and is active
3. **Human Acceptance Gate**: APPROVE_SPRINT_OUTCOMES required
4. **Cleanup Sweep Execution**: Orphaned code detection with ls -R vs git status
5. **Artifact Review**: Present cleanup recommendations with APPROVE_CLEANUP
6. **Documentation Updates**: keygoals.md, architecture.md evolution
7. **Postmortem Generation**: documentation/postmortems/ creation
8. **State Cleanup**: Reset sprint state in PROJECT_REGISTRY.json

## Cleanup Sweep Implementation
**MANDATORY ORPHANED CODE DETECTION**: Prevents artifact rot accumulation

**Comprehensive Directory Scan**:
```bash
# Execute full directory sweep
ls -R . > /tmp/full_directory_listing.txt
git status --porcelain > /tmp/git_status.txt
```

**Intelligent Classification Engine**:
- **Production Code**: Files in active sprint locked_files + version controlled
- **Temporary Artifacts**: test_temp.py, old_version.bak, *.tmp files
- **Orphaned Files**: Sprint-created files not in production or temp categories

**Cleanup Recommendation Report**:
```
🧹 SPRINT CLEANUP SWEEP RESULTS
=====================================

📂 Directory Analysis Complete
Found: 1,247 files total | Git tracked: 892 | Uncommitted: 23

🔍 CLASSIFICATION RESULTS:

✅ PRODUCTION CODE (Keep - 856 files)
- Sprint deliverables properly committed
- Core functionality maintained
- Version control integrity preserved

🗑️ TEMPORARY ARTIFACTS (Auto-delete - 45 files)
- test_temp.py (debug artifact)
- old_version.bak (backup file)
- *.log (temporary logs)
- __pycache__/ (bytecode)

⚠️ ORPHANED FILES (Review required - 12 files)
1. experiment_auth.py - Created during sprint, not in production
2. debug_ui.html - UI testing artifact
3. temp_config.json - Temporary configuration
4. backup_auth.sql - Database backup

📋 CLEANUP RECOMMENDATIONS:
KEEP: [List of production files]
DELETE: [List of temp artifacts]
REVIEW: [List of orphaned files with descriptions]

APPROVE_CLEANUP to execute recommendations
```

## Documentation Evolution
**Core Document Updates**:
- **keygoals.md**: Sprint outcomes reflected in project objectives
- **architecture.md**: New patterns, constraints, and architectural decisions documented
- **projectimplementationplan.md**: Sprint completion status updated

**Evolution Logic**:
- Extract architectural decisions from sprint deliverables
- Update constraint documentation
- Preserve sprint learnings for future reference

## Postmortem Generation
**Structured Postmortem Creation**:
```
# SPRINT POSTMORTEM: [SPRINT_ID]

## Sprint Overview
**ID**: 2026-01-10_plan_002_user_auth
**Duration**: [Start Date] - [End Date]
**Status**: COMPLETED
**Planning Quality**: 95% (9/10 gates passed)

## Outcomes Achieved
✅ [List of completed objectives]
✅ [Key deliverables]
✅ [Quality metrics met]

## Lessons Learned
📈 What Went Well:
- [Positive outcomes and successful patterns]

⚠️ Areas for Improvement:
- [Challenges encountered and solutions]

🔧 Technical Decisions:
- [Architectural choices made and rationale]

## Process Improvements
🎯 Planning Quality Gates:
- [Which gates were most valuable]
- [Gates that need refinement]

📊 Metrics & KPIs:
- Planning completeness: 95%
- Execution efficiency: [X] iterations
- Code quality: [Pass/fail rate]

## Recommendations for Future Sprints
- [Process improvements]
- [Technical standards]
- [Quality practices]

## Artifacts Cleaned Up
🗑️ Removed: [X] orphaned files
📦 Archived: [X] temporary artifacts
✅ Preserved: [X] production deliverables
```

## State Management
**PROJECT_REGISTRY.json Updates**:
```json
{
  "sprints": {
    "active": null,
    "history": [
      {
        "id": "2026-01-10_plan_002_user_auth",
        "status": "completed",
        "postmortem_path": "documentation/postmortems/2026-01-10_postmortem_002.md",
        "completed": "2026-01-10T16:45:00Z",
        "cleanup_executed": true,
        "artifacts_cleaned": 12
      }
    ]
  }
}
```

## Required Skills
- **cleanup-specialist**: Executes orphaned code detection and classification
- **sprint-planning-specialist**: Handles documentation updates and postmortem generation
- Model: default (standard operations)
- Context: fork (isolated cleanup work)
- Permissions: read, run_terminal_cmd, write (documentation updates)

## Error Handling
- **No Active Sprint**: "⚠️ No active sprint to end. Use /listsprints to view sprint status."
- **Incomplete Sprint**: "⚠️ Sprint marked as incomplete. Use /abandon-sprint to cancel."
- **Cleanup Rejected**: "❌ Cleanup not approved. Sprint remains active for manual cleanup."
- **Documentation Update Failed**: "⚠️ Documentation updates incomplete. Manual updates required."

## Integration
- **Repository Hygiene**: Prevents accumulation of test_temp.py and orphaned files
- **Knowledge Capture**: Sprint learnings preserved in global documentation
- **Professional Closure**: Structured completion ritual improves team discipline
- **State Consistency**: Clean transition between sprint states

## Professional Discipline
This command enforces professional sprint completion rituals, ensuring clean handoffs, captured learnings, and maintained repository hygiene. No more forgotten artifacts or undocumented architectural decisions.
