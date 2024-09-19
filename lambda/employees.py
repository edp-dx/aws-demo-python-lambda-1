import json
import boto3

def handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Employees')

    response = table.scan()

    return {
        'statusCode': 200,
        'body': json.dumps(response['Items'])
    }
