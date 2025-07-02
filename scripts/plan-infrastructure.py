#!/usr/bin/env python3
"""Generate Terraform plan (placeholder)."""
import subprocess


def main():
    subprocess.run(['terraform', 'init'], check=False)
    subprocess.run(['terraform', 'plan', '-out=tfplan'], check=False)


if __name__ == '__main__':
    main()
