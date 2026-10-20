# 👁️ Gojo Satoru Super Wallpaper (HyperOS / MIUI & Android)

[![Platform](https://img.shields.io/badge/Platform-Android%20%7C%20Xiaomi%20HyperOS%20%7C%20MIUI-blue.svg)](https://android.com)
[![Engine](https://img.shields.io/badge/Engine-OpenGL%20ES%202.0%20LiveWallpaper-cyan.svg)]()
[![Resolution](https://img.shields.io/badge/Resolution-1220x2712%2024fps-blue.svg)]()
[![License](https://img.shields.io/badge/License-MIT%20%2F%20Non--Commercial-green.svg)]()

A high-performance **Gojo Satoru (Limitless / Six Eyes Reveal)** Super Wallpaper for Android devices, natively optimized for **Xiaomi HyperOS** and **MIUI**.

Lockscreen plays the opening segment and holds at **3.375000s**. Unlock jumps directly to the home segment at **3.416667s**, including direct AOD unlock and unlock during the intro.

---

## 🌟 Features

- **Domain boundary**: Lock holds on source frame 81 (3.375s), after the hand sign and before the first background cracks. Home starts on frame 82 (3.416667s), a forced video keyframe.
- **Separate lock and home segments**: Frame zero is used only for lock startup. Screen-off does not decode a frame-zero preroll; a matching `home.jpg` covers the home seek until a home frame is available.
- **Standalone Package**: Configured with unique package identifier `com.androradar.walls6.gojo`, allowing seamless side-by-side installation with Sukuna Super Wallpaper without conflicts.
- **Native HyperOS / MIUI Intent Hooks**: Registered with `miui.service.wallpaper.SuperWallpaperService` and `is_super_wallpaper=true` for seamless integration into Xiaomi's wallpaper pipeline.
- **Universal Android Compatibility**: Also works on Samsung One UI, Google Pixel, OnePlus OxygenOS, and stock Android via the Google Wallpapers app.

---

## 📁 Repository Structure

```
GojoSuperWallpaper/
├── prebuilt/
│   └── GojoSuperWallpaper.apk     # Ready-to-install signed APK (17.63 MB)
├── miside_decompiled/             # Full Apktool source tree
│   ├── AndroidManifest.xml        # Unique package `com.androradar.walls6.gojo`
│   ├── apktool.yml                # apktool build configuration
│   ├── assets/
│   │   ├── backup.jpg             # Lock startup fallback image
│   │   ├── sukuna_aod.png         # Companion AOD texture
│   │   └── unlocked.mp4           # 1220x2712 native 24fps video; home IDR at 3.416667s
│   ├── res/                       # App icons, strings & wallpaper metadata
│   └── smali/                     # Modified OpenGL ES wallpaper engine & shader logic
│       └── com/androradar/walls6/
│           ├── VideoPlayer.smali                # Requested playback mode and texture readiness
│           └── VideoPlayer$VideoHandler.smali   # Serialized lock/home decoder messages
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
To install without ADB, copy `prebuilt/GojoSuperWallpaper.apk` into your device download folder:
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


## Playback fix and verification (v1.1.0)

See [playback behavior, exact frames and checks](docs/PLAYBACK.md), the [boundary image](docs/transition-boundary.jpg), and [project navigation map](docs/PROJECT_MAP.md).

`media-timing.json` records the reviewed source clip/hash, lock hold and first home frame. `scripts/prepare_media.py <source.mp4>` rebuilds media with a home IDR and matching fallback image. Historical anchor patchers are not part of the build and can overwrite these fixes if replayed.
