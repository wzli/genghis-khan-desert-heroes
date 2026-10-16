#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate localized stage_en.ini for OpenCJSH / Hero.exe.
Translates all internal binary game records:
- Section 1: Generals (396 records)
- Section 2: Castles (34 records)
- Section 3: Soldiers / Units (110 records)
- Section 4: Magic Spells (24 records)
- Section 5: Items (59 records)
"""

import os
import struct

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
GAME_DIR = os.path.join(BASE_DIR, 'assets', 'game')

def main():
    src_ini = os.path.join(GAME_DIR, 'stage_zh.ini')
    if not os.path.exists(src_ini):
        src_ini = os.path.join(GAME_DIR, 'stage.ini')
    
    with open(src_ini, 'rb') as f:
        data = bytearray(f.read())
    
    # Load English texts
    with open(os.path.join(GAME_DIR, 'text_en', 'general.txt'), 'r', encoding='latin1') as f:
        en_gens = [l.split('\t')[0].strip() for l in f.readlines()[1:]]

    with open(os.path.join(GAME_DIR, 'text_en', 'castle.txt'), 'r', encoding='latin1') as f:
        en_castles = [l.split('\t')[0].strip() for l in f.readlines()[1:]]

    with open(os.path.join(GAME_DIR, 'text_en', 'soldier.txt'), 'r', encoding='latin1') as f:
        en_soldiers = [l.split('\t')[0].strip() for l in f.readlines()[1:]]

    with open(os.path.join(GAME_DIR, 'text_en', 'magic.txt'), 'r', encoding='latin1') as f:
        en_magics = [l.split('\t')[0].strip() for l in f.readlines()[1:]]

    with open(os.path.join(GAME_DIR, 'text_en', 'Item.txt'), 'r', encoding='latin1') as f:
        en_items = [l.split('\t')[0].strip() for l in f.readlines()[1:]]

    def pad_name(name, max_len=20):
        if len(name) >= max_len:
            name = name[:max_len-1]
        raw = name.encode('latin1')
        return raw + b'\x00' * (max_len - len(raw))

    # Sec 1: Generals (396)
    for i in range(396):
        off = 4 + i * 268 + 4
        name = en_gens[i]
        if name == 'Michael of Chernigov': name = 'M. of Chernigov'
        if name == 'Albert of Buxhoeveden': name = 'Albert Buxhoev.'
        data[off:off+20] = pad_name(name)

    # Sec 2: Castles (34)
    for i in range(34):
        off = 106132 + 4 + i * 144 + 8
        name = en_castles[i]
        data[off:off+20] = pad_name(name)

    # Sec 3: Soldiers (110)
    for i in range(110):
        off = 0x1b1b8 + 4 + i * 92 + 4
        name = en_soldiers[i]
        data[off:off+20] = pad_name(name)

    # Sec 4: Magics (24)
    for i in range(24):
        off = 0x1d944 + 4 + i * 76 + 4
        name = en_magics[i]
        data[off:off+20] = pad_name(name)

    # Sec 5: Items (59)
    for i in range(59):
        off = 0x1e068 + 4 + i * 72 + 4
        name = en_items[i]
        data[off:off+20] = pad_name(name)

    assert len(data) == 127240, f"Size changed: {len(data)} != 127240"
    
    out_ini = os.path.join(GAME_DIR, 'stage_en.ini')
    with open(out_ini, 'wb') as f:
        f.write(data)
    print(f"[SUCCESS] Wrote localized stage_en.ini ({len(data)} bytes).")

if __name__ == '__main__':
    main()
