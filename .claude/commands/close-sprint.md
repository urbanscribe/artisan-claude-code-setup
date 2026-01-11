# CLOSE-SPRINT: Complete Active Sprint with Architectural Handoff
**Purpose**: Mark current sprint as completed, trigger architectural evolution, and perform cleanup while preserving artifacts.

## COMMAND EXECUTION PROTOCOL

### Trigger Conditions
**Completion Scenarios**:
- Sprint objectives fully achieved
- All acceptance criteria met
- Final testing passed
- Ready for architectural handoff

### Pre-Close Validation
**Completion Readiness Check**:
1. **Active Sprint Verification**: Confirm sprint exists and status is "active"
2. **Deliverable Assessment**: Verify all planned work completed
3. **Testing Validation**: Confirm final tests passed
4. **Documentation Completeness**: Ensure plan and deliverables documented

### Architectural Handoff Preparation
**Evolution Data Collection**:
1. **Pattern Recognition**: Identify new patterns established during sprint
2. **Constraint Updates**: Determine architectural boundaries that changed
3. **Knowledge Transfer**: Document learnings and decisions made
4. **Documentation Updates**: Prepare changes for global architecture files

## SPRINT COMPLETION SEQUENCE

### Step 1: Final State Capture
**Completion Snapshot**:
```json
{
  "sprint_completion": {
    "id": "2026-01-09_plan_004_user_auth",
    "completed_timestamp": "2026-01-09T16:45:00Z",
    "final_phase": "evaluation",
    "final_iteration": 5,
    "completion_status": "success",
    "final_files": [
      "src/auth/UserAuthenticator.ts",
      "src/auth/AuthMiddleware.ts",
      "tests/auth/AuthenticationTests.ts",
      "documentation/api/auth-endpoints.md"
    ],
    "artifacts_preserved": [
      "temp/claudecode/2026-01-09_plan_004_user_auth/debug.log",
      "temp/claudecode/2026-01-09_plan_004_user_auth/test_results.json"
    ]
  }
}
```

### Step 2: Comprehensive Artifact Analysis
**Evaluator-Driven Orphaned Code Detection and Architectural Assessment**:

**Artifact Inventory and Analysis**:
```python
# comprehensive_artifact_analysis.py
def analyze_sprint_artifacts(sprint_temp_dir, final_deliverables, sprint_context):
    """Comprehensive analysis of sprint artifacts for architectural insights and cleanup."""

    analysis_results = {
        'orphaned_artifacts': [],
        'architectural_insights': [],
        'pattern_discoveries': [],
        'lessons_learned': [],
        'cleanup_recommendations': []
    }

    if os.path.exists(sprint_temp_dir):
        for root, dirs, files in os.walk(sprint_temp_dir):
            for file in files:
                file_path = os.path.join(root, file)
                file_analysis = analyze_artifact_file(file_path, final_deliverables, sprint_context)

                if file_analysis['is_orphaned']:
                    analysis_results['orphaned_artifacts'].append(file_analysis)
                else:
                    # Extract architectural value from non-orphaned artifacts
                    insights = extract_architectural_insights(file_path, sprint_context)
                    if insights:
                        analysis_results['architectural_insights'].extend(insights)

    # Generate cleanup recommendations
    analysis_results['cleanup_recommendations'] = generate_cleanup_strategy(
        analysis_results['orphaned_artifacts'],
        analysis_results['architectural_insights']
    )

    return analysis_results

def analyze_artifact_file(file_path, final_deliverables, sprint_context):
    """Detailed analysis of individual artifact file."""

    file_info = {
        'path': file_path,
        'is_orphaned': True,
        'value_assessment': 'unknown',
        'architectural_significance': 'low',
        'retention_recommendation': 'cleanup'
    }

    # Check direct references in final deliverables
    is_referenced = any(
        file_path in delivered_file or
        os.path.basename(file_path) in delivered_file
        for delivered_file in final_deliverables
    )

    if is_referenced:
        file_info['is_orphaned'] = False
        file_info['value_assessment'] = 'referenced'
        file_info['retention_recommendation'] = 'preserve'
        return file_info

    # Analyze content for architectural value
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        # Check for architectural keywords and patterns
        architectural_indicators = [
            'pattern', 'architecture', 'design', 'decision',
            'constraint', 'requirement', 'interface', 'contract',
            'protocol', 'strategy', 'approach', 'solution'
        ]

        content_lower = content.lower()
        architectural_matches = sum(1 for indicator in architectural_indicators
                                  if indicator in content_lower)

        if architectural_matches >= 3:
            file_info['architectural_significance'] = 'high'
            file_info['is_orphaned'] = False
            file_info['value_assessment'] = 'architectural_insight'
            file_info['retention_recommendation'] = 'preserve'

        # Check for lessons learned indicators
        lesson_indicators = [
            'lesson', 'learned', 'improvement', 'issue', 'problem',
            'solution', 'challenge', 'mistake', 'success', 'failure'
        ]

        lesson_matches = sum(1 for indicator in lesson_indicators
                           if indicator in content_lower)

        if lesson_matches >= 2:
            file_info['architectural_significance'] = 'medium'
            file_info['is_orphaned'] = False
            file_info['value_assessment'] = 'lessons_learned'
            file_info['retention_recommendation'] = 'review'

    except Exception:
        pass

    return file_info
```

