import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('EMPLOYEE')

def lambda_handler(event, context):
    employee = json.loads(event['body'])
    table.put_item(Item=employee)
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'SUCCESS'})
    }
