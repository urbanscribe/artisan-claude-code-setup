# Artisan's Claude Code Operating System

# Artisan's Claude Code Operating System

## 🎯 What This Is

**Artisan's Claude Code Operating System** transforms Claude Code from a basic AI coding assistant into a **comprehensive professional development environment** that enforces structured project foundation, sprint lifecycle management, and enterprise-grade quality controls.

Instead of casual "jump right in" development, you get **20 specialized AI professionals** working together in a sophisticated **Global Context, Local Execution** model with **professional discipline enforcement**.

## 🚀 Quick Start: Get Started in 5 Minutes

### Prerequisites
- **Claude Code installed** ([Installation guide](https://docs.anthropic.com/claude/docs/claude-code))
- **Terminal/command prompt access**
- **Empty or existing project directory**

### Step 1: Clone This Repository
```bash
# Download the setup files (replace 'my-project' with your project name)
git clone https://github.com/urbanscribe/artisan-claude-code-setup.git my-project-setup
cd my-project-setup
```

### Step 2: Set Your Project Location
```bash
# Tell the setup where to install (use your actual project path)
export CC_DESTINATION=/path/to/your/project

# Example: If your project is in ~/my-app
export CC_DESTINATION=~/my-app
```

### Step 3: Run Setup
```bash
# This installs everything automatically
./scripts/setup.sh
```

### Step 4: Start Using Your AI Team
```bash
# Go to your project
cd "$CC_DESTINATION"

# Start Claude Code
claude

# Try your first feature
/implement "build a user login system"
```

**That's it!** 🎉 You now have a professional AI development team ready to work with you.

**After setup, your project will contain only:**
- `CLAUDE.md` - Global context and invariants (in project root)
- `.claude/` - Complete AI system (all internal files contained here)

**No other folders or files are created in your project root!** 🧹

---

## 📋 What You Get: 20 AI Specialists + Professional Workflow

### 🤖 Your AI Development Team
- **20 Specialized AI Professionals** (foundation, planning, coding, testing, review, recovery, etc.)
- **Enterprise-Grade Quality Controls** (confidence scoring, architectural validation, security checks)
- **Professional Workflow Enforcement** (structured development, human approval gates, sprint management)

### 🚀 Professional Development Commands
- **`/implement "feature"`** - Build complete features with full AI team coordination
- **`/startprojectplanning`** - Guided project foundation establishment
- **`/startsprintplanning`** - 5-phase planning with 10 quality gates
- **`/startnewsprint [name]`** - Create execution boundaries with manifestos
- **`/projectstatus`** - Real-time project and sprint visibility
- **`/listsprints`** - Sprint management dashboard
- **`/endsprint`** - Professional completion with cleanup
- **`/repair "issue"`** - Targeted problem fixing
- **`/restoreralphwiggam`** - Intelligent system recovery

### 🛡️ Enterprise-Grade Features
- **Stateful Security**: PROJECT_REGISTRY.json maintains integrity across sessions
- **Worktree Isolation**: Prevents cross-project contamination
- **Ralph Wiggum Loops**: Automated iterative perfection (promise-based execution)
- **Human Approval Gates**: You control all major architectural decisions
- **Context Pruning**: Memory management prevents confusion between phases
- **Recovery Systems**: Multiple levels of system restoration

---

## 🏗️ ARTISAN'S OPERATING SYSTEM OVERVIEW

### **The Professional Discipline Transformation**
Artisan's Operating System prevents casual development through **enforced structured workflows**:

#### **1. Project Foundation Layer**
- **`/startprojectplanning`**: Guided initialization preventing superficial setup
- **Quality Enforcement**: Foundation required before any development work
- **Stakeholder Integration**: Vision, goals, and architecture establishment
- **Professional Setup**: Replaces "jump right in" with structured initialization

#### **2. Sprint Operating System**
- **`/startsprintplanning`**: 5-phase planning with integrated quality gates
- **`/startnewsprint`**: Execution boundary establishment with immutable manifestos
- **`/implement`**: Ralph Wiggum execution with promise tag enforcement
- **`/endsprint`**: Professional completion with cleanup and documentation
- **`/listsprints`**: Visual sprint management and status tracking
- **`/projectstatus`**: Comprehensive project visibility and guidance

#### **3. Execution Control Enhancement**
- **Ralph Wiggum Resilience**: Promise tag enforcement preventing loop failures
- **Sprint-Aware Skills**: All development skills respect manifesto boundaries
- **Iteration Management**: Safety bounds with human escalation capability
- **Boundary Enforcement**: Physical blocking of out-of-scope operations

#### **4. Recovery & Resilience**
- **`/restoreralphwiggam`**: Registry priority recovery from CLAUDE.md overwrites
- **`./setup.sh --restore`**: Out-of-band recovery preserving professional state
- **State Reconstruction**: FULL/PARTIAL/MINIMAL confidence level recovery
- **Professional Continuity**: System survives disruptions maintaining integrity

### **Three-Tier Architecture**
Artisan's Operating System follows strict architectural separation:
- **CLAUDE.md**: Absolute invariants and sovereignty rules
- **rules/sub/**: Procedural logic and workflow guidance
- **skills/**: Pure capability definitions with appropriate tool restrictions

---

## 📋 COMMANDS REFERENCE

### **Project Foundation Commands**

#### `/startprojectplanning`
**Purpose**: Guided project initialization replacing casual development approach
**Workflow**: Stakeholder interviews → keygoals.md → architecture.md → projectimplementationplan.md
**Quality Gates**: Foundation completeness validation
**Output**: Professional foundation establishment with structured documentation

### **Sprint Planning Commands**

#### `/startsprintplanning`
**Purpose**: 5-phase sprint planning with comprehensive quality gates
**Phases**:
1. Initial Plan Generation (APPROVE_INITIAL_DRAFT)
2. Architectural Analysis (APPROVE_ARCHITECTURAL_ANALYSIS)
3. Decision Finalization (APPROVE_FINAL_PLAN)
4. Testing Integration (APPROVE_TESTING_STRATEGY)
5. Final Validation (APPROVE_SPRINT_PLAN)
**Quality Assurance**: planning-qa-specialist executes 10-gate checklist
**Output**: Complete sprint plan with all quality gates validated

#### `/startnewsprint [optional_sprint_name]`
**Purpose**: Sprint execution boundary establishment with immutable manifesto
**Validation**: Planning checklist completed requirement
**Manifesto Creation**: Immutable token preventing "Loss of Intent"
**Boundaries**: File scope locking for professional execution isolation
**Output**: Execution-ready sprint with established boundaries

### **Execution Commands**

#### `/implement [optional_sprint_id]`
**Purpose**: Professional execution engine with Ralph Wiggum resilience
**Sprint Validation**: Active sprint and manifesto verification
**Ralph Wiggum Integration**: Promise tag enforcement (<promise>SANITY_CHECK_PASS</promise>)
**Iteration Management**: 10-iteration safety bound with human escalation
**Boundary Enforcement**: Operations restricted to manifesto scope
**Output**: Complete feature implementation with quality validation

### **Sprint Management Commands**

#### `/listsprints`
**Purpose**: Visual sprint dashboard with comprehensive management interface
**Display**: Active sprints (green), completed sprints (grey), reverse chronological
**Features**: Status indicators, quick actions, ASCII dashboard, lifecycle states
**Quick Actions**: Continue sprint, view plan, end sprint, abandon sprint
**Output**: Professional sprint management interface with actionable controls

#### `/projectstatus`
**Purpose**: Comprehensive project status dashboard for session resumption
**Sections**:
- Project Overview: Foundation status, active sprint, current phase
- Sprint Status: Phase, iteration progress, boundary enforcement
- Planning Checklist: Real-time 10-gate validation with timestamps
- Blockage Detection: Incomplete requirements identification
- Recommended Actions: Contextual next-step guidance
- Quick Stats: Sprint metrics and quality scores
**Output**: Human-readable project visibility enabling professional workflow management

#### `/endsprint`
**Purpose**: Professional sprint completion with cleanup and documentation
**Workflow**: Human acceptance → orphaned code detection → documentation updates → postmortem
**Cleanup Sweep**: ls -R vs git status comparison with intelligent classification
**Documentation**: keygoals.md/architecture.md evolution with sprint learnings
**Postmortem**: Comprehensive sprint retrospective and lessons learned
**Output**: Clean sprint completion with captured knowledge and maintained hygiene

### **Recovery Commands**

#### `/restoreralphwiggam`
**Purpose**: Intelligent recovery from CLAUDE.md overwrites with registry priority
**Priority Logic**: PROJECT_REGISTRY.json → documentation scan → invariant reconstruction
**Recovery Levels**: FULL (complete restoration), PARTIAL (foundation rebuilt), MINIMAL (core physics)
**Promise Tags**: <promise>RECOVERED</promise>, <promise>PARTIAL</promise>, <promise>MINIMAL</promise>
**Output**: System restoration with confidence level reporting and capability assessment

---

## 🏃 PROJECT JOURNEYS - COMPLETE USER EXPERIENCES

### **Journey 1: Single Sprint Project**
```
1. /startprojectplanning     → Establish project foundation
2. /startsprintplanning      → Complete planning with quality gates
3. /startnewsprint user_auth → Create & activate sprint
4. /implement               → Execute Ralph Wiggum loops
5. /endsprint               → Complete with cleanup
```

### **Journey 2: Multi-Sprint Project with Active Sprint Management**
```
Foundation Phase:
├── /startprojectplanning → Project foundation established

Sprint 1 Planning & Execution:
├── /startsprintplanning → Plan completed, all 10 gates passed
├── /startnewsprint user_auth → sprint_user_auth_v1 created & ACTIVE
├── /implement → Ralph Wiggum execution begins
├── [Work progresses to iteration 3, testing phase]

Parallel Sprint 2 Planning:
├── /startsprintplanning → Plan sprint 2 while sprint 1 executes
├── /startnewsprint payment_flow → sprint_payment_flow_v1 created as PLANNED
├── /listsprints → Shows: user_auth (🔄 ACTIVE), payment_flow (📋 PLANNED)

Sprint Switching:
├── /implement sprint_payment_flow_v1 → Switches active sprint
├── sprint_user_auth_v1 → PAUSED (progress preserved)
├── sprint_payment_flow_v1 → ACTIVE, fresh execution starts

Sprint Resume:
├── /implement sprint_user_auth_v1 → Switches back to paused sprint
├── "Resuming from iteration 3, testing phase. Continue? [Y/n]"
├── User: y → Continues from exact interruption point

Completion:
├── /endsprint (user_auth active) → Cleanup, postmortem, completion
├── Auto-prompt: "Activate sprint_payment_flow_v1? [Y/n]"
```

### **Journey 3: Sprint Interruption & Resume**
```
Active sprint: sprint_user_auth_v1 at iteration 3, coding phase

1. [System interruption - browser crash, restart, etc.]
2. /projectstatus
   ├── Shows: "Active Sprint: sprint_user_auth_v1"
   ├── "Last activity: iteration 3, coding phase"
   ├── "Status: Interrupted - resume available"

3. /implement
   ├── "Found interrupted sprint with saved progress"
   ├── "Resuming from iteration 3, coding phase. Continue? [Y/n]"
   ├── User confirms → Continues Ralph Wiggum from coding phase
   ├── Completes: coding → testing → evaluation → iteration 4

4. /projectstatus → Shows resumed progress and current status
```

### **Journey 4: Planning Resume After Interruption**
```
Context: Planning interrupted during architectural analysis (phase 2/5)

1. /startsprintplanning
   ├── Detects: "Incomplete planning found"
   ├── Shows: "Last completed: initial draft"
   ├── "Resuming from architectural analysis phase"

2. Continues from architectural analysis:
   ├── Code location analysis ✅
   ├── Duplication elimination ✅
   ├── Architecture preservation ✅
   └── Remaining phases complete

3. Final approval: APPROVE_SPRINT_PLAN
4. Ready for: /startnewsprint [name]
```

### **Journey 5: Disaster Recovery & System Restoration**
```
Context: CLAUDE.md accidentally overwritten, system state lost

1. /restoreralphwiggam
   ├── "PROJECT_REGISTRY.json intact - registry priority recovery"
   ├── Reconstructs CLAUDE.md invariants from registry
   ├── Restores all sovereignty rules and physics
   ├── Output: <promise>RECOVERED</promise>

2. /projectstatus
   ├── Shows: "System recovered - all state preserved"
   ├── Displays: Active sprint, foundation status, project health

3. /implement
   ├── Detects: "Sprint progress preserved during recovery"
   ├── "Resuming from last saved state. Continue? [Y/n]"
   ├── Continues professional development seamlessly
```

### **Active Sprint Management Principles**
- **Single Active Sprint:** Only one sprint executes Ralph Wiggum loops at a time
- **State Transitions:** planned → active → paused → completed
- **Activation Methods:** `/listsprints` [Activate] or `/implement [sprint_id]`
- **Resume Safety:** Paused sprints preserve exact execution state
- **Clear Status:** `/projectstatus` always shows active sprint context
- **Switching Confirmation:** System prompts before changing active sprint

---

## 🤖 SKILLS REFERENCE

### **Foundation & Planning Skills**

#### `foundation-specialist`
**Purpose**: Guided project foundation establishment
**Capabilities**: Stakeholder interviews, documentation creation, quality validation
**Tools**: read, grep, run_terminal_cmd (foundation-appropriate)
**Model**: opus-4.5 (complex stakeholder interactions)
**Integration**: Updates PROJECT_REGISTRY.json.foundation.complete = true

#### `sprint-planning-specialist`
**Purpose**: Multi-phase sprint planning orchestration
**Capabilities**: 5-phase workflow management, APPROVE_* gate handling, quality integration
**Tools**: read, grep, run_terminal_cmd (planning-appropriate)
**Model**: opus-4.5 (complex multi-phase orchestration)
**Integration**: Manages PROJECT_REGISTRY.json planning_checklist state

#### `planning-qa-specialist`
**Purpose**: Comprehensive planning quality assurance execution
**Capabilities**: 10-gate checklist validation, evidence-based assessment, gap identification
**Tools**: read, grep, run_terminal_cmd (validation-appropriate)
**Model**: opus-4.5 (deep architectural analysis)
**Integration**: Updates PROJECT_REGISTRY.json planning_checklist.completed

### **Execution Skills**

#### `coder`
**Purpose**: Sprint-aware code implementation with boundary enforcement
**Capabilities**: TDD execution, boundary validation, progress tracking, promise management
**Tools**: read, grep, run_terminal_cmd, edit (sprint-scoped)
**Model**: opus-4.5 (complex implementation)
**Integration**: Updates PROJECT_REGISTRY.json execution_context

#### `tester`
**Purpose**: Sprint-scoped testing with artifact isolation
**Capabilities**: Boundary-constrained testing, UI validation, artifact management, promise enforcement
**Tools**: run_terminal_cmd, grep, read (testing-appropriate)
**Model**: opus-4.5 (comprehensive validation)
**Integration**: Manages sprint-specific test artifacts and results

#### `evaluator`
**Purpose**: Sprint context evaluation with quality gate enforcement
**Capabilities**: Boundary-aware assessment, SANITY_CHECK_PASS validation, progress tracking
**Tools**: read, grep, run_terminal_cmd (evaluation-appropriate)
**Model**: opus-4.5 (architectural assessment)
**Integration**: Updates PROJECT_REGISTRY.json evaluation results

### **Support & Management Skills**

#### `recovery-specialist`
**Purpose**: Intelligent system restoration from disruptions
**Capabilities**: Registry priority analysis, state reconstruction, graceful degradation
**Tools**: read, grep, run_terminal_cmd (recovery-appropriate)
**Model**: default (reliable restoration)
**Integration**: Maintains PROJECT_REGISTRY.json integrity across recovery scenarios

#### `cleanup-specialist`
**Purpose**: Orphaned code detection and artifact management
**Capabilities**: Directory scanning, classification, human approval workflow, hygiene maintenance
**Tools**: run_terminal_cmd, read, grep (cleanup-appropriate)
**Model**: default (reliable maintenance)
**Integration**: Updates PROJECT_REGISTRY.json cleanup execution status

#### `discipline-enforcer`
**Purpose**: Professional workflow enforcement and compliance validation
**Capabilities**: Foundation gate monitoring, sovereignty enforcement, practice reinforcement
**Tools**: read (enforcement-appropriate)
**Model**: default (reliable compliance)
**Integration**: Active enforcement during all professional OS operations

#### `project-status-analyst`
**Purpose**: Comprehensive project dashboard generation
**Capabilities**: State parsing, status reporting, blockage detection, action recommendations
**Tools**: read (analysis-appropriate)
**Model**: default (reliable reporting)
**Integration**: Real-time PROJECT_REGISTRY.json interpretation

#### `user-guidance-specialist`
**Purpose**: Contextual workflow assistance and professional education
**Capabilities**: Command enhancement, error recovery guidance, workflow navigation
**Tools**: read (guidance-appropriate)
**Model**: default (reliable assistance)
**Integration**: Enhances all command outputs with contextual guidance

---

## 🔄 WORKFLOW DIAGRAMS

### **Complete Artisan Operating System Workflow**
```
FOUNDATION PHASE
/startprojectplanning
    ↓ (foundation.complete = true)
/startsprintplanning
    ↓ (APPROVE_SPRINT_PLAN)
/startnewsprint
    ↓ (manifesto_locked = true)
EXECUTION PHASE
/implement
    ↓ (SANITY_CHECK_PASS)
/endsprint
    ↓ (cleanup + documentation)
RECOVERY (as needed)
/restoreralphwiggam
    ↓ (system restoration)
MONITORING
/projectstatus, /listsprints
    ↓ (continuous visibility)
```

### **Sprint Planning Quality Gates**
```
Phase 1: Initial Draft → APPROVE_INITIAL_DRAFT
Phase 2: Architectural Analysis → APPROVE_ARCHITECTURAL_ANALYSIS
    ├── Goals Clarity ✅
    ├── Code Location ✅
    ├── Duplication Elimination ✅
    ├── Architecture Preservation ✅
    ├── Step-by-Step Execution ✅
    ├── Strategic Logging ✅
    ├── Dependency Management ✅
    ├── UI-First Design ✅
    ├── Architectural Decisions ✅
    └── Testing Integration ✅
Phase 3: Decision Finalization → APPROVE_FINAL_PLAN
Phase 4: Testing Strategy → APPROVE_TESTING_STRATEGY
Phase 5: Final Validation → APPROVE_SPRINT_PLAN
```

### **Execution Boundary Enforcement**
```
PROJECT_REGISTRY.json.sprints.active
├── manifesto_locked: true
├── locked_files: [...]
└── execution_context: {...}

File Operations → Boundary Check → ALLOWED/BLOCKED
Command Execution → Context Validation → ALLOWED/BLOCKED
Promise Tags → Enforcement → Loop Control
```

---

## 🛡️ QUALITY GATES & BLOCKING MECHANISMS

### **Foundation Gate**
**Trigger**: Any development operation when foundation.incomplete
**Mechanism**: safety_pre_tool.py blocks write/edit operations
**Resolution**: Complete /startprojectplanning
**Purpose**: Prevents #1 project failure cause

### **Planning Checklist Enforcement**
**Trigger**: /startnewsprint with incomplete planning
**Mechanism**: Validation against PROJECT_REGISTRY.json planning_checklist
**Resolution**: Complete /startsprintplanning quality gates
**Purpose**: Ensures comprehensive planning before execution

### **Sprint Boundary Enforcement**
**Trigger**: File operations outside locked_files scope
**Mechanism**: safety_pre_tool.py boundary validation
**Resolution**: Operate within manifesto boundaries
**Purpose**: Prevents scope creep and maintains execution focus

### **Ralph Wiggum Promise Enforcement**
**Trigger**: /implement execution without completion markers
**Mechanism**: Hook validation of <promise>SANITY_CHECK_PASS</promise>
**Resolution**: Generate proper completion markers
**Purpose**: Prevents 70% of execution loop failures

### **Workflow Sequence Enforcement**
**Trigger**: Out-of-order command execution
**Mechanism**: State validation in safety_pre_tool.py
**Resolution**: Follow professional workflow sequence
**Purpose**: Maintains structured development discipline

---

## 📊 STATE MANAGEMENT

### **PROJECT_REGISTRY.json Structure**
```json
{
  "foundation": {
    "complete": true,
    "keygoals_hash": "a1b2c3...",
    "architecture_hash": "d4e5f6...",
    "sprint_roadmap": ["sprint_001", "sprint_002"]
  },
  "planning_checklist": {
    "completed": true,
    "validation_report": {
      "goals_clarity": {"status": "passed", "timestamp": "2026-01-10T10:30:00Z"},
      // ... 9 more gates
    },
    "final_assessment": {
      "confidence_score": 9,
      "gaps_identified": [],
      "ready_for_execution": true
    }
  },
  "sprints": {
    "active": {
      "id": "2026-01-10_sprint_001",
      "phase": "execution",
      "manifesto_locked": true,
      "locked_files": ["src/feature.py", "tests/test_feature.py"],
      "iteration": 3,
      "max_iterations": 10,
      "execution_context": {
        "current_step": "testing",
        "progress_markers": {"tests_written": true, "implementation_complete": true},
        "promise_tags_validated": ["READY_FOR_TESTER", "READY_FOR_EVALUATOR"]
      }
    },
    "history": [
      {
        "id": "2026-01-09_sprint_foundation",
        "status": "completed",
        "postmortem_path": "documentation/postmortems/2026-01-09_postmortem.md",
        "cleanup_executed": true
      }
    ]
  },
  "metadata": {
    "version": "1.0",
    "created": "2026-01-10T00:00:00Z",
    "last_modified": "2026-01-10T12:00:00Z"
  }
}
```

### **State Synchronization Requirements**
- **Every Command**: Begins with PROJECT_REGISTRY.json read
- **Status Output**: Displays "OS_STATUS: Project [Name] | Sprint [ID] | Phase [Phase]"
- **State Updates**: Commands update registry with progress and completion status
- **Integrity Checks**: Registry corruption triggers recovery mechanisms

---

## 🔧 SETUP & DEPLOYMENT

### **Standard Setup**
```bash
export CC_DESTINATION=/path/to/your/project
./claude_code/setup/scripts/setup.sh
```

### **Recovery Setup**
```bash
export CC_DESTINATION=/path/to/your/project
./claude_code/setup/scripts/setup.sh --restore
```

### **Post-Setup Initialization**
```bash
cd $CC_DESTINATION
/startprojectplanning    # Establish professional foundation
```

### **Verification**
- PROJECT_REGISTRY.json created and valid
- .claude/ directory with all commands and skills
- CLAUDE.md with sovereignty rules
- All hooks and safety mechanisms operational

---

## 🚨 TROUBLESHOOTING GUIDE

### **Common Issues**

#### **"System Lock: Project foundation not established"**
**Cause**: Attempting development before foundation completion
**Solution**: Run /startprojectplanning to establish project foundation
**Prevention**: Always complete foundation before development work

#### **"Sprint blocked: Planning checklist incomplete"**
**Cause**: Attempting sprint creation without complete planning
**Solution**: Run /startsprintplanning to complete all quality gates
**Prevention**: Ensure all 10 planning quality gates pass before sprint execution

#### **"Sprint boundary violation"**
**Cause**: File operations outside established manifesto scope
**Solution**: Operate only within sprint locked_files boundaries
**Prevention**: Review sprint manifesto before execution operations

#### **"Maximum iterations reached"**
**Cause**: Complex features exceeding 10-iteration safety bound
**Solution**: Use --escalate-iterations flag for human override
**Prevention**: Break complex features into smaller, focused sprints

#### **"Registry corruption detected"**
**Cause**: PROJECT_REGISTRY.json file corruption or loss
**Solution**: Run /restoreralphwiggam or ./setup.sh --restore
**Prevention**: Avoid manual editing of PROJECT_REGISTRY.json

### **Recovery Procedures**

#### **CLAUDE.md Overwrite Recovery**
1. Run /restoreralphwiggam
2. Verify recovery confidence level (FULL/PARTIAL/MINIMAL)
3. Check system functionality post-recovery
4. Resume professional workflow

#### **Registry Corruption Recovery**
1. Execute ./setup.sh --restore
2. Verify PROJECT_REGISTRY.json reconstruction
3. Confirm system state restoration
4. Continue with professional workflows

#### **Sprint State Recovery**
1. Check /projectstatus for current state
2. Use /listsprints to identify active sprints
3. Resume execution with appropriate commands
4. Complete sprint with /endsprint if needed

---

## 💡 BEST PRACTICES & TIPS

### **Professional Workflow Discipline**
- **Always start with foundation**: /startprojectplanning prevents superficial setup
- **Complete planning thoroughly**: All 10 quality gates ensure execution success
- **Respect boundaries**: Stay within manifesto scope for focused execution
- **Use promise tags**: Proper completion markers prevent loop failures
- **Maintain hygiene**: Regular cleanup prevents artifact accumulation

### **Quality Assurance Practices**
- **TDD enforcement**: Tests first, implementation second
- **Strategic logging**: Surgical points, not excessive butter-spreading
- **Session context**: Unified get_db_session_context() usage
- **Architecture alignment**: Follow established patterns and constraints
- **Code review**: Professional evaluation before completion acceptance

### **State Management Best Practices**
- **Never edit PROJECT_REGISTRY.json manually**: Use commands for state changes
- **Regular status checks**: /projectstatus provides workflow visibility
- **Clean sprint completion**: /endsprint maintains repository hygiene
- **Recovery readiness**: Keep system recoverable with registry priority

### **Performance Optimization**
- **Work in MAIN branch**: No feature branches for professional workflows
- **Async operations**: Use async/await for proper session management
- **Dependency management**: Update pyproject.toml for proper integration
- **Minimal overhead**: Artisan's Operating System adds minimal development friction

### **Team Collaboration**
- **Shared foundation**: All team members work within established project context
- **Sprint isolation**: Concurrent sprints maintain proper boundaries
- **Documentation evolution**: Sprint completions update global knowledge
- **Postmortem reviews**: Lessons learned improve future sprint execution

---

## 🎯 CONCLUSION

Artisan's Claude Code Operating System transforms AI-assisted development from casual experimentation into **enterprise-grade professional workflows**. Through enforced project foundation, comprehensive sprint management, quality gate enforcement, and intelligent recovery, the system prevents the major causes of project failure while maintaining the flexibility and power of AI assistance.

**The result**: A development environment where professional discipline is invisible yet omnipresent, enabling teams to deliver high-quality software through structured, repeatable processes that scale from individual developers to enterprise teams.

**Ready for professional development excellence.** 🚀✨

### **Sprint Engine Benefits**
- **🎯 Focused Work**: Each sprint has clear goals and boundaries
- **🔄 Iterative Improvement**: Ralph Wiggum loops ensure perfection
- **🛡️ Quality Assurance**: Reality Auditor prevents false victories
- **📊 Progress Tracking**: Always know where you stand
- **🔒 Safety First**: Enterprise-grade security and isolation
- **👥 Team Scaling**: Multiple sprints can run in parallel

---

## 🎁 What You Get

### **12 AI Specialists with Sprint Focus**
- **Planner**: Creates sprint plans with hydration validation
- **Coder**: Writes code within sprint boundaries
- **Tester**: Tests with sprint-scoped validation
- **Evaluator**: Reviews with confidence scoring
- **Sanity Checker**: Reality Auditor for UI/data integrity
- **Architect Reviewer**: Ensures architectural consistency
- **QA Enforcer**: Eliminates open architectural choices
- **UI Validator**: Tests visual regression and accessibility
- **Dependency Researcher**: Evaluates external libraries
- **Self-Assessor**: Automated quality scoring (0-100)
- **Skeptic**: Challenges assumptions with evidence
- **Async Optimizer**: Performance and concurrency optimization

### **Sprint Engine Infrastructure**
- **SPRINT_STATE.json**: Automatic sprint lifecycle management
- **Sprint Discovery**: Intelligent active sprint identification
- **Artifact Management**: Organized temp storage with cleanup
- **Boundary Enforcement**: Stateful fail-closed security
- **Context Pruning**: Clean phase transitions with manifesto generation

### **Global Context, Local Execution**
- **Smart Memory (CLAUDE.md)**: <15 lines of absolute invariants
- **Three-Tier Rules System**: CLAUDE.md → 7 main rules → 16 sub-rules
- **Plan Hydration**: Automatic context pulling with validation gates
- **Stateful Enforcement**: Worktree isolation and repair scope locking
- **Context Reset Protocol**: Manifesto generation between phases

### **Enterprise-Grade Quality**
- **Ralph Wiggum Loops**: Iterative perfection with progress tracking
- **Reality Auditor**: Prevents "Victory Too Early" with SANITY_CHECK_PASS
- **Data Integrity Rubrics**: Nonsense prevention for UI/API features
- **Hook Denial Recovery**: Graceful handling of security blocks
- **Audit Logging**: Complete operation traceability

### **Human-Centric Design**
- **Approval Gates**: Human control at all major decisions
- **Context Pruning**: Mandatory /clear for memory management
- **Progress Transparency**: Real-time sprint status and completion tracking
- **Error Recovery**: Self-healing with human escalation paths
- **Parallel Development**: Multiple sprints with safe coordination

---





## 🏗️ THREE-TIER RULES SYSTEM

Your AI team operates within a sophisticated hierarchical rules system that ensures consistency, quality, and efficiency:

### Core Layer: CLAUDE.md (Absolute Invariants)
**What it contains**: Non-negotiable physics-level rules that cannot change
- Database integrity (no resets/drops/duplicates, use get_db_session_context())
- Git safety (no writes, read-only operations only)
- Human sovereignty (architectural decisions require approval)
- Worktree boundaries (agents stay within project scope)

### Main Rules Layer: 7 Task-Specific Rules
**When loaded**: Conditionally based on workflow phase and task requirements

#### Planning & Discovery Rules
- **`project-discovery.md`** - Forces ingestion of existing architectural docs before planning
- **`tdd-enforcer.md`** - Ensures test-driven development gates throughout workflow

#### Architecture & Quality Rules
- **`dependency-integrator.md`** - Manages external libraries and API integrations
- **`architect-reviewer.md`** - Validates architectural consistency and patterns
- **`confidence-booster.md`** - Automated quality improvement for low-confidence outputs

#### Implementation Rules
- **`checklist-polisher.md`** - Applies comprehensive quality checklists
- **`cover-letter-generator.md`** - Creates dev handoffs for Ralph Wiggum loops

### Sub-Rules Layer: 16 Detailed Specializations
**When loaded**: Only when specific conditions are met, minimizing token usage

#### Development Standards
- **`core_invariants.md`** - Operational procedures (async patterns, logging, error handling)
- **`tdd_examples.md`** - Test structure templates and patterns
- **`async_patterns.md`** - Concurrency and performance optimization
- **`arch_basics.md`** - Fundamental architectural patterns

#### Quality Assurance
- **`confidence_check.md`** - 0-100 scoring rubric for output validation
- **`common_checks.md`** - Shared validation patterns (logging, errors, performance)
- **`polish_checklist.md`** - Comprehensive quality improvement checklists
- **`phase_markers.md`** - Standardized markers for plan progression

#### External Integration
- **`dependency_licenses.md`** - License compatibility validation
- **`dependency_security.md`** - Security vulnerability assessment
- **`external_verification.md`** - API and external service validation

#### UI & Testing
- **`ui_debug_modes.md`** - Browser testing and debug configurations
- **`tool_wildcards.md`** - Advanced tool permission patterns
- **`error_patterns.md`** - Error handling and recovery patterns
- **`doc_revision_rules.md`** - Documentation update guidelines
- **`hook-denial-recovery.md`** - Security violation response protocols

### How the Rules System Works
1. **CLAUDE.md loads automatically** - Core invariants available in every session
2. **Main rules load conditionally** - Based on workflow phase (planning, implementation, etc.)
3. **Sub-rules load on-demand** - Only when specific expertise needed
4. **Token efficiency** - Rules load hierarchically to minimize context usage
5. **Quality enforcement** - Rules ensure architectural consistency and code quality

---



## 🏃‍♂️ WORKING WITH SPRINTS: Complete Development Lifecycle

### **Sprint Engine for Beginners**

The Sprint Engine manages development in focused, time-boxed cycles. Think of each sprint as a "development story" with clear beginning, middle, and end.

#### **Phase 1: Sprint Planning (Set Your Goals)**
**What happens**: AI team analyzes your request and creates a detailed plan
**What you do**: Review and approve the plan
**Commands**:
```bash
/implement "build a user login system"
/hydrate-plan  # (automatically runs) pulls global context
APPROVE_PLAN   # Type this when ready
```

#### **Phase 2: Sprint Execution (Build the Feature)**
**What happens**: AI team writes code, tests, and validates
**What you do**: Approve at quality gates, use `/clear` when prompted
**What you'll see**:
```
🧹 Memory cleared. Ready for next phase.
⚠️ HUMAN APPROVAL NEEDED: APPROVE_CODE_WRITE
🔄 Ralph Wiggum: Entering iterative refinement mode
✅ READY_FOR_TESTER (iteration 1)
🧪 Testing phase...
✅ SANITY_CHECK_PASS - UI validation complete
🎉 EVALUATION_COMPLETE - Feature ready!
```

#### **Phase 3: Sprint Completion (Wrap Up & Learn)**
**What happens**: AI captures learnings, updates global documentation
**What you do**: Review final results
**Commands**:
```bash
/close-sprint  # Marks sprint complete, triggers updates
```

### **Sprint Lifecycle Best Practices**

#### **🎯 Start Small, Think Big**
- **First Sprint**: Start with something simple like "add a contact form"
- **Build Confidence**: Each successful sprint teaches you the flow
- **Scale Up**: Use learnings to tackle bigger features

#### **📝 Plan Your Sprints**
- **Clear Descriptions**: "build user registration with email verification" (good)
- **Avoid Vague**: "make the app better" (too vague)
- **Scope Appropriately**: One main feature per sprint
- **Include Context**: Mention existing features to integrate with

#### **🔄 Master the Approval Flow**
```bash
# Pattern: Command → Review → Approve → Clear → Continue
/implement "your feature"
/* READ the generated plan carefully */
/* ASK questions if anything unclear */
APPROVE_PLAN
/clear  # Always do this when prompted!
/* Continue with next approvals */
APPROVE_CODE_WRITE
/clear
APPROVE_EVALUATION
```

#### **🧠 Context Management is Critical**
- **`/clear` is your friend**: Always type it when Claude prompts
- **Why it matters**: Prevents confusion between planning and coding
- **What happens**: Fresh start with only current phase context
- **When forgotten**: Claude might mix up ideas from different phases

#### **📊 Monitor Progress**
- **Check Status**: Files appear in `documentation/plans/`
- **Watch for Signals**:
  - ✅ `READY_FOR_TESTER` - Code implementation complete
  - ✅ `SANITY_CHECK_PASS` - UI/Data validation successful
  - ✅ `EVALUATION_COMPLETE` - Sprint finished successfully
  - 🔄 `Ralph Wiggum: Entering iterative refinement` - Auto-improvement active

#### **🚨 Handle Issues**
- **Stuck?**: Use `/repair "describe the problem"`
- **Complex debugging**: Use `/debug-issue "problem description"`
- **Plan validation**: Use `/test-plan` before major approvals
- **Wrong direction**: `/abandon-sprint` and start over

#### **👥 Scale to Multiple Features**
```bash
# Terminal 1: Backend sprint
/implement "build API endpoints"
/close-sprint

# Terminal 2: Frontend sprint (new terminal)
/clear
/implement "build user interface"
```

#### **📚 Learn from Each Sprint**
- **Review Results**: Check what was built in `temp/claudecode/[sprint_id]/`
- **Read Updates**: See how global docs improved in `documentation/main/`
- **Build Knowledge**: Each sprint makes the AI team smarter about your project

### **Sprint Engine Mindset**

#### **Think in Stories**
- Each sprint tells a complete development story
- Beginning: Clear requirements and planning
- Middle: Focused execution with quality gates
- End: Production-ready feature with documentation updates

#### **Trust the Process**
- **AI handles complexity**: You focus on direction and approvals
- **Quality is built-in**: Automated testing and validation
- **Mistakes are caught**: Multiple review layers prevent issues
- **Learning happens**: Each sprint improves the system

#### **Human + AI Partnership**
- **You provide**: Direction, approvals, business context
- **AI provides**: Technical execution, quality assurance, consistency
- **Together**: Professional-grade software development

---

## 🤖 INTERACTIVE SETUP (Guided Installation)

**Want the setup to ask you questions and customize based on your project? Use the interactive script!**

```bash
# Run the interactive setup script
./scripts/setup-interactive.sh
```

**What it does:**
- ✅ **Asks about your project type** (new or existing)
- ✅ **Gathers project information** (tech stack, documentation location, etc.)
- ✅ **Customizes the installation** based on your answers
- ✅ **Sets up documentation structure** intelligently
- ✅ **Provides personalized guidance** for next steps

**Perfect for:**
- First-time users who want guidance
- Complex projects with custom documentation structures
- Teams that want tailored setup recommendations

**Takes about 3-5 minutes** with questions and customization.

**Example interaction:**
```bash
$ ./scripts/setup-interactive.sh

🚀 CLAUDE CODE INTERACTIVE SETUP
This guided setup will ask you questions...

❓ Are you setting up Claude Code for a NEW project or EXISTING project? [existing]: existing
❓ What is the full path to your project directory? [/current/path]:
❓ Does your project have existing documentation? [Y/n]: y
❓ Where is your documentation folder? [docs]: docs/api
❓ What is your primary tech stack? [Python]: Python/FastAPI
❓ Is this project using Git? [Y/n]: y
❓ Do you want worktree isolation for parallel development? [Y/n]: y
❓ Enable debug mode for development? [y/N]: n
❓ Enable enterprise security features? [Y/n]: y
❓ Enable comprehensive audit logging? [Y/n]: y

✅ Setup completed successfully!
```

---

## 🚀 AUTOMATED SETUP (Works for Both New & Existing Projects)

**Want it done in 30 seconds with no questions? Use the automated script!**

```bash
# 1. Clone the setup repository
git clone <repository-url> claude-code-setup
cd claude-code-setup

# 2. Set your project location
export CC_DESTINATION=/path/to/your/project  # New or existing project folder

# 3. Run the automated setup
./scripts/setup.sh
```

**What it does automatically:**
- ✅ Copies CLAUDE.md (project memory)
- ✅ Creates all `.claude/` folders and files
- ✅ Sets up 12 AI specialists and complete three-tier rules system (7 main + 16 sub-rules)
- ✅ Creates documentation structure
- ✅ Preserves existing files in existing projects
- ✅ Sets proper permissions and security

---

## 📋 AVAILABLE COMMANDS & WHEN TO USE THEM

### `/implement "feature description"` - MAIN WORKFLOW COMMAND
**When to use**: For building complete features from start to finish
**Why use it**: Orchestrates the entire AI team through planning → coding → testing → evaluation
**What it does**:
- Planner creates detailed implementation plan
- Coder writes production-ready code with tests
- Tester validates with real data and browsers
- Evaluator ensures quality standards
- Human approval gates at each major phase
**Example**: `/implement "add user authentication with email verification"`
**When NOT to use**: For quick fixes or debugging (use `/repair` or `/debug-issue` instead)

### `/repair "what broke"` - TARGETED FIX COMMAND
**When to use**: When something specific is broken and needs fixing
**Why use it**: Provides scoped repair with strict boundaries to prevent unintended changes
**What it does**:
- Isolates the exact problem area
- Applies surgical fixes only within approved scope
- Re-tests the specific functionality
- Maintains data integrity and prevents side effects
**Example**: `/repair "login form validation not working in Firefox"`
**When NOT to use**: For new feature development (use `/implement` instead)

### `/test-plan` - PLAN VALIDATION COMMAND
**When to use**: Before approving implementation to ensure plan quality
**Why use it**: Catches architectural issues, missing requirements, and quality problems early
**What it does**:
- Validates plan completeness and structure
- Checks architectural compliance
- Verifies TDD requirements and testing strategy
- Ensures database safety and human control points
**Example**: `/test-plan` (validates the current PLAN.md in documentation/plans/)
**When NOT to use**: During active development (use as pre-approval check)

### `/debug-issue "problem description"` - SYSTEMATIC DEBUGGING COMMAND
**When to use**: When you need structured debugging with browser verification
**Why use it**: Provides comprehensive debugging methodology beyond basic troubleshooting
**What it does**:
- Enables debug mode and strategic logging
- Reproduces issues with systematic testing
- Uses browser verification and console analysis
- Applies targeted fixes with validation
**Example**: `/debug-issue "API calls failing after deployment"`
**When NOT to use**: For simple syntax errors (ask Claude directly)

### `/collect-knowledge` - KNOWLEDGE INTEGRATION COMMAND
**When to use**: When adding this setup to existing projects with documentation
**Why use it**: Ensures the AI team understands your existing architecture and codebase
**What it does**:
- Reads all files in `documentation/main/`
- Analyzes existing architectural decisions
- Builds context about your project's patterns and conventions
- Makes this knowledge available to all AI team members
**Example**: `/collect-knowledge "Ingest existing project documentation and architectural decisions"`
**When NOT to use**: For new projects (knowledge collection happens automatically during `/implement`)

### `/create-sprint` - SPRINT INITIALIZATION COMMAND
**When to use**: To start a new focused development cycle
**Why use it**: Sets up sprint boundaries, generates global context hash, and initializes state tracking
**What it does**:
- Creates unique sprint ID with timestamp
- Generates SHA256 hash of global documentation
- Initializes SPRINT_STATE.json with boundaries
- Sets up temp directory for sprint artifacts
**Example**: `/create-sprint "build user authentication system"`
**When NOT to use**: During active sprint (use `/switch-sprint` instead)

### `/list-sprints` - SPRINT STATUS COMMAND
**When to use**: To see all sprints and their current status
**Why use it**: Provides overview of development progress and sprint history
**What it does**:
- Shows active sprint with detailed status
- Lists completed and abandoned sprints
- Displays global context synchronization status
- Provides interactive sprint selection guidance
**Example**: `/list-sprints`
**When NOT to use**: When you need to take action (use specific commands instead)

### `/switch-sprint` - SPRINT CONTEXT SWITCHING COMMAND
**When to use**: To change which sprint you're currently working on
**Why use it**: Safely transitions between different development contexts
**What it does**:
- Validates sprint ID and state integrity
- Performs global context reconciliation
- Updates active sprint in SPRINT_STATE.json
- Handles hash mismatch resolution
**Example**: `/switch-sprint 2026-01-09_plan_003_user_auth`
**When NOT to use**: During critical sprint execution (complete current first)

### `/close-sprint` - SPRINT COMPLETION COMMAND
**When to use**: When a sprint is finished and ready for delivery
**Why use it**: Properly completes sprint with handoff and cleanup
**What it does**:
- Performs orphaned code detection
- Triggers architectural evolution updates
- Updates global documentation with learnings
- Finalizes sprint state and moves to history
**Example**: `/close-sprint`
**When NOT to use**: If sprint isn't truly complete (use `/abandon-sprint` instead)

### `/abandon-sprint` - SPRINT CANCELLATION COMMAND
**When to use**: When a sprint needs to be stopped before completion
**Why use it**: Cleanly cancels sprint while preserving artifacts for future reference
**What it does**:
- Documents abandonment reason
- Preserves all artifacts in organized storage
- Updates sprint state to abandoned
- Captures lessons learned for future sprints
**Example**: `/abandon-sprint`
**When NOT to use**: For completed work (use `/close-sprint` instead)

### Step 5: Quick Command Reference

| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/implement "feature"` | **Build complete features** - Full AI team workflow | New development, major features |
| `/repair "issue"` | **Fix specific problems** - Scoped, surgical fixes | Bug fixes, targeted improvements |
| `/debug-issue "problem"` | **Systematic debugging** - Browser testing, root cause analysis | Complex issues, performance problems |
| `/test-plan` | **Plan validation** - Quality check before implementation | Plan review, pre-approval |
| `/collect-knowledge "context"` | **Project integration** - Learn existing architecture | Adding to existing projects |

### Step 6: Understanding Ralph Wiggum - The Iterative Refinement System

**Ralph Wiggum is your AI team's secret weapon for perfection!** 🔄

#### How It Works
After initial implementation, Claude enters **iterative improvement mode**:

```
Planning → Initial Code → Ralph Loop → Perfection
                      ↓
               🔄 ITERATE UNTIL PERFECT 🔄
                      ↓
            Testing → Fixing → Re-testing
```

#### What You'll See
**Progress Tracking:**
```
🤖 Starting feature implementation...
📋 PLAN CREATED: documentation/plans/plan_001.md
⚠️ Type: APPROVE_PLAN
[... planning phases ...]
💻 Code implementation starting...
🔄 Ralph Wiggum: Entering iterative refinement mode
📊 Progress: temp/progress.txt updated
✅ READY_FOR_TESTER (iteration 1)
🧪 Testing phase...
⚠️ Issues found, auto-correcting...
✅ READY_FOR_TESTER (iteration 2)
🔄 Ralph continues until perfect...
🎉 EVALUATION_COMPLETE - Feature ready!
```

#### The Promise/Done Protocol
- **Promise**: "I will implement this feature perfectly"
- **Working**: Active coding and refinement
- **Done**: Feature meets all quality standards
- **Progress**: Tracked in `/temp/progress.txt`

#### Human Control Points
- **Iteration Limits**: Max 50 cycles, human intervention at 40
- **Quality Gates**: Must pass confidence scoring (≥80)
- **Escalation**: Human approval for complex issues
- **Memory Management**: `/clear` commands prevent context drift

#### When Ralph Wiggum Activates
- ✅ After initial `/implement` planning phases
- ✅ During complex feature development
- ✅ When quality issues are detected
- ✅ For performance optimization needs

**Ralph Wiggum means you get enterprise-quality results with minimal human intervention!** 🎯

---

## 🧠 KNOWLEDGE MANAGEMENT SYSTEM

### How the AI Team Learns About Your Project

**For New Projects:**
- The `/implement` command automatically initializes architectural documentation
- AI team creates `documentation/main/` folder with project-specific docs
- Knowledge builds organically as you develop features

**For Existing Projects:**
- Use `/collect-knowledge` to ingest your existing documentation
- Place architectural docs in `documentation/main/` folder
- The AI team reads these files during planning phases

### Key Documentation Locations:
```
documentation/main/
├── proposedarchitecture.md    # Core architectural decisions
├── [api-docs].md             # API patterns and conventions
├── [data-models].md          # Database schemas and patterns
└── [domain-rules].md         # Business logic and constraints
```

### Knowledge Persistence:
- **CLAUDE.md**: Core invariants loaded every session
- **Rules System**: Hierarchical guidance (core → main → sub-rules)
- **Architectural Docs**: Project-specific patterns and decisions
- **Session Context**: Maintained within individual Claude sessions

---


## Step-by-Step Setup (Copy These Files)

### Step 4: Copy the AI Team Instructions
Copy the files that define how each AI specialist behaves.

**Where to put them**: `.claude/skills/` (the skills folder you created)
```bash
# Copy all 12 AI specialist instruction files
cp /path/to/this/setup/.claude/skills/*.md .claude/skills/
```

**What each specialist does**:
- `planner.md` - Creates sprint plans with hydration validation
- `coder.md` - Writes code within sprint boundaries
- `tester.md` - Tests with sprint-scoped validation
- `evaluator.md` - Reviews with confidence scoring
- `sanity-checker.md` - Reality Auditor for UI/data integrity
- `architect-reviewer.md` - Ensures architectural consistency
- Plus 6 more specialists for QA, research, optimization, etc.

### Step 5: Copy Safety Guards
Copy the safety check programs that run automatically before and after Claude Code does anything.

**Where to put them**: `.claude/hooks/` (the hooks folder you created)
```bash
# Copy the safety programs (from the setup repository)
cp /path/to/setup/repo/.claude/hooks/*.py .claude/hooks/

# Make them executable (able to run)
chmod +x .claude/hooks/*.py
```

**What each guard does**:
- `safety_pre_tool.py` - Checks before Claude does anything risky (like deleting files)
- `validation_post_tool.py` - Checks after work is done and catches problems

### Step 6: Copy Special Commands
Copy the custom commands you can type to make the AI team do specific jobs.

**Where to put them**: `.claude/commands/` (the commands folder you created)
```bash
# Copy the command definitions (from the setup repository)
cp /path/to/setup/repo/.claude/commands/*.md .claude/commands/
```

**Commands you can use**:
- `/implement "feature description"` - **PRIMARY**: Builds complete features from planning to deployment
- `/repair "what broke"` - **TARGETED**: Fixes specific issues with surgical precision
- `/test-plan` - **VALIDATION**: Checks plan quality before implementation approval
- `/debug-issue "problem"` - **DEBUGGING**: Systematic debugging with browser verification
- `/collect-knowledge "description"` - **INTEGRATION**: Ingests existing project docs for existing projects

### Step 7: Copy Permission Settings
Copy the settings file that controls what Claude Code can and cannot do automatically.

**Where to put it**: `.claude/settings.json` (in the .claude folder)
```bash
# Copy the permission settings (from the setup repository)
cp /path/to/setup/repo/.claude/settings.json .claude/settings.json
```

**What this controls**:
- Which actions Claude can do without asking (like reading files)
- Which actions need your approval (like changing code)
- Which safety checks run automatically

### Step 8: Create Extra Folders
Make the folders where plans and tests will be stored.

```bash
# Create folders for plans and test scripts
mkdir -p documentation/plans tests/poc_scripts

# Make sure all .claude files can be read/executed
chmod -R 755 .claude/
```

**What these folders are for**:
- `documentation/plans/` - Where the AI team saves their detailed plans
- `tests/poc_scripts/` - Where quick test programs go to verify ideas

## Why This Setup Is Special

This setup uses advanced techniques from the creators of Claude AI:

### Smart Memory System
- **CLAUDE.md**: Automatically loads all your project rules every time
- **No need to repeat instructions**: Claude "remembers" your preferences
- **Faster development**: No explaining rules over and over

### Architectural Documentation
- **Source of Truth**: `/documentation/main/` contains your project's architectural decisions
- **Always Current**: Agents read and update these docs as they work
- **Consistency Guarantee**: Every feature aligns with established patterns
- **Living Documentation**: Architecture evolves with your project

### Team Coordination
- **4 AI specialists**: Each handles one job (plan, code, test, review)
- **They work together**: Hand off work automatically like real developers
- **Architectural Awareness**: All agents consult `/documentation/main/` docs
- **Human control**: You approve every major decision

### Safety First
- **Automatic checks**: Prevents dangerous mistakes before they happen
- **Permission system**: Controls what Claude can do without asking
- **Quality gates**: Forces proper testing and review processes
- **Architectural validation**: Ensures changes align with established patterns
- **Token enforcement**: Workflow tokens must be properly formatted
- **Context monitoring**: Warns when plans get too large for reliable processing
- **Scope validation**: Repair operations validate file paths exist before proceeding

### Parallel Work
- **Multiple Claude instances**: Work on different features simultaneously
- **Git worktrees**: Keep separate code branches organized
- **Code + review at same time**: One Claude codes, another reviews

### Enterprise-Grade Quality Assurance
- **Comprehensive Testing Suite**: Database integrity, workflow execution, security hardening, enterprise features
- **Three-Tier Rules System**: Hierarchical rules for optimal token usage and specialization
- **Automated Quality Assessment**: Self-assessment with confidence scoring and improvement recommendations
- **Skeptical Validation**: Assumption challenging with evidence-based decision making
- **Browser-First Validation**: UI testing with visual regression and accessibility compliance
- **Performance Optimization**: Async patterns, caching, and resource efficiency
- **Dependency Research**: Thorough evaluation of third-party libraries and services

## Architectural Documentation System

Your AI team maintains architectural consistency through a central documentation system:

### The `/documentation/main/` Folder
This folder contains your project's architectural "source of truth":

```
documentation/main/
├── proposedarchitecture.md     # Core architectural decisions
├── [other architectural docs]  # API patterns, data models, etc.
```

### How It Works
- **Planning Phase**: Agents read `proposedarchitecture.md` to align new features
- **Implementation**: Code follows established patterns from these documents
- **Review Phase**: Evaluator checks architectural consistency
- **Evolution**: Documents get updated when new patterns are established

### Key Documents
- **`proposedarchitecture.md`**: Technology choices, design patterns, coding standards
- **API Documentation**: How endpoints should be designed
- **Data Models**: Database schema patterns and conventions

### Why This Matters
- **Consistency**: Every feature follows the same architectural patterns
- **Scalability**: Large teams can work without conflicting approaches
- **Maintenance**: Clear documentation of why decisions were made
- **Evolution**: Architecture grows organically with your project

## Clean Project Structure After Setup

**Your project root stays clean! Only these files exist after setup:**

```
your_project/
├── CLAUDE.md                    # ⚠️ Global context (auto-loaded by Claude)
└── .claude/                     # 🏗️ Complete AI system (all internals here)
    ├── PROJECT_REGISTRY.json    # 📊 Professional OS state management
    ├── settings.json            # ⚙️ Claude Code configuration
    ├── repair_lock.json         # 🔒 HARD repair scope enforcement
    ├── rules/                   # 📋 Rules system (7 main + 16 sub-rules)
    ├── skills/                  # 🤖 20 AI specialists
    ├── commands/                # 🎮 23 professional commands
    └── hooks/                   # 🛡️ Safety & validation systems
```

**No clutter in your project root!** 🎉

**The AI team creates user content through workflow:**
- `documentation/main/` (created by `/startprojectplanning`)
- `documentation/plans/` (created during sprint planning)
- `temp/` (temporary artifacts during development)

**But these are created by you through the professional workflow, not by the setup script.**

## How to Use It

### Step 1: Start Claude Code
Open your terminal/command prompt and start the AI assistant.

```bash
# Go to your project folder
cd your-project-folder

# Start Claude Code
claude
```

You'll see Claude Code start up and show a prompt where you can type commands.

### Step 2: Choose Your Starting Point

**New Project?** Start with architecture setup:
```bash
/implement "Initialize project architecture for a web application"
```

**Existing Project?** First collect knowledge, then implement:
```bash
/collect-knowledge "Integrate existing project documentation"
/implement "Add user authentication to existing app"
```

### Step 3: The AI Team Workflow

When you type `/implement`, your **12 AI specialists** work together in phases:

#### Phase 1: Planning & Architecture 🤔
- **Planner** creates detailed implementation plan
- **Architect Reviewer** validates against existing patterns
- **QA Enforcer** ensures no open architectural decisions
- **Human Approval**: Type `APPROVE_PLAN` to continue

#### Phase 2: Code Implementation 💻
- **Coder** writes production-ready code with tests first
- **Dependency Researcher** validates external libraries
- **Async Optimizer** ensures performance patterns
- **Human Approval**: Type `APPROVE_CODE_WRITE` to continue

#### Phase 3: Quality Assurance 🧪
- **Tester** runs comprehensive tests with real data
- **Sanity Checker** validates UI/data coherence
- **Self-Assessor** provides quality scoring (0-100)
- **Human Approval**: Type `APPROVE_EVALUATION` to continue

#### Phase 4: Ralph Wiggum Iterative Refinement 🔄
**The secret sauce - automated improvement loops!**

After initial implementation, Claude enters **Ralph Wiggum mode**:
- Tracks progress in `/temp/progress.txt`
- Iteratively improves code until perfect
- **Promise → Working → Done** cycle for each refinement
- Self-corrects issues without human intervention
- Maximum 50 iterations with human escalation if needed

**You see markers like:**
```
READY_FOR_TESTER
EVALUATION_COMPLETE
SANITY_CHECK_PASS
```

### Step 4: Key Commands for Different Situations

#### 🚀 `/implement "feature description"` - BUILD COMPLETE FEATURES
**PRIMARY COMMAND** - Your main workflow starter
```bash
/implement "build a user registration system with email verification"
/implement "add shopping cart functionality"
/implement "create admin dashboard with analytics"
```

**Triggers Full AI Team Workflow:**
1. Planning → Architecture → Implementation → Testing → Evaluation
2. Ralph Wiggum iterative refinement for perfection
3. Human approval gates at key decision points

**When to Use:**
- ✅ New feature development
- ✅ Major functionality additions
- ✅ Complete system components

#### 🔧 `/repair "what broke"` - FIX SPECIFIC ISSUES
**When something breaks during or after development**
```bash
/repair "login validation not working in Firefox"
/repair "API endpoint returning 500 errors"
/repair "database connection failing after deployment"
```

**Provides Surgical Fixes:**
- Isolates exact problem scope
- Prevents unintended side effects
- Re-tests only affected functionality
- Hard scope enforcement (can't modify unrelated code)

**When to Use:**
- ✅ After `/implement` reveals issues
- ✅ Production bug fixes
- ✅ Targeted improvements

#### 🔍 `/debug-issue "problem description"` - SYSTEMATIC DEBUGGING
**For complex debugging with browser verification**
```bash
/debug-issue "API calls failing after user login"
/debug-issue "UI not updating after form submission"
/debug-issue "performance degradation on product pages"
```

**Comprehensive Debug Process:**
- Enables debug mode and logging
- Browser console analysis
- Step-by-step issue reproduction
- Root cause identification and fix

**When to Use:**
- ✅ Multi-component issues
- ✅ Browser-specific problems
- ✅ Performance investigations

#### 📋 `/test-plan` - PLAN QUALITY VALIDATION
**Before approving implementation plans**
```bash
/test-plan  # Validates current PLAN.md
```

**Validates Plan Quality:**
- Checks architectural compliance
- Verifies TDD requirements
- Ensures database safety
- Confirms human control points

**When to Use:**
- ✅ After initial plan creation
- ✅ Before major implementation approval
- ✅ When reviewing complex plans

#### 📚 `/collect-knowledge "context description"` - PROJECT INTEGRATION
**For existing projects - gathers and integrates documentation**
```bash
/collect-knowledge "Ingest existing API documentation and architecture"
/collect-knowledge "Learn current database schema and patterns"
/collect-knowledge "Understand existing testing and deployment processes"
```

**Knowledge Integration:**
- Reads `documentation/main/` folder
- Analyzes existing codebase patterns
- Makes architectural knowledge available to all AI specialists
- Updates CLAUDE.md with project-specific context

**When to Use:**
- ✅ Adding to existing projects
- ✅ After significant architectural changes
- ✅ Before complex feature implementations

### Step 5: Understanding Ralph Wiggum - The Iterative Refinement System

**Ralph Wiggum is your AI team's secret weapon for perfection!** 🔄

#### How It Works
After initial implementation, Claude enters **iterative improvement mode**:

```
Planning → Initial Code → Ralph Loop → Perfection
                      ↓
               🔄 ITERATE UNTIL PERFECT 🔄
                      ↓
            Testing → Fixing → Re-testing
```

#### What You'll See
**Progress Tracking:**
```
🤖 Starting feature implementation...
📋 PLAN CREATED: documentation/plans/plan_001.md
⚠️ Type: APPROVE_PLAN
[... planning phases ...]
💻 Code implementation starting...
🔄 Ralph Wiggum: Entering iterative refinement mode
📊 Progress: temp/progress.txt updated
✅ READY_FOR_TESTER (iteration 1)
🧪 Testing phase...
⚠️ Issues found, auto-correcting...
✅ READY_FOR_TESTER (iteration 2)
🔄 Ralph continues until perfect...
🎉 EVALUATION_COMPLETE - Feature ready!
```

#### The Promise/Done Protocol
- **Promise**: "I will implement this feature perfectly"
- **Working**: Active coding and refinement
- **Done**: Feature meets all quality standards
- **Progress**: Tracked in `/temp/progress.txt`

#### Human Control Points
- **Iteration Limits**: Max 50 cycles, human intervention at 40
- **Quality Gates**: Must pass confidence scoring (≥80)
- **Escalation**: Human approval for complex issues
- **Memory Management**: `/clear` commands prevent context drift

#### When Ralph Wiggum Activates
- ✅ After initial `/implement` planning phases
- ✅ During complex feature development
- ✅ When quality issues are detected
- ✅ For performance optimization needs

**Ralph Wiggum means you get enterprise-quality results with minimal human intervention!** 🎯

### Step 7: What You'll Experience

**The AI Team Workflow in Action:**

#### Initial Response
```
🤖 Starting feature implementation: add a login system...

📋 PLAN CREATED: documentation/plans/2025-01-08_plan_001_login_system.md

⚠️  HUMAN APPROVAL NEEDED:
Type: APPROVE_PLAN
```

#### Planning Phases
```
🧹 Memory cleared. Ready for next phase.

🤖 Architect Reviewer: Validating architectural patterns...
✅ QA Enforcer: No open decisions detected
⚠️  HUMAN APPROVAL NEEDED:
Type: APPROVE_FINAL_PLAN
```

#### Ralph Wiggum Iterative Refinement
```
🔄 Ralph Wiggum: Entering iterative refinement mode
📊 Progress tracking: temp/progress.txt

💻 Coder: Writing initial implementation...
🧪 Tester: Running test suite...
⚠️  Issues detected, auto-correcting...

✅ READY_FOR_TESTER (iteration 1)
🔄 Ralph continues improving...

✅ SANITY_CHECK_PASS
🎉 EVALUATION_COMPLETE - Feature production-ready!
```

This continues until the feature is complete!

### Step 4: Fixing Problems
If something breaks during development:

```bash
/repair "login button not working in browser test"
```

**What happens**: Claude will focus only on fixing that specific problem, re-test it, and continue.

### Step 5: Memory Management (Important!)
Claude Code can get "confused" if it remembers too many things at once. Always type `/clear` when Claude tells you to:

```bash
# Example: After approving a plan
APPROVE_PLAN

# Claude will say:
/clear

# You type:
/clear

# Then Claude continues with the next step
```

**Why this matters**: Prevents Claude from mixing up ideas between planning and coding phases.

### Advanced: Multiple Claude Teams (For Big Projects)

For really big features, you can run multiple Claude Code instances at the same time, like having several development teams working in parallel.

#### Method 1: Separate Features
If your big feature has independent parts:

```bash
# Create separate folders for each part
git worktree add ../login-backend backend-login
git worktree add ../login-frontend frontend-login

# Start one Claude for backend work
cd ../login-backend && claude /implement "build login API server"

# Start another Claude for frontend work (in a new terminal)
cd ../login-frontend && claude /implement "build login web page"
```

**Result**: Two Claude teams build different parts at the same time.

#### Method 2: Code + Review at Same Time
One Claude writes code, another Claude reviews it simultaneously:

```bash
# Terminal 1: Claude writes the code
claude "invoke @Coder to implement the login system"

# Terminal 2: Different Claude reviews (open new terminal)
/clear
claude "Review the login code and check for security issues"
```

**Result**: Faster development with built-in code review.

### Security Settings (What Claude Can Do)

Claude Code follows a "secure by default" approach - it asks permission for dangerous actions.

```json
{
  "permissions": {
    "Read": "allow",        // Claude can read files without asking
    "Grep": "allow",        // Claude can search text without asking
    "Glob": "allow",        // Claude can list files without asking
    "Edit": "prompt",       // Claude MUST ask before changing any code
    "Bash": {
      "git status": "allow",    // Safe: just shows git status
      "git diff": "allow",      // Safe: shows changes
      "npm test": "prompt",     // Dangerous: running tests needs approval
      "python -m pytest": "prompt" // Dangerous: running tests needs approval
    }
  }
}
```

**Why these settings?**
- **Reading/Searching: Allowed** - These are safe operations that don't change anything
- **Code Changes: Need Approval** - You must confirm every code edit (the main safety feature)
- **Test Running: Need Approval** - Tests might change databases or files, so you approve them
- **Git Commands: Carefully Controlled** - Read-only git commands are OK, write commands are blocked

### Context Management Best Practices

```bash
# Clear context between major workflow shifts
/clear

# Use checklists for complex multi-step tasks
claude "Create a markdown checklist for the 10-step migration plan"
```

### MCP Integration (Optional)

For advanced UI testing and external integrations, configure MCP servers:

```json
// .mcp.json
{
  "mcpServers": {
    "puppeteer": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-puppeteer"],
      "env": {
        "HEADLESS": "true"
      }
    }
  }
}
```

### Individual Subagent Usage

```bash
# Use subagents directly for specific tasks
claude "delegate to Planner: Plan the database schema for user management"
claude "delegate to Coder: Implement the login API endpoint"
claude "delegate to Tester: Test the user registration flow"
claude "delegate to Evaluator: Review the authentication implementation"
```

## Configuration Customization

### Modifying Global Rules

Edit `CLAUDE.md` to customize operational procedures:

```yaml
global_rules:
  - No database resets/drops/duplicates
  - Async preferred; use get_db_session_context()
  - TDD gates: Tests in /tests/ folder, no mocks, real data
  # Add your project-specific rules here
```

### Adjusting Safety Settings

```yaml
safety:
  protected_files:
    - .env
    - .github/workflows/*.yml
    # Add your protected files
```

### Workflow Tuning

```yaml
workflow:
  max_agent_iterations: 5  # Increase for complex tasks
  human_intervention_timeout: 300  # Seconds to wait for human input
```

## Meet Your AI Team

### Core Development Team

#### The Planner 🤔
**Job**: Creates detailed plans before any coding starts
**What they do**:
- Researches your existing code to understand what you have
- Writes step-by-step plans in `documentation/plans/`
- Makes sure the plan covers everything needed
- Asks you questions to improve the plan

#### The Coder 💻
**Job**: Writes the actual code following the plan
**What they do**:
- Reads the plan and writes code to match it exactly
- Creates tests first, then writes code to pass those tests
- Makes only the changes needed (no extra stuff)
- Shows you exactly what files they changed

#### The Tester 🧪
**Job**: Makes sure everything works correctly
**What they do**:
- Runs all kinds of tests (unit tests, integration tests, UI tests)
- Uses real data, not fake test data
- Checks that the code works in browsers and with databases
- Reports any problems found and how to fix them

#### The Evaluator ✅
**Job**: Final review and quality check
**What they do**:
- Reviews all the code, tests, and results
- Checks that everything meets your standards
- Calculates how complete the work is
- Gives final approval or asks for fixes

### Quality Assurance Specialists

#### The Sanity Checker 🔍
**Job**: Reality auditor for UI/data coherence
**What they do**:
- Performs browser-first validation with visual evidence
- Checks for N/A, NaN, null values in UI and data
- Validates console errors, network failures, and logical consistency
- Issues SANITY_CHECK_PASS tokens based on visual evidence

#### The Architect Reviewer 🏗️
**Job**: Architecture consistency validator
**What they do**:
- Ensures all implementations align with established patterns
- Validates domain boundaries and layer isolation
- Checks SOLID principles and dependency directions
- Prevents architectural drift and maintains consistency

#### The QA Enforcer 🚫
**Job**: Choice elimination enforcer
**What they do**:
- Blocks any output containing unresolved architectural decisions
- Detects forbidden patterns like "could," "might," or "TBD"
- Enforces evidence-based decision making
- Requires definitive yes/no decisions with justifications

#### The UI Validator 🎨
**Job**: UI testing automation specialist
**What they do**:
- Performs visual regression testing and functional validation
- Tests accessibility compliance and cross-browser compatibility
- Measures Core Web Vitals and performance metrics
- Ensures visual accuracy and user experience quality

### Research and Optimization Specialists

#### The Dependency Researcher 🔬
**Job**: External dependency specialist
**What they do**:
- Researches and evaluates third-party libraries and services
- Performs comprehensive market analysis and technical evaluation
- Assesses security, performance, and maintenance viability
- Provides evidence-based recommendations with migration guidance

#### The Self-Assessor 📊
**Job**: Quality self-assessment expert
**What they do**:
- Provides automated code quality scoring (0-100 scale)
- Analyzes structure, readability, maintainability, and reliability
- Generates targeted improvement recommendations
- Tracks quality trends and identifies technical debt

#### The Skeptic 🤨
**Job**: Assumption challenger and validator
**What they do**:
- Challenges unstated assumptions with evidence-based validation
- Performs web research to verify technical and business claims
- Detects cognitive biases in decision-making processes
- Ensures decisions are based on verified facts, not beliefs

#### The Async Optimizer ⚡
**Job**: Performance optimization specialist
**What they do**:
- Identifies I/O-bound and CPU-bound optimization opportunities
- Implements async patterns, caching, and resource management
- Provides performance monitoring and automated recommendations
- Optimizes for concurrency, memory usage, and response times

## Safety Features

### Automatic Guards
The system has safety programs that run automatically:

### Before Actions (Pre-Tool Guard)
- **Stops dangerous commands**: Prevents deleting files, formatting disks, etc.
- **Cache cleanup allowed**: Can delete `__pycache__` and `node_modules/.cache` folders
- **Worktree protection**: Claude can only change files in the current project area
- **File protection**: Important files like `.env` can't be accidentally changed
- **Size limits**: Warns about very large files

### After Actions (Post-Tool Guard)
- **Error detection**: Catches crashes, failed tests, and exceptions
- **Lazy code detection**: Finds placeholder comments like "add code here"
- **Workflow stops**: Prevents continuing if serious problems found
- **Clear feedback**: Tells you exactly what went wrong and what to do

## How the Team Works Together

### The `/implement` Process
When you type `/implement "build a chat app"`, here's what happens:

1. **Planning** 📋
   - Planner creates a detailed plan
   - You review and approve it

2. **Coding** 💻
   - Coder writes the actual code
   - Tests are written first, then code

3. **Testing** 🧪
   - Tester runs all tests and checks everything works
   - Uses real data and browsers

4. **Review** ✅
   - Evaluator checks quality and gives final approval

### What If Something Goes Wrong?
- **Auto-retry**: Failed steps try again automatically
- **Human help**: Serious problems stop and ask for your guidance
- **Fix command**: Use `/repair "what broke"` to fix specific issues
- **Logging**: Everything is tracked so you can see what happened

## Best Practices

### Project Setup
- Always copy the complete setup structure
- Customize CLAUDE.md operational procedures for your project's needs
- Test the setup with a simple feature first

### Workflow Usage
- Use `/implement` for complete features
- Individual subagents for specific tasks
- Review plans before approving implementation
- Never commit without human review

### Maintenance
- Update global rules as project evolves
- Monitor hook effectiveness and adjust safety settings
- Review workflow metrics and optimize iteration limits

## Troubleshooting

### Common Issues

**Subagent not responding**:
- Check YAML syntax in subagent definitions
- Verify file permissions on plugin scripts
- Ensure Claude Code can access .claude directory

**Safety hook blocking valid operations**:
- Review safety context in CLAUDE.md
- Check for false positives in safety patterns
- Adjust safety settings for your environment

**Workflow hanging**:
- Check operational procedures in CLAUDE.md
- Review timeout settings
- Examine logs for stuck operations

**Plan validation failing**:
- Ensure documentation/plans/ directory exists
- Check required sections in PLAN.md format
- Verify file permissions

### Debug Mode

Enable detailed logging by adding to CLAUDE.md operational procedures:
```yaml
debug:
  enable_logging: true
  log_level: DEBUG
  log_file: .claude/debug.log
```

## Metrics and Monitoring

### Built-in Metrics
- Phase completion times
- Error rates and recovery success
- Test coverage and quality scores
- Human intervention frequency

### Monitoring Commands
```bash
# View recent workflow executions
claude "show workflow history"

# Check subagent performance
claude "analyze subagent metrics"

# Review safety hook activity
claude "show safety incidents"
```

## Support and Extension

### Adding Custom Subagents
1. Create new YAML file in `.claude/subagents/`
2. Define role, expertise, and prompt template
3. Add to workflow orchestration if needed

### Creating Custom Commands
1. Create markdown file in `.claude/commands/`
2. Define description and argument hints
3. Include orchestration instructions

### Extending Safety Rules
1. Modify `safety_pre_tool.py` for new validations
2. Update CLAUDE.md safety context with additional protected patterns
3. Test thoroughly before deployment

---

## 🚀 AUTOMATED SETUP (Much Easier!)

**OR YOU CAN DO ALL THIS AUTOMATICALLY** with one command instead of copying files manually!

### Quick Automated Setup

```bash
# 1. Set where you want to install (replace with your project path)
export CC_DESTINATION=/path/to/your/project

# 2. Run the automated setup script
./scripts/setup.sh
```

**What the script does automatically:**
- ✅ Copies CLAUDE.md to your project
- ✅ Creates all `.claude/` folders
- ✅ Copies 12 AI specialist skills
- ✅ Copies 7 main rules + 16 sub-rules
- ✅ Copies safety programs (hooks)
- ✅ Copies special commands
- ✅ Sets up security settings
- ✅ Creates work directories
- ✅ Sets proper permissions
- ✅ Verifies everything worked

**Example usage:**
```bash
# For a project in your home directory
export CC_DESTINATION=~/my-awesome-app
./scripts/setup.sh

# Or for current directory
export CC_DESTINATION=.
./scripts/setup.sh
```

**What you'll see:**
```
ℹ️  Setting up Claude Code environment in: /home/user/my-awesome-app
ℹ️  Step 1: Copying CLAUDE.md (project memory file)...
✅ CLAUDE.md copied to project root
ℹ️  Step 2: Creating .claude directory structure...
✅ .claude directories created
[...more steps...]
🎉 Claude Code Multi-Agent Setup Complete!

What you can do now:
  1. Go to your project: cd /home/user/my-awesome-app
  2. Start Claude: claude
  3. Establish project foundation: /startprojectplanning
```

**That's it!** The script handles all setup steps for you.

---

## 🚀 POST-INSTALLATION: Getting Started Checklist

**After setup is complete, here's how to start using your AI development team:**

### ✅ Step 1: Verify Setup Success
```bash
# Check that all files are in place
find .claude/ -name "*.md" | wc -l  # Should show ~40 files

# Verify Claude Code can access your setup
claude --help
```

### ✅ Step 2: Choose Your Starting Point

**For New Projects:**
```bash
# Initialize project architecture
/implement "Initialize project architecture for a [describe your app type]"
# Follow approval prompts (APPROVE_PLAN, etc.)
```

**For Existing Projects:**
```bash
# First, let AI team learn your existing architecture
/collect-knowledge "Integrate existing project documentation and patterns"

/implement "Add [new feature] to existing [describe your project]"
```

### ✅ Step 3: Learn the Approval Flow
When you run `/implement`, you'll see prompts like:
```
⚠️ HUMAN APPROVAL NEEDED:
Type: APPROVE_PLAN
```
**Always read the plan/docs first, then type the approval command.**

### ✅ Step 4: Master Memory Management
Claude will prompt you to type `/clear` between major phases:
```
🧹 Memory cleared. Ready for next phase.
```
**This prevents context confusion - always do it when instructed!**

### ✅ Step 5: Understand Progress Indicators
Watch for these signs of success:
- ✅ `READY_FOR_TESTER` - Code implementation complete
- ✅ `SANITY_CHECK_PASS` - UI/data validation successful
- ✅ `EVALUATION_COMPLETE` - Feature production-ready
- 🔄 `Ralph Wiggum: Entering iterative refinement mode` - Auto-improvement active

### ✅ Step 6: Know When to Use Each Command

| Situation | Command | Example |
|-----------|---------|---------|
| **New feature** | `/implement "feature"` | `/implement "add user login"` |
| **Bug fix** | `/repair "issue"` | `/repair "login button broken"` |
| **Complex debugging** | `/debug-issue "problem"` | `/debug-issue "API timeout errors"` |
| **Plan review** | `/test-plan` | `/test-plan` |
| **Project integration** | `/collect-knowledge "context"` | `/collect-knowledge "learn existing APIs"` |

### ✅ Step 7: Monitor Quality Gates
Your AI team enforces enterprise standards:
- **Confidence Scores**: Must be ≥80
- **Test Coverage**: Real data testing required
- **Architectural Compliance**: Follows established patterns
- **Security**: No dangerous operations allowed

### ✅ Step 8: Scale to Multiple Features
For bigger projects, run parallel development:
```bash
# Terminal 1: Backend work
claude /implement "build API endpoints"

# Terminal 2: Frontend work (in new terminal)
/clear  # Start fresh
claude /implement "build user interface"
```

### 🎯 Success Indicators
- **Plans created** in `documentation/plans/`
- **Code written** with proper structure
- **Tests passing** with real data
- **Quality scores** ≥80 confidence
- **Human approvals** at appropriate checkpoints

**Remember: You're the human conductor of this AI orchestra. Guide with approvals, but let Ralph Wiggum handle the perfection!** 🎼🤖

---

**Welcome to AI-powered development! Your team of 12 specialists is ready to build production-quality software with you.** 🚀✨

### Manual Setup (Alternative)

If you prefer to do it step by step, follow the detailed instructions above.

## Verify Your Clean Setup

After setup, your project root should contain **only** these items:

```bash
# Check project root (should be clean!)
ls -la
# Expected: CLAUDE.md, .claude/, .git/ (if initialized), .DS_Store (macOS)

# Verify .claude/ structure
ls -la .claude/
# Expected: PROJECT_REGISTRY.json, settings.json, repair_lock.json, rules/, skills/, commands/, hooks/

# Count Claude Code files (should show 72+ files)
find .claude/ -type f | wc -l

# Verify key files exist
ls -la .claude/PROJECT_REGISTRY.json  # Professional OS state
ls -la .claude/settings.json          # Claude Code configuration
ls -la .claude/skills/                # 20 AI specialists
ls -la .claude/commands/              # 23 professional commands
ls -la .claude/hooks/                 # Safety systems
```

### If `/implement` Doesn't Work
Sometimes the special commands don't load. Here's how to do it manually:

```bash
# Start Claude normally
claude

# Tell Claude what to do step by step:
# Type: "Use @Planner to create a plan for: add a login system"
# Wait for Claude to respond, then type: APPROVE_PLAN
# Type: /clear (when Claude tells you to)
# Continue with each approval step...
```

## Production Readiness Checklist

### Pre-Deployment Verification
- [ ] All 12 skills implemented with proper YAML frontmatter and forked contexts
- [ ] All 7 main rules + 16 sub-rules implemented and functional
- [ ] Comprehensive testing completed (database integrity, workflow execution, security hardening, enterprise features)
- [ ] Database integrity testing passed with real data preservation verified
- [ ] Workflow execution testing completed end-to-end with all gates functional
- [ ] Security hardening validated (rm ban, worktree isolation, repair scope enforcement)
- [ ] Enterprise features tested (multi-agent coordination, audit logging, compliance)
- [ ] Implementation plan updated to reflect 100% completion status
- [ ] README.md updated with accurate status and comprehensive troubleshooting

### Deployment Checklist
- [ ] Set `CC_DESTINATION` environment variable to target project directory
- [ ] Execute `./scripts/setup.sh` and verify successful completion
- [ ] Verify all 46 files installed correctly
- [ ] Test Claude Code initialization: `claude`
- [ ] Verify `.claude/` directory structure with all subdirectories
- [ ] Confirm architectural documentation created in `documentation/main/`
- [ ] Validate repair_lock.json properly initialized
- [ ] Test safety hooks are executable and functional

### Post-Deployment Testing
- [ ] Execute `/implement "create user registration system"` end-to-end
- [ ] Verify all workflow gates execute properly (A through F)
- [ ] Confirm context resets work at each human gate
- [ ] Test sanity checker integration for UI features
- [ ] Validate Ralph loop functionality and progress tracking
- [ ] Check multi-agent coordination and parallel operation
- [ ] Verify audit logging captures complete operation trail

### Rollback Procedures
**If deployment fails or issues are discovered:**

1. **Immediate Stop**: Stop all Claude Code instances
2. **Isolate Changes**: Move `.claude/` directory to backup location
3. **Restore Previous State**: Revert any modified project files
4. **Clean Environment**: Remove any test data or artifacts
5. **Report Issues**: Document specific failures for investigation
6. **Selective Re-deployment**: Address issues and redeploy incrementally

**Rollback Commands:**
```bash
# Backup current setup
mv .claude .claude.backup.$(date +%Y%m%d_%H%M%S)

# Restore previous CLAUDE.md if needed
git checkout HEAD~1 -- CLAUDE.md

# Clean test artifacts
rm -rf temp/ logs/ documentation/plans/*
```

## Your First Test - Quick Checklist

**For Automated Setup:**
- [ ] Set `CC_DESTINATION` environment variable
- [ ] Ran `./scripts/setup.sh` successfully
- [ ] Claude Code works when you type `claude`
- [ ] You can see the `.claude/` folder with all subfolders
- [ ] Try: `/startprojectplanning` (establish foundation first)

**For Interactive Setup:**
- [ ] Ran `./scripts/setup-interactive.sh` and answered questions
- [ ] Setup completed with your custom configuration
- [ ] Claude Code works when you type `claude`
- [ ] Check that documentation was set up according to your answers
- [ ] Try: `/startprojectplanning` (establish foundation first)

**Both Methods - Verify Everything Works:**
- [ ] You can see `documentation/main/`, `documentation/plans/`, and `tests/poc_scripts/` folders
- [ ] Check that `documentation/main/proposedarchitecture.md` was created
- [ ] Watch how Claude asks for approvals at each step
- [ ] Notice how Claude references your architectural documents
- [ ] Test `/collect-knowledge` if you have existing docs
- [ ] Try `/debug-issue` and `/test-plan` commands

---

*This setup turns Claude Code into a full development team that works with you. Start with simple features to learn how it works, then use it for bigger projects. Remember: you control all the important decisions - Claude Code is your smart assistant, not your replacement.*
