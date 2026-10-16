# Genghis Khan: Desert Heroes (成吉思汗之大漠英雄傳)
## Turnkey Native PC Edition (Windows & Linux) with Full English & Traditional Chinese Support

[![GitHub Release](https://img.shields.io/github/v/release/wzli/genghis-khan-desert-heroes?include_prereleases&color=blue)](https://github.com/wzli/genghis-khan-desert-heroes/releases)
[![Platform](https://img.shields.io/badge/Platform-Windows%2010%2F11%20%7C%20Linux%20%7C%20SteamDeck-blue)](https://github.com/wzli/genghis-khan-desert-heroes)
[![Languages](https://img.shields.io/badge/Languages-English%20%7C%20%E7%B9%81%E9%AB%94%E4%B8%AD%E6%96%87-orange)](https://github.com/wzli/genghis-khan-desert-heroes)
[![Engine](https://img.shields.io/badge/Engine-DirectDraw%20(cnc--ddraw)-purple)](https://github.com/wzli/genghis-khan-desert-heroes)
[![License](https://img.shields.io/badge/License-Non--Commercial%20Preservation-lightgrey)](https://github.com/wzli/genghis-khan-desert-heroes)

A complete, modern, turnkey release of the classic 2001/1999 commercial RTS/historical strategy game **成吉思汗之大漠英雄傳** (*Genghis Khan: Desert Heroes* / *Legend of the Desert Heroes*, developed by 詮積資訊 GrandTech / 智冠 Soft-World / 光譜 T-Time).

Pre-configured to run out-of-the-box natively on **Windows 10/11** and **Linux / Steam Deck** with modern 4K high-resolution display scaling, native window borders, 16-channel MIDI + PCM audio synthesis, an authentic 100% bilingual English/Traditional Chinese localization system, crash fixes, and pre-unlocked historical campaign stages.

---

## 📥 Download Game (Ready-to-Play Turnkey Package)

> [!IMPORTANT]
> **Because original CD audio, cinematics, and game media total 284 MB, the full playable game package is distributed via high-speed release mirrors rather than bloated directly into the git source repository.**
> Download the pre-packaged, zero-setup 284 MB archive from any mirror below:

| Mirror | Direct Download Link | Format / Speed |
| :--- | :--- | :--- |
| **GitHub Releases (v1.0)** | [📥 **Download Game Release (284 MB)**](https://github.com/wzli/genghis-khan-desert-heroes/releases/download/v1.0/Genghis_Khan_Desert_Heroes_v1.0_Bilingual.7z) | `.7z` / Global High-Speed CDN |
| **Internet Archive (archive.org)** | [📥 **Download from Archive.org**](https://archive.org/download/genghis-khan-desert-heroes-1999-native/Genghis_Khan_Desert_Heroes_v1.0_Bilingual.7z) | `.7z` / Permanent Digital Preservation & [Torrent](https://archive.org/download/genghis-khan-desert-heroes-1999-native/genghis-khan-desert-heroes-1999-native_archive.torrent) |
| **China Fast Mirror (国内直链)** | [📥 **国内免翻墙极速下载 (284 MB)**](https://ghfast.top/https://github.com/wzli/genghis-khan-desert-heroes/releases/download/v1.0/Genghis_Khan_Desert_Heroes_v1.0_Bilingual.7z) | `.7z` / Direct Mirror for Mainland China |

---

### ⚡ 30-Second Quick Start

#### 🪟 On Windows 10 / 11 / 7
1. **Download** `Genghis_Khan_Desert_Heroes_v1.0_Bilingual.7z` from the table above.
2. **Extract** the 7z archive anywhere on your PC (using [7-Zip](https://www.7-zip.org/) or WinRAR).
3. **Double-click `Launch_Game_Win.bat`** to play!
   - *To toggle between English and Traditional Chinese, double-click `Switch_Language_Win.bat`.*
   - *Press `Alt + Enter` anytime for borderless 4K fullscreen.*

#### 🐧 On Linux / Steam Deck
1. **Download** `Genghis_Khan_Desert_Heroes_v1.0_Bilingual.7z` from the table above.
2. **Extract** the archive and open a terminal inside the folder:
   ```bash
   ./setup.sh
   ./run_native.sh
   ```
   *(On Steam Deck, run `./setup.sh` in Desktop Mode once, then add `run_native.sh` as a Non-Steam Game to launch in Gaming Mode).*

#### 🛠 Or Clone via Git (Zero-Config Auto-Downloader)
If you clone this repository directly via Git, `./setup.sh` will automatically detect missing binaries, download the 284 MB package for you, and extract everything into place:
```bash
git clone https://github.com/wzli/genghis-khan-desert-heroes.git
cd genghis-khan-desert-heroes
./setup.sh
./run_native.sh
```

---

## Table of Contents
1. [Download Game (Ready-to-Play Package)](#-download-game-ready-to-play-turnkey-package)
2. [Quick Start & Language Options](#-quick-start)
3. [Setup & Execution (Linux & Windows)](#-complete-setup--execution)
   - [Automated Setup Script (Linux)](#1-automated-setup-script-recommended)
   - [Flatpak Wine (Linux & Steam Deck)](#2-flatpak-wine-universal-linux--steam-deck)
   - [Native System Wine (Linux)](#3-native-system-wine)
   - [Running on Windows 10 / 11 / 7](#4-running-on-windows-windows-10--11--7)
   - [Container / Docker Deployment](#5-container--docker-deployment)
4. [Key Improvements Over the Original Release](#-key-improvements-over-the-original-release)
5. [Controls, Hotkeys & Button Mappings](#-controls-hotkeys--button-mappings)
6. [Language Switching (English & Chinese)](#-language-switching)
7. [Directory Structure](#-directory-structure)
8. [Disclaimer & Notice-and-Takedown](#-disclaimer--notice-and-takedown)
9. [Troubleshooting & FAQs](#-troubleshooting--faqs)

---

## 🚀 Quick Start

Run the turnkey launcher directly from this directory:

### Run in English (Default)
```bash
./run_native.sh --lang en
```

### Run in Traditional Chinese (Original 1999)
```bash
./run_native.sh --lang zh
```

### Desktop Shortcut
You can also double-click the desktop icon:
```
成吉思汗之大漠英雄傳 (Genghis Khan 1999)
```
*(Automatically placed on `~/Desktop` and in your Linux application menu).*

---

## 🛠 Complete Setup & Wine Installation

The game engine runs on top of a lightweight Wine compatibility layer paired with our native DirectDraw wrapper. You can set it up using any of the four methods below:

### 1. Automated Setup Script (Recommended)
Run the built-in environment installer:
```bash
./setup.sh
```
This script will:
- Detect your Linux distribution and installed Wine runtime.
- Automatically offer to install `org.winehq.Wine` via Flatpak if system Wine is missing.
- Verify `7z` (required for save migration) and MIDI dependencies.
- Create system and desktop menu shortcuts (`~/Desktop/成吉思汗之大漠英雄傳.desktop`).
- Ensure all launcher permissions are executable.

---

### 2. Flatpak Wine (Universal Linux & Steam Deck)
The cleanest, zero-conflict method that works identically on **Ubuntu, Fedora, Arch, openSUSE, and Steam Deck (SteamOS)** without multiarch library headaches:

```bash
# Add Flathub if not already enabled
flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo

# Install Wine 11.0 runtime
flatpak install --user flathub org.winehq.Wine
```
`./run_native.sh` automatically detects Flatpak Wine and configures all required Big5/UTF-8 locales and DirectDraw DLL overrides.

---

### 3. Native System Wine
If you prefer running native Wine installed directly on your host OS:

#### Ubuntu / Debian (x86_64 / i386)
```bash
sudo dpkg --add-architecture i386
sudo apt-get update
sudo apt-get install -y wine wine32 wine64 libwine libwine:i386 p7zip-full timidity
```

#### Fedora / RHEL / AlmaLinux
```bash
sudo dnf install -y wine p7zip p7zip-plugins timidity++
```

#### Arch Linux / Manjaro
```bash
# Enable [multilib] in /etc/pacman.conf, then:
sudo pacman -S --needed wine wine-mono wine-gecko p7zip timidity++
```

---

### 4. Running on Windows (Windows 10 / 11 / 7)
The engine and patches are 100% compatible with modern Windows:
- **To Play**: Double-click `Launch_Game_Win.bat` (or run `assets\game\Hero.exe` directly).
- **To Switch Language**: Run `Switch_Language_Win.bat` to select English or Traditional Chinese.
- **Alt + Enter**: Toggle between borderless fullscreen and windowed mode anytime.


---

### 5. Container / Docker Deployment
A complete `Dockerfile` is included for fully isolated containerized execution:

```bash
# 1. Build the container image
docker build -t opencjsh .

# 2. Allow X11 access for local GUI
xhost +local:root

# 3. Launch the game in Docker
docker run --rm -it \
  --net=host \
  --ipc=host \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix:ro \
  -v /dev/snd:/dev/snd \
  -v $(pwd):/game \
  opencjsh
```

---

## ✨ Key Improvements Over the Original 1999 Release

| Improvement | Original 1999 Release | Turnkey Linux Edition |
| :--- | :--- | :--- |
| **CD-ROM DRM Check** | Required physical CD-ROM Disc 2 on startup (`請放入成吉思汗第二片光碟`). | **Bypassed**: Patched `0x4331e0` in `Hero.exe` for 100% portable drive play without discs. |
| **DirectDraw Graphics** | Legacy 16-bit DirectDraw (crashed on modern Windows/Wine, wrong colors). | **Modern GPU Scaling**: Powered by `cnc-ddraw` with OpenGL/GDI backends, 4:3 aspect lock. |
| **Window Mode** | Borderless fixed canvas; no window borders, cannot drag or resize. | **System Window Borders**: Clean 800x600 bordered window with draggable title bar. |
| **Fullscreen Toggle** | Hard locked into startup resolution; no way to exit fullscreen. | **Seamless Toggle**: Press **`Alt + Enter`** anytime for instant fullscreen $\leftrightarrow$ windowed switch. |
| **Windowed Display Flashing**| Wine DirectDraw triggers XRandR mode probe, flashing or blacking out monitors. | **Zero Flashing**: Enforced `nonexclusive=true` and `toggle_borderless=true` with hardware OpenGL scaling. |
| **Visual Artifacts** | Top black bar vertical offset bug and tile grid cell lines on background images. | **Fixed**: Corrected render surface viewport and texture strides. |
| **Audio Subsystem** | Silent or broken MIDI/WAV audio on modern operating systems. | **Restored**: TiMidity++ 16-channel MIDI BGM + 16-bit PCM DirectSound battle sound effects. |
| **Dialogue Spacing & Wrapping** | Monospaced 24px character spacing (`M o t h e r   o f   m y`), lines capped at 17 chars. | **Re-Engineered**: Patched `0x46ce12` to 12px ASCII spacing, expanded lines to 34/24 chars with smart word wrapping. |
| **Mouse & Menu Latency** | DirectDraw software cursor interpolation (`adjmouse=true`) and background process contention caused severe mouse lag and stutter. | **Zero Mouse Lag**: Direct 1:1 hardware mouse pass-through (`adjmouse=false`), locked 60 FPS pacing, and clean process teardown. |
| **Complete 33-Stage Campaigns**| Unlocked/cleared campaign stages (13–38) had untranslated Big5 or `????` question marks. | **100% Localized**: All 33 stages translated across top bars (`stage*.stg`), unit rosters (`stage*.spr`), and scripts (`Talk*.txt`). |
| **Menu Bitmaps** | Chinese text baked directly into 8-bit bitmaps (`mainmenu`, `single`, `stage`, etc.). | **Localized**: Re-composited golden serif English typography matching original game textures. |
| **Menu Hover Sprites** | Chinese hover overlays in `selects.dat`. | **Localized**: Re-rasterized all 5 interactive button hover sprites in `selects.dat`. |
| **Multiplayer Menus & Lobby** | Untranslated Chinese multiplayer bitmaps (`netmenu00`–`netmenu03`), hover sprites, and Chinese lobby strings. | **Fully Localized**: All 4 multiplayer signboards, hover sprites (`selects.dat`), button sprites (`netgraphics.dat`), and 57 lobby strings translated. |
| **Tactical Battle HUD** | Chinese command buttons baked in `windows.dat` (`攻擊`, `防禦`, `堅守`, etc.). | **Localized**: All 32 tactical HUD button sprites and 4 panels translated in-place. |
| **Speaker & Roster Names** | Chinese character names in dialogue headers and hero roster (`也速該`, `鐵木真`). | **Localized**: Reversed `stage.ini` database and translated all 396 generals, 34 castles, 110 units. |
| **Campaign Progression** | Required manually playing through 30+ stages from scratch. | **Unlocked Roster**: Pre-unlocked campaign save files included in `assets/game/Save/` (Stages 11–19 ready to play). |
| **Dialogue Manual Progression** | Dialogue auto-scrolled and disappeared on timers, rushing the reader. | **Disabled Auto-Progress**: All dialogues wait indefinitely for player confirmation (`Space`, `Enter`, or click); zero auto-advance. |
| **Edge Map Scroll Speed** | Mouse panning at window boundaries scrolled way too fast, causing erratic camera movement. | **Calibrated & Configurable**: Tuned scroll tick divider at `0x42f6e9` from 3 to 50 ($\approx 16.7\times$ slower) with increased edge inception delay ($3 \to 10$ ticks) for precise, steady camera control. Configurable via `scripts/set_scroll_speed.py`. |

---

## ⌨️ Complete Game Controls & Hotkeys Guide

### 1. Tactical Combat Commands & Stances
| Key | Command | Panel Button | Description |
| :---: | :---: | :---: | :--- |
| **`A`** | **Attack** | `ATK` | Order selected regiment to march and engage target enemies |
| **`D`** | **Defend** | `DEF` | Take defensive stance, holding position and repelling attackers |
| **`F`** | **Hold Ground** | `HOLD` | Hold ground strictly; do not break formation or pursue enemies |
| **`S`** | **Stop** | `STOP` | Immediately halt movement and cancel current orders |
| **`V`** | **Patrol** | `PATROL` | Patrol between current location and clicked target position |
| **`Z`** | **Retreat Lightly Wounded** | `L.WND` | Auto-retreat to base tent/castle when company HP drops below 70% |
| **`X`** | **Retreat Heavily Wounded** | `H.WND` | Auto-retreat to base tent/castle when company HP drops below 30% |
| **`C`** | **Fight to the Death** | `STAND` | Stand ground; fight to the last man without retreating |
| **`N`** | **Cycle Formation** | *(Icons)* | Cycle selected company through formation layouts (Line, Wedge, Square, etc.) |

---

### 2. Tactical Side Panel Tabs
| Hotkey | Tab Button | Mode | Description |
| :---: | :---: | :---: | :--- |
| **`Q`** / `F1` | **`[ WAR ]`** | **War / Combat** | Main battle orders panel (`ATK`, `DEF`, `HOLD`, `L.WND`, `H.WND`, `STAND`, `PATROL`, `STOP`). **Use this to return from General Stats!** |
| **`W`** / `F2` | **`[ INT ]`** | **Intel / Stats** | General Intelligence & attributes (portrait, attributes, equipment, skills). **Automatically opened when right-clicking a general.** |
| **`E`** / `F3` | **`[ CMD ]`** | **Command / Admin** | Castle administration, construction (`BUILD`), and transport orders. |
| **`R`** / `F4` | **`[ GRP ]`** | **Group / Roster** | Squad group management and army roster overview. |

> [!TIP]
> **Returning from General Stats**: If you right-click a general to inspect their attributes, simply press **`Q`** (or click the **`[ WAR ]`** tab at the top-right of the tactical box, or left-click any unit) to instantly return to the combat commands!

---

### 3. Squad Selection & Control Groups
| Shortcut | Action | Description |
| :--- | :--- | :--- |
| **`1` – `6`** | **Recall Control Group** | Select squad control group 1 through 6 |
| **`Ctrl + 1` – `6`** | **Assign Control Group** | Bind currently selected companies to squad group 1 through 6 |
| **`Tab`** | **Cycle Selection** | Cycle selection through your active regiments on the battlefield |
| **`,` / `<`** | **Previous Squad** | Select previous squad in roster |
| **`.` / `>`** | **Next Squad** | Select next squad in roster |
| **`B`** | **Cycle Bases / Castles** | Pan camera between owned castles and base tents |
| **`G`** | **Gather / Rally** | Rally scattered regiments together |
| **`T`** | **Lock Target** | Track and lock camera focus onto selected tactical unit |

---

### 4. Camera & Viewport Navigation
| Input | Action | Description |
| :--- | :--- | :--- |
| **`Arrow Keys`** | **Pan Camera** | Scroll camera Up, Down, Left, Right |
| **`Page Up`** / **`Page Down`** | **Diagonal Pan** | Pan camera Up-Right / Down-Right |
| **`Home`** | **Center on Base** | Instantly center camera on your headquarters tent or castle |
| **`End`** | **Diagonal Pan** | Pan camera Down-Left |
| **`Space`** | **Center on Unit** | Center camera viewport on currently selected regiment / commander |
| **Screen Edge Hover** | **Edge Scroll** | Move cursor to window boundary to pan map ($\approx 16.7\times$ calibrated speed) |
| **Minimap Click** | **Minimap Jump** | Left-click anywhere on the diamond minimap to immediately jump camera |
| **`F7`** | **Toggle Grid** | Toggle isometric terrain coordinate grid overlay |
| **`/`** | **Toggle Range** | Toggle combat attack and movement range overlay |

---

### 5. Game Speed & Simulation Controls
| Shortcut | Action | Description |
| :--- | :--- | :--- |
| **`+` / `=`** or **`Numpad +`** | **Increase Speed** | Speed up game simulation (11 levels: Speed 0 up to Speed 10 max) |
| **`-` / `_`** or **`Numpad -`** | **Decrease Speed** | Slow down game simulation (down to Speed 0 slow motion) |
| **`Space`** | **Pause / Resume** | Pause or unpause game simulation (also advances dialogue text when open) |
| **`P`** | **Pause Toggle** | Alternate pause toggle hotkey |

---

### 6. Window, Dialogue & System Hotkeys
| Shortcut | Action | Description |
| :--- | :--- | :--- |
| **`Space` / `Enter` / Click** | **Advance Dialogue** | Progress to next sentence or speaker (auto-progression is disabled) |
| **`Alt + Enter`** | **Toggle Fullscreen** | Instant seamless toggle between 800x600 window and borderless 4K fullscreen |
| **`Esc`** | **Cancel / Close** | Deselect active company, cancel targeting crosshair, or close open popups |
| **`F9`** | **Quick Save** | Instantly save active game campaign |
| **`F11`** | **Debug / Performance** | Toggle engine frame performance and diagnostic overlay |

---

### 7. Complete Mouse Controls
| Input | Context | Action |
| :--- | :--- | :--- |
| **Left Click** | Unit / General | Select regiment or commander |
| **Left Click** | Ground (Unit selected)| Move / march to clicked destination |
| **Left Click** | Enemy Unit | Order active regiment to attack target |
| **Left Click** | HUD Buttons & Tabs | Issue command, stance, formation, or switch side panel tabs |
| **Left Click** | Minimap | Instantly jump camera to target map quadrant |
| **Left Click** | Dialogue Box | Advance dialogue to next page/speaker |
| **Left Click + Drag** | Battlefield | Rubber-band box-select multiple units / armies simultaneously |
| **Right Click** | General in Troop List | Open **General Stats & Attributes** panel (`INT` tab) |
| **Right Click** | Battlefield | Cancel active targeting order, deselect current company |
| **Right Click** | Menus / Submenus | Dismiss submenu or cancel action |
| **Screen Edge Hover** | Window Borders | Smooth edge-scroll camera in that direction |

#### Fine-Tuning Map Edge Scroll Speed
If you prefer a different panning speed, use `scripts/set_scroll_speed.py`:
```bash
python3 scripts/set_scroll_speed.py [preset|threshold]
```
- `fast` (threshold 16, inception 5): Moderate panning speed.
- `normal` (threshold 25, inception 6): Calm panning.
- `slow` (threshold 35, inception 8): $\approx 12\times$ slower than original.
- `gentle` (**Default**, threshold 50, inception 10): $\approx 16.7\times$ slower than original, very steady & controllable (~1 camera step/sec).
- `crawl` (threshold 70, inception 12): Ultra-slow micro-nudging.
- Custom value: `python3 scripts/set_scroll_speed.py 40 8` (custom threshold and inception delay).

---

### 8. Battlefield Tactical Commands (HUD Visual Layout)
When a general or soldier regiment is selected during combat, the bottom-right tactical panel exposes the following stances and orders:

```
+-----------------------------------------------------------+
|  [ WAR ] (Q)   [ INT ] (W)      [ CMD ] (E)      [ GRP ](R)
+-----------------------------------------------------------+
|  [ ATK ] (A) Attack Enemy      |  [ PATROL ] (V) Engage/Scout 
|  [ DEF ] (D) Defend Position   |  [ STOP ]   (S) Halt Orders  
|  [ HOLD ](F) Hold Ground       |  [ RALLY ]  (G) Regroup Unit 
+--------------------------------+--------------------------+
|  [ L.WND ] (Z) Retreat if Lightly Wounded (Fall back at 70% HP)
|  [ H.WND ] (X) Retreat if Heavily Wounded (Fall back at 30% HP)
|  [ STAND ] (C) Fight to the Death (Never retreat)             
+-----------------------------------------------------------+
```

---

### City Management & Economy Buttons
Inside castle administration and market interfaces:
| Button | Meaning | Action |
| :--- | :--- | :--- |
| **`BUILD`** | Construction / 建設 | Upgrade city defenses, walls, and production facilities |
| **`TRANS`** | Transport / 輸送 | Send supplies, gold, and provisions to allied forts |
| **`TRADE`** | Commerce / 商業 | Open trade routes with neighboring merchants |
| **`ITEMS`** | Inventory / 道具 | Equip weapons, armor, relics, and steed saddles to commanders |
| **`BUY`** | Market Purchase / 購買 | Purchase food, iron, weapons, or horses |
| **`SELL`** | Market Sale / 賣出 | Sell excess goods to balance treasury funds |

---

## 🌐 Language Switching & Dual-Boot System

The game supports instantaneous, 100% loss-free switching between **Authentic English** and **Traditional Chinese (Original 1999)**.

### Switch to English
```bash
./switch_language.sh en
# Or launch directly:
./run_native.sh --lang en
```
- Activates `Hero.exe.en` with 12px ASCII character spacing, 34/24 line wraps, and 57 localized multiplayer setup strings.
- Deploys English menu bitmaps (`*_en.bmp`), multiplayer signboards (`netmenu00_en.bmp`–`netmenu03_en.bmp`), English hover states (`selects_en.dat`), multiplayer button sprites (`netgraphics_en.dat`), and English tactical HUD sprites (`windows_en.dat`).
- Loads English generals database (`stage_en.ini`) and English campaign rosters (`Save_en/`).
- Loads full English chronicle scripts and biographies (`text_en/*.txt`).

### Switch to Traditional Chinese
```bash
./switch_language.sh zh
# Or launch directly:
./run_native.sh --lang zh
```
- Restores original untouched binary `Hero.exe.zh` (24px double-byte spacing).
- Restores original Traditional Chinese bitmaps, multiplayer menus, `selects_zh.dat`, `netgraphics_zh.dat`, `windows_zh.dat`, and `stage_zh.ini`.
- Restores original Big5 campaign rosters (`Save_zh/`) and Chinese texts (`text_zh/*.txt`).

---

## 🔬 Technical Reverse Engineering Documentation

For a comprehensive deep dive into the disassembled PE opcodes, memory layouts, bounds-guard code caves, variable ASCII font kerning arithmetic, and proprietary binary file formats, see:

👉 **[REVERSE_ENGINEERING.md](REVERSE_ENGINEERING.md)**

---

## 📁 Directory Structure

```
genghis-khan-desert-heroes/
├── README.md                      # Comprehensive user guide & hotkeys manual
├── REVERSE_ENGINEERING.md         # Technical reverse engineering documentation
├── setup.sh                       # One-click Linux environment installer & desktop shortcut
├── run_native.sh                  # Turnkey native game launcher (--lang en | --lang zh)
├── switch_language.sh             # Instant bilingual asset & binary switcher (Linux)
├── Launch_Game_Win.bat            # One-click Windows 10/11 launcher
├── Switch_Language_Win.bat        # Interactive Windows bilingual switcher
├── Dockerfile                     # Isolated container runtime
│
├── assets/
│   ├── icon.png                   # High-resolution application icon
│   ├── HeroIcon.ico               # Original game executable icon
│   ├── music/                     # High-quality CD audio soundtrack (14 tracks)
│   ├── fonts/                     # Font files for UI rasterization
│   └── game/                      # Complete standalone game root
│       ├── Hero.exe               # Active game binary (swapped between .en and .zh)
│       ├── Hero.exe.en            # Patched 12px ASCII engine & localized multiplayer binary
│       ├── Hero.exe.zh            # Original 1999 binary (DRM-bypassed, bounds-guarded)
│       ├── ddraw.dll / ddraw.ini  # High-resolution hardware DirectDraw wrapper & 60 FPS pacing
│       ├── windows.dat            # Active HUD, button sprites, and interface panels
│       ├── selects.dat            # Active menu button hover highlight sprites
│       ├── netgraphics.dat        # Active multiplayer button sprites
│       ├── netmenu00-03.bmp       # Active multiplayer menu and lobby bitmaps
│       ├── stage.ini              # Active general, castle, and soldier database
│       ├── record.sav             # Active campaign victory records & unlocked stages
│       │
│       ├── Save/                  # Active player save files (Stages 11-19 pre-unlocked)
│       ├── Save_en/               # English-localized general roster saves
│       ├── Save_zh/               # Original Traditional Chinese general roster saves
│       │
│       ├── text_en/               # Complete English translation text database
│       ├── text_zh/               # Original Traditional Chinese text database
│       └── wav/                   # DirectSound 16-bit PCM sound effects
│
└── scripts/                       # Engine tools & speed calibration
    ├── focus_window.py            # Linux window foreground manager
    └── set_scroll_speed.py        # Interactive map edge scroll speed tuner
```

---

## ⚖️ Disclaimer & Notice-and-Takedown

* This release is a **free, non-commercial community preservation and compatibility project** for the classic 2001/1999 video game *成吉思汗之大漠英雄傳* (*Genghis Khan: Desert Heroes*).
* All copyrights, trademarks, and intellectual property remain the property of their respective original owners. No revenue, donations, ads, or paywalls are associated with this project.
* **Takedown Policy**: If you are a copyright holder or successor entity and wish for any material or download links to be removed, please contact `wzli.dev@gmail.com` and we will immediately take down the requested links upon notice.

---

## ❓ Troubleshooting & FAQs

### Q1: The game launches, but I don't hear background music (BGM).
**Answer**:
The game plays background music via MIDI. Ensure TiMidity++ or a software MIDI synthesizer is running:
- **Ubuntu/Debian**: `sudo apt install timidity freepats && timidity -iA -B2,8 -Os &`
- **Arch**: `sudo pacman -S timidity++ && systemctl --user start timidity`
- Sound effects (WAV) work out-of-the-box via DirectSound without extra configuration.

### Q2: How do I play in true Fullscreen?
**Answer**:
Press **`Alt + Enter`** at any time while the game is running to toggle between the 800x600 bordered window and borderless fullscreen. Your monitor's 4:3 aspect ratio is preserved without horizontal stretching.

### Q3: How do I adjust window resolution or shaders?
**Answer**:
You can edit `assets/game/ddraw.ini` directly:
- `renderer=gdi` (fastest, maximum compatibility) or `renderer=opengl` (supports GPU shaders).
- `windowed=true` or `fullscreen=true`.
- `filter=linear` or `filter=point` (crisp pixel art).

### Q4: Can I run this on a Steam Deck?
**Answer**:
Yes! In Desktop Mode on Steam Deck:
1. Run `./setup.sh` (installs `org.winehq.Wine` via Flatpak).
2. Add `run_native.sh` as a **Non-Steam Game** in the Steam client.
3. Switch back to Gaming Mode and launch with full controller and trackpad support.

### Q5: How is display flashing prevented on multi-monitor and 4K setups?
**Answer**:
Older DirectDraw applications attempt to probe hardware display modes or switch physical CRTC modes on launch, which can reset monitor refresh rates or cause momentary black screens on high-refresh/multi-monitor setups. This release solves this cleanly by:
1. Enforcing non-exclusive borderless mode (`toggle_borderless=true` and `nonexclusive=true`) in `assets/game/ddraw.ini` so DirectDraw operates as a standard desktop surface.
2. Utilizing the hardware OpenGL backend, which stretches the 800x600 canvas seamlessly to your native monitor resolution (including 4K 3840x2160) without renegotiating physical display modes.

### Q6: Why was the mouse lagging or sluggish in the start menu?
**Answer**:
Older DirectDraw wrappers sometimes enable software cursor coordinate scaling and interpolation (`adjmouse=true`), which adds latency behind physical cursor input on high-DPI displays. Furthermore, repeated launches under containerized Wine (Flatpak) can leave orphan processes competing for X11 events.
This has been completely eliminated:
1. `assets/game/ddraw.ini` has `adjmouse=false` configured across all sections, passing mouse inputs 1:1 directly to the hardware.
2. Frame pacing is locked at `maxfps=60` and `minfps=60`.
3. `./run_native.sh` automatically performs comprehensive process cleanup (`flatpak kill` and `pkill -9`) on every startup.

### Q7: Are the multiplayer menus and network modes localized?
**Answer**:
Yes! All multiplayer interfaces are fully translated:
- **Signboard & Lobby Bitmaps**: All four multiplayer backgrounds (`netmenu00` through `netmenu03`) feature golden serif headers (*Multiplayer Mode*, *LAN Game*, *Scenario Settings*, *Select Ruler*) and translated button plates (*LAN Game*, *Internet Game*, *Main Menu*, *Host Game*, *Join Game*, *Cancel*, *Confirm*).
- **Hover Highlights**: Dynamic hover sprites in `selects.dat` (sprites 24–26) glow in royal blue with crisp English lettering when the mouse moves over them.
- **Button Sprites**: All multiplayer action buttons in `netgraphics.dat` (*Start Game*, *Host Game*, *Join Game*, *Confirm*, *Cancel*) are translated with both normal and depressed states.
- **Lobby Configuration Strings**: Over 50 setup strings in `Hero.exe.en` (*Host Name*, *Player Name*, *Speed*, *Resource*, *Scenario*, *Diff.*, *None*, *AI*, *Ready!*) are localized.
- Both English and Traditional Chinese modes are switched seamlessly using `./switch_language.sh en` or `./switch_language.sh zh`.

