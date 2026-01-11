#!/usr/bin/env python3
"""
PostToolUse hook for Claude Code.
Provides error detection and workflow validation.
"""

import sys
import json
import re

def detect_token_isolation(output: str) -> dict:
    """Check if READY_FOR_* tokens are properly isolated on their own line."""
    import re

    # Check for workflow tokens that should be isolated
    token_pattern = r'(READY_FOR_(?:CODER|TESTER|EVALUATOR|EVALUATION_COMPLETE))'

    # Find all token occurrences
    matches = re.findall(token_pattern, output)

    if not matches:
        return {'isolated': True, 'issues': []}  # No tokens found, no issue

    issues = []
    lines = output.split('\n')

    for token in matches:
        # Find the line containing this token
        for i, line in enumerate(lines):
            if token in line:
                # Check if token is on its own line (possibly with whitespace)
                stripped_line = line.strip()
                if stripped_line != token:
                    issues.append({
                        'token': token,
                        'line': i + 1,
                        'content': stripped_line,
                        'error': f'Token not isolated - found: "{stripped_line}"'
                    })

                # Check if preceded by blank line (look back 1-2 lines)
                prev_lines_isolated = True
                for offset in [1, 2]:
                    if i - offset >= 0:
                        prev_line = lines[i - offset].strip()
                        if prev_line and not prev_line.startswith('//') and not prev_line.startswith('#'):
                            prev_lines_isolated = False
                            break

                if not prev_lines_isolated:
                    issues.append({
                        'token': token,
                        'line': i + 1,
                        'error': 'Token not properly separated by blank line'
                    })

    return {
        'isolated': len(issues) == 0,
        'issues': issues
    }

def check_ui_artifact_validation(output: str) -> dict:
    """Check if UI testing was actually performed with real artifacts."""
    # Look for the UI artifacts confirmation
    if 'READY_FOR_EVALUATOR' in output:
        # If READY_FOR_EVALUATOR is present, check for UI artifacts confirmation
        if 'UI artifacts provided by human? = yes' not in output:
            return {
                'ui_artifacts_missing': True,
                'message': 'READY_FOR_EVALUATOR present but no UI artifacts confirmation found',
                'severity': 'high',
                'blocks_workflow': True
            }
    return {'ui_artifacts_missing': False}

def check_repair_scope_validation(output: str, tool_input: dict) -> dict:
    """Check if repair scope validation was properly performed."""
    # Only check outputs that appear to be from repair workflow
    if 'INVALID_SCOPE:' in output:
        # Extract the invalid paths
        import re
        invalid_match = re.search(r'INVALID_SCOPE:\s*\[(.*?)\]', output)
        if invalid_match:
            invalid_paths = invalid_match.group(1)
            return {
                'scope_invalid': True,
                'missing_paths': invalid_paths,
                'message': f'Repair scope validation failed: missing paths {invalid_paths}',
                'severity': 'high',
                'blocks_workflow': True
            }

    # If we see FAIL_SCOPE in output, it means scope was defined but we should verify it was validated
    if 'FAIL_SCOPE:' in output and 'INVALID_SCOPE:' not in output:
        # Scope was defined but not validated as invalid - this is OK
        return {'scope_invalid': False}

    return {'scope_invalid': False}

def check_plan_context_bloom(tool_input: dict) -> dict:
    """Check if PLAN.md files are getting too large (context bloom risk)."""
    # Only check for write/edit operations to plan files
    if tool_input.get('tool') not in ['write', 'edit']:
        return {'warning': False}

    parameters = tool_input.get('parameters', {})
    file_path = parameters.get('file_path', '')

    # Check if this is a plan file
    if 'documentation/plans/' not in file_path:
        return {'warning': False}

    try:
        import os
        if os.path.exists(file_path):
            file_size = os.path.getsize(file_path)
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
                line_count = len(lines)

            # Warning thresholds
            size_kb = file_size / 1024
            if size_kb > 10 or line_count > 1500:
                return {
                    'warning': True,
                    'message': f'[WARNING: Plan size indicates potential context drift ({size_kb:.1f}KB, {line_count} lines). Consider splitting the feature or summarizing sections.]',
                    'severity': 'medium',
                    'size_kb': size_kb,
                    'lines': line_count
                }
    except (OSError, IOError) as e:
        # If we can't read the file, don't block but log the issue
        return {
            'warning': True,
            'message': f'[WARNING: Could not check plan file size: {str(e)}]',
            'severity': 'low'
        }

    return {'warning': False}

