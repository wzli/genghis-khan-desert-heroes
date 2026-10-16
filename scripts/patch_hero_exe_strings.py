#!/usr/bin/env python3
import os

GAME_DIR = os.path.abspath('assets/game')
HERO_EN = os.path.join(GAME_DIR, 'Hero.exe.en')

REPLACEMENTS = [
    # (offset, zh_string, en_string)
    (0x8d284, "劇本類型", "Scenario"),
    (0x8d278, "戰役選擇", "Campaign"),
    (0x8d270, "遊戲者", "Player"),
    (0x8d264, "君主選擇", "Leader"),
    (0x8d25c, "同盟", "Ally"),
    (0x8d250, "遊戲速度", "Speed"),
    (0x8d244, "城堡資源", "Resource"),
    (0x8d238, "城堡發展", "City Dev"),
    (0x8d228, "顯示地圖", "Show Map"),
    (0x8d220, "難易度", "Diff."),
    (0x8d218, "未設定", "None"),
    (0x8d210, "電腦", "AI"),
    (0x8d204, "我準備好了", "Ready!"),
    (0x8d1fc, "武將數", "Heroes"),
    (0x8d1f0, "城堡等級", "City Lvl"),
    (0x8d1e4, "史實戰役", "History"),
    (0x8d1d8, "虛構戰役", "Fiction"),
    (0x8d1cc, "蒙古的紛亂", "Mongolia"),
    (0x8d1c0, "東亞的沉淪", "E. Asia"),
    (0x8d1b4, "歐亞的浩劫", "Eurasia"),
    (0x880a0, "特殊兵種", "Special"),
    (0x8d290, "請輸入玩家名字", "Player Name:"),
    (0x8d2a0, "請輸入團長名字", "Host Name:"),
    (0x8d2b0, "選擇遊戲團", "Game Group"),
    (0x8d2bc, "連線類別", "Net Type"),
    (0x8d0b0, "快", "Hi"),
    (0x8d0b4, "慢", "Lo"),
    (0x8d0a8, "標準", "Norm"),
    (0x8d0f4, "一般", "Norm"),
    (0x8d108, "普通", "Norm"),
    (0x8d07c, "易", "Ez"),
    (0x8d078, "難", "Hd"),
    (0x8d0fc, "中", "Md"),
    (0x8d11c, "關閉", "Off"),
    (0x8d09c, "視野全開", "All Map"),
    (0x8d090, "標準征服", "Conquest"),
    (0x8d088, "弒君", "King"),
    (0x8d080, "年限", "Time"),
    (0x8d0d0, "全數", "All"),
    (0x8d0ec, "低", "Lo"),
    (0x8d0f0, "高", "Hi"),
    (0x8d100, "少", "Lo"),
    (0x8d104, "大", "Hi"),
    (0x8d110, "小", "Lo"),
    (0x8d114, "極小", "Min"),
    (0x8d1a8, "3城上限3人", "3City-3Max"),
    (0x8d19c, "4城上限4人", "4City-4Max"),
    (0x8d190, "5城上限5人", "5City-5Max"),
    (0x8d184, "6城上限6人", "6City-6Max"),
    (0x8d178, "7城上限7人", "7City-7Max"),
    (0x8d16c, "8城上限8人", "8City-8Max"),
    (0x8d160, "9城上限8人", "9City-8Max"),
    (0x8d154, "10城上限8人", "10City-8Max"),
    (0x8d148, "11城上限8人", "11City-8Max"),
    (0x8d13c, "12城上限8人", "12City-8Max"),
    (0x8d130, "14城上限8人", "14City-8Max"),
    (0x8d124, "16城上限8人", "16City-8Max"),
]

def main():
    if not os.path.exists(HERO_EN):
        print(f"Error: {HERO_EN} not found.")
        return

    with open(HERO_EN, 'rb') as f:
        data = bytearray(f.read())

    count = 0
    for off, zh_s, en_s in REPLACEMENTS:
        zh_bytes = zh_s.encode('big5')
        en_bytes = en_s.encode('latin1')
        total_len = len(zh_bytes)
        # Pad remaining length with 0x00
        padded_en = en_bytes.ljust(total_len, b'\x00')
        data[off:off+total_len] = padded_en
        count += 1

    with open(HERO_EN, 'wb') as f:
        f.write(data)

    print(f"Successfully patched {count} UI strings in {HERO_EN}")

if __name__ == '__main__':
    main()
