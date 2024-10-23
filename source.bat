@echo off
if "%CD%"=="" set "CD=%~dp0"
cd "%CD%"
python -m venv .venv
call .venv\Scripts\activate.bat
pip install -r requirements.txt