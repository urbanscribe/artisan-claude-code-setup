# SWITCH-SPRINT: Change Active Sprint Context with State Validation
**Purpose**: Safely change active sprint context with comprehensive state validation and sovereignty enforcement.

## COMMAND EXECUTION PROTOCOL

### Command Syntax
**Basic Usage**:
```
/switch-sprint [sprint_id]
```

**Examples**:
```
/switch-sprint 2026-01-09_plan_004_user_auth
/switch-sprint 2026-01-08_plan_003_api_endpoints
```

### Sprint ID Validation
**Target Sprint Verification**:
1. **ID Format Check**: Validate YYYY-MM-DD_plan_NNN_feature format
2. **Existence Verification**: Confirm sprint exists in active_sprint or sprint_history
3. **Status Compatibility**: Allow switching to active or completed sprints only
4. **File Accessibility**: Verify plan file exists and is readable

### State Preservation Protocol
**Current Sprint Cleanup**:
1. **Active Sprint Check**: If switching away from active sprint, preserve current state
2. **Progress Checkpoint**: Save current phase, iteration, and locked_files
3. **Context Summary**: Generate transition summary for continuity
4. **State Update**: Mark current sprint as "paused" if switching temporarily

### Target Sprint Activation
**New Context Establishment**:
1. **State Restoration**: Load target sprint's complete state from SPRINT_STATE.json
2. **Context Validation**: Verify sprint's global context hash against current
3. **File Scope Restoration**: Re-establish locked_files boundaries
4. **Phase Continuity**: Resume from saved phase and iteration
5. **Artifact Directory**: Reactivate or recreate temp/claudecode/[sprint_id]/

### Global Context Reconciliation
**Hash Conflict Resolution**:
```python
# context_reconciliation.py
def reconcile_global_context(target_sprint_hash, current_global_hash):
    """Handle global context differences during sprint switching."""

    if target_sprint_hash == current_global_hash:
        return "VERIFIED", "Global context unchanged"

    # Calculate differences
    differences = detect_context_changes(target_sprint_hash, current_global_hash)

    if not differences:
        return "VERIFIED", "No functional differences detected"

    # Present options to user
    conflict_summary = format_conflict_summary(differences)

    return "CONFLICT_DETECTED", conflict_summary, [
        "APPROVE_CURRENT_CONTEXT - Use current global context",
        "KEEP_ORIGINAL_CONTEXT - Continue with sprint's original context",
        "ABORT_SWITCH - Cancel sprint switch"
    ]
```

### Sovereignty Enforcement
**Sprint Boundary Activation**:
1. **File Lock Restoration**: Reapply target sprint's locked_files restrictions
2. **Path Validation Reset**: Update safety_pre_tool.py with new boundaries
3. **Artifact Isolation**: Ensure temp directory separation
4. **Context Sovereignty**: Prevent cross-sprint operations

## SWITCH VALIDATION SEQUENCE

### Pre-Switch Checks
**Safety Validation**:
- [ ] Target sprint exists and is accessible
- [ ] No critical operations currently in progress
- [ ] Current sprint state properly saved
- [ ] User confirmation for context conflicts

### Switch Execution
**Stateful Transition**:
1. **Save Current State**: Preserve active sprint context
2. **Load Target State**: Restore target sprint context
3. **Validate Compatibility**: Check global context alignment
4. **Apply Boundaries**: Enforce new sprint sovereignty
5. **Confirm Success**: Verify switch completed successfully

### Post-Switch Verification
**Activation Confirmation**:
- [ ] New sprint shows as active in status displays
- [ ] File operations respect new boundaries
- [ ] Context pruning applied to prevent drift
- [ ] Commands reflect new sprint context

## ERROR HANDLING AND RECOVERY

### Invalid Sprint ID
**Graceful Failure**:
```
❌ INVALID SPRINT ID: 2026-01-09_plan_999_nonexistent

Available sprints:
🏃 2026-01-09_plan_004_user_auth (active)
✅ 2026-01-08_plan_003_api_endpoints (completed)
⏸️ 2026-01-06_plan_001_initial_setup (abandoned)

Use: /listsprints to see all available sprints
Use: /switch-sprint [valid_id] to switch context
```

### Context Conflict Scenarios
**Resolution Options**:
```
⚠️  GLOBAL CONTEXT CONFLICT DETECTED

Sprint "2026-01-08_plan_003_api_endpoints" was created with different global context:

Changes detected:
- Security rules updated (rm ban strengthened)
- Database patterns modified (async requirements added)
- Quality standards enhanced (additional TDD gates)

OPTIONS:
1. APPROVE_CURRENT_CONTEXT - Update sprint to use current global context
2. KEEP_ORIGINAL_CONTEXT - Continue with sprint's original context
3. ABORT_SWITCH - Cancel switch and stay in current sprint

Choose option (1-3):
```

### State Corruption Recovery
**Automatic Repair**:
1. **Backup Creation**: Preserve corrupted state as backup
2. **State Reconstruction**: Rebuild from available sprint data
3. **Integrity Verification**: Validate reconstructed state
4. **User Notification**: Report repair actions taken

## INTEGRATION WITH EXISTING SYSTEMS

### Safety Hook Coordination
**Enforcement Synchronization**:
- **Immediate Update**: safety_pre_tool.py ingests new SPRINT_STATE.json
- **Boundary Activation**: File path validation uses new locked_files array
- **Error Message Update**: Clear messages reflect current sprint context
- **Real-time Enforcement**: All subsequent operations respect new boundaries

### Command System Integration
**Workflow Continuity**:
- **Status Updates**: /listsprints reflects switch immediately
- **Context Awareness**: All commands operate within new sprint boundaries
- **Progress Continuity**: Phase and iteration tracking resumes correctly
- **Artifact Management**: Temp directory switches to new sprint location

### Startup Protocol Integration
**Seamless Transitions**:
- **Context Pruning**: Apply manifesto generation for clean transition
- **Clear Requirement**: Enforce /clear before operating in new context
- **State Persistence**: Maintain sprint progress across switches
- **User Guidance**: Clear instructions for post-switch operations

## SUCCESS VALIDATION

### Switch Completeness
**State Transition Verification**:
- ✅ Target sprint becomes active in SPRINT_STATE.json
- ✅ Previous sprint properly preserved or marked as paused
- ✅ File boundaries correctly applied to new sprint scope
- ✅ Global context reconciliation handled appropriately
- ✅ Safety hooks updated with new enforcement rules

### Context Integrity
**Continuity Preservation**:
- ✅ Sprint progress and phase information maintained
- ✅ Locked files and boundaries correctly restored
- ✅ Artifact directory isolation preserved
- ✅ Global context conflicts properly resolved
- ✅ No cross-sprint contamination during transition

### User Experience
**Seamless Operation**:
- ✅ Clear error messages for invalid operations
- ✅ Interactive conflict resolution when needed
- ✅ Immediate status updates after successful switch
- ✅ Preserved context allows immediate continuation
- ✅ Safety enforcement prevents accidental violations

### System Reliability
**Robust Operation**:
- ✅ Graceful handling of corrupted state files
- ✅ Recovery mechanisms for failed switches
- ✅ Comprehensive validation before state changes
- ✅ Atomic operations prevent partial switch states
- ✅ Backup and rollback capabilities for safety
