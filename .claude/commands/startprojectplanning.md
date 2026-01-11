# /startprojectplanning - Professional Project Foundation

## Purpose
Initialize a new project with structured foundation, replacing casual "jump right in" development with professional discipline. This command enforces the #1 cause of project failure prevention by requiring proper vision, goals, and architecture before any development work.

## Workflow
1. **MANDATORY STATE SYNC**: Read PROJECT_REGISTRY.json first
2. **OS_STATUS Output**: "OS_STATUS: Project [Name] | Sprint [Planning] | Phase [foundation]"
3. **Foundation Check**: Block if foundation already complete (suggest /projectstatus)
4. **Guided Interviews**: Stakeholder vision and objectives gathering
5. **Document Creation**: keygoals.md, architecture.md, projectimplementationplan.md
6. **Quality Validation**: Foundation completeness verification
7. **State Update**: Mark foundation as complete in PROJECT_REGISTRY.json

## Command Structure
```
OS_STATUS: Project [Name] | Sprint [Planning] | Phase [foundation]
```

## Required Skills
- foundation-specialist (patient interviewer, structured thinker, quality-focused)
- Model: opus-4.5 (complex stakeholder interactions)
- Context: fork (isolated foundation work)
- Permissions: read, grep, run_terminal_cmd (foundation-appropriate)

## Output Format
```
📋 PROJECT FOUNDATION INITIALIZATION
========================================

🎯 VISION CAPTURE
- Stakeholder interviews completed
- Project vision documented
- Success criteria defined

📝 DOCUMENTATION CREATED
- keygoals.md: Vision, objectives, success metrics
- architecture.md: Technical patterns, constraints
- projectimplementationplan.md: High-level sprint roadmap

✅ FOUNDATION COMPLETE
========================================
Ready for sprint planning: /startsprintplanning
```

## Error Handling
- **Foundation Already Complete**: "⚠️ Project foundation already established. Use /projectstatus to view current state."
- **Missing Prerequisites**: Clear guidance on what needs to be prepared
- **State Corruption**: Registry validation and recovery suggestions

## Integration
- Updates PROJECT_REGISTRY.json.foundation.complete = true
- Generates document hashes for integrity validation
- Enables subsequent sprint planning workflows
- Blocks casual development until foundation complete

## Professional Discipline
This command physically prevents the #1 cause of project failure by requiring structured setup before any development work begins. No more unstructured jumping into code - every project starts with professional foundation.

## User Guidance Output
**MANDATORY STATE SYNC**: Read PROJECT_REGISTRY.json → Display OS_STATUS

**Post-Execution Guidance**:
```
🎯 FOUNDATION ESTABLISHED
✅ Project foundation complete
✅ Keygoals.md, architecture.md, projectimplementationplan.md created

🎯 NEXT STEPS
1. Run /startsprintplanning to begin structured sprint development
2. Use /projectstatus to monitor project health
3. Begin professional development workflow

💡 PROFESSIONAL DISCIPLINE: Foundation-first prevents 60% of project failures
```

**Guidance Logic**:
- Always display after successful foundation completion
- Show clear progression path to sprint planning
- Reinforce professional discipline benefits
- Provide immediate next-action guidance
