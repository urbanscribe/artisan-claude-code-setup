# Confidence Check Sub-Rule (Tier 3)
## Purpose
Provides detailed scoring rubric for automated quality assessment and remediation triggering.

## SCORING DIMENSIONS (0-100 Scale)

### 1. Clarity (20% weight)
**Objective Assessment**:
- **10**: Objectives perfectly clear, no ambiguity, single interpretation possible
- **7-9**: Mostly clear with minor gaps requiring minimal clarification
- **4-6**: Significant ambiguity requiring substantial clarification
- **0-3**: Unclear, contradictory, or incomprehensible objectives

**Evaluation Criteria**:
- Terminology consistently defined
- Scope boundaries explicitly stated
- Success criteria measurable and unambiguous
- Assumptions and constraints clearly documented

### 2. Evidence & Sources (25% weight)
**Verification Requirements**:
- **10**: All claims backed by multiple verifiable sources with citations
- **7-9**: Most claims supported, minor gaps in sourcing
- **4-6**: Some unsupported claims requiring additional research
- **0-3**: Mostly unsupported or speculative claims

**Evidence Standards**:
- Empirical data or established research cited
- Industry best practices referenced
- Historical precedent or case studies included
- Expert consensus or authoritative sources used

### 3. Risk Analysis & Trade-offs (25% weight)
**Comprehensive Assessment**:
- **10**: All major risks identified with specific mitigation strategies
- **7-9**: Major risks identified with general mitigation approaches
- **4-6**: Some risks noted without comprehensive mitigation
- **0-3**: Risks ignored or major blind spots present

**Risk Evaluation**:
- Technical risks (scalability, performance, compatibility)
- Business risks (timeline, budget, stakeholder impact)
- Operational risks (deployment, maintenance, support)
- Alternative approaches evaluated with trade-offs analyzed

### 4. Reputation Stake (30% weight)
**Quality Commitment**:
- **10**: Willing to personally guarantee quality and outcomes
- **7-9**: High confidence with documented caveats
- **4-6**: Significant doubts about reliability or completeness
- **0-3**: Would not stake professional reputation on quality

**Stake Assessment**:
- Independent verification of claims
- Peer review simulation performed
- Edge cases and failure modes considered
- Long-term viability and sustainability evaluated

## AUTOMATED SCORING PROCESS

### Scoring Calculation
```
Total_Score = (Clarity × 0.20) + (Evidence × 0.25) + (Risk × 0.25) + (Stake × 0.30)
```

### Threshold Actions
- **≥90**: Enterprise-ready, proceed without remediation
- **80-89**: High quality, optional minor improvements
- **70-79**: Good quality, systematic improvements recommended
- **60-69**: Adequate quality, significant enhancements required
- **<60**: Poor quality, fundamental rework required

## REMEDIATION TRIGGERING

### Automatic Intervention Levels
- **<80 Total**: Invoke confidence-booster skill automatically
- **<60 Total**: Require human review and approval before proceeding
- **<40 Total**: Block workflow advancement until quality improved

### Remediation Focus Areas
- **Clarity Issues**: Rewrite ambiguous sections, add definitions, clarify scope
- **Evidence Gaps**: Research and add citations, validate claims, add data
- **Risk Oversights**: Perform risk analysis, develop mitigation strategies
- **Stake Concerns**: Independent verification, peer review, edge case testing

## QUALITY VALIDATION CHECKLIST

### Pre-Scoring Validation
- [ ] All required sections present and complete
- [ ] Claims specific and measurable, not vague
- [ ] Sources cited with accessible references
- [ ] Assumptions explicitly stated and justified
- [ ] Edge cases and failure modes considered

### Scoring Consistency Checks
- [ ] Individual dimension scores justify total calculation
- [ ] Weighting applied correctly per dimension
- [ ] Threshold actions appropriate for score
- [ ] Remediation recommendations specific and actionable

## INTEGRATION POINTS

### Hook Integration
- **validation_post_tool.py**: Automatic scoring on output completion
- **Pre-deployment gates**: Confidence checks before workflow advancement
- **Quality dashboards**: Score tracking and trend analysis

### Skill Integration
- **confidence-booster**: Triggered automatically for scores <80
- **evaluator**: Uses confidence scores for approval decisions
- **skeptic**: Challenges low-confidence elements

### Workflow Integration
- **Planning phase**: Confidence validation of specifications
- **Implementation phase**: Code quality confidence assessment
- **Testing phase**: Test coverage and effectiveness evaluation
- **Deployment phase**: Overall deliverable confidence verification

## CONTINUOUS IMPROVEMENT

### Scoring Calibration
- **Regular Review**: Scoring criteria validated against outcomes
- **Domain Adaptation**: Dimension weights adjusted for specific contexts
- **New Dimensions**: Additional quality aspects added as needed
- **Threshold Tuning**: Action thresholds refined based on experience

### Process Optimization
- **Automation Enhancement**: More aspects scored automatically
- **Feedback Integration**: User feedback improves scoring accuracy
- **Training Updates**: Team training improved based on common issues
- **Tool Refinement**: Scoring tools enhanced for better accuracy

## EXCEPTION HANDLING

### Override Protocols
- **Documented Justification**: Any confidence threshold override requires explanation
- **Escalation Requirements**: Low confidence overrides need management approval
- **Follow-up Tracking**: Override outcomes monitored for process improvement
- **Pattern Analysis**: Override reasons analyzed for systemic improvements

### Special Cases
- **Research Outputs**: Different standards for exploratory vs. implementation work
- **Time-Critical Deliveries**: Accelerated remediation for urgent requirements
- **Legacy Integration**: Adjusted standards for existing system compatibility
- **Experimental Features**: Higher tolerance for uncertainty in innovative approaches
