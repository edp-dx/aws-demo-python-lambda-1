#!/bin/bash

if [ "$(dirname "$0")" == "$(pwd)" ]; then
    echo "You are already in the virtual environment."
else
    source $(dirname "$0")/venv/bin/activate
fi
