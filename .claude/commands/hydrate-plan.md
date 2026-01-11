# HYDRATE-PLAN: Automatic Global Context Integration
**Purpose**: Automatically pull relevant global context into sprint plans to prevent architectural drift and ensure consistency.

## COMMAND EXECUTION PROTOCOL

### Trigger Conditions
**Automatic Activation**:
- Executed automatically during `/implement` workflow at planning phase
- Can be invoked manually: `/hydrate-plan`
- Integrated into Planner workflow as first validation step

### Global Context Sources
**Documentation Ingestion**:
1. **CLAUDE.md**: Core invariants and operational procedures
2. **documentation/main/architecture.md**: Technology choices and patterns
3. **documentation/main/keygoals.md**: Project objectives and constraints
4. **Active Rules**: Currently loaded rule set from .claude/rules/

### Context Hash Generation
**Integrity Verification**:
```bash
# Generate SHA256 hash of global context files
GLOBAL_HASH=$(find documentation/main/ CLAUDE.md .claude/rules/ -type f -exec sha256sum {} \; | sort | sha256sum | cut -d' ' -f1)

# Store in SPRINT_STATE.json global_context.current_hash
echo "$GLOBAL_HASH" > /tmp/current_global_hash.txt
```

### Hydration Content Mapping
**Automatic Content Extraction**:
- **Tech Stack**: Extract from architecture.md "Technology Choices" section
- **Database Patterns**: Pull from CLAUDE.md database operation rules
- **Security Requirements**: Extract enterprise hardening constraints
- **Quality Standards**: Gather TDD gates, async patterns, and assessment rules

### Plan Integration
**Structured Insertion**:
1. **Locate Hydration Section**: Find "## Sprint Context Hydration" in plan
2. **Update Global Context References**: Populate with extracted content
3. **Generate Hash**: Insert current GLOBAL_HASH into validation section
4. **Set Validation Status**: Mark as "VERIFIED" with current timestamp

## VALIDATION LOGIC

### Hash Verification Protocol
**Stale Context Detection**:
1. **Compare Hashes**: Match plan's stored hash vs current GLOBAL_HASH
2. **Status Determination**:
   - **VERIFIED**: Hashes match, proceed with execution
   - **CONFLICT_DETECTED**: Hashes differ, require human approval
3. **Human Gate**: If CONFLICT_DETECTED, display differences and require approval

### Conflict Resolution
**Human Approval Protocol**:
```
⚠️  GLOBAL CONTEXT CONFLICT DETECTED
The plan was created with different global context.

Changes detected:
- Architecture: Updated technology choices
- Security: New enterprise hardening rules
- Quality: Additional assessment requirements

OPTIONS:
1. APPROVE_UPDATED_CONTEXT - Use current global context
2. KEEP_ORIGINAL_PLAN - Continue with original context
3. ABORT_SPRINT - Cancel and recreate plan

Type your choice:
```

## DATA INTEGRITY RUBRIC INTEGRATION

### Automatic Rubric Population
**Nonsense Prevention Setup**:
1. **Chart/Data Validation**: "Must check for N/A, NaN, null, undefined values in all data displays"
2. **Business Logic Checks**: "Flag impossible values (negative stock prices, 0.00% volatility, invalid percentages)"
3. **UI State Verification**: "Confirm meaningful data display, not placeholder content or empty charts"
4. **Sanity Checker Requirements**: "Visual proof required before Victory Declaration - no empty charts, red console errors, or nonsensical data"

### Victory Declaration Gate
**Enforced Validation**:
- **Sanity Checker Integration**: Automatically invoke @sanity-checker for UI features
- **Data Integrity Verification**: Block READY_FOR_EVALUATOR without rubric compliance
- **Visual Evidence Required**: Screenshot validation for chart/data displays

## INTEGRATION WITH PLANNING WORKFLOW

### Automatic Execution Sequence
**Planning Phase Integration**:
1. **Pre-Planning**: Generate current GLOBAL_HASH
2. **Plan Creation**: Inject hydration section with current context
3. **Validation Gate**: Compare hashes and enforce approval for conflicts
4. **Rubric Setup**: Populate data integrity requirements
5. **Proceed to Implementation**: Only after hydration VERIFIED

### Manual Command Usage
**Direct Invocation**:
```
/hydrate-plan
```
**Result**: Updates current plan with latest global context and validation status

## SUCCESS VALIDATION

### Hydration Completeness
**Content Verification**:
- ✅ Global Context References populated with actual content
- ✅ Active Constraints extracted from current rules
- ✅ Data Integrity Rubric fully specified
- ✅ Hash validation functional

### Conflict Detection
**Accuracy Metrics**:
- ✅ Detects all global context changes
- ✅ Provides clear conflict summary
- ✅ Enforces human approval for changes
- ✅ Maintains execution integrity

### Integration Quality
**Workflow Harmony**:
- ✅ Seamless integration with /implement
- ✅ Non-disruptive to existing workflows
- ✅ Clear feedback for conflict resolution
- ✅ Preserves plan structure and readability
