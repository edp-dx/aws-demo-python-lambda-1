import json
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table_name = 'EmployeeTable'

def get_employees_handler(event, context):
    table = dynamodb.Table(table_name)
    response = table.scan()
    return {
        'statusCode': 200,
        'body': json.dumps(response['Items'])
    }

def post_employee_handler(event, context):
    table = dynamodb.Table(table_name)
    body = json.loads(event['body'])
    table.put_item(Item=body)
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'SUCCESS'})
    }
