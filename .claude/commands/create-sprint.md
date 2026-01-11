# CREATE-SPRINT: Sprint Initialization with Global Context Hashing
**Purpose**: Initialize new sprint with unique ID, generate global context hash, and establish sprint boundaries.

## COMMAND EXECUTION PROTOCOL

### Command Syntax
**Basic Usage**:
```
/create-sprint "sprint description"
```

**Advanced Usage**:
```
/create-sprint "implement user authentication" --template=feature --scope=auth
```

### Sprint ID Generation
**Unique Identifier Creation**:
```bash
# Generate timestamp-based sprint ID
TIMESTAMP=$(date +"%Y-%m-%d")
COUNTER_FILE=".claude/sprint_counter.txt"

# Increment counter
if [ -f "$COUNTER_FILE" ]; then
    COUNTER=$(( $(cat "$COUNTER_FILE") + 1 ))
else
    COUNTER=1
fi
echo $COUNTER > "$COUNTER_FILE"

# Format: YYYY-MM-DD_plan_NNN_description_slug
SPRINT_ID="${TIMESTAMP}_plan_$(printf "%03d" $COUNTER)_$(echo "$SPRINT_DESCRIPTION" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/_/g' | sed 's/__*/_/g' | cut -c1-30)"
```

## GLOBAL CONTEXT HASH GENERATION

