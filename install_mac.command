#!/bin/zsh
cd "$(dirname "$0")"
echo "=== Setting up FL Studio Skin Generator ==="
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r app_files/requirements.txt
echo "=== Setup Complete! You can now run the tool. ==="
pause