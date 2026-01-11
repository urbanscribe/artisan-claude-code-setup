# Dependency Licenses Sub-Rule (Tier 3)
## Purpose
Ensures all software dependencies have compatible licenses and proper attribution to prevent legal issues and maintain compliance.

## LICENSE COMPATIBILITY MATRIX

### License Categories
**PERMISSIVE LICENSES** (Generally Compatible):
- MIT: Highly permissive, allows commercial use, modification, distribution
- BSD 2-Clause/3-Clause: Similar to MIT with minimal restrictions
- Apache 2.0: Permissive with patent protection clauses
- ISC: Functionally equivalent to BSD/MIT

**COPYLEFT LICENSES** (Require Careful Evaluation):
- GPL 2.0/3.0: Strong copyleft, derivative works must be GPL
- LGPL 2.1/3.0: Weak copyleft, allows linking without GPL requirement
- AGPL 3.0: Network copyleft, requires source disclosure over network
- EPL 2.0: Weak copyleft with business-friendly terms

**PROPRIETARY/LICENSED** (Case-by-Case):
- Commercial licenses requiring purchase
- Dual-licensing schemes (open source + commercial)
- Research/academic use only licenses

## LICENSE COMPATIBILITY RULES

### Permissive + Permissive = Compatible
**LOW RISK COMBINATIONS**:
```python
# dependency_licenses/license_compatibility.py
from typing import Set, Dict, List
from dataclasses import dataclass

@dataclass
class LicenseCompatibility:
    """License compatibility rules and restrictions."""
    license_name: str
    compatible_with: Set[str]
    restrictions: List[str]
    attribution_required: bool
    source_disclosure_required: bool

LICENSE_MATRIX = {
    'MIT': LicenseCompatibility(
        license_name='MIT',
        compatible_with={'MIT', 'BSD-2-Clause', 'BSD-3-Clause', 'Apache-2.0', 'ISC'},
        restrictions=[],
        attribution_required=True,
        source_disclosure_required=False
    ),
    'Apache-2.0': LicenseCompatibility(
        license_name='Apache-2.0',
        compatible_with={'MIT', 'BSD-2-Clause', 'BSD-3-Clause', 'Apache-2.0', 'ISC'},
        restrictions=[],
        attribution_required=True,
        source_disclosure_required=False
    ),
    'GPL-3.0': LicenseCompatibility(
        license_name='GPL-3.0',
        compatible_with={'GPL-3.0', 'AGPL-3.0'},
        restrictions=['Derivative works must be GPL licensed', 'Source code must be disclosed'],
        attribution_required=True,
        source_disclosure_required=True
    ),
    'LGPL-2.1': LicenseCompatibility(
        license_name='LGPL-2.1',
        compatible_with={'MIT', 'BSD-2-Clause', 'BSD-3-Clause', 'Apache-2.0', 'ISC', 'GPL-2.0', 'GPL-3.0', 'LGPL-2.1'},
        restrictions=['Modifications to LGPL code must be LGPL licensed'],
        attribution_required=True,
        source_disclosure_required=False
    )
}

def check_license_compatibility(licenses: List[str]) -> Dict[str, Any]:
    """
    Check compatibility of multiple licenses.

    Args:
        licenses: List of license identifiers

    Returns:
        Dict with compatibility analysis
    """
    if not licenses:
        return {'compatible': True, 'issues': []}

    # Get compatibility info for each license
    license_infos = []
    for license_name in licenses:
        if license_name in LICENSE_MATRIX:
            license_infos.append(LICENSE_MATRIX[license_name])
        else:
            return {
                'compatible': False,
                'issues': [f'Unknown license: {license_name}'],
                'recommendation': 'Review license manually or consult legal'
            }

    # Check pairwise compatibility
    issues = []
    all_compatible = True

    for i, license_a in enumerate(license_infos):
        for j, license_b in enumerate(license_infos[i+1:], i+1):
            if license_b.license_name not in license_a.compatible_with:
                all_compatible = False
                issues.append(
                    f'{license_a.license_name} is not compatible with {license_b.license_name}'
                )

    # Collect all restrictions
    all_restrictions = []
    attribution_required = False
    source_required = False

    for license_info in license_infos:
        all_restrictions.extend(license_info.restrictions)
        attribution_required |= license_info.attribution_required
        source_required |= license_info.source_disclosure_required

    return {
        'compatible': all_compatible,
        'issues': issues,
        'restrictions': list(set(all_restrictions)),
        'attribution_required': attribution_required,
        'source_disclosure_required': source_required,
        'recommendation': _get_recommendation(all_compatible, issues)
    }

def _get_recommendation(compatible: bool, issues: List[str]) -> str:
    """Generate recommendation based on compatibility analysis."""
    if compatible:
        return 'Licenses are compatible - proceed with standard attribution'

    if any('GPL' in issue for issue in issues):
        return 'GPL incompatibility detected - consider alternative dependencies or re-licensing'

    return 'License conflicts detected - consult legal counsel before proceeding'
```

