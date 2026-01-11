# Tool Wildcards Sub-Rule (Tier 3)
## Purpose
Defines Claude Code v2.1 wildcard permission configurations for secure, controlled tool access.

## WILDCARD PERMISSION PATTERNS

### Bash Command Wildcards
**DOCKER OPERATIONS**:
```json
{
  "Bash": {
    "allow": [
      "docker compose ps",
      "docker compose logs",
      "docker compose up -d",
      "docker compose down",
      "docker build --no-cache .",
      "docker run --rm **"
    ],
    "deny": [
      "docker system prune",
      "docker volume rm **",
      "docker rmi **",
      "docker compose down -v"
    ]
  }
}
```

**PACKAGE MANAGEMENT**:
```json
{
  "Bash": {
    "allow": [
      "npm install",
      "npm ci",
      "npm run build",
      "npm run test",
      "pip install -r requirements.txt",
      "pip install --upgrade **",
      "poetry install",
      "poetry add **"
    ],
    "deny": [
      "npm uninstall **",
      "npm prune",
      "pip uninstall **",
      "poetry remove **"
    ]
  }
}
```

### File Operation Wildcards
**CODE FILE ACCESS**:
```json
{
  "Edit": {
    "allow": [
      "**/*.py",
      "**/*.js",
      "**/*.ts",
      "**/*.html",
      "**/*.css",
      "**/*.md",
      "**/*.json",
      "**/*.yaml",
      "**/*.yml"
    ],
    "deny": [
      "**/node_modules/**",
      "**/__pycache__/**",
      "**/.git/**",
      "**/dist/**",
      "**/build/**",
      "**/*.lock",
      "**/*-lock.*"
    ]
  }
}
```

**CONFIGURATION FILES**:
```json
{
  "Read": {
    "allow": [
      "**/pyproject.toml",
      "**/requirements*.txt",
      "**/package.json",
      "**/tsconfig.json",
      "**/docker-compose*.yml",
      "**/.env.example",
      "**/README.md",
      "**/docs/**"
    ],
    "deny": [
      "**/.env",
      "**/.env.local",
      "**/.env.production",
      "**/secrets/**",
      "**/*.key",
      "**/*.pem"
    ]
  }
}
```

## TOOL-SPECIFIC WILDCARDS

### Run Command Permissions
**DEVELOPMENT SERVERS**:
```json
{
  "Run": {
    "allow": [
      "python manage.py runserver",
      "python -m uvicorn main:app",
      "npm start",
      "npm run dev",
      "flask run",
      "django-admin runserver"
    ],
    "deny": [
      "python manage.py shell",
      "python -c 'import os; os.system(**)'",
      "eval **",
      "exec **"
    ]
  }
}
```

### Search and Grep Permissions
**CODE ANALYSIS**:
```json
{
  "Grep": {
    "allow": [
      "**/*.py",
      "**/*.js",
      "**/*.ts",
      "**/*.html",
      "**/*.css"
    ],
    "deny": [
      "**/node_modules/**",
      "**/__pycache__/**",
      "**/.git/**",
      "**/dist/**",
      "**/build/**",
      "**/*.log",
      "**/*.tmp"
    ]
  }
}
```

## SECURITY WILDCARD PATTERNS

### Destructive Operation Prevention
**ABSOLUTE DENIES**:
```json
{
  "Bash": {
    "deny": [
      "rm -rf /**",
      "rm -rf /*",
      "rm -rf /home/**",
      "rm -rf /usr/**",
      "rm -rf /etc/**",
      "format **",
      "fdisk **",
      "mkfs **",
      "dd if=**",
      "shutdown",
      "reboot",
      "halt",
      "systemctl disable **",
      "systemctl stop **"
    ]
  }
}
```

### Database Operation Safety
**CONTROLLED ACCESS**:
```json
{
  "Bash": {
    "allow": [
      "psql -d ** -c 'SELECT COUNT(*) FROM **'",
      "mysql -e 'SELECT COUNT(*) FROM **'",
      "sqlite3 ** '.schema'",
      "sqlite3 ** 'SELECT COUNT(*) FROM **'"
    ],
    "deny": [
      "psql -d ** -c 'DROP **'",
      "psql -d ** -c 'DELETE FROM **'",
      "mysql -e 'DROP **'",
      "mysql -e 'DELETE FROM **'",
      "sqlite3 ** 'DROP **'",
      "sqlite3 ** 'DELETE FROM **'"
    ]
  }
}
```

## CONTEXT-AWARE WILDCARDS

### Project-Specific Permissions
**FRAMEWORK-BASED ACCESS**:
```json
{
  "Edit": {
    "allow": [
      "src/**/*.py",
      "app/**/*.py",
      "api/**/*.py",
      "tests/**/*.py",
      "migrations/**/*.py",
      "**/templates/**/*.html",
      "**/static/**/*.css",
      "**/static/**/*.js"
    ],
    "deny": [
      "migrations/versions/*.py",
      "**/migrations/**",
      "**/node_modules/**",
      "**/__pycache__/**"
    ]
  }
}
```

