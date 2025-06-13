@echo off
echo [INFO] Activating virtual environment...
call venv\Scripts\activate.bat

echo [INFO] Using local Python and pip...
venv\Scripts\python.exe -m pip install --upgrade pip
venv\Scripts\python.exe -m pip install -r requirements.txt
