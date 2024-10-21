from aws_cdk import (
    Stack,
    aws_lambda as lambda_,
    aws_apigateway as apigateway,
)
from constructs import Construct

class HelloApiStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        get_employees_lambda = lambda_.Function(
            self, "GetEmployeesFunction",
            runtime=lambda_.Runtime.PYTHON_3_8,
            handler="get_employees.handler",
            code=lambda_.Code.from_asset("lambda")
        )

        add_employee_lambda = lambda_.Function(
            self, "AddEmployeeFunction",
            runtime=lambda_.Runtime.PYTHON_3_8,
            handler="add_employee.handler",
            code=lambda_.Code.from_asset("lambda")
        )

        api = apigateway.RestApi(self, "employees-api",
            rest_api_name="Employee Service",
            description="This service serves employees."
        )

        get_employees_integration = apigateway.LambdaIntegration(get_employees_lambda,
            request_templates={"application/json": "{ \"statusCode\": \"200\" }"}
        )

        add_employee_integration = apigateway.LambdaIntegration(add_employee_lambda,
            request_templates={"application/json": "{ \"statusCode\": \"200\" }"}
        )

        api.root.add_method("GET", get_employees_integration)   # GET /
        api.root.add_method("POST", add_employee_integration)  # POST /
