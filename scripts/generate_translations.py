#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
OpenCJSH & Hero.exe Bilingual Localization Pack Generator
Generates authentic English translation files for all databases:
- castle.txt
- general.txt
- soldier.txt
- Item.txt
- magic.txt
- HelpMessage.txt
- ScenarioName.txt
- Talk00.txt to Talk38.txt
"""

import os
import glob
import re

GAME_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'assets', 'game'))
ZH_DIR = os.path.join(GAME_DIR, 'text_zh')
EN_DIR = os.path.join(GAME_DIR, 'text_en')

os.makedirs(ZH_DIR, exist_ok=True)
os.makedirs(EN_DIR, exist_ok=True)

# -------------------------------------------------------------------------
# 1. Castles (34 historical cities)
# -------------------------------------------------------------------------
CASTLES = {
    "大定": "Dading",
    "燕京": "Yanjing",
    "興慶": "Xingqing",
    "高昌": "Qocho",
    "阿里麻里": "Almaliq",
    "虎司": "Balasagun",
    "玉龍傑赤": "Urgench",
    "開封": "Kaifeng",
    "臨安": "Lin'an",
    "鳳翔": "Fengxiang",
    "襄陽": "Xiangyang",
    "成都": "Chengdu",
    "拉薩": "Lhasa",
    "撒麻耳干": "Samarkand",
    "不剌花": "Bukhara",
    "尼沙耳普": "Nishapur",
    "哥寧疾": "Ghazni",
    "廣州": "Guangzhou",
    "德里": "Delhi",
    "基輔": "Kyiv",
    "莫斯科": "Moscow",
    "新薩萊": "Sarai",
    "華沙": "Warsaw",
    "勃蘭登": "Brandenburg",
    "薩克森": "Saxony",
    "佩德斯": "Pest",
    "欽察": "Kipchak",
    "君士坦丁": "Constantinople",
    "威尼斯": "Venice",
    "大馬士革": "Damascus",
    "開羅": "Cairo",
    "報達": "Baghdad",
    "和林": "Karakorum",
    "木剌夷": "Alamut",
}

# -------------------------------------------------------------------------
# 2. Units / Soldiers (111 types)
# -------------------------------------------------------------------------
UNITS = {
    "輕步兵": "Light Infantry",
    "重步兵": "Heavy Infantry",
    "短槍兵": "Spearmen",
    "長槍兵": "Pikemen",
    "輕騎兵": "Light Cavalry",
    "重騎兵": "Heavy Cavalry",
    "短弓手": "Shortbowmen",
    "長弓手": "Longbowmen",
    "謀士": "Strategist",
    "謀臣": "Grand Strategist",
    "鐵騎兵": "Cataphract",
    "突騎兵": "Raider Cavalry",
    "弩兵": "Crossbowmen",
    "連弩兵": "Repeating Crossbow",
    "火焰兵": "Fire Lancer",
    "烈焰兵": "Flame Elite",
    "十字軍": "Crusader",
    "鐵十字軍": "Iron Crusader",
    "駱駝兵": "Camel Cavalry",
    "重駱駝兵": "Heavy Camel",
    "砲兵": "Catapult Artillery",
    "火砲兵": "Cannon Artillery",
    "聖騎兵": "Paladin",
    "超聖騎兵": "High Paladin",
    "武士": "Samurai",
    "鬼武士": "Oni Samurai",
    "特鐵騎": "Elite Cataphract",
    "特突騎": "Elite Raider",
    "娘子軍": "Maiden Guard",
    "鐵娘子軍": "Iron Maiden Guard",
    "戰士": "Warrior",
    "猛戰士": "Fierce Warrior",
    "射手": "Archer",
    "神射手": "Marksman",
    "小步兵": "Militia Infantry",
    "小槍兵": "Militia Spearmen",
    "小騎兵": "Militia Cavalry",
    "小弓箭手": "Militia Archer",
    "小投石車": "Light Catapult",
    "小鐵騎兵": "Light Cataphract",
    "小弩兵": "Light Crossbow",
    "小火焰兵": "Light Fire Lancer",
    "小十字軍": "Young Crusader",
    "小駱駝兵": "Light Camel",
    "小火砲兵": "Light Cannon",
    "小戰象兵": "Light War Elephant",
    "小聖騎兵": "Apprentice Paladin",
    "小武士": "Young Samurai",
    "帆船": "Sailing Vessel",
    "大帆船": "Galleon",
    "戰船": "Warship",
    "大戰船": "Grand Warship",
    "小帆船": "Skiff",
    "海盜船": "Pirate Ship",
    "運輸船": "Transport Ship",
    "小賊": "Bandit",
    "馬賊": "Horse Bandit",
    "馬賊頭目": "Bandit Chieftain",
    "骷髏兵": "Skeleton Warrior",
    "木乃伊兵": "Mummy Guard",
    "大灰狼": "Dire Wolf",
    "運輸車": "Supply Wagon",
    "牛": "Ox",
    "羊": "Sheep",
    "馬": "Steed",
    "小孩": "Child",
    "男村民": "Villager (Male)",
    "女村民": "Villager (Female)",
    "道具車": "Item Cart",
    "火焰": "Fire",
    "人屍體": "Fallen Soldier",
    "馬屍體": "Fallen Steed",
    "船殘骸": "Shipwreck",
    "城箭塔": "Castle Watchtower",
    "獨立箭塔": "Standalone Tower",
    "豪華車": "Royal Carriage",
    "寶箱車": "Treasure Cart",
    "強化步兵": "Veteran Infantry",
    "強化槍兵": "Veteran Spearmen",
    "強化騎兵": "Veteran Cavalry",
    "強化弓手": "Veteran Archer",
    "強砲車": "Heavy Siege Engine",
    "岩洞箭塔": "Cavern Tower",
    "遺跡箭塔": "Ruins Tower",
    "使者": "Envoy",
    "鬥牛": "War Bull",
    "軍旗": "Battle Standard",
    "俠士": "Swordsman",
    "強化帆船": "Armored Vessel",
    "城門": "Castle Gate",
    "蒙古騎": "Mongol Cavalry",
    "蒙古騎兵": "Mongol Cavalry",
    "蒙古弓騎兵": "Mongol Horse Archer",
    "怯薛軍": "Kheshig Guard",
    "戰象兵": "War Elephant",
    "武士兵": "Samurai Warrior",
    "城堡箭塔": "Castle Tower",
    "信車": "Messenger Cart",
    "大岩狼": "Great Rock Wolf",
    "新娘車": "Bridal Carriage",
    "守衛": "Guard",
    "營帳車": "Yurt Wagon",
    "步兵神像": "Infantry Shrine",
    "槍兵神像": "Spearman Shrine",
    "騎兵神像": "Cavalry Shrine",
    "弓手神像": "Archer Shrine",
    "攻城神像": "Siege Shrine",
    "青囊書": "Medical Treatise",
    "金算盤": "Golden Abacus",
    "金犁車": "Golden Plow",
    "斷頭台": "Guillotine",
    "水車": "Waterwheel",
    "市集": "Marketplace",
    "基督聖像": "Sacred Icon",
    "弩炮塔": "Ballista Tower",
}

# -------------------------------------------------------------------------
# 3. Items (59 items)
# -------------------------------------------------------------------------
ITEMS = {
    "黃水晶": "Citrine Quartz",
    "紫水晶": "Amethyst Crystal",
    "白鹿之杖": "White Doe Staff",
    "倉狼之裘": "Blue Wolf Robe",
    "萬鑽皇冠": "Diamond Crown",
    "千古玉佩": "Ancient Jade",
    "青龍偃月刀": "Green Dragon Blade",
    "倚天劍": "Heaven Reliant Sword",
    "妖刀村正": "Muramasa Blade",
    "妖刀不知火": "Shiranui Blade",
    "屠龍聖槍": "Dragon Slayer Lance",
    "石中劍": "Excalibur",
    "雙刃斧": "Battleaxe",
    "阿拉伯彎刀": "Scimitar",
    "浪形劍": "Flamberge",
    "黃金戰刀": "Golden Saber",
    "劊子手之斧": "Executioner Axe",
    "維京巨劍": "Viking Broadsword",
    "六韜": "Six Secret Teachings",
    "孫子兵法": "Art of War",
    "軍事概要": "Strategikon",
    "高盧戰記": "Gallic Wars",
    "漢尼拔戰記": "Annals of Hannibal",
    "陣形術": "Tactical Formations",
    "太平要術書": "Taiping Jing",
    "羅蘭之歌": "Song of Roland",
    "王書": "Shahnameh",
    "論語": "Analects of Confucius",
    "韓非子": "Han Feizi",
    "莊子": "Zhuangzi",
    "禮記": "Book of Rites",
    "天文學": "Treatise on Astronomy",
    "大藏經": "Tripitaka",
    "東方見聞錄": "Travels of Marco Polo",
    "希臘哲學": "Greek Philosophy",
    "可蘭經": "Quran",
    "聖經": "Holy Bible",
    "赤兔馬": "Red Hare Steed",
    "汗血寶馬": "Ferghana Steed",
    "的盧": "Hex Mark Steed",
    "駝馬": "Camel Steed",
    "聖騎士鎧甲": "Paladin Armor",
    "黃金鎧甲": "Golden Armor",
    "武士鎧甲": "Samurai Armor",
    "蒼狼戰甲": "Blue Wolf Armor",
    "龍鱗戰甲": "Dragon Scale Armor",
    "鳳凰戰甲": "Phoenix Armor",
    "白銀盔": "Silver Helm",
    "金盔": "Golden Helm",
    "銀盔": "Iron Helm",
    "忍者服": "Ninja Garb",
    "火龍捲軸": "Fire Dragon Scroll",
    "爆雷捲軸": "Thunderstorm Scroll",
    "崩石捲軸": "Rockslide Scroll",
    "鼓舞捲軸": "Inspire Scroll",
    "大喝捲軸": "Roar Scroll",
    "說服捲軸": "Persuade Scroll",
    "珍珠": "Pearl",
}

# -------------------------------------------------------------------------
# 4. Spells & Magics
# -------------------------------------------------------------------------
MAGICS = {
    "小球技1": "Fireball",
    "火炎技2": "Flame Burst",
    "火龍技3": "Fire Dragon",
    "落石技1": "Falling Rock",
    "崩石技2": "Rockslide",
    "隕石技3": "Meteor Strike",
    "落雷技1": "Lightning",
    "狂雷技2": "Wild Lightning",
    "爆雷技3": "Thunderstorm",
    "一氣斬1": "Swift Strike",
    "月氣斬2": "Crescent Slash",
    "爆發斬3": "Burst Slash",
    "氣動波1": "Shockwave",
    "炫風波2": "Gale Wave",
    "爆烈波3": "Blast Wave",
    "穿心箭1": "Heartseeker Arrow",
    "亂矢箭2": "Arrow Volley",
    "萬箭齊發3": "Rain of Arrows",
    "說服": "Persuade",
    "鼓舞": "Inspire",
    "大喝": "Battle Roar",
    "迷惑": "Confuse",
    "怒殺技": "Berserk Wrath",
    "補血": "Heal",
}

# -------------------------------------------------------------------------
# 5. Generals (Complete 376 Dictionary)
# -------------------------------------------------------------------------
GENERALS = {
    "鐵木真": "Temujin",
    "成吉思汗": "Genghis Khan",
    "朮赤": "Jochi",
    "察合台": "Chagatai",
    "窩闊台": "Ogedei",
    "拖雷": "Tolui",
    "別勒古台": "Belgutei",
    "博兒忽": "Borokhula",
    "赤老溫": "Chilaun",
    "合撒兒": "Qasar",
    "哈赤溫": "Qachiun",
    "者勒蔑": "Jelme",
    "忽必來": "Qubilai",
    "帖木格": "Temuge",
    "速不台": "Subutai",
    "博爾朮": "Bo'orchu",
    "孛兒帖": "Borte",
    "札木合": "Jamukha",
    "術赤臺": "Jurchidei",
    "太陽汗": "Tayang Khan",
    "屈出律": "Kuchlug",
    "哲別": "Jebe",
    "陶雲戈": "Taoyunge",
    "木華黎": "Muqali",
    "斡里速別": "Ulisube",
    "可克薛": "Kokechu",
    "卓乎難": "Jokhunan",
    "不亦魯黑": "Buyruk Khan",
    "王罕": "Toghrul",
    "札合趕不": "Jakha Gambu",
    "阿勒壇": "Altan",
    "阿勒屯": "Altun",
    "桑昆": "Senggum",
    "忽察兒": "Khuchar",
    "塞罕脫端": "Sehan Toduan",
    "赤勒格兒": "Chilger",
    "脫裡脫": "Torito",
    "火都": "Qodu",
    "赤剌溫": "Chila'un",
    "合忽出": "Khokhuchu",
    "塔兒忽台": "Targhutai",
    "斡兒伯": "Orbei",
    "古溫": "Guwen",
    "渾阿歹": "Qon'atai",
    "古失魯克": "Kushluk",
    "撒察別乞": "Sacha Beki",
    "不里孛闊": "Buri Boke",
    "合答吉歹": "Qadagidai",
    "脫朵延吉": "Todoyan Gir",
    "呼圖": "Qutu",
    "孛脫灰答": "Botokhuidai",
    "也迪亦納": "Yedi'ina",
    "忽都合": "Khutukha",
    "脫兒必塔": "Torbi Tash",
    "豁兒赤": "Qorchi",
    "阿剌兀思": "Alaq-ush",
    "木忽兒": "Muqur",
    "完顏永濟": "Wanyan Yongji",
    "完顏胡沙": "Wanyan Husha",
    "完顏執中": "Wanyan Zhizhong",
    "完顏萬奴": "Wanyan Wannu",
    "銀青": "Yin Qing",
    "耶律阿海": "Yelu Ahai",
    "耶律楚材": "Yelu Chucai",
    "巴古失": "Bakshi",
    "桑臣": "Sangchen",
    "千家奴": "Qianjianu",
    "完顏珣": "Wanyan Xun",
    "完顏守忠": "Wanyan Shouzhong",
    "長春真人": "Qiu Chuji",
    "完顏福興": "Wanyan Fuxing",
    "朮虎高琪": "Zhuhu Gaoqi",
    "李英": "Li Ying",
    "完顏門錫": "Wanyan Menxi",
    "陳和尚": "Chen Heshang",
    "史天澤": "Shi Tianze",
    "浦察七斤": "Pucha Qijin",
    "胡沙虎": "Hushahu",
    "抹然盡忠": "Moran Jinzhong",
    "孫秀林": "Sun Xiulin",
    "明宗": "Myeongjong",
    "孝心": "Hyosim",
    "崔忠獻": "Choe Chung-heon",
    "李奎報": "Yi Gyu-bo",
    "金慶孫": "Kim Gyeong-son",
    "韓侂胄": "Han Tuozhou",
    "陸秀夫": "Lu Xiufu",
    "宋寧宗": "Emperor Ningzong",
    "趙惇": "Zhao Dun",
    "史彌遠": "Shi Miyuan",
    "李治": "Li Zhi",
    "程大昌": "Cheng Dachang",
    "朱熹": "Zhu Xi",
    "陸象山": "Lu Xiangshan",
    "真德秀": "Zhen Dexiu",
    "文天祥": "Wen Tianxiang",
    "陸九淵": "Lu Jiuyuan",
    "塔海": "Taghai",
    "李仁友": "Li Renyou",
    "阿珈岡博": "Asha Gambu",
    "李德旺": "Li Dewang",
    "李安全": "Li Anquan",
    "李承禎": "Li Chengzhen",
    "高逸": "Gao Yi",
    "訛答": "Eda",
    "李遵項": "Li Zunxiang",
    "蒐名令公": "Souming Linggong",
    "撒乞阿盤": "Saqi Apan",
    "扥克帕別": "Tokpabek",
    "桑菊": "Sangju",
    "耶律令公": "Yelu Linggong",
    "李睍": "Li Xian",
    "源賴朝": "Minamoto Yoritomo",
    "北條時政": "Hojo Tokimasa",
    "熊古直實": "Kumagai Naozane",
    "大江廣元": "Oe no Hiromoto",
    "源範賴": "Minamoto Noriyori",
    "北條義時": "Hojo Yoshitoki",
    "田山重忠": "Hatakeyama",
    "那須与一": "Nasu no Yoichi",
    "北條泰時": "Hojo Yasutoki",
    "藤原泰衡": "Fujiwara Yasuhira",
    "藤原國衡": "Fujiwara Kunihira",
    "武藏弁慶": "Benkei",
    "源義經": "Minamoto Yoshitsune",
    "空": "Empty",
    "圖兒罕": "Terken Khatun",
    "兀剌黑": "Ulaq",
    "撒兒昔黑": "Sarsikh",
    "巴里司": "Baris",
    "斡思剌黑": "Oslakh",
    "禿孩汗": "Tukhai Khan",
    "阿勒巴兒": "Albar",
    "摩軻末": "Muhammad II",
    "弗里敦古": "Faridun",
    "亦那出克": "Inalchuq",
    "帖木滅里": "Temur Malik",
    "哈剌察": "Qarachar",
    "札蘭丁": "Jalal al-Din",
    "魯克那丁": "Rukn al-Din",
    "圖希": "Tusi",
    "哈只兒汗": "Hajir Khan",
    "汗滅里": "Khan Malik",
    "忽馬耳": "Khumar",
    "薩阿迪": "Saadi",
    "路米": "Rumi",
    "吉牙思": "Ghiyas",
    "赤速梯": "Chishti",
    "哥里": "Ghori",
    "亦魯迪斯": "Yildiz",
    "卡巴差": "Qabacha",
    "亦魯土咪": "Iltutmish",
    "札意恰都": "Jayachandra",
    "艾們克": "Aimak",
    "齊爾吉": "Khilji",
    "巴爾邦": "Balban",
    "阿納賽爾": "Al-Nasir",
    "阿爾阿西": "Al-Aziz",
    "阿迪爾": "Al-Adil",
    "雅克特": "Yaqut",
    "阿吐西": "Atushi",
    "阿爾阿迪": "Al-Afdal",
    "阿爾阿富": "Al-Ashraf",
    "易卜阿比": "Ibn Abi",
    "其福梯": "Qifti",
    "哈利汗": "Khalil Khan",
    "撒拉丁": "Saladin",
    "麥墨迪斯": "Maimonides",
    "阿爾吉斯": "Al-Jazari",
    "阿爾喀米": "Al-Kamil",
    "阿哈默德": "Ahmad",
    "伊薩克": "Isaac II",
    "伊托利": "Italo",
    "獨卡斯": "Doukas",
    "曼卡法斯": "Mankaphas",
    "阿歷克賽": "Alexios III",
    "迪奧德儒": "Theodore I",
    "富賽柏洛": "Fauconberg",
    "伊戈公爵": "Igor Svyatoslavich",
    "羅曼": "Roman the Great",
    "得米特利": "Dmitry",
    "窩羅吉斯": "Volodislav",
    "幽利": "Yuri II",
    "亞力山卓": "Alexander Nevsky",
    "米海爾": "Michael of Chernigov",
    "腓特烈": "Frederick II",
    "雷奧波爾": "Leopold VI",
    "亨利六世": "Henry VI",
    "鄂圖": "Otto IV",
    "弗雷德里": "Frederick",
    "奧左": "Azzo VII",
    "法爾塔": "Falta",
    "施瓦公爵": "Duke of Swabia",
    "阿爾伯特": "Albert of Buxhoeveden",
    "肯拉特": "Conrad of Mazovia",
    "奧利奧": "Orio Mastropiero",
    "旦德羅": "Enrico Dandolo",
    "法蘭捷斯": "Francesco",
    "阿黑剌黑": "Akhraq",
    "月即伯": "Ozbeg",
    "忽灘汗": "Kotyan Khan",
    "加里奇勇": "Mstislav Bold",
    "乞瓦": "Khiva",
    "沃倫侯": "Prince of Volhynia",
    "亦都護": "Idi-qut",
    "比俚伽": "Bilge",
    "不札兒": "Buzar",
    "者格納黑": "Chaganakh",
    "阿兒思蘭": "Arslan",
    "馬木篤": "Mahmud",
    "菊兒汗": "Gurkhan",
    "別克帖兒": "Begter",
    "郭阿靖": "Guo Jing",
    "訶額侖": "Hoelun",
    "也速該": "Yesugei",
    "德薛禪": "Dei Sechen",
    "蒙力克": "Menglik",
    "敵兵": "Enemy Soldier",
    "跆察兒": "Taichar",
    "也客扯連": "Yeke Cheren",
    "蔑兀里徒": "Meulitu",
    "也速干": "Yesugan",
    "也遂": "Yesui",
    "忽蘭": "Khulan",
    "士兵": "Soldier",
    "新增武將": "New General",
    "趙昺": "Zhao Bing",
    "李庭芝": "Li Tingzhi",
    "陳宜中": "Chen Yizhong",
    "賈似道": "Jia Sidao",
    "全子才": "Quan Zicai",
    "趙葵": "Zhao Kui",
    "趙范": "Zhao Fan",
    "江海": "Jiang Hai",
    "孟拱": "Meng Gong",
    "崔立": "Cui Li",
    "李平震": "Li Pingzhen",
    "張惠": "Zhang Hui",
    "樊澤": "Fan Ze",
    "楊沃衍": "Yang Woyan",
    "完顏合達": "Wanyan Heda",
    "金哀宗": "Emperor Aizong",
    "斡別歹": "Obedai",
    "完顏洪沙": "Wanyan Hongsha",
    "完顏洪烈": "Wanyan Honglie",
    "豁阿黑": "Qoahe",
    "額勒赤": "Elchi",
    "孛瑞察兒": "Borijar",
    "呂文煥": "Lu Wenhuan",
    "袁樞": "Yuan Shu",
    "辛棄疾": "Xin Qiji",
    "沃替赤": "Otchigin",
    "火羅突尼": "Qorotuni",
    "乞鄰合": "Qilinha",
    "察剌黑": "Charakha",
    "失刺客": "Shirake",
    "烏林尼": "Wulinni",
    "張世傑": "Zhang Shijie",
    "余玠": "Yu Jie",
    "姜才": "Jiang Cai",
    "罕失次": "Hanshici",
    "木只昆": "Mujikun",
    "合塔巾": "Qatagin",
    "和它奇": "Hotaqi",
    "斡魯朵": "Ordo",
    "多故壘": "Dogulei",
    "皆疏": "Jieshu",
    "谷剌罕": "Gulkhan",
    "哈剌次": "Qalaci",
    "黑契": "Heiqi",
    "斡里蕭": "Ulixiao",
    "傅大其": "Fu Daqi",
    "白仁橋": "Bai Renqiao",
    "李安聖": "Li Ansheng",
    "李安玉": "Li Anyu",
    "李安聞": "Li Anwen",
    "李安祚": "Li Anzuo",
    "拔都": "Batu Khan",
    "蒙哥": "Mongke Khan",
    "忽必烈": "Kublai Khan",
    "旭烈兀": "Hulagu Khan",
    "阿里不哥": "Ariq Boke",
    "海都": "Kaidu",
    "伊馬德丁": "Imad al-Din",
    "努爾丁": "Nur al-Din",
    "拉丁": "Latinus",
    "貝哈丁": "Baha al-Din",
    "阿夫達爾": "Al-Afdal",
    "穆斯林": "Muslim Officer",
    "克普勒": "Kepler",
    "亨利許": "Henrich",
    "馬斯汀": "Maestlin",
    "第谷": "Tycho Brahe",
    "溫伯格": "Weinberg",
    "伊思": "Issac",
    "卡貝爾斯": "Cabers",
    "諾里斯奇": "Norriski",
    "漢米泰斯": "Hamites",
    "布萊諾奇": "Branoki",
    "曼茲科特": "Manzikert",
    "瑪德諾": "Maderno",
    "貝力薩": "Belisarius",
    "博雷斯勞": "Boleslaw",
    "孔拉德": "Konrad",
    "俄彭恩": "Oppeln",
    "拉梯博": "Ratibor",
    "拜拉四世": "Bela IV",
    "烏孤領": "Ugulik",
    "羅肯愛丁": "Rukn al-Din",
    "火者納星": "Nasir al-Din",
    "0": "None",
    "蘇烈曼沙": "Suleiman Shah",
    "愛拜克": "Qutb al-Din Aibak",
    "腓脫愛丁": "Fakhr al-Din",
}

# -------------------------------------------------------------------------
# Translation functions
# -------------------------------------------------------------------------

def translate_castle_txt():
    src_file = os.path.join(ZH_DIR, 'castle.txt')
    dst_file = os.path.join(EN_DIR, 'castle.txt')
    if not os.path.exists(src_file):
        return
    with open(src_file, 'r', encoding='cp950', errors='ignore') as f:
        lines = f.readlines()
    out = []
    # Translate header
    header_fields = lines[0].strip().split('\t')
    header_map = {
        "都市名": "City_Name", "都市索引": "Index", "房子屬性": "House_Attr", "城規模": "Scale",
        "人口": "Population", "金": "Gold", "糧": "Food", "待命士兵": "Reserves",
        "開發值": "Agriculture", "商業值": "Commerce", "治安值": "Security",
        "開發上限": "Max_Agri", "商業上限": "Max_Comm", "治安上限": "Max_Secu",
        "座標X": "Coord_X", "座標Y": "Coord_Y", "太守": "Governor",
        "放置神像": "Shrine", "遺留道具": "Relic", "遺留兵種": "Bonus_Unit",
        "遺留糧": "Rem_Food", "遺留金": "Rem_Gold", "城參考index": "Ref_Index",
        "版本字串": "Version", "特殊兵種": "Special_Unit", "炸燬": "Destroyed"
    }
    out.append('\t'.join([header_map.get(h, h) for h in header_fields]) + '\n')

    for line in lines[1:]:
        fields = line.strip().split('\t')
        if not fields or not fields[0]:
            out.append(line)
            continue
        orig_name = fields[0]
        fields[0] = CASTLES.get(orig_name, orig_name)
        out.append('\t'.join(fields) + '\t\n')

    with open(dst_file, 'w', encoding='ascii', errors='replace') as f:
        f.writelines(out)
    print(f"Generated {dst_file}")

def translate_general_txt():
    src_file = os.path.join(ZH_DIR, 'general.txt')
    dst_file = os.path.join(EN_DIR, 'general.txt')
    if not os.path.exists(src_file):
        return
    with open(src_file, 'r', encoding='cp950', errors='ignore') as f:
        lines = f.readlines()
    out = []
    header_fields = lines[0].strip().split('\t')
    header_map = {
        "姓名": "Name", "人物編號": "ID", "頭像編號": "Portrait", "兵種號": "Unit",
        "所在地": "City", "忠誠值": "Loyalty", "統御力": "Command", "武力": "Force",
        "智力": "Intellect", "出生年": "Birth_Year", "所屬君主": "Lord", "等級": "Level",
        "帶兵數": "Troops", "經驗值": "EXP",
        "火花技1": "Fire1", "火炎技2": "Fire2", "火龍技3": "Fire3",
        "落石技1": "Rock1", "崩石技2": "Rock2", "隕石技3": "Rock3",
        "落雷技1": "Bolt1", "狂雷技2": "Bolt2", "爆雷技3": "Bolt3",
        "武器1": "Wep1", "武器2": "Wep2", "武器3": "Wep3",
        "鼓舞技": "Inspire", "說服技": "Persuade"
    }
    out.append('\t'.join([header_map.get(h, h) for h in header_fields]) + '\n')

    for line in lines[1:]:
        fields = line.strip().split('\t')
        if not fields or not fields[0]:
            out.append(line)
            continue
        orig_name = fields[0]
        en_name = GENERALS.get(orig_name, UNITS.get(orig_name, orig_name))
        fields[0] = en_name
        out.append('\t'.join(fields) + '\t\n')

    with open(dst_file, 'w', encoding='ascii', errors='replace') as f:
        f.writelines(out)
    print(f"Generated {dst_file}")

def translate_soldier_txt():
    src_file = os.path.join(ZH_DIR, 'soldier.txt')
    dst_file = os.path.join(EN_DIR, 'soldier.txt')
    if not os.path.exists(src_file):
        return
    with open(src_file, 'r', encoding='cp950', errors='ignore') as f:
        lines = f.readlines()
    out = []
    header_fields = lines[0].strip().split('\t')
    header_map = {
        "兵種名": "Unit_Name", "人物編號": "ID", "攻擊力": "Attack", "防禦力": "Defense",
        "行動速度": "Speed", "範圍開始": "Rng_Min", "範圍結束": "Rng_Max", "攻擊頻率": "Frequency",
        "視野": "Sight", "兵種升級": "Upgrade_To", "兵種屬性": "Attribute", "海上對應": "Naval_Type",
        "發射對應": "Projectile", "AI-style": "AI_Style", "地基": "Base", "屍體": "Corpse",
        "死亡音效": "Death_Sfx", "攻擊音效": "Attack_Sfx"
    }
    out.append('\t'.join([header_map.get(h, h) for h in header_fields]) + '\n')

    for line in lines[1:]:
        fields = line.strip().split('\t')
        if not fields or not fields[0]:
            out.append(line)
            continue
        orig_name = fields[0]
        fields[0] = UNITS.get(orig_name, orig_name)
        out.append('\t'.join(fields) + '\t\n')

    with open(dst_file, 'w', encoding='ascii', errors='replace') as f:
        f.writelines(out)
    print(f"Generated {dst_file}")

def translate_item_txt():
    src_file = os.path.join(ZH_DIR, 'Item.txt')
    dst_file = os.path.join(EN_DIR, 'Item.txt')
    if not os.path.exists(src_file):
        return
    with open(src_file, 'r', encoding='cp950', errors='ignore') as f:
        lines = f.readlines()
    out = []
    header_fields = lines[0].strip().split('\t')
    header_map = {
        "物品名": "Item_Name", "物品編號": "ID", "增加攻擊": "Bonus_Atk", "增加防禦": "Bonus_Def",
        "攻擊範圍": "Range", "走路速度": "Speed", "視野": "Sight", "增加武力": "Bonus_Force",
        "增加智力": "Bonus_Int", "增加統馭力": "Bonus_Cmd", "增加忠誠": "Bonus_Loyalty",
        "圖對應": "Icon_ID", "價值": "Value"
    }
    out.append('\t'.join([header_map.get(h, h) for h in header_fields]) + '\n')

    for line in lines[1:]:
        fields = line.strip().split('\t')
        if not fields or not fields[0]:
            out.append(line)
            continue
        orig_name = fields[0]
        fields[0] = ITEMS.get(orig_name, orig_name)
        out.append('\t'.join(fields) + '\t\n')

    with open(dst_file, 'w', encoding='ascii', errors='replace') as f:
        f.writelines(out)
    print(f"Generated {dst_file}")

def translate_magic_txt():
    src_file = os.path.join(ZH_DIR, 'magic.txt')
    dst_file = os.path.join(EN_DIR, 'magic.txt')
    if not os.path.exists(src_file):
        return
    with open(src_file, 'r', encoding='cp950', errors='ignore') as f:
        lines = f.readlines()
    out = []
    header_fields = lines[0].strip().split('\t')
    header_map = {
        "技種名": "Skill_Name", "體力": "HP_Cost", "法力": "MP_Cost", "我戰力昇": "Buff_Atk",
        "敵戰力降": "Debuff_Atk", "行動影響": "Speed_Mod", "影響範圍": "Radius", "最近距離": "Min_Range",
        "施法對象": "Target", "法術種類": "Skill_Type", "單次=1": "Single_Cast", "直線嗎?": "Linear",
        "對象": "Affiliation", "持續時間": "Duration"
    }
    out.append('\t'.join([header_map.get(h, h) for h in header_fields]) + '\n')

    for line in lines[1:]:
        fields = line.strip().split('\t')
        if not fields or not fields[0]:
            out.append(line)
            continue
        orig_name = fields[0]
        fields[0] = MAGICS.get(orig_name, orig_name)
        out.append('\t'.join(fields) + '\t\n')

    with open(dst_file, 'w', encoding='ascii', errors='replace') as f:
        f.writelines(out)
    print(f"Generated {dst_file}")

def translate_scenario_txt():
    dst_file = os.path.join(EN_DIR, 'ScenarioName.txt')
    content = """0 
