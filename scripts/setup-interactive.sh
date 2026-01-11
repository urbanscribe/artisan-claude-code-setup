#!/bin/bash

# Claude Code Interactive Setup Script
# Guided installation with questions and customization

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
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

log_question() {
    echo -e "${CYAN}❓ $1${NC}"
}

log_header() {
    echo -e "${PURPLE}🚀 $1${NC}"
    echo "─────────────────────────────────────────────────────────────"
}

# Function to get user input with default
get_input() {
    local prompt="$1"
    local default="$2"
    local response

    if [ -n "$default" ]; then
        read -p "$(echo -e ${CYAN}"❓ $prompt [$default]: "${NC})" response
        response=${response:-$default}
    else
        read -p "$(echo -e ${CYAN}"❓ $prompt: "${NC})" response
        while [ -z "$response" ]; do
            read -p "$(echo -e ${RED}"Required. $prompt: "${NC})" response
        done
    fi

    echo "$response"
}

# Function to get yes/no with default
get_yes_no() {
    local prompt="$1"
    local default="$2"
    local response

    while true; do
        if [ "$default" = "y" ]; then
            read -p "$(echo -e ${CYAN}"❓ $prompt [Y/n]: "${NC})" response
            response=${response:-y}
        else
            read -p "$(echo -e ${CYAN}"❓ $prompt [y/N]: "${NC})" response
            response=${response:-n}
        fi

        case $response in
            [Yy]|[Yy][Ee][Ss]) echo "y"; return ;;
            [Nn]|[Nn][Oo]) echo "n"; return ;;
            *) log_warning "Please answer yes or no." ;;
        esac
    done
}

# Function to validate path exists
validate_path() {
    local path="$1"
    local description="$2"

    if [ ! -d "$path" ]; then
        log_error "$description directory does not exist: $path"
        return 1
    fi
    return 0
}

# Function to create directory if it doesn't exist
ensure_dir() {
    local dir="$1"
    local description="$2"

    if [ ! -d "$dir" ]; then
        log_info "Creating $description directory: $dir"
        mkdir -p "$dir"
        log_success "$description directory created"
    else
        log_info "$description directory already exists"
    fi
}

# Function to copy with error handling
safe_copy() {
    local src="$1"
    local dst="$2"
    local description="$3"

    if [ -e "$src" ]; then
        cp -r "$src" "$dst"
        log_success "$description copied"
    else
        log_error "$description not found: $src"
        return 1
    fi
}

