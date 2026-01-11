# ABANDON-SPRINT: Cancel Active Sprint with Artifact Preservation
**Purpose**: Safely cancel current sprint, preserve all artifacts for analysis, and prepare for new sprint initiation.

## COMMAND EXECUTION PROTOCOL

### Trigger Conditions
**Abandonment Scenarios**:
- Requirements fundamentally changed
- Technical approach proven infeasible
- Higher priority work requires immediate attention
- External factors make continuation impossible
- Strategic pivot requires different direction

### Pre-Abandon Validation
**Cancellation Readiness Check**:
1. **Active Sprint Verification**: Confirm sprint exists and status is "active"
2. **Reason Documentation**: Require human-provided abandonment reason
3. **Artifact Preservation**: Ensure all work is safely preserved
4. **State Consistency**: Verify no corrupted or inconsistent state

## SPRINT ABANDONMENT SEQUENCE

### Step 1: Reason Documentation
**Structured Abandonment Record**:
```json
{
  "abandonment_record": {
    "sprint_id": "2026-01-09_plan_004_user_auth",
    "abandoned_timestamp": "2026-01-09T14:30:00Z",
    "reason_category": "requirements_changed|technical_blocker|priority_shift|external_factors",
    "reason_description": "User requirements shifted to SAML authentication instead of JWT",
    "work_completed_percentage": 65,
    "valuable_insights_preserved": [
      "JWT token validation logic in temp/jwt_validator.ts",
      "User session management patterns in temp/session_design.md",
      "Performance benchmarks for auth endpoints in temp/auth_benchmarks.csv"
    ],
    "lessons_learned": [
      "JWT tokens have better mobile app compatibility than initially planned",
      "Session management complexity was underestimated",
      "SAML integration will be needed for enterprise customers"
    ]
  }
}
```

### Step 2: Artifact Preservation
**Complete Work Preservation**:
1. **Temp Directory Archival**: Preserve entire temp/claudecode/[sprint_id]/ directory
2. **Metadata Preservation**: Save all sprint metadata and state information
3. **Partial Deliverables**: Identify and preserve any completed work components
4. **Knowledge Capture**: Document insights and learnings for future reference

### Step 3: State Cleanup
**Safe State Transition**:
```json
{
  "active_sprint": null,
  "sprint_history": [
    {
      "id": "2026-01-09_plan_004_user_auth",
      "abandoned": "2026-01-09T14:30:00Z",
      "status": "abandoned",
      "reason": "requirements_changed",
      "work_completed_percentage": 65,
      "artifacts_preserved": true,
      "partial_deliverables": ["temp/claudecode/2026-01-09_plan_004_user_auth/jwt_validator.ts"],
      "lessons_learned": ["JWT better for mobile", "SAML needed for enterprise"]
    }
  ]
}
```

### Step 4: Boundary Removal
**Sovereignty Cleanup**:
1. **File Lock Removal**: Clear all locked_files restrictions
2. **Path Validation Reset**: Remove sprint-specific file boundaries
3. **Safety Hook Reset**: Return to default enforcement state
4. **Context Isolation**: Ensure no cross-sprint interference

## ARTIFACT MANAGEMENT STRATEGY

### Preservation Categories
**Intelligent Artifact Handling**:
- **Valuable Code**: Completed components that might be reusable
- **Design Documents**: Architecture decisions and design rationale
- **Test Results**: Performance data and validation results
- **Debug Logs**: Error patterns and troubleshooting information
- **Research Findings**: Technical investigations and evaluations
- **Meeting Notes**: Requirements discussions and decisions

### Storage Organization
**Archived Structure**:
```
temp/claudecode/abandoned/
├── 2026-01-09_plan_004_user_auth/
│   ├── artifacts/          # All original temp files
│   ├── metadata.json       # Abandonment record
│   ├── partial_work/       # Completed components
│   └── analysis/          # Insights and lessons
└── archive_index.json     # Catalog of all abandoned sprints
```

### Retention Policy
**Preservation Guidelines**:
- **Immediate Retention**: All artifacts preserved for minimum 90 days
- **Review Cycles**: Quarterly review of abandoned sprint value
- **Archival Process**: Valuable insights migrated to knowledge base
- **Cleanup Authorization**: Explicit approval required for permanent deletion

## LESSONS LEARNED CAPTURE

### Structured Learning Process
**Knowledge Extraction**:
1. **Technical Learnings**: What worked well and what didn't
2. **Process Insights**: Sprint methodology effectiveness
3. **Requirements Understanding**: How requirements evolved
4. **Risk Assessment**: Early warning signs that were missed
5. **Success Patterns**: What enabled the completed portion

### Future Sprint Preparation
**Preventive Measures**:
- **Risk Mitigation**: Patterns to avoid similar issues
- **Success Factors**: What enabled progress before abandonment
- **Early Warning**: Indicators to watch for in future sprints
- **Alternative Approaches**: Different strategies to consider

## SYSTEM RECOVERY PROTOCOL

### State Consistency Restoration
**Clean System State**:
1. **Active Sprint Clearing**: Ensure no lingering active sprint references
2. **File Boundary Removal**: Complete elimination of sprint-specific restrictions
3. **Safety Hook Reset**: Return to default security enforcement
4. **Context Isolation**: Prevent any cross-contamination

### New Sprint Preparation
**Clean Slate Assurance**:
1. **State File Validation**: Confirm SPRINT_STATE.json is consistent
2. **Directory Readiness**: Ensure temp/claudecode/ is ready for new sprint
3. **Command Availability**: Verify all sprint commands functional
4. **Context Pruning**: Apply clean context for new work

## SUCCESS VALIDATION

### Abandonment Integrity
**Safe Cancellation Verification**:
- ✅ Sprint status correctly updated to "abandoned" in SPRINT_STATE.json
- ✅ Abandonment timestamp and reason properly recorded
- ✅ Active sprint cleared to prevent interference
- ✅ File boundaries completely removed
- ✅ Safety hooks reset to default state

### Artifact Preservation
**Work Protection Quality**:
- ✅ All temp directory contents preserved in archival structure
- ✅ Valuable components identified and flagged for future reference
- ✅ Metadata and abandonment reasons fully documented
- ✅ Lessons learned captured for organizational knowledge
- ✅ Archival structure allows easy future retrieval

### System State Cleanliness
**Recovery Completeness**:
- ✅ No active sprint locks preventing new work
- ✅ File operation boundaries completely cleared
- ✅ Safety enforcement returned to default configuration
- ✅ Context isolation maintained for new sprint creation
- ✅ Command system ready for immediate new sprint initiation

### Learning Capture Effectiveness
**Knowledge Preservation**:
- ✅ Technical lessons documented and categorized
- ✅ Process insights captured for methodology improvement
- ✅ Risk patterns identified for future prevention
- ✅ Success factors preserved for replication
- ✅ Alternative approaches documented for future consideration

### Operational Continuity
**System Resilience**:
- ✅ Graceful handling of sprint cancellation
- ✅ Minimal disruption to development workflow
- ✅ Clear path for immediate new sprint creation
- ✅ Preserved work available for future reference
- ✅ No permanent system state corruption