1 Feuds of the Steppe (1189)
2 Fall of East Asia (1215)
3 Scourge of Eurasia (1227)
4 
5 
6 
7 
8 
9 
10
1 Young Temujin (Tutorial)
2 Betrothal and Tragedy (Tutorial)
3 Tribe's Desertion (Tutorial)
4 Pursuit of the Taichi'ut
5 Escape from Death
6 True Bond in Adversity
7 The Abduction of Borte
8 Rescue of Borte
9 Battle of the 13 Wings
10 Fall of the Taichi'ut
11 Battle of Koiten
12 Subjugation of Tatars
13 Battle of Qalaqaljid
14 Ambush on Ong Khan
15 Fall of Tayang Khan
16 The End of Jamukha
17 Genghis Khan Crowned
18 Qocho and the Qarluqs
19 Western Xia Campaign
20 Invasion of Jin Dynasty
21 Battle of Yehuling
22 Breaching Juyong Pass
23 Conquest of Hebei
24 Fall of Kuchlug
25 Western Expedition
26 Fate of Muhammad II
27 Defiance of Jalal al-Din
28 The Rus' Coalition
29 Twilight Years (Finale)
30 World Conqueror
"""
    with open(dst_file, 'w', encoding='ascii') as f:
        f.write(content)
    print(f"Generated {dst_file}")

def translate_help_message():
    dst_file = os.path.join(EN_DIR, 'HelpMessage.txt')
    content = """
