# /startsprintplanning - Professional Sprint Planning with Quality Gates

## Purpose
Execute comprehensive 5-phase sprint planning workflow with integrated quality checklist and human approval gates. This enforces professional discipline by requiring ALL 10 planning quality gates pass before sprint execution, preventing the "Victory Too Early" syndrome.

## Workflow Overview
**MANDATORY STATE SYNC**: Read PROJECT_REGISTRY.json → Output OS_STATUS
**FOUNDATION VALIDATION**: Block if foundation.complete ≠ true
**5-PHASE EXECUTION**: Multi-phase planning with APPROVE_* gates
**QUALITY ASSURANCE**: Planning-qa-specialist executes comprehensive checklist
**FINAL VALIDATION**: Complete checklist report with ✅/❌ indicators

## Phase 1: Initial Plan Generation
**State Sync**: PROJECT_REGISTRY.json read → "OS_STATUS: Project [Name] | Sprint [Planning] | Phase [draft_generation]"
**Foundation Check**: Confirm foundation.complete = true
**AI Draft Creation**: Generate sprint plan with objectives, research findings, proposed approach, TDD-driven plan
**APPROVE_INITIAL_DRAFT Gate**: Human must approve to continue

**Output Format**:
```
OS_STATUS: Project [Name] | Sprint [Planning] | Phase [draft_generation]
✅ INITIAL_DRAFT_COMPLETE - Plan generated with objectives, research, approach, TDD framework
APPROVE_INITIAL_DRAFT to continue
```

## Phase 2: Architectural Analysis Pass (Quality Gates)
**Comprehensive Checklist Execution**: Execute ALL 10 planning quality validations

**Planning Quality Assurance Execution**:
```
📋 PLANNING CHECKLIST EXECUTION REPORT
==========================================

🔍 EXECUTING: Goals Clarity Verification
✅ Goals identified: [specific objectives listed]
✅ Success conditions: [explicit conditions, no null outputs]

🔍 EXECUTING: Code Location Analysis
✅ Found [X] relevant files: [file list]
✅ No placeholders - all dependencies mapped

🔍 EXECUTING: Duplication Elimination
✅ [Analysis results and unification plans]

🔍 EXECUTING: Architecture Preservation
✅ Domain-driven design alignment verified
✅ get_db_session_context() usage enforced

🔍 EXECUTING: Step-by-Step Execution
✅ [X]-step implementation roadmap detailed
✅ Dependencies and risks specified

🔍 EXECUTING: Strategic Logging
✅ Surgical logging points: [specific points identified]

🔍 EXECUTING: Dependency Management
✅ [Library research and integration plans]

🔍 EXECUTING: UI-First Design
✅ Early validation requirements specified

🔍 EXECUTING: Architectural Decisions
✅ All choices researched and made (no team options)

🔍 EXECUTING: Testing Integration
✅ TDD checkpoints and UI testing strategy defined

==========================================
PHASE 2 STATUS: ALL_GATES_PASSED
==========================================
APPROVE_ARCHITECTURAL_ANALYSIS to continue
```

**APPROVE_ARCHITECTURAL_ANALYSIS Gate**: Human approval required for all quality gates passed

## Phase 3: Decision Finalization
**Architectural Choice Research**: Deep analysis of all architectural decisions
**Consistency Validation**: Cross-reference with CLAUDE.md, rules/sub/, skills
**Self-Assessment**: Confidence evaluation (0-10 scale) with gap identification
**Final Checklist**: Current vs target state analysis
**APPROVE_FINAL_PLAN Gate**: Human approval for final plan

## Phase 4: Testing Integration & POC
**UI Testing Strategy**: Debug accordions, early validation phases
**POC Script Generation**: Service layer verification script
**Testing Gates**: TDD checkpoints throughout execution
**APPROVE_TESTING_STRATEGY Gate**: Human approval for testing approach

## Phase 5: Final Validation & Instructions
**Complete Checklist Validation**: Verify ALL 10 quality gates completed with timestamps
**Team Instructions Generation**: Cover letter for dev team with success conditions
**Final Human Approval**: APPROVE_SPRINT_PLAN

