@echo off
if "%CD%"=="" set "CD=%~dp0"
cd "%CD%"
python -m venv .venv
call .venv\Scripts\activate
pip install -r requirements.txt