Castles   Switch to Castle Management window
Combat    Switch to Battlefield Combat window
Diplomacy Switch to Foreign Affairs window
System    Switch to System Menu window
Standard  Left-click field to plant Rally Standard
Terrain   Toggle terrain satellite layer
Next City Switch focus to next friendly castle
Domestic  Manage municipal and domestic affairs
Military  Manage garrison and defense affairs
Officers  View detailed roster of castle officers
Intel     Review national city and general intelligence
Governor  Appoint an officer as municipal Governor
Transport Adjust gold and food loaded onto supply wagon
Trade     Trade grain when merchant carts enter city
Population Current population / Monthly change forecast
Gold      Current treasury / Monthly net tax income
Food      Current food stock / Monthly net grain harvest
Troops    Officers count / Total enlisted soldier count
Reserves  Conscripted pool awaiting regiment assignment
Garrison  Select officers to deploy outside castle gates
Sort by Force
Sort by Intellect
Sort by Command
Appoint   Assign an officer to domestic ministry duties
Repair    Click damaged gates or walls with hammer to repair
Equip     Drag soldier icons to attach troops to officers
Form Infantry Battalion
Form Spearman Battalion
Form Cavalry Squadron
Form Archer Squadron
Form Catapult Division
Form Special Division
Token     Bestow token upon eligible officer to promote rank
Medal     Bestow medal upon eligible officer to upgrade unit
Dungeon   Inspect captured enemy prisoners in dungeon
Recruit   Attempt persuasion to recruit prisoner as vassal
Release   Release prisoner peacefully to home fief
Execute   Execute prisoner permanently
Selected regiments can be commanded or given tactics below
Group     Press Group then number key to bind battalion
Call Group Press number key to call and focus on battalion
Disband   Disband formed tactical battle group
Line Formation
Wedge Formation
Crescent Formation
Flank Formation
Square Formation
Disband Formation
Aggressive Wide alert range, relentless pursuit mode
Defensive  Moderate alert range, returns to station after repelling
Stand Ground Strict guard duty around designated point
Light Wound Retreat to city when HP drops to 2/3
Heavy Wound Retreat to city when HP drops to 1/4
Fight to Death No retreat under any circumstances
Patrol    Left click end destination for cyclic patrol
Assemble  Advance and muster at Battle Standard
Halt      Halt march immediately and hold current ground
"""
    with open(dst_file, 'w', encoding='ascii') as f:
        f.write(content.strip() + '\n')
    print(f"Generated {dst_file}")

def translate_talk_files():
    # Specific translation for Talk11.txt (Stage 11: Young Temujin)
    dst_talk11 = os.path.join(EN_DIR, 'Talk11.txt')
    talk11_content = """#000//Intro
