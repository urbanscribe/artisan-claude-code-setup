# Documentation Revision Rules Sub-Rule (Tier 3)
## Purpose
Defines systematic documentation maintenance, update triggers, and revision control for living documentation.

## DOCUMENTATION UPDATE TRIGGERS

### Code Change Documentation
**AUTOMATIC UPDATE REQUIREMENTS**:
```markdown
## Code Change Documentation Protocol

### Trigger Events
- [ ] New feature implementation
- [ ] API endpoint modification
- [ ] Database schema changes
- [ ] Configuration parameter additions
- [ ] Error handling modifications
- [ ] Security policy updates

### Required Documentation Updates
When code changes occur, update these documentation files:

#### /documentation/main/architecture.md
- [ ] Architecture pattern changes
- [ ] Component relationship modifications
- [ ] Technology stack updates
- [ ] Design decision rationales

#### /documentation/main/keygoals.md
- [ ] Success criteria modifications
- [ ] Business objective changes
- [ ] Performance target updates
- [ ] Compliance requirement additions

#### API Documentation
- [ ] Endpoint signature changes
- [ ] Request/response format updates
- [ ] Authentication requirement modifications
- [ ] Rate limiting policy changes

#### README.md Updates
- [ ] Installation instruction changes
- [ ] Configuration parameter additions
- [ ] Usage example updates
- [ ] Troubleshooting guide additions
```

### Architecture Documentation Updates
**PATTERN EVOLUTION TRACKING**:
```markdown
# Architecture Documentation Update Protocol

## Pattern Establishment Trigger
When implementing a solution that:
- [ ] Creates reusable component pattern
- [ ] Establishes new architectural relationship
- [ ] Introduces novel design approach
- [ ] Modifies existing architectural boundaries

## Documentation Requirements
Update /documentation/main/proposedarchitecture.md with:

### New Pattern Documentation
```
## [Pattern Name]

### Context
[When and why this pattern applies]

### Problem
[Issue this pattern solves]

### Solution
[Detailed implementation approach]

### Consequences
[Benefits, trade-offs, and considerations]

### Examples
[Code examples showing pattern usage]

### Related Patterns
[Connections to other established patterns]
```

### Implementation Evidence
- [ ] Working code demonstrating pattern
- [ ] Test coverage for pattern usage
- [ ] Performance validation
- [ ] Team consensus on pattern adoption
```

## DOCUMENTATION MAINTENANCE WORKFLOW

### Weekly Documentation Review
**REGULAR MAINTENANCE PROCESS**:
```markdown
# Weekly Documentation Review Checklist

## Completeness Check
- [ ] All code features documented
- [ ] API endpoints fully specified
- [ ] Configuration options listed
- [ ] Error conditions documented
- [ ] Performance characteristics noted

## Accuracy Verification
- [ ] Code examples functional
- [ ] Command outputs current
- [ ] Version numbers updated
- [ ] Contact information correct
- [ ] Links functional

## Clarity Assessment
- [ ] Language accessible to target audience
- [ ] Technical terms defined
- [ ] Examples clear and complete
- [ ] Navigation logical
- [ ] Formatting consistent

## Update Requirements
- [ ] Recent changes documented
- [ ] Known issues noted
- [ ] Future plans mentioned
- [ ] Contributing guidelines current
```

### Pull Request Documentation Review
**CODE REVIEW INTEGRATION**:
```markdown
# PR Documentation Review Checklist

## Content Changes
- [ ] New features documented in user guide
- [ ] API changes reflected in API docs
- [ ] Breaking changes noted in migration guide
- [ ] Error messages documented

## Technical Documentation
- [ ] Code comments added for complex logic
- [ ] Function docstrings complete
- [ ] Class documentation provided
- [ ] Type hints documented

## Review Integration
- [ ] Documentation PR linked to code PR
- [ ] Technical review includes documentation
- [ ] Documentation review includes technical validation
- [ ] Cross-team review for user-facing changes
```

## DOCUMENTATION VERSION CONTROL

