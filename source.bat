@echo off

if "%1"=="" (
    echo Usage: source.bat ENVIRONMENT
    exit /b 1
)

if "%1"=="dev" (
    setx AWS_PROFILE dev
    setx CDK_DEFAULT_ACCOUNT <accountId>
    setx CDK_DEFAULT_REGION us-west-2
) else if "%1"=="prod" (
    setx AWS_PROFILE prod
    setx CDK_DEFAULT_ACCOUNT <accountId>
    setx CDK_DEFAULT_REGION us-west-2
) else (
    echo Invalid environment: %1
    exit /b 1
)