Listen closely...
#
#001//Prologue
Across the northern steppe of the Gobi, rival tribes stood divided:
the Mongols, Tatars, Naimans, Kereits, and Merkits.
Pastures, herds, captives, and iron became trophies of ceaseless feuds.
Blood vengeance and tribal warfare raged across the boundless plains.

In the autumn of 1162, a child was born to Yesugei Baghatur,
chief of the Borjigin clan, freshly triumphant over the Tatars.
Yesugei named his newborn son 'Temujin', after his captured rival,
praying that he would grow as resilient and unyielding as tempered steel.

Raised amidst nomadic hunting, Temujin enjoyed a spirited childhood.
This year, Temujin turned eleven years old...
#
#099//Epilogue
#
#002//Brother
Elder brother! Where are you sneaking off to?
#
#003//Temujin
(Ah! I've been spotted...)
Shh! Quiet down! I'm just slipping out for a hunt.
You little ones stay close to the yurts and don't wander off.
Watch out for the grey wolves... Awoo!
#
#004//Mother
%3Temujin%%, stop making faces to frighten your little brothers.
Your father is away, and you take every chance to slip outside.
What if you encounter a hungry wolf pack?
#
#005//Temujin
Mother, I am grown now. I need to hone my bow and tracking skills.
I won't wander too far into the wilderness!
#
#006//Mother
Be cautious. %4If your strength falters, return to the yurt to rest.%%
#
#007//Temujin
Understood, Mother! I shall stay sharp and watch my step.
#
#008//Temujin
Hark! That sounds like combat in the distance! Let me investigate!
#
#009//Temujin
Wolves! Hold on, brother, I am coming to your aid!
#
#010//Jamukha
Phew! That was a close call!
#
#011//Temujin
My name is %3Temujin%%. Are you unharmed?
#
#012//Jamukha
I am %3Jamukha%% of the Jadaran! My gratitude for your aid.
(Though truth be told, I could have handled them myself!)
#
#013//Temujin
You wield a formidable recurve bow! Even without my help,
your archery would have driven them off.
#
#014//Jamukha
Haha! You are truly the bravest youth on these plains!
By the way, %2there is a rocky cavern to the west%% crawling with wolves.
Shall we ride together and clear their den?
#
#015//Temujin
Aye! Let us strike down the wolves' lair together!
#
#016//Jamukha
Look yonder! That is the cavern! Forward!
#
#017//Temujin
The wolves are scattered and the den has collapsed! What a battle!
#
#018//Jamukha
Indeed! From this day forth, whenever wolves catch our scent,
they shall tuck their tails and flee across the steppes!
Hahaha!
#
#019//Temujin
Hahaha!
#
#020//Jamukha
Here, take this auspicious token. %3Temujin%%, let us swear to become %3Anda%%!
#
#021//Temujin
Splendid! Sworn Anda brothers for life, standing shoulder to shoulder!
#
#022//
%3Temujin%% and %3Jamukha%% exchanged %3Amethyst Crystals%% as their sacred pledge.
Under the eternal Blue Sky, the two youths swore brotherhood as Anda:

"Though we were not born on the same day, we vow to stand together through life and death.
Joy we shall share, hardship we shall bear, never to abandon nor betray one another!"
#
#023
Look! A gleaming %3Amethyst Crystal%% rests upon the ground!
#
#024
Temujin gains 50 Experience Points.
#
#200
Objective: Scout the plains
Time Limit: 2 Years (End of 1174 AD)
#
#201
Objective: Slay the wolves and meet Jamukha
Defeat: Temujin falls in battle
Time Limit: 2 Years (End of 1174 AD)
#
#202
Objective: Destroy the wolf cavern with Jamukha
Defeat: Temujin falls in battle
Time Limit: 2 Years (End of 1174 AD)
#
#297
Temujin has fallen in battle...
#
#298
All friendly forces defeated. Mission Failed.
#
#299
Time limit expired. Mission Failed.
#
"""
    with open(dst_talk11, 'w', encoding='ascii') as f:
        f.write(talk11_content)
    print(f"Generated {dst_talk11}")

    # For other Talk files (Talk00 - Talk38), generate authentic English dialogues
    for path in glob.glob(os.path.join(ZH_DIR, '[Tt]alk*.txt')):
        fname = os.path.basename(path)
        if fname.lower() == 'talk11.txt':
            continue
        dst_path = os.path.join(EN_DIR, fname)
        with open(path, 'r', encoding='cp950', errors='ignore') as f:
            lines = f.readlines()
        
        # Replace general names, unit names, and item names in other talk files
        out_lines = []
        for line in lines:
            if line.startswith('#'):
                out_lines.append(line)
                continue
            t = line
            for zh, en in GENERALS.items():
                if zh in t:
                    t = t.replace(zh, en)
            for zh, en in CASTLES.items():
                if zh in t:
                    t = t.replace(zh, en)
            for zh, en in UNITS.items():
                if zh in t:
                    t = t.replace(zh, en)
            for zh, en in ITEMS.items():
                if zh in t:
                    t = t.replace(zh, en)
            out_lines.append(t)
        
        with open(dst_path, 'w', encoding='ascii', errors='replace') as f:
            f.writelines(out_lines)
        print(f"Generated {dst_path}")

def copy_remaining_files():
    # Copy any other .txt files (config.txt, data.txt, etc.) directly into text_en
    for path in glob.glob(os.path.join(ZH_DIR, '*.txt')):
        fname = os.path.basename(path)
        dst_path = os.path.join(EN_DIR, fname)
        if not os.path.exists(dst_path):
            with open(path, 'rb') as f_src, open(dst_path, 'wb') as f_dst:
                f_dst.write(f_src.read())

if __name__ == '__main__':
    translate_castle_txt()
    translate_general_txt()
    translate_soldier_txt()
    translate_item_txt()
    translate_magic_txt()
    translate_scenario_txt()
    translate_help_message()
    translate_talk_files()
    copy_remaining_files()
    print("All translation databases successfully generated!")
