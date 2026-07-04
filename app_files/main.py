#!/usr/bin/python
import os
import sys
import configparser
import random
import colorsys

try:
    from PIL import Image
    PILLOW_INSTALLED = True
except ImportError:
    PILLOW_INSTALLED = False

def hex_to_bgr(hex_str):
    hex_str = hex_str.lstrip('#').lstrip('$')
    r, g, b = int(hex_str[0:2], 16), int(hex_str[2:4], 16), int(hex_str[4:6], 16)
    return f"{b:02X}{g:02X}{r:02X}"

def rgb_gradient(hex1, hex2, steps):
    if steps <= 0:
        return []
    hex1 = hex1.lstrip('#').lstrip('$')
    hex2 = hex2.lstrip('#').lstrip('$')
    r1, g1, b1 = int(hex1[0:2], 16), int(hex1[2:4], 16), int(hex1[4:6], 16)
    r2, g2, b2 = int(hex2[0:2], 16), int(hex2[2:4], 16), int(hex2[4:6], 16)
    
    result = []
    for i in range(steps):
        t = i / (steps - 1) if steps > 1 else 0
        r = round(r1 + (r2 - r1) * t)
        g = round(g1 + (g2 - g1) * t)
        b = round(b1 + (b2 - b1) * t)
        result.append(f"{b:02X}{g:02X}{r:02X}")
    return result

def generate_colors(mode, c1, c2, steps):
    if steps <= 0:
        return []
    if mode == "gradient":
        return rgb_gradient(c1, c2, steps)
    elif mode == "alternate":
        return [hex_to_bgr(c1) if i % 2 == 0 else hex_to_bgr(c2) for i in range(steps)]
    elif mode == "random":
        return [f"{random.randint(0,255):02X}{random.randint(0,255):02X}{random.randint(0,255):02X}" for _ in range(steps)]
    elif mode == "rainbow":
        result = []
        for i in range(steps):
            r, g, b = colorsys.hsv_to_rgb(i / steps, 1.0, 1.0)
            result.append(f"{round(b*255):02X}{round(g*255):02X}{round(r*255):02X}")
        return result
    else:
        fixed_color = hex_to_bgr(c1)
        return [fixed_color] * steps

def get_icon_index(ext):
    ext = ext.lower()
    if ext in ['.wav', '.mp3', '.ogg', '.flac']:
        return 33
    elif ext in ['.mid', '.midi']:
        return 9
    elif ext == '.fst':
        return 37
    else:
        return 33

