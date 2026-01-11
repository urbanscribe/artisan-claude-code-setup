# EXTRACT-CONSTRAINTS: Sprint-Specific Architectural Element Extraction
**Purpose**: Pull sprint-relevant architectural elements and constraints to ensure focused, bounded execution.

## COMMAND EXECUTION PROTOCOL

### Trigger Conditions
**Automatic Activation**:
- Executed during `/implement` workflow as part of hydration process
- Can be invoked manually: `/extract-constraints`
- Integrated into Planner constraint gathering phase

### Constraint Source Analysis
**Architectural Element Mining**:
1. **CLAUDE.md**: Extract physics-level rules and operational constraints
2. **documentation/main/architecture.md**: Pull relevant technology patterns
3. **documentation/main/keygoals.md**: Extract project objectives and boundaries
4. **.claude/rules/sub/**: Load sprint-relevant detail rules

### Sprint Context Analysis
**Relevance Filtering**:
1. **Feature Type Detection**: Analyze sprint description for technology domains
2. **Integration Points**: Identify required external system interactions
3. **Performance Requirements**: Extract relevant performance constraints
4. **Security Boundaries**: Pull applicable security and access rules

## CONSTRAINT EXTRACTION ENGINE

### Rule Relevance Scoring
**Context-Based Filtering**:
```python
# constraint_engine/relevance_scorer.py
def calculate_rule_relevance(rule_content: str, sprint_context: str) -> float:
    """Calculate how relevant a rule is to the current sprint."""

    # Keyword matching for sprint type detection
    sprint_keywords = extract_keywords(sprint_context.lower())
    rule_keywords = extract_keywords(rule_content.lower())

    # Technology domain matching
    tech_domains = {
        'database': ['sql', 'postgres', 'orm', 'migration', 'transaction'],
        'frontend': ['react', 'ui', 'component', 'typescript', 'css'],
        'backend': ['api', 'endpoint', 'server', 'authentication', 'routing'],
        'security': ['auth', 'permission', 'encryption', 'validation', 'access'],
        'testing': ['test', 'tdd', 'coverage', 'assertion', 'mock']
    }

    domain_scores = {}
    for domain, keywords in tech_domains.items():
        sprint_matches = len(set(sprint_keywords) & set(keywords))
        rule_matches = len(set(rule_keywords) & set(keywords))
        domain_scores[domain] = min(sprint_matches * rule_matches, 10)

    # Overall relevance score
    max_domain_score = max(domain_scores.values()) if domain_scores else 0
    keyword_overlap = len(set(sprint_keywords) & set(rule_keywords))

    return min(max_domain_score + keyword_overlap, 10)
```

### Constraint Categorization
**Structured Organization**:
- **Technology Constraints**: Specific technology choices and versions
- **Quality Constraints**: Code quality and testing requirements
- **Security Constraints**: Authentication and access control rules
- **Performance Constraints**: Speed, scalability, and resource requirements
- **Integration Constraints**: External system interaction rules

## ACTIVE CONSTRAINTS INTEGRATION

### Plan Section Population
**Automatic Content Insertion**:
1. **Locate Constraints Section**: Find "## Active Constraints:" in plan
2. **Relevance Filtering**: Include only constraints with score > 3
3. **Priority Ordering**: Sort by relevance score descending
4. **Contextual Formatting**: Adapt constraint language to sprint context

### Constraint Examples
**Technology-Specific Constraints**:
```
DATABASE: Use get_db_session_context() for all database operations
FRONTEND: Implement with TypeScript and React patterns
SECURITY: Follow enterprise authentication protocols
TESTING: Maintain >80% test coverage with TDD approach
```

## SPRINT BOUNDARY ESTABLISHMENT

### File Scope Determination
**Automatic Lock Generation**:
1. **Sprint Analysis**: Parse sprint description for feature scope
2. **File Path Prediction**: Generate expected file locations based on patterns
3. **Directory Boundaries**: Establish worktree sovereignty limits
4. **Integration Points**: Identify required external file dependencies

### SPRINT_STATE.json Update
**Boundary Enforcement Setup**:
```json
{
  "active_sprint": {
    "locked_files": [
      "src/features/new-feature/",
      "tests/features/new-feature/",
      "documentation/plans/2026-01-09_plan_004_new_feature.md"
    ],
    "allowed_directories": [
      "src/features/",
      "tests/features/"
    ],
    "prohibited_patterns": [
      "src/legacy/",
      "database/migrations/"
    ]
  }
}
```

## CONSTRAINT VALIDATION INTEGRATION

### Pre-Execution Verification
**Boundary Compliance Check**:
1. **File Scope Validation**: Confirm all planned files within locked_files
2. **Dependency Verification**: Ensure required external files are accessible
3. **Pattern Compliance**: Check for prohibited file operation patterns
4. **Integration Safety**: Validate external system interaction permissions

### Execution Time Enforcement
**Safety Hook Integration**:
- **Path Validation**: safety_pre_tool.py checks against locked_files array
- **Pattern Blocking**: Prevent operations matching prohibited_patterns
- **Scope Enforcement**: Hard block operations outside sprint boundaries

## INTEGRATION WITH PLANNING WORKFLOW

### Constraint Gathering Sequence
**Planning Phase Integration**:
1. **Context Analysis**: Extract sprint description and objectives
2. **Rule Relevance Scoring**: Calculate applicability of all global rules
3. **Constraint Extraction**: Pull high-relevance rules and requirements
4. **Boundary Establishment**: Generate file scope and operation limits
5. **Plan Integration**: Insert constraints into hydration section

### Manual Constraint Review
**Direct Command Execution**:
```
/extract-constraints
```
**Result**: Displays all extracted constraints with relevance scores and boundary recommendations

## DYNAMIC CONSTRAINT EVOLUTION

### Sprint Learning Integration
**Adaptive Constraints**:
1. **Execution Monitoring**: Track constraint effectiveness during sprint
2. **Pattern Recognition**: Identify additional constraints needed
3. **Rule Refinement**: Suggest improvements to global rule set
4. **Boundary Adjustment**: Modify file scope based on execution patterns

### Architectural Learning
**Knowledge Transfer**:
1. **Constraint Effectiveness**: Measure which constraints prevented issues
2. **New Pattern Discovery**: Identify constraints needed for future sprints
3. **Global Rule Updates**: Propose additions to CLAUDE.md and rule system
4. **Documentation Updates**: Update architecture.md with learned patterns

## SUCCESS VALIDATION

### Extraction Accuracy
**Relevance Quality**:
- ✅ High-relevance constraints identified and prioritized
- ✅ Low-relevance constraints filtered out appropriately
- ✅ Context-aware constraint adaptation
- ✅ Sprint-specific boundary establishment

### Integration Effectiveness
**Workflow Compatibility**:
- ✅ Seamless integration with hydration process
- ✅ Non-disruptive to planning workflow
- ✅ Clear constraint presentation
- ✅ Flexible boundary enforcement

### Boundary Enforcement
**Execution Safety**:
- ✅ File scope restrictions properly enforced
- ✅ Prohibited operations blocked effectively
- ✅ Integration dependencies maintained
- ✅ Sprint sovereignty preserved

### Learning Capability
**Adaptive Improvement**:
- ✅ Constraint effectiveness tracking
- ✅ New pattern discovery and proposal
- ✅ Global rule refinement suggestions
- ✅ Architectural knowledge evolution
