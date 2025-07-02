#!/usr/bin/env python3
"""Estimate AWS costs from configuration (placeholder)."""
import json
from pathlib import Path


def estimate(config_path: Path) -> float:
    with config_path.open() as f:
        data = json.load(f)
    res = data.get('infrastructure', {}).get('resources', {})
    # Simplistic example: cpu units * memory GB * 0.1
    cpu = float(res.get('cpu', '0'))
    mem = float(res.get('memory', '0'))
    cost = (cpu + mem) * 0.1
    print(f"Estimated cost for {config_path}: ${cost:.2f}")
    return cost


def main():
    total = 0.0
    for cfg in Path('applications').rglob('deploy-config.json'):
        total += estimate(cfg)
    print(f"Total estimated monthly cost: ${total:.2f}")


if __name__ == '__main__':
    main()
