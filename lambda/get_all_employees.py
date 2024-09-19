import json
import boto3

def handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Employee')
    
    response = table.scan()
    employees = response['Items']
    
    return {
        'statusCode': 200,
        'body': json.dumps(employees)
    }
