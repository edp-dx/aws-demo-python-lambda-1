from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
)
from constructs import Construct

class HelloApiStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Define the Lambda function for getting employees
        get_employees_lambda = _lambda.Function(
            self, 'GetEmployeesFunction',
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler='get_employees.handler',
            code=_lambda.Code.from_asset('lambda')
        )

        # Define the Lambda function for adding an employee
        add_employee_lambda = _lambda.Function(
            self, 'AddEmployeeFunction',
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler='add_employee.handler',
            code=_lambda.Code.from_asset('lambda')
        )

        # Define the API Gateway REST API
        api = apigw.RestApi(self, 'employees-api',
            rest_api_name='Employee Service',
            description='This service serves employees.'
        )

        # Integrate the Lambda functions with API Gateway
        get_employees_integration = apigw.LambdaIntegration(get_employees_lambda)
        add_employee_integration = apigw.LambdaIntegration(add_employee_lambda)

        # Create the GET /employees endpoint
        api.root.resource_for_path('/employees').add_method('GET', get_employees_integration)

        # Create the POST /employee endpoint
        api.root.resource_for_path('/employee').add_method('POST', add_employee_integration)