### Copyleft License Handling
**HIGH RISK SCENARIOS**:
```python
# dependency_licenses/copyleft_analysis.py
def analyze_copyleft_impact(dependencies: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Analyze impact of copyleft licenses on project licensing.

    Args:
        dependencies: List of dependency dicts with 'name', 'license', 'usage' keys

    Returns:
        Dict with copyleft impact analysis
    """
    copyleft_licenses = {'GPL-2.0', 'GPL-3.0', 'AGPL-3.0', 'LGPL-2.1', 'LGPL-3.0'}
    strong_copyleft = {'GPL-2.0', 'GPL-3.0', 'AGPL-3.0'}

    analysis = {
        'copyleft_dependencies': [],
        'strong_copyleft': [],
        'weak_copyleft': [],
        'project_impact': 'permissive',
        'recommendations': []
    }

    for dep in dependencies:
        license_name = dep.get('license', '').upper()

        if any(cl in license_name for cl in copyleft_licenses):
            analysis['copyleft_dependencies'].append(dep)

            if any(cl in license_name for cl in strong_copyleft):
                analysis['strong_copyleft'].append(dep)
                analysis['project_impact'] = 'strong_copyleft'
            else:
                analysis['weak_copyleft'].append(dep)
                if analysis['project_impact'] == 'permissive':
                    analysis['project_impact'] = 'weak_copyleft'

    # Generate recommendations
    if analysis['strong_copyleft']:
        analysis['recommendations'].extend([
            'Consider re-licensing project to GPL-compatible license',
            'Evaluate alternative dependencies without strong copyleft',
            'Consult legal counsel for GPL compliance requirements'
        ])

    if analysis['weak_copyleft']:
        analysis['recommendations'].extend([
            'LGPL dependencies are generally safe for linking',
            'Avoid modifying LGPL-licensed code if possible',
            'Document LGPL dependencies in license notices'
        ])

    return analysis
```

## LICENSE SCANNING AND VALIDATION

