#!/bin/bash

if [ -z "$BASH_SOURCE" ]; then
    echo "Error: Could not determine script location."
    exit 1
fi

export CDK_DEPLOY_ACCOUNT=your-aws-account-id
export CDK_DEPLOY_REGION=your-aws-region

cd "$(dirname "$BASH_SOURCE")"
cdk deploy
