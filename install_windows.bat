@echo off
cd /d "%~dp0"
echo === Setting up FL Studio Skin Generator ===
python -m venv venv
call venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r app_files/requirements.txt
echo === Setup Complete! You can now run the tool. ===
pause