def detect_hallucination_patterns(output: str) -> dict:
    """Detect lazy agent hallucination patterns in tool output."""
    lazy_patterns = [
        r'\.\.\..*existing code.*\.\.\.',
        r'\.\.\..*rest of.*\.\.\.',
        r'\.\.\..*implementation.*\.\.\.',
        r'\.\.\..*add.*here.*\.\.\.',
        r'//.*TODO.*implement',
        r'#.*TODO.*implement',
        r'/\*.*TODO.*\*/',
        r'placeholder',
        r'stub.*implementation',
        r'mock.*implementation'
    ]

    for pattern in lazy_patterns:
        if re.search(pattern, output, re.IGNORECASE | re.MULTILINE):
            return {
                'has_hallucinations': True,
                'pattern': pattern,
                'severity': 'high',
                'blocks_workflow': True,
                'message': f'Detected lazy agent pattern: {pattern}'
            }

    return {'has_hallucinations': False, 'severity': 'low', 'blocks_workflow': False}

def enforce_sanity_checker_gate(output: str, tool_input: dict) -> dict:
    """Intercept READY_FOR_EVALUATOR and require SANITY_CHECK_PASS for UI/API features."""
    if 'READY_FOR_EVALUATOR' not in output:
        return {'sanity_required': False}

    # Check if project involves UI/API components
    involves_ui_api = check_for_ui_api_changes(tool_input)

    if not involves_ui_api:
        return {'sanity_required': False, 'reason': 'No UI/API features detected'}

    # Require proof of sanity-checker execution
    sanity_proof = verify_sanity_checker_execution(tool_input)

    if not sanity_proof:
        return {
            'sanity_required': True,
            'sanity_check_missing': True,
            'message': 'ERROR: Completeness proof missing. Invoke @sanity-checker to verify UI/Data integrity before proceeding.',
            'severity': 'high',
            'blocks_workflow': True
        }

    return {'sanity_required': True, 'sanity_check_passed': True}

def check_for_ui_api_changes(tool_input: dict) -> bool:
    """Determine if current work involves UI or API changes requiring sanity check."""
    # Check recent tool context for UI/API indicators
    parameters = tool_input.get('parameters', {})
    command = parameters.get('command', '').lower()

    ui_api_indicators = [
        '.html', '.css', '.js', '.jsx', '.tsx',
        'api/', 'frontend/', 'ui/', 'component',
        'chart', 'graph', 'dashboard', 'visual',
        'react', 'vue', 'angular', 'svelte'
    ]

    for indicator in ui_api_indicators:
        if indicator in command:
            return True

    # Check file paths if available
    file_path = parameters.get('file_path', '')
    for indicator in ui_api_indicators:
        if indicator in file_path.lower():
            return True

    return False

def verify_sanity_checker_execution(tool_input: dict) -> bool:
    """Check if sanity-checker has been successfully executed."""
    # For now, check if SANITY_CHECK_PASS appears in recent context
    # In production, this would check logs or session state
    output = tool_input.get('output', '')
    return 'SANITY_CHECK_PASS' in output or 'SANITY_CHECK_COMPLETE' in output

def detect_error_patterns(output: str) -> dict:
    """Detect error patterns in command output."""
    error_indicators = [
        r'Traceback\s*\(most recent call last\):',
        r'FAILED',
        r'ERROR',
        r'Exception',
        r'AssertionError',
        r'ValueError',
        r'TypeError',
        r'AttributeError',
        r'ImportError',
        r'ModuleNotFoundError',
        r'SyntaxError',
        r'IndentationError',
        r'NameError',
        r'ZeroDivisionError',
        r'IndexError',
        r'KeyError',
        r'FileNotFoundError',
        r'PermissionError',
        r'ConnectionError',
        r'TimeoutError'
    ]

    for pattern in error_indicators:
        if re.search(pattern, output, re.IGNORECASE | re.MULTILINE):
            return {
                'has_errors': True,
                'error_type': pattern,
                'severity': 'high',
                'blocks_workflow': True
            }

    return {'has_errors': False, 'severity': 'low', 'blocks_workflow': False}

