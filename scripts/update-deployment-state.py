#!/usr/bin/env python3
"""Update deployment state in DynamoDB and S3 (placeholder)."""
import boto3
import json
from pathlib import Path


def main():
    ddb = boto3.resource('dynamodb')
    table = ddb.Table('deployment-state')
    app_name = Path('.').resolve().name
    table.put_item(Item={'app_name': app_name, 'state': 'deployed'})
    print("Deployment state updated")


if __name__ == '__main__':
    main()
