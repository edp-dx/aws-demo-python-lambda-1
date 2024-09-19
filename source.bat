@echo off

if "%CD%"=="%~dp0" (
    echo Running from the project root.
) else (
    echo Not running from the project root. Changing directory...
    cd "%~dp0"
)

REM Activate the virtual environment
if exist .venv (
    echo Activating virtual environment...
    .venv\Scripts\activate.bat
) else (
    echo No virtual environment found. Please create one and install dependencies.
)
