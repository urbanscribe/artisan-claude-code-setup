# UPDATE-ARCHITECTURE: Automatic Architectural Documentation Evolution
**Purpose**: Automatically update global architectural documentation based on sprint completion analysis and pattern recognition results.

## COMMAND EXECUTION PROTOCOL

### Trigger Conditions
**Automatic Activation**:
- Executed automatically by /close-sprint when architectural updates are approved
- Can be invoked manually: `/update-architecture [sprint_id]`
- Integrated into sprint completion workflow

### Documentation Source Analysis
**Global Documentation Ingestion**:
1. **documentation/main/architecture.md**: Current architectural patterns and decisions
2. **documentation/main/keygoals.md**: Project objectives and constraints
3. **SPRINT_STATE.json**: Completed sprint metadata and analysis results
4. **Sprint Artifacts**: Evaluator analysis results and pattern discoveries

## ARCHITECTURAL EVOLUTION ENGINE

### Update Qualification Assessment
**Trigger Condition Evaluation**:
```python
def should_trigger_architectural_update(sprint_completion_data):
    """Determine if sprint completion qualifies for architectural updates."""

    # Micro-change exclusion criteria
    micro_change_indicators = [
        'test_only', 'refactor_only', 'bugfix_only',
        'documentation_only', 'no_new_patterns'
    ]

    if any(indicator in sprint_completion_data.get('change_type', '')
           for indicator in micro_change_indicators):
        return False, "Micro-change - no architectural update needed"

    # Significant change indicators
    significant_indicators = [
        'new_pattern_established',
        'architectural_decision_made',
        'constraint_modified',
        'integration_pattern_changed',
        'quality_standard_improved'
    ]

    significant_changes = sum(1 for indicator in significant_indicators
                            if sprint_completion_data.get(indicator, False))

    if significant_changes >= 2:
        return True, f"Significant changes detected: {significant_changes} indicators"

    # Pattern recognition threshold
    patterns_identified = len(sprint_completion_data.get('patterns_identified', []))
    if patterns_identified >= 1:
        return True, f"New patterns identified: {patterns_identified}"

    return False, "No significant architectural changes detected"
```

### Documentation Update Generation
**Automated Content Creation**:

**Architecture.md Update Generation**:
```python
def generate_architecture_updates(sprint_analysis):
    """Generate proposed updates for architecture.md."""

    updates = []

    # Pattern documentation
    for pattern in sprint_analysis.get('patterns_identified', []):
        update = f"""
### {pattern['name']}
**Context**: Sprint {sprint_analysis['sprint_id']} - {sprint_analysis['description']}
**Pattern**: {pattern['description']}
**Components**: {', '.join(pattern.get('components', []))}
**Usage**: {pattern.get('usage', 'Apply to relevant future implementations')}
**Rationale**: {pattern.get('rationale', 'Based on sprint implementation experience')}
**Established**: {sprint_analysis['completion_date']}
"""
        updates.append({
            'type': 'new_pattern',
            'content': update,
            'section': 'Patterns Established'
        })

    # Integration pattern updates
    integration_patterns = sprint_analysis.get('integration_patterns', [])
    if integration_patterns:
        update = f"""
### Integration Pattern Updates
**Context**: Sprint {sprint_analysis['sprint_id']} integration improvements
**Updates**: {', '.join(integration_patterns)}
**Impact**: Enhanced system interoperability and data flow
"""
        updates.append({
            'type': 'integration_update',
            'content': update,
            'section': 'Integration Patterns'
        })

    return updates
```

**Keygoals.md Update Generation**:
```python
def generate_keygoals_updates(sprint_analysis):
    """Generate proposed updates for keygoals.md."""

    updates = []

    # New objectives from sprint learnings
    lessons_learned = sprint_analysis.get('lessons_learned', [])
    for lesson in lessons_learned:
        if 'new_objective' in lesson.get('type', ''):
            update = f"""
### {lesson['objective_title']}
**Context**: Sprint {sprint_analysis['sprint_id']} revealed {lesson['gap_identified']}
**Objective**: {lesson['objective_description']}
**Success Criteria**: {lesson['success_measures']}
**Timeline**: {lesson['recommended_timeline']}
**Priority**: {lesson.get('priority', 'medium')}
**Established**: {sprint_analysis['completion_date']}
"""
            updates.append({
                'type': 'new_objective',
                'content': update,
                'category': lesson.get('category', 'technical')
            })

    # Updated constraints from sprint challenges
    constraint_updates = sprint_analysis.get('constraint_updates', [])
    if constraint_updates:
        update = f"""
### Updated Project Constraints
**Context**: Sprint {sprint_analysis['sprint_id']} implementation experience
**Constraint Updates**: {', '.join(constraint_updates)}
**Rationale**: Improved delivery quality and reduced technical debt
**Effective**: {sprint_analysis['completion_date']}
"""
        updates.append({
            'type': 'constraint_update',
            'content': update,
            'category': 'constraints'
        })

    return updates
```