### Automated License Detection
**DEPENDENCY ANALYSIS TOOLS**:
```python
# dependency_licenses/license_scanner.py
import subprocess
import json
import re
from typing import Dict, List, Any, Optional
from pathlib import Path

class LicenseScanner:
    """Automated license scanning for dependencies."""

    def scan_python_dependencies(self, requirements_file: str = 'requirements.txt') -> List[Dict[str, Any]]:
        """Scan Python dependencies for licenses."""
        dependencies = []

        try:
            # Use pip-licenses or similar tool
            result = subprocess.run([
                'pip-licenses',
                '--format=json',
                '--with-urls',
                '--with-license-file'
            ], capture_output=True, text=True, cwd='.')

            if result.returncode == 0:
                license_data = json.loads(result.stdout)
                for dep in license_data:
                    dependencies.append({
                        'name': dep.get('Name', ''),
                        'version': dep.get('Version', ''),
                        'license': dep.get('License', ''),
                        'url': dep.get('URL', ''),
                        'license_file': dep.get('LicenseFile', '')
                    })
        except FileNotFoundError:
            # Fallback: parse requirements.txt and query PyPI
            dependencies = self._scan_requirements_fallback(requirements_file)

        return dependencies

    def _scan_requirements_fallback(self, requirements_file: str) -> List[Dict[str, Any]]:
        """Fallback license scanning using PyPI API."""
        dependencies = []

        if not Path(requirements_file).exists():
            return dependencies

        with open(requirements_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    # Extract package name (basic parsing)
                    package_name = re.split(r'[=<>~]', line)[0].strip()
                    if package_name:
                        license_info = self._get_pypi_license(package_name)
                        if license_info:
                            dependencies.append(license_info)

        return dependencies

    def _get_pypi_license(self, package_name: str) -> Optional[Dict[str, Any]]:
        """Get license info from PyPI API."""
        try:
            import requests

            response = requests.get(f'https://pypi.org/pypi/{package_name}/json', timeout=10)
            if response.status_code == 200:
                data = response.json()
                info = data.get('info', {})

                return {
                    'name': package_name,
                    'version': info.get('version', ''),
                    'license': info.get('license', ''),
                    'url': info.get('home_page', ''),
                    'license_file': None
                }
        except Exception:
            pass

        return None

    def scan_javascript_dependencies(self, package_json: str = 'package.json') -> List[Dict[str, Any]]:
        """Scan JavaScript dependencies for licenses."""
        dependencies = []

        try:
            # Use license-checker or similar npm tool
            result = subprocess.run([
                'npx', 'license-checker',
                '--json',
                '--production'
            ], capture_output=True, text=True, cwd='.')

            if result.returncode == 0:
                license_data = json.loads(result.stdout)
                for dep_path, dep_info in license_data.items():
                    package_name = dep_path.split('@')[0]
                    dependencies.append({
                        'name': package_name,
                        'version': dep_info.get('version', ''),
                        'license': dep_info.get('licenses', ''),
                        'url': dep_info.get('repository', ''),
                        'license_file': dep_info.get('licenseFile', '')
                    })
        except FileNotFoundError:
            # Fallback: parse package.json
            dependencies = self._scan_package_json_fallback(package_json)

        return dependencies

    def _scan_package_json_fallback(self, package_json: str) -> List[Dict[str, Any]]:
        """Fallback scanning using package.json."""
        dependencies = []

        try:
            with open(package_json, 'r') as f:
                data = json.load(f)

            all_deps = {}
            all_deps.update(data.get('dependencies', {}))
            all_deps.update(data.get('devDependencies', {}))

            for name, version in all_deps.items():
                # Note: This is a basic fallback - real license checking requires npm tools
                dependencies.append({
                    'name': name,
                    'version': version,
                    'license': 'UNKNOWN - requires npm license-checker',
                    'url': '',
                    'license_file': None
                })
        except Exception:
            pass

        return dependencies
```

## LICENSE COMPLIANCE WORKFLOW

### Dependency Review Process
**SYSTEMATIC LICENSE EVALUATION**:
```markdown
# License Compliance Workflow

## Phase 1: Automated Scanning
- [ ] Run automated license scanning tools
- [ ] Identify all dependencies and their licenses
- [ ] Flag unknown or problematic licenses
- [ ] Generate license compatibility report

## Phase 2: Manual Review
- [ ] Review automated scan results
- [ ] Verify license accuracy against source
- [ ] Check license compatibility matrix
- [ ] Identify attribution requirements

## Phase 3: Risk Assessment
- [ ] Evaluate business risk of license incompatibilities
- [ ] Assess impact of copyleft license adoption
- [ ] Consider alternative dependencies if needed
- [ ] Document risk mitigation strategies

## Phase 4: Compliance Implementation
- [ ] Add license notices to project documentation
- [ ] Include attribution in distributed software
- [ ] Update license files with dependency attributions
- [ ] Configure automated compliance checking
```

### License Notice Generation
**ATTRIBUTION AUTOMATION**:
```python
# dependency_licenses/notice_generator.py
def generate_license_notices(dependencies: List[Dict[str, Any]]) -> str:
    """
    Generate license notice text for all dependencies.

    Args:
        dependencies: List of dependency dictionaries

    Returns:
        Formatted license notice text
    """
    notices = [
        "This software includes third-party components with the following licenses:",
        ""
    ]

    # Group by license
    by_license = {}
    for dep in dependencies:
        license_name = dep.get('license', 'Unknown')
        if license_name not in by_license:
            by_license[license_name] = []
        by_license[license_name].append(dep)

    # Generate notices for each license group
    for license_name, deps in by_license.items():
        notices.append(f"## {license_name} License")
        notices.append("")

        for dep in sorted(deps, key=lambda x: x['name']):
            name = dep['name']
            version = dep.get('version', '')
            url = dep.get('url', '')

            notice_line = f"- {name}"
            if version:
                notice_line += f" ({version})"
            if url:
                notice_line += f" - {url}"

            notices.append(notice_line)

        notices.append("")

    return "\n".join(notices)

def generate_attribution_file(dependencies: List[Dict[str, Any]], output_file: str = 'LICENSE-ATTRIBUTIONS.txt'):
    """Generate attribution file for distribution."""
    notices = generate_license_notices(dependencies)

    with open(output_file, 'w') as f:
        f.write("Third-Party Software Attributions\n")
        f.write("==================================\n")
        f.write("\n")
        f.write(notices)
        f.write("\n")
        f.write("For full license texts, see individual package documentation.\n")

    return output_file
```

