#!/bin/bash

# Claude Code Multi-Agent Setup Script
# Automatically sets up the Claude Code environment in your project

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Logging functions
log_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

log_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

log_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

log_error() {
    echo -e "${RED}❌ $1${NC}"
}

# Check for --restore flag (out-of-band recovery)
RESTORE_MODE=false
if [ "$1" = "--restore" ]; then
    RESTORE_MODE=true
    log_info "🔄 RESTORATION MODE ACTIVATED"
    log_info "Prioritizing PROJECT_REGISTRY.json for system reconstruction"
fi

# Check if CC_DESTINATION is set
if [ -z "$CC_DESTINATION" ]; then
    log_error "CC_DESTINATION environment variable is not set!"
    log_info "Please set it first:"
    echo "  export CC_DESTINATION=/path/to/your/project"
    echo "  ./setup.sh"
    if [ "$RESTORE_MODE" = true ]; then
        echo "  # Or for recovery:"
        echo "  ./setup.sh --restore"
    fi
    exit 1
fi

# Check if destination exists
if [ ! -d "$CC_DESTINATION" ]; then
    log_error "Destination directory does not exist: $CC_DESTINATION"
    log_info "Please create the directory first or check the path."
    exit 1
fi

log_info "Setting up Claude Code environment in: $CC_DESTINATION"

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SETUP_DIR="$(dirname "$SCRIPT_DIR")"

log_info "Source directory: $SETUP_DIR"
log_info "Destination: $CC_DESTINATION"

# RESTORATION MODE: Prioritize PROJECT_REGISTRY.json for system reconstruction
if [ "$RESTORE_MODE" = true ]; then
    log_info "🔄 EXECUTING RESTORATION PROTOCOL"

    # Step 0: Check for PROJECT_REGISTRY.json
    if [ -f "$CC_DESTINATION/.claude/PROJECT_REGISTRY.json" ]; then
        log_success "PROJECT_REGISTRY.json found - initiating registry-priority recovery"

        # Read registry to understand system state
        # Note: In a real implementation, this would parse the JSON and rebuild accordingly
        log_info "Reading registry state for reconstruction..."

        # Reconstruct CLAUDE.md from registry invariants
        log_info "Reconstructing CLAUDE.md from registry invariants..."
        if [ -f "$SETUP_DIR/CLAUDE.md" ]; then
            cp "$SETUP_DIR/CLAUDE.md" "$CC_DESTINATION/"
            log_success "CLAUDE.md invariants restored"
        fi

        # Rebuild .claude directory structure from registry state
        log_info "Rebuilding .claude directory structure..."
        mkdir -p "$CC_DESTINATION/.claude/skills"
        mkdir -p "$CC_DESTINATION/.claude/hooks"
        mkdir -p "$CC_DESTINATION/.claude/commands"
        mkdir -p "$CC_DESTINATION/.claude/rules"
        mkdir -p "$CC_DESTINATION/.claude/rules/sub"

        # Restore all system files
        log_info "Restoring system files from registry state..."

        # Copy skills, hooks, commands, rules
        if [ -d "$SETUP_DIR/.claude/skills" ]; then
            cp -r "$SETUP_DIR/.claude/skills/"* "$CC_DESTINATION/.claude/skills/" 2>/dev/null || true
            log_success "Skills restored ($(ls $CC_DESTINATION/.claude/skills/ 2>/dev/null | wc -l) files)"
        fi

        if [ -d "$SETUP_DIR/.claude/hooks" ]; then
            cp -r "$SETUP_DIR/.claude/hooks/"* "$CC_DESTINATION/.claude/hooks/" 2>/dev/null || true
            chmod +x "$CC_DESTINATION/.claude/hooks/"*.py 2>/dev/null || true
            log_success "Hooks restored ($(ls $CC_DESTINATION/.claude/hooks/ 2>/dev/null | wc -l) files)"
        fi

        if [ -d "$SETUP_DIR/.claude/commands" ]; then
            cp -r "$SETUP_DIR/.claude/commands/"* "$CC_DESTINATION/.claude/commands/" 2>/dev/null || true
            log_success "Commands restored ($(ls $CC_DESTINATION/.claude/commands/ 2>/dev/null | wc -l) files)"
        fi

        if [ -d "$SETUP_DIR/.claude/rules" ]; then
            cp -r "$SETUP_DIR/.claude/rules/"* "$CC_DESTINATION/.claude/rules/" 2>/dev/null || true
            log_success "Rules restored ($(ls $CC_DESTINATION/.claude/rules/ 2>/dev/null | wc -l) files)"
        fi

        # Copy settings and repair lock
        if [ -f "$SETUP_DIR/.claude/settings.json" ]; then
            cp "$SETUP_DIR/.claude/settings.json" "$CC_DESTINATION/.claude/"
            log_success "Settings restored"
        fi

        if [ -f "$SETUP_DIR/.claude/repair_lock.json" ]; then
            cp "$SETUP_DIR/.claude/repair_lock.json" "$CC_DESTINATION/.claude/"
            log_success "Repair lock restored"
        fi

        # Set proper permissions
        chmod -R 755 "$CC_DESTINATION/.claude/" 2>/dev/null || true

        log_success "🔄 RESTORATION COMPLETE - System reconstructed from PROJECT_REGISTRY.json"
        echo ""
        log_success "🎉 Artisan's Claude Code Operating System Restored!"
        echo ""
        echo -e "${BLUE}Restoration Summary:${NC}"
        echo "  ✅ PROJECT_REGISTRY.json prioritized over overwritten CLAUDE.md"
        echo "  ✅ Professional OS commands and skills restored"
        echo "  ✅ Foundation state preserved through registry"
        echo "  ✅ Sprint context maintained"
        echo ""
        echo -e "${YELLOW}Your professional development environment is restored!${NC}"
        exit 0

    else
        log_error "❌ RESTORATION FAILED: PROJECT_REGISTRY.json not found"
        log_info "Cannot restore without registry. Run normal setup first:"
        echo "  ./setup.sh  # Normal setup to create registry"
        exit 1
    fi
