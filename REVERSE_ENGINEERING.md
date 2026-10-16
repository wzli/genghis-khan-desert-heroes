# Technical Reverse Engineering & Binary Architecture: Genghis Khan (成吉思汗之大漠英雄傳)

This document provides a technical disassembly and reverse-engineering reference for the 2001/1999 Windows game **成吉思汗之大漠英雄傳** (*Genghis Khan: Desert Heroes*, executable `Hero.exe`).

All analyses were performed using static binary disassembly, dynamic tracing under Wine/GDB, and custom Python instrumentation.

---

## 1. Executable Environment & Binary Profile

| Property | Value / Specification |
| :--- | :--- |
| **Binary Name** | `Hero.exe` |
| **Format** | Win32 Portable Executable (PE32, x86 32-bit) |
| **Subsystem** | Windows GUI (`IMAGE_SUBSYSTEM_WINDOWS_GUI`) |
| **Compiler / Toolchain** | Microsoft Visual C++ 6.0 (MSVC 6.0, SP3/SP4) |
| **Image Base (VA)** | `0x00400000` |
| **Entry Point (OEP)** | `0x00473cf0` (File offset `0x73cf0`) |
| **Section Alignment** | `0x1000` (4096 bytes) |
| **File Alignment** | `0x1000` (Direct 1:1 mapping between Virtual Address and File Offset) |
| **Primary Sections** | `.text` (`0x401000` - `0x480000`, 508 KB), `.rdata` (`0x480000` - `0x498000`), `.data` (`0x498000` - `0x4c2000`), `.rsrc` (`0x4c2000` - `0x4cb000`) |

---

## 2. Text Rendering Engine & ASCII Variable Font Spacing

### Background
In the original 1999 engine, all in-game text rendering was built strictly for double-byte Big-5 Traditional Chinese characters ($24 \times 24$ pixels). Single-byte ASCII English strings suffered from hardcoded monospacing where every single letter was spaced 24 pixels apart (e.g. `M o t h e r   o f   m y   s o n`), causing extreme visual fragmentation and severe line overflow.

### Disassembly Analysis (`0x0046ce0f`)
The font rasterization function at virtual address `0x46ce0f` calculates the horizontal screen coordinate $X$ for character glyphs:

```asm
; Original MSVC arithmetic at 0x46ce0f (File offset 0x6ce0f):
0046ce0f: 8d 04 40        lea    eax, [eax + eax*2]    ; eax = col * 3
0046ce12: 8d 0c c1        lea    ecx, [ecx + eax*8]    ; ecx = base_x + (col * 3) * 8 = base_x + col * 24
```

### The 12px ASCII Font Patch
To enable proportional ASCII text rendering in English mode, the stride multiplier was halved from 24 pixels to 12 pixels, doubling dialogue character capacity per line:

```asm
; Patched arithmetic at 0x46ce12 in Hero.exe.en:
0046ce12: 8d 0c 81        lea    ecx, [ecx + eax*4]    ; ecx = base_x + (col * 3) * 4 = base_x + col * 12
```

### Line Wrap & Buffer Capacities
To prevent text from truncating at the original Chinese 17-character limit, line wrap boundaries and loop comparison registers were updated:

| Virtual Address | File Offset | Original Bytes | Patched Bytes | Purpose |
| :--- | :--- | :--- | :--- | :--- |
| `0x0046ce12` | `0x6ce12` | `8d 0c c1` | `8d 0c 81` | Character step advance: $24\text{px} \to 12\text{px}$ |
| `0x0046caef + 3` | `0x6caf2` | `11` | `22` | Max characters per line without portrait: $17 \to 34$ |
| `0x0046cb0c + 3` | `0x6cb0f` | `11` | `22` | Loop boundary check: $17 \to 34$ |
| `0x0046cb1c + 3` | `0x6cb1f` | `0c` | `18` | Max characters per line with portrait: $12 \to 24$ |
| `0x0046cc6c + 2` | `0x6cc6e` | `11` | `22` | Wrap jump threshold: $17 \to 34$ |
| `0x0046cdd0 + 2` | `0x6cdd2` | `11` | `22` | Formatting buffer index: $17 \to 34$ |

---

## 3. Unit Picking Bounds Crash Fix (VA `0x00420bd5`)

### Bug Description & Root Cause
During combat (especially when paused or clicking near map boundaries, minimap, UI bars, or empty viewport borders), the game abruptly crashed with a fatal page fault:

```
Unhandled exception: page fault on read access to 0xfefc8bcb in 32-bit code (0x00420bd5).
Register dump: EAX:005409d3 ECX:05bfe670 EDX:fefc8bbc
Backtrace: => 0x00420bd5 in hero: testb $1, 0xf(%edx)
```

