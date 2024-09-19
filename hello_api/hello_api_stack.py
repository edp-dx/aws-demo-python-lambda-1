from aws_cdk import (
    aws_lambda as _lambda,
    aws_apigateway as apigw,
    aws_dynamodb as dynamodb,
    core
)

class HelloApiStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Define the DynamoDB table
        table = dynamodb.Table(
            self, 'EmployeeTable',
            partition_key={'name': 'id', 'type': dynamodb.AttributeType.NUMBER},
            table_name='EMPLOYEE'
        )

        # Define the Lambda resource for GET /employees
        get_employees_lambda = _lambda.Function(
            self, 'GetEmployeesHandler',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.from_asset('lambda'),
            handler='get_employees.lambda_handler',
            environment={
                'TABLE_NAME': table.table_name
            }
        )

        # Define the Lambda resource for POST /employee
        post_employee_lambda = _lambda.Function(
            self, 'PostEmployeeHandler',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.from_asset('lambda'),
            handler='post_employee.lambda_handler',
            environment={
                'TABLE_NAME': table.table_name
            }
        )

        # Grant Lambda functions permissions to access the DynamoDB table
        table.grant_read_write_data(get_employees_lambda)
        table.grant_read_write_data(post_employee_lambda)

        # Define the API Gateway resource
        api = apigw.RestApi(self, 'employee-api')

        employees = api.root.add_resource('employees')
        employees.add_method('GET', apigw.LambdaIntegration(get_employees_lambda))

        employee = api.root.add_resource('employee')
        employee.add_method('POST', apigw.LambdaIntegration(post_employee_lambda))