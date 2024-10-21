import json

def handler(event, context):
    body = json.loads(event['body'])
    new_employee = {
        'id': body['id'],
        'name': body['name']
    }
    # Here, you would normally save the new_employee to a database
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Employee added successfully'})
    }