## HUMAN APPROVAL AND INTEGRATION

### Update Preview and Approval
**Comprehensive Review Interface**:
```
ARCHITECTURAL DOCUMENTATION UPDATES - REVIEW REQUIRED
======================================================

Sprint: 2026-01-09_plan_004_user_auth
Analysis: 3 patterns identified, 2 objectives recommended

📝 PROPOSED ARCHITECTURE.MD UPDATES:
=====================================

SECTION: New Patterns Established

### JWT Authentication Pattern
**Context**: Sprint 2026-01-09_plan_004_user_auth - Implement user authentication
**Pattern**: Stateless authentication with middleware integration
**Components**: UserAuthenticator, AuthMiddleware, TokenManager
**Usage**: Apply to all future authentication requirements
**Rationale**: Improved scalability and simplified session management
**Established**: 2026-01-09T16:45:00Z

SECTION: Integration Patterns

### API Middleware Integration
**Context**: Sprint authentication middleware implementation
**Updates**: Request validation, token refresh strategies
**Impact**: Enhanced API security and user experience

🎯 PROPOSED KEYGOALS.MD UPDATES:
=================================

SECTION: Security Infrastructure

### Enterprise Authentication System
**Context**: Sprint revealed need for comprehensive auth solution
**Objective**: Implement enterprise-grade authentication across all services
**Success Criteria**: 99.9% uptime, <5s response time, full audit logging
**Timeline**: Q2 2026 (3 months)
**Priority**: high
**Established**: 2026-01-09T16:45:00Z

APPROVAL OPTIONS:
1. APPROVE_ALL - Implement all proposed updates
2. APPROVE_BY_SECTION - Review and approve each section individually
3. MODIFY_AND_APPROVE - Suggest modifications before approval
4. REJECT_ALL - Cancel documentation updates

Choose approval approach (1-4):
```

### Automatic Documentation Integration
**Version-Controlled Updates**:
1. **Backup Creation**: Preserve original documentation versions
2. **Update Application**: Insert approved changes with proper formatting
3. **Version Tracking**: Add timestamps and sprint references
4. **Cross-linking**: Establish relationships between related updates
5. **Validation**: Verify documentation integrity after updates

## UPDATE LIFECYCLE MANAGEMENT

### Update Persistence and Tracking
**Comprehensive Audit Trail**:
```json
{
  "architectural_updates": [
    {
      "sprint_id": "2026-01-09_plan_004_user_auth",
      "update_type": "new_pattern",
      "document": "architecture.md",
      "section": "Authentication Patterns",
      "content_hash": "abc123...",
      "applied_date": "2026-01-09T16:50:00Z",
      "approved_by": "human_review",
      "rollback_available": true
    }
  ],
  "update_impact_assessment": {
    "patterns_added": 1,
    "objectives_modified": 1,
    "constraints_updated": 0,
    "future_sprints_affected": 3
  }
}
```

### Rollback and Version Control
**Safe Update Management**:
- **Automatic Backups**: Pre-update snapshots of all modified documents
- **Rollback Capability**: One-click reversion for any update set
- **Version History**: Complete chronological record of architectural evolution
- **Conflict Detection**: Prevent concurrent conflicting updates

## SUCCESS VALIDATION

### Update Accuracy
**Content Quality Verification**:
- ✅ Pattern descriptions accurately reflect implementation approaches
- ✅ Usage guidelines provide clear application criteria
- ✅ Rationale explanations justify architectural decisions
- ✅ Cross-references establish proper relationships
- ✅ Version tracking maintains complete audit trail

### Integration Completeness
**Documentation Consistency**:
- ✅ Updates properly integrated into existing document structure
- ✅ Formatting consistent with established documentation standards
- ✅ Links and references correctly established between documents
- ✅ Searchability and discoverability maintained
- ✅ Future sprint guidance clearly articulated

### Human Oversight Effectiveness
**Approval Process Quality**:
- ✅ Comprehensive preview allows thorough review
- ✅ Granular approval options support selective acceptance
- ✅ Modification capabilities enable improvement suggestions
- ✅ Clear audit trail documents all decision rationales
- ✅ Rollback capability provides safety net for errors

### Architectural Evolution Impact
**Knowledge Preservation Success**:
- ✅ Sprint learnings permanently captured in global documentation
- ✅ Future sprints benefit from established patterns and constraints
- ✅ Technical debt accumulation prevented through proactive updates
- ✅ Team knowledge base continuously enriched
- ✅ Architectural drift eliminated through systematic evolution
