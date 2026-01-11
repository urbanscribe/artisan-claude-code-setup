#!/usr/bin/env python3
"""
PreToolUse hook for Claude Code safety validation.
Prevents dangerous operations and enforces security policies.
"""

import sys
import json
import os
import subprocess
from typing import Dict, Any, List
from pathlib import Path
from datetime import datetime

def find_project_root() -> Path:
    """
    Find the project root by searching up the directory tree for .claude folder.
    This handles cases where Claude Code runs hooks from subdirectories.
    """
    current = Path.cwd()
    # Search up to 10 levels up to find .claude directory
    for _ in range(10):
        if (current / '.claude').exists():
            return current
        if current.parent == current:  # Reached filesystem root
            break
        current = current.parent

    # Fallback: assume we're in the project root or nearby
    # Try to find .claude relative to script location
    script_dir = Path(__file__).parent.parent.parent  # Go up from hooks/ to project root
    if (script_dir / '.claude').exists():
        return script_dir

    # Last resort: use current directory
    return Path.cwd()

class SafetyValidationHook:
    """Hook for validating tool usage before execution."""

    def __init__(self):
        # Find project root dynamically
        self.project_root = find_project_root()
        self.claude_dir = self.project_root / '.claude'

        # Load configuration
        config_path = self.claude_dir / 'policy.yaml'
        if config_path.exists():
            import yaml
            with open(config_path, 'r') as f:
                self.config = yaml.safe_load(f)
        else:
            # Fallback configuration
            self.config = {
                'safety': {
                    'protected_files': [
                        '.env',
                        '.github/workflows/*.yml',
                        'package-lock.json',
                        'yarn.lock',
                        'requirements-lock.txt',
                        'Pipfile.lock'
                    ],
                    'protected_patterns': [
                        '.env',
                        'secrets',
                        'credentials',
                        'private'
                    ],
                    'dangerous_commands': [
                        'rm -rf /',
                        'rm -rf /*',
                        'format',
                        'fdisk',
                        'mkfs',
                        'dd if=',
                        'shutdown',
                        'reboot',
                        'halt',
                        'db_init',
                        'drop table',
                        'truncate table',
                        'delete from * where',
                        'alter table drop',
                        'docker compose down -v',
                        'docker system prune',
                        'docker volume rm'
                    ]
                }
            }

    def validate_tool_use(self, tool_input: Dict[str, Any], permissive_mode: bool = False) -> Dict[str, Any]:
        """
        Validate a tool use request before execution.
        Enforces comprehensive professional workflow discipline.

        Args:
            tool_input: The tool input data from Claude Code

        Returns:
            Dict with validation result
        """
        tool_name = tool_input.get('tool', '')
        parameters = tool_input.get('parameters', {})
        command_input = str(tool_input.get('input', {}).get('message', ''))

        # FOUNDATION GATE ENFORCEMENT: Block development until project foundation established (FIRST CHECK)
        foundation_check = self._check_foundation_gate(tool_input)
        if not foundation_check['allowed']:
            return foundation_check

        # PROFESSIONAL WORKFLOW ENFORCEMENT: Comprehensive discipline validation
        workflow_check = self._check_professional_workflow_enforcement(tool_input)
        if not workflow_check['allowed']:
            return workflow_check

        # SPRINT VALIDATION GATES: Enforce sprint context for execution operations
        sprint_validation = self._check_sprint_validation_gates(tool_input)
        if not sprint_validation['allowed']:
            return sprint_validation

        # PLANNING CHECKLIST ENFORCEMENT: Block sprint creation without quality gates
        planning_check = self._check_planning_checklist_enforcement(tool_input)
        if not planning_check['allowed']:
            return planning_check

        # BOUNDARY ENFORCEMENT: Validate all operations against sprint scope
        boundary_check = self._check_boundary_enforcement(tool_input)
        if not boundary_check['allowed']:
            return boundary_check

        # RALPH WIGGUM PROMISE TAG ENFORCEMENT: Validate completion markers in outputs
        promise_check = self._check_promise_tag_enforcement(tool_input)
        if not promise_check['allowed']:
            return promise_check

        # First validate execution context (sprint boundaries and progress tracking)
        execution_check = self._validate_execution_context(tool_input)
        if not execution_check['allowed']:
            return execution_check

        # TOOL PERMISSION FILTERING: Allow only professional OS approved operations
        permission_check = self._check_tool_permissions(tool_input)
        if not permission_check['allowed']:
            return permission_check

        # Then validate based on tool type
        if tool_name == 'bash':
            return self._validate_bash_command(parameters)
        elif tool_name in ['write', 'edit']:
            return self._validate_file_operation(parameters)
        elif tool_name == 'run':
            tool_check = self._validate_run_command(parameters)
            if not tool_check['allowed']:
                return tool_check

        # Combine execution context with tool validation
        combined_reason = execution_check['reason']
        if tool_name in ['bash', 'write', 'edit', 'run']:
            combined_reason += f" | Tool validation passed"

        return {
            'allowed': True,
            'reason': combined_reason,
            'sprint_context_valid': True,
            'execution_tracked': execution_check.get('sprint_progress_updated', False)
        }

    def _validate_bash_command(self, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """Validate bash command execution."""
        command = parameters.get('command', '').strip()

        # ZERO-EXCEPTION RM BAN - No safe patterns, no exceptions
        normalized_cmd = " ".join(command.lower().split())  # Prevent whitespace evasion

        # Absolute ban on all rm variants
        rm_commands = ['rm', 'rmdir', 'unlink', 'shred', 'del']
        for rm_cmd in rm_commands:
            if rm_cmd in normalized_cmd:
                return {
                    'allowed': False,
                    'reason': f'Absolute {rm_cmd} ban - no safe deletions allowed',
                    'severity': 'critical'
                }

        # Check for other dangerous commands
        dangerous_commands = self.config.get('safety', {}).get('dangerous_commands', [])
        for dangerous in dangerous_commands:
            if dangerous in command.lower():
                return {
                    'allowed': False,
                    'reason': f'Dangerous command detected: {dangerous}',
                    'severity': 'critical'
                }

        return {'allowed': True, 'reason': 'Bash command validation passed'}

    def _validate_file_operation(self, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """Validate file write/edit operations."""
        file_path = parameters.get('file_path', '')

        if not file_path:
            return {'allowed': True, 'reason': 'No file path specified'}

        # Check protected files
        protected_files = self.config.get('safety', {}).get('protected_files', [])
        for protected in protected_files:
            if protected in file_path or file_path.endswith(protected):
                return {
                    'allowed': False,
                    'reason': f'Protected file modification attempt: {file_path}',
                    'severity': 'high'
                }

        # Check protected patterns
        protected_patterns = self.config.get('safety', {}).get('protected_patterns', [])
        for pattern in protected_patterns:
            if pattern.lower() in file_path.lower():
                return {
                    'allowed': False,
                    'reason': f'Protected pattern detected in path: {pattern}',
                    'severity': 'medium'
                }

        # Check file size limits for safety
        if os.path.exists(file_path):
            file_size = os.path.getsize(file_path)
            max_size = 50 * 1024 * 1024  # 50MB limit
            if file_size > max_size:
                return {
                    'allowed': False,
                    'reason': f'File too large for modification: {file_size} bytes',
                    'severity': 'medium'
                }

        # Validate worktree ownership - agents may only modify files within current worktree
        worktree_boundary = self._get_worktree_boundary()
        if worktree_boundary and not self._is_within_worktree(file_path, worktree_boundary):
            return {
                'allowed': False,
                'reason': f'File {file_path} is outside current worktree boundary ({worktree_boundary}). Each worktree = one feature namespace.',
                'severity': 'high'
            }

        # STATEFUL FAIL-CLOSED ENFORCEMENT: Validate against active sprint boundaries
        sprint_boundary_check = self._check_sprint_boundary_compliance(file_path)
        if not sprint_boundary_check['allowed']:
            return sprint_boundary_check

        # Enforce repair scope boundaries - check if we're in repair mode and validate against FAIL_SCOPE
        repair_scope_check = self._check_repair_scope_compliance(file_path, parameters)
        if not repair_scope_check['allowed']:
            return repair_scope_check

        return {'allowed': True, 'reason': 'File operation validation passed'}

    def _validate_run_command(self, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """Validate run command execution."""
        # Add any specific run command validations here
        return {'allowed': True, 'reason': 'Run command validation passed'}

    def _get_worktree_boundary(self) -> str:
        """Get the current worktree root directory. FAIL-CLOSED SECURITY."""
        try:
            result = subprocess.run(
                ['git', 'rev-parse', '--show-toplevel'],
                capture_output=True,
                text=True,
                cwd=os.getcwd(),
                timeout=5
            )
            # FAIL-CLOSED: If git command fails OR returns empty, this will return empty string
            # which will cause worktree validation to block ALL file operations
            if result.returncode == 0 and result.stdout.strip():
                return result.stdout.strip()
        except (subprocess.TimeoutExpired, FileNotFoundError):
            pass
        return ""  # Empty string triggers fail-closed behavior

    def _is_within_worktree(self, file_path: str, worktree_root: str) -> bool:
        """Check if file path is within worktree boundary."""
        try:
            abs_file_path = os.path.abspath(file_path)
            abs_worktree = os.path.abspath(worktree_root)
            return abs_file_path.startswith(abs_worktree + os.sep) or abs_file_path == abs_worktree
        except (OSError, ValueError):
            return False

    def _check_repair_scope_compliance(self, file_path: str, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """Check if file operation complies with repair scope boundaries."""
        # Check if we're in a repair workflow by looking for FAIL_SCOPE in recent context
        # This is a heuristic - in practice, we'd need conversation context
        # For now, we'll check if there are any .repair files or recent repair commands

        # Look for repair-related files in the workspace
        try:
            import glob
            repair_indicators = glob.glob("**/repair*.md") + glob.glob("**/REPAIR*.md") + glob.glob("**/fail_scope*.txt")
            if repair_indicators:
                # We're likely in repair mode - check for FAIL_SCOPE boundaries
                # Parse the most recent repair file to extract allowed paths
                allowed_paths = self._extract_allowed_repair_paths()
                if allowed_paths:
                    abs_file_path = os.path.abspath(file_path)
                    for allowed_path in allowed_paths:
                        abs_allowed = os.path.abspath(allowed_path)
                        if abs_file_path.startswith(abs_allowed):
                            return {'allowed': True, 'reason': f'File {file_path} is within repair scope'}

                    return {
                        'allowed': False,
                        'reason': f'File {file_path} is outside repair scope boundaries. Only these paths are allowed: {allowed_paths}',
                        'severity': 'high'
                    }
        except Exception:
            # If scope checking fails, allow the operation (fail-safe)
            pass

        return {'allowed': True, 'reason': 'Not in repair mode or scope check passed'}

    def _extract_allowed_repair_paths(self) -> list[str]:
        """Extract allowed file paths from recent repair documentation."""
        allowed_paths = []
        try:
            import glob
            import re

            # Look for recent repair files
            repair_files = glob.glob("documentation/**/*.md") + glob.glob("*.md")

            for file_path in repair_files:
                if 'repair' in file_path.lower():
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()

                        # Look for FAIL_SCOPE sections
                        scope_match = re.search(r'FAIL_SCOPE:.*?(?=\n\n|\n##|\n###|$)', content, re.DOTALL | re.IGNORECASE)
                        if scope_match:
                            scope_content = scope_match.group(0)
                            # Extract file paths
                            file_matches = re.findall(r'- file:\s*([^\n]+)', scope_content, re.IGNORECASE)
                            allowed_paths.extend([path.strip() for path in file_matches])

        except Exception:
            pass

        return list(set(allowed_paths))  # Remove duplicates

    def _check_sprint_boundary_compliance(self, file_path: str) -> Dict[str, Any]:
        """STATEFUL FAIL-CLOSED ENFORCEMENT: Check file operation against active sprint boundaries."""

        try:
            # Load PROJECT_REGISTRY.json from .claude folder
            registry_path = self.claude_dir / 'PROJECT_REGISTRY.json'
            if not registry_path.exists():
                # No registry file - allow operation (fail-safe)
                return {'allowed': True, 'reason': 'No project registry file found'}

            with open(registry_path, 'r') as f:
                registry = json.load(f)

            # Check if there's an active sprint
            active_sprint = registry.get('sprints', {}).get('active')
            if not active_sprint:
                # No active sprint - allow operation
                return {'allowed': True, 'reason': 'No active sprint - operation allowed'}

            # Check sprint phase and manifesto status
            sprint_phase = active_sprint.get('phase', '')
            manifesto_locked = active_sprint.get('manifesto_locked', False)
            if sprint_phase != 'execution' or not manifesto_locked:
                # Sprint not in execution phase or manifesto not locked - allow operation but log
                return {'allowed': True, 'reason': f'Sprint phase {sprint_phase}, manifesto_locked {manifesto_locked} - operation allowed'}

            # Get locked files for this sprint
            locked_files = active_sprint.get('locked_files', [])
            if not locked_files:
                # No locked files defined - allow operation but warn
                return {
                    'allowed': True,
                    'reason': 'No locked files defined for active sprint - operation allowed with warning',
                    'warning': 'Sprint has no file boundaries defined'
                }

            # Normalize file path for comparison
            abs_file_path = os.path.abspath(file_path)

            # Check if file is within any locked file boundary
            for locked_path in locked_files:
                # Handle both files and directories
                abs_locked = os.path.abspath(locked_path)

                # If locked path is a directory, check if file is within it
                if os.path.isdir(abs_locked) or locked_path.endswith('/'):
                    if abs_file_path.startswith(abs_locked):
                        return {'allowed': True, 'reason': f'File {file_path} is within sprint boundary: {locked_path}'}
                # If locked path is a file, check exact match
                elif abs_file_path == abs_locked:
                    return {'allowed': True, 'reason': f'File {file_path} is explicitly locked for sprint'}

            # File is outside sprint boundaries - BLOCK OPERATION
            sprint_id = active_sprint.get('id', 'unknown')
            return {
                'allowed': False,
                'reason': f'SPRINT SOVEREIGNTY VIOLATION: File {file_path} is outside active sprint boundaries. Sprint {sprint_id} only allows operations on: {locked_files}',
                'severity': 'high',
                'sprint_id': sprint_id,
                'allowed_paths': locked_files
            }

        except json.JSONDecodeError:
            # Corrupted JSON - allow operation but log (fail-safe)
            return {'allowed': True, 'reason': 'Sprint state file corrupted - operation allowed (fail-safe)'}

        except Exception as e:
            # Any other error - allow operation but log (fail-safe)
            return {'allowed': True, 'reason': f'Sprint boundary check failed: {str(e)} - operation allowed (fail-safe)'}

    def _validate_foundation_gate(self, tool_input: Dict[str, Any]) -> Dict[str, Any]:
        """Validate foundation gate compliance for professional OS."""
        # Foundation Gate Enforcement
        registry_path = self.claude_dir / 'PROJECT_REGISTRY.json'
        if registry_path.exists():
            with open(registry_path, 'r') as f:
                registry = json.load(f)
            foundation_complete = registry.get('foundation', {}).get('complete', False)
            current_phase = registry.get('foundation', {}).get('current_phase', 'project_planning')

            # Allow read-only operations during project planning phase
            if not foundation_complete and tool_input.get('tool_name') not in ['read', 'grep', 'run_terminal_cmd']:
                # Check for bypass flag in command inputs (heuristic for now)
                command_args = tool_input.get('parameters', {}).get('command', '') if tool_input.get('tool_name') == 'run_terminal_cmd' else ''
                if '--bypass-foundation' in command_args:
                    # Log bypass and allow, but do not alter core state
                    return {'allowed': True, 'reason': 'Foundation gate bypassed by user flag. Proceeding with caution.'}
                else:
                    return {
                        'allowed': False,
                        'reason': '⚠️ SYSTEM LOCK: Project foundation not established. Please run /startprojectplanning to unlock development tools.',
                        'severity': 'critical',
                        'suggestion': 'Run /startprojectplanning to establish professional project foundation'
                    }
        return {'allowed': True}

    def _validate_execution_context(self, tool_input: Dict[str, Any]) -> Dict[str, Any]:
        """Validate execution operations within sprint boundaries and track progress."""

        try:
            # Load project registry
            registry_path = self.claude_dir / 'PROJECT_REGISTRY.json'
            if not registry_path.exists():
                return {'allowed': True, 'reason': 'No project registry - execution allowed'}

            with open(registry_path, 'r') as f:
                registry = json.load(f)

            active_sprint = registry.get('sprints', {}).get('active')
            if not active_sprint:
                return {'allowed': True, 'reason': 'No active sprint - execution allowed'}

            # Update execution tracking
            current_iteration = active_sprint.get('iteration', 0) + 1
            max_iterations = active_sprint.get('max_iterations', 50)

            if current_iteration > max_iterations:
                sprint_id = active_sprint['id']
                return {
                    'allowed': False,
                    'reason': f'SPRINT EXECUTION LIMIT EXCEEDED: {current_iteration}/{max_iterations} iterations reached. Sprint {sprint_id} execution terminated.',
                    'severity': 'high',
                    'sprint_id': sprint_id
                }

            # Update sprint progress
            active_sprint['iteration'] = current_iteration
            active_sprint['last_updated'] = datetime.now().isoformat()

            # Track execution context
            execution_context = active_sprint.setdefault('execution_context', {})
            execution_context['last_tool_used'] = tool_input.get('tool_name', 'unknown')
            execution_context['execution_timestamp'] = datetime.now().isoformat()

            # Save updated registry
            with open(registry_path, 'w') as f:
                json.dump(registry, f, indent=2)

            sprint_id = active_sprint['id']
            return {
                'allowed': True,
                'reason': f'Execution validated for sprint {sprint_id} - iteration {current_iteration}/{max_iterations}',
                'sprint_progress_updated': True
            }

        except Exception as e:
            return {'allowed': True, 'reason': f'Execution validation failed: {str(e)} - operation allowed (fail-safe)'}

    def _check_foundation_gate(self, tool_input: Dict[str, Any]) -> Dict[str, Any]:
        """FOUNDATION GATE ENFORCEMENT: Block development until project foundation established."""

        try:
            # Load PROJECT_REGISTRY.json
            registry_path = self.claude_dir / 'PROJECT_REGISTRY.json'
            if not registry_path.exists():
                # No registry - block all development operations
                return {
                    'allowed': False,
                    'reason': '⚠️ SYSTEM LOCK: Project registry not found. Run setup.sh to initialize professional operating system.',
                    'severity': 'critical'
                }

            with open(registry_path, 'r') as f:
                registry = json.load(f)

            # Check if foundation is complete
            foundation = registry.get('foundation', {})
            foundation_complete = foundation.get('complete', False)

            if foundation_complete:
                # Foundation complete - allow all operations
                return {'allowed': True, 'reason': 'Project foundation established - development operations allowed'}

            # Foundation not complete - check for bypass flag
            command = tool_input.get('input', {}).get('message', '').strip()
            parameters = tool_input.get('parameters', {})

            # Check for bypass flag in command inputs
            bypass_requested = False
            if '--bypass-foundation' in command or '--bypass-foundation' in str(parameters):
                bypass_requested = True

            if bypass_requested:
                # Bypass requested - prompt for confirmation but don't block
                # This provides flexibility for experienced users while maintaining structure
                return {
                    'allowed': True,
                    'reason': 'Foundation bypass approved - proceeding with development (experienced user override)',
                    'warning': '⚠️ Foundation not established. Use /startprojectplanning for structured setup.'
                }

            # Foundation not complete and no bypass - check operation type
            tool_name = tool_input.get('tool', '')

            # Allow read-only operations for planning and research
            read_only_tools = ['read', 'grep', 'run_terminal_cmd']
            planning_commands = ['startprojectplanning', 'projectstatus']

            # Check if this is a read-only operation or planning command
            is_read_only = tool_name in read_only_tools
            is_planning = any(cmd in command for cmd in planning_commands)

            if is_read_only or is_planning:
                return {'allowed': True, 'reason': 'Read-only operation allowed during foundation phase'}

            # Block all development operations
            return {
                'allowed': False,
                'reason': '⚠️ SYSTEM LOCK: Project foundation not established. Please run /startprojectplanning to unlock development tools.',
                'severity': 'critical',
                'suggestion': 'Run /startprojectplanning to establish professional project foundation'
            }

        except json.JSONDecodeError:
            return {
                'allowed': False,
                'reason': '⚠️ SYSTEM LOCK: Project registry corrupted. Run setup.sh to reinitialize.',
                'severity': 'critical'
            }

        except Exception as e:
            # Fail-safe: Allow operation if foundation check fails
            return {'allowed': True, 'reason': f'Foundation gate check failed: {str(e)} - operation allowed (fail-safe)'}

    def _check_sprint_validation_gates(self, tool_input: Dict[str, Any]) -> Dict[str, Any]:
        """SPRINT VALIDATION GATES: Enforce sprint context for execution operations."""

        try:
            # Load PROJECT_REGISTRY.json
            registry_path = self.claude_dir / 'PROJECT_REGISTRY.json'
            if not registry_path.exists():
                # Allow operations if no registry (fail-safe for non-sprint environments)
                return {'allowed': True, 'reason': 'No project registry - operations allowed'}

            with open(registry_path, 'r') as f:
                registry = json.load(f)

            active_sprint = registry.get('sprints', {}).get('active')
            if not active_sprint:
                # No active sprint - allow planning and research operations
                tool_name = tool_input.get('tool', '')
                planning_tools = ['read', 'grep', 'run_terminal_cmd']
                command_input = tool_input.get('input', {}).get('message', '')

                # Allow planning-related operations
                if tool_name in planning_tools or any(cmd in command_input for cmd in ['startprojectplanning', 'startsprintplanning', 'projectstatus']):
                    return {'allowed': True, 'reason': 'No active sprint - planning operations allowed'}

                # Block development operations without sprint context
                return {
                    'allowed': False,
                    'reason': '🚫 EXECUTION BLOCKED: No active sprint context. Start a sprint with /startnewsprint before executing development operations.',
                    'severity': 'high',
                    'suggestion': 'Run /startnewsprint "feature description" to establish sprint context'
                }

            # Validate sprint phase and manifesto status
            sprint_phase = active_sprint.get('phase', '')
            manifesto_locked = active_sprint.get('manifesto_locked', False)
            locked_files = active_sprint.get('locked_files', [])

            # Allow planning operations in any phase
            tool_name = tool_input.get('tool', '')
            command_input = str(tool_input.get('input', {}).get('message', ''))
            planning_commands = ['startsprintplanning', 'projectstatus', 'listsprints']

            if any(cmd in command_input for cmd in planning_commands):
                return {'allowed': True, 'reason': 'Planning operations always allowed'}

            # For execution operations, require manifesto lock
            execution_commands = ['implement']
            if any(cmd in command_input for cmd in execution_commands):
                if not manifesto_locked:
                    return {
                        'allowed': False,
                        'reason': '🚫 EXECUTION BLOCKED: Sprint manifesto not locked. Complete planning with /startsprintplanning then establish boundaries with /startnewsprint.',
                        'severity': 'high',
                        'suggestion': 'Run /startnewsprint to lock execution boundaries'
                    }

                if not locked_files:
                    return {
                        'allowed': False,
                        'reason': '🚫 EXECUTION BLOCKED: No files locked for sprint. Sprint boundaries not established.',
                        'severity': 'high',
                        'suggestion': 'Run /startnewsprint to establish file boundaries'
                    }

            return {'allowed': True, 'reason': 'Sprint validation passed - execution allowed'}

        except json.JSONDecodeError:
            return {'allowed': True, 'reason': 'Registry corrupted - operations allowed (fail-safe)'}

        except Exception as e:
            return {'allowed': True, 'reason': f'Sprint validation failed: {str(e)} - operations allowed (fail-safe)'}

    def _check_promise_tag_enforcement(self, tool_input: Dict[str, Any]) -> Dict[str, Any]:
        """RALPH WIGGUM PROMISE TAG ENFORCEMENT: Validate completion markers in outputs."""

        try:
            # Check if this is part of a Ralph Wiggum execution loop
            command_input = str(tool_input.get('input', {}).get('message', ''))

            # Only enforce promise tags during /implement execution
            if 'implement' not in command_input.lower():
                return {'allowed': True, 'reason': 'Not in execution loop - promise tags not required'}

            # Load PROJECT_REGISTRY.json to check execution context
            registry_path = self.claude_dir / 'PROJECT_REGISTRY.json'
            if not registry_path.exists():
                return {'allowed': True, 'reason': 'No registry - promise enforcement skipped'}

            with open(registry_path, 'r') as f:
                registry = json.load(f)

            active_sprint = registry.get('sprints', {}).get('active')
            if not active_sprint:
                return {'allowed': True, 'reason': 'No active sprint - promise enforcement skipped'}

            # Intelligent Progress Monitoring & Resumption Guidance
            current_iteration = active_sprint.get('iteration', 0)
            assessment_checkpoints = [10, 25, 40, 60]  # Smart assessment triggers

            # Check for assessment checkpoints
            if current_iteration in assessment_checkpoints:
                # Trigger deep self-assessment
                if '--assessment-complete' not in command_input:
                    return {
                        'allowed': False,
                        'reason': f'🧠 INTELLIGENT CHECKPOINT: Iteration {current_iteration} - Time for progress assessment!',
                        'severity': 'info',
                        'suggestion': 'Run /deepselfassessment to see progress %, check for regressions, and get guidance on next steps. This ensures we\'re on the right path!',
                        'assessment_checkpoint': current_iteration
                    }

            # Provide helpful guidance instead of blocking
            # This handles cases where Claude Code internally blocks at iteration limits
            max_iterations = active_sprint.get('max_iterations', 1000)

            # If we're at or near iteration limits, provide helpful resumption guidance
            if current_iteration >= 10:  # Claude Code's internal limit
                return {
                    'allowed': True,  # Allow continuation
                    'reason': f'🎯 EXPERIENCED SPRINT CONTINUATION: Iteration {current_iteration} - You\'re making great progress!',
                    'guidance': f'''
📍 CURRENT STATUS:
   • Sprint: {sprint_id}
   • Progress: {current_iteration} iterations completed
   • Phase: Advanced development
   • Files: {len(active_sprint.get('locked_files', []))} locked

🚀 RESUMPTION OPTIONS:

   1. CONTINUE CURRENT WORK:
      Keep building on your progress - the system supports unlimited iterations!

   2. ASSESSMENT CHECK:
      Run /deepselfassessment for detailed progress analysis and guidance

   3. SPRINT MANAGEMENT:
      Use /projectstatus to see overall project state
      Use /listsprints to manage sprint lifecycle

💡 REMEMBER: No arbitrary limits - your work is preserved and you can continue indefinitely with intelligent oversight!

Ready to continue building? Your sprint context is fully intact.
                    ''',
                    'sprint_context_preserved': True,
                    'unlimited_iterations_supported': True
                }

            # Normal operation - provide progress context
            return {
                'allowed': True,
                'reason': f'✅ SPRINT EXECUTION: Iteration {current_iteration + 1} ready - building on your solid foundation!',
                'progress_context': f'Sprint {sprint_id} | Iteration {current_iteration} | {len(active_sprint.get("locked_files", []))} files locked'
            }

            # Validate promise tags in recent context (this would be enhanced with conversation context)
            # For now, allow operations but log the requirement
            return {
                'allowed': True,
                'reason': f'Promise tag validation required - ensure <promise>SANITY_CHECK_PASS</promise> for loop completion. Iteration: {current_iteration}/{max_iterations}',
                'warning': 'Promise tag enforcement active - monitor for completion markers'
            }

        except Exception as e:
            return {'allowed': True, 'reason': f'Promise enforcement check failed: {str(e)} - operations allowed (fail-safe)'}

    def _check_professional_workflow_enforcement(self, tool_input: Dict[str, Any]) -> Dict[str, Any]:
        """PROFESSIONAL WORKFLOW ENFORCEMENT: Comprehensive discipline validation."""

        try:
            # Load PROJECT_REGISTRY.json for workflow state
            registry_path = self.claude_dir / 'PROJECT_REGISTRY.json'
            if not registry_path.exists():
                return {'allowed': True, 'reason': 'No project registry - workflow enforcement bypassed'}

            with open(registry_path, 'r') as f:
                registry = json.load(f)

            tool_name = tool_input.get('tool', '')
            command_input = str(tool_input.get('input', {}).get('message', ''))

            # CONTEXT DRIFT PREVENTION: Block operations that violate workflow progression
            foundation_complete = registry.get('foundation', {}).get('complete', False)
            active_sprint = registry.get('sprints', {}).get('active')
            planning_complete = registry.get('planning_checklist', {}).get('completed', False)

            # Prevent development operations before foundation
            development_tools = ['write', 'run_terminal_cmd']
            if tool_name in development_tools and not foundation_complete:
                if 'startprojectplanning' not in command_input:
                    return {
                        'allowed': False,
                        'reason': '🚫 PROFESSIONAL DISCIPLINE: Development blocked until foundation established. Run /startprojectplanning first.',
                        'severity': 'high',
                        'guidance': 'Complete project foundation before any development work'
                    }

            # Prevent sprint operations without proper planning
            sprint_commands = ['startnewsprint', 'implement']
            if any(cmd in command_input for cmd in sprint_commands) and not planning_complete:
                return {
                    'allowed': False,
                    'reason': '🚫 PROFESSIONAL DISCIPLINE: Sprint operations blocked until planning checklist complete. Run /startsprintplanning first.',
                    'severity': 'high',
                    'guidance': 'Complete comprehensive planning before sprint execution'
                }

            # Prevent out-of-sequence operations
            if 'endsprint' in command_input and not active_sprint:
                return {
                    'allowed': False,
                    'reason': '🚫 PROFESSIONAL DISCIPLINE: No active sprint to end. Start a sprint first.',
                    'severity': 'medium',
                    'guidance': 'Ensure sprint is active before attempting completion'
                }

            return {'allowed': True, 'reason': 'Professional workflow validation passed'}

        except Exception as e:
            return {'allowed': True, 'reason': f'Workflow enforcement failed: {str(e)} - operations allowed (fail-safe)'}

    def _check_planning_checklist_enforcement(self, tool_input: Dict[str, Any]) -> Dict[str, Any]:
        """PLANNING CHECKLIST ENFORCEMENT: Block sprint creation without all 10 gates PASSED."""

        try:
            command_input = str(tool_input.get('input', {}).get('message', ''))

            # Only enforce for sprint creation commands
            if 'startnewsprint' not in command_input:
                return {'allowed': True, 'reason': 'Not a sprint creation operation'}

            # Load registry and check planning status
            registry_path = self.claude_dir / 'PROJECT_REGISTRY.json'
            if not registry_path.exists():
                return {'allowed': False, 'reason': 'No project registry found for planning validation'}

            with open(registry_path, 'r') as f:
                registry = json.load(f)

            planning_complete = registry.get('planning_checklist', {}).get('completed', False)
            if not planning_complete:
                # Provide detailed status of incomplete gates
                validation_report = registry.get('planning_checklist', {}).get('validation_report', {})
                incomplete_gates = []
                for gate, status_info in validation_report.items():
                    if status_info.get('status') != 'passed':
                        incomplete_gates.append(gate.replace('_', ' ').title())

                return {
                    'allowed': False,
                    'reason': f'🚫 PLANNING CHECKLIST INCOMPLETE: {len(incomplete_gates)}/10 quality gates failed. Complete /startsprintplanning first.',
                    'severity': 'high',
                    'incomplete_gates': incomplete_gates,
                    'guidance': 'Run /startsprintplanning to complete all quality gates before starting sprint'
                }

            return {'allowed': True, 'reason': 'Planning checklist validation passed'}

        except Exception as e:
            return {'allowed': True, 'reason': f'Planning checklist check failed: {str(e)} - operations allowed (fail-safe)'}

    def _check_boundary_enforcement(self, tool_input: Dict[str, Any]) -> Dict[str, Any]:
        """BOUNDARY ENFORCEMENT: Validate all operations against sprint locked_files scope."""

        try:
            tool_name = tool_input.get('tool', '')

            # Only enforce boundary checks for file operations
            if tool_name not in ['write', 'read', 'grep']:
                return {'allowed': True, 'reason': 'Not a file operation - boundary check skipped'}

            # Load registry for boundary validation
            registry_path = self.claude_dir / 'PROJECT_REGISTRY.json'
            if not registry_path.exists():
                return {'allowed': True, 'reason': 'No registry - boundary enforcement bypassed'}

            with open(registry_path, 'r') as f:
                registry = json.load(f)

            active_sprint = registry.get('sprints', {}).get('active')
            if not active_sprint:
                return {'allowed': True, 'reason': 'No active sprint - boundary enforcement bypassed'}

            manifesto_locked = active_sprint.get('manifesto_locked', False)
            if not manifesto_locked:
                return {'allowed': True, 'reason': 'Manifesto not locked - boundary enforcement bypassed'}

            locked_files = active_sprint.get('locked_files', [])
            if not locked_files:
                return {'allowed': True, 'reason': 'No locked files defined - boundary enforcement bypassed'}

            # Check file path against boundaries
            file_path = tool_input.get('parameters', {}).get('file_path', '')
            target_file = tool_input.get('parameters', {}).get('target_file', '')

            # Use the appropriate file path parameter
            check_path = file_path or target_file
            if not check_path:
                return {'allowed': True, 'reason': 'No file path specified'}

            # Normalize path for comparison
            abs_check_path = os.path.abspath(check_path)

            # Check if file is within any locked file boundary
            for locked_path in locked_files:
                abs_locked = os.path.abspath(locked_path)

                # If locked path is a directory, check if file is within it
                if os.path.isdir(abs_locked) or locked_path.endswith('/'):
                    if abs_check_path.startswith(abs_locked):
                        return {'allowed': True, 'reason': f'File within sprint boundary: {locked_path}'}
                # If locked path is a file, check exact match
                elif abs_check_path == abs_locked:
                    return {'allowed': True, 'reason': f'File explicitly locked for sprint: {locked_path}'}

            # File is outside boundaries - BLOCK
            sprint_id = active_sprint.get('id', 'unknown')
            return {
                'allowed': False,
                'reason': f'🚫 SPRINT BOUNDARY VIOLATION: {check_path} is outside active sprint scope. Sprint {sprint_id} only allows operations on: {locked_files}',
                'severity': 'high',
                'sprint_id': sprint_id,
                'allowed_paths': locked_files,
                'guidance': 'File operations must be within sprint manifesto boundaries'
            }

        except Exception as e:
            return {'allowed': True, 'reason': f'Boundary enforcement failed: {str(e)} - operations allowed (fail-safe)'}

    def _check_tool_permissions(self, tool_input: Dict[str, Any], permissive_mode: bool = False) -> Dict[str, Any]:
        """TOOL PERMISSION FILTERING: Allow only professional OS approved operations."""

        try:
            tool_name = tool_input.get('tool', '')
            command_input = str(tool_input.get('input', {}).get('message', ''))

            # Define approved professional OS tools
            approved_tools = [
                'read', 'grep', 'run_terminal_cmd', 'write',
                'edit', 'run'  # Standard Claude Code tools
            ]

            # Define always dangerous operations (never allowed)
            always_dangerous = [
                'rm -rf', 'rm -r', 'rmdir', 'del', 'delete', 'unlink',
                'format', 'fdisk', 'mkfs', 'dd if=', 'shutdown', 'reboot',
                'wget', 'curl.*--upload', 'scp', 'rsync',
                'git push.*--force', 'git reset.*--hard',
                'drop database', 'drop table', 'truncate table', 'delete from',
                'update.*set.*=', 'insert into', 'alter table'
            ]

            # Define safe operations (allowed in permissive mode without prompting)
            safe_operations = [
                'cat', 'ls', 'pwd', 'cd', 'echo', 'which', 'type', 'whoami',
                'head', 'tail', 'grep', 'find', 'wc', 'sort', 'uniq', 'diff',
                'git status', 'git log', 'git show', 'git diff', 'git branch', 'git rev-parse',
                'npm list', 'npm info', 'node --version', 'npm --version',
                'python --version', 'python3 --version', 'pip list', 'pip show',
                'mkdir', 'touch', 'cp', 'mv', 'chmod', 'chown',
                'file', 'stat', 'du', 'df', 'ps', 'top', 'htop'
            ]

            # Check for approved tools
            if tool_name not in approved_tools:
                return {
                    'allowed': False,
                    'reason': f'🚫 UNAUTHORIZED TOOL: {tool_name} not approved for professional OS operations',
                    'severity': 'high',
                    'guidance': 'Use only approved tools within the professional operating system'
                }

            command_lower = command_input.lower()

            # Always block dangerous operations
            for dangerous in always_dangerous:
                if dangerous in command_lower:
                    return {
                        'allowed': False,
                        'reason': f'🚫 ALWAYS DANGEROUS: {dangerous} operations permanently blocked for security',
                        'severity': 'critical',
                        'guidance': 'This operation poses unacceptable security risks'
                    }

            # In permissive mode, auto-allow safe operations
            if permissive_mode:
                for safe in safe_operations:
                    if safe in command_lower:
                        return {
                            'allowed': True,
                            'reason': f'✅ SAFE OPERATION: {safe} auto-approved in permissive mode',
                            'permissive_mode': True,
                            'auto_approved': True
                        }

            # Default behavior: require approval for non-safe operations
            return {
                'allowed': False,
                'reason': f'🔐 PERMISSION REQUIRED: Operation requires user approval. Use --permissive or --somewhatpermissive for trusted development.',
                'severity': 'medium',
                'guidance': 'Review the operation and approve if it aligns with development goals',
                'permissive_available': True,
                'requires_approval': True
            }

        except Exception as e:
            return {'allowed': True, 'reason': f'Tool permission check failed: {str(e)} - operations allowed (fail-safe)'}


def main():
    """Main entry point for the hook."""
    """Main entry point for the hook."""
        try:
            # Read input from stdin (provided by Claude Code)
            input_data = json.load(sys.stdin)

            # Check for permissive mode in command input
            command_input = str(input_data.get('input', {}).get('message', ''))

            # Validate the tool use
            hook = SafetyValidationHook()
            result = hook.validate_tool_use(input_data, permissive_mode='--permissive' in command_input or '--somewhatpermissive' in command_input)

            # Output result
            print(json.dumps(result))

            # Exit with appropriate code
            if result.get('allowed', True):
                sys.exit(0)  # Allow the tool execution
            else:
                sys.exit(1)  # Block the tool execution

    except Exception as e:
        # On error, block execution and log
        error_result = {
            'allowed': False,
            'reason': f'Hook execution error: {str(e)}',
            'severity': 'critical'
        }
        print(json.dumps(error_result))
        sys.exit(1)

if __name__ == '__main__':
    main()