def main():
    """Main entry point for the validation hook."""
    try:
        # Read input from stdin (provided by Claude Code)
        input_data = json.load(sys.stdin)

        success = input_data.get('success', True)
        tool_name = input_data.get('tool', 'unknown')
        output = input_data.get('output', '')

        # Analyze output for error patterns, hallucinations, and token isolation
        error_analysis = detect_error_patterns(output)
        hallucination_analysis = detect_hallucination_patterns(output)
        token_analysis = detect_token_isolation(output)

        # Check for context bloom in plan files
        context_bloom_warning = check_plan_context_bloom(input_data)

        # Check repair scope validation
        scope_validation = check_repair_scope_validation(output, input_data)

        # Check UI artifact validation
        ui_validation = check_ui_artifact_validation(output)

        # Check sanity checker gate for UI/API projects
        sanity_gate = enforce_sanity_checker_gate(output, input_data)

        if success and not error_analysis['has_errors'] and not hallucination_analysis['has_hallucinations'] and token_analysis['isolated'] and not scope_validation.get('scope_invalid', False) and not ui_validation.get('ui_artifacts_missing', False) and not sanity_gate.get('sanity_check_missing', False):
            feedback = {
                'feedback_type': 'success',
                'message': f'{tool_name} completed successfully',
                'severity': 'low'
            }
        else:
            error_msg = input_data.get('error', 'Unknown error')

            # Prioritize sanity checker gate (prevents Victory Too Early)
            if sanity_gate.get('sanity_check_missing', False):
                feedback = {
                    'feedback_type': 'error',
                    'message': f'{tool_name} attempted to advance to evaluation without sanity check: {sanity_gate["message"]}',
                    'corrective_action': 'SANITY CHECK REQUIRED - WORKFLOW BLOCKED. Must invoke @sanity-checker for UI/API features before evaluation.',
                    'severity': sanity_gate['severity'],
                    'blocks_workflow': sanity_gate['blocks_workflow']
                }
            # Then prioritize UI artifact validation (blocks hallucinated testing)
            elif ui_validation.get('ui_artifacts_missing', False):
                feedback = {
                    'feedback_type': 'error',
                    'message': f'{tool_name} attempted to advance without UI artifact validation: {ui_validation["message"]}',
                    'corrective_action': 'UI ARTIFACT VALIDATION FAILED - WORKFLOW BLOCKED. Cannot proceed to evaluation without confirmed UI artifacts.',
                    'severity': ui_validation['severity'],
                    'blocks_workflow': ui_validation['blocks_workflow']
                }
            # Then check scope validation issues (critical for repair safety)
            elif scope_validation.get('scope_invalid', False):
                feedback = {
                    'feedback_type': 'error',
                    'message': f'{tool_name} detected invalid repair scope: {scope_validation["message"]}',
                    'corrective_action': 'SCOPE VALIDATION FAILED - WORKFLOW BLOCKED. Repair scope contains non-existent paths.',
                    'severity': scope_validation['severity'],
                    'blocks_workflow': scope_validation['blocks_workflow']
                }
            # Then check token isolation issues
            elif not token_analysis['isolated']:
                issue_details = '; '.join([f"{issue['token']}: {issue['error']}" for issue in token_analysis['issues']])
                feedback = {
                    'feedback_type': 'error',
                    'message': f'{tool_name} has improperly formatted workflow tokens: {issue_details}',
                    'corrective_action': 'TOKEN ISOLATION ERROR - WORKFLOW BLOCKED. Tokens must be on their own line at the end, preceded by a blank line.',
                    'severity': 'high',
                    'blocks_workflow': True
                }
            # Then check hallucinations
            elif hallucination_analysis['has_hallucinations']:
                feedback = {
                    'feedback_type': 'error',
                    'message': f'{tool_name} produced lazy/hallucinated output: {hallucination_analysis["message"]}',
                    'corrective_action': 'HALLUCINATION DETECTED - DO NOT PROCEED. Agent left placeholder content instead of real implementation.',
                    'severity': hallucination_analysis['severity'],
                    'blocks_workflow': hallucination_analysis['blocks_workflow']
                }
            elif error_analysis['has_errors']:
                feedback = {
                    'feedback_type': 'error',
                    'message': f'{tool_name} failed with {error_analysis["error_type"]}: {error_msg}',
                    'corrective_action': 'ERROR DETECTED - DO NOT PROCEED WITH READY_FOR_* TOKENS. Address the error first.',
                    'severity': error_analysis['severity'],
                    'blocks_workflow': error_analysis['blocks_workflow']
                }
            else:
                feedback = {
                    'feedback_type': 'error',
                    'message': f'{tool_name} failed: {error_msg}',
                    'corrective_action': 'Review the error and try again',
                    'severity': 'medium'
                }

        # Output feedback
        print(json.dumps(feedback))

        # Add context bloom warning as separate feedback if needed
        if context_bloom_warning.get('warning', False):
            warning_feedback = {
                'feedback_type': 'warning',
                'message': context_bloom_warning['message'],
                'severity': context_bloom_warning['severity'],
                'blocks_workflow': False
            }
            print(json.dumps(warning_feedback))

    except Exception as e:
        # On error, provide minimal error feedback
        error_feedback = {
            'feedback_type': 'error',
            'message': f'Hook error: {str(e)}',
            'severity': 'low'
        }
        print(json.dumps(error_feedback))

if __name__ == '__main__':
    main()
