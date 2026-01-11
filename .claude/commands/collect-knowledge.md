description: Collect and integrate existing project knowledge from documentation/main/ folder. argument-hint: [integration-description]
-------------------------------------------------------------------------------------------------------------------------

Knowledge Collection & Integration: $1
====================================

Collect and integrate existing project knowledge to make it available to the AI development team.

## Knowledge Collection Process

### 1. Documentation Discovery
**Read all architectural documentation:**
- `documentation/main/proposedarchitecture.md` - Core architectural decisions
- `documentation/main/*.md` - All architectural and domain documentation
- Any existing API docs, data models, or business rules

### 2. Codebase Analysis
**Analyze existing code patterns:**
- Project structure and organization
- Coding conventions and patterns
- Technology stack usage
- Database schemas and relationships (if accessible)

### 3. Integration Synthesis
**Create comprehensive knowledge summary:**
- Architectural principles and constraints
- Technology choices and justifications
- Coding standards and patterns
- Business rules and domain logic
- Integration points and dependencies

### 4. Knowledge Persistence
**Make knowledge available to all team members:**
- Update CLAUDE.md with project-specific context (if needed)
- Ensure all AI skills can reference this knowledge
- Validate knowledge integration through test queries

## When This Knowledge is Used

### Planning Phase
- Reference existing architecture for new features
- Ensure consistency with established patterns
- Identify integration points for new functionality

### Implementation Phase
- Follow established coding conventions
- Use approved technology stack components
- Maintain architectural boundaries

### Testing Phase
- Apply existing testing patterns and strategies
- Verify compliance with architectural constraints
- Ensure new features integrate properly

### Evaluation Phase
- Validate against architectural standards
- Check consistency with established patterns
- Ensure no architectural drift introduced

## Output Format

COLLECT_KNOWLEDGE_COMPLETE
Knowledge_Sources_Read: [count]
Architectural_Patterns_Identified: [count]
Integration_Complete: [yes/no]
Team_Readiness: [ready/not_ready]

## Why This Matters

Prevents architectural inconsistencies and ensures the AI team understands your project's unique context, patterns, and constraints before beginning development work.

Use this command when adding Claude Code setup to existing projects or when significant architectural changes have been made that the team needs to understand.
