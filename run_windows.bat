@echo off
cd /d "%~dp0"

:: Prevent running if the user skipped the install step
if not exist venv\ (
    echo ERROR: Environment not found!
    echo Please double-click install_windows.bat first.
    echo.
    pause
    exit /b
)

call venv\Scripts\activate
python app_files/main.py

echo.
pause