### Change Tracking System
**VERSION HISTORY MAINTENANCE**:
```markdown
# Documentation Version History

## Version Control Strategy
- [ ] Documentation versioned with code releases
- [ ] Major version bumps for breaking changes
- [ ] Minor versions for feature additions
- [ ] Patch versions for corrections

## Change Documentation
Each documentation change must include:

### Change Record Format
```
## [Date] - [Version]

### Changed
- [List of changes]

### Added
- [New features or sections]

### Fixed
- [Corrections and improvements]

### Removed
- [Deprecated content]
```

### Review and Approval
- [ ] Technical accuracy reviewed
- [ ] Editorial quality checked
- [ ] Stakeholder approval obtained
- [ ] Legal compliance verified
```

## DOCUMENTATION QUALITY STANDARDS

### Content Standards
**INFORMATION QUALITY REQUIREMENTS**:
```markdown
# Documentation Quality Standards

## Accuracy
- [ ] Technical information correct
- [ ] Code examples functional
- [ ] Command outputs verified
- [ ] Version dependencies accurate
- [ ] Performance claims validated

## Completeness
- [ ] All features documented
- [ ] Prerequisites specified
- [ ] Limitations noted
- [ ] Troubleshooting covered
- [ ] Examples provided

## Clarity
- [ ] Language appropriate for audience
- [ ] Technical terms defined
- [ ] Instructions unambiguous
- [ ] Visual aids clear
- [ ] Structure logical

## Consistency
- [ ] Terminology standardized
- [ ] Format consistent
- [ ] Style guide followed
- [ ] Voice and tone uniform
```

### Technical Documentation Standards
**CODE-RELATED CONTENT**:
```markdown
# Technical Documentation Standards

## API Documentation
- [ ] All endpoints documented
- [ ] Parameters specified with types
- [ ] Response formats defined
- [ ] Error codes listed
- [ ] Authentication requirements noted

## Code Documentation
- [ ] Function purposes clear
- [ ] Parameter usage explained
- [ ] Return values described
- [ ] Exceptions documented
- [ ] Usage examples provided

## Configuration Documentation
- [ ] All options listed
- [ ] Default values specified
- [ ] Valid ranges defined
- [ ] Effects of changes explained
- [ ] Examples provided
```

## DOCUMENTATION TOOLS AND PROCESSES

### Automated Documentation Generation
**TOOL INTEGRATION**:
```python
# docs/generate_api_docs.py
"""
Automated API documentation generation
"""
import inspect
from fastapi import FastAPI
from typing import Dict, List
import json

def generate_api_docs(app: FastAPI) -> Dict[str, Any]:
    """Generate comprehensive API documentation."""
    docs = {
        'endpoints': {},
        'models': {},
        'version': '1.0.0',
        'generated_at': datetime.utcnow().isoformat()
    }

    for route in app.routes:
        if hasattr(route, 'methods') and hasattr(route, 'path'):
            endpoint_docs = {
                'path': route.path,
                'methods': list(route.methods),
                'summary': getattr(route, 'summary', ''),
                'description': getattr(route, 'description', ''),
                'parameters': [],
                'responses': {}
            }

            # Extract function signature
            if hasattr(route, 'endpoint'):
                sig = inspect.signature(route.endpoint)
                for param_name, param in sig.parameters.items():
                    if param_name not in ['request', 'response']:
                        endpoint_docs['parameters'].append({
                            'name': param_name,
                            'type': str(param.annotation),
                            'required': param.default == param.empty
                        })

            docs['endpoints'][route.path] = endpoint_docs

    return docs

# Usage
if __name__ == '__main__':
    from main import app  # Import FastAPI app
    docs = generate_api_docs(app)

    with open('api_docs.json', 'w') as f:
        json.dump(docs, f, indent=2)
```