### Hash Source Files
**Comprehensive Context Capture**:
1. **CLAUDE.md**: Core invariants and operational procedures
2. **documentation/main/architecture.md**: Technology choices and patterns
3. **documentation/main/keygoals.md**: Project objectives and constraints
4. **.claude/rules/**: All active rules and constraints
5. **.claude/skills/**: Available AI specialist capabilities

### Hash Calculation Algorithm
**SHA256 Integrity Verification**:
```bash
# Generate comprehensive global context hash
GLOBAL_HASH=$(find documentation/main/ CLAUDE.md .claude/rules/ .claude/skills/ -type f -name "*.md" -exec sha256sum {} \; | sort | sha256sum | cut -d' ' -f1)

echo "Global Context Hash: $GLOBAL_HASH"
```

### Hash Storage and Tracking
**SPRINT_STATE.json Integration**:
```json
{
  "global_context": {
    "architecture_last_updated": "2026-01-09T12:00:00Z",
    "goals_last_updated": "2026-01-07T09:15:00Z",
    "current_hash": "a1b2c3d4e5f6...",
    "hash_sources": [
      "CLAUDE.md",
      "documentation/main/architecture.md",
      "documentation/main/keygoals.md",
      ".claude/rules/",
      ".claude/skills/"
    ]
  }
}
```

## SPRINT INITIALIZATION SEQUENCE

### Step 1: Validation Checks
**Pre-Creation Verification**:
1. **No Active Sprint**: Check SPRINT_STATE.json for null active_sprint
2. **Description Provided**: Ensure sprint description is meaningful
3. **Global Context Accessible**: Verify all hash source files exist
4. **Directory Permissions**: Confirm write access to required directories

### Step 2: Sprint Structure Creation
**Plan File Generation**:
1. **Template Selection**: Choose appropriate plan template based on sprint type
2. **Hydration Section Injection**: Add Sprint Context Hydration section
3. **Global Hash Insertion**: Populate validation section with current hash
4. **Data Integrity Rubric**: Add nonsense prevention requirements

### Step 3: SPRINT_STATE.json Update
**State Management**:
```json
{
  "active_sprint": {
    "id": "2026-01-09_plan_004_user_auth",
    "plan_path": "documentation/plans/2026-01-09_plan_004_user_auth.md",
    "phase": "planning",
    "iteration": 1,
    "status": "active",
    "created": "2026-01-09T14:30:00Z",
    "last_updated": "2026-01-09T14:30:00Z",
    "description": "implement user authentication",
    "global_context_hash": "a1b2c3d4e5f6...",
    "locked_files": [],
    "temp_directory": "temp/claudecode/2026-01-09_plan_004_user_auth"
  }
}
```

### Step 4: Directory Structure Setup
**Sprint Workspace Creation**:
1. **Temp Directory**: Create sprint-specific artifact storage
2. **Plan Directory**: Ensure documentation/plans/ exists
3. **Initial Boundaries**: Set up basic file scope constraints

## PLAN TEMPLATE INTEGRATION

### Hydration Section Population
**Automatic Content Injection**:
```
## Sprint Context Hydration
**Global Context References:**
- Tech Stack: [Auto-populated from architecture.md]
- Database Patterns: [Auto-populated from CLAUDE.md]
- Security Requirements: [Auto-populated from rules]
- Quality Standards: [Auto-populated from assessment rules]

**Active Constraints:**
- [Auto-populated from extract-constraints]

**Data Integrity Rubric (Nonsense Prevention):**
- **Chart/Data Validation**: Must check for N/A, NaN, null, undefined values
- **Business Logic Checks**: Flag impossible values (negative stock prices, 0.00% volatility)
- **UI State Verification**: Confirm meaningful data display, not placeholder content
- **Sanity Checker Requirements**: Visual proof required before Victory Declaration

**Hydration Validation:**
- **Global Context Hash**: a1b2c3d4e5f6...
- **Validation Status**: VERIFIED
- **Last Verified**: 2026-01-09T14:30:00Z
```

### Template Variants
**Sprint Type Selection**:
- **feature**: Standard feature implementation template
- **refactor**: Code restructuring and cleanup template
- **research**: Technology evaluation and prototyping template
- **infrastructure**: System setup and configuration template

## INTEGRATION WITH WORKFLOW

### Sprint Startup Protocol
**Post-Creation Actions**:
1. **Context Pruning Preparation**: Generate initial manifesto for planning phase
2. **Human /clear Requirement**: Set up for clean context transition
3. **Planner Activation**: Ready for `/implement` workflow continuation
4. **Boundary Enforcement**: Initialize safety hook integration

### State Persistence
**Automatic Updates**:
- **Progress Tracking**: Update SPRINT_STATE.json on phase transitions
- **Hash Verification**: Re-verify global context on each execution
- **Artifact Management**: Track temp directory usage and cleanup needs
- **Completion Recording**: Update sprint_history on successful completion

## ERROR HANDLING AND RECOVERY

### Creation Failure Scenarios
**Recovery Protocols**:
1. **Hash Generation Failure**: Fallback to timestamp-based pseudo-hash
2. **File System Issues**: Clean up partial directory creation
3. **State Corruption**: Restore from backup or recreate state
4. **Template Missing**: Use basic template with manual completion

### Conflict Resolution
**Concurrent Creation Prevention**:
1. **Lock File Creation**: Prevent multiple simultaneous sprint creation
2. **State Consistency**: Verify SPRINT_STATE.json integrity before updates
3. **Rollback Capability**: Ability to undo sprint creation if needed

## SUCCESS VALIDATION

### Creation Completeness
**Initialization Verification**:
- ✅ Sprint ID properly formatted and unique
- ✅ Global context hash accurately calculated
- ✅ Plan file created with hydration section
- ✅ SPRINT_STATE.json correctly updated
- ✅ Directory structure properly established

### Hash Integrity
**Context Capture Accuracy**:
- ✅ All specified source files included in hash
- ✅ Hash calculation deterministic and reproducible
- ✅ Hash storage properly integrated with state management
- ✅ Hash verification functional for conflict detection

### Template Integration
**Plan Quality**:
- ✅ Hydration section properly populated
- ✅ Data integrity rubric included
- ✅ Validation status correctly set
- ✅ Template appropriate for sprint type

### Workflow Readiness
**Integration Completeness**:
- ✅ Sprint discoverable by sprint-discovery rule
- ✅ Ready for /implement workflow continuation
- ✅ Safety hooks can enforce boundaries
- ✅ State persistence functional
