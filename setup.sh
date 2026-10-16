#!/bin/bash
set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR"

echo "=================================================================="
echo " 成吉思汗之大漠英雄傳 (Genghis Khan 1999) - System Setup & Installer"
echo "=================================================================="

# 0. Check for game assets (if cloned via git without heavy binaries)
if [ ! -f "$DIR/assets/game/Hero.exe" ] && [ ! -f "$DIR/assets/game/Hero.exe.en" ]; then
    echo "=================================================================="
    echo " [INFO] Game binary and media assets not found in assets/game/."
    echo " [INFO] Downloading pre-packaged game release (284 MB)..."
    echo "=================================================================="
    
    DL_URL="https://github.com/wzli/genghis-khan-desert-heroes/releases/download/v1.0/Genghis_Khan_Desert_Heroes_v1.0_Bilingual.7z"
    DL_BACKUP="https://archive.org/download/genghis-khan-desert-heroes-1999-native/Genghis_Khan_Desert_Heroes_v1.0_Bilingual.7z"
    DL_CHINA="https://ghfast.top/https://github.com/wzli/genghis-khan-desert-heroes/releases/download/v1.0/Genghis_Khan_Desert_Heroes_v1.0_Bilingual.7z"
    
    TMP_7Z="/tmp/Genghis_Khan_Release.7z"
    TMP_DIR="/tmp/Genghis_Khan_Extract_$$"
    
    if ! command -v 7z &>/dev/null && ! command -v 7za &>/dev/null; then
        echo "[INFO] 7z is required to extract game assets. Installing p7zip..."
        if command -v apt-get &>/dev/null; then
            sudo apt-get update && sudo apt-get install -y p7zip-full || true
        elif command -v dnf &>/dev/null; then
            sudo dnf install -y p7zip p7zip-plugins || true
        elif command -v pacman &>/dev/null; then
            sudo pacman -S --needed p7zip || true
        fi
    fi
    
    echo "[INFO] Fetching archive..."
    if command -v curl &>/dev/null; then
        curl -L --fail --progress-bar -o "$TMP_7Z" "$DL_URL" || \
        curl -L --fail --progress-bar -o "$TMP_7Z" "$DL_CHINA" || \
        curl -L --fail --progress-bar -o "$TMP_7Z" "$DL_BACKUP"
    elif command -v wget &>/dev/null; then
        wget -O "$TMP_7Z" "$DL_URL" || \
        wget -O "$TMP_7Z" "$DL_CHINA" || \
        wget -O "$TMP_7Z" "$DL_BACKUP"
    else
        echo "[ERROR] Neither curl nor wget found. Please download $DL_URL manually."
        exit 1
    fi
    
    echo "[INFO] Extracting assets..."
    SEVENZIP_CMD="7z"
    command -v 7z &>/dev/null || SEVENZIP_CMD="7za"
    "$SEVENZIP_CMD" x "$TMP_7Z" -o"$TMP_DIR" -y > /dev/null
    
    mkdir -p "$DIR/assets"
    cp -rn "$TMP_DIR"/Genghis_Khan_Desert_Heroes/assets/* "$DIR/assets/" 2>/dev/null || true
    rm -rf "$TMP_DIR" "$TMP_7Z"
    echo "[OK] Game assets successfully installed!"
fi

# 1. Detect Wine runtime
HAS_WINE=false
HAS_FLATPAK_WINE=false

if command -v wine &>/dev/null; then
    HAS_WINE=true
    echo "[OK] System Wine found: $(wine --version 2>&1 | head -n 1)"
elif command -v flatpak &>/dev/null && flatpak info org.winehq.Wine &>/dev/null; then
    HAS_FLATPAK_WINE=true
    echo "[OK] Flatpak Wine runtime found (org.winehq.Wine)"
fi

if [ "$HAS_WINE" = false ] && [ "$HAS_FLATPAK_WINE" = false ]; then
    echo "[INFO] No Wine runtime detected. Attempting automatic setup..."
    if command -v flatpak &>/dev/null; then
        echo "[INFO] Installing org.winehq.Wine via Flatpak (Flathub)..."
        flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo || true
        flatpak install --user -y flathub org.winehq.Wine
        HAS_FLATPAK_WINE=true
    elif command -v apt-get &>/dev/null; then
        echo "[INFO] Debian/Ubuntu detected. To install Wine, run:"
        echo "  sudo dpkg --add-architecture i386 && sudo apt-get update && sudo apt-get install -y wine32 wine64"
    elif command -v dnf &>/dev/null; then
        echo "[INFO] Fedora/RHEL detected. To install Wine, run:"
        echo "  sudo dnf install -y wine"
    elif command -v pacman &>/dev/null; then
        echo "[INFO] Arch Linux detected. To install Wine, run:"
        echo "  sudo pacman -S --needed wine"
    fi
fi

# 2. Check for Timidity MIDI (for BGM music)
if command -v timidity &>/dev/null; then
    echo "[OK] TiMidity++ MIDI synthesizer found."
else
    echo "[INFO] Note: TiMidity++ is recommended for background MIDI music playback."
fi

# 3. Generate Desktop Launcher
DESKTOP_DIR="$HOME/Desktop"
APP_DIR="$HOME/.local/share/applications"
mkdir -p "$APP_DIR"

DESKTOP_FILE_CONTENT="[Desktop Entry]
Version=1.0
Type=Application
Name=成吉思汗之大漠英雄傳 (Genghis Khan: Desert Heroes)
Comment=Turnkey Linux Edition of Genghis Khan with Authentic English & Chinese Modes
Exec=$DIR/run_native.sh
Icon=$DIR/assets/icon.png
Path=$DIR
Terminal=false
StartupNotify=true
Categories=Game;StrategyGame;"

echo "$DESKTOP_FILE_CONTENT" > "$APP_DIR/opencjsh.desktop"
chmod +x "$APP_DIR/opencjsh.desktop"

if [ -d "$DESKTOP_DIR" ]; then
    echo "$DESKTOP_FILE_CONTENT" > "$DESKTOP_DIR/成吉思汗之大漠英雄傳.desktop"
    chmod +x "$DESKTOP_DIR/成吉思汗之大漠英雄傳.desktop"
    echo "[OK] Desktop shortcut created at: $DESKTOP_DIR/成吉思汗之大漠英雄傳.desktop"
fi

# 4. Fix permissions on helper scripts
chmod +x run_native.sh switch_language.sh scripts/*.py Launch_Game_Win.bat Switch_Language_Win.bat 2>/dev/null || true
ln -sfn run_native.sh run_opencjsh.sh

echo "=================================================================="
echo " [SUCCESS] Setup complete!"
echo " Launch the game using:"
echo "   ./run_native.sh --lang en   # Authentic English"
echo "   ./run_native.sh --lang zh   # Traditional Chinese (Original)"
echo " Or double-click the shortcut on your desktop."
echo "=================================================================="
