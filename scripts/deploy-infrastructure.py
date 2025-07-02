#!/usr/bin/env python3
"""Deploy infrastructure via Terraform (placeholder)."""
import subprocess


def main():
    subprocess.run(['terraform', 'apply', '-auto-approve'], check=False)


if __name__ == '__main__':
    main()
