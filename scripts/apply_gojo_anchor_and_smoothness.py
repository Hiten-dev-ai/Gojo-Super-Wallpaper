import os
import shutil
import subprocess

gojo_root = r"D:\Projects\GojoSuperWallpaper"
sukuna_root = r"D:\Projects\SukunaSuperWallpaper"

# 1. Copy test_gojo_105.mp4 to unlocked.mp4
test_gojo_vid = r"C:\Users\hiten_9mpt\.gemini\antigravity\brain\bedfd4a0-9133-46b8-a077-4f5c8d8e64d8\test_gojo_105.mp4"
dst_vid = os.path.join(gojo_root, "miside_decompiled", "assets", "unlocked.mp4")
shutil.copyfile(test_gojo_vid, dst_vid)
print("Copied test_gojo_105.mp4 to Gojo unlocked.mp4, size:", os.path.getsize(dst_vid))

# 2. Extract preview/backup at 1.050s
backup_jpg = os.path.join(gojo_root, "miside_decompiled", "assets", "backup.jpg")
subprocess.run(["ffmpeg", "-y", "-ss", "00:00:01.050", "-i", dst_vid, "-vframes", "1", backup_jpg], check=True)
for drawable in ["banner.jpg", "preview.jpg"]:
    p = os.path.join(gojo_root, "miside_decompiled", "res", "drawable-xxhdpi-v4", drawable)
    shutil.copyfile(backup_jpg, p)
print("Updated Gojo backup.jpg and drawables at 1.050s")

# 3. Copy smoothed VideoStream.smali from Sukuna
sukuna_stream = os.path.join(sukuna_root, "miside_decompiled", "smali", "com", "androradar", "walls6", "VideoStream.smali")
gojo_stream = os.path.join(gojo_root, "miside_decompiled", "smali", "com", "androradar", "walls6", "VideoStream.smali")
shutil.copyfile(sukuna_stream, gojo_stream)
print("Copied smoothed VideoStream.smali from Sukuna to Gojo")

# 4. Update VideoPlayer.smali in Gojo (playToLock -> 0x100590)
p_path = os.path.join(gojo_root, "miside_decompiled", "smali", "com", "androradar", "walls6", "VideoPlayer.smali")
with open(p_path, "r", encoding="utf-8") as f:
    p_content = f.read()

# It might have 0x1e8480 (2.0s) or 0x1b7740 (1.8s)
for old_val in ["0x1e8480", "0x1b7740"]:
    if old_val in p_content:
        p_content = p_content.replace(old_val, "0x100590")
        print(f"Replaced {old_val} with 0x100590 in Gojo VideoPlayer.smali")

with open(p_path, "w", encoding="utf-8", newline="") as f:
    f.write(p_content)

# 5. Update VideoPlayer$VideoHandler.smali in Gojo (resumeAdvance -> 0x100590)
h_path = os.path.join(gojo_root, "miside_decompiled", "smali", "com", "androradar", "walls6", "VideoPlayer$VideoHandler.smali")
with open(h_path, "r", encoding="utf-8") as f:
    h_content = f.read()

for old_val in ["0x1e8480", "0x1b7740"]:
    if old_val in h_content:
        h_content = h_content.replace(old_val, "0x100590")
        print(f"Replaced {old_val} with 0x100590 in Gojo VideoPlayer$VideoHandler.smali")

with open(h_path, "w", encoding="utf-8", newline="") as f:
    f.write(h_content)

print("All Gojo smali updates completed!")
