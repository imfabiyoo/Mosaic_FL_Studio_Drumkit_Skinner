# FL Studio Drum-Kit Skinner & Mosaic Generator
**Created by @imfabiyoo**

Welcome! If you want to customize your FL Studio browser layout with custom text colors or full mosaic artwork, you are in the right place. 

This tool does all the heavy lifting for you. You do not need to know how to code to use this! Just follow the simple steps below.

---

## Step 1: The One-Time Setup (Read This First!)
Before you can run the tool, your computer needs to know how to read the code. You only have to do this once.

**1. Download Python**
This script runs on a language called Python. 
* Go to Python.org and download the latest version.
* **CRITICAL FOR WINDOWS USERS:** When the installer pops up, look at the very bottom of the window. You **MUST** check the box that says **"Add Python to PATH"** before you click install. If you skip this, the tool will not work!

**2. Install the Script's Engine**
Now that Python is installed, we need to download the tools that slice your images.
* **Mac Users:** Double-click the `install_mac.command` file.
* **Windows Users:** Double-click the `install_windows.bat` file.
* A black text window (Terminal/Command Prompt) will pop up and text will scroll by. Don't panic! It is just safely downloading the image tools it needs. When it finishes, you can close that window.

---

## Step 2: How to Use the Tool
Once the setup is done, running the tool is incredibly easy.

1. **Add your image:** Place the picture you want to use inside the `image` folder.
2. **Tweak your settings:** Open the `settings.txt` file. This is where you tell the tool where your drum kit is located and what colors you want to use. Save the file when you are done.
3. **Run it:**
   * **Mac Users:** Double-click `run_mac.command`.
   * **Windows Users:** Double-click `run_windows.bat`.
4. Open FL Studio and enjoy your new custom layout!

---

## Troubleshooting & Fixes (The "Help, it broke!" Section)
If things aren't working right, don't worry. Here are the most common issues and exactly how to fix them:

### Windows Issues
* **Error: "Python is not recognized as an internal or external command"**
  * **The Fix:** You forgot to check the "Add to PATH" box when installing Python. Uninstall Python from your computer, download it again, and make sure that box is checked at the bottom of the installer!
* **The black window opens and instantly closes before I can read it!**
  * **The Fix:** This usually means there is a typo in your `settings.txt` file. Double-check that your folder paths are correct and that you didn't accidentally delete any important formatting.

### Mac Issues
* **Error: "install_mac.command cannot be opened because it is from an unidentified developer."**
  * **The Fix:** Apple tries to block apps that don't come from the App Store. Open your Mac's **System Settings > Privacy & Security**. Scroll down, and you will see a message saying the script was blocked. Click **"Open Anyway"**. 
* **Error: "Permission Denied" when trying to double-click the Mac files.**
  * **The Fix:** Your Mac is being overly protective. Open the "Terminal" app on your Mac. Type `chmod +x ` (make sure to include the space at the end). Then, drag and drop the `.command` file directly into the Terminal window and press Enter. You can now double-click it normally!

---

## How to Update to a New Version
When a new update is released to fix bugs or add features, here is how you upgrade without breaking anything:
1. Download the new version of the tool from this GitHub page (click the green "Code" button and select "Download ZIP").
2. Replace the old `app_files` folder with the new `app_files` folder. 
3. **Do not** overwrite your `settings.txt` or `image` folder! This way, you keep all your custom configurations and artwork perfectly intact.

---

## What do all these files do?
If you are curious, here is how the folder is organized:
* `app_files/` — The "brain" of the tool. You never need to touch anything in here.
* `install` / `run` files — Your easy double-click buttons to make the script work.
* `.gitignore` & `README.md` — Files used by GitHub to display this page and keep our backend environment files (like `venv/`) out of the final download. You can ignore them!
