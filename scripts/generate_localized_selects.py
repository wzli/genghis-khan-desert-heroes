#!/usr/bin/env python3
import os, struct
from PIL import Image, ImageDraw, ImageFont, ImageFilter

GAME_DIR = os.path.abspath('assets/game')
FONT_SERIF = '/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf'

def create_hover_sprite(text, bg_tile, orig_sprite_pal, width=238, height=38):
    canvas = Image.new('RGB', (width, height))
    tw_tile, th_tile = bg_tile.size
    for x in range(0, width, tw_tile):
        for y in range(0, height, th_tile):
            canvas.paste(bg_tile, (x, y))
            
    glow_mask = Image.new('L', (width, height), 0)
    font = ImageFont.truetype(FONT_SERIF, 20)
    bbox = font.getbbox(text)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    tx = (width - tw) // 2
    ty = (height - th) // 2 - 2
    
    glow_draw = ImageDraw.Draw(glow_mask)
    glow_draw.text((tx, ty), text, font=font, fill=255)
    blurred_glow = glow_mask.filter(ImageFilter.GaussianBlur(radius=2.0))
    
    glow_rgb = Image.new('RGB', (width, height), (255, 240, 120))
    canvas.paste(glow_rgb, (0, 0), blurred_glow)
    
    draw = ImageDraw.Draw(canvas)
    draw.text((tx, ty), text, font=font, fill=(255, 255, 220))
    
    pal_img = Image.new('P', (1, 1))
    pal_img.putpalette(orig_sprite_pal)
    
    quantized = canvas.quantize(palette=pal_img)
    return quantized.tobytes()

def create_netmenu_hover_sprite(text, orig_px, orig_pal, width=214, height=43):
    orig_im = Image.frombytes('P', (width, height), orig_px)
    orig_im.putpalette(orig_pal)
    
    rgb = orig_im.convert('RGB')
    draw = ImageDraw.Draw(rgb)
    # Clear inner area while preserving outer metallic beveled border
    draw.rectangle([13, 5, width - 14, height - 6], fill=(11, 80, 164))
    
    font = ImageFont.truetype(FONT_SERIF, 20)
    bbox = font.getbbox(text)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    tx = (width - tw) // 2
    ty = (height - th) // 2 - 2
    
    glow_mask = Image.new('L', (width, height), 0)
    gdraw = ImageDraw.Draw(glow_mask)
    gdraw.text((tx, ty), text, font=font, fill=255)
    blurred = glow_mask.filter(ImageFilter.GaussianBlur(radius=2.0))
    
    glow_rgb = Image.new('RGB', (width, height), (120, 180, 255))
    rgb.paste(glow_rgb, (0, 0), blurred)
    
    draw = ImageDraw.Draw(rgb)
    draw.text((tx, ty), text, font=font, fill=(255, 255, 255))
    
    pal_img = Image.new('P', (1, 1))
    pal_img.putpalette(orig_pal)
    q = rgb.quantize(palette=pal_img)
    
    q_data = list(q.getflattened_data() if hasattr(q, 'getflattened_data') else q.getdata())
    orig_data = list(orig_im.getflattened_data() if hasattr(orig_im, 'getflattened_data') else orig_im.getdata())
    
    # Restore outer beveled border pixels exactly from original
    for y in range(height):
        for x in range(width):
            if not (13 <= x <= width - 14 and 5 <= y <= height - 6):
                q_data[y * width + x] = orig_data[y * width + x]
                
    return bytes(q_data)

def main():
    src_dat = os.path.join(GAME_DIR, 'selects.dat')
    zh_dat = os.path.join(GAME_DIR, 'selects_zh.dat')
    en_dat = os.path.join(GAME_DIR, 'selects_en.dat')
    
    if not os.path.exists(zh_dat):
        with open(src_dat, 'rb') as f_in, open(zh_dat, 'wb') as f_out:
            f_out.write(f_in.read())
        print(f"Backed up {src_dat} to {zh_dat}")
        
    with open(zh_dat, 'rb') as f:
        data = bytearray(f.read())
        
    offsets = [struct.unpack('<I', data[i:i+4])[0] for i in range(0, 0x578, 4)]
    
    # Brown tile from mainmenu_zh.bmp
    mm = Image.open(os.path.join(GAME_DIR, 'mainmenu_zh.bmp')).convert('RGB')
    brown_tile = mm.crop((481, 183, 481+22, 183+18))
    
    # Green tile from single_zh.bmp
    single = Image.open(os.path.join(GAME_DIR, 'single_zh.bmp')).convert('RGB')
    green_tile = single.crop((485, 210, 485+22, 210+18))
    
    mainmenu_pal = Image.open(os.path.join(GAME_DIR, 'mainmenu_zh.bmp')).getpalette()
    single_pal = Image.open(os.path.join(GAME_DIR, 'single_zh.bmp')).getpalette()
    net1_pal = Image.open(os.path.join(GAME_DIR, 'netmenu01_zh.bmp')).getpalette()
    
    sprites_info = [
        # (index, text, tile, palette)
        (0, "Single Player", brown_tile, mainmenu_pal),
        (1, "Multiplayer", brown_tile, mainmenu_pal),
        (2, "Load Game", brown_tile, mainmenu_pal),
        (3, "Credits", brown_tile, mainmenu_pal),
        (4, "Exit Game", brown_tile, mainmenu_pal),
        (5, "Story Mode", green_tile, single_pal),
        (6, "Conquest Mode", green_tile, single_pal),
        (7, "Skirmish", green_tile, single_pal),
        (8, "Main Menu", green_tile, single_pal),
    ]
    
    for idx, text, tile, pal in sprites_info:
        off = offsets[idx]
        w, h = struct.unpack('<HH', data[off:off+4])
        new_pixels = create_hover_sprite(text, tile, pal, width=w, height=h)
        assert len(new_pixels) == w * h
        data[off+4:off+4+len(new_pixels)] = new_pixels
        print(f"Patched sprite {idx} ({text}, {w}x{h}) at {hex(off)}")
        
    net_sprites = [
        (24, "LAN Game"),
        (25, "Internet Game"),
        (26, "Main Menu"),
    ]
    for idx, text in net_sprites:
        off = offsets[idx]
        w, h = struct.unpack('<HH', data[off:off+4])
        orig_px = bytes(data[off+4:off+4+w*h])
        new_pixels = create_netmenu_hover_sprite(text, orig_px, net1_pal, width=w, height=h)
        assert len(new_pixels) == w * h
        data[off+4:off+4+len(new_pixels)] = new_pixels
        print(f"Patched netmenu hover sprite {idx} ({text}, {w}x{h}) at {hex(off)}")
        
    with open(en_dat, 'wb') as f:
        f.write(data)
    print(f"Saved {en_dat}")
    
    # Copy to active selects.dat
    with open(src_dat, 'wb') as f:
        f.write(data)
    print("Updated active selects.dat with English hover sprites!")

if __name__ == '__main__':
    main()
