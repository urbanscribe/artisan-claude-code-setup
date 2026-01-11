# /deepselfassessment - Intelligent Sprint Progress Analysis & Intervention

## Purpose
Perform comprehensive self-assessment of sprint progress with regression detection, completion percentage calculation, and detailed path correction guidance. This replaces arbitrary iteration limits with intelligent human-in-the-loop decision making.

## Assessment Triggers
**Automatic Triggers:**
- Iteration 25 reached (primary checkpoint)
- Manual invocation: `/deepselfassessment`
- Optional: Iterations 10, 40, 60 for complex sprints

**Context Preservation:**
- Maintains full sprint execution state
- No interruption of active work
- Provides actionable intelligence for continuation

## Progress Analysis Engine (MANDATORY STATE SYNC)

### 0) Completion Percentage Calculation
**MANDATORY STATE SYNC**: Read PROJECT_REGISTRY.json → Analyze sprint objectives vs deliverables

**Progress Metrics:**
- **Objective Completion:** Compare current deliverables to sprint manifesto goals
- **Quality Gates:** Verify testing integration and UI validation completion
- **Dependency Resolution:** Check library integration and architectural decisions
- **Regression Impact:** Assess any reversions from recent refactoring work

**Output Format:**
```
SPRINT PROGRESS ASSESSMENT
========================
Completion: 68% (Prior: 52% | Rate: +16%)
Objectives Met: 8/12 | Quality Gates: 6/8 | Dependencies: 4/5
Regression Status: ✅ NONE DETECTED
Estimated Completion: 14 iterations | Confidence: HIGH
```

### 1) Issue Verification & Regression Detection
**MANDATORY STATE SYNC**: Compare current iteration state to previous iterations

**Regression Analysis:**
- **Code Quality:** Verify recent refactoring preserved
- **Testing Integrity:** Confirm real database testing (no mocks/resets)
- **Architectural Compliance:** Check domain-driven design alignment
- **UI/UX Standards:** Validate accessibility and usability requirements

**Output Format:**
```
REGRESSION ANALYSIS
==================
✅ Recent refactor work preserved
✅ Database integrity maintained
⚠️  Testing gaps identified (2 critical)
❌ UI validation incomplete (-15% progress impact)
```

### 2) Rate Analysis & Completion Estimation
**MANDATORY STATE SYNC**: Analyze progress velocity across iterations

**Velocity Metrics:**
- **Progress Rate:** Percentage points per iteration
- **Completion Trajectory:** ETA calculation based on current velocity
- **Blockage Detection:** Identify factors slowing progress
- **Acceleration Opportunities:** Suggest optimization strategies

**Output Format:**
```
PROGRESS VELOCITY ANALYSIS
=========================
Current Rate: +2.3%/iteration (Target: +3.0%)
ETA to 100%: 14 iterations (Confidence: 78%)
Blockage Factor: Testing complexity (-0.7%/iteration)
Acceleration: Parallel testing implementation (+1.2% potential)
```

## Intervention Decision Framework

### Assessment-Based Recommendations
**Progress Velocity > 2.5%/iteration:**
```
✅ CONTINUE EXECUTION
Recommendation: Proceed with current approach
Optimization: Consider parallel testing implementation
```

**Progress Velocity 1.5-2.5%/iteration:**
```
⚠️  ASSESSMENT RECOMMENDED
Issues Detected: [specific problems]
Recommendation: Address identified issues before continuation
```

**Progress Velocity < 1.5%/iteration:**
```
🚫 INTERVENTION REQUIRED
Critical Issues: [blocking problems]
Recommendation: Halt execution, address root causes
Alternative: Sprint restructuring or abandonment
```

## Path Correction Instructions

### Detailed Guidance Format
**When Issues Detected:** Provide comprehensive "Dear Team" instructions

```
DEAR TEAM,

SPRINT PROGRESS ANALYSIS COMPLETE
================================

CURRENT STATUS:
- Completion: 68%
- Primary Blockage: Testing integration gaps
- Secondary Issue: UI validation incomplete

REQUIRED ACTIONS:

1. **IMMEDIATE TESTING INTEGRATION**
   - Implement real database testing (no mocks)
   - Verify data integrity across user flows
   - Document testing procedures for regression prevention

2. **UI VALIDATION COMPLETION**
   - Complete accessibility requirements
   - Implement cross-browser validation
   - Add performance benchmarking

3. **PROGRESS ACCELERATION**
   - Parallelize testing and development workflows
   - Implement automated validation gates
   - Daily progress checkpoints

CODE, TEST, AND REDELIVER WITH THESE CORRECTIONS.
Focus on meaningful progress, not micro-steps.

END OF ASSESSMENT
================
```

## Integration with Ralph Wiggum Loop

### Assessment Integration Points
**Iteration 25 (Primary Checkpoint):**
- Automatic `/deepselfassessment` trigger
- Human approval required for continuation
- Progress report generation
- Path correction if needed

**Manual Invocation:**
- Available anytime during sprint execution
- No iteration restrictions
- Full assessment on demand

### State Management Integration
**PROJECT_REGISTRY.json Extensions:**
```json
{
  "sprints": {
    "active": {
      "progress_tracking": {
        "completion_percentage": 68,
        "last_assessment_iteration": 25,
        "regression_events": [],
        "progress_rate": 2.3,
        "estimated_completion_iterations": 14
      }
    }
  }
}
```

## Quality Assurance Integration

### Testing Requirements Enforcement
**MANDATORY VERIFICATION:**
- [ ] Real database testing (no resets/drops/duplication)
- [ ] UI-first validation with browser testing
- [ ] Data integrity preservation across iterations
- [ ] Performance benchmarking inclusion

**VIOLATION DETECTION:**
```
TESTING INTEGRITY VIOLATION DETECTED
===================================
❌ Mock data usage detected (reset operations found)
❌ Database isolation (test environment duplication)
❌ UI testing bypassed (no browser validation)

CORRECTIVE ACTION REQUIRED:
- Implement real data testing
- Remove mock data dependencies
- Add browser-based UI validation
```

## Success Validation

### Assessment Completeness
- ✅ Progress percentage calculated and trended
- ✅ Regression analysis completed
- ✅ Rate analysis with ETA estimation
- ✅ Testing integrity verified
- ✅ Path correction instructions provided
- ✅ State management updated

### User Experience Validation
- ✅ Clear progress visibility provided
- ✅ Actionable guidance delivered
- ✅ No execution interruption during assessment
- ✅ Sprint continuation possible after correction
- ✅ Learning applied to future assessments

## Emergency Override Mechanism

### Human Escalation for False Positives
**When Assessment Incorrectly Blocks:**
- Manual override: `--override-assessment`
- Justification required: `--justification "explanation"`
- Audit trail maintained in sprint history

**Usage:**
```
/deepselfassessment --override-assessment --justification "Assessment incorrectly detected regression - recent refactor actually improved code quality"
```

This ensures the intelligent assessment system remains helpful rather than becoming a blocker itself.
