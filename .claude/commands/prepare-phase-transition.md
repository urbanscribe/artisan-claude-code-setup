# PREPARE-PHASE-TRANSITION: Generate Execution Manifesto and Enforce Context Pruning
**Purpose**: Create phase transition manifesto and enforce mandatory /clear to prevent context drift and ensure clean phase execution.

## COMMAND EXECUTION PROTOCOL

### Trigger Conditions
**Automatic Activation**:
- Executed automatically during `/implement` workflow at phase transitions
- Can be invoked manually: `/prepare-phase-transition`
- Integrated into sprint startup protocol

### Phase Transition Detection
**Context Change Identification**:
1. **Current Phase Analysis**: Determine active sprint phase (planning, implementation, testing, evaluation)
2. **Transition Requirements**: Identify needed context changes for next phase
3. **Manifesto Scope**: Define what execution focus requires for clean transition
4. **Clear Enforcement**: Establish /clear requirement boundaries

## EXECUTION MANIFESTO GENERATION

### Manifesto Content Structure
**1-Page Execution Summary**:
```
PHASE TRANSITION MANIFESTO
==========================

SPRINT: 2026-01-09_plan_004_user_auth
FROM: planning → implementation
GENERATED: 2026-01-09T14:30:00Z

EXECUTION FOCUS:
🎯 Primary Objective: Implement JWT-based user authentication system
🎯 Success Criteria: All auth endpoints functional, tests passing
🎯 Quality Gates: TDD compliance, security validation, performance benchmarks

CONTEXT BOUNDARIES:
🔒 Locked Files: src/auth/, tests/auth/, documentation/api/
🔒 Prohibited Operations: No database schema changes, no external API integration
🔒 Global Constraints: Use get_db_session_context(), async patterns required

EXECUTION GUIDELINES:
📋 Implementation Steps: 8 specific tasks with acceptance criteria
📋 Testing Strategy: Unit tests first, integration tests second
📋 Code Standards: TypeScript strict mode, error handling required
📋 Performance Targets: <100ms auth latency, <50MB memory usage

RISK MITIGATION:
⚠️ Watch For: Session management complexity, token security validation
⚠️ Early Indicators: Failing authentication tests, performance degradation
⚠️ Escalation Triggers: Security vulnerabilities, >200ms response times

CONTEXT PRUNING REQUIRED:
🧹 /clear Mandatory: Execute /clear before proceeding to maintain phase focus
🧹 Context Bloom Prevention: Previous planning chatter removed from execution context
🧹 Manifesto-Driven Execution: Operate only within manifesto boundaries
```

### Manifesto Generation Logic
**Context-Aware Content Creation**:
```python
# manifesto_generator.py
def generate_execution_manifesto(sprint_state, from_phase, to_phase):
    """Generate focused execution manifesto for phase transition."""

    manifesto = {
        'sprint_id': sprint_state['active_sprint']['id'],
        'transition': f'{from_phase} → {to_phase}',
        'timestamp': datetime.now().isoformat(),
        'execution_focus': extract_execution_focus(sprint_state, to_phase),
        'context_boundaries': establish_context_boundaries(sprint_state),
        'execution_guidelines': define_execution_guidelines(to_phase),
        'risk_mitigation': identify_risk_factors(sprint_state, to_phase),
        'context_pruning': {
            'clear_required': True,
            'bloom_prevention': True,
            'manifesto_driven': True,
            'reasoning': 'Prevents context drift and ensures phase sovereignty'
        }
    }

    return manifesto
```

### Phase-Specific Content Adaptation
**Context-Aware Manifesto**:
- **Planning → Implementation**: Focus on coding standards, testing requirements, performance targets
- **Implementation → Testing**: Emphasize test coverage, validation criteria, quality gates
- **Testing → Evaluation**: Highlight success metrics, documentation requirements, handoff preparation
- **Evaluation → Complete**: Summarize achievements, identify patterns, prepare architectural updates

## CONTEXT PRUNING ENFORCEMENT

