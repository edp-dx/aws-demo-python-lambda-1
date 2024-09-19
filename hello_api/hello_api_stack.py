from aws_cdk import (aws_lambda as _lambda, aws_apigateway as apigateway, core)

class HelloApiStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Define the Lambda function
        hello_lambda = _lambda.Function(
            self, 'HelloHandler',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.from_asset('lambda'),
            handler='hello_world.lambda_handler',
        )

        # Define API Gateway
        api = apigateway.LambdaRestApi(
            self, 'hello-api',
            handler=hello_lambda,
        )
