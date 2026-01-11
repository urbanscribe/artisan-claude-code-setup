# Hook Denial Recovery Sub-Rule (Tier 3)
## Purpose
Teaches agents how to handle security hook denials gracefully and escalate to human assistance.

## DENIAL SCENARIOS

### RM Ban Denial
**Trigger**: Agent attempts any rm, rmdir, unlink, shred, or del command
**Response Protocol**:
1. **Immediate Apology**: "I apologize, but I cannot execute rm commands due to absolute security policy"
2. **Clear Explanation**: "The zero-exception rm ban prevents all deletion operations to ensure data safety"
3. **Escalation Path**: "Please ask a human team member to perform this deletion manually"
4. **No Retry**: Do not attempt workarounds or alternative commands

### Worktree Boundary Denial
**Trigger**: Agent attempts file operations outside git worktree
**Response Protocol**:
1. **Immediate Apology**: "I apologize, but this operation is outside the current worktree boundary"
2. **Clear Explanation**: "All file operations must stay within the git worktree for security isolation"
3. **Escalation Path**: "Please ensure you're in the correct worktree or ask a human to adjust the boundary"
4. **No Retry**: Do not attempt to navigate outside boundaries

### Repair Scope Denial
**Trigger**: Agent attempts modification outside BOSS-approved repair scope
**Response Protocol**:
1. **Immediate Apology**: "I apologize, but this file is outside the approved repair scope"
2. **Clear Explanation**: "Only BOSS-approved paths can be modified during repair operations"
3. **Escalation Path**: "Please ask the BOSS (human) to add this path to repair_lock.json"
4. **No Retry**: Do not attempt to unlock or modify scope yourself

## GENERAL RECOVERY PRINCIPLES

### Do Not Loop
- **Single Attempt**: If hook denies, stop immediately
- **No Workarounds**: Do not try alternative approaches
- **No Evasion**: Do not attempt to bypass security measures

### Clear Communication
- **Structured Response**: Use the exact apology + explanation + escalation format
- **No Technical Jargon**: Explain in plain English why the operation was blocked
- **Actionable Next Steps**: Tell the human exactly what to do

### Human Escalation
- **Identify BOSS**: Direct requests to human team members
- **Specific Request**: Tell them exactly what path/permission is needed
- **Wait for Approval**: Do not proceed until human provides workaround

## INTEGRATION
- Loaded automatically when hook denial detected
- Referenced in safety_pre_tool.py error responses
- Prevents infinite retry loops on security blocks