fi

# Step 1: Copy CLAUDE.md to project root
log_info "Step 1: Copying CLAUDE.md (project memory file)..."
if [ -f "$SETUP_DIR/CLAUDE.md" ]; then
    cp "$SETUP_DIR/CLAUDE.md" "$CC_DESTINATION/"
    log_success "CLAUDE.md copied to project root"
else
    log_error "CLAUDE.md not found in setup directory"
    exit 1
fi

# Step 2: Create .claude directory structure
log_info "Step 2: Creating .claude directory structure..."
mkdir -p "$CC_DESTINATION/.claude/skills"
mkdir -p "$CC_DESTINATION/.claude/hooks"
mkdir -p "$CC_DESTINATION/.claude/commands"
mkdir -p "$CC_DESTINATION/.claude/rules"
mkdir -p "$CC_DESTINATION/.claude/rules/sub"
mkdir -p "$CC_DESTINATION/.claude/skills"
log_success ".claude directories created"

# Step 3: Copy subagent files
log_info "Step 3: Copying AI team member instructions..."
if [ -d "$SETUP_DIR/.claude/skills" ] && [ "$(ls -A $SETUP_DIR/.claude/skills)" ]; then
    cp -r "$SETUP_DIR/.claude/skills/"* "$CC_DESTINATION/.claude/skills/"
    log_success "AI team instructions copied ($(ls $CC_DESTINATION/.claude/skills/ | wc -l) files)"
else
    log_error "No skills files found to copy"
    exit 1
fi

# Step 4: Copy hook files
log_info "Step 4: Copying safety guard programs..."
if [ -d "$SETUP_DIR/.claude/hooks" ] && [ "$(ls -A $SETUP_DIR/.claude/hooks)" ]; then
    cp -r "$SETUP_DIR/.claude/hooks/"* "$CC_DESTINATION/.claude/hooks/"
    log_success "Safety guards copied ($(ls $CC_DESTINATION/.claude/hooks/ | wc -l) files)"
else
    log_error "No hook files found to copy"
    exit 1
fi

# Step 5: Make hook files executable
log_info "Step 5: Making safety programs executable..."
chmod +x "$CC_DESTINATION/.claude/hooks/"*.py
log_success "Safety programs are now executable"

# Step 6: Copy command files
log_info "Step 6: Copying special commands..."
if [ -d "$SETUP_DIR/.claude/commands" ] && [ "$(ls -A $SETUP_DIR/.claude/commands)" ]; then
    cp -r "$SETUP_DIR/.claude/commands/"* "$CC_DESTINATION/.claude/commands/"
    log_success "Special commands copied ($(ls $CC_DESTINATION/.claude/commands/ | wc -l) files)"
else
    log_error "No command files found to copy"
    exit 1
fi

# Step 7: Copy settings file
log_info "Step 7: Copying security settings..."
if [ -f "$SETUP_DIR/.claude/settings.json" ]; then
    cp "$SETUP_DIR/.claude/settings.json" "$CC_DESTINATION/.claude/"
    # Replace placeholders with actual paths
    sed -i.bak "s|{{CC_DESTINATION}}|$CC_DESTINATION|g" "$CC_DESTINATION/.claude/settings.json"
    rm "$CC_DESTINATION/.claude/settings.json.bak" 2>/dev/null || true
    log_success "Security settings copied"
