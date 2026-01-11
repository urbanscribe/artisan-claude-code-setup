# SPRINT-DISCOVERY: Active Sprint Identification and Prioritization

## AUTOMATIC SPRINT DISCOVERY PROTOCOL

### Primary Discovery Logic
**SPRINT_STATE.json Priority Check**:
1. **Read SPRINT_STATE.json** from project root
2. **Check active_sprint field** for non-null value
3. **Validate active sprint**:
   - Plan file exists at specified plan_path
   - Plan file is readable
   - Status is "active"
4. **If valid active sprint found**: Set as current execution context

### Fallback Discovery Logic (No Active Sprint)
**Documentation Scan Protocol**:
1. **Scan documentation/plans/** directory for plan files
2. **Filter valid plan files**: Must match pattern `*plan_*.md`
3. **Sort by priority**:
   - **Primary**: Most recently modified file
   - **Secondary**: Highest numbered plan ID
   - **Tertiary**: Lexicographically latest filename

### Sprint Validation Requirements
**MANDATORY VALIDATION CHECKS**:
- [ ] Plan file exists and is readable
- [ ] Plan contains valid sprint metadata (title, date, objectives)
- [ ] No conflicting active sprints in history
- [ ] Global context hash matches (if specified)
- [ ] Plan follows required structure format

## SPRINT ACTIVATION WORKFLOW

### Automatic Activation (/implement Integration)
**COMMAND TRIGGER**: When `/implement` command executes
1. **Pre-execution discovery**: Run sprint discovery protocol
2. **Context validation**: Ensure discovered sprint is appropriate for new work
3. **State update**: Update SPRINT_STATE.json with new active sprint
4. **File locking**: Initialize locked_files array with sprint scope
5. **Proceed with implementation**: Continue with normal workflow

### Manual Sprint Management
**COMMAND INTEGRATION**:
- **/switch-sprint [id]**: Manually select specific sprint by ID
- **/sprint-status**: Display current active sprint and available options
- **/create-sprint "description"**: Initialize new sprint with generated ID

### Context Sovereignty Enforcement
**EXECUTION BOUNDARIES**:
- **File scope restriction**: Only locked_files array paths are writable
- **Context isolation**: Sprint execution cannot modify global architecture
- **Artifact containment**: All temporary files in sprint-specific temp directory
- **State persistence**: Progress tracked in SPRINT_STATE.json

## DISCOVERY EDGE CASES

### Multiple Recent Plans
**CONFLICT RESOLUTION**:
1. **Time-based priority**: Most recently modified takes precedence
2. **Human resolution**: If timestamps identical, prompt user to choose
3. **Plan maturity**: Completed plans excluded from active consideration

### Missing or Corrupted State
**FAIL-SAFE PROTOCOLS**:
1. **JSON validation**: Verify SPRINT_STATE.json is valid JSON
2. **Backup recovery**: Attempt to recover from sprint_history if corrupted
3. **Fresh initialization**: Create new state if recovery impossible
4. **Human notification**: Alert user to state issues requiring attention

### Global Context Conflicts
**HASH VALIDATION**:
1. **Hash comparison**: Compare stored vs current global context hash
2. **Stale detection**: If hash mismatch, mark sprint as potentially stale
3. **Human validation**: Require human approval before proceeding with stale sprint
4. **Re-hydration**: Update sprint context with current global state

## SPRINT METADATA REQUIREMENTS

### Required Sprint Attributes
**MANDATORY FIELDS**:
- **id**: Unique identifier (format: YYYY-MM-DD_plan_NNN_feature)
- **plan_path**: Relative path to plan document
- **status**: active|completed|abandoned
- **created**: ISO timestamp
- **locked_files**: Array of file/directory paths in scope

### Optional Sprint Attributes
**ENHANCEMENT FIELDS**:
- **phase**: planning|implementation|testing|evaluation
- **iteration**: Current Ralph Wiggum loop count
- **global_context_hash**: Hash of global docs at sprint start
- **temp_directory**: Path to sprint artifacts

## INTEGRATION WITH EXISTING SYSTEMS

### Rules System Coordination
**HIERARCHICAL LOADING**:
1. **Global rules first**: CLAUDE.md and core rules always loaded
2. **Sprint rules second**: Sprint-specific constraints applied
3. **Context precedence**: Global laws override sprint preferences
4. **Dynamic loading**: Rules loaded based on sprint requirements

### Command System Extensions
**NEW COMMANDS**:
- **/sprint-discovery**: Manual trigger of discovery protocol
- **/validate-sprint-context**: Check current sprint validity
- **/sprint-boundaries**: Display current file scope restrictions

### Hook System Integration
**VALIDATION ENHANCEMENT**:
- **safety_pre_tool.py**: Ingest SPRINT_STATE.json for file path validation
- **validation_post_tool.py**: Check sprint state consistency after operations
- **Stateful enforcement**: Hook blocks operations outside sprint scope

## SUCCESS VALIDATION

### Discovery Accuracy
**CORRECTNESS METRICS**:
- **Active sprint detection**: 100% accuracy when active sprint exists
- **Fallback selection**: Most appropriate plan selected when no active sprint
- **Validation success**: All discovered sprints pass validation checks
- **Context integrity**: No false positives for stale or invalid sprints

### Performance Impact
**EFFICIENCY REQUIREMENTS**:
- **Discovery speed**: < 1 second for typical project sizes
- **Memory usage**: Minimal additional memory for state management
- **File I/O overhead**: < 100ms for SPRINT_STATE.json operations
- **Scalability**: Performance maintained with 100+ sprint history entries
