# Phase Markers Sub-Rule (Tier 3)
## Purpose
Standardizes phase completion markers and plan formatting for consistent workflow tracking.

## REQUIRED MARKER FORMAT

### Planning Phase Markers
**STANDARD COMPLETION SIGNALS**:
```
INITIAL_PLAN_COMPLETE
├── Architecture Summary: [brief overview]
├── Key Decisions: [major architectural choices]
├── Unresolved: NONE
└── READY_FOR_PLANNER_REVIEW
```

**IMPROVED PLAN MARKERS**:
```
PLAN_IMPROVEMENT_COMPLETE
├── Clarity Score: [1-10]
├── Risk Assessment: [identified risks]
├── Unresolved: NONE
└── READY_FOR_FINAL_PLAN
```

**FINAL PLAN MARKERS**:
```
FINAL_PLAN_COMPLETE
├── ARCH_DECISIONS:
│   ├── [Decision 1] → [Reason] → [Code Location]
│   └── [Decision 2] → [Reason] → [Code Location]
├── Unresolved: NONE
└── READY_FOR_CODER
```

### Implementation Phase Markers
**CODING COMPLETION**:
```
CODING_COMPLETE
├── Files Modified: [count]
├── Tests Added: [count]
├── Test Execution: [0 failures]
└── READY_FOR_TESTER
```

**TESTING COMPLETION**:
```
TESTING_COMPLETE
├── Unit Tests: [passed/failed]
├── Integration Tests: [passed/failed]
├── UI Tests: [passed/failed]
├── Coverage: [percentage]%
└── READY_FOR_EVALUATOR
```

### Evaluation Phase Markers
**QUALITY ASSESSMENT**:
```
EVALUATION_COMPLETE
├── Confidence Score: [0-100]
├── Critical Issues: [count]
├── Approval Status: [APPROVED/REQUIRES_FIXES]
└── READY_FOR_DEPLOYMENT
```

**SANITY CHECK COMPLETION**:
```
SANITY_CHECK_COMPLETE
├── UI Integrity: [PASS/FAIL]
├── Data Coherence: [PASS/FAIL]
├── Console Errors: [count]
├── Logic Violations: [count]
└── READY_FOR_EVALUATOR
```

## MARKER VALIDATION RULES

### Format Consistency
**REQUIRED ELEMENTS**:
- [ ] All caps marker names
- [ ] Underscore separation (READY_FOR_*)
- [ ] Complete marker on single line
- [ ] Preceded by blank line
- [ ] Followed by detailed breakdown

### Content Completeness
**MANDATORY DETAILS**:
- [ ] Quantitative metrics where applicable
- [ ] Status indicators (PASS/FAIL, counts, percentages)
- [ ] Clear next step indication
- [ ] Error summaries when applicable

### Timing Requirements
**PROPER SEQUENCE**:
- [ ] Markers appear at phase completion
- [ ] No markers before work completion
- [ ] All prerequisites met before marker
- [ ] Next phase requirements clearly stated

## PLAN FORMATTING STANDARDS

### Document Structure
**STANDARD OUTLINE**:
```
# YYYY-MM-DD_plan_N_feature.md
├── Executive Summary
│   ├── Feature Description
│   ├── Business Value
│   ├── Success Criteria
│   └── Timeline Estimate
├── Technical Specification
│   ├── Functional Requirements
│   ├── Non-Functional Requirements
│   ├── API Specifications
│   └── Data Models
├── Implementation Plan
│   ├── Architecture Decisions
│   ├── Component Design
│   ├── Testing Strategy
│   └── Deployment Plan
├── Risk Assessment
│   ├── Technical Risks
│   ├── Business Risks
│   └── Mitigation Strategies
└── Success Metrics
    ├── Quality Gates
    ├── Performance Benchmarks
    └── Monitoring Requirements
```