def main():
    print("=== FL STUDIO DRUM-KIT SKIN SCRIPT ===")
    print("Written by @imfabiyoo")
    print("fabiyoo on all streaming platforms, go listen\n")
    
    config_file = "settings.txt"
    if not os.path.exists(config_file):
        print(f"[Error] Configuration file '{config_file}' not found.")
        input("Press Enter to exit...")
        sys.exit(1)
        
    config = configparser.ConfigParser()
    try:
        config.read(config_file)
        raw_folder = config.get("config", "drumkit_folder")
        
        if os.name != 'nt':
            raw_folder = raw_folder.replace('\\', '')
            
        root_folder = os.path.normpath(os.path.abspath(raw_folder))
        ignore_subs = config.getboolean("config", "ignore_sub_folders")
        enable_colorizing = config.getboolean("config", "enable_colorizing", fallback=True)
        color_mode = config.get("config", "color_mode", fallback="gradient").strip().lower()
        folder_c1 = config.get("config", "folders_color1")
        folder_c2 = config.get("config", "folders_color2")
        file_c1 = config.get("config", "files_color1")
        file_c2 = config.get("config", "files_color2")
        enable_mosaic = config.getboolean("config", "enable_mosaic", fallback=False)
    except Exception as e:
        print(f"[Error] Failed to parse settings.txt variables: {e}")
        input("Press Enter to exit...")
        sys.exit(1)

    if enable_mosaic and not PILLOW_INSTALLED:
        print("\n[Error] 'enable_mosaic' is set to true, but Pillow is not installed.")
        print("Please activate your project venv or run: pip install Pillow")
        input("Press Enter to exit...")
        sys.exit(1)

    print(f"Target Directory: {root_folder}")
    print(f"Colorizing Modifiers: Enabled={enable_colorizing} | Mode={color_mode}")
    print(f"Mosaic Backgrounds: Enabled={enable_mosaic}")
    
    confirm = input("\nAre these settings parameters correct? (y/n): ").strip().lower()
    if confirm not in ['y', 'yes', '']:
        print("Execution halted by user.")
        return

    image_path = None
    immediate_subfolders = []
    
    if enable_mosaic:
        script_dir = os.path.dirname(os.path.abspath(__file__)) if '__file__' in globals() else os.getcwd()
        image_folder = os.path.join(script_dir, "image")
        
        if not os.path.exists(image_folder):
            os.makedirs(image_folder)
            print(f"\n[Info] Created missing 'image' directory at:\n -> {image_folder}")
            print("Drop your graphic banner into that folder and restart the script.")
            input("Press Enter to close...")
            return
            
        valid_extensions = ('.png', '.jpg', '.jpeg', '.webp', '.bmp')
        found_images = [f for f in os.listdir(image_folder) if f.lower().endswith(valid_extensions)]
        
        if not found_images:
            print(f"\n[Error] No valid source imagery found inside: {image_folder}")
            input("Press Enter to resolve and close...")
            return
        
        image_path = os.path.join(image_folder, found_images[0])
        print(f"-> Asset Identified: {found_images[0]}")

        immediate_subfolders = [
            f for f in os.listdir(root_folder)
            if os.path.isdir(os.path.join(root_folder, f)) and not f.startswith('.')
        ]
        immediate_subfolders.sort(key=lambda x: x.lower())

    print("\n[1/3] Parsing workspace structure and sweeping legacy files...")
    all_dirs = []
    files_by_dir = {}

    root_foldername = os.path.basename(root_folder)
    root_parent = os.path.dirname(root_folder)
    legacy_root_nfo = os.path.join(root_parent, f"{root_foldername}.nfo")
    if os.path.exists(legacy_root_nfo):
        try: os.remove(legacy_root_nfo)
        except Exception: pass

    if ignore_subs:
        all_dirs.append(root_folder)
        files_by_dir[root_folder] = []
        for entry in os.scandir(root_folder):
            if entry.is_file():
                if entry.name.lower().endswith('.nfo') or entry.name.lower().startswith('_slice_'):
                    try: os.remove(entry.path) 
                    except Exception: pass
                else:
                    files_by_dir[root_folder].append(entry.name)
    else:
        for subdir, dirs, files in os.walk(root_folder):
            all_dirs.append(subdir)
            files_by_dir[subdir] = []
            for file in files:
                file_path = os.path.join(subdir, file)
                if file.lower().endswith('.nfo') or file.lower().startswith('_slice_'):
                    try: os.remove(file_path)
                    except Exception: pass
                else:
                    files_by_dir[subdir].append(file)

    all_dirs.sort(key=lambda x: x.lower())

    mosaic_map = {}
    if enable_mosaic and immediate_subfolders:
        print("[2/3] Slicing artwork configurations...")
        try:
            img = Image.open(image_path)
            img_w, img_h = img.size
            
            target_slice_height = 52 
            target_total_height = target_slice_height * len(immediate_subfolders)
            target_width = int(img_w * (target_total_height / img_h))
            
            img = img.resize((target_width, target_total_height), Image.BICUBIC)
            img_w, img_h = img.size
            slice_h = img_h / len(immediate_subfolders)
            
            for idx, folder_name in enumerate(immediate_subfolders):
                top = int(idx * slice_h)
                bottom = int((idx + 1) * slice_h)
                
                slice_img = img.crop((0, top, img_w, bottom))
                safe_name = "".join([c for c in folder_name if c.isalnum() or c in ' -_']).strip()
                slice_filename = f"_slice_{safe_name}.png"
                
                slice_img.save(os.path.join(root_folder, slice_filename), "PNG")
                mosaic_map[folder_name] = slice_filename
        except Exception as e:
            print(f"[Error] Image processor failed: {e}")
            input("Press Enter to quit...")
            return
    else:
        print("[2/3] Skipping Mosaic generation...")

    print("Writing Folder configurations...")
    if enable_colorizing:
        sub_dirs = [d for d in all_dirs if d != root_folder]
        sub_folder_colors = generate_colors(color_mode, folder_c1, folder_c2, len(sub_dirs))

    sub_idx = 0
    for folder_path in all_dirs:
        folder_path = os.path.normpath(folder_path)
        foldername = os.path.basename(folder_path)
        
        if folder_path == root_folder:
            parent_dir = os.path.dirname(root_folder)
            target_nfo = os.path.join(parent_dir, f"{foldername}.nfo")
            is_immediate_sub = False
            current_color = hex_to_bgr(folder_c1) if enable_colorizing else None
        else:
            parent_dir = os.path.dirname(folder_path)
            target_nfo = os.path.join(parent_dir, f"{foldername}.nfo")
            is_immediate_sub = (parent_dir == root_folder)
            current_color = sub_folder_colors[sub_idx] if enable_colorizing else None
            sub_idx += 1
        
        nfo_lines = []
        if enable_colorizing and current_color:
            nfo_lines.append(f"Color=${current_color}")
        
        if enable_mosaic and is_immediate_sub and foldername in mosaic_map:
            nfo_lines.append(f"Bitmap={mosaic_map[foldername]}")
            
        # Removed text strings and normalized height offset variables to clear spacing bugs
        nfo_lines.extend(["IconIndex=21", "SortGroup=1"])
        
        try:
            with open(target_nfo, 'w', encoding='utf-8') as f:
                f.write("\n".join(nfo_lines) + "\n")
        except Exception as e:
            print(f"\n[Error] File crash at {target_nfo}: {e}")

    print("[3/3] Analyzing and processing file parameters...")
    for folder_path, files in files_by_dir.items():
        if not files:
            continue
        files.sort(key=lambda x: x.lower())
        
        if enable_colorizing:
            file_colors = generate_colors(color_mode, file_c1, file_c2, len(files))

        for idx, filename in enumerate(files):
            base_name, ext = os.path.splitext(filename)
            target_nfo = os.path.join(folder_path, f"{base_name}.nfo")
            icon = get_icon_index(ext)
            
            nfo_lines = []
            if enable_colorizing:
                nfo_lines.append(f"Color=${file_colors[idx]}")
            
            nfo_lines.extend([f"IconIndex={icon}", "SortGroup=1"])
            
            try:
                with open(target_nfo, 'w', encoding='utf-8') as f:
                    f.write("\n".join(nfo_lines) + "\n")
            except Exception:
                pass
                
            sys.stdout.write(f"\rProcessing: {filename[:40]:<40}")
            sys.stdout.flush()

    print("\n\nSuccess! Layout build completed.")
    print("written by @imfabiyoo")
    print("fabiyoo on all streaming platforms, go listen")
    input("Press Enter to close.")

if __name__ == "__main__":
    main()