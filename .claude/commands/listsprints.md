# /listsprints - Visual Sprint Dashboard & Management

## Purpose
Provide comprehensive visual sprint management with status indicators, lifecycle overview, and quick actions. This enables professional sprint tracking and management across multiple concurrent sprints.

## Dashboard Features
**MANDATORY STATE SYNC**: Read PROJECT_REGISTRY.json → Output OS_STATUS
**Visual Design**: Text-based dashboard providing 95% of full UI value with 50% effort
**Status Indicators**: Clear visual cues for sprint lifecycle states
**Reverse Chronological**: Active sprints first, then completed in reverse order
**Color Coding**: Green (active), Grey (completed/abandoned)
**Quick Actions**: Interactive links for common operations

## Dashboard Output Format
```
📊 SPRINT MANAGEMENT DASHBOARD
=====================================

🎯 ACTIVE SPRINTS (2)
----------------------
🟢 2026-01-10_plan_002_user_auth
    Status: Execution | Phase: Active | Iterations: 3/10
    Files: 15 locked | Boundaries: Enforced
    Actions: [Continue] [View Plan] [End Sprint]

🟢 2026-01-09_plan_001_foundation
    Status: Planning | Phase: Quality Gates | Progress: 8/10
    Files: 0 locked | Boundaries: Pending
    Actions: [Complete Planning] [View Checklist] [Abandon]

⚪ COMPLETED SPRINTS (1)
-------------------------
⚪ 2026-01-08_initial_setup
    Status: Completed | Completed: 2026-01-08T14:30:00Z
    Postmortem: Available | Quality Score: 92%
    Actions: [View Postmortem] [Archive Sprint]

📋 SPRINT SUMMARY
==================
Total Sprints: 3 | Active: 2 | Completed: 1
Planning Quality: 95% | Execution Success: 87%
Average Completion: 4.2 days

🎯 RECOMMENDED ACTIONS
1. Complete planning for foundation sprint
2. Continue user_auth sprint execution
3. Review completed sprint postmortem
```

## Enhanced Table Format (Alternative View)
```
| ID | Status | Phase | Files | Actions |
|----|--------|-------|-------|---------|
| 🟢 2026-01-10_plan_002_user_auth | Active | Execution (3/10) | 15 locked | Continue • Plan • End |
| 🟢 2026-01-09_plan_001_foundation | Planning | Quality Gates (8/10) | 0 | Complete • Checklist • Abandon |
| ⚪ 2026-01-08_initial_setup | Completed | Done | Archived | Postmortem • Archive |
```

## ASCII Art Dashboard
**Text-Based Visual Representation**:
```
SPRINT LIFECYCLE OVERVIEW
==========================

Planning → Manifesto → Execution → Completion
    ↑           ↑           ↑           ↑
    ├─── Quality Gates ────┼─── Boundaries ────┼─── Cleanup ────▶
    │         ✅               🔒               🧹
    │     8/10 passed     15 files locked   12 artifacts cleaned
    │
Active Sprint: user_auth (Execution Phase)
███████████████████████░ 70% Complete

Recent Activity:
• 2026-01-10 14:30: Manifesto approved
• 2026-01-10 14:25: Planning checklist completed
• 2026-01-10 14:20: Quality gates validation passed
```

## Quick Action Integration
**Interactive Commands Generated**:
- **Continue**: `/implement "continue sprint"`
- **Complete Planning**: `/startsprintplanning --continue [sprint_id]`
- **View Plan**: Open plan document in editor
- **View Checklist**: `/projectstatus --checklist [sprint_id]`
- **End Sprint**: `/endsprint [sprint_id]`
- **Abandon**: `/abandon-sprint [sprint_id]`
- **View Postmortem**: Open postmortem document
- **Archive**: Move sprint to archive status

## Status Indicator Legend
- **🟢 Green**: Active sprint (execution ready)
- **🟡 Yellow**: Planning in progress (quality gates incomplete)
- **⚪ Grey**: Completed/abandoned (historical)
- **🔴 Red**: Blocked (issues preventing progress)

## Sprint Lifecycle States
- **planning**: Initial planning phase
- **quality_gates**: Checklist validation in progress
- **planning_checklist_complete**: All gates passed
- **manifesto_locked**: Execution boundaries established
- **execution**: Active development
- **cleanup_pending**: Completion initiated
- **completed**: Successfully finished
- **abandoned**: Cancelled without completion

## Required Skills
- **project-status-analyst**: Generates dashboard from PROJECT_REGISTRY.json data
- Model: default (standard reporting)
- Context: default (real-time status)
- Permissions: read (registry access only)

## Integration
- **Real-time Status**: Reflects current PROJECT_REGISTRY.json state
- **Multi-sprint Support**: Handles concurrent active sprints
- **Workflow Guidance**: Suggests next actions based on sprint states
- **Professional Visibility**: Enables structured sprint management

## Professional Discipline
This dashboard enforces visibility into sprint states, preventing forgotten sprints and enabling structured multi-sprint coordination. No more invisible sprint management - everything is tracked and actionable.
