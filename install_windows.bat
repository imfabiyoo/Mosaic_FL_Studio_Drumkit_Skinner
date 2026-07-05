@echo off
cd /d "%~dp0"
echo === Setting up FL Studio Skin Generator ===

:: Check if Python is installed and added to PATH
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not recognized!
    echo You likely forgot to check the "Add Python to PATH" box during installation.
    echo Please uninstall Python, reinstall it, and make sure to check that box.
    echo.
    pause
    exit /b
)

python -m venv venv
call venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r app_files/requirements.txt

echo === Setup Complete! You can now run the tool. ===
pause