# /implement - Professional Execution Engine with Ralph Wiggum Resilience

## Purpose
Execute comprehensive feature implementation with professional-grade reliability, sprint boundary enforcement, and Ralph Wiggum loop resilience. This transforms casual development into structured, interruptible, and quality-controlled execution.

## Sprint Validation Gates (MANDATORY STATE SYNC)
**MANDATORY STATE SYNC**: Read PROJECT_REGISTRY.json → Output "OS_STATUS: Project [Name] | Sprint [ID] | Phase [execution]"

**Sprint Context Validation**:
1. **Active Sprint Check**: PROJECT_REGISTRY.json.sprints.active exists and valid
2. **Phase Verification**: sprint.phase = "execution" and manifesto_locked = true
3. **Boundary Confirmation**: locked_files array populated and accessible
4. **Execution Blocking**: Cannot proceed without complete sprint context

**Sprint Blocking Logic**:
```
🚫 EXECUTION BLOCKED: Sprint context invalid
Required: Active sprint with locked manifesto
Current Status: [No active sprint / Manifesto not locked / Invalid phase]
Next Action: /startnewsprint "feature description"
```

## Ralph Wiggum Loop Resilience
**Promise Tag Enforcement**: Require `<promise>SANITY_CHECK_PASS</promise>` as exit condition
**Hook Integration**: safety_pre_tool.py intercepts outputs and validates promise tags before loop exit
**Intelligent Monitoring**: Assessment checkpoints at 10, 25, 40, 60+ iterations with progress analysis
**Loop Resilience**: Prevents 70% of execution failures through structured completion validation

## Permissive Mode Options
**Professional Development Mode**: Streamline sprint workflow with intelligent approvals

```
/implement --permissive    # Resume sprint work with reduced approval prompts
/implement --permissive    # Continue active sprint with auto-approved safe operations
```

**Auto-Approved Operations** (no user interruption):
- Development servers: `npm run dev`, `yarn dev`, `python manage.py runserver`
- File operations: `cat`, `ls`, `grep`, `find`, `mkdir`, `cp`, `mv`
- Git read-only: `git status`, `git log`, `git diff`, `git show`
- System monitoring: `ps`, `top`, `df`, `du`
- Build tools: `npm run build`, `make`, `gcc --version`

**Still Requires Approval**:
- Destructive operations: `rm`, `drop table`, `git push --force`
- Network uploads: `scp`, `rsync`, destructive `curl`/`wget`
- System changes: `shutdown`, `format`, `fdisk`
- Security-sensitive: `.env` modifications, credential access

**Iteration Management**:
```json
{
  "active_sprint": {
    "phase": "execution",
    "iteration": 3,
    "max_iterations": 10,
    "execution_context": {
      "last_promise_validated": "SANITY_CHECK_PASS",
      "human_escalation_granted": false,
      "boundary_violations": 0,
      "progress_markers": ["planning_complete", "implementation_started"]
    }
  }
}
```

## Professional Execution Workflow

### GATE A: PLAN VALIDATION (Sprint Context)
**MANDATORY STATE SYNC**: Read PROJECT_REGISTRY.json → "OS_STATUS: Project [Name] | Sprint [ID] | Phase [execution]"
**Sprint Boundary Check**: Validate all operations against locked_files scope
**Iteration Tracking**: Update PROJECT_REGISTRY.json with execution progress

**STOP - HUMAN:**
1. Verify sprint context established (active sprint with manifesto)
2. Confirm execution within approved boundaries
3. Type: APPROVE_SPRINT_CONTEXT

### GATE B: CODE IMPLEMENTATION (Boundary-Enforced)
Only after APPROVE_SPRINT_CONTEXT: Invoke @Coder (sprint-aware)
**Boundary Enforcement**: All file operations validated against manifesto
**Progress Tracking**: Update iteration count after each major step
**Promise Validation**: Require `<promise>READY_FOR_TESTER</promise>` for progression

