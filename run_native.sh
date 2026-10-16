#!/bin/bash
set -e
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GAME_DIR="$DIR/assets/game"

SELECTED_LANG=""
REMAINING_ARGS=()

# Parse arguments
while [[ $# -gt 0 ]]; do
    case "$1" in
        --help|-h|help)
            echo "成吉思汗之大漠英雄傳 (Genghis Khan 1999) - Turnkey Native Launcher"
            echo ""
            echo "Usage: $0 [OPTIONS]"
            echo ""
            echo "Options:"
            echo "  --lang en, -l en    Launch game in English"
            echo "  --lang zh, -l zh    Launch game in Traditional Chinese (Original)"
            echo "  --help, -h          Show this help message"
            echo ""
            echo "Window Controls:"
            echo "  Alt + Enter         Toggle Windowed / Borderless Fullscreen"
            exit 0
            ;;
        --lang|-l)
            SELECTED_LANG="$2"
            shift 2
            ;;
        --lang=*)
            SELECTED_LANG="${1#*=}"
            shift
            ;;
        *)
            echo "Note: Ignoring unrecognized option '$1'. Run with --help for options."
            shift
            ;;
    esac
done

# Clean up any stale instances before launching
flatpak kill org.winehq.Wine 2>/dev/null || true
pkill -9 -x "Hero.exe" 2>/dev/null || true
pkill -9 -f "org.winehq.Wine" 2>/dev/null || true
sleep 0.5

# Ensure game assets exist, or run setup.sh automatically
if [ ! -f "$GAME_DIR/Hero.exe" ] && [ ! -f "$GAME_DIR/Hero.exe.en" ]; then
    echo "[INFO] Game assets not found. Launching setup.sh to download..."
    "$DIR/setup.sh"
fi

# If language specified, apply it; otherwise default to English on first run
if [ -n "$SELECTED_LANG" ]; then
    "$DIR/switch_language.sh" "$SELECTED_LANG"
elif [ ! -f "$GAME_DIR/.current_language" ]; then
    "$DIR/switch_language.sh" "en"
fi

# Detect current language setting
CUR_LANG="English"
if [ -f "$GAME_DIR/.current_language" ]; then
    CUR_LANG="$(cat "$GAME_DIR/.current_language")"
fi

# Set C.UTF-8 for the shell script runner
export LC_ALL="C.UTF-8"
export LANG="C.UTF-8"

# Wine inside Flatpak uses compiled zh_TW.UTF-8 (Big5 codepage 950)
WINE_LOCPATH="${WINE_LOCPATH:-$HOME/.var/app/org.winehq.Wine/data/locale}"
WINE_LC_ALL="zh_TW.UTF-8"
WINE_LANG="zh_TW.UTF-8"

export WINEDLLOVERRIDES="ddraw=n,b;winmm=n,b"
export WINEDEBUG="-all"

cd "$GAME_DIR"

echo "=========================================================="
echo " Starting 成吉思汗之大漠英雄傳 (Genghis Khan 1999)"
echo " Language: $CUR_LANG"
echo " Window Mode: 800x600 Windowed with Borders (Press Alt+Enter for Fullscreen)"
echo " DirectDraw Engine: cnc-ddraw (OpenGL renderer)"
echo "=========================================================="

# Launch background window raiser so the game appears in the foreground
if [ -f "$DIR/scripts/focus_window.py" ]; then
    python3 "$DIR/scripts/focus_window.py" &
fi

# Determine Wine invocation method
if command -v wine &>/dev/null; then
    exec wine Hero.exe
elif command -v flatpak &>/dev/null && flatpak info org.winehq.Wine &>/dev/null; then
    exec flatpak run --env=WINEDLLOVERRIDES="ddraw=n,b;winmm=n,b" \
                     --env=LOCPATH="$WINE_LOCPATH" \
                     --env=LC_ALL="$WINE_LC_ALL" \
                     --env=LANG="$WINE_LANG" \
                     --env=WINEDEBUG="-all" \
                     org.winehq.Wine Hero.exe
else
    echo "Error: Wine is not installed. Please install wine or flatpak org.winehq.Wine."
    exit 1
fi
