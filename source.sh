#!/bin/bash

if [ "$PWD" = "$(dirname $0)" ]; then
    echo "Running from the project root."
else
    echo "Not running from the project root. Changing directory..."
    cd "$(dirname $0)"
fi

# Activate the virtual environment
if [ -d ".venv" ]; then
    echo "Activating virtual environment..."
    source .venv/bin/activate
else
    echo "No virtual environment found. Please create one and install dependencies."
fi
