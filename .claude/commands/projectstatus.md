# /projectstatus - Comprehensive Project Status Dashboard

## Purpose
Generate human-readable project status dashboard for session resumption, progress tracking, and troubleshooting. This addresses the critical workflow pain points of understanding current state and identifying next actions.

## Dashboard Sections
**MANDATORY STATE SYNC**: Read PROJECT_REGISTRY.json → Output OS_STATUS
**Comprehensive Overview**: Foundation status, active sprint, current phase
**Real-time Validation**: Planning checklist status with timestamps
**Blockage Detection**: Identifies incomplete requirements
**Actionable Guidance**: Clear next-step recommendations
**Progress Metrics**: Quality scores and completion rates

## Dashboard Output Format
```
📊 PROJECT STATUS DASHBOARD
=======================================

🎯 PROJECT OVERVIEW
Project: [Name] | Phase: [Current Phase] | Status: [Active/Planning/Complete]
Foundation: ✅ Complete | Last Updated: 2026-01-10 14:00
Active Sprint: [ID] | Status: [Active/Planning/Complete]
Current Phase: Execution (Iteration 3/10)

🔍 CURRENT SPRINT STATUS
Sprint: 2026-01-10_plan_002_user_auth
Phase: Execution | Status: ✅ Active | Manifesto: Locked
Files in Scope: 15 | Boundaries: Enforced | Iterations: 3/10
Next Action: Continue Ralph Wiggum loop
Progress: ████████░░░░ 70% Complete

📋 PLANNING CHECKLIST STATUS
✅ GOALS CLARITY: PASSED (2026-01-10 10:30)
✅ CODE LOCATION: PASSED (2026-01-10 10:35)
✅ DUPLICATION ELIMINATION: PASSED (2026-01-10 10:40)
✅ ARCHITECTURE PRESERVATION: PASSED (2026-01-10 10:45)
✅ STEP-BY-STEP EXECUTION: PASSED (2026-01-10 10:50)
✅ STRATEGIC LOGGING: PASSED (2026-01-10 10:55)
✅ DEPENDENCY MANAGEMENT: PASSED (2026-01-10 11:00)
✅ UI-FIRST DESIGN: PASSED (2026-01-10 11:05)
✅ ARCHITECTURAL DECISIONS: PASSED (2026-01-10 11:10)
✅ TESTING INTEGRATION: PASSED (2026-01-10 11:15)

==========================================
FINAL STATUS: ALL_GATES_PASSED | READY_FOR_EXECUTION
==========================================

🚧 CURRENT BLOCKAGES
None detected - All systems operational

🎯 RECOMMENDED NEXT ACTIONS
1. Continue sprint execution: /implement "continue user login feature"
2. View sprint details: /listsprints
3. Check recent activity: /projectstatus --recent

⚡ QUICK STATS
Total Sprints: 3 | Completed: 2 | Active: 1
Planning Quality: 95% | Execution Success: 87%
Average Sprint Duration: 4.2 days
```

## Blockage Detection Logic
**Incomplete Foundation**:
```
🚫 FOUNDATION INCOMPLETE
Project foundation not established
Next Action: /startprojectplanning
```

**Planning Incomplete**:
```
🚫 PLANNING BLOCKED
Planning checklist incomplete: 3/10 gates passed
Missing: Architecture, Testing, Dependencies
Next Action: /startsprintplanning --continue
```

**Sprint Blocked**:
```
🚫 SPRINT BOUNDARY VIOLATION
Attempted operation outside manifesto boundaries
File: unauthorized.py | Boundary: user_auth sprint only
Next Action: Review manifesto or switch sprint context
```

## Command Options
- **--recent**: Show recent activity log
- **--checklist [sprint_id]**: Detailed checklist status for specific sprint
- **--blockages**: Focus on issues preventing progress
- **--metrics**: Show detailed project metrics

## Recent Activity View (--recent)
```
🕐 RECENT PROJECT ACTIVITY
================================

2026-01-10 16:45 | Sprint completed: user_auth
2026-01-10 16:30 | Cleanup executed: 12 artifacts removed
2026-01-10 15:20 | Manifesto approved: execution boundaries locked
2026-01-10 14:30 | Planning checklist completed: all gates passed
2026-01-10 14:00 | Foundation established: project ready for sprints
```

