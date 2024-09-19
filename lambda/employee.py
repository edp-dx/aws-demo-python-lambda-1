import json
import boto3

def handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Employees')

    body = json.loads(event['body'])
    table.put_item(Item=body)

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'SUCCESS'})
    }
