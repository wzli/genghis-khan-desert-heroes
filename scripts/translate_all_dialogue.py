#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Complete English Localization Engine for Genghis Khan 1999 (OpenCJSH).
Translates:
- All 33 Talk*.txt / talk*.txt narrative & dialogue scripts (0% question mark replacements)
- Game.txt campaign names, faction titles, and descriptors
- All 33 stage*.stg binary files (stage titles in top bar)
- All 33 stage*.spr binary files (in-game unit and general names)
"""

import os
import sys
import glob
import re
import time
import textwrap
import requests

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
GAME_DIR = os.path.join(BASE_DIR, 'assets', 'game')
ZH_DIR = os.path.join(GAME_DIR, 'text_zh')
EN_DIR = os.path.join(GAME_DIR, 'text_en')

# Import dictionaries from generate_translations
sys.path.insert(0, os.path.join(BASE_DIR, 'scripts'))
import generate_translations as gt

NAME_MAP = dict(gt.GENERALS)
NAME_MAP.update(gt.CASTLES)
NAME_MAP.update(gt.UNITS)
NAME_MAP.update(gt.ITEMS)
NAME_MAP.update({
    '別克帖兒': 'Begter',
    '別勒古台': 'Belgutei',
    '合撒兒': 'Qasar',
    '帖木格': 'Temuge',
    '合赤溫': 'Qachi\'un',
    '也速該': 'Yesugei',
    '訶額侖': 'Hoelun',
    '鐵木真': 'Temujin',
    '札木合': 'Jamukha',
    '孛兒帖': 'Borte',
    '德薛禪': 'Dei Sechen',
    '大灰狼': 'Grey Wolf',
    '馬兒': 'Steed',
    '小金魚': 'goldfish',
    '大汗': 'Khan',
    '可汗': 'Khagan',
    '安答': 'Anda',
    '安達': 'Anda',
    '長生天': 'Eternal Blue Sky',
    '蒙古': 'Mongol',
    '克烈': 'Kereit',
    '乃蠻': 'Naiman',
    '蔑兒乞': 'Merkit',
    '塔塔兒': 'Tatar',
    '泰赤烏': 'Taichi\'ut',
    '翁吉剌': 'Onggirat',
    '弘吉剌': 'Onggirat',
    '札答蘭': 'Jadaran',
    '乞顏': 'Kiyad',
    '主兒勤': 'Jurchin',
    '汪古': 'Ongud',
    '金國': 'Jin Dynasty',
    '西夏': 'Western Xia',
    '南宋': 'Southern Song',
    '西遼': 'Qara Khitai',
    '花剌子模': 'Khwarazm',
    '斡羅斯': 'Rus\'',
    '草原': 'Steppe',
    '部落': 'Clan',
    '步兵': 'Infantry',
    '弓兵': 'Archer',
    '騎兵': 'Cavalry',
    '槍兵': 'Spearman',
    '盜賊': 'Bandit',
    '馬賊': 'Bandit',
    '狼': 'Wolf',
})

# Sorted by length descending for greedy replacement
SORTED_NAMES = sorted(NAME_MAP.items(), key=lambda x: len(x[0]), reverse=True)

SPEAKER_MAP = {
    '暫用': 'Intro',
    '前言': 'Prologue',
    '後序': 'Epilogue',
    '娘': 'Mother',
    '媽': 'Mother',
    '鐵': 'Temujin',
    '也': 'Yesugei',
    '蒙': 'Menglik',
    '弟': 'Brother',
    '哈': 'Qasar',
    '合': 'Qachi\'un',
    '別': 'Belgutei',
    '克': 'Begter',
    '札': 'Jamukha',
    '孛': 'Borte',
    '德': 'Dei Sechen',
    '王': 'Ong Khan',
    '太': 'Tayang Khan',
    '博': 'Bo\'orchu',
    '者': 'Jebe',
    '木': 'Muqali',
    '赤': 'Chilaun',
    '速': 'Subutai',
    '闊': 'Ogedei',
    '托': 'Tolui',
    '察': 'Chagatai',
    '朮': 'Jochi',
    '孩': 'Child',
    '民': 'Villager',
    '兵': 'Soldier',
    '使': 'Envoy',
    '將': 'General',
    '騎': 'Rider',
    '術': 'Shaman',
    '巫': 'Shaman',
    '賊': 'Bandit',
    '狼': 'Wolf',
}

def translate_gt(text):
    if not text.strip():
        return text
    url = 'https://translate.googleapis.com/translate_a/single'
    params = {'client': 'gtx', 'sl': 'zh-TW', 'tl': 'en', 'dt': 't', 'q': text}
    for attempt in range(3):
        try:
            r = requests.get(url, params=params, timeout=10)
            if r.status_code == 200:
                data = r.json()
                return ''.join(item[0] for item in data[0] if item[0])
        except Exception:
            time.sleep(0.5)
    return text

def clean_punct(text):
    text = text.replace('，', ', ').replace('。', '. ').replace('！', '! ').replace('？', '? ')
    text = text.replace('：', ': ').replace('；', '; ').replace('（', '(').replace('）', ')')
    text = text.replace('「', '"').replace('」', '"').replace('『', '"').replace('』', '"')
    text = text.replace('、', ', ').replace('‧', '.').replace('…', '...').replace('—', '-')
    text = re.sub(r' +', ' ', text)
    text = re.sub(r' ,', ',', text)
    text = re.sub(r' \.', '.', text)
    text = re.sub(r' !', '!', text)
    text = re.sub(r' \?', '?', text)
    return text.strip()

def translate_paragraph(para):
    if not para.strip():
        return para
    if not any('\u4e00' <= c <= '\u9fff' for c in para):
        return para

    # Protect tags %1...%%, %2...%%, etc.
    tags = []
    def tag_repl(m):
        idx = len(tags)
        t_num = m.group(1)
        t_inner = m.group(2)
        for zh, en in SORTED_NAMES:
            t_inner = t_inner.replace(zh, en)
        if any('\u4e00' <= c <= '\u9fff' for c in t_inner):
            t_inner = translate_gt(t_inner)
        t_inner = clean_punct(t_inner)
        tags.append(f'%{t_num}{t_inner}%%')
        return f' __TAG{idx}__ '

    masked = re.sub(r'%([1-4])(.*?)%%', tag_repl, para)

    # Replace known historical entities before sending to GT
    for zh, en in SORTED_NAMES:
        masked = masked.replace(zh, en)

    if any('\u4e00' <= c <= '\u9fff' for c in masked):
        en = translate_gt(masked)
    else:
        en = masked

    en = clean_punct(en)

    # Restore tags
    for i, tag in enumerate(tags):
        en = re.sub(rf'__TAG{i}__', tag, en, flags=re.IGNORECASE)

    # Post-clean entity translations
    for zh, en in SORTED_NAMES:
        en = en.replace(zh, en)

    # Wrap cleanly at 32 chars
    wrapped_lines = []
    for line in en.splitlines():
        if line.strip():
            w = textwrap.fill(line.strip(), width=32, break_long_words=False)
            wrapped_lines.append(w)
        else:
            wrapped_lines.append('')
    return '\n'.join(wrapped_lines)

def translate_talk_file(src_path, dst_path):
    print(f"Translating {os.path.basename(src_path)} -> {os.path.basename(dst_path)}...")
    with open(src_path, 'rb') as f:
        content = f.read().decode('big5', 'ignore')

    out_sections = []
    lines = content.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith('#'):
            if '//' in line:
                tag, comment = line.split('//', 1)
                comment = comment.strip()
                spk = SPEAKER_MAP.get(comment, None)
                if not spk:
                    for zh, en in SORTED_NAMES:
                        if zh in comment:
                            spk = en
                            break
                if not spk:
                    spk = translate_gt(comment) if any('\u4e00' <= c <= '\u9fff' for c in comment) else comment
                out_sections.append(f"{tag}//{spk}")
            else:
                out_sections.append(line)
            i += 1
            continue

        block_lines = []
        while i < len(lines) and not lines[i].startswith('#'):
            block_lines.append(lines[i])
            i += 1

        paras = []
        cur_para = []
        for bl in block_lines:
            if bl.strip():
                cur_para.append(bl.strip())
            else:
                if cur_para:
                    paras.append(' '.join(cur_para))
                    cur_para = []
                paras.append('')
        if cur_para:
            paras.append(' '.join(cur_para))

        trans_paras = []
        for p in paras:
            if p:
                trans_paras.append(translate_paragraph(p))
            else:
                trans_paras.append('')

        for tp in trans_paras:
            out_sections.append(tp)

    out_text = '\n'.join(out_sections) + '\n'
    out_ascii = out_text.encode('ascii', errors='ignore').decode('ascii')
    with open(dst_path, 'w', encoding='ascii') as f:
        f.write(out_ascii)

    q_count = out_ascii.count('?')
    print(f"  -> Generated {os.path.basename(dst_path)}: {len(out_ascii)} bytes, {q_count} ?")

def translate_all_talk_files():
    print("==================================================")
    print(" 1. Translating all Talk narrative scripts")
    print("==================================================")
    for path in sorted(glob.glob(os.path.join(ZH_DIR, '[Tt]alk*.txt'))):
        fname = os.path.basename(path)
        if fname.lower() in ['talk11.txt', 'talk12.txt']:
            print(f"Skipping {fname} (already authentic English)")
            continue
        dst = os.path.join(EN_DIR, fname)
        translate_talk_file(path, dst)

def translate_game_txt():
    print("==================================================")
    print(" 2. Translating Game.txt")
    print("==================================================")
    src = os.path.join(ZH_DIR, 'Game.txt')
    dst = os.path.join(EN_DIR, 'Game.txt')
    with open(src, 'rb') as f:
        lines = f.read().decode('big5', 'ignore').splitlines()

    out_lines = []
    batch = []

    def flush_batch():
        if not batch: return
        joined = '\n'.join(batch)
        trans = translate_gt(joined)
        res = trans.splitlines()
        for idx, (orig, t_line) in enumerate(zip(batch, res)):
            clean_t = clean_punct(t_line)
            for zh, en in SORTED_NAMES:
                clean_t = clean_t.replace(zh, en)
            out_lines.append(clean_t)
        batch.clear()

    for idx, l in enumerate(lines):
        if not l.strip():
            flush_batch()
            out_lines.append('')
            continue
        matched = False
        for zh, en in SORTED_NAMES:
            if l.strip() == zh:
                flush_batch()
                out_lines.append(en)
                matched = True
                break
        if matched:
            continue
        batch.append(l.strip())
        if len(batch) >= 40:
            flush_batch()
    flush_batch()

    out_text = '\r\n'.join(out_lines) + '\r\n'
    out_ascii = out_text.encode('ascii', errors='ignore').decode('ascii')
    with open(dst, 'w', encoding='ascii') as f:
        f.write(out_ascii)
    print(f"  -> Generated {dst}: {len(out_ascii)} bytes, {out_ascii.count('?')} ?")

STAGE_TITLES = {
    'stage01': 'Feuds of the Steppe',
    'stage02': 'Fall of East Asia',
    'stage03': 'Scourge of Eurasia',
    'stage04': 'Feuds of the Steppe',
    'stage11': 'Young Temujin',
    'stage12': 'Tragic Fate',
    'stage13': "Tribe's Desertion",
    'stage14': "Pursuit of the Taichi'ut",
    'stage15': 'Escape from Death',
    'stage16': 'True Bond in Adversity',
    'stage17': 'The Abduction of Borte',
    'stage18': 'Rescue of Borte',
    'stage19': 'Battle of the 13 Wings',
    'stage20': 'Fall of the Taichi\'ut',
    'stage21': 'Battle of Koiten',
    'stage22': 'Subjugation of Tatars',
    'stage23': 'Battle of Qalaqaljid',
    'stage24': 'Ambush on Ong Khan',
    'stage25': 'Fall of Tayang Khan',
    'stage26': 'The End of Jamukha',
    'stage27': 'Genghis Khan Crowned',
    'stage28': 'Qocho and the Qarluqs',
    'stage29': 'Western Xia Campaign',
    'stage30': 'Invasion of Jin Dynasty',
    'stage31': 'Battle of Yehuling',
    'stage32': 'Breaching Juyong Pass',
    'stage33': 'Conquest of Hebei',
    'stage34': 'Fall of Kuchlug',
    'stage35': 'Western Expedition',
    'stage36': 'Fate of Muhammad II',
    'stage37': 'Defiance of Jalal al-Din',
    'stage38': 'The Rus\' Coalition',
    'stage39': 'Twilight Years (Finale)',
}

def translate_all_stg_files():
    print("==================================================")
    print(" 3. Translating stage*.stg files (top-bar titles)")
    print("==================================================")
    stg_files = sorted(glob.glob(os.path.join(GAME_DIR, 'stage*.stg')))
    for f in stg_files:
        base = os.path.basename(f)
        if '_en' in base or '_zh' in base:
            continue
        stage_key = base.split('.')[0]
        title = STAGE_TITLES.get(stage_key, 'Genghis Khan')

        zh_backup = os.path.join(GAME_DIR, f"{stage_key}_zh.stg")
        en_target = os.path.join(GAME_DIR, f"{stage_key}_en.stg")

        with open(f, 'rb') as fp:
            data = bytearray(fp.read())

        if not os.path.exists(zh_backup):
            with open(zh_backup, 'wb') as fp:
                fp.write(data)

        title_bytes = title.encode('ascii')[:23] + b'\x00'
        title_bytes = title_bytes.ljust(24, b'\x00')
        data[8:32] = title_bytes

        with open(en_target, 'wb') as fp:
            fp.write(data)
        print(f"  -> Generated {os.path.basename(en_target)}: title='{title}'")

def translate_all_spr_files():
    print("==================================================")
    print(" 4. Translating stage*.spr files (battlefield unit rosters)")
    print("==================================================")
    spr_files = sorted(glob.glob(os.path.join(GAME_DIR, 'stage*.spr')))
    for f in spr_files:
        base = os.path.basename(f)
        if '_en' in base or '_zh' in base:
            continue
        stage_key = base.split('.')[0]
        zh_backup = os.path.join(GAME_DIR, f"{stage_key}_zh.spr")
        en_target = os.path.join(GAME_DIR, f"{stage_key}_en.spr")

        with open(f, 'rb') as fp:
            data = bytearray(fp.read())

        if not os.path.exists(zh_backup):
            with open(zh_backup, 'wb') as fp:
                fp.write(data)

        rec_size = 548
        name_len = 20
        total_units = (len(data) - 0x134) // rec_size + 1
        replaced_count = 0

        for r in range(total_units):
            off = 0x134 + r * rec_size
            if off + name_len > len(data):
                break
            raw_name = bytes(data[off:off+name_len]).split(b'\x00')[0]
            if not raw_name:
                continue
            try:
                zh_name = raw_name.decode('big5').strip()
            except Exception:
                continue

            en_name = NAME_MAP.get(zh_name, None)
            if not en_name:
                for zh_k, en_v in SORTED_NAMES:
                    if zh_k in zh_name:
                        en_name = en_v
                        break
            if en_name:
                en_bytes = en_name.encode('ascii')[:name_len-1] + b'\x00'
                en_bytes = en_bytes.ljust(name_len, b'\x00')
                data[off:off+name_len] = en_bytes
                replaced_count += 1

        with open(en_target, 'wb') as fp:
            fp.write(data)
        print(f"  -> Generated {os.path.basename(en_target)}: {replaced_count} unit names localized")

if __name__ == '__main__':
    translate_all_talk_files()
    translate_game_txt()
    translate_all_stg_files()
    translate_all_spr_files()
    print("==================================================")
    print(" ALL TRANSLATIONS GENERATED SUCCESSFULLY!")
    print("==================================================")
