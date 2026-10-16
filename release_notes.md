# Genghis Khan: Desert Heroes (成吉思汗之大漠英雄傳) v1.0 Turnkey Native Edition

A complete, modern, turnkey release of the classic 2001/1999 PC RTS/historical strategy game **成吉思汗之大漠英雄傳** (*Genghis Khan: Desert Heroes* / *Legend of the Desert Heroes*), developed by 詮積資訊 (GrandTech) and published by 智冠科技 (Soft-World) / 光譜資訊 (T-Time).

## ✨ Key Features & Enhancements
- **Multi-Platform Native Support**: Runs out-of-the-box natively on **Windows 10/11** (via `Launch_Game_Win.bat`) and **Linux / Steam Deck** (via `./run_native.sh`) without requiring legacy virtual machines (DOSBox / PCem).
- **Modern 4K DirectDraw Display Engine**: Powered by `cnc-ddraw` with hardware-accelerated OpenGL/GDI rendering, 4:3 integer aspect correction, clean system window borders, and seamless `Alt + Enter` fullscreen toggle.
- **100% Dual-Language Localization**:
  - Full English translation with custom 12px ASCII proportional font kerning arithmetic patch (`0x46ce12`).
  - Original 1999 Traditional Chinese mode preserved with authentic Big-5 font and assets.
  - Interactive 1-click language switcher (`switch_language.sh` on Linux, `Switch_Language_Win.bat` on Windows).
- **Critical Bugfixes & Reverse-Engineered Code Caves**:
  - **Bounds-Guard Patch (`0x420bd5`)**: Fixed the fatal unhandled page fault crash when clicking on the tactical map while paused or near UI boundaries.
  - **Calibrated Mouse Edge Scrolling**: Reduced panning speed by ~16.7x (50 timer ticks divider) for steady, controllable RTS camera control.
  - **Manual Dialogue Progression**: Neutralized auto-advancing timers so dialogues wait indefinitely for player confirmation (`Space`, `Enter`, or click).
  - **Speed Controls**: In-game game speed adjustable via top-row `+`/`-` keys and Numpad keys.
  - **DRM Bypass**: Bypassed CD-ROM Disc 2 hardware check for 100% portable drive play.
- **Audio & Media**: 14 high-quality CD audio tracks (OGG), 16-bit PCM battle sound effects, and high-resolution intro cutscene (`Title.avi`).
- **Save Games**: Pre-unlocked historical campaign stages (Hero11–Hero19).

## 🚀 Quick Start
- **Windows**: Extract the archive and double-click `Launch_Game_Win.bat`.
- **Linux / Steam Deck**: Extract the archive and run `./setup.sh` (or `./run_native.sh`).

## ⚖️ Non-Commercial Disclaimer & Takedown Policy
This release is a free, non-commercial community preservation and reverse-engineering enhancement project. All original assets remain the intellectual property of their original creators. No revenue, donations, ads, or paywalls are associated with this project.
If you are a copyright holder or successor entity and wish for any materials or links to be removed, please contact `wzli.dev@gmail.com` and we will immediately take down the requested links upon notice.
