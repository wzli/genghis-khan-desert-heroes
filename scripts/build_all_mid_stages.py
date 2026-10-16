#!/usr/bin/env python3
import os
import sys
import re

import mid_stages_common as common
import stage18_19
import stage20_21
import stage22_23
import stage24_25
import stage26_27

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
ZH_DIR = os.path.join(BASE_DIR, 'assets', 'game', 'text_zh')
EN_DIR = os.path.join(BASE_DIR, 'assets', 'game', 'text_en')

STAGE_MAP = [
    ('talk18.txt', stage18_19.TALK18_SECTIONS),
    ('talk19.txt', stage18_19.TALK19_SECTIONS),
    ('talk20.txt', stage20_21.TALK20_SECTIONS),
    ('talk21.txt', stage21_sections := stage20_21.TALK21_SECTIONS),
    ('Talk22.txt', stage22_23.TALK22_SECTIONS),
    ('Talk23.txt', stage22_23.TALK23_SECTIONS),
    ('Talk24.txt', stage24_25.TALK24_SECTIONS),
    ('Talk25.txt', stage24_25.TALK25_SECTIONS),
    ('Talk26.txt', stage26_27.TALK26_SECTIONS),
    ('Talk27.txt', stage26_27.TALK27_SECTIONS),
]

def main():
    print("=" * 60)
    print("BUILDING AND VERIFYING MID STAGES (talk18 - Talk27)")
    print("=" * 60)
    
    all_passed = True
    
    for filename, sections in STAGE_MAP:
        zh_path = os.path.join(ZH_DIR, filename)
        en_path = os.path.join(EN_DIR, filename)
        
        # 1. Read Chinese original sections
        with open(zh_path, 'rb') as f:
            zh_content = f.read().decode('big5')
        zh_headers = [l for l in zh_content.splitlines() if l.startswith('#') and l != '#']
        
        # Extract section numbers from zh headers
        zh_sec_nums = []
        for h in zh_headers:
            m = re.match(r'#(\d+)', h)
            if m:
                zh_sec_nums.append(m.group(1))
            else:
                zh_sec_nums.append(h)
                
        en_sec_nums = []
        for h, _ in sections:
            m = re.match(r'#(\d+)', h)
            if m:
                en_sec_nums.append(m.group(1))
            else:
                en_sec_nums.append(h)
                
        if zh_sec_nums != en_sec_nums:
            print(f"[ERROR] Section ID mismatch in {filename}!")
            print(f"  ZH: {len(zh_sec_nums)} sections")
            print(f"  EN: {len(en_sec_nums)} sections")
            diff = [f"ZH:{z} vs EN:{e}" for z, e in zip(zh_sec_nums, en_sec_nums) if z != e]
            print("  Differences:", diff[:10])
            all_passed = False
            continue
            
        # 2. Build translated file
        content = common.build_stage_file(sections, wrap_dialogue=True, dialogue_width=32)
        
        # 3. Write file in 100% ASCII
        with open(en_path, 'wb') as f:
            f.write(content.encode('ascii'))
            
        # 4. Verification
        ok, msg = common.verify_file(en_path)
        if not ok:
            print(f"[ERROR] Verification failed for {filename}: {msg}")
            all_passed = False
            continue
            
        # 5. Check line lengths
        lines = content.splitlines()
        max_vis = 0
        long_lines = []
        for l in lines:
            if l.startswith('#'):
                continue
            vis = common.visible_len(l)
            if vis > max_vis:
                max_vis = vis
            # Flag if single dialogue line is excessively long (> 40 visible chars)
            if vis > 40:
                long_lines.append((vis, l))
                
        print(f"[SUCCESS] {filename:11s} -> {len(sections)} sections, {len(content)} bytes, max_vis_line: {max_vis}")
        if long_lines:
            print(f"  Warning: {len(long_lines)} lines with vis_len > 40:")
            for vl, ll in long_lines[:3]:
                print(f"    ({vl}) {ll}")

    print("=" * 60)
    if all_passed:
        print("ALL 10 MID STAGE FILES COMPILED AND VERIFIED PERFECTLY!")
    else:
        print("SOME FILES HAD ISSUES. PLEASE CHECK OUTPUT ABOVE.")
    print("=" * 60)
    return 0 if all_passed else 1

if __name__ == '__main__':
    sys.exit(main())
