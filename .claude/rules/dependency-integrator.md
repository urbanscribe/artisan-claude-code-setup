# Dependency Integrator Rule (Main Rule - Tier 2)
## Purpose
Manages external dependency research, validation, and integration with no open architectural choices.

## DEPENDENCY DISCOVERY PROTOCOL

### Phase A: Requirement Analysis
**MANDATORY ASSESSMENT**: Before any dependency decisions
- Analyze feature requirements for external dependency needs
- Identify potential technology candidates
- Research market landscape and alternatives
- **GATE**: No dependency selection without comprehensive research

### Phase B: Technology Evaluation
**SYSTEMATIC EVALUATION**: Each dependency candidate must be assessed on:
- **Functionality**: Feature completeness and API coverage
- **Maturity**: Version stability, community adoption, maintenance status
- **Compatibility**: Language/framework version compatibility
- **Licensing**: License compatibility and restrictions
- **Security**: Known vulnerabilities and update frequency
- **Performance**: Benchmark comparisons and resource requirements
- **Support**: Documentation quality and community responsiveness

### Phase C: Risk Assessment
**COMPREHENSIVE RISK ANALYSIS**:
- **Technical Debt**: Long-term maintenance burden
- **Vendor Lock-in**: Switching costs and alternatives
- **Breaking Changes**: Update frequency and migration complexity
- **End-of-Life**: Support timeline and migration planning
- **Scalability**: Performance degradation and resource scaling

## FORBIDDEN PATTERNS (AUTOMATIC BLOCK)

### ❌ "I'll Pick This One"
- **BLOCK**: Arbitrary dependency selection without evaluation
- **REASON**: Unvalidated choices lead to technical debt
- **REMEDIATION**: Complete systematic evaluation process

### ❌ "Latest Version Always"
- **BLOCK**: Automatic latest version adoption
- **REASON**: Stability and compatibility risks
- **REMEDIATION**: Version stability assessment required

### ❌ "Copy From Other Project"
- **BLOCK**: Blind adoption from other projects
- **REASON**: Different requirements may invalidate choices
- **REMEDIATION**: Fresh evaluation for current context

### ❌ "Trust the Stars"
- **BLOCK**: GitHub stars as sole selection criteria
- **REASON**: Popularity doesn't equal suitability
- **REMEDIATION**: Multi-factor evaluation required

## DEPENDENCY MANAGEMENT STANDARDS

### Version Pinning Strategy
- **Production**: Exact version pinning for stability
- **Development**: Compatible version ranges for flexibility
- **Security Updates**: Automated vulnerability scanning
- **Update Process**: Systematic testing before upgrades

### Integration Requirements
- **Configuration Management**: Environment-specific settings
- **Error Handling**: Graceful degradation on dependency failures
- **Monitoring**: Dependency health and performance tracking
- **Documentation**: Integration guides and troubleshooting

### License Compliance
- **Compatibility Check**: License compatibility across stack
- **Distribution Rights**: Usage rights for intended deployment
- **Attribution Requirements**: Proper credit and notices
- **Legal Review**: Complex licenses require legal consultation

## ENFORCEMENT MECHANISMS

### Automated Validation
- **License Scanning**: Automatic license compatibility checking
- **Security Auditing**: Vulnerability database integration
- **Compatibility Testing**: Automated version conflict detection
- **Update Monitoring**: Dependency freshness tracking

### Human Approval Gates
- **Major Dependencies**: Explicit approval for critical infrastructure
- **License Concerns**: Legal review for complex licensing
- **Security Issues**: Immediate remediation for vulnerabilities
- **Breaking Changes**: Migration planning for major updates

## SUCCESS CRITERIA

### Process Compliance
- **100% Evaluated**: No dependency added without evaluation
- **Risk Documented**: All risks identified and mitigation planned
- **Alternatives Considered**: Multiple options evaluated and justified
- **Future-Proofed**: Migration path planned for potential changes

### Quality Outcomes
- **Stable Stack**: Dependencies chosen for long-term viability
- **Secure Foundation**: No known vulnerabilities in production
- **Maintainable Code**: Dependencies support rather than hinder development
- **Scalable Architecture**: Dependencies support growth requirements

## INTEGRATION POINTS

### Workflow Integration
- **Planning Phase**: Dependency research integrated into planning
- **Architecture Phase**: Technology choices validated against requirements
- **Implementation Phase**: Dependencies properly configured and tested
- **Deployment Phase**: Production dependency management verified

### Tool Integration
- **Package Managers**: Proper integration with pip/npm/yarn
- **Security Scanners**: Automated vulnerability detection
- **License Checkers**: Automated license compliance validation
- **Update Monitors**: Automated dependency freshness tracking

## EXCEPTION HANDLING

### Emergency Dependencies
- **Justification Required**: Documented business case for expedited adoption
- **Temporary Status**: Marked as temporary with migration plan
- **Timeline Commitment**: Maximum timeframe before proper evaluation

### Legacy Dependencies
- **Migration Planning**: Clear path to modern alternatives
- **Risk Mitigation**: Additional monitoring and contingency planning
- **Sunset Timeline**: Maximum support timeframe defined
