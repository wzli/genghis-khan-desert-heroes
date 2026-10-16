# Title: [Release] Genghis Khan: Desert Heroes (成吉思汗之大漠英雄傳, 1999/2001) – Fully Restored Turnkey PC Edition (Win 10/11 & Linux/Steam Deck) with First-Ever English Translation & 4K Fix

Hi everyone,

*Genghis Khan: Desert Heroes* (成吉思汗之大漠英雄傳) was a rare, commercial historical RTS + RPG hybrid developed in Taiwan by GrandTech (詮積資訊) and published by Soft-World (智冠) / T-Time (光譜) in 2001 (re-released as v1.15 in 2004). 

Until recently, Western gamers and modern retro enthusiasts couldn't easily play it because:
1. It was never localized into English.
2. In classic retro threads, it was trapped inside an 8GB Windows 98 virtual machine image due to DirectDraw compatibility issues on modern NT kernels.
3. In modern environments, it suffered from severe mouse lag, aggressive screen edge scrolling, and an unhandled page fault crash (`0x420bd5`) whenever the player clicked the tactical map while paused or near UI edges.

We reverse-engineered `Hero.exe` and reconstructed the entire game into a standalone, lightweight (284 MB) turnkey release that runs natively on modern Windows and Linux without any VM.

### What Was Restored / Enhanced:
* **Native Windows 10/11 & Linux / Steam Deck Support**: Runs directly on modern OSes without virtual machines. Includes turnkey launchers for both Windows (`Launch_Game_Win.bat`) and Linux (`./run_native.sh`).
* **Modern 4K DirectDraw GPU Scaling**: Powered by `cnc-ddraw` with OpenGL/GDI backends, 4:3 integer aspect correction, window borders, and seamless `Alt + Enter` borderless fullscreen switching.
* **First-Ever Complete English Localization**:
  - Re-engineered the in-engine text rasterizer at `0x46ce0f` from double-byte 24px spacing down to natural 12px ASCII proportional font kerning, doubling line character capacity without text truncation.
  - Translated all menus, UI signboards, tactical battle HUD buttons (`windows.dat`), hover overlays (`selects.dat`), and all 396 historical generals in `stage.ini` into English.
  - Authentic 1999 Traditional Chinese mode is fully preserved and switchable anytime via 1-click script (`Switch_Language_Win.bat` / `switch_language.sh`).
* **Bounds-Guard Code Cave (`0x420bd5` Crash Fix)**:
  - Installed a detour at `0x420bcc` calling a safe bounds-check code cave at `0x47f480`, preventing out-of-bounds pointer dereferences and eliminating crashes when paused or clicking off-map.
* **Calibrated Edge-of-Screen Panning**:
  - Tuned the multimedia timer tick divider (`0x42f6e9`) from 3 to 50 (~16.7x slower) and edge inception delay to 10 ticks, providing smooth, controllable RTS camera panning.
* **Manual Dialogue Progression**: Neutralized forced countdown timers so story dialogues wait for player input (`Space` / `Enter` / click).
* **Speed Controls**: In-game game speed can be toggled using top-row `+`/`-` keys and Numpad keys.
* **Audio & FMV**: Includes all 14 CD audio tracks (OGG), 16-bit PCM sound effects, and high-res intro video.

### Downloads & Source Code:
* **GitHub Repository & Full Reverse-Engineering Docs**:
  https://github.com/wzli/genghis-khan-desert-heroes
* **GitHub Release v1.0 (Direct 284 MB 7z)**:
  https://github.com/wzli/genghis-khan-desert-heroes/releases/tag/v1.0
* **Internet Archive Preservation Mirror**:
  https://archive.org/details/genghis-khan-desert-heroes-1999-native

### Disclaimer:
This is a non-commercial community preservation and compatibility project. All intellectual property remains with the original developers and publishers. If you are a copyright holder and wish for links to be removed, contact wzli.dev@gmail.com.
