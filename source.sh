#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: source.sh <environment>"
  exit 1
fi

if [ "$1" == "dev" ]; then
  export AWS_PROFILE=dev
  export CDK_DEFAULT_ACCOUNT=<accountId>
  export CDK_DEFAULT_REGION=us-west-2
elif [ "$1" == "prod" ]; then
  export AWS_PROFILE=prod
  export CDK_DEFAULT_ACCOUNT=<accountId>
  export CDK_DEFAULT_REGION=us-west-2
else
  echo "Invalid environment: $1"
  exit 1
fi
