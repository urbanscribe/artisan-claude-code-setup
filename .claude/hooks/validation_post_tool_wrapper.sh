#!/bin/bash
# Get the directory where this script is located (.claude/hooks)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# .claude directory is parent of hooks
CLAUDE_DIR="$(dirname "$SCRIPT_DIR")"
# Project root is parent of .claude
PROJECT_ROOT="$(dirname "$CLAUDE_DIR")"

# Change to project root and run the script, passing stdin through
cd "$PROJECT_ROOT" && python3 .claude/hooks/validation_post_tool.py < /dev/stdin