### Step 3: Evaluator Analysis and Human Approval
**Comprehensive Architectural Assessment and Approval Gates**:

**Evaluator Analysis Process**:
1. **Pattern Recognition**: Automatic scanning of deliverables for architectural patterns
2. **Artifact Analysis**: Deep evaluation of temp directory for insights and cleanup
3. **Documentation Impact Assessment**: Analysis of required global documentation updates
4. **Knowledge Transfer Preparation**: Formulation of lessons learned and pattern documentation

**Human Approval Gate Presentation**:
```
SPRINT ARCHITECTURAL EVOLUTION ASSESSMENT
==========================================

Sprint: 2026-01-09_plan_004_user_auth
Completed: 2026-01-09T16:45:00Z
Evaluator Analysis: COMPLETED

📊 DELIVERABLES ANALYSIS:
Final Files: 4 production deliverables
Patterns Identified: 3 architectural patterns
Integration Points: 2 new system interactions
Quality Improvements: 1 testing strategy enhancement

🔍 ARTIFACT ANALYSIS:
Total Artifacts: 12 files (45KB)
Architectural Insights: 3 valuable documents
Lessons Learned: 2 documented learnings
Orphaned Files: 7 candidates for cleanup

📝 PROPOSED ARCHITECTURAL UPDATES:

ARCHITECTURE.MD CHANGES:
------------------------
• Add "JWT Authentication Pattern" section
  - Stateless authentication with middleware integration
  - Components: UserAuthenticator, AuthMiddleware, TokenManager
  - Usage: All future authentication requirements

• Update "API Integration Patterns"
  - Add middleware-based request validation
  - Document token refresh strategies

• Add "Testing Strategy Enhancement"
  - Integration test-first approach
  - Contract validation for API endpoints

KEYGOALS.MD CHANGES:
--------------------
• Add Security Infrastructure Objective
  - Enterprise-grade authentication system
  - Timeline: Q2 2026, Budget: $50K

🧹 CLEANUP RECOMMENDATIONS:
Preserve (3 files): debug.log, test_results.json, performance_benchmarks.csv
Review (2 files): scratch_notes.md, user_feedback.md
Remove (7 files): alternative_approach.ts, api_design_v2.json, temp_calculations.xlsx

APPROVAL OPTIONS:
1. APPROVE_ALL - Accept all recommendations
2. APPROVE_UPDATES_ONLY - Accept documentation updates, review cleanup manually
3. REVIEW_CHANGES - Examine proposed changes in detail
4. REJECT_ALL - Cancel architectural evolution

Choose approval level (1-4):
```

**Approval Processing**:
- **APPROVE_ALL**: Automatic implementation of all recommendations
- **APPROVE_UPDATES_ONLY**: Documentation updates applied, cleanup requires separate approval
- **REVIEW_CHANGES**: Detailed examination interface for each proposed change
- **REJECT_ALL**: Sprint completion without architectural evolution

### Step 4: Architectural Evolution Assessment
**Comprehensive Evaluation and Update Generation**:
1. **Significance Assessment**: Evaluate if sprint qualifies for architectural updates
2. **Pattern Recognition**: Identify new architectural patterns from deliverables
3. **Documentation Impact Analysis**: Determine required global documentation changes
4. **Update Proposal Generation**: Create comprehensive update proposals for human review

