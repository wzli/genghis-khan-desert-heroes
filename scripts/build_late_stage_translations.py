#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master localization builder and verifier for Late Stages (Talk28.txt to talk38.txt).
"""

import os
import sys
import re

import translations_data_28_30 as d28_30
import translations_data_31_33 as d31_33
import translations_data_34_35 as d34_35
import translations_data_36_38 as d36_38

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
ZH_DIR = os.path.join(BASE_DIR, 'assets', 'game', 'text_zh')
EN_DIR = os.path.join(BASE_DIR, 'assets', 'game', 'text_en')

FILE_MAP = {
    'Talk28.txt': d28_30.TALK28_DATA,
    'Talk29.txt': d28_30.TALK29_DATA,
    'Talk30.txt': d28_30.TALK30_DATA,
    'Talk31.txt': d31_33.TALK31_DATA,
    'Talk32.txt': d31_33.TALK32_DATA,
    'talk33.txt': d31_33.TALK33_DATA,
    'talk34.txt': d34_35.TALK34_DATA,
    'talk35.txt': d34_35.TALK35_DATA,
    'talk36.txt': d36_38.TALK36_DATA,
    'talk37.txt': d36_38.TALK37_DATA,
    'talk38.txt': d36_38.TALK38_DATA,
}

def generate_file(filename, data):
    zh_path = os.path.join(ZH_DIR, filename)
    en_path = os.path.join(EN_DIR, filename)
    
    with open(zh_path, 'rb') as f:
        zh_lines = f.read().decode('cp950').splitlines()
    
    zh_headers = [l for l in zh_lines if l.startswith('#') and l.strip() != '#']
    data_keys = list(data.keys())
    
    assert len(zh_headers) == len(data_keys), f'Header count mismatch in {filename}: {len(zh_headers)} vs {len(data_keys)}'
    
    out_lines = []
    for key, text in data.items():
        out_lines.append(f'#{key}')
        if text.strip():
            out_lines.append(text)
        out_lines.append('#')
    
    # Trailing empty lines matching game format
    out_lines.extend(['', '', '', ''])
    
    content = '\n'.join(out_lines) + '\n'
    
    # Ensure ASCII
    ascii_content = content.encode('ascii').decode('ascii')
    with open(en_path, 'w', encoding='ascii', newline='\n') as f:
        f.write(ascii_content)
    
    print(f'[OK] Generated {filename} ({len(ascii_content)} bytes, {len(data)} sections)')

def verify_file(filename, data):
    en_path = os.path.join(EN_DIR, filename)
    zh_path = os.path.join(ZH_DIR, filename)
    
    with open(en_path, 'rb') as f:
        raw = f.read()
    
    # 1. ASCII check
    try:
        text = raw.decode('ascii')
    except UnicodeDecodeError as e:
        raise AssertionError(f'{filename} contains non-ASCII bytes: {e}')
    
    # 2. Check for invalid placeholder ?
    # Valid question marks are preceded by a word or end of sentence.
    # Placeholder ? usually looks like ?? or ? surrounded by Chinese/replacement.
    q_matches = re.findall(r'\?{2,}', text)
    if q_matches:
        raise AssertionError(f'{filename} contains consecutive question marks: {q_matches}')
    
    # Check that any ? is grammatically part of a question
    lines = text.splitlines()
    for lineno, line in enumerate(lines, 1):
        if '?' in line:
            # Check context of ?
            if not re.search(r'\w+.*\?', line) and not line.strip() == '?':
                print(f'  [Warning] Question mark in {filename}:{lineno}: {line}')
    
    # 3. Check formatting tags (%1...%%, %2...%%, %3...%%, %4...%%)
    open_tags = len(re.findall(r'%[1-4]', text))
    close_tags = len(re.findall(r'%%', text))
    if open_tags != close_tags:
        raise AssertionError(f'{filename} tag mismatch: {open_tags} opening tags vs {close_tags} closing tags')
    
    # Tags spanning multiple lines are fine, but check no malformed %
    
    # 4. Check section structure
    sec_headers = [l for l in lines if l.startswith('#') and l.strip() != '#']
    if len(sec_headers) != len(data):
        raise AssertionError(f'{filename} section count mismatch: {len(sec_headers)} vs expected {len(data)}')
    
    # 5. Check line lengths of dialogue
    long_lines = []
    for lineno, line in enumerate(lines, 1):
        if line.startswith('#'):
            continue
        # Strip trailing spaces
        l_str = line.rstrip()
        if len(l_str) > 36:
            long_lines.append((lineno, len(l_str), l_str))
    
    if long_lines:
        print(f'  [Note] {filename} has {len(long_lines)} lines > 36 chars:')
        for lno, llen, lval in long_lines[:5]:
            print(f'    Line {lno} ({llen} chars): {lval}')
    
    print(f'[VERIFIED] {filename}: 100% ASCII, {len(sec_headers)} sections, {open_tags} tag pairs matched.')

def main():
    print('========================================================')
    print(' Building Late Stages Localizations (Talk28 - talk38)')
    print('========================================================')
    for fname, d in FILE_MAP.items():
        generate_file(fname, d)
    
    print('\n========================================================')
    print(' Verifying Localizations')
    print('========================================================')
    for fname, d in FILE_MAP.items():
        verify_file(fname, d)
    print('\nAll 11 files generated and verified successfully!')

if __name__ == '__main__':
    main()
