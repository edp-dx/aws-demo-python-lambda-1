from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigateway,
)
from constructs import Construct

class HelloApiStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        get_employees_lambda = _lambda.Function(
            self, 'GetEmployeesHandler',
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler='hello_world.get_employees',
            code=_lambda.Code.from_asset('lambda')
        )

        add_employee_lambda = _lambda.Function(
            self, 'AddEmployeeHandler',
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler='hello_world.add_employee',
            code=_lambda.Code.from_asset('lambda')
        )

        api = apigateway.RestApi(self, "hello-api",
            rest_api_name="Hello Service",
            description="This service serves employees."
        )

        get_employees_integration = apigateway.LambdaIntegration(get_employees_lambda)
        add_employee_integration = apigateway.LambdaIntegration(add_employee_lambda)

        api.root.add_resource("employees").add_method("GET", get_employees_integration)
        api.root.add_resource("employee").add_method("POST", add_employee_integration)
