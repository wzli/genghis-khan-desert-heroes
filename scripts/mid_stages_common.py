import re
import os

def visible_len(s):
    # Strips game formatting tags %1, %2, %3, %4, %%
    clean = re.sub(r'%[1-4]|%%', '', s)
    return len(clean)

def wrap_text(text, width=32):
    """
    Wraps text paragraphs into lines of visible width ~30-34 characters.
    Preserves deliberate empty lines. Never breaks words.
    """
    if not text:
        return ""
    paras = text.split('\n')
    out_paras = []
    for para in paras:
        stripped = para.strip()
        if not stripped:
            out_paras.append('')
            continue
        words = stripped.split(' ')
        lines = []
        cur_line = []
        cur_vis = 0
        for w in words:
            if not w:
                continue
            w_vis = visible_len(w)
            space_vis = 1 if cur_line else 0
            if cur_vis + space_vis + w_vis <= width or not cur_line:
                cur_line.append(w)
                cur_vis += space_vis + w_vis
            else:
                lines.append(' '.join(cur_line))
                cur_line = [w]
                cur_vis = w_vis
        if cur_line:
            lines.append(' '.join(cur_line))
        out_paras.append('\n'.join(lines))
    return '\n'.join(out_paras)

def build_stage_file(sections, wrap_dialogue=True, dialogue_width=32):
    """
    sections is a list of tuples: (header, content_text)
    header: e.g. '#000//Intro', '#002//Temujin', '#200', etc.
    content_text: string with dialogue or narration.
    """
    lines = []
    for header, content in sections:
        lines.append(header)
        if content is not None and content != "":
            sec_num_match = re.match(r'#(\d+)', header)
            sec_num = int(sec_num_match.group(1)) if sec_num_match else 0
            
            if wrap_dialogue and 2 <= sec_num < 200:
                wrapped = wrap_text(content, width=dialogue_width)
                for l in wrapped.split('\n'):
                    lines.append(l)
            elif sec_num == 1 or sec_num == 99 or sec_num == 0:
                wrapped = wrap_text(content, width=dialogue_width)
                for l in wrapped.split('\n'):
                    lines.append(l)
            else:
                for l in content.split('\n'):
                    lines.append(l)
        lines.append('#')
    return '\n'.join(lines) + '\n'

def verify_file(filepath):
    """
    Verifies that filepath is 100% ASCII, valid formatting, no placeholder questions.
    """
    if not os.path.exists(filepath):
        return False, f"File {filepath} does not exist"
    with open(filepath, 'rb') as f:
        raw = f.read()
    
    try:
        text = raw.decode('ascii')
    except UnicodeDecodeError as e:
        return False, f"Non-ASCII character detected: {e}"
    
    if '??' in text:
        return False, "Found '??' placeholder sequence"
    
    lines = text.splitlines()
    sec_count = 0
    for l in lines:
        if l.startswith('#') and l != '#':
            sec_count += 1
            
    return True, f"OK ({sec_count} sections, {len(text)} chars, 100% ASCII)"
