from aws_cdk import (
    aws_apigateway as apigateway,
    aws_lambda as _lambda,
    aws_dynamodb as dynamodb,
    Stack
)
from constructs import Construct

class HelloApiStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        table = dynamodb.Table(
            self, "EmployeeTable",
            partition_key={"name": "id", "type": dynamodb.AttributeType.NUMBER},
            table_name="Employee"
        )

        get_employees_lambda = _lambda.Function(
            self, "GetEmployeesFunction",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="hello_world.get_employees",
            code=_lambda.Code.from_asset("lambda")
        )

        add_employee_lambda = _lambda.Function(
            self, "AddEmployeeFunction",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="hello_world.add_employee",
            code=_lambda.Code.from_asset("lambda")
        )

        api = apigateway.RestApi(self, "employees-api",
                                 rest_api_name="Employee Service",
                                 description="This service serves employees.")

        employees = api.root.add_resource("employees")
        employees.add_method("GET", apigateway.LambdaIntegration(get_employees_lambda))

        employee = api.root.add_resource("employee")
        employee.add_method("POST", apigateway.LambdaIntegration(add_employee_lambda))
