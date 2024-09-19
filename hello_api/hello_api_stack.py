from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigateway
)
from constructs import Construct

class HelloApiStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create a Lambda function for GET /employees
        get_employees_lambda = _lambda.Function(
            self, 'GetEmployeesFunction',
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler='hello_world.get_employees_handler',
            code=_lambda.Code.from_asset('lambda')
        )

        # Create a Lambda function for POST /employee
        post_employee_lambda = _lambda.Function(
            self, 'PostEmployeeFunction',
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler='hello_world.post_employee_handler',
            code=_lambda.Code.from_asset('lambda')
        )

        # Create an API Gateway
        api = apigateway.RestApi(self, 'hello-api',
            rest_api_name='Hello Service',
            description='This service serves Hello API.'
        )

        # Integrate the GET /employees Lambda function
        get_employees_integration = apigateway.LambdaIntegration(get_employees_lambda)
        api.root.add_resource('employees').add_method('GET', get_employees_integration)

        # Integrate the POST /employee Lambda function
        post_employee_integration = apigateway.LambdaIntegration(post_employee_lambda)
        api.root.add_resource('employee').add_method('POST', post_employee_integration)
