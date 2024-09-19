# aws-demo-python-lambda-1

This project contains AWS Lambda functions for handling employee data.

## Endpoints

- `GET /employees` - Retrieves a list of all employees.
- `POST /employee` - Adds a new employee.

## Project Structure

```plaintext
├── README.md
├── app.py
├── cdk.json
├── lambda/
│   ├── employees.py
│   ├── employee.py
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

## Deployment

This project uses GitHub Actions for CI/CD. The pipeline is defined in `.github/workflows/ci-cd.yaml`.

# app.py

from aws_cdk import core
from hello_api.hello_api_stack import HelloApiStack

app = core.App()
HelloApiStack(app, "HelloApiStack")

app.synth()

# lambda/employees.py

import json

def lambda_handler(event, context):
    # This would realistically fetch data from a database
    employees = [
        {"id": 1, "name": "John Smith", "role": "Developer"},
        {"id": 2, "name": "Jane Doe", "role": "Manager"},
    ]
    return {
        'statusCode': 200,
        'body': json.dumps(employees)
    }

# lambda/employee.py

import json

def lambda_handler(event, context):
    body = json.loads(event['body'])
    new_employee = {
        "id": body['id'],
        "name": body['name'],
        "role": body['role']
    }
    # This would realistically save the new employee to a database
    return {
        'statusCode': 201,
        'body': json.dumps(new_employee)
    }

# requirements.txt

aws-cdk.core
aws-cdk.aws-lambda
aws-cdk.aws-apigateway

# setup.py

import setuptools

with open("README.md") as fp:
    long_description = fp.read()

setuptools.setup(
    name="aws_demo_python_lambda",
    version="1.0.0",
    description="An AWS CDK Python app for AWS Lambda functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="author",
    package_dir={"": "hello_api"},
    packages=setuptools.find_packages(where="hello_api"),
    install_requires=[
        "aws-cdk.core",
        "aws-cdk.aws-lambda",
        "aws-cdk.aws-apigateway",
    ],
    python_requires=">=3.6",
)

# source.bat

call cdk deploy

# source.sh

#!/bin/sh
cdk deploy

# hello_api/__init__.py

# hello_api/hello_api_stack.py

from aws_cdk import (
    core,
    aws_lambda as _lambda,
    aws_apigateway as apigateway
)

class HelloApiStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        get_employees_lambda = _lambda.Function(
            self, 'GetEmployeesHandler',
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler='employees.lambda_handler',
            code=_lambda.Code.from_asset('lambda')
        )

        add_employee_lambda = _lambda.Function(
            self, 'AddEmployeeHandler',
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler='employee.lambda_handler',
            code=_lambda.Code.from_asset('lambda')
        )

        api = apigateway.RestApi(self, 'employees-api',
            rest_api_name='Employees Service',
            description='This service serves employees.'
        )

        employees_resource = api.root.add_resource('employees')
        employees_resource.add_method('GET', apigateway.LambdaIntegration(get_employees_lambda))

        employee_resource = api.root.add_resource('employee')
        employee_resource.add_method('POST', apigateway.LambdaIntegration(add_employee_lambda))

# .github/workflows/ci-cd.yaml

name: CI/CD Pipeline

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.8'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Deploy CDK Stack
        env:
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
        run: |
          pip install aws-cdk.core aws-cdk.aws-lambda aws-cdk.aws-apigateway
          cdk deploy --require-approval never