#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate localized windows_en.dat for OpenCJSH / Hero.exe.
Translates all in-game HUD and window button bitmaps and background panels:
- Save Menu (31..42): Save Game, Load Game, Objectives, Restart, Main Menu, Exit Game
- City/Build (65..72): BUILD, TRANS, TRADE, ITEMS
- Market/Trade (123..126): BUY, SELL
- Tactical Stance (161..168): HOLD, L.WND, H.WND, STAND
- Tactical Action (169..174): PATROL, RALLY, STOP
- Confirmation Small (207..210): CONFIRM, CANCEL
- Confirmation Large (224..227): CONFIRM, CANCEL
- Difficulty (241..246): EASY, NORMAL, HARD
- Tactical Rally (322, 323): RALLY
- Restart Game (334, 335): RESTART
- Tactical Battlefield HUD Panel (175 & 177): ATK, DEF, HOLD, L.WND, H.WND, STAND, PATROL, STOP, WAR, INT, CMD, GRP
- System Menu Panel (49): SYSTEM, Save/Load/Objectives/Restart/Menu/Exit, Subtitles, Speed
- Diplomacy Panel (28): DIPLOMACY
- Empty City Panel (317): EMPTY
"""

import os
import struct
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
GAME_DIR = os.path.join(BASE_DIR, 'assets', 'game')
FONT_SANS = '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'

def main():
    src_dat = os.path.join(GAME_DIR, 'windows_zh.dat')
    if not os.path.exists(src_dat):
        src_dat = os.path.join(GAME_DIR, 'windows.dat')
        
    with open(src_dat, 'rb') as f:
        data = bytearray(f.read())
        
    num_sprites = 350
    offsets = struct.unpack(f'<{num_sprites}I', data[:num_sprites*4])

    with open(os.path.join(GAME_DIR, 'mainmenu_en.bmp'), 'rb') as f:
        bmp_pal = f.read()[54:54+1024]
    pal = []
    for i in range(256):
        pal.extend([bmp_pal[i*4+2], bmp_pal[i*4+1], bmp_pal[i*4]])

    pal_img = Image.new('P', (1, 1))
    pal_img.putpalette(pal)

    def get_sprite(idx):
        off = offsets[idx]
        w, h = struct.unpack('<HH', data[off:off+4])
        pix = data[off+4:off+4+w*h]
        im = Image.frombytes('P', (w, h), pix)
        im.putpalette(pal)
        return im, w, h, off

    def patch_button(idx, text, is_active=False, font_size=10, bx=2, by=2, text_rgb=None, shadow_rgb=None, bg_idx=None, y_offset=0):
        off = offsets[idx]
        w, h = struct.unpack('<HH', data[off:off+4])
        pixels = list(data[off+4:off+4+w*h])
        
        if bg_idx is None:
            from collections import Counter
            c = Counter(pixels)
            bg_idx = c.most_common(1)[0][0]
        
        # Fill interior
        for y in range(by, h - by):
            for x in range(bx, w - bx):
                pixels[y * w + x] = bg_idx
                
        img = Image.frombytes('P', (w, h), bytes(pixels))
        img.putpalette(pal)
        rgb = img.convert('RGB')
        draw = ImageDraw.Draw(rgb)
        
        font = ImageFont.truetype(FONT_SANS, font_size)
        bbox = font.getbbox(text)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        tx = (w - tw) // 2 - bbox[0]
        ty = (h - th) // 2 - bbox[1] + y_offset
        
        if shadow_rgb:
            draw.text((tx+1, ty+1), text, font=font, fill=shadow_rgb)
        if text_rgb:
            draw.text((tx, ty), text, font=font, fill=text_rgb)
            
        q = rgb.quantize(palette=pal_img)
        new_pixels = q.tobytes()
        assert len(new_pixels) == w * h
        data[off+4:off+4+w*h] = new_pixels

    # 1. Patch individual button sprites
    all_buttons = [
        # Save Menu (31..42, 119x24)
        (31, 'Save Game', False, 13, 3, 3, (255, 220, 80), (20, 20, 40), 253, 0),
        (32, 'Save Game', True, 13, 3, 3, (255, 255, 255), (20, 40, 60), 252, 0),
        (33, 'Load Game', False, 13, 3, 3, (255, 220, 80), (20, 20, 40), 253, 0),
        (34, 'Load Game', True, 13, 3, 3, (255, 255, 255), (20, 40, 60), 252, 0),
        (35, 'Objectives', False, 13, 3, 3, (255, 220, 80), (20, 20, 40), 253, 0),
        (36, 'Objectives', True, 13, 3, 3, (255, 255, 255), (20, 40, 60), 252, 0),
        (37, 'Restart', False, 13, 3, 3, (255, 220, 80), (20, 20, 40), 253, 0),
        (38, 'Restart', True, 13, 3, 3, (255, 255, 255), (20, 40, 60), 252, 0),
        (39, 'Main Menu', False, 13, 3, 3, (255, 220, 80), (20, 20, 40), 253, 0),
        (40, 'Main Menu', True, 13, 3, 3, (255, 255, 255), (20, 40, 60), 252, 0),
        (41, 'Exit Game', False, 13, 3, 3, (255, 220, 80), (20, 20, 40), 253, 0),
        (42, 'Exit Game', True, 13, 3, 3, (255, 255, 255), (20, 40, 60), 252, 0),
        
        # Build (65..72, 42x21)
        (65, 'BUILD', False, 9, 2, 2, (0, 0, 0), (250, 230, 180), 217, 0),
        (66, 'BUILD', True, 9, 2, 2, (255, 255, 100), (0, 80, 0), 191, 0),
        (67, 'TRANS', False, 9, 2, 2, (0, 0, 0), (250, 230, 180), 217, 0),
        (68, 'TRANS', True, 9, 2, 2, (255, 255, 100), (0, 80, 0), 191, 0),
        (69, 'TRADE', False, 9, 2, 2, (0, 0, 0), (250, 230, 180), 217, 0),
        (70, 'TRADE', True, 9, 2, 2, (255, 255, 100), (0, 80, 0), 191, 0),
        (71, 'ITEMS', False, 9, 2, 2, (0, 0, 0), (250, 230, 180), 217, 0),
        (72, 'ITEMS', True, 9, 2, 2, (255, 255, 100), (0, 80, 0), 191, 0),
        
        # Trade (123..126, 44x23)
        (123, 'BUY', False, 11, 2, 2, (255, 220, 80), (30, 30, 30), 249, 0),
        (124, 'BUY', True, 11, 2, 2, (255, 255, 255), (30, 30, 30), 190, 0),
        (125, 'SELL', False, 11, 2, 2, (255, 220, 80), (30, 30, 30), 249, 0),
        (126, 'SELL', True, 11, 2, 2, (255, 255, 255), (30, 30, 30), 190, 0),
        
        # Tactical Stance (161..168, 32x34)
        (161, 'HOLD', False, 10, 1, 1, (239, 236, 236), (10, 36, 28), 192, 0),
        (162, 'HOLD', True, 10, 1, 1, (215, 232, 184), (10, 36, 28), 194, 0),
        (163, 'L.WND', False, 9, 1, 1, (239, 236, 236), (10, 36, 28), 192, 0),
        (164, 'L.WND', True, 9, 1, 1, (215, 232, 184), (10, 36, 28), 194, 0),
        (165, 'H.WND', False, 9, 1, 1, (239, 236, 236), (10, 36, 28), 192, 0),
        (166, 'H.WND', True, 9, 1, 1, (215, 232, 184), (10, 36, 28), 194, 0),
        (167, 'STAND', False, 9, 1, 1, (239, 236, 236), (10, 36, 28), 192, 0),
        (168, 'STAND', True, 9, 1, 1, (215, 232, 184), (10, 36, 28), 194, 0),
        
        # Tactical Action (169..174, 38x17)
        (169, 'PATROL', False, 8, 1, 1, (255, 255, 255), (40, 40, 40), 247, -1),
        (170, 'PATROL', True, 8, 1, 1, (175, 152, 152), (30, 30, 30), 250, -1),
        (171, 'RALLY', False, 8, 1, 1, (255, 255, 255), (40, 40, 40), 247, -1),
        (172, 'RALLY', True, 8, 1, 1, (175, 152, 152), (30, 30, 30), 250, -1),
        (173, 'STOP', False, 8, 1, 1, (255, 255, 255), (40, 40, 40), 247, -1),
        (174, 'STOP', True, 8, 1, 1, (175, 152, 152), (30, 30, 30), 250, -1),
        
        # Confirm Small (207..210, 65x25)
        (207, 'CONFIRM', False, 10, 2, 2, (0, 0, 0), (250, 230, 180), 167, 0),
        (208, 'CONFIRM', True, 10, 2, 2, (255, 255, 100), (60, 40, 0), 168, 0),
        (209, 'CANCEL', False, 10, 2, 2, (0, 0, 0), (250, 230, 180), 167, 0),
        (210, 'CANCEL', True, 10, 2, 2, (255, 255, 100), (60, 40, 0), 168, 0),
        
        # Confirm Large (224..227, 104x32)
        (224, 'CONFIRM', False, 14, 3, 3, (0, 0, 0), (250, 230, 180), 221, 0),
        (225, 'CONFIRM', True, 14, 3, 3, (255, 255, 100), (0, 80, 0), 221, 0),
        (226, 'CANCEL', False, 14, 3, 3, (0, 0, 0), (250, 230, 180), 221, 0),
        (227, 'CANCEL', True, 14, 3, 3, (120, 100, 70), (40, 30, 20), 221, 0),
        
        # Difficulty (241..246, 51x24)
        (241, 'EASY', False, 11, 2, 2, (0, 0, 0), (250, 230, 180), 125, 0),
        (244, 'EASY', True, 11, 2, 2, (255, 255, 100), (40, 40, 0), 252, 0),
        (242, 'NORMAL', False, 10, 2, 2, (0, 0, 0), (250, 230, 180), 125, 0),
        (245, 'NORMAL', True, 10, 2, 2, (255, 255, 100), (40, 40, 0), 252, 0),
        (243, 'HARD', False, 11, 2, 2, (0, 0, 0), (250, 230, 180), 125, 0),
        (246, 'HARD', True, 11, 2, 2, (255, 255, 100), (40, 40, 0), 252, 0),
        
        # Rally (322, 323, 40x19)
        (322, 'RALLY', False, 9, 1, 1, (0, 0, 0), (250, 230, 180), 169, 0),
        (323, 'RALLY', True, 9, 1, 1, (255, 255, 100), (40, 40, 0), 167, 0),
        
        # Restart (334, 335, 109x37)
        (334, 'RESTART', False, 14, 3, 3, (0, 0, 0), (250, 230, 180), 167, 0),
        (335, 'RESTART', True, 14, 3, 3, (255, 255, 100), (40, 40, 0), 168, 0),
    ]

    for item in all_buttons:
        patch_button(*item)

    # 2. Patch HUD panels (175, 177, 49, 28, 317)
    font_btn = ImageFont.truetype(FONT_SANS, 9)
    font_tab = ImageFont.truetype(FONT_SANS, 10)
    font_act = ImageFont.truetype(FONT_SANS, 8)
    font_scroll = ImageFont.truetype(FONT_SANS, 13)
    font_slider = ImageFont.truetype(FONT_SANS, 9)

    # Panels 175 & 177
    for idx, is_177 in [(175, False), (177, True)]:
        im, w, h, off = get_sprite(idx)
        rgb = im.convert('RGB')
        draw = ImageDraw.Draw(rgb)
        y_base = 76 if is_177 else 340
        
        buttons = [
            (128, y_base, 'ATK'),
            (164, y_base, 'DEF'),
            (200, y_base, 'HOLD'),
            (128, y_base + 40, 'L.WND'),
            (164, y_base + 40, 'H.WND'),
            (200, y_base + 40, 'STAND'),
        ]
        for bx, by, txt in buttons:
            draw.rectangle([bx + 2, by + 2, bx + 32 - 3, by + 34 - 3], fill=(23, 72, 44))
            bbox = font_btn.getbbox(txt)
            tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
            tx = bx + (32 - tw) // 2 - bbox[0]
            ty = by + (34 - th) // 2 - bbox[1]
            draw.text((tx + 1, ty + 1), txt, font=font_btn, fill=(10, 36, 28))
            draw.text((tx, ty), txt, font=font_btn, fill=(239, 236, 236))
            
        act_buttons = [
            (138, y_base + 82, 'PATROL'),
            (188, y_base + 82, 'STOP'),
        ]
        for bx, by, txt in act_buttons:
            draw.rectangle([bx + 1, by + 1, bx + 38 - 2, by + 17 - 2], fill=(139, 132, 144))
            bbox = font_act.getbbox(txt)
            tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
            tx = bx + (38 - tw) // 2 - bbox[0]
            ty = by + (17 - th) // 2 - bbox[1] - 1
            draw.text((tx + 1, ty + 1), txt, font=font_act, fill=(40, 40, 40))
            draw.text((tx, ty), txt, font=font_act, fill=(255, 255, 255))
            
        gy = 8 if is_177 else 272
        draw.rectangle([10, gy, 34, gy + 24], fill=(130, 95, 65))
        bbox = font_tab.getbbox('GRP')
        tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
        draw.text((10 + (24 - tw)//2 - bbox[0], gy + (24 - th)//2 - bbox[1]), 'GRP', font=font_tab, fill=(240, 220, 160))
        
        if not is_177:
            tabs = [(8, 'WAR'), (32, 'INT'), (56, 'CMD')]
            for ty_pos, ttxt in tabs:
                draw.rectangle([210, ty_pos, 232, ty_pos + 22], fill=(230, 200, 140))
                bbox = font_tab.getbbox(ttxt)
                tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
                tx = 210 + (22 - tw)//2 - bbox[0]
                ty = ty_pos + (22 - th)//2 - bbox[1]
                draw.text((tx + 1, ty + 1), ttxt, font=font_tab, fill=(60, 40, 20))
                draw.text((tx, ty), ttxt, font=font_tab, fill=(255, 255, 220))
                
        q = rgb.quantize(palette=pal_img)
        data[off+4:off+4+w*h] = q.tobytes()

    # Panel 49 (System Menu)
    im, w, h, off = get_sprite(49)
    rgb = im.convert('RGB')
    draw = ImageDraw.Draw(rgb)
    draw.rectangle([80, 12, 160, 36], fill=(240, 240, 230))
    bbox = font_scroll.getbbox('SYSTEM')
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text((80 + (80 - tw)//2 - bbox[0], 12 + (24 - th)//2 - bbox[1]), 'SYSTEM', font=font_scroll, fill=(30, 30, 30))

    labels = ['Save Game', 'Load Game', 'Objectives', 'Restart', 'Main Menu', 'Exit Game']
    font_menu = ImageFont.truetype(FONT_SANS, 12)
    for i, lbl in enumerate(labels):
        by = 63 + i * 32
        draw.rectangle([64, by + 3, 178, by + 21], fill=(20, 30, 45))
        bbox = font_menu.getbbox(lbl)
        tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
        tx = 61 + (119 - tw)//2 - bbox[0]
        ty = by + (24 - th)//2 - bbox[1]
        draw.text((tx + 1, ty + 1), lbl, font=font_menu, fill=(10, 15, 25))
        draw.text((tx, ty), lbl, font=font_menu, fill=(255, 220, 80))

    draw.rectangle([30, 380, 75, 405], fill=(130, 95, 65))
    draw.text((32, 386), 'Subtitles', font=font_slider, fill=(240, 220, 160))
    draw.rectangle([30, 425, 75, 450], fill=(130, 95, 65))
    draw.text((32, 430), 'Speed', font=font_slider, fill=(240, 220, 160))
    data[off+4:off+4+w*h] = rgb.quantize(palette=pal_img).tobytes()

    # Panel 28 (Diplomacy)
    im, w, h, off = get_sprite(28)
    rgb = im.convert('RGB')
    draw = ImageDraw.Draw(rgb)
    draw.rectangle([60, 12, 160, 36], fill=(240, 240, 230))
    bbox = font_scroll.getbbox('DIPLOMACY')
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text((60 + (100 - tw)//2 - bbox[0], 12 + (24 - th)//2 - bbox[1]), 'DIPLOMACY', font=font_scroll, fill=(30, 30, 30))
    data[off+4:off+4+w*h] = rgb.quantize(palette=pal_img).tobytes()

    # Panel 317 (Empty City)
    im, w, h, off = get_sprite(317)
    rgb = im.convert('RGB')
    draw = ImageDraw.Draw(rgb)
    draw.rectangle([80, 380, 160, 412], fill=(180, 150, 120))
    bbox = font_scroll.getbbox('EMPTY')
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text((80 + (80 - tw)//2 - bbox[0], 380 + (32 - th)//2 - bbox[1]), 'EMPTY', font=font_scroll, fill=(255, 255, 240))
    data[off+4:off+4+w*h] = rgb.quantize(palette=pal_img).tobytes()

    # Write out windows_en.dat
    out_dat = os.path.join(GAME_DIR, 'windows_en.dat')
    with open(out_dat, 'wb') as f:
        f.write(data)
    print(f"[SUCCESS] Wrote complete localized windows_en.dat ({len(data)} bytes).")

    # Update active windows.dat if current language is English
    cur_lang_file = os.path.join(GAME_DIR, '.current_language')
    cur_lang = "English"
    if os.path.exists(cur_lang_file):
        with open(cur_lang_file, 'r') as f:
            cur_lang = f.read().strip()
    
    if cur_lang == "English":
        with open(os.path.join(GAME_DIR, 'windows.dat'), 'wb') as f:
            f.write(data)
        print("[SUCCESS] Updated active windows.dat with English HUD and buttons.")

if __name__ == '__main__':
    main()
