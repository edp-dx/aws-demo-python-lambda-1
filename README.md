# aws-demo-python-lambda

This project demonstrates how to build and deploy AWS Lambda functions using AWS CDK and Python.

## Project Structure

```plaintext
├── README.md
├── app.py
├── cdk.json
├── lambda/
│   └── hello_world.py
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

## Setup Instructions

1. Install dependencies:

```sh
pip install -r requirements.txt
```

2. Synthesize the CloudFormation template:

```sh
cdk synth
```

3. Deploy the stack:

```sh
cdk deploy
```