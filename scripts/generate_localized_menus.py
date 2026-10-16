#!/usr/bin/env python3
import os
from PIL import Image, ImageDraw, ImageFont

GAME_DIR = os.path.abspath('assets/game')
FONT_SERIF = '/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf'

def backup_zh(name):
    src = os.path.join(GAME_DIR, f"{name}.bmp")
    zh_dst = os.path.join(GAME_DIR, f"{name}_zh.bmp")
    if not os.path.exists(zh_dst):
        with open(src, 'rb') as f_in, open(zh_dst, 'wb') as f_out:
            f_out.write(f_in.read())
        print(f"Backed up original {name}.bmp to {name}_zh.bmp")

def render_styled_text(draw, box, text, font, fill_color, shadow_color, shadow_offset=(2, 2)):
    bbox = font.getbbox(text)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    
    bw = box[2] - box[0]
    bh = box[3] - box[1]
    
    tx = box[0] + (bw - tw) // 2
    ty = box[1] + (bh - th) // 2 - 2
    
    # Shadow
    ox, oy = shadow_offset
    draw.text((tx + ox, ty + oy), text, font=font, fill=shadow_color)
    if ox > 1 or oy > 1:
        draw.text((tx + ox//2, ty + oy//2), text, font=font, fill=(shadow_color[0]//2, shadow_color[1]//2, shadow_color[2]//2))
    # Main text
    draw.text((tx, ty), text, font=font, fill=fill_color)

def process_mainmenu():
    backup_zh("mainmenu")
    im = Image.open(os.path.join(GAME_DIR, "mainmenu_zh.bmp"))
    rgb = im.convert('RGB')
    
    # Clean brown tile
    tile = rgb.crop((481, 183, 481+22, 183+18))
    
    buttons = [
        (175, "Single Player"),
        (235, "Multiplayer"),
        (295, "Load Game"),
        (355, "Credits"),
        (415, "Exit Game")
    ]
    
    font = ImageFont.truetype(FONT_SERIF, 20)
    for y_top, text in buttons:
        # Fill brown button inner area seamlessly
        for x in range(276, 524, 22):
            for y in range(y_top + 1, y_top + 39, 18):
                rgb.paste(tile, (x, y))
        
        draw = ImageDraw.Draw(rgb)
        box = (275, y_top + 1, 525, y_top + 39)
        render_styled_text(draw, box, text, font, 
                           fill_color=(255, 235, 80), 
                           shadow_color=(30, 15, 5),
                           shadow_offset=(2, 2))
        
    out = rgb.quantize(palette=im)
    out_path = os.path.join(GAME_DIR, "mainmenu_en.bmp")
    out.save(out_path)
    print(f"Generated {out_path}")

def process_single():
    backup_zh("single")
    im = Image.open(os.path.join(GAME_DIR, "single_zh.bmp"))
    rgb = im.convert('RGB')
    
    tile = rgb.crop((485, 210, 485+22, 210+18))
    
    buttons = [
        (201, "Story Mode"),
        (263, "Conquest Mode"),
        (325, "Skirmish"),
        (389, "Main Menu")
    ]
    
    font = ImageFont.truetype(FONT_SERIF, 20)
    for y_top, text in buttons:
        for x in range(276, 524, 22):
            for y in range(y_top + 2, y_top + 41, 18):
                rgb.paste(tile, (x, y))
                
        draw = ImageDraw.Draw(rgb)
        box = (275, y_top + 2, 525, y_top + 41)
        render_styled_text(draw, box, text, font,
                           fill_color=(255, 240, 90),
                           shadow_color=(20, 30, 10),
                           shadow_offset=(2, 2))
        
    out = rgb.quantize(palette=im)
    out_path = os.path.join(GAME_DIR, "single_en.bmp")
    out.save(out_path)
    print(f"Generated {out_path}")

def process_story():
    backup_zh("story")
    im = Image.open(os.path.join(GAME_DIR, "story_zh.bmp"))
    rgb = im.convert('RGB')
    
    # Use clean green button tile from single.bmp
    single_im = Image.open(os.path.join(GAME_DIR, "single_zh.bmp")).convert('RGB')
    tile = single_im.crop((485, 210, 485+22, 210+18))
    
    buttons = [
        (201, "Standard Campaign"),
        (263, "Short Scenarios"),
        (325, "Tutorial Mode"),
        (389, "Main Menu")
    ]
    
    font = ImageFont.truetype(FONT_SERIF, 19)
    for y_top, text in buttons:
        for x in range(276, 524, 22):
            for y in range(y_top + 2, y_top + 41, 18):
                rgb.paste(tile, (x, y))
                
        draw = ImageDraw.Draw(rgb)
        box = (275, y_top + 2, 525, y_top + 41)
        render_styled_text(draw, box, text, font,
                           fill_color=(255, 240, 90),
                           shadow_color=(20, 30, 10),
                           shadow_offset=(2, 2))
        
    out = rgb.quantize(palette=im)
    out_path = os.path.join(GAME_DIR, "story_en.bmp")
    out.save(out_path)
    print(f"Generated {out_path}")

def process_stage():
    backup_zh("stage")
    im = Image.open(os.path.join(GAME_DIR, "stage_zh.bmp"))
    rgb = im.convert('RGB')
    
    btn_bg = (195, 137, 57)
    draw = ImageDraw.Draw(rgb)
    
    cancel_box = (291, 550, 391, 576)
    confirm_box = (401, 550, 501, 576)
    
    draw.rectangle(cancel_box, fill=btn_bg)
    draw.rectangle(confirm_box, fill=btn_bg)
    
    font = ImageFont.truetype(FONT_SERIF, 16)
    render_styled_text(draw, cancel_box, "Cancel", font,
                       fill_color=(20, 10, 5),
                       shadow_color=(225, 185, 100),
                       shadow_offset=(1, 1))
    render_styled_text(draw, confirm_box, "Confirm", font,
                       fill_color=(20, 10, 5),
                       shadow_color=(225, 185, 100),
                       shadow_offset=(1, 1))
        
    out = rgb.quantize(palette=im)
    out_path = os.path.join(GAME_DIR, "stage_en.bmp")
    out.save(out_path)
    print(f"Generated {out_path}")

def process_act_bg():
    backup_zh("act_bg")
    im = Image.open(os.path.join(GAME_DIR, "act_bg_zh.bmp"))
    rgb = im.convert('RGB')
    
    btn_bg = (195, 137, 57)
    draw = ImageDraw.Draw(rgb)
    
    cancel_box = (57, 533, 157, 556)
    confirm_box = (167, 533, 267, 556)
    
    draw.rectangle(cancel_box, fill=btn_bg)
    draw.rectangle(confirm_box, fill=btn_bg)
    
    font = ImageFont.truetype(FONT_SERIF, 16)
    render_styled_text(draw, cancel_box, "Cancel", font,
                       fill_color=(20, 10, 5),
                       shadow_color=(225, 185, 100),
                       shadow_offset=(1, 1))
    render_styled_text(draw, confirm_box, "Confirm", font,
                       fill_color=(20, 10, 5),
                       shadow_color=(225, 185, 100),
                       shadow_offset=(1, 1))
        
    out = rgb.quantize(palette=im)
    out_path = os.path.join(GAME_DIR, "act_bg_en.bmp")
    out.save(out_path)
    print(f"Generated {out_path}")

def render_signboard(rgb, title_text):
    wood_tile = rgb.crop((260, 4, 285, 54))
    tw, th = wood_tile.size
    for x in range(275, 525, tw):
        rgb.paste(wood_tile, (x, 4))
    draw = ImageDraw.Draw(rgb)
    font_sign = ImageFont.truetype(FONT_SERIF, 24)
    render_styled_text(draw, (255, 3, 548, 55), title_text, font_sign,
                       fill_color=(255, 235, 90), shadow_color=(20, 10, 5), shadow_offset=(2, 2))

def process_netmenu00():
    backup_zh("netmenu00")
    im = Image.open(os.path.join(GAME_DIR, "netmenu00_zh.bmp"))
    rgb = im.convert('RGB')
    
    render_signboard(rgb, "Scenario Settings")
    
    btn_bg = (195, 137, 57)
    draw = ImageDraw.Draw(rgb)
    cancel_box = (604, 528, 704, 554)
    draw.rectangle(cancel_box, fill=btn_bg)
    
    font = ImageFont.truetype(FONT_SERIF, 15)
    render_styled_text(draw, cancel_box, "Cancel", font,
                       fill_color=(20, 10, 5),
                       shadow_color=(225, 185, 100),
                       shadow_offset=(1, 1))
    
    out = rgb.quantize(palette=im)
    out_path = os.path.join(GAME_DIR, "netmenu00_en.bmp")
    out.save(out_path)
    print(f"Generated {out_path}")

def process_netmenu01():
    backup_zh("netmenu01")
    im = Image.open(os.path.join(GAME_DIR, "netmenu01_zh.bmp"))
    rgb = im.convert('RGB')
    
    render_signboard(rgb, "Multiplayer Mode")
    
    buttons = [
        (199, "LAN Game"),
        (264, "Internet Game"),
        (329, "Main Menu")
    ]
    font = ImageFont.truetype(FONT_SERIF, 19)
    draw = ImageDraw.Draw(rgb)
    for y_top, text in buttons:
        draw.rectangle((305, y_top + 4, 495, y_top + 39), fill=(25, 45, 9))
        box = (305, y_top + 4, 495, y_top + 39)
        render_styled_text(draw, box, text, font,
                           fill_color=(255, 240, 90),
                           shadow_color=(10, 20, 5),
                           shadow_offset=(2, 2))
        
    out = rgb.quantize(palette=im)
    out_path = os.path.join(GAME_DIR, "netmenu01_en.bmp")
    out.save(out_path)
    print(f"Generated {out_path}")

def process_netmenu02():
    backup_zh("netmenu02")
    im = Image.open(os.path.join(GAME_DIR, "netmenu02_zh.bmp"))
    rgb = im.convert('RGB')
    
    render_signboard(rgb, "LAN Game")
    
    draw = ImageDraw.Draw(rgb)
    font = ImageFont.truetype(FONT_SERIF, 14)
    for (x0, x1), text in [((243, 347), "Host Game"), ((353, 457), "Join Game"), ((497, 601), "Cancel")]:
        draw.rectangle((x0 + 14, 553, x1 - 14, 579), fill=(186, 137, 53))
        box = (x0 + 14, 553, x1 - 14, 579)
        render_styled_text(draw, box, text, font,
                           fill_color=(20, 10, 5), shadow_color=(225, 185, 100), shadow_offset=(1, 1))
    
    out = rgb.quantize(palette=im)
    out_path = os.path.join(GAME_DIR, "netmenu02_en.bmp")
    out.save(out_path)
    print(f"Generated {out_path}")

def process_netmenu03():
    backup_zh("netmenu03")
    im = Image.open(os.path.join(GAME_DIR, "netmenu03_zh.bmp"))
    rgb = im.convert('RGB')
    
    render_signboard(rgb, "Select Ruler")
    
    btn_bg = (195, 137, 57)
    draw = ImageDraw.Draw(rgb)
    confirm_box = (348, 551, 448, 577)
    draw.rectangle(confirm_box, fill=btn_bg)
    
    font = ImageFont.truetype(FONT_SERIF, 15)
    render_styled_text(draw, confirm_box, "Confirm", font,
                       fill_color=(20, 10, 5), shadow_color=(225, 185, 100), shadow_offset=(1, 1))
    
    out = rgb.quantize(palette=im)
    out_path = os.path.join(GAME_DIR, "netmenu03_en.bmp")
    out.save(out_path)
    print(f"Generated {out_path}")

if __name__ == '__main__':
    process_mainmenu()
    process_single()
    process_story()
    process_stage()
    process_act_bg()
    process_netmenu00()
    process_netmenu01()
    process_netmenu02()
    process_netmenu03()
    print("All localized menu bitmaps generated successfully!")