### Section Formatting
**CONSISTENT STRUCTURE**:
- **Headers**: # ## ### hierarchy with consistent capitalization
- **Lists**: - for unordered, 1. 2. 3. for ordered sequences
- **Code Blocks**: ```language for syntax highlighting
- **Tables**: | Column | Headers | with proper alignment
- **Links**: [Text](URL) for cross-references

### Content Standards
**QUALITY REQUIREMENTS**:
- **Specificity**: No vague terms (e.g., "good performance" → "response time <200ms")
- **Measurability**: All requirements quantifiable and testable
- **Traceability**: Each requirement linked to business objective
- **Completeness**: No TBD or TODO placeholders

## WORKFLOW INTEGRATION MARKERS

### Human Gate Indicators
**APPROVAL SIGNALS**:
```
APPROVE_PLAN
├── Review Complete: [timestamp]
├── Concerns Addressed: [yes/no]
└── Confidence Level: [high/medium/low]
```

**ESCALATION MARKERS**:
```
HUMAN_GATE_REQUIRED
├── Issue Type: [clarification/technical/blocker]
├── Description: [specific problem]
├── Impact: [timeline/quality/scope]
└── Required Action: [human decision needed]
```

### Error Condition Markers
**FAILURE SIGNALS**:
```
VALIDATION_FAILED
├── Check Type: [security/performance/compatibility]
├── Severity: [critical/high/medium]
├── Description: [specific failure]
└── Remediation Required: [yes/no]
```

**RECOVERY MARKERS**:
```
RECOVERY_COMPLETE
├── Issue Resolved: [description]
├── Root Cause: [identified cause]
├── Prevention: [future safeguards]
└── Confidence Restored: [yes/no]
```

## MARKER AUTOMATION RULES

### Hook Integration
**VALIDATION_POST_TOOL.PY**:
```python
def validate_phase_markers(output: str) -> dict:
    """Validate required phase markers are present and correctly formatted"""
    required_markers = [
        'READY_FOR_',
        'COMPLETE',
        '_SCORE:',
        'APPROVE_'
    ]

    for marker in required_markers:
        if marker in output:
            # Validate format and completeness
            pass

    return {'markers_valid': True}
```

### Command Integration
**IMPLEMENT.MD WORKFLOW**:
- **Pre-marker validation**: Ensure all prerequisites met
- **Marker generation**: Automatic insertion at phase completion
- **Post-marker validation**: Verify marker format and content
- **Progress tracking**: Update global progress state

## MARKER MONITORING AND ANALYTICS

### Progress Tracking
**GLOBAL STATE MANAGEMENT**:
```python
# /temp/progress.txt format
PHASE:ITERATION:STATUS:TIMESTAMP
PLANNING:1:INITIAL_PLAN_COMPLETE:2024-01-09_10:00
CODING:2:READY_FOR_TESTER:2024-01-09_11:30
TESTING:1:READY_FOR_EVALUATOR:2024-01-09_12:00
```

### Analytics Dashboard
**METRICS COLLECTION**:
- **Phase Duration**: Time spent in each workflow phase
- **Marker Frequency**: How often phases complete successfully
- **Error Patterns**: Common failure points and remediation
- **Quality Trends**: Confidence scores and issue counts over time

### Alert System
**PROGRESS MONITORING**:
- **Stagnation Alerts**: No progress markers for extended periods
- **Error Spikes**: Increased failure markers in specific phases
- **Quality Degradation**: Declining confidence scores
- **Timeline Deviations**: Phases taking longer than expected

## MARKER MAINTENANCE PROTOCOLS

### Version Control
**MARKER EVOLUTION**:
- [ ] New markers added with clear documentation
- [ ] Deprecated markers phased out with migration path
- [ ] Marker format changes backward compatible
- [ ] Version history maintained for audit trails

### Quality Assurance
**VALIDATION PROCESSES**:
- [ ] All markers tested in integration scenarios
- [ ] Marker parsing validated across different contexts
- [ ] Human readability confirmed for all markers
- [ ] Automation compatibility verified

### Training Updates
**TEAM EDUCATION**:
- [ ] New team members trained on marker system
- [ ] Marker updates communicated to entire team
- [ ] Documentation updated with new markers
- [ ] Examples provided for proper marker usage

## EXCEPTION HANDLING

### Marker Conflicts
**RESOLUTION PROTOCOLS**:
- **Duplicate Markers**: Most recent marker takes precedence
- **Conflicting Status**: Human arbitration required
- **Invalid Format**: Automatic correction with warning
- **Missing Context**: Marker rejected with explanation required

### Emergency Overrides
**CRISIS MANAGEMENT**:
- **Marker Bypass**: Documented justification required
- **Accelerated Workflow**: Emergency markers for urgent situations
- **Post-Crisis Review**: Override usage analyzed for process improvement
- **Prevention Updates**: New safeguards implemented based on incidents

## PERFORMANCE IMPACT ASSESSMENT

### Processing Overhead
**EFFICIENCY METRICS**:
- [ ] Marker validation adds minimal latency
- [ ] Progress tracking doesn't impact workflow speed
- [ ] Analytics processing remains lightweight
- [ ] Storage requirements stay within bounds

### Scalability Considerations
**GROWTH ACCOMMODATION**:
- [ ] Marker system supports multiple concurrent workflows
- [ ] Progress tracking scales with team size
- [ ] Analytics handle increased marker volume
- [ ] System remains responsive under load

## COMPLIANCE AND AUDIT

### Regulatory Requirements
**DOCUMENTATION STANDARDS**:
- [ ] All markers logged for audit trails
- [ ] Marker timestamps immutable and verifiable
- [ ] Progress records retained for required periods
- [ ] Access controls on marker modification

### Quality Assurance
**VALIDATION FRAMEWORK**:
- [ ] Regular audits of marker usage patterns
- [ ] Automated checks for marker consistency
- [ ] Manual reviews of critical workflow markers
- [ ] Continuous improvement based on marker analytics
