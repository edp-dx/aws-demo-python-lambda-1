import json

def lambda_handler(event, context):
    # Extract employee data from request
    body = json.loads(event['body'])
    new_employee = {
        "id": body["id"],
        "name": body["name"]
    }
    
    # Here, you would add code to save the new employee to a database.
    # For simplicity, we'll return the new employee data as a success response.
    
    return {
        'statusCode': 201,
        'body': json.dumps(new_employee)
    }
