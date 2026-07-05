#!/bin/zsh
cd "$(dirname "$0")"
echo "=== Setting up FL Studio Skin Generator ==="

# Check if python3 is actually installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed or not recognized."
    echo "Please download it from Python.org and try again."
    echo "Press Enter to exit..."
    read
    exit 1
fi

python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r app_files/requirements.txt

echo "=== Setup Complete! You can now run the tool. ==="
echo "Press Enter to close this window..."
read