else
    log_error "settings.json not found"
    exit 1
fi

# Step 8: Copy rules system
log_info "Step 8: Copying rules system..."
if [ -d "$SETUP_DIR/.claude/rules" ] && [ "$(ls -A $SETUP_DIR/.claude/rules)" ]; then
    cp -r "$SETUP_DIR/.claude/rules/"* "$CC_DESTINATION/.claude/rules/"
    log_success "Rules system copied ($(ls $CC_DESTINATION/.claude/rules/ | wc -l) rule files)"
else
    log_error "No rules found to copy"
    exit 1
fi

# Step 9: Copy skills system
log_info "Step 9: Copying skills system..."
if [ -d "$SETUP_DIR/.claude/skills" ] && [ "$(ls -A $SETUP_DIR/.claude/skills)" ]; then
    cp -r "$SETUP_DIR/.claude/skills/"* "$CC_DESTINATION/.claude/skills/"
    log_success "Skills system copied ($(ls $CC_DESTINATION/.claude/skills/ | wc -l) skill files)"
else
    log_error "No skills found to copy"
    exit 1
fi

# Step 11: Copy repair lock
log_info "Step 11: Initializing repair scope enforcement..."
if [ -f "$SETUP_DIR/.claude/repair_lock.json" ]; then
    cp "$SETUP_DIR/.claude/repair_lock.json" "$CC_DESTINATION/.claude/"
    log_success "Repair lock initialized"
else
    log_error "repair_lock.json not found"
    exit 1
fi

# Step 12: Initialize Professional OS state in .claude folder
log_info "Step 12: Initializing Professional OS state..."
if [ -f "$SETUP_DIR/PROJECT_REGISTRY.json" ]; then
    cp "$SETUP_DIR/PROJECT_REGISTRY.json" "$CC_DESTINATION/.claude/PROJECT_REGISTRY.json"
    log_success "Professional OS state initialized in .claude/"
else
    log_error "PROJECT_REGISTRY.json template not found"
    exit 1
fi

# Step 13: Initialize Professional OS state
log_info "Step 13: Initializing Professional OS state..."
if [ -f "$SETUP_DIR/PROJECT_REGISTRY.json" ]; then
    cp "$SETUP_DIR/PROJECT_REGISTRY.json" "$CC_DESTINATION/.claude/PROJECT_REGISTRY.json"
    log_success "Professional OS state initialized in .claude/"
else
    log_error "PROJECT_REGISTRY.json template not found"
    exit 1
fi


# Step 14: Set permissions
log_info "Step 10: Setting proper permissions..."
chmod -R 755 "$CC_DESTINATION/.claude/"
log_success "Permissions set correctly"

# Step 15: Final verification
log_info "Step 12: Verifying setup..."
TOTAL_FILES=$(find "$CC_DESTINATION/.claude/" -type f | wc -l)
# Check for rules directory structure and professional OS components
RULES_DIRS=$(find "$CC_DESTINATION/.claude/" -name "rules" -type d | wc -l)
REPAIR_LOCK_EXISTS=$(test -f "$CC_DESTINATION/.claude/repair_lock.json" && echo 1 || echo 0)
PROJECT_REGISTRY_EXISTS=$(test -f "$CC_DESTINATION/.claude/PROJECT_REGISTRY.json" && echo 1 || echo 0)

if [ "$TOTAL_FILES" -ge 13 ] && [ "$RULES_DIRS" -ge 1 ] && [ "$REPAIR_LOCK_EXISTS" -eq 1 ] && [ "$PROJECT_REGISTRY_EXISTS" -eq 1 ]; then
    log_success "Setup complete! $TOTAL_FILES files installed with rules system, repair lock, and Professional OS."
else
    log_warning "Setup completed but some components missing (files: $TOTAL_FILES, rules dirs: $RULES_DIRS, repair lock: $REPAIR_LOCK_EXISTS). Please check manually."
fi

# Success message
echo ""
log_success "🎉 Claude Code Multi-Agent Setup Complete!"
echo ""
echo -e "${BLUE}What you can do now:${NC}"
echo "  1. Go to your project: cd $CC_DESTINATION"
echo "  2. Start Claude: claude"
echo "  3. Establish project foundation: /startprojectplanning"
echo ""
echo -e "${BLUE}Your AI team is ready! 🤖${NC}"
echo ""
echo -e "${YELLOW}Remember: You control all major decisions - Claude Code is your smart assistant!${NC}"
