import json

def lambda_handler(event, context):
    # Simulate saving employee to the database
    body = json.loads(event['body'])
    employee = {
        "id": body.get("id"),
        "name": body.get("name")
    }
    return {
        'statusCode': 200,
        'body': json.dumps({"message": "SUCCESS", "employee": employee})
    }