At `0x420b60`, the tactical hit-tester converts mouse coordinates $(x, y)$ into a linear tile index:
$$\text{TileIndex} = (Y_{\text{tile}} \times \text{Stride}) + X_{\text{tile}} + \text{Base}$$

At `0x420bd2` (file offset `0x20bd2`), the engine executed:
```asm
00420bd2: 8b 0c 81        mov    (%ecx, %eax, 4), %edx ; edx = tile_array[eax] (NO BOUNDS CHECK!)
00420bd5: f6 42 0f 01     testb  $0x1, 0xf(%edx)       ; DEREFERENCES [edx + 0xf] (NO NULL/SANITY CHECK!)
```

When clicking off-map or while paused, `%eax` held an invalid integer (`0x005409d3` $\approx 5.5\times 10^6$), causing `%edx` to read unmapped memory (`0xfefc8bbc`). The subsequent dereference `0xf(%edx)` triggered an immediate segmentation violation.

### The Code Cave Bounds Guard (`0x0047f480`)
A 19-byte detour hook was placed at `0x420bcc` redirecting to an unused padding cave in `.text` at `0x47f480`:

```asm
; Code Cave at VA 0x0047f480 (File Offset 0x7f480):
0047f480: 85 c9                 test   %ecx, %ecx            ; Is array pointer valid?
0047f482: 74 20                 je     0x47f4a4              ; Fail -> safe exit
0047f484: 85 c0                 test   %eax, %eax            ; Is index negative?
0047f486: 78 1c                 js     0x47f4a4              ; Fail -> safe exit
0047f488: 3d 00 00 10 00        cmp    $0x100000, %eax       ; Is index within max map bound?
0047f48d: 73 15                 jae    0x47f4a4              ; Fail -> safe exit
0047f48f: 8b 14 81              mov    (%ecx, %eax, 4), %edx ; Safely fetch pointer
0047f492: 85 d2                 test   %edx, %edx            ; Is pointer null?
0047f494: 74 0e                 je     0x47f4a4              ; Fail -> safe exit
0047f496: 81 fa 00 00 01 00     cmp    $0x10000, %edx        ; Is pointer above Windows null page?
0047f49c: 72 06                 jb     0x47f4a4              ; Fail -> safe exit
0047f49e: f6 42 0f 01           testb  $0x1, 0xf(%edx)       ; Safe dereference!
0047f4a2: eb 05                 jmp    0x47f4a9              ; Proceed
0047f4a4: e9 e5 17 fa ff        jmp    0x420c8e              ; Clean no-hit exit path (0x420c8e)
0047f4a9: e9 31 17 fa ff        jmp    0x420bdf              ; Resume normal hit logic (0x420bdf)
```

**Result**: 100% crash elimination across all screen boundaries, dialogue overlays, and pause states.

---

## 4. Mouse Edge Scroll Speed Calibration

### Mechanism
In `WndProc` / `OnMouseMove` (`0x43ef0`), edge collision flags are set when cursor coordinates touch window borders ($x \le 10$, $x \ge 796$, $y \le 2$, $y \ge 596$). The active scroll direction is stored in global `0x4bd358`.

In the main rendering loop at `0x42f6da` (file offset `0x2f6da`):
```asm
0042f6da: 39 1d 58 d3 4b 00     cmp    %ebx, 0x4bd358        ; Is edge scroll active?
0042f6e0: 74 6c                 je     0x42f74e
0042f6e2: 66 83 3d 04 8b 4b 00 03  cmpw $0x3, 0x4b8b04       ; Check multimedia timer ticks
0042f6ea: 72 62                 jb     0x42f74e
0042f6ec: a1 18 d3 4b 00        mov    0x4bd318, %eax
0042f6f1: 66 89 1d 04 8b 4b 00  mov    %bx, 0x4b8b04         ; Reset tick counter
0042f6f8: 39 c3                 cmp    %eax, %ebx
0042f6fa: 74 15                 je     0x42f711
0042f6fc: e8 af e8 fe ff        call   0x42dfb0              ; Advance viewport 1 tile
```

On modern CPUs, a threshold of `3` timer ticks caused violent screen panning.

### The Patch
1. **Tick Threshold** (`0x42f6e9`): `0x03` $\to$ **`0x32` (50 decimal)**. Reduces viewport stepping rate by $\approx 16.7\times$ down to ~1.2 camera steps/second.
2. **Inception Delay** (`0x441ea`): `0x03` $\to$ **`0x0a` (10 ticks)**. Prevents accidental panning when cursor briefly brushes against the border.

