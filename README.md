# aws-demo-python-lambda-1

This project is an AWS CDK application written in Python that deploys serverless functions for managing employees.

## Project Structure

- `app.py`: The main entry point for the CDK application.
- `cdk.json`: Configuration file for the CDK application.
- `requirements.txt`: Python dependencies.
- `setup.py`: Python package setup.
- `source.bat` and `source.sh`: Scripts for deploying the CDK application.
- `lambda/hello_world.py`: Lambda functions for handling employee-related endpoints.
- `hello_api/`: CDK stack definition.
  - `hello_api_stack.py`: Defines the AWS resources and API Gateway.

## Deployment

To deploy the CDK application, you can use the provided scripts:

### Windows

```sh
source.bat
```

### Unix

```sh
source.sh
```