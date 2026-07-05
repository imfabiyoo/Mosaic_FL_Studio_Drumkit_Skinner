#!/bin/zsh
cd "$(dirname "$0")"

# Prevent running if the user skipped the install step
if [ ! -d "venv" ]; then
    echo "ERROR: Environment not found!"
    echo "Please double-click install_mac.command first."
    echo "Press Enter to exit..."
    read
    exit 1
fi

source venv/bin/activate
python3 app_files/main.py

echo ""
echo "Press Enter to close this window..."
read