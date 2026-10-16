# Title: Running a 2001 DirectDraw Windows 98 RTS Natively on Linux & Steam Deck in 4K: Genghis Khan: Desert Heroes (成吉思汗之大漠英雄傳) Turnkey Release

Hey r/linux_gaming,

Classic late-90s / early-2000s Asian PC RTS games are notorious for DirectDraw quirks, Big-5 codepage dependencies, and aggressive CD copy-protection checks that frequently break on modern Wine without deep manual tweaking.

We took *Genghis Khan: Desert Heroes* (成吉思汗之大漠英雄傳, 2001/1999), a rare historical RTS from Taiwan that was previously only playable on Linux through an 8GB Windows 98 disk image in DOSBox-X, and reverse-engineered it to run natively, smoothly, and cleanly on modern Linux and Steam Deck.

### The Technical Fixes under Linux & Wine:
1. **Zero Display Flashing & XRandR Lockups**:
   - Vintage DirectDraw games under Wine probe fullscreen video modes using XRandR, which can flicker or blank external monitors.
   - We paired `cnc-ddraw` with OpenGL hardware rendering (`renderer=opengl`), enforcing `nonexclusive=true` and `toggle_borderless=true`. This allows integer 4K upscaling (4:3 aspect lock) and instant `Alt + Enter` borderless windowed switching with zero monitor blinking.
2. **Zero Mouse Latency**:
   - Disabled DirectDraw synthetic cursor polling (`adjmouse=false`) and configured 60 FPS frame pacing.
3. **Big-5 vs UTF-8 Codepage Translation**:
   - The engine relies on Big-5 encoding (Code Page 950). Our turnkey `./run_native.sh` launcher auto-detects system Wine or Flatpak Wine (`org.winehq.Wine`), configuring `zh_TW.UTF-8` and `WINEDLLOVERRIDES="ddraw=n,b;winmm=n,b"` automatically.
4. **Binary Crash Fixes**:
   - Decompiled the binary in x86 disassembly and fixed an unhandled page fault at `0x420bd5` (`testb $1, 0xf(%edx)`) caused by unverified tile hit indices during pause states by detouring execution through a safe bounds-check code cave at `0x47f480`.
5. **English Font Kerning Patch**:
   - The original text rendering engine had a hardcoded $24\text{px}$ step multiplier (`lea ecx, [base_x + col*24]`) for Chinese characters, making English letters look like `M o t h e r`. We patched `0x46ce12` to $12\text{px}$ ASCII spacing and doubled the line wrap buffer limits, completing a full bilingual translation.

### How to Run on Linux / SteamOS:
```bash
# 1. Clone repository
git clone https://github.com/wzli/genghis-khan-desert-heroes.git
cd genghis-khan-desert-heroes

# 2. Download the 284 MB game package from GitHub Releases or Archive.org
# Extract it into the directory

# 3. Setup and Launch
./setup.sh
./run_native.sh --lang en   # English
./run_native.sh --lang zh   # Traditional Chinese (Original)
```

GitHub Repo with complete disassembly write-up:
https://github.com/wzli/genghis-khan-desert-heroes
