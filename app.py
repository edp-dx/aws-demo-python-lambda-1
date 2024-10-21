#!/usr/bin/env python3
import os
import aws_cdk as cdk
from hello_api.hello_api_stack import HelloApiStack

app = cdk.App()
HelloApiStack(app, "HelloApiStack", env=cdk.Environment(
    account=os.getenv('CDK_DEFAULT_ACCOUNT'),
    region=os.getenv('CDK_DEFAULT_REGION')
))

app.synth()
