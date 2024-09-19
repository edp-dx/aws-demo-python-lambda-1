import json

def lambda_handler(event, context):
    # Sample data to mimic database retrieval
    employees = [
        {"id": 1, "name": "DHONI"},
        {"id": 2, "name": "KHOLI"}
    ]
    
    return {
        'statusCode': 200,
        'body': json.dumps(employees)
    }
