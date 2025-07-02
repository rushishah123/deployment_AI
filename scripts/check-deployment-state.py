#!/usr/bin/env python3
"""Check deployment state in DynamoDB (placeholder)."""
import boto3
from pathlib import Path
import json


def get_state(table, app_name):
    resp = table.get_item(Key={'app_name': app_name})
    return resp.get('Item')


def main():
    table_name = 'deployment-state'
    app_name = Path('.').resolve().name
    ddb = boto3.resource('dynamodb')
    table = ddb.Table(table_name)
    state = get_state(table, app_name)
    if state:
        print('update_existing')
    else:
        print('create_new')


if __name__ == '__main__':
    main()
