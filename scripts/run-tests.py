#!/usr/bin/env python3
"""Run unit and integration tests (placeholder)."""
import subprocess
from pathlib import Path


def run_pytest(path: Path):
    if path.exists():
        subprocess.run(['pytest', str(path)], check=False)


def main():
    run_pytest(Path('tests'))


if __name__ == '__main__':
    main()
