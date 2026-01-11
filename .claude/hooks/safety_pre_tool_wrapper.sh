#!/bin/bash
# Find the project root by looking for .claude directory
PROJECT_ROOT=$(find . -name ".claude" -type d 2>/dev/null | head -1 | xargs dirname 2>/dev/null)
if [ -z "$PROJECT_ROOT" ]; then
  PROJECT_ROOT=$(git rev-parse --show-toplevel 2>/dev/null)
fi
if [ -z "$PROJECT_ROOT" ]; then
  PROJECT_ROOT=$(pwd)
fi

# Change to project root and run the script
cd "$PROJECT_ROOT" && python3 .claude/hooks/safety_pre_tool.py