### Mandatory /clear Protocol
**Session Reset Requirements**:
1. **Manifesto Presentation**: Display complete execution manifesto
2. **Clear Command Requirement**: Explicitly require user to execute /clear
3. **Context Validation**: Verify clean session state before proceeding
4. **Phase Sovereignty**: Ensure no cross-phase context contamination

### Context Bloom Prevention
**Session Hygiene Enforcement**:
```python
# context_pruning.py
def enforce_context_pruning(manifesto):
    """Ensure clean context transition between phases."""

    # Validate manifesto acceptance
    if not manifesto.get('accepted', False):
        return False, "Manifesto must be accepted before proceeding"

    # Check for context bloom indicators
    bloom_indicators = [
        'previous phase planning',
        'draft implementation notes',
        'exploratory testing results',
        'evaluation criteria from different phase'
    ]

    # Require explicit /clear execution
    clear_executed = check_clear_execution_status()
    if not clear_executed:
        return False, "Mandatory /clear required before phase transition"

    # Verify phase sovereignty
    sovereignty_maintained = validate_phase_sovereignty(manifesto)
    if not sovereignty_maintained:
        return False, "Phase sovereignty violation detected"

    return True, "Context pruning successfully enforced"
```

### Phase Transition Gates
**Execution Control Points**:
1. **Pre-Transition Validation**: Manifesto generation and acceptance
2. **Clear Enforcement**: Mandatory session reset requirement
3. **Context Verification**: Bloom prevention validation
4. **Phase Activation**: Clean execution context establishment

## INTEGRATION WITH WORKFLOW

### Automatic Execution Sequence
**Sprint Startup Protocol**:
1. **Sprint Activation**: Load active sprint context
2. **Phase Assessment**: Determine current execution phase
3. **Manifesto Generation**: Create execution focus document
4. **Human Approval**: Require manifesto acceptance
5. **Clear Enforcement**: Mandate session reset
6. **Phase Execution**: Proceed with clean context

### Manual Transition Support
**Direct Command Usage**:
```
/prepare-phase-transition
```
**Result**: Generates manifesto for current phase transition and enforces context pruning requirements

## MANIFESTO LIFECYCLE MANAGEMENT

### Manifesto Persistence
**Execution Context Preservation**:
- **Temp Storage**: Save manifesto in sprint temp directory
- **State Integration**: Reference in SPRINT_STATE.json
- **Progress Tracking**: Update as phase execution progresses
- **Completion Archival**: Preserve successful manifestos

### Manifesto Evolution
**Dynamic Updates**:
- **Progress Integration**: Update with completed tasks and achievements
- **Risk Adjustment**: Modify based on encountered challenges
- **Scope Changes**: Adapt to approved requirement modifications
- **Success Metrics**: Track against defined criteria

## SUCCESS VALIDATION

### Manifesto Quality
**Content Effectiveness**:
- ✅ Clear execution focus and success criteria defined
- ✅ Context boundaries and constraints properly established
- ✅ Risk mitigation strategies identified and actionable
- ✅ Phase-specific guidelines appropriate for execution context
- ✅ Execution summary fits 1-page constraint

### Context Pruning Effectiveness
**Session Hygiene**:
- ✅ Mandatory /clear enforced before phase transitions
- ✅ Context bloom prevented through manifesto boundaries
- ✅ Phase sovereignty maintained throughout execution
- ✅ Cross-phase contamination eliminated
- ✅ Clean execution context established and preserved

### Transition Smoothness
**Workflow Continuity**:
- ✅ Automatic manifesto generation at appropriate transition points
- ✅ Human approval integrated without disrupting flow
- ✅ Clear enforcement non-intrusive but mandatory
- ✅ Phase activation occurs only after proper preparation
- ✅ Context verification prevents execution with stale focus

### Execution Focus
**Phase Sovereignty**:
- ✅ Manifesto-driven execution prevents scope creep
- ✅ Context boundaries respected throughout phase
- ✅ Risk mitigation actively monitored and addressed
- ✅ Success criteria drive execution decisions
- ✅ Phase completion properly validated against manifesto
