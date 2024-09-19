@echo off
if "%CD%" == "%~dp0" (
    echo You are already in the virtual environment.
) else (
    call "%~dp0venv\Scripts\activate.bat"
)