**Final Validation Report**:
```
📋 PLANNING CHECKLIST VALIDATION REPORT
==========================================

✅ GOALS CLARITY
   - All user objectives identified and documented
   - Success conditions explicitly stated (no null outputs, real data)
   - Final success metrics defined

✅ CODE LOCATION ANALYSIS
   - Every relevant file, class, method identified
   - No placeholders or "TBD" entries
   - Dependencies and imports mapped

✅ DUPLICATION ELIMINATION
   - Overlapping functionality identified
   - Unification plan specified
   - Legacy code deprecation strategy defined

✅ ARCHITECTURE PRESERVATION
   - Domain-driven design alignment verified
   - get_db_session_context() usage enforced
   - No proliferation or excessive complication

✅ STEP-BY-STEP EXECUTION
   - Detailed implementation roadmap
   - Dependencies, risks, acceptance criteria defined
   - Clear file modification lists

✅ STRATEGIC LOGGING
   - Surgical logging points identified (not excessive)
   - Key data flow tracking points specified
   - No "butter-spread" logging patterns

✅ DEPENDENCY MANAGEMENT
   - Libraries researched and justified
   - pyproject.toml integration planned
   - Proper architectural dependency handling

✅ UI-FIRST DESIGN
   - Early frontend validation requirements
   - Debug accordions for development phase
   - User feedback integration points

✅ ARCHITECTURAL DECISIONS
   - All choices researched and made (no team options)
   - Consistent with CLAUDE.md/rules/skills
   - Deep self-assessment completed (confidence 8+/10)

✅ TESTING INTEGRATION
   - TDD checkpoints throughout execution
   - UI testing strategy with browser validation
   - No database resets/drops in testing

==========================================
FINAL STATUS: ALL_GATES_PASSED | READY_FOR_SPRINT
==========================================
```

## Required Skills
- **sprint-planning-specialist**: Orchestrates 5-phase workflow with APPROVE_* gates
- **planning-qa-specialist**: Executes comprehensive checklist with detailed validation reports
- Model: opus-4.5 (complex multi-phase planning and architectural analysis)
- Context: fork (isolated planning work)
- Permissions: read, grep, run_terminal_cmd (analysis-appropriate)

## State Management
- Updates PROJECT_REGISTRY.json planning_checklist section with completion timestamps
- Sets planning_checklist.completed = true only when ALL 10 gates pass
- Maintains audit trail of checklist execution and validation results

## Error Handling
- **Foundation Incomplete**: "⚠️ Cannot start sprint planning - foundation not established. Run /startprojectplanning first."
- **Sprint Already Active**: "⚠️ Sprint already active. Complete current sprint with /endsprint before starting new planning."
- **Quality Gates Failed**: "🚫 PLANNING BLOCKED: Quality gates incomplete. Return to /startsprintplanning to complete requirements."

## Integration
- Works with /startnewsprint blocking mechanism (validates planning_checklist.completed = true)
- Enables professional sprint execution workflow
- Prevents casual development through enforced quality gates

## User Guidance Output
**MANDATORY STATE SYNC**: Read PROJECT_REGISTRY.json → Display OS_STATUS

**Phase-Specific Guidance**:

**After APPROVE_INITIAL_DRAFT**:
```
📋 PLANNING PHASE 1 COMPLETE
✅ Initial sprint plan generated
✅ Research findings documented
✅ TDD framework established

🎯 NEXT: Phase 2 - Architectural Analysis
Run planning checklist execution to validate all quality gates
💡 PROFESSIONAL TIP: Quality gates prevent "Victory Too Early" syndrome
```

**After APPROVE_ARCHITECTURAL_ANALYSIS**:
```
📋 PLANNING PHASE 2 COMPLETE
✅ All 10 quality gates validated
✅ Code location analysis complete
✅ Architecture preservation confirmed
✅ Dependencies researched

🎯 NEXT: Phase 3 - Decision Finalization
Complete architectural decisions for execution readiness
💡 PROFESSIONAL TIP: Clear decisions prevent team option paralysis
```

**After APPROVE_FINAL_PLAN**:
```
📋 SPRINT PLANNING COMPLETE
✅ All planning phases completed
✅ Quality gates: 10/10 PASSED
✅ Confidence score: [X]/10
✅ Ready for sprint execution

🎯 NEXT STEPS
1. Run /startnewsprint to lock execution boundaries
2. Use /projectstatus to verify planning completion
3. Begin professional sprint execution

💡 PROFESSIONAL DISCIPLINE: Comprehensive planning enables focused execution
```

**Guidance Logic**:
- Display after each APPROVE_* gate completion
- Show current phase progress and next requirements
- Provide professional discipline reinforcement
- Include specific next-action commands
- Adapt guidance based on PROJECT_REGISTRY.json planning state
