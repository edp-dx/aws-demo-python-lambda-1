@echo off

if "%~dp0" == "" (
    echo Error: Could not determine script location.
    exit /b 1
)

set CDK_DEPLOY_ACCOUNT=your-aws-account-id
set CDK_DEPLOY_REGION=your-aws-region

cd "%~dp0"
cdk deploy
