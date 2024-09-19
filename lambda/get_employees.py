import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('EMPLOYEE')

def lambda_handler(event, context):
    response = table.scan()
    employees = response['Items']
    return {
        'statusCode': 200,
        'body': json.dumps(employees)
    }
