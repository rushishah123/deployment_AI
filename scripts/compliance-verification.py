#!/usr/bin/env python3
"""Verify compliance settings (placeholder)."""
import json
from pathlib import Path


def verify(config_path: Path) -> list:
    with config_path.open() as f:
        data = json.load(f)
    levels = set(data['application'].get('compliance_level', []))
    required = {'hipaa', 'gdpr'}
    missing = required - levels
    if missing:
        print(f"{config_path} missing compliance: {missing}")
    return list(missing)


def main():
    failures = []
    for cfg in Path('applications').rglob('deploy-config.json'):
        failures.extend(verify(cfg))
    if failures:
        exit(1)


if __name__ == '__main__':
    main()
