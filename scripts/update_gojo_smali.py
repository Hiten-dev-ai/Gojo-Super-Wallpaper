import os

base_dir = r"D:\Projects\GojoSuperWallpaper\miside_decompiled\smali\com\androradar\walls6"

files_to_patch = [
    os.path.join(base_dir, "VideoPlayer.smali"),
    os.path.join(base_dir, "VideoPlayer$VideoHandler.smali")
]

for file_path in files_to_patch:
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        continue
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "0x1b7740" in content:
        content = content.replace("0x1b7740", "0x1e8480")
        with open(file_path, "w", encoding="utf-8", newline="") as f:
            f.write(content)
        print(f"Patched 0x1b7740 -> 0x1e8480 in {os.path.basename(file_path)}")
    elif "0x1e8480" in content:
        print(f"Already contains 0x1e8480 in {os.path.basename(file_path)}")
    else:
        print(f"Warning: Neither pattern found in {os.path.basename(file_path)}")