Configurable in realtime via `scripts/set_scroll_speed.py`.

---

## 5. Dialogue Auto-Progression Neutralization

In the original game, story dialogues vanished automatically on timer expiration:
- Inter-speaker dialogue timer at `0x46cbac` (`cmpw $0x14, 0x4bd34c`).
- Intra-speech pause timer at `0x46cda4` (`cmpw $0x28, 0x4bd34c`).

### The Patch
Both conditional jumps (`jbe` / `jb`) were neutralised:
- `0x46cbb4`: `76 43` (`jbe +0x43`) $\to$ `90 90` (`NOP NOP`).
- `0x46cdac`: `72 24` (`jb +0x24`) $\to$ `90 90` (`NOP NOP`).

**Result**: Dialogues remain on screen indefinitely until the player explicitly advances with `Space`, `Enter`, or mouse click.

---

## 6. Speed Control & Keyboard Hotkey Code Cave (`0x0047f456`)

The game engine natively supports three simulation speeds (Slow, Normal, Fast) via global variable `0x4aef70`. However, the original keyboard handler only listened for Numpad keys (`VK_ADD` `0x6B` and `VK_SUBTRACT` `0x6D`), ignoring top-row `+` and `-` keys on laptops and 60%/75% keyboards.

### The Code Cave (`0x0047f456`)
Installed an intercept hook in `WndProc` at `0x431ac` translating top-row keycodes:
```asm
; Intercept at VA 0x0047f456 (File offset 0x7f456):
0047f456: 83 f8 3d              cmp    $0x3d, %eax           ; '=' / '+' top-row key
0047f459: 74 0b                 je     0x47f466              ; Translate to speed up
0047f45b: 83 f8 bd              cmp    $0xbd, %eax           ; '-' / '_' top-row key
0047f45e: 74 0b                 je     0x47f46b              ; Translate to speed down
0047f460: 3d bb 00 00 00        cmp    $0xbb, %eax           ; OEM_PLUS key
0047f465: c3                    ret
0047f466: b8 6b 00 00 00        mov    $0x6b, %eax           ; Map to VK_ADD
0047f46b: b8 6d 00 00 00        mov    $0x6d, %eax           ; Map to VK_SUBTRACT
0047f470: c3                    ret
```

---

## 7. CD-ROM Disc 2 DRM Bypass (`0x004331e0`)

The original game queried `GetDriveTypeA` and searched for a physical volume labeled `成吉思汗第二片光碟`. If missing, it displayed a modal error and terminated:

```asm
; Original at 0x004331e0 (File offset 0x331e0):
004331e0: 85 c0                 test   %eax, %eax
004331e2: 75 1a                 jne    0x4331fe              ; Error jump if CD missing
```

### The Patch
```asm
004331e0: 90 90                 nop    nop
004331e2: 90 90                 nop    nop
```
The routine is forced to return success (`%eax = 1`), enabling 100% portable drive play without requiring disc images or virtual CD-ROM drives.

---

## 8. Proprietary Binary File Formats

### A. `stage.ini` (General & Unit Database)
- **File Size**: Fixed 127,240 bytes.
- **Roster Structure**:
  - `0x000000 - 0x0198c0`: **396 General Records** (264 bytes/record).
    - Offset `0x00`: `char name[20]` (Null-terminated string).
    - Offset `0x14`: `uint16_t portrait_id`.
    - Offset `0x16`: `uint8_t leadership`, `strength`, `intelligence`, `politics`.
    - Offset `0x20`: Troop company capacity and specialization flags.
  - `0x0198c0 - 0x01aae0`: **34 Castle Records** (136 bytes/record).
  - `0x01aae0 - 0x01d0a0`: **110 Soldier / Regiment Records** (88 bytes/record).
  - `0x01d0a0 - 0x01f108`: **24 Magic Spells & 59 Inventory Items**.

### B. `windows.dat`, `selects.dat`, `netgraphics.dat` (Sprite Archives)
- **Header Structure**:
  - `uint32_t num_sprites`: Total count of graphic elements.
  - `uint32_t index_table[num_sprites]`: Absolute file offset table for each sprite record.
- **Sprite Record Structure**:
  - `int16_t width, height`: Dimensions.
  - `int16_t hotspot_x, hotspot_y`: Anchor coordinates.
  - `uint8_t encoding`: RLE compressed or linear indexed 8-bit palette pixels.
- **Palette**: Master 256-color palette with transparent index `0x00` (cyan key `RGB(0, 255, 255)`).
