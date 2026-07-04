
FL STUDIO DRUM-KIT SKIN SCRIPT
Written by @imfabiyoo

An automation script designed to customize your FL Studio browser layout via .nfo generation. It handles text coloring alongside continuous graphical mosaic artwork setups.

FEATURES:
- 5 Color Modes: gradient, solid, alternate, rainbow, and random.
- Mosaic Generation: Slices images from the 'image' folder into banners matching your sidebar folders.
- Automatic cleaning removes old layouts before rebuilding.

DEPENDENCIES:
1. Python 3.9 or higher
2. Pillow (Required ONLY if enable_mosaic = true is enabled)
* Note: Core features like gradients and config parsing use pure Python standard libraries. No extra pip installs needed!

PROJECT STRUCTURE:
your-project-folder/
├── main.py             
├── settings.txt        
└── image/              <-- Drop your mosaic image here (.jpg or .png)

HOW TO RUN IN TERMINAL


1. Open your Terminal (macOS) or Command Prompt (Windows).

2. Navigate to your project folder:
   cd "path/to/your-project-folder"

3. Build an isolated environment:
   Windows: python -m venv venv
   macOS:   python3 -m venv venv

4. Turn on the environment:
   Windows (CMD):        venv\Scripts\activate.bat
   Windows (PowerShell): .\venv\Scripts\Activate.ps1
   macOS:                source venv/bin/activate

   (You will see a "(venv)" prefix pop up on your command line)

5. Install the image processing engine (if using Mosaic mode):
   pip install Pillow

6. Edit 'settings.txt' with your exact kit folder path, then run:
   Windows: python main.py
   macOS:   python3 main.py
