from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigateway,
)
from constructs import Construct

class HelloApiStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Define the Lambda function for GET /employees
        get_employees_lambda = _lambda.Function(
            self, "GetEmployeesFunction",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="get_employees.lambda_handler",
            code=_lambda.Code.from_asset("lambda")
        )

        # Define the Lambda function for POST /employee
        post_employee_lambda = _lambda.Function(
            self, "PostEmployeeFunction",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="post_employee.lambda_handler",
            code=_lambda.Code.from_asset("lambda")
        )

        # Define the API Gateway
        api = apigateway.RestApi(self, "employee-api",
            rest_api_name="Employee Service",
            description="This service serves employees."
        )

        # Integrate GET /employees with the get_employees_lambda function
        get_employees_integration = apigateway.LambdaIntegration(get_employees_lambda,
            request_templates={"application/json": "{\"statusCode\": \"200\"}"}
        )

        api.root.add_resource("employees").add_method("GET", get_employees_integration)

        # Integrate POST /employee with the post_employee_lambda function
        post_employee_integration = apigateway.LambdaIntegration(post_employee_lambda,
            request_templates={"application/json": "{\"statusCode\": \"200\"}"}
        )

        api.root.add_resource("employee").add_method("POST", post_employee_integration)