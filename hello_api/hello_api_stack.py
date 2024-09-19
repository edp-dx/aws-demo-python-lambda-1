from aws_cdk import (
    aws_lambda as _lambda,
    aws_apigateway as apigateway,
    core
)

class HelloApiStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Define the Lambda function for GET /employees
        get_employees_lambda = _lambda.Function(
            self, 'GetEmployeesHandler',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.from_asset('lambda'),
            handler='get_employees.lambda_handler',
        )

        # Define the Lambda function for POST /employee
        post_employee_lambda = _lambda.Function(
            self, 'PostEmployeeHandler',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.from_asset('lambda'),
            handler='post_employee.lambda_handler',
        )

        # Define API Gateway
        api = apigateway.RestApi(
            self, 'employee-api',
            rest_api_name='Employee Service'
        )

        # Define the GET /employees endpoint
        get_employees_integration = apigateway.LambdaIntegration(get_employees_lambda)
        api.root.add_resource('employees').add_method('GET', get_employees_integration)

        # Define the POST /employee endpoint
        post_employee_integration = apigateway.LambdaIntegration(post_employee_lambda)
        api.root.add_resource('employee').add_method('POST', post_employee_integration)