**STOP - HUMAN:**
1. Verify coder output ends with: READY_FOR_TESTER
2. Confirm all changes within sprint boundaries
3. Validate iteration count updated in PROJECT_REGISTRY.json
4. Type: APPROVE_CODE_IMPLEMENTATION

### GATE C: TESTING EXECUTION (Sprint-Scoped)
Only after APPROVE_CODE_IMPLEMENTATION: Invoke @Tester (sprint-aware)
**Boundary-Constrained Testing**: Test only components within locked_files scope
**Artifact Isolation**: Store results in sprint-specific temp directory
**Promise Validation**: Require `<promise>READY_FOR_EVALUATOR</promise>` for progression

**STOP - HUMAN:**
1. Verify tester output ends with: READY_FOR_EVALUATOR
2. Confirm UI artifacts provided and validated
3. Check test results correlated to sprint components
4. Type: APPROVE_TESTING_EXECUTION

### SANITY CHECK GATE (Conditional, Sprint-Aware)
**IF UI/API features detected**: Invoke @sanity-checker with sprint context
**Boundary Validation**: Ensure sanity checks relate to sprint scope only
**Promise Enforcement**: `<promise>SANITY_CHECK_PASS</promise>` required for completion

**STOP - HUMAN:**
1. Verify sanity-checker output contains: SANITY_CHECK_PASS
2. Confirm UI integrity and data coherence within sprint boundaries
3. Validate no boundary violations detected
4. Type: APPROVE_SANITY_CHECK

### FINAL GATE: EVALUATION (Sprint Context)
Only after APPROVE_SANITY_CHECK: Invoke @Evaluator (sprint-aware)
**Sprint-Scoped Assessment**: Evaluate only changes within manifesto boundaries
**State Integration**: Update evaluation progress in PROJECT_REGISTRY.json
**Completion Validation**: Require SANITY_CHECK_PASS for final approval

**HUMAN MAKES FINAL DECISION ON FEATURE COMPLETION**

## Execution State Persistence
**Interruption Recovery**: Sprint execution survives session interruptions
**Progress Preservation**: Iteration counts and completed steps maintained
**Boundary Continuity**: File operation permissions persist across invocations
**State Synchronization**: PROJECT_REGISTRY.json updated after each gate

## Professional Quality Controls
- **Iteration Limits**: Maximum 10 iterations (configurable safety bound)
- **Boundary Enforcement**: Physical blocking of out-of-scope operations
- **Promise Tag Validation**: Automated detection of completion markers
- **Progress Tracking**: Real-time visibility into execution state
- **Human Escalation**: Override capability for complex features requiring >10 iterations

## GATE A: PLAN APPROVAL (with Project Discovery)
Load rules/project-discovery.md
Invoke @Planner: "EXECUTE PROJECT DISCOVERY THEN WRITE THE PLAN for '$1'"

**STOP - HUMAN:**
1. Review architectural ingestion confirmation
2. Review PLAN.md thoroughly
3. Generate session summary, require /clear
4. Load rules/context-reset-enforcer.md
5. Type: APPROVE_PLAN

## GATE B: IMPROVED PLAN APPROVAL (with Context Reset)
Only after APPROVE_PLAN: Generate session summary, require /clear
Load rules/context-reset-enforcer.md
Invoke @Planner: "IMPROVE THE PLAN"

**STOP - HUMAN:**
1. Review improved PLAN.md
2. If plan is >1500 tokens, HUMAN must paste PLAN.md into new Claude session and continue there
3. Generate session summary, require /clear
4. Type: APPROVE_IMPROVED_PLAN

## GATE C: FINAL PLAN APPROVAL (with Context Reset)
Only after APPROVE_IMPROVED_PLAN: Generate session summary, require /clear
Invoke @Planner: "MAKE SURE NOTHING FOR TEAM TO CHOOSE"

