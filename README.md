# 👁️ Gojo Satoru Super Wallpaper (HyperOS / MIUI & Android)

[![Platform](https://img.shields.io/badge/Platform-Android%20%7C%20Xiaomi%20HyperOS%20%7C%20MIUI-blue.svg)](https://android.com)
[![Engine](https://img.shields.io/badge/Engine-OpenGL%20ES%202.0%20LiveWallpaper-cyan.svg)]()
[![Resolution](https://img.shields.io/badge/Resolution-1080x1920%2024fps-blue.svg)]()
[![License](https://img.shields.io/badge/License-MIT%20%2F%20Non--Commercial-green.svg)]()

A high-performance **Gojo Satoru (Limitless / Six Eyes Reveal)** Super Wallpaper for Android devices, natively optimized for **Xiaomi HyperOS** and **MIUI**.

Features an AMOLED standby frame on lockscreen standby, transitioning smoothly into the iconic blindfold removal and **Six Eyes (六眼)** reveal animation at **2.000s** when unlocked.

---

## 🌟 Features

- **Six Eyes Reveal**: Exact keyframe alignment at **2.000s** (`2000000 µs` = `0x1e8480`) where Satoru Gojo lifts his blindfold to reveal his glowing blue Six Eyes.
- **AMOLED Frame 0 Standby**: Lockscreen keyguard renders a static standby Frame 0 (`backup.jpg`) during standby to eliminate battery drain and prevent keyguard desync.
- **Standalone Package**: Configured with unique package identifier `com.androradar.walls6.gojo`, allowing seamless side-by-side installation with Sukuna Super Wallpaper without conflicts.
- **Native HyperOS / MIUI Intent Hooks**: Registered with `miui.service.wallpaper.SuperWallpaperService` and `is_super_wallpaper=true` for seamless integration into Xiaomi's wallpaper pipeline.
- **Universal Android Compatibility**: Also works on Samsung One UI, Google Pixel, OnePlus OxygenOS, and stock Android via the Google Wallpapers app.

---

## 📁 Repository Structure

```
GojoSuperWallpaper/
├── prebuilt/
│   └── GojoSuperWallpaper.apk     # Ready-to-install signed APK (9.72 MB)
├── miside_decompiled/             # Full Apktool source tree
│   ├── AndroidManifest.xml        # Unique package `com.androradar.walls6.gojo`
│   ├── apktool.yml                # apktool build configuration
│   ├── assets/
│   │   ├── backup.jpg             # Frame 0 standby image
│   │   ├── sukuna_aod.png         # Companion AOD texture
│   │   └── unlocked.mp4           # 1080x1920 24fps video with keyframe at 2.000s
│   ├── res/                       # App icons, strings & wallpaper metadata
│   └── smali/                     # Modified OpenGL ES wallpaper engine & shader logic
│       └── com/androradar/walls6/
│           ├── VideoPlayer.smali                # playToLock paused at 2.0s (0x1e8480)
│           └── VideoPlayer$VideoHandler.smali   # resumeAdvance direct seek at 2.0s (0x1e8480)
├── scripts/
│   ├── update_gojo_smali.py       # Timestamp patching utility
│   └── install_helper.py          # Device installation helper
├── build.ps1                      # One-click PowerShell build & sign script
├── build.bat                      # One-click Batch build script
├── .gitignore
└── README.md
```

---

## 🚀 Installation

### Option 1: Direct ADB Install (Screen Unlocked)
Unlock your device screen and run:
```bash
adb -s SCU4VSEQ8HV8RG85 install -r -d prebuilt/GojoSuperWallpaper.apk
```
*(On Xiaomi / HyperOS devices, tap **Install** on the "Install via USB" system prompt when it appears).*

### Option 2: On-Device File Manager
The APK is also pre-staged in your device download folder:
1. Open the **Files** / **File Manager** app on your phone.
2. Navigate to **Downloads** (`/sdcard/Download/`).
3. Tap **GojoSuperWallpaper.apk** and confirm install.

### Apply the Wallpaper
- **Xiaomi HyperOS / MIUI**:
  1. Open **Settings** > **Wallpaper** > **Super Wallpaper** (or Live Wallpapers).
  2. Select **Gojo Satoru Super Wallpaper** (`com.androradar.walls6.gojo`).
  3. Apply to **Both Lock Screen and Home Screen**.
- **Other Android Devices**:
  1. Install [Google Wallpapers](https://play.google.com/store/apps/details?id=com.google.android.apps.wallpaper) from the Play Store.
  2. Open Wallpapers > **Live Wallpapers** > Select **Gojo Satoru Super Wallpaper** > Apply.

---

## 🛠️ Building from Source

Recompile and sign using the PowerShell build script:
```powershell
.\build.ps1
```
This executes `apktool` to compile `miside_decompiled/` and `uber-apk-signer` to zipalign and sign with Android debug credentials.
