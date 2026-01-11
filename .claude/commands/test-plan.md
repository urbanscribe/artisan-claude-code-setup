description: Test the current implementation plan for completeness and adherence to standards. argument-hint: [optional-plan-name]
---------------------------------------------------------------------------------------------------------------

Test Plan Validation: $1
========================

Please thoroughly validate the implementation plan for completeness and adherence to project standards.

## Validation Checklist

### Plan Structure
- [ ] Contains all required sections (Objective, Success Criteria, Research Findings, etc.)
- [ ] Includes specific file paths and method names
- [ ] Has clear acceptance criteria for each phase

### Architectural Compliance
- [ ] Follows domain-driven design principles
- [ ] Preserves async patterns and unified session management
- [ ] Includes strategic logging at key points only
- [ ] Uses proper dependency management

### TDD Requirements
- [ ] Specifies tests in /tests/ subfolders (not root)
- [ ] Includes POC scripts in /tests/poc_scripts/ for API verification
- [ ] Requires real data testing (no mocks)
- [ ] Includes UI/browser testing instructions

### Database Safety
- [ ] No database resets/drops/duplicates mentioned
- [ ] Uses get_db_session_context() for all operations
- [ ] Preserves data integrity in testing

### Human Control Points
- [ ] All architectural decisions resolved (nothing for team to choose)
- [ ] Clear approval checkpoints identified
- [ ] Work specified in MAIN branch only

## Report Format

### Issues Found
- [Critical/High/Medium/Low]: [Description] - [Required Action]

### Recommendations
[APPROVE / REQUEST REVISIONS] - [Justification]

If revisions needed, provide specific guidance on what to change.
