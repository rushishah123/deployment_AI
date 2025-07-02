#!/usr/bin/env python3
"""Perform basic security configuration audit."""
import json
from pathlib import Path


REQUIRED_ENCRYPTION = True


def audit_config(config_path: Path) -> list:
    with config_path.open() as f:
        data = json.load(f)
    issues = []
    sec = data.get('security', {})
    if not sec.get('encryption_at_rest'):
        issues.append('Encryption at rest disabled')
    if not sec.get('encryption_in_transit'):
        issues.append('Encryption in transit disabled')
    if issues:
        print(f"Security issues in {config_path}: {issues}")
    else:
        print(f"{config_path} passed security audit")
    return issues


def main():
    configs = Path('applications').rglob('deploy-config.json')
    overall = []
    for cfg in configs:
        overall.extend(audit_config(cfg))
    if overall:
        exit(1)


if __name__ == '__main__':
    main()
