# VALIDATE-ARCHITECTURE: Plan Compliance Verification
**Purpose**: Check sprint plan compliance with global architectural rules and constraints to prevent violations.

## COMMAND EXECUTION PROTOCOL

### Trigger Conditions
**Automatic Activation**:
- Executed during `/implement` workflow after plan creation
- Can be invoked manually: `/validate-architecture`
- Integrated into Planner validation sequence

### Rule Source Loading
**Global Architecture Ingestion**:
1. **CLAUDE.md**: Load core invariants and physics-level rules
2. **.claude/rules/**: Load all active task-specific and detail rules
3. **documentation/main/architecture.md**: Load established patterns and technology choices
4. **SPRINT_STATE.json**: Load current sprint boundaries and constraints

### Compliance Validation Framework
**Multi-Layer Verification**:
- **Physics-Level Rules**: CLAUDE.md invariants (no DB resets, no git writes, no rm)
- **Architectural Patterns**: Established technology choices and design patterns
- **Quality Standards**: TDD requirements, async patterns, security constraints
- **Sprint Boundaries**: Worktree sovereignty and repair scope limitations

## VALIDATION CATEGORIES

### Technology Stack Compliance
**Architecture Alignment**:
- **Approved Technologies**: Verify plan uses only documented tech stack
- **Integration Patterns**: Confirm adherence to established integration approaches
- **Version Compatibility**: Check compatibility with existing system versions
- **Migration Strategy**: Validate transition approach for new technologies

### Security Constraint Verification
**Enterprise Hardening**:
- **RM Ban Compliance**: No dangerous file operations in plan
- **Worktree Sovereignty**: Operations limited to current git worktree
- **Repair Scope**: Only BOSS-controlled path modifications
- **Authentication Patterns**: Follow established security protocols

### Quality Standard Enforcement
**Development Excellence**:
- **TDD Gates**: Test-first development requirements met
- **Async Patterns**: Proper concurrency implementation
- **Type Safety**: Type hints and validation requirements
- **Code Quality**: Self-assessment and quality metrics integration

### Database Operation Validation
**Data Integrity Protection**:
- **Session Context Usage**: All DB operations use get_db_session_context()
- **No Destructive Operations**: No resets, drops, or duplicates
- **Transaction Safety**: Proper transaction boundaries and error handling
- **Migration Safety**: Safe schema evolution patterns

## VIOLATION DETECTION ENGINE

### Pattern-Based Scanning
**Automated Rule Checking**:
```python
# validation_engine/pattern_scanner.py
VIOLATION_PATTERNS = {
    'physics_violations': [
        r'\brm\s+-rf\b',  # Dangerous file operations
        r'\bgit\s+(commit|push|merge)\b',  # Git write operations
        r'\bDROP\s+DATABASE\b|\bTRUNCATE\b',  # DB destructive operations
    ],
    'architecture_violations': [
        r'\bDjango\b|\bRails\b',  # Non-approved frameworks
        r'\bSQLite\b',  # Non-enterprise database
        r'\bvanilla\s+JS\b',  # Non-TypeScript frontend
    ],
    'quality_violations': [
        r'\bTODO\b|\bFIXME\b',  # Unresolved development markers
        r'def\s+\w+\([^)]*\):\s*$',  # Missing type hints (Python)
        r'\bany\b|\bunknown\b',  # TypeScript any types
    ]
}

def scan_plan_violations(plan_content: str) -> Dict[str, List[str]]:
    """Scan plan for architectural violations."""
    violations = {}
    for category, patterns in VIOLATION_PATTERNS.items():
        category_violations = []
        for pattern in patterns:
            matches = re.findall(pattern, plan_content, re.IGNORECASE)
            if matches:
                category_violations.extend(matches)
        if category_violations:
            violations[category] = list(set(category_violations))
    return violations
```

### Severity Classification
**Violation Impact Assessment**:
- **Critical**: Physics-level violations (DB resets, rm operations)
- **High**: Architecture deviations (non-approved technologies)
- **Medium**: Quality standard violations (missing type hints)
- **Low**: Best practice deviations (naming inconsistencies)

## COMPLIANCE REPORTING

### Validation Output Format
**Structured Results**:
```
ARCHITECTURE VALIDATION REPORT
================================

SPRINT: [sprint_id]
PLAN: [plan_path]
VALIDATION STATUS: [PASS/FAIL/BLOCKED]

CRITICAL VIOLATIONS (0):
- None detected

HIGH VIOLATIONS (0):
- None detected

MEDIUM VIOLATIONS (2):
- Missing type hints in API endpoints
- Async pattern not specified for concurrent operations

LOW VIOLATIONS (1):
- Variable naming inconsistent with patterns

RECOMMENDATIONS:
1. Add type hints to all function parameters
2. Specify async/await patterns for I/O operations
3. Review variable naming against established conventions

APPROVAL REQUIRED: [YES/NO]
```

### Human Approval Protocol
**Violation Resolution**:
- **Auto-Pass**: No violations detected, proceed automatically
- **Human Review**: Violations found, display report and require approval
- **Blocked Execution**: Critical violations prevent execution until resolved

## INTEGRATION WITH PLANNING WORKFLOW

### Automatic Validation Sequence
**Planning Phase Integration**:
1. **Plan Creation**: Generate initial plan structure
2. **Hydration**: Pull global context and constraints
3. **Validation**: Run architecture compliance check
4. **Approval Gate**: Human review for violations
5. **Proceed/Fix**: Continue or return to planning

### Manual Validation Usage
**Direct Command Execution**:
```
/validate-architecture
```
**Result**: Comprehensive compliance report for current sprint plan

## REMEDIATION GUIDANCE

### Automatic Fix Suggestions
**Violation Resolution**:
- **Missing Type Hints**: Generate type annotation templates
- **Async Pattern Missing**: Provide async/await code examples
- **Technology Violations**: Suggest approved alternatives
- **Security Issues**: Provide secure implementation patterns

### Plan Update Protocol
**Compliance Enforcement**:
1. **Violation Detection**: Identify specific rule violations
2. **Impact Assessment**: Determine severity and blocking status
3. **Fix Generation**: Provide specific remediation instructions
4. **Re-validation**: Allow plan updates and re-checking

## SUCCESS VALIDATION

### Detection Accuracy
**Validation Quality**:
- ✅ Identifies all physics-level violations
- ✅ Catches architectural deviations
- ✅ Enforces quality standards
- ✅ Provides actionable remediation

### Integration Smoothness
**Workflow Compatibility**:
- ✅ Non-disruptive to planning process
- ✅ Clear violation reporting
- ✅ Flexible approval mechanisms
- ✅ Supports iterative plan improvement

### False Positive Management
**Accuracy Optimization**:
- ✅ Context-aware pattern matching
- ✅ Configurable rule sensitivity
- ✅ Human override capabilities
- ✅ Continuous rule refinement
