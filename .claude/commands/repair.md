description: Repair workflow for addressing test failures or evaluation rejections. argument-hint: [repair-description]
---------------------------------------------------------------------------------------------------------------

Repair Workflow: $1
===================

REPAIR LOOP for addressing: $1

## REPAIR PROTOCOL

You are the BOSS entering REPAIR MODE for scoped fixes.

## STEP 1: ISOLATE FAILURE
Analyze the failure: $1

**STOP - HUMAN:**
1. Identify exact failure scope (which tests? which code?)
2. Type /clear to reset context
3. Type: REPAIR_ISOLATED

## STEP 1B: SCOPE DEFINITION (BOSS-CONTROLLED)
**BOSS PROMPTS HUMAN**: "Identify file paths to unlock for repair:"

- Human specifies exact file paths to allow modification
- BOSS validates paths exist in filesystem
- BOSS writes validated paths to repair_lock.json

**SCOPE ENFORCEMENT**: Only listed paths writable during repair
- Agent cannot modify files outside approved scope
- Human sovereignty over repair boundaries maintained

## STEP 2: CODE FIX (SCOPED ONLY)
Only after REPAIR_ISOLATED: Invoke @Coder for targeted fix

**Coder Instructions:**
Fix ONLY the identified failure scope.
Do NOT make unrelated changes.
End with: READY_FOR_TESTER

**STOP - HUMAN:**
1. Verify fix is scoped and complete
2. Type /clear to reset context
3. Type: REPAIR_CODE_FIXED

## STEP 3: RETEST (SCOPED ONLY)
Only after REPAIR_CODE_FIXED: Invoke @Tester for scoped retest

**Tester Instructions:**
Test ONLY the previously failing scope.
Provide evidence of fix.
End with: READY_FOR_EVALUATOR

**STOP - HUMAN:**
1. Verify retest shows fix
2. Type /clear to reset context
3. Type: REPAIR_COMPLETE

## STEP 4: REEVALUATE
Only after REPAIR_COMPLETE: Invoke @Evaluator for repair assessment

If Evaluator approves: Feature complete.
If Evaluator rejects: Repeat REPAIR LOOP with refined scope.