### Environment-Specific Controls
**DEVELOPMENT VS PRODUCTION**:
```json
{
  "Bash": {
    "allow_dev": [
      "python manage.py shell",
      "npm run dev",
      "docker compose up",
      "pytest --cov-report html"
    ],
    "allow_prod": [
      "python manage.py migrate",
      "npm run build",
      "docker compose up -d",
      "pytest"
    ],
    "deny_all": [
      "rm -rf **",
      "sudo **",
      "> /dev/null",
      "curl ** | bash"
    ]
  }
}
```

## WILDCARD VALIDATION RULES

### Permission Consistency
**LOGICAL VALIDATION**:
- [ ] Allow patterns don't conflict with deny patterns
- [ ] Wildcards properly scoped to project boundaries
- [ ] Tool-specific permissions appropriate for tool capabilities
- [ ] Security-critical operations explicitly denied

### Pattern Effectiveness
**COVERAGE VERIFICATION**:
- [ ] Common legitimate operations covered by allow patterns
- [ ] Destructive operations blocked by deny patterns
- [ ] Wildcard patterns tested against real file structures
- [ ] Permission changes logged for audit trails

### Maintenance Requirements
**PATTERN UPDATES**:
- [ ] New file types added to appropriate allow patterns
- [ ] Deprecated patterns removed from allow lists
- [ ] Security vulnerabilities addressed with new deny patterns
- [ ] Tool updates reflected in permission configurations

## WILDCARD TESTING PROTOCOLS

### Permission Testing
**AUTOMATED VALIDATION**:
```python
def test_wildcard_permissions():
    # Test allow patterns
    assert matches_pattern("src/main.py", ["src/**/*.py"])
    assert matches_pattern("tests/test_user.py", ["tests/**/*.py"])

    # Test deny patterns
    assert not matches_pattern("node_modules/package.json", ["**/node_modules/**"])
    assert not matches_pattern(".env", ["**/.env*"])

    # Test conflicts
    assert no_conflicts([
        "allow": ["src/**/*.py"],
        "deny": ["src/**/*.pyc"]
    ])
```

### Integration Testing
**END-TO-END VALIDATION**:
- [ ] Tool executions respect wildcard permissions
- [ ] Denied operations properly blocked with clear messages
- [ ] Allowed operations execute successfully
- [ ] Permission changes take effect immediately

### Security Auditing
**VULNERABILITY ASSESSMENT**:
- [ ] Wildcard patterns don't allow unintended access
- [ ] Deny patterns comprehensive for destructive operations
- [ ] Privilege escalation prevented through pattern restrictions
- [ ] Audit logging captures all permission decisions

## WILDCARD MANAGEMENT WORKFLOW

### Permission Definition
**STRUCTURED APPROACH**:
1. **Tool Analysis**: Understand tool capabilities and security implications
2. **Use Case Identification**: Document legitimate use cases for each tool
3. **Pattern Development**: Create allow patterns for legitimate operations
4. **Security Review**: Define deny patterns for dangerous operations
5. **Testing Validation**: Test patterns against real scenarios

### Permission Updates
**CHANGE MANAGEMENT**:
1. **Change Request**: Document need for permission modification
2. **Security Review**: Assess security implications of change
3. **Testing**: Validate change doesn't break existing functionality
4. **Deployment**: Update permissions with audit trail
5. **Monitoring**: Monitor for unexpected permission usage

### Incident Response
**VIOLATION HANDLING**:
1. **Detection**: Identify permission violation attempts
2. **Analysis**: Determine if legitimate need or security threat
3. **Response**: Block malicious attempts, adjust permissions for legitimate needs
4. **Documentation**: Record incident and resolution for future reference
5. **Prevention**: Update patterns to prevent similar incidents

## PERFORMANCE CONSIDERATIONS

### Pattern Efficiency
**OPTIMIZATION REQUIREMENTS**:
- [ ] Wildcard patterns compile efficiently
- [ ] Pattern matching doesn't impact tool execution performance
- [ ] Memory usage remains bounded with large pattern sets
- [ ] CPU overhead minimal for permission checks

### Scalability Planning
**GROWTH ACCOMMODATION**:
- [ ] Pattern sets support project growth
- [ ] New team members don't require individual permission grants
- [ ] Multi-project setups supported through context-aware patterns
- [ ] Cloud deployment environments properly configured

## COMPLIANCE INTEGRATION

### Regulatory Requirements
**STANDARDS ALIGNMENT**:
- [ ] SOX compliance for financial systems
- [ ] HIPAA compliance for healthcare data
- [ ] GDPR compliance for personal data
- [ ] Industry-specific security frameworks

### Audit Preparation
**TRAIL MAINTENANCE**:
- [ ] Permission changes logged with justification
- [ ] Access attempts recorded for forensic analysis
- [ ] Pattern updates documented with business rationale
- [ ] Regular permission audits conducted and documented