## Metrics Dashboard (--metrics)
```
📈 PROJECT METRICS
===================

Planning Quality: 95% (19/20 gates passed across all sprints)
Execution Efficiency: 87% (successful iterations/total)
Code Quality: 92% (sanity checks passed)
Sprint Completion Rate: 100% (3/3 sprints completed)

Quality Gate Performance:
- Goals Clarity: 100% (3/3 passed)
- Code Location: 100% (3/3 passed)
- Architecture: 95% (19/20 passed)
- Testing: 90% (18/20 passed)

Average Sprint Metrics:
- Planning Time: 2.1 hours
- Execution Iterations: 8.2
- Cleanup Artifacts: 12.3
- Documentation Updates: 3.1 files
```

## Required Skills
- **project-status-analyst**: Generates comprehensive dashboard from registry data
- Model: default (standard reporting and analysis)
- Context: default (real-time status generation)
- Permissions: read (registry access only)

## Error Handling
- **Registry Corruption**: "⚠️ Project registry corrupted. Run setup.sh to reinitialize."
- **No Foundation**: "⚠️ Project not initialized. Run /startprojectplanning first."
- **State Inconsistency**: "⚠️ State inconsistency detected. Run /projectstatus --repair for diagnosis."

## Integration
- **Session Resumption**: Critical for understanding current state after interruptions
- **Workflow Guidance**: Prevents confusion about next steps
- **Progress Tracking**: Enables visibility into planning and execution quality
- **Troubleshooting**: Identifies blockages and provides solutions

## Professional Discipline
This dashboard enforces project visibility and prevents the "invisible project" syndrome. Every session begins with clear state awareness and actionable guidance, maintaining professional development practices.

## User Guidance Output
**MANDATORY STATE SYNC**: Read PROJECT_REGISTRY.json → Display OS_STATUS

**Contextual Guidance Based on Project State**:

**Foundation Incomplete**:
```
🚫 FOUNDATION INCOMPLETE
Project foundation not established

🎯 IMMEDIATE ACTION REQUIRED
Run /startprojectplanning to establish professional foundation
Without foundation, all development operations are blocked

💡 PROFESSIONAL DISCIPLINE: Foundation prevents 60% of project failures
```

**Planning Phase**:
```
📋 PLANNING PHASE ACTIVE
Planning checklist: [X]/10 gates completed

🎯 NEXT ACTIONS
1. Continue /startsprintplanning to complete quality gates
2. Use /projectstatus --checklist for detailed gate status
3. Complete all 10 gates before sprint execution

💡 PROFESSIONAL TIP: Quality gates prevent "Victory Too Early" syndrome
```

**Sprint Execution Ready**:
```
🎯 SPRINT EXECUTION READY
All planning complete, sprint boundaries established

🎯 NEXT ACTIONS
1. Run /implement to begin Ralph Wiggum execution
2. Use /projectstatus to monitor progress
3. Execute within manifesto boundaries only

💡 PROFESSIONAL DISCIPLINE: Structured execution prevents scope creep
```

**Sprint Active**:
```
🏃 SPRINT EXECUTION ACTIVE
Sprint: [ID] | Iteration: [X]/10 | Status: [Phase]

🎯 CURRENT FOCUS
Continue sprint execution within established boundaries
Use /projectstatus --recent for activity updates

💡 PROFESSIONAL TIP: Stay within manifesto boundaries for quality control
```

**Sprint Completed**:
```
✅ SPRINT COMPLETED
Sprint: [ID] | Status: Complete | Quality Score: [X]%

🎯 NEXT ACTIONS
1. Run /endsprint to complete cleanup and documentation
2. Use /listsprints to view sprint history
3. Start new sprint or review project progress

💡 PROFESSIONAL DISCIPLINE: Completion rituals improve team performance
```

**Guidance Logic**:
- Always display after status dashboard output
- Adapt guidance based on PROJECT_REGISTRY.json state
- Provide clear next-action priorities
- Include professional discipline reinforcement
- Offer specific command suggestions
- Address current project phase requirements
