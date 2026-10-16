#!/usr/bin/env python3
import os, struct
from PIL import Image, ImageDraw, ImageFont

GAME_DIR = os.path.abspath('assets/game')
FONT_SANS = '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'

def main():
    src_dat = os.path.join(GAME_DIR, 'netGraphics.dat')
    zh_dat = os.path.join(GAME_DIR, 'netGraphics_zh.dat')
    en_dat = os.path.join(GAME_DIR, 'netGraphics_en.dat')

    if not os.path.exists(zh_dat):
        with open(src_dat, 'rb') as f_in, open(zh_dat, 'wb') as f_out:
            f_out.write(f_in.read())
        print(f"Backed up {src_dat} to {zh_dat}")

    with open(zh_dat, 'rb') as f:
        data = bytearray(f.read())

    num_sprites = 350
    offsets = struct.unpack(f'<{num_sprites}I', data[:num_sprites*4])

    pal = Image.open(os.path.join(GAME_DIR, 'mainmenu_en.bmp')).getpalette()
    pal_img = Image.new('P', (1, 1))
    pal_img.putpalette(pal)

    def patch_button(idx, text, is_pressed=False, font_size=12, bx=14, by=4, text_rgb=(0, 0, 0), shadow_rgb=(240, 200, 120)):
        off = offsets[idx]
        w, h = struct.unpack('<HH', data[off:off+4])
        pixels = list(data[off+4:off+4+w*h])
        
        # Determine background index from inner area
        bg_idx = pixels[(h // 2) * w + (w // 2)]
        
        # Fill interior text area
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
        ty = (h - th) // 2 - bbox[1] - 1
        if is_pressed:
            tx += 1
            ty += 1

        if shadow_rgb:
            draw.text((tx + 1, ty + 1), text, font=font, fill=shadow_rgb)
        if text_rgb:
            draw.text((tx, ty), text, font=font, fill=text_rgb)

        q = rgb.quantize(palette=pal_img)
        new_pixels = q.tobytes()
        assert len(new_pixels) == w * h
        data[off+4:off+4+w*h] = new_pixels
        print(f"Patched netGraphics sprite {idx}: '{text}' ({w}x{h}, pressed={is_pressed})")

    # Button patches in netGraphics.dat:
    # 1. Start Game (3, 4, 104x32)
    patch_button(3, "Start Game", is_pressed=False, font_size=14, bx=14, by=4)
    patch_button(4, "Start Game", is_pressed=True,  font_size=14, bx=14, by=4)

    # 2. Host Game (7, 8, 104x32)
    patch_button(7, "Host Game", is_pressed=False, font_size=14, bx=14, by=4)
    patch_button(8, "Host Game", is_pressed=True,  font_size=14, bx=14, by=4)

    # 3. Join Game (13, 14, 104x32)
    patch_button(13, "Join Game", is_pressed=False, font_size=14, bx=14, by=4)
    patch_button(14, "Join Game", is_pressed=True,  font_size=14, bx=14, by=4)

    # 4. Confirm (15, 16, 65x25)
    patch_button(15, "Confirm", is_pressed=False, font_size=11, bx=6, by=3)
    patch_button(16, "Confirm", is_pressed=True,  font_size=11, bx=6, by=3)

    # 5. Cancel (17, 18, 65x25)
    patch_button(17, "Cancel", is_pressed=False, font_size=11, bx=6, by=3)
    patch_button(18, "Cancel", is_pressed=True,  font_size=11, bx=6, by=3)

    with open(en_dat, 'wb') as f:
        f.write(data)
    print(f"Saved {en_dat}")

    with open(src_dat, 'wb') as f:
        f.write(data)
    print("Updated active netGraphics.dat!")

if __name__ == '__main__':
    main()