### Step 5: Human Approval and Integration
**Controlled Architectural Evolution**:
1. **Update Presentation**: Display proposed architectural changes for approval
2. **Human Review**: Allow detailed examination and modification suggestions
3. **Approval Processing**: Apply approved updates to global documentation
4. **Integration Verification**: Confirm documentation updates are properly applied

### Step 6: State Finalization
**SPRINT_STATE.json Updates**:
```json
{
  "active_sprint": null,
  "sprint_history": [
    {
      "id": "2026-01-09_plan_004_user_auth",
      "completed": "2026-01-09T16:45:00Z",
      "status": "completed",
      "final_files": ["src/auth/", "tests/auth/", "documentation/api/auth-endpoints.md"],
      "artifacts_cleaned": 5,
      "architectural_updates": ["New authentication pattern documented"],
      "lessons_learned": ["JWT tokens preferred over sessions for scalability"]
    }
  ],
  "global_context": {
    "architecture_last_updated": "2026-01-09T16:45:00Z",
    "current_hash": "updated_hash_after_architecture_changes"
  }
}
```

## ARCHITECTURAL EVOLUTION TRIGGER CONDITIONS

### Automatic Evaluation Triggers
**Sprint Completion Analysis**:
- ✅ **Sprint Completion**: Any sprint ending triggers comprehensive evaluation
- ✅ **New Architectural Decisions**: Patterns that affect future sprint planning
- ✅ **Global Constraint Changes**: Boundaries requiring documentation updates
- ❌ **Micro-changes Excluded**: Test additions, minor refactors don't trigger updates

**Evaluation Criteria**:
```python
def evaluate_architectural_significance(sprint_data):
    """Determine if sprint completion requires architectural updates."""

    significance_score = 0

    # Pattern establishment (high impact)
    if sprint_data.get('new_patterns_established', 0) > 0:
        significance_score += 3

    # Architectural decisions (high impact)
    if sprint_data.get('architectural_decisions_made', False):
        significance_score += 3

    # Constraint modifications (medium impact)
    if sprint_data.get('constraints_modified', False):
        significance_score += 2

    # Integration changes (medium impact)
    if sprint_data.get('integration_patterns_changed', False):
        significance_score += 2

    # Quality improvements (low impact)
    if sprint_data.get('quality_standards_improved', False):
        significance_score += 1

    # Micro-change exclusions
    micro_indicators = [
        'test_only_changes',
        'documentation_only_updates',
        'minor_refactoring',
        'bug_fixes_only'
    ]

    for indicator in micro_indicators:
        if sprint_data.get(indicator, False):
            significance_score = max(0, significance_score - 1)

    return significance_score >= 2  # Threshold for architectural updates
```

## ARCHITECTURAL HANDOFF PROTOCOL

### Pattern Recognition Engine
**Automatic Pattern Detection and Analysis**:
- **Code Patterns**: Identify recurring implementation approaches, naming conventions, structural patterns
- **Integration Patterns**: Document API designs, data flow patterns, service interaction approaches
- **Testing Patterns**: Note testing strategies, coverage approaches, quality assurance methods
- **Error Handling Patterns**: Document exception management, validation approaches, recovery strategies
- **Performance Patterns**: Identify optimization techniques, caching strategies, scalability approaches

**Pattern Recognition Algorithm**:
```python
def analyze_sprint_patterns(deliverables, artifacts):
    """Analyze sprint deliverables for architectural patterns."""

    patterns = {
        'implementation_patterns': [],
        'integration_patterns': [],
        'testing_patterns': [],
        'architectural_decisions': []
    }

    # Analyze code files for patterns
    for file_path in deliverables:
        if file_path.endswith(('.ts', '.js', '.py')):
            patterns_found = analyze_code_patterns(file_path)
            patterns['implementation_patterns'].extend(patterns_found)

    # Analyze artifacts for additional insights
    for artifact in artifacts:
        if 'design' in artifact.lower() or 'architecture' in artifact.lower():
            design_patterns = extract_design_patterns(artifact)
            patterns['architectural_decisions'].extend(design_patterns)

    return consolidate_patterns(patterns)
```

### Documentation Updates
**Automatic Global Architecture Evolution**:

