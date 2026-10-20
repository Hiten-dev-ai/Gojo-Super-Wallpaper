import os
import shutil
import subprocess

gojo_root = r"D:\Projects\GojoSuperWallpaper"
vid_path = os.path.join(gojo_root, "miside_decompiled", "assets", "unlocked.mp4")

# 1. Extract backup.jpg at 0.0s
backup_jpg = os.path.join(gojo_root, "miside_decompiled", "assets", "backup.jpg")
subprocess.run(["ffmpeg", "-y", "-ss", "00:00:00.000", "-i", vid_path, "-vframes", "1", backup_jpg], check=True)

# 2. Extract preview/banner at 3.0s
preview_jpg = os.path.join(gojo_root, "miside_decompiled", "res", "drawable-xxhdpi-v4", "preview.jpg")
banner_jpg = os.path.join(gojo_root, "miside_decompiled", "res", "drawable-xxhdpi-v4", "banner.jpg")
subprocess.run(["ffmpeg", "-y", "-ss", "00:00:03.000", "-i", vid_path, "-vframes", "1", preview_jpg], check=True)
shutil.copyfile(preview_jpg, banner_jpg)
print("Updated Gojo drawables (backup at 0.0s, preview/banner at 3.0s)!")

# 3. Update VideoPlayer.smali in Gojo (playToLock -> 0x2dc6c0)
base = os.path.join(gojo_root, "miside_decompiled", "smali", "com", "androradar", "walls6")
p_path = os.path.join(base, "VideoPlayer.smali")
with open(p_path, "r", encoding="utf-8") as f:
    c = f.read()

for old in ["0x100590", "0x1e8480", "0x1b7740"]:
    if old in c:
        c = c.replace(old, "0x2dc6c0")
        print(f"Replaced {old} with 0x2dc6c0 in Gojo VideoPlayer.smali")

with open(p_path, "w", encoding="utf-8", newline="") as f:
    f.write(c)

# 4. Update VideoPlayer$VideoHandler.smali in Gojo (resumeAdvance -> 0x2dc6c0)
h_path = os.path.join(base, "VideoPlayer$VideoHandler.smali")
with open(h_path, "r", encoding="utf-8") as f:
    c = f.read()

for old in ["0x100590", "0x1e8480", "0x1b7740"]:
    if old in c:
        c = c.replace(old, "0x2dc6c0")
        print(f"Replaced {old} with 0x2dc6c0 in Gojo VideoPlayer$VideoHandler.smali")

with open(h_path, "w", encoding="utf-8", newline="") as f:
    f.write(c)

print("All Gojo assets and smali updated to 3.0s (0x2dc6c0)!")