# Main setup function
main() {
    echo ""
    log_header "CLAUDE CODE INTERACTIVE SETUP"
    echo "This guided setup will ask you questions to customize"
    echo "the installation for your specific project needs."
    echo ""

    # Step 1: Get project type
    echo ""
    log_header "STEP 1: PROJECT TYPE"
    PROJECT_TYPE=$(get_input "Are you setting up Claude Code for a NEW project or EXISTING project?" "existing")

    case $PROJECT_TYPE in
        [Nn][Ee][Ww])
            PROJECT_TYPE="new"
            log_info "Setting up for a NEW project"
            ;;
        [Ee][Xx][Ii][Ss][Tt]*)
            PROJECT_TYPE="existing"
            log_info "Setting up for an EXISTING project"
            ;;
        *)
            PROJECT_TYPE="existing"
            log_info "Defaulting to existing project setup"
            ;;
    esac

    # Step 2: Get project path
    echo ""
    log_header "STEP 2: PROJECT LOCATION"
    DEFAULT_PATH=$(pwd)
    PROJECT_PATH=$(get_input "What is the full path to your project directory?" "$DEFAULT_PATH")

    # Validate project path
    if [ "$PROJECT_TYPE" = "existing" ]; then
        if ! validate_path "$PROJECT_PATH" "Project"; then
            log_error "Cannot continue without valid project directory"
            exit 1
        fi
    fi

    # Step 3: Gather project information
    echo ""
    log_header "STEP 3: PROJECT INFORMATION"

    if [ "$PROJECT_TYPE" = "existing" ]; then
        # For existing projects, gather more details
        HAS_DOCS=$(get_yes_no "Does your project have existing documentation?" "y")

        if [ "$HAS_DOCS" = "y" ]; then
            DOCS_PATH=$(get_input "Where is your documentation folder? (relative to project root or absolute path)" "docs")

            # Check if it's relative or absolute
            if [[ "$DOCS_PATH" != /* ]]; then
                DOCS_PATH="$PROJECT_PATH/$DOCS_PATH"
            fi

            if validate_path "$DOCS_PATH" "Documentation"; then
                USE_EXISTING_DOCS="y"
                log_info "Will integrate with existing documentation at: $DOCS_PATH"
            else
                USE_EXISTING_DOCS="n"
                log_warning "Documentation path not found. Will create new structure."
            fi
        else
            USE_EXISTING_DOCS="n"
            DOCS_PATH="$PROJECT_PATH/documentation"
            log_info "Will create new documentation structure"
        fi

        # Tech stack questions
        TECH_STACK=$(get_input "What is your primary tech stack? (e.g., Python/FastAPI, Node.js/React, etc.)" "Python")
        log_info "Tech stack: $TECH_STACK"

        USE_GIT=$(get_yes_no "Is this project using Git?" "y")
        if [ "$USE_GIT" = "y" ]; then
            WORKTREE_SUPPORT=$(get_yes_no "Do you want worktree isolation for parallel development?" "y")
        else
            WORKTREE_SUPPORT="n"
            log_warning "Git worktree features will be disabled (project not using Git)"
        fi

    else
        # For new projects
        USE_EXISTING_DOCS="n"
        DOCS_PATH="$PROJECT_PATH/documentation"
        TECH_STACK=$(get_input "What tech stack will you be using?" "Python/FastAPI")
        WORKTREE_SUPPORT="y"
        log_info "Setting up for new project with tech stack: $TECH_STACK"
    fi

    # Step 4: Advanced options
    echo ""
    log_header "STEP 4: ADVANCED OPTIONS"

    DEBUG_MODE=$(get_yes_no "Enable debug mode for development?" "n")
    ENTERPRISE_MODE=$(get_yes_no "Enable enterprise security features?" "y")

    if [ "$ENTERPRISE_MODE" = "y" ]; then
        AUDIT_LOGGING=$(get_yes_no "Enable comprehensive audit logging?" "y")
    else
        AUDIT_LOGGING="n"
    fi

    # Step 5: Confirmation
    echo ""
    log_header "STEP 5: SETUP CONFIRMATION"

    echo "Please review your configuration:"
    echo "📁 Project Path: $PROJECT_PATH"
    echo "🏗️  Project Type: $PROJECT_TYPE"
    echo "📚 Documentation: ${USE_EXISTING_DOCS:-n} (${DOCS_PATH:-$PROJECT_PATH/documentation})"
    echo "⚙️  Tech Stack: $TECH_STACK"
    echo "🔧 Worktree Support: ${WORKTREE_SUPPORT:-n}"
    echo "🐛 Debug Mode: $DEBUG_MODE"
    echo "🏢 Enterprise Mode: $ENTERPRISE_MODE"
    echo "📊 Audit Logging: ${AUDIT_LOGGING:-n}"
    echo ""

    CONFIRM=$(get_yes_no "Proceed with this configuration?" "y")

    if [ "$CONFIRM" = "n" ]; then
        log_info "Setup cancelled. Run the script again to restart."
        exit 0
    fi

    # Step 6: Execute setup
    echo ""
    log_header "STEP 6: EXECUTING SETUP"

    # Set the destination for the automated script
    export CC_DESTINATION="$PROJECT_PATH"

    # Get script locations
    SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    SETUP_DIR="$(dirname "$SCRIPT_DIR")"

    log_info "Starting automated setup..."
    log_info "Source: $SETUP_DIR"
    log_info "Destination: $PROJECT_PATH"

    # Run the automated setup script
    if [ -f "$SCRIPT_DIR/setup.sh" ]; then
        bash "$SCRIPT_DIR/setup.sh"
    else
        log_error "setup.sh not found in scripts directory"
        exit 1
    fi

    # Step 7: Post-setup customization
    echo ""
    log_header "STEP 7: POST-SETUP CUSTOMIZATION"

    # Handle existing documentation
    if [ "$USE_EXISTING_DOCS" = "y" ] && [ -d "$DOCS_PATH" ]; then
        log_info "Setting up existing documentation integration..."

        # Create the main documentation link
        MAIN_DOCS="$PROJECT_PATH/documentation/main"

        # Copy existing docs or create symlinks
        if [ "$DOCS_PATH" != "$MAIN_DOCS" ]; then
            ensure_dir "$MAIN_DOCS" "main documentation"

            # Ask user how to handle existing docs
            DOC_METHOD=$(get_input "How to integrate existing docs? (copy/symlink/leave)" "copy")

            case $DOC_METHOD in
                [Cc][Oo][Pp][Yy])
                    log_info "Copying existing documentation..."
                    cp -r "$DOCS_PATH"/* "$MAIN_DOCS/" 2>/dev/null || true
                    log_success "Existing documentation copied"
                    ;;
                [Ss][Yy][Mm]*)
                    log_info "Creating documentation symlink..."
                    ln -sf "$DOCS_PATH" "$MAIN_DOCS/existing-docs"
                    log_success "Documentation symlink created"
                    ;;
                *)
                    log_info "Leaving existing documentation as-is"
                    ;;
            esac
        fi
    fi

    # Customize CLAUDE.md based on tech stack
    if [ -f "$PROJECT_PATH/CLAUDE.md" ]; then
        log_info "Customizing CLAUDE.md for your tech stack..."

        # Add tech stack specific guidance
        case $TECH_STACK in
            *[Pp]ython*)
                TECH_ADDITION="### Python-Specific Patterns
- **Async/Await**: Use async patterns for I/O operations (see rules/sub/async_patterns.md)
- **Type Hints**: Required for all function parameters and return values
- **Session Management**: Use get_db_session_context() for database operations"
                ;;
            *[Nn]ode*[Jj]s*|*[Rr]eact*)
                TECH_ADDITION="### JavaScript/Node.js Patterns
- **Async/Await**: Use async patterns for I/O operations (see rules/sub/async_patterns.md)
- **ES6+ Features**: Modern JavaScript patterns preferred
- **Error Handling**: Comprehensive try/catch with proper error propagation"
                ;;
            *)
                TECH_ADDITION="### Tech Stack Integration
- Consult rules/sub/arch_basics.md for fundamental patterns
- Use dependency-integrator.md for library selections
- Follow async_patterns.md for concurrency needs"
                ;;
        esac

        echo -e "\n$TECH_ADDITION" >> "$PROJECT_PATH/CLAUDE.md"
        log_success "Tech stack guidance added to CLAUDE.md"
    fi

    # Configure debug mode
    if [ "$DEBUG_MODE" = "y" ]; then
        log_info "Enabling debug mode..."

        # Create debug configuration
        cat > "$PROJECT_PATH/.claude/debug-config.json" << EOF
{
  "debug_mode": true,
  "ui_debug_accordions": true,
  "enhanced_logging": true,
  "performance_monitoring": true
}
EOF
        log_success "Debug configuration created"
    fi

    # Enterprise features
    if [ "$ENTERPRISE_MODE" = "y" ]; then
        log_info "Configuring enterprise features..."

        # Enhanced security settings
        if [ -f "$PROJECT_PATH/.claude/settings.json" ]; then
            # Add enterprise security settings
            sed -i 's/"allow": "allow"/"allow": "prompt"/g' "$PROJECT_PATH/.claude/settings.json" 2>/dev/null || true
            log_success "Enterprise security settings applied"
        fi

        # Audit logging setup
        if [ "$AUDIT_LOGGING" = "y" ]; then
            ensure_dir "$PROJECT_PATH/logs" "audit logs"
            log_success "Audit logging directory created"
        fi
    fi

    # Step 8: Final instructions
    echo ""
    log_header "🎉 SETUP COMPLETE!"

    echo ""
    echo "Your Claude Code AI team is now ready!"
    echo ""
    echo "📋 Next Steps:"
    echo "1. cd $PROJECT_PATH"
    echo "2. claude"
    echo "3. /implement \"Describe your first feature\""
    echo ""

    if [ "$PROJECT_TYPE" = "existing" ] && [ "$USE_EXISTING_DOCS" = "y" ]; then
        echo "4. /collect-knowledge \"Integrate existing project documentation\""
        echo ""
    fi

    echo "📚 Documentation:"
    echo "- README.md: Complete usage guide"
    echo "- CLAUDE.md: Project rules (auto-loaded)"
    echo "- .claude/: All AI team configurations"
    echo ""

    if [ "$DEBUG_MODE" = "y" ]; then
        echo "🐛 Debug Mode: Enabled (check .claude/debug-config.json)"
        echo ""
    fi

    if [ "$ENTERPRISE_MODE" = "y" ]; then
        echo "🏢 Enterprise Features: Enabled with enhanced security"
        echo ""
    fi

    log_success "Interactive setup completed successfully!"
    echo ""
    echo "🚀 Happy coding with your AI development team!"
}

# Run main function
main "$@"
