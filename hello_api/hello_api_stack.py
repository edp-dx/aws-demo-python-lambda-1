from aws_cdk import (
    aws_lambda as _lambda,
    aws_apigateway as apigw,
    aws_dynamodb as dynamodb,
    core
)

class HelloApiStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        table = dynamodb.Table(
            self, "Employees",
            partition_key={"name": "id", "type": dynamodb.AttributeType.STRING}
        )

        get_employees_lambda = _lambda.Function(
            self, 'GetEmployeesHandler',
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler='employees.handler',
            code=_lambda.Code.asset('lambda')
        )

        post_employee_lambda = _lambda.Function(
            self, 'PostEmployeeHandler',
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler='employee.handler',
            code=_lambda.Code.asset('lambda')
        )

        api = apigw.RestApi(self, 'employees-api')

        employees = api.root.add_resource('employees')
        employees.add_method('GET', apigw.LambdaIntegration(get_employees_lambda))
        
        employee = api.root.add_resource('employee')
        employee.add_method('POST', apigw.LambdaIntegration(post_employee_lambda))
