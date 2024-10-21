import json

def get_employees(event, context):
    employees = [
        {"id": 1, "name": "DHONI"},
        {"id": 2, "name": "KHOLI"}
    ]
    return {
        "statusCode": 200,
        "body": json.dumps(employees)
    }

def add_employee(event, context):
    body = json.loads(event["body"])
    new_employee = {
        "id": body["id"],
        "name": body["name"]
    }
    # In a real application, you'd save this to a database
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "SUCCESS"})
    }
