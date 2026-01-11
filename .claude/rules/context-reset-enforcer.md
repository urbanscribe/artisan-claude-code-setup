# Context Reset Enforcer Rule (Tier 2)
## Purpose
Prevents context drift by enforcing clean slates between workflow phases.

## SESSION SUMMARY PROTOCOL
At every Human Gate (B, C, D, E), generate comprehensive session summary:
- **Phase Completed**: What was accomplished
- **Key Decisions**: Important choices made
- **Outstanding Items**: What remains to be done
- **Context Markers**: Important facts to preserve
- **Transition Notes**: Handover information for next phase

## MANDATORY /clear REQUIREMENT
**HUMAN MUST EXECUTE /clear** after reviewing session summary.

## WHY THIS MATTERS
Context drift occurs when agents remember draft mistakes during execution. Clean slate ensures agents follow Final Approved Plan, not hallucinated drafts.

## ENFORCEMENT
- Session summary automatically generated
- /clear command validation required
- Context isolation confirmed before proceeding

## INTEGRATION
- Loaded by /implement command at all human gates (B, C, D, E)
- Referenced in BOSS agent instructions
- Prevents cross-phase contamination
