# AWS Demo Python Lambda

This project demonstrates the use of AWS Lambda with Python using AWS CDK.

## Project Structure

```
.
├── README.md
├── app.py
├── cdk.json
├── lambda/
│   ├── get_all_employees.py
│   ├── add_employee.py
├── requirements.txt
├── setup.py
├── source.bat
├── source.sh
├── hello_api/
│   ├── __init__.py
│   ├── hello_api_stack.py
└── .github/
    └── workflows/
        └── ci-cd.yaml
```

## Deploy

To deploy the stack, run:

```
cdk deploy
```

## Destroy

To destroy the stack, run:

```
cdk destroy
```