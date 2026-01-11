# TDD Enforcer Rule (Main Rule - Tier 2)
## Purpose
Enforces Test-Driven Development as an absolute gatekeeper throughout the entire workflow.

## MANDATORY TDD GATES

### Gate A: Planning Phase
**REQUIREMENT**: Before any code planning, TDD structure must be established.
- Identify all test scenarios from user requirements
- Create failing test placeholders in `/tests/` subfolders
- Ensure test coverage plan covers all user stories
- **BLOCK**: No planning advancement without test structure

### Gate B: Architecture Phase
**REQUIREMENT**: Architecture must enable testable design.
- Validate dependency injection for testability
- Ensure interfaces/contracts are defined for mocking
- Confirm database operations use `get_db_session_context()`
- **BLOCK**: No architectural decisions without testability validation

### Gate C: Implementation Phase
**REQUIREMENT**: Code implementation follows strict TDD cycle.
- **RED**: Write failing test first (test must fail initially)
- **GREEN**: Implement minimal code to pass test
- **REFACTOR**: Clean code while maintaining test coverage
- **BLOCK**: No code commits without passing tests

### Gate D: Integration Phase
**REQUIREMENT**: All components tested together.
- Integration tests validate component interactions
- End-to-end tests verify complete workflows
- Performance tests ensure non-regression
- **BLOCK**: No integration without comprehensive test coverage

### Gate E: Deployment Phase
**REQUIREMENT**: Production deployment requires test validation.
- All tests pass in production-like environment
- Regression tests prevent deployment of breaking changes
- Monitoring tests validate production health
- **BLOCK**: No deployment without test sign-off

## TDD INFRASTRUCTURE REQUIREMENTS

### Test Organization
- **Directory Structure**: `/tests/` with subfolders per component
- **Naming Convention**: `test_*.py` for unit tests, `integration_*.py` for integration
- **Fixture Management**: Shared test fixtures for common setup
- **Mock Strategy**: External dependencies mocked, internal logic tested directly

### Test Quality Standards
- **Coverage Minimum**: 90% code coverage required
- **Test Isolation**: Each test independent and repeatable
- **Real Data Testing**: No mocks for business logic validation
- **Performance Benchmarks**: Tests include performance assertions

## FORBIDDEN PATTERNS (AUTOMATIC BLOCK)

### ❌ "Tests Later"
- **BLOCK**: Any plan suggesting implementation before tests
- **REASON**: Violates TDD fundamental principle
- **REMEDIATION**: Replan with test-first approach

### ❌ "Mock Everything"
- **BLOCK**: Over-reliance on mocks for business logic
- **REASON**: Masks integration issues and real-world problems
- **REMEDIATION**: Use real data and selective mocking only for external dependencies

### ❌ "Manual Testing Only"
- **BLOCK**: Plans without automated test coverage
- **REASON**: Unreliable, unscalable, prone to human error
- **REMEDIATION**: Implement comprehensive automated test suite

### ❌ "Skip Tests for Speed"
- **BLOCK**: Any suggestion to bypass tests for velocity
- **REASON**: Technical debt accumulation, quality degradation
- **REMEDIATION**: Enforce TDD discipline regardless of timeline pressure

## ENFORCEMENT MECHANISMS

### Automated Validation
- **Hook Integration**: validation_post_tool.py checks for test execution
- **Command Blocking**: /implement blocks advancement without test completion
- **Coverage Reporting**: Automatic coverage analysis and reporting

### Human Oversight Gates
- **Test Review**: Human validation of test quality and coverage
- **Coverage Approval**: Explicit sign-off on coverage metrics
- **Exception Approval**: Human override requires documented justification

## SUCCESS CRITERIA

### Process Compliance
- **100% Gate Adherence**: All TDD gates enforced without exception
- **Zero Test Debt**: No accumulation of untested code
- **Quality Maintenance**: Test suite grows with codebase

### Quality Outcomes
- **Defect Prevention**: Issues caught during development, not production
- **Regression Protection**: Test suite prevents functionality breakage
- **Confidence Building**: Comprehensive tests enable fearless refactoring

## INTEGRATION
- **Activated**: Automatically by /implement command at all phases
- **Referenced**: In planner, coder, tester skill instructions
- **Reported**: Test status included in all phase completion markers
