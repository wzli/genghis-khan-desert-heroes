#!/bin/bash
set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GAME_DIR="$DIR/assets/game"
ZH_DIR="$GAME_DIR/text_zh"
EN_DIR="$GAME_DIR/text_en"

LANG_CHOICE="${1:-}"

if [ -z "$LANG_CHOICE" ]; then
    echo "Usage: $0 [en|zh]"
    echo "  en - Switch game text to Authentic English"
    echo "  zh - Switch game text to Authentic Traditional Chinese (Original)"
    exit 1
fi

case "$LANG_CHOICE" in
    en|EN|eng|ENG|english|English)
        echo "Switching game language to English..."
        cp "$EN_DIR"/*.txt "$GAME_DIR"/
        if [ -f "$GAME_DIR/Hero.exe.en" ]; then
            cp "$GAME_DIR/Hero.exe.en" "$GAME_DIR/Hero.exe"
        fi
        for menu in mainmenu single story stage act_bg netmenu00 netmenu01 netmenu02 netmenu03; do
            if [ -f "$GAME_DIR/${menu}_en.bmp" ]; then
                cp "$GAME_DIR/${menu}_en.bmp" "$GAME_DIR/${menu}.bmp"
            fi
        done
        if [ -f "$GAME_DIR/selects_en.dat" ]; then
            cp "$GAME_DIR/selects_en.dat" "$GAME_DIR/selects.dat"
        fi
        if [ -f "$GAME_DIR/windows_en.dat" ]; then
            cp "$GAME_DIR/windows_en.dat" "$GAME_DIR/windows.dat"
        fi
        if [ -f "$GAME_DIR/netGraphics_en.dat" ]; then
            cp "$GAME_DIR/netGraphics_en.dat" "$GAME_DIR/netGraphics.dat"
            cp "$GAME_DIR/netGraphics_en.dat" "$GAME_DIR/netgraphics.dat"
        fi
        if [ -f "$GAME_DIR/stage_en.ini" ]; then
            cp "$GAME_DIR/stage_en.ini" "$GAME_DIR/stage.ini"
        fi
        for f in "$GAME_DIR"/stage*_en.spr; do
            [ -e "$f" ] || continue
            base="$(basename "$f" _en.spr)"
            cp "$f" "$GAME_DIR/${base}.spr"
        done
        for f in "$GAME_DIR"/stage*_en.stg; do
            [ -e "$f" ] || continue
            base="$(basename "$f" _en.stg)"
            cp "$f" "$GAME_DIR/${base}.stg"
        done
        if [ -d "$GAME_DIR/Save_en" ]; then
            mkdir -p "$GAME_DIR/Save"
            cp "$GAME_DIR/Save_en"/* "$GAME_DIR/Save/" 2>/dev/null || true
        fi
        echo "English" > "$GAME_DIR/.current_language"
        echo "[SUCCESS] Game text and menu UI switched to Authentic English!"
        ;;
    zh|ZH|ch|CH|cn|CN|chs|CHS|cht|CHT|chinese|Chinese|tw|TW|tc|TC)
        echo "Switching game language to Traditional Chinese..."
        cp "$ZH_DIR"/*.txt "$GAME_DIR"/
        if [ -f "$GAME_DIR/Hero.exe.zh" ]; then
            cp "$GAME_DIR/Hero.exe.zh" "$GAME_DIR/Hero.exe"
        fi
        for menu in mainmenu single story stage act_bg netmenu00 netmenu01 netmenu02 netmenu03; do
            if [ -f "$GAME_DIR/${menu}_zh.bmp" ]; then
                cp "$GAME_DIR/${menu}_zh.bmp" "$GAME_DIR/${menu}.bmp"
            fi
        done
        if [ -f "$GAME_DIR/selects_zh.dat" ]; then
            cp "$GAME_DIR/selects_zh.dat" "$GAME_DIR/selects.dat"
        fi
        if [ -f "$GAME_DIR/windows_zh.dat" ]; then
            cp "$GAME_DIR/windows_zh.dat" "$GAME_DIR/windows.dat"
        fi
        if [ -f "$GAME_DIR/netGraphics_zh.dat" ]; then
            cp "$GAME_DIR/netGraphics_zh.dat" "$GAME_DIR/netGraphics.dat"
            cp "$GAME_DIR/netGraphics_zh.dat" "$GAME_DIR/netgraphics.dat"
        fi
        if [ -f "$GAME_DIR/stage_zh.ini" ]; then
            cp "$GAME_DIR/stage_zh.ini" "$GAME_DIR/stage.ini"
        fi
        for f in "$GAME_DIR"/stage*_zh.spr; do
            [ -e "$f" ] || continue
            base="$(basename "$f" _zh.spr)"
            cp "$f" "$GAME_DIR/${base}.spr"
        done
        for f in "$GAME_DIR"/stage*_zh.stg; do
            [ -e "$f" ] || continue
            base="$(basename "$f" _zh.stg)"
            cp "$f" "$GAME_DIR/${base}.stg"
        done
        if [ -d "$GAME_DIR/Save_zh" ]; then
            mkdir -p "$GAME_DIR/Save"
            cp "$GAME_DIR/Save_zh"/* "$GAME_DIR/Save/" 2>/dev/null || true
        fi
        echo "Chinese" > "$GAME_DIR/.current_language"
        echo "[SUCCESS] Game text and menu UI switched to Traditional Chinese (Original)!"
        ;;
    *)
        echo "Error: Unknown language '$LANG_CHOICE'. Choose 'en' or 'zh'."
        exit 1
        ;;
esac
