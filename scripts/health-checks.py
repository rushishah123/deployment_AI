#!/usr/bin/env python3
"""Perform simple health checks."""
import requests
import sys


def check_endpoint(url: str) -> bool:
    try:
        resp = requests.get(url, timeout=5)
        return resp.status_code == 200
    except Exception as exc:
        print(f"Health check failed for {url}: {exc}")
        return False


def main():
    urls = sys.argv[1:]
    all_ok = True
    for u in urls:
        if not check_endpoint(u):
            all_ok = False
    if not all_ok:
        sys.exit(1)


if __name__ == '__main__':
    main()