## COMPLIANCE MONITORING

### Continuous License Checking
**CI/CD INTEGRATION**:
```yaml
# .github/workflows/license-check.yml
name: License Compliance

on:
  push:
  pull_request:
  schedule:
    - cron: '0 0 * * 0'  # Weekly license audit

jobs:
  license-check:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pip-licenses safety

      - name: Check Python licenses
        run: |
          pip-licenses --format=markdown --output-file=python-licenses.md
          pip-licenses --format=json --output-file=python-licenses.json

      - name: Check JavaScript licenses
        run: |
          npm install -g license-checker
          npx license-checker --json --production > js-licenses.json
          npx license-checker --markdown --production > js-licenses.md

      - name: Validate license compatibility
        run: |
          python scripts/validate_licenses.py python-licenses.json js-licenses.json

      - name: Check for security vulnerabilities
        run: |
          safety check --json > security-audit.json

      - name: Upload license reports
        uses: actions/upload-artifact@v3
        with:
          name: license-reports
          path: |
            python-licenses.*
            js-licenses.*
            security-audit.json
```

### License Change Alerts
**DEPENDENCY MONITORING**:
```python
# dependency_licenses/license_monitor.py
import json
import hashlib
from pathlib import Path
from typing import Dict, List, Any, Optional

class LicenseMonitor:
    """Monitor dependency licenses for changes."""

    def __init__(self, baseline_file: str = 'license-baseline.json'):
        self.baseline_file = Path(baseline_file)
        self.baseline = self._load_baseline()

    def _load_baseline(self) -> Dict[str, Any]:
        """Load license baseline."""
        if self.baseline_file.exists():
            with open(self.baseline_file, 'r') as f:
                return json.load(f)
        return {}

    def check_for_changes(self, current_dependencies: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Check for license changes compared to baseline."""
        changes = {
            'new_dependencies': [],
            'removed_dependencies': [],
            'license_changes': [],
            'new_licenses': []
        }

        current_deps = {dep['name']: dep for dep in current_dependencies}
        baseline_deps = self.baseline.get('dependencies', {})

        # Check for new dependencies
        for name, dep in current_deps.items():
            if name not in baseline_deps:
                changes['new_dependencies'].append(dep)

        # Check for removed dependencies
        for name in baseline_deps:
            if name not in current_deps:
                changes['removed_dependencies'].append(baseline_deps[name])

        # Check for license changes
        for name, current_dep in current_deps.items():
            if name in baseline_deps:
                baseline_dep = baseline_deps[name]
                if current_dep.get('license') != baseline_dep.get('license'):
                    changes['license_changes'].append({
                        'dependency': name,
                        'old_license': baseline_dep.get('license'),
                        'new_license': current_dep.get('license')
                    })

        # Check for new license types
        current_licenses = {dep.get('license') for dep in current_dependencies}
        baseline_licenses = set(self.baseline.get('licenses', []))

        new_licenses = current_licenses - baseline_licenses
        changes['new_licenses'] = list(new_licenses)

        return changes

    def update_baseline(self, dependencies: List[Dict[str, Any]]):
        """Update license baseline."""
        licenses = list({dep.get('license') for dep in dependencies if dep.get('license')})

        baseline_data = {
            'dependencies': {dep['name']: dep for dep in dependencies},
            'licenses': licenses,
            'updated_at': datetime.utcnow().isoformat()
        }

        with open(self.baseline_file, 'w') as f:
            json.dump(baseline_data, f, indent=2)
```

This dependency licenses sub-rule establishes comprehensive license compliance protocols ensuring all software dependencies are legally compatible and properly attributed. The automated scanning, compatibility checking, and compliance workflows prevent legal issues while maintaining proper attribution for open source dependencies.```
<xai:function_call name="write">
<parameter name="file_path">claude_code/setup/.claude/rules/sub/dependency_security.md
