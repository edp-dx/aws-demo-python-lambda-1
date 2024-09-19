from aws_cdk import (
    core,
    aws_lambda as _lambda,
    aws_apigateway as apigateway,
    aws_dynamodb as dynamodb,
)

class HelloApiStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        
        # DynamoDB table
        table = dynamodb.Table(
            self, 'Employee',
            partition_key={'name': 'id', 'type': dynamodb.AttributeType.STRING}
        )
        
        # Lambda for GET /employees
        get_all_employees_lambda = _lambda.Function(
            self, 'GetAllEmployeesFunction',
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler='get_all_employees.handler',
            code=_lambda.Code.from_asset('lambda')
        )
        
        # Lambda for POST /employee
        add_employee_lambda = _lambda.Function(
            self, 'AddEmployeeFunction',
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler='add_employee.handler',
            code=_lambda.Code.from_asset('lambda')
        )
        
        # API Gateway
        api = apigateway.RestApi(self, 'hello-api')
        
        # GET /employees
        employees = api.root.add_resource('employees')
        employees.add_method(
            'GET', 
            apigateway.LambdaIntegration(get_all_employees_lambda)
        )
        
        # POST /employee
        employee = api.root.add_resource('employee')
        employee.add_method(
            'POST', 
            apigateway.LambdaIntegration(add_employee_lambda)
        )
