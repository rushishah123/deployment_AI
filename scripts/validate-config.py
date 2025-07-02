#!/usr/bin/env python3
"""Validate deployment configurations against schema."""
import json
import sys
from pathlib import Path

import jsonschema

SCHEMA_PATH = Path('config/deploy-schema.json')


def load_schema():
    with SCHEMA_PATH.open() as f:
        return json.load(f)


def validate_config(config_path: Path, schema: dict) -> bool:
    with config_path.open() as f:
        data = json.load(f)
    try:
        jsonschema.validate(instance=data, schema=schema)
        print(f"{config_path} valid")
        return True
    except jsonschema.ValidationError as exc:
        print(f"Validation error in {config_path}: {exc.message}")
        return False


def main():
    schema = load_schema()
    configs = Path('applications').rglob('deploy-config.json')
    success = True
    for cfg in configs:
        if not validate_config(cfg, schema):
            success = False
    if not success:
        sys.exit(1)


if __name__ == '__main__':
    main()
