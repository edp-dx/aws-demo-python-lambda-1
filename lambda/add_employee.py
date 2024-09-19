import json
import boto3

def handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Employee')
    
    employee = json.loads(event['body'])
    table.put_item(Item=employee)
    
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'SUCCESS'})
    }
