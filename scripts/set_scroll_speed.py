#!/usr/bin/env python3
import sys, os

BIN_PATHS = [
    'assets/game/Hero.exe',
    'assets/game/Hero.exe.en',
    'assets/game/Hero.exe.zh'
]

THRESH_OFF = 0x2f6e9
INCEPT_OFF = 0x441ea

PRESETS = {
    'fast': (16, 5),       # moderate panning
    'normal': (25, 6),     # calm
    'slow': (35, 8),       # very slow (~12x slower than original)
    'gentle': (50, 10),    # ultra gentle (~17x slower than original, 1 step/sec)
    'crawl': (70, 12),     # micro-nudging
}

def patch_bin(path, thresh, incept=None):
    if not os.path.isfile(path):
        return False
    with open(path, 'rb') as f:
        data = bytearray(f.read())
    
    assert data[0x2f6e2:0x2f6e9] == bytes.fromhex('66833d048b4b00'), f"Invalid header at 0x2f6e2 in {path}"
    old_thresh = data[THRESH_OFF]
    data[THRESH_OFF] = thresh

    old_incept = None
    if incept is not None:
        assert data[0x441e8:0x441ea] == bytes.fromhex('83f9'), f"Invalid header at 0x441e8 in {path}"
        old_incept = data[INCEPT_OFF]
        data[INCEPT_OFF] = incept

    with open(path, 'wb') as f:
        f.write(data)

    incept_str = f", inception delay {old_incept} -> {incept}" if old_incept is not None else ""
    print(f"[{os.path.basename(path)}] Scroll threshold: {old_thresh} -> {thresh} (0x{thresh:02x}){incept_str}")
    return True

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/set_scroll_speed.py <value|preset> [inception_delay]")
        print("Presets:")
        for name, (th, inc) in PRESETS.items():
            print(f"  {name:10s} : threshold={th:2d}, inception={inc}")
        print("\nCurrent settings:")
        for p in BIN_PATHS:
            if os.path.isfile(p):
                with open(p, 'rb') as f:
                    d = f.read()
                print(f"  {p:26s} : threshold={d[THRESH_OFF]} (0x{d[THRESH_OFF]:02x}), inception={d[INCEPT_OFF]}")
        sys.exit(0)

    arg = sys.argv[1].lower()
    incept = int(sys.argv[2]) if len(sys.argv) > 2 else None

    if arg in PRESETS:
        thresh, def_inc = PRESETS[arg]
        if incept is None:
            incept = def_inc
    else:
        try:
            thresh = int(arg)
        except ValueError:
            print(f"Error: unknown preset or invalid number '{arg}'")
            sys.exit(1)

    for p in BIN_PATHS:
        patch_bin(p, thresh, incept)

    print(f"\nSuccessfully updated all game binaries to threshold {thresh} (0x{thresh:02x})!")

if __name__ == '__main__':
    main()
