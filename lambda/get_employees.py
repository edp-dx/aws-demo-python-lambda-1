import json

def lambda_handler(event, context):
    # Simulate fetching employees from the database
    employees = [
        {"id": 1, "name": "DHONI"},
        {"id": 2, "name": "KHOLI"}
    ]
    return {
        'statusCode': 200,
        'body': json.dumps(employees)
    }