**Proposed Architecture.md Updates**:
```
### New Patterns Established

#### [Pattern Name - Auto-detected from sprint]
**Context**: Sprint [sprint_id] - [sprint_description]
**Pattern**: [Automatically extracted from implementation analysis]
**Components**:
- [Auto-detected components from deliverables]
**Usage**: [Recommended application scenarios]
**Rationale**: [Extracted benefits and lessons learned]

#### [Additional Patterns - Auto-detected]
**Context**: Sprint [sprint_id] architectural decisions
**Pattern**: [Integration/testing/error handling patterns]
**Benefits**: [Measured improvements and outcomes]
**Application**: [Future sprint requirements]
```

**Proposed Keygoals.md Updates**:
```
### Updated Objectives ([Current Date])

#### [New Objective from Sprint Learnings]
**Context**: Sprint [sprint_id] revealed [gap/opportunity]
**Objective**: [Automatically formulated from sprint outcomes]
**Success Criteria**: [Measurable goals based on sprint results]
**Timeline**: [Recommended implementation timeline]
```

**Human Approval Gate for Documentation Updates**:
```
ARCHITECTURAL EVOLUTION PROPOSAL
=================================

Sprint: 2026-01-09_plan_004_user_auth
Completed: 2026-01-09T16:45:00Z

PROPOSED DOCUMENTATION UPDATES:
==============================

📝 Architecture.md Changes:
• Add "JWT Authentication Pattern" section
• Update "API Integration Patterns" with new middleware approach
• Document "Testing Strategy Enhancement" for integration-first testing

🎯 Keygoals.md Changes:
• Add objective for enterprise authentication system
• Update security requirements based on JWT implementation experience

📊 Pattern Recognition Results:
• Identified 3 new implementation patterns
• Found 2 integration pattern improvements
• Discovered 1 testing strategy enhancement

APPROVE_DOCUMENTATION_UPDATES [y/n]: Accept these architectural updates?
```

**Automatic Documentation Integration**:
- **Approved Updates**: Automatically merged into global documentation files
- **Version Control**: Timestamp and sprint reference added to all changes
- **Cross-references**: Links between related patterns and objectives established
- **Change Tracking**: Complete audit trail of architectural evolution

### Constraint Evolution
**Global Rule Updates**:
- **New Constraints**: Based on sprint learnings and challenges
- **Pattern Requirements**: Mandatory patterns for future sprints
- **Quality Standards**: Updated based on achieved excellence levels
- **Integration Rules**: New system interaction requirements

## CLEANUP AND PRESERVATION

### Selective Artifact Management
**Intelligent Preservation**:
- **Debug Logs**: Always preserve (research-backed debugging value)
- **Test Results**: Keep for regression analysis and performance tracking
- **Design Documents**: Review for architectural insights
- **Alternative Approaches**: Remove to prevent confusion
- **Scratch Work**: Evaluate for undocumented insights

### Storage Optimization
**Artifact Lifecycle**:
- **Immediate Cleanup**: Remove obviously obsolete files
- **Review Queue**: Flag files needing human evaluation
- **Archival Process**: Compress and store valuable artifacts
- **Automatic Cleanup**: Remove temp files after retention period

## SUCCESS VALIDATION

### Completion Integrity
**Sprint Closure Verification**:
- ✅ All deliverables properly documented and accessible
- ✅ Sprint status updated to "completed" in SPRINT_STATE.json
- ✅ Final files recorded in sprint history
- ✅ Completion timestamp and metrics captured
- ✅ Active sprint cleared for new sprint creation

### Architectural Evolution
**Knowledge Transfer Success**:
- ✅ New patterns identified and documented
- ✅ Global architecture files updated appropriately
- ✅ Constraint evolution applied to future sprints
- ✅ Lessons learned preserved for organizational knowledge
- ✅ Documentation maintains consistency and clarity

### Cleanup Effectiveness
**Artifact Management Quality**:
- ✅ Orphaned code detected and categorized
- ✅ Human approval required for significant cleanup
- ✅ Valuable artifacts preserved for future reference
- ✅ Storage optimization applied appropriately
- ✅ Cleanup actions logged and reversible

### System State Integrity
**Post-Closure Validation**:
- ✅ No active sprint lock preventing new work
- ✅ File boundaries completely removed
- ✅ Safety hooks reset to default state
- ✅ Global context hash updated if architecture changed
- ✅ Sprint history accurately reflects completion status