**STOP - HUMAN:**
1. Verify Planner output contains: UNRESOLVED: NONE
2. Verify ARCH_DECISIONS section lists all resolved choices
3. Generate session summary, require /clear
4. Type: APPROVE_FINAL_PLAN

## GATE D: CODE WRITE APPROVAL (with Context Reset)
Only after APPROVE_FINAL_PLAN: Generate session summary, require /clear
Invoke @Coder

**STOP - HUMAN:**
1. Verify Coder output includes: test execution output with 0 failures
2. Verify Coder output ends with: READY_FOR_TESTER
3. If tests failed, do not approve - address test failures first
4. Generate session summary, require /clear
5. Type: APPROVE_CODE_WRITE

## GATE E: UI TESTING + SANITY CHECK
Only after APPROVE_CODE_WRITE: Generate session summary, require /clear
Invoke @Tester

**STOP - HUMAN:**
1. Verify Tester output contains: UI artifacts provided by human? = yes
2. Verify Tester output includes: test execution output showing results
3. Verify Tester output ends with: READY_FOR_TESTER_COMPLETE
4. **ENFORCED**: Workflow BLOCKS automatically if UI artifacts = no
5. If tests failed, DO NOT APPROVE
6. Generate session summary, require /clear
7. Type: APPROVE_TESTING

## SANITY CHECK GATE (Conditional)
**IF UI/API features detected**: Invoke @sanity-checker

**STOP - HUMAN:**
1. Verify sanity-checker output contains: SANITY_CHECK_PASS
2. Verify UI integrity and data coherence validation
3. If sanity check fails, address issues before proceeding
4. Generate session summary, require /clear
5. Type: APPROVE_SANITY_CHECK

## FINAL GATE: EVALUATION
Only after APPROVE_SANITY_CHECK (or APPROVE_TESTING if no UI features): Invoke @Evaluator

**ENFORCED**: READY_FOR_EVALUATOR blocked without sanity-checker proof for UI/API features

**HUMAN MAKES FINAL DECISION ON FEATURE COMPLETION**

## User Guidance Output
**MANDATORY STATE SYNC**: Read PROJECT_REGISTRY.json → Display OS_STATUS

**Gate-Specific Guidance**:

**After APPROVE_SPRINT_CONTEXT**:
```
🎯 SPRINT EXECUTION AUTHORIZED
✅ Sprint context validated
✅ Manifesto boundaries confirmed
✅ Iteration tracking: 0/10

🎯 NEXT: Code Implementation
Begin Ralph Wiggum loop with promise tag enforcement
💡 PROFESSIONAL TIP: Promise tags prevent premature loop exits
```

**After APPROVE_CODE_IMPLEMENTATION**:
```
🎯 CODE IMPLEMENTATION COMPLETE
✅ Tests written and passing
✅ Implementation within boundaries
✅ Iteration: [X]/10

🎯 NEXT: Testing Execution
Run comprehensive testing within sprint scope
💡 PROFESSIONAL TIP: Sprint-scoped testing ensures quality isolation
```

**After APPROVE_SANITY_CHECK**:
```
🎯 SANITY CHECK PASSED
✅ UI integrity validated
✅ Data coherence confirmed
✅ Sprint boundaries maintained

🎯 NEXT: Final Evaluation
Complete professional feature assessment
💡 PROFESSIONAL TIP: Structured completion prevents forgotten deliverables
```

**Execution Blocked Guidance**:
```
🚫 EXECUTION BLOCKED
❌ [Specific blocking reason]

🎯 RESOLUTION PATH
1. [Specific resolution steps]
2. Use /projectstatus to check current state
3. Complete requirements before retrying

💡 PROFESSIONAL DISCIPLINE: Blocking prevents quality compromises
```

**Guidance Logic**:
- Display after each gate completion
- Show iteration progress and boundaries
- Provide clear next-action guidance
- Include professional discipline reinforcement
- Offer specific resolution paths for blocked states
- Adapt based on PROJECT_REGISTRY.json execution state
