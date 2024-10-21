# AWS Demo Python Lambda

This project demonstrates the use of AWS Lambda functions with Python and the AWS CDK (Cloud Development Kit).

## Project Structure

The project is structured as follows:

```
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

## Getting Started

To deploy this project, follow these steps:

1. Install the dependencies:

```
pip install -r requirements.txt
```

2. Synthesize the CloudFormation template:

```
cdk synth
```

3. Deploy the stack:

```
cdk deploy
```

## Lambda Functions

The Lambda functions are located in the `lambda/` directory. The `hello_world.py` file contains a sample Lambda function.

## CDK Stack

The CDK stack is defined in the `hello_api/hello_api_stack.py` file. This stack includes the definition of the Lambda functions and the API Gateway.

## CI/CD

The CI/CD pipeline is defined in the `.github/workflows/ci-cd.yaml` file. This pipeline automatically deploys the stack to AWS whenever changes are pushed to the repository.