### Documentation Testing
**VALIDATION PROCESSES**:
```python
# tests/test_documentation.py
"""
Documentation validation tests
"""
import pytest
import requests
import json
from pathlib import Path

class TestDocumentation:
    """Test documentation accuracy and completeness."""

    def test_api_docs_match_implementation(self):
        """Test that API docs match actual implementation."""
        # Load API docs
        with open('api_docs.json', 'r') as f:
            api_docs = json.load(f)

        # Test each endpoint exists
        for path, endpoint_info in api_docs['endpoints'].items():
            response = requests.options(f'http://localhost:8000{path}')
            assert response.status_code in [200, 404]  # Endpoint exists or not

            if response.status_code == 200:
                allowed_methods = response.headers.get('allow', '').split(', ')
                documented_methods = endpoint_info['methods']
                assert set(allowed_methods) == set(documented_methods)

    def test_readme_examples_work(self):
        """Test that README examples are functional."""
        # This would execute code examples from README
        # and verify they work as documented
        pass

    def test_documentation_links_valid(self):
        """Test that documentation links are not broken."""
        docs_path = Path('docs')

        for md_file in docs_path.glob('**/*.md'):
            content = md_file.read_text()

            # Find markdown links
            import re
            links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)

            for text, url in links:
                if url.startswith('http'):
                    # Test external links (with timeout)
                    try:
                        response = requests.head(url, timeout=5, allow_redirects=True)
                        assert response.status_code < 400
                    except requests.RequestException:
                        # Log but don't fail - external links can be temporarily down
                        pytest.skip(f"External link {url} not accessible")

    def test_code_examples_syntax_valid(self):
        """Test that code examples have valid syntax."""
        # This would use AST parsing to validate Python code examples
        # and other syntax checkers for different languages
        pass
```

## DOCUMENTATION GOVERNANCE

### Ownership and Responsibility
**MAINTENANCE ASSIGNMENT**:
```markdown
# Documentation Ownership Matrix

## By Component
| Component | Primary Owner | Secondary Owner | Reviewers |
|-----------|---------------|-----------------|-----------|
| API Docs | Backend Lead | API Developer | Product Manager |
| User Guide | Product Manager | Tech Writer | UX Designer |
| Architecture | Tech Lead | Senior Developer | System Architect |
| Deployment | DevOps Lead | Infrastructure Engineer | Release Manager |

## Update Frequency Requirements
- **API Documentation**: Updated with every endpoint change
- **User Guides**: Reviewed monthly, updated with feature releases
- **Architecture Docs**: Updated with architectural decisions
- **Troubleshooting**: Updated when issues discovered

## Quality Gates
- **Technical Review**: Required for technical documentation
- **Editorial Review**: Required for user-facing documentation
- **Stakeholder Review**: Required for business-critical documentation
- **Legal Review**: Required for compliance-related documentation
```

### Review and Approval Process
**QUALITY ASSURANCE WORKFLOW**:
```markdown
# Documentation Review Process

## Review Triggers
- [ ] Pull request with documentation changes
- [ ] Scheduled review cycles
- [ ] User feedback indicating issues
- [ ] System changes requiring documentation updates

## Review Checklist
### Technical Accuracy
- [ ] Information technically correct
- [ ] Code examples functional
- [ ] Commands tested and working
- [ ] Version information current

### Editorial Quality
- [ ] Grammar and spelling correct
- [ ] Language clear and concise
- [ ] Formatting consistent
- [ ] Structure logical

### Completeness
- [ ] All required information included
- [ ] Prerequisites and assumptions stated
- [ ] Edge cases covered
- [ ] Troubleshooting information provided

## Approval Requirements
- [ ] Technical reviewer approval
- [ ] Editorial reviewer approval
- [ ] Stakeholder approval for user-facing content
- [ ] Legal approval for compliance content
```

This documentation revision rules sub-rule establishes systematic processes for maintaining accurate, current, and comprehensive documentation that evolves with the codebase. The rules ensure documentation quality, establish update triggers, and provide governance for documentation maintenance across the development lifecycle.```
<xai:function_call name="write">
<parameter name="file_path">claude_code/setup/.claude/rules/sub/external_verification.md
