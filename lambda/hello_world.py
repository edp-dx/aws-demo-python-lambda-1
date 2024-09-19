import json
import boto3

dynamodb = boto3.resource('dynamodb')
table_name = "Employee"

def get_employees(event, context):
    table = dynamodb.Table(table_name)
    response = table.scan()
    employees = response.get('Items', [])
    return {
        'statusCode': 200,
        'body': json.dumps(employees)
    }

def add_employee(event, context):
    table = dynamodb.Table(table_name)
    employee = json.loads(event['body'])
    table.put_item(Item=employee)
    return {
        'statusCode': 200,
        'body': json.dumps({"message": "SUCCESS"})
    }
