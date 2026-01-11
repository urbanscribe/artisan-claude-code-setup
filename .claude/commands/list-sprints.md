# LIST-SPRINTS: Display All Sprints with Status Overview
**Purpose**: Show comprehensive sprint status information with active sprint highlighting and completion tracking.

## COMMAND EXECUTION PROTOCOL

### Trigger Conditions
**Manual Invocation**:
```
/list-sprints
```
**Also triggered automatically**:
- During startup protocol when no active sprint is found
- After sprint operations to show updated status
- When user needs to see available sprint options

### SPRINT_STATE.json Data Ingestion
**Complete State Analysis**:
1. **Read SPRINT_STATE.json** from project root
2. **Parse active_sprint** object (if not null)
3. **Parse sprint_history** array
4. **Extract global_context** metadata
5. **Validate JSON structure** and handle corruption gracefully

### Sprint Status Display Format
**Comprehensive Status Report**:
```
SPRINT STATUS OVERVIEW
======================

ACTIVE SPRINT:
🏃 2026-01-09_plan_004_user_auth
   Status: active | Phase: implementation | Iteration: 3
   Created: 2026-01-09T10:30:00Z
   Description: Implement user authentication system
   Locked Files: 12 files in scope
   Global Context: VERIFIED (hash: a1b2c3d4...)

RECENT SPRINTS:
✅ 2026-01-08_plan_003_api_endpoints (completed)
   Finished: 2026-01-08T16:20:00Z | Duration: 2.5 hours
   Final Files: 8 files delivered | Status: completed

✅ 2026-01-07_plan_002_database_setup (completed)
   Finished: 2026-01-07T14:15:00Z | Duration: 1.8 hours
   Final Files: 5 files delivered | Status: completed

⏸️  2026-01-06_plan_001_initial_setup (abandoned)
   Abandoned: 2026-01-06T11:45:00Z | Duration: 45 minutes
   Reason: Requirements changed | Status: abandoned

GLOBAL CONTEXT STATUS:
📅 Last Updated: 2026-01-08T12:00:00Z
🔒 Current Hash: a1b2c3d4e5f6...
📊 Total Sprints: 4 (3 completed, 1 active, 0 abandoned)
```

### Status Indicators and Formatting
**Visual Status Encoding**:
- **🏃 Active Sprint**: Green highlight, full details, current phase/iteration
- **✅ Completed Sprints**: Checkmark, completion timestamp, file count
- **⏸️ Abandoned Sprints**: Pause symbol, abandonment reason, partial metrics
- **📅 Global Context**: Clock icon, last update time, hash status
- **🔒 Hash Status**: Lock icon with VERIFIED/CONFLICT_DETECTED indicators

### Sprint Metrics Calculation
**Computed Statistics**:
```python
# sprint_metrics.py
def calculate_sprint_metrics(sprint_data):
    """Calculate comprehensive sprint statistics."""

    if not sprint_data:
        return {}

    # Duration calculation
    created = datetime.fromisoformat(sprint_data['created'].replace('Z', '+00:00'))
    completed = datetime.fromisoformat(sprint_data.get('completed', datetime.now().isoformat()).replace('Z', '+00:00'))
    duration_hours = (completed - created).total_seconds() / 3600

    # File count (locked_files for active, final_files for completed)
    if 'locked_files' in sprint_data:
        file_count = len(sprint_data['locked_files'])
        file_type = 'locked'
    elif 'final_files' in sprint_data:
        file_count = len(sprint_data['final_files'])
        file_type = 'delivered'
    else:
        file_count = 0
        file_type = 'unknown'

    return {
        'duration_hours': round(duration_hours, 1),
        'file_count': file_count,
        'file_type': file_type,
        'completion_rate': calculate_completion_rate(sprint_data)
    }
```

### Global Context Validation
**Hash Status Verification**:
1. **Current Hash Generation**: Recalculate global context hash
2. **Comparison**: Match against stored global_context.current_hash
3. **Status Display**: Show VERIFIED or CONFLICT_DETECTED
4. **Action Required**: If CONFLICT_DETECTED, suggest hydration validation

### Sprint Health Assessment
**Quality Metrics**:
- **Completion Rate**: Files delivered vs planned (for completed sprints)
- **Duration Assessment**: Compare against typical sprint durations
- **Success Indicators**: Completion status and abandonment reasons
- **Trend Analysis**: Success rates and average durations

## SPRINT SELECTION ASSISTANCE

### Interactive Sprint Selection
**User Guidance for Selection**:
```
AVAILABLE SPRINTS:
1. 🏃 2026-01-09_plan_004_user_auth (ACTIVE)
   Status: active | Phase: implementation
   Use: /switch-sprint 2026-01-09_plan_004_user_auth

2. ✅ 2026-01-08_plan_003_api_endpoints (completed)
   Status: completed | Files: 8 delivered
   Use: /switch-sprint 2026-01-08_plan_003_api_endpoints

3. ⏸️ 2026-01-06_plan_001_initial_setup (abandoned)
   Status: abandoned | Reason: Requirements changed
   Use: /switch-sprint 2026-01-06_plan_001_initial_setup

To switch sprints: /switch-sprint [sprint_id]
To create new sprint: /create-sprint "description"
```

### Context Awareness
**Sprint Suitability Indicators**:
- **Active Sprint**: Shows current work focus and locked files
- **Completed Sprints**: Indicates stable, delivered functionality
- **Abandoned Sprints**: May contain partial work or alternative approaches
- **Global Context**: Shows which sprints align with current architectural state

## ERROR HANDLING AND RECOVERY

### JSON Corruption Detection
**State File Validation**:
1. **Syntax Check**: Verify valid JSON structure
2. **Schema Validation**: Check required fields exist
3. **Data Integrity**: Validate timestamp formats and ID patterns
4. **Recovery Options**: Suggest backup restoration or state recreation

### Missing Sprint Data
**Graceful Degradation**:
1. **Partial Display**: Show available data with missing field indicators
2. **Default Values**: Use sensible defaults for missing metrics
3. **User Notification**: Alert about data quality issues
4. **Repair Suggestions**: Recommend /create-sprint or manual state fixes

## INTEGRATION WITH WORKFLOW

### Startup Protocol Integration
**Automatic Status Display**:
1. **No Active Sprint**: Show list with selection prompt
2. **Active Sprint Available**: Display current status and options
3. **Context Conflicts**: Highlight hash mismatches requiring attention
4. **Quick Actions**: Provide immediate command suggestions

### Command Chain Integration
**Workflow Continuity**:
- **Post-Creation**: Auto-display after /create-sprint
- **Post-Switch**: Show new active sprint details after /switch-sprint
- **Post-Close**: Update display after /close-sprint completion
- **Regular Status**: Available for manual status checks

## SUCCESS VALIDATION

### Display Completeness
**Information Coverage**:
- ✅ All sprints listed with clear status indicators
- ✅ Active sprint prominently highlighted
- ✅ Comprehensive metrics for each sprint
- ✅ Global context status clearly shown
- ✅ Interactive selection guidance provided

### Data Accuracy
**Information Quality**:
- ✅ Real-time data from SPRINT_STATE.json
- ✅ Accurate calculations and metrics
- ✅ Current hash validation performed
- ✅ Status indicators reflect actual state
- ✅ Timestamps and durations correctly calculated

### User Experience
**Navigation Support**:
- ✅ Clear visual hierarchy and formatting
- ✅ Actionable command suggestions
- ✅ Context-aware recommendations
- ✅ Error handling with helpful messages
- ✅ Performance optimized for frequent checks
