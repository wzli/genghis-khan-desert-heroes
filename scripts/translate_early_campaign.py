#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Authentic English Translations for Genghis Khan 1999 (Early Stages).
Files:
1. Talk00.txt
2. Talk01.txt
3. Talk02.txt
4. Talk03.txt
5. Talk04.txt
6. talk13.txt
7. Talk14.txt
8. talk15.txt
9. talk16.txt
10. talk17.txt
"""

import os
import sys
import re

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
EN_DIR = os.path.join(BASE_DIR, 'assets', 'game', 'text_en')

def build_talk00():
    sections = [
        ("#000", ""),
        ("#001//Liu Bei", "Greetings to all players of\nSanGuo BaYe!\nWelcome to our game!"),
        ("#002//Cao Cao", "Everyone wants to play the\nConquest Mode! Why are we\nbarging in to interrupt?!"),
        ("#003//Sun Quan", "Because Conquest Mode is not\navailable in this demo trial,\nwe are here together to give\na brief overview!\n(I got battered in the demo\nstage, so the director ought\nto give me more lines!)"),
        ("#004//Liu Bei", "Indeed! Story Mode stars the\nthree of us across mission\nstages, letting you live each\nhero's legendary life!"),
        ("#005//Cao Cao", "And what about Conquest Mode?"),
        ("#006//Sun Quan", "Conquest Mode spans an immense\nworld map, vast as the true\nrealm of the Three Kingdoms!"),
        ("#007//Liu Bei", "Across more than 500 screens,\nthere are 38 cities, over 200\ngenerals, countless squads,\nand bustling merchants and\nbandits roaming about!"),
        ("#008//Cao Cao", "Over two hundred generals?!\nThen let the others step up\nand speak their minds!"),
        ("#009//Lu Bu", "My martial might is peerless\nunder Heaven! Greatest hero of\nthe Three Kingdoms! Give me\nyour full support!"),
        ("#010//Kongming", "A worthy lord needs wisdom\nin domestic rule, seeking talent\nand expanding armies. Only firm\nfoundations endure!"),
        ("#011//Yuan Shao", "My power is formidable in every\nway, with camps full of famed\nheroes! I am your finest choice!"),
        ("#012//Dong Zhuo", "Bah! With Grand Preceptor Dong\nhere, you rebels deserve death!\nGo assemble in hell together!"),
        ("#013//Sima Yi", "Well spoken!\nWho knows who will descend into\nhell first!\n\n(Do you not know the realm\nbelongs to my Sima clan at\nlast? As the saying goes:\nquietly feast on three bowls\nof rice!)"),
        ("#014//Diaochan", "Pray allow this humble maiden\na word. We must state the rules\nclearly; after all, we shall all\nmeet upon the battlefield!"),
        ("#015//Liu Bei", "Dispatch generals with the\n'Persuade' skill to scout the\nwilds for wandering talent!\nMany hands make light work!"),
        ("#016//Guan Yu", "Whether managing affairs within\nthe walls or slaying enemies in\nthe field, you gain experience!"),
        ("#017//Zhang Fei", "Grinding and leveling up?\nOl' Zhang loves finding bandit\nlairs to sharpen my blade!"),
        ("#018//Zhao Yun", "My lord can lead all generals\ninto campaign together, feeling\nthe grand clash of thousands\nof steeds and infantry!"),
        ("#019//Cao Cao", "Unshackled by turn-based rules!\nPure real-time gameplay, tense\nand electrifying... truly\n'Cao-per' magnificent!"),
        ("#020//Zhang Liao", "Unit types counter one another.\nHarmonizing officer strengths\nwith support troops is the\nhighest rule of battle!"),
        ("#021//Xun Yu", "With each city seized, manage\ndomestic affairs with care,\nand fresh recruits will flow\nwithout end."),
        ("#022//Guo Jia", "Governance and war proceed\ntogether. Keep a sharp mind\nand adapt your tactics to carry\nout your grand unification!"),
        ("#023//Sun Quan", "Disasters strike any stronghold\nunawares, but riots from poor\npublic order can be averted!"),
        ("#024//Lu Xun", "When merchant carts arrive,\ncommerce thrives. Transport\nwagons haul supplies between\nour strongholds."),
        ("#025//Diaochan", "Could you explain the combat\nsystem in greater detail?"),
        ("#026//Zhou Yu", "Strategist generals can cast\nspecial tactics from the rear,\ngreatly increasing victory!"),
        ("#027//Ma Chao", "When health falls below half,\nexpend all skill power to unleash\na devastating fury strike!"),
        ("#028//Diaochan", "If a general's health reaches\nzero, will they perish?"),
        ("#029//Sun Quan", "No, they are merely incapacitated\nfor battle, though they can\nstill walk. Resting in a city\nrestores them over time.\n\nA grayed-out general has been\ntaken prisoner, and will be\nthrown into the dungeon of an\nenemy stronghold.\n\nUnless executed by a ruthless\nfoe, they will survive!"),
        ("#030//Diaochan", "How can we rescue them?"),
        ("#031//Sun Quan", "If captive in the field, slay\ntheir escort to free them.\nIf held in a dungeon, conquer\nthe city to liberate them!\nAlas, I was locked away during\nthe demo stage..."),
        ("#032//Diaochan", "That sounds wonderfully fun!"),
        ("#033//Cao Cao", "Naturally, it is 'Cao-per'\nthrilling! Tell your friends\nand classmates to join the fray!\n\n(Rumor has it there is a secret\nstage for Diaochan... clear it\nfor a spicy surprise... *wink*)"),
        ("#034//Liu Bei", "Real-Time Strategy RPG\n'SanGuo BaYe', priced at\n599 NT, launching late\nNovember!"),
        ("#035//Diaochan", "To all players who love us, be\nsure to bring us home!\nFarewell!!"),
        ("#036", ""),
        ("#037", ""),
        ("#038", ""),
        ("#039", ""),
        ("#040", ""),
    ]
    return format_sections(sections)

def build_talk01():
    sections = [
        ("#000//Intro", "Listen closely..."),
        ("#001//Prologue", ""),
        ("#099//Epilogue", ""),
        ("#002", "Congratulations!\nYou have unified all of\nthe Mongol steppe."),
        ("#003", ""),
        ("#004", ""),
        ("#005", ""),
        ("#006", ""),
        ("#007", ""),
        ("#008", ""),
        ("#009", ""),
        ("#200", "Objective: Crush all clans\nand unify the Mongol steppe\nDefeat: Our forces are wiped\nout\nTime Limit: 100 Years\n(End of 1281 AD)"),
        ("#298", "All friendly forces defeated.\nMission Failed."),
        ("#299", "Time limit expired.\nMission Failed."),
    ]
    return format_sections(sections)

def build_talk02():
    sections = [
        ("#000//Intro", "Listen closely..."),
        ("#001//Prologue", ""),
        ("#099//Epilogue", ""),
        ("#002", "Congratulations!\nYou have unified the entire\nEast Asian mainland."),
        ("#200", "Objective: Crush all nations\nand unify the East Asian\nmainland\nDefeat: Our forces are wiped\nout\nTime Limit: 100 Years\n(End of 1303 AD)"),
        ("#298", "All friendly forces defeated.\nMission Failed."),
        ("#299", "Time limit expired.\nMission Failed."),
    ]
    return format_sections(sections)

def build_talk03():
    sections = [
        ("#000//Intro", "Listen closely..."),
        ("#001//Prologue", ""),
        ("#099//Epilogue", ""),
        ("#002", "Congratulations!\nYou have unified the entire\nEurasian continent."),
        ("#200", "Objective: Crush all nations\nand unify the entire\nEurasian continent\nDefeat: Our forces are wiped\nout\nTime Limit: 100 Years\n(End of 1317 AD)"),
        ("#298", "All friendly forces defeated.\nMission Failed."),
        ("#299", "Time limit expired.\nMission Failed."),
    ]
    return format_sections(sections)

def build_talk04():
    sections = [
        ("#000//Intro", "Listen closely..."),
        ("#001//Prologue", ""),
        ("#099//Epilogue", ""),
        ("#002", "Congratulations!\nYou have unified all of\nthe Mongol steppe."),
        ("#003", "The demo trial time has expired!\nHow we wished to see you\nachieve complete unification!\n\nAs a special gift for our first\nbatch of buyers, the boxed game\nincludes an exquisite quill pen\nand an adorable yurt pen\nholder! So charming!\n\nWe look forward to meeting you\nin the full game. Farewell!"),
        ("#004", "Demo version time limit: 1 year."),
        ("#005", ""),
        ("#006", ""),
        ("#007", ""),
        ("#008", ""),
        ("#009", ""),
        ("#010", ""),
        ("#011", ""),
        ("#012", ""),
        ("#013", ""),
        ("#014", ""),
        ("#015", ""),
        ("#016", ""),
        ("#017", ""),
        ("#018", ""),
        ("#019", ""),
        ("#200", "Objective: Crush all nations\nand eradicate outlaw bandit\nforces\nDefeat: Our forces are wiped\nout\nTime Limit: 1 Year\n(End of 1182 AD)"),
        ("#298", "All friendly forces defeated.\nMission Failed."),
        ("#299", "Time limit expired.\nMission Failed."),
    ]
    return format_sections(sections)

def build_talk13():
    sections = [
        ("#000//Intro", "Listen closely..."),
        ("#001//Prologue", 
         "Following the death of Yesugei,\n"
         "the Mongol people lost their\n"
         "mighty and valiant leader.\n"
         "In those days, succession was\n"
         "not strictly hereditary; instead,\n"
         "a Kurultai was held, where the\n"
         "clans gathered to elect a Khan\n"
         "of renown and stature.\n"
         "Among the Mongol clans were the\n"
         "Taichi'ut, Jurchin, Kiyad, and\n"
         "others, yet none could put forth\n"
         "a leader of supreme command.\n"
         "Thus, many clansmen resolved\n"
         "to migrate elsewhere."),
        ("#099//Epilogue", ""),
        ("#002//Mother", 
         "Alas! Your father has passed,\n"
         "leaving us widows and orphans.\n"
         "I fear the clansmen will abandon\n"
         "us one by one."),
        ("#003//Temujin", 
         "Mother, rest easy. I shall take\n"
         "upon myself the duty of guarding\n"
         "our people. I go now to persuade\n"
         "them to stay in peace."),
        ("#004//Mother", 
         "Mother knows your heart is brave\n"
         "and worthy of great tasks.\n"
         "Yet on this boundless steppe,\n"
         "men depend on a mighty leader\n"
         "to sustain their safety and\n"
         "wealth. You are still young..."),
        ("#005//Temujin", "Let my deeds prove all things!"),
        ("#006//Jamukha", 
         "%3Temujin%%, news of your\n"
         "misfortune reached my ears, so\n"
         "I rode swiftly to visit you."),
        ("#007//Temujin", 
         "%3Jamukha%%, you are my true\n"
         "anda! I am setting out to urge\n"
         "our clansmen not to desert us."),
        ("#008//Jamukha", 
         "This... (He believes this task\n"
         "is simple!) Since that is your\n"
         "wish, I shall ride beside you!"),
        ("#009//Menglik", 
         "A bitter calamity! %2My flock of\n"
         "sheep took fright from wolves\n"
         "and scattered into the wilds!%%\n"
         "Can you help me gather them?"),
        ("#010//Temujin", 
         "Aye! I shall herd all your sheep\n"
         "safely back into the pen."),
        ("#011//Menglik", 
         "Your father and I were sworn\n"
         "andas. We pledged to share life\n"
         "and death, never to forsake each\n"
         "other. I... I shall remain!"),
        ("#012//Temujin", 
         "Do you speak truly? Mother will\n"
         "rejoice to hear this!"),
        ("#013//Orbei", 
         "Tracks of grey wolves have been\n"
         "seen around here of late. I have\n"
         "no wish to dwell beside beasts!"),
        ("#014//Temujin", 
         "%2If we shatter the rocky cavern\n"
         "where the pack nests, we can\n"
         "drive the wolves far away!%%\n"
         "%3Jamukha%%, I need your aid!"),
        ("#015//Jamukha", "Leave it to me!"),
        ("#016//Orbei", 
         "We and %3Targhutai%% belonged of\n"
         "old to the %3Taichi'ut clan%%.\n"
         "We submitted to %3Yesugei%% of\n"
         "the %3Kiyad%%. Now he is dead...\n"
         "There is no staying here! Move!"),
        ("#017//Temujin", 
         "%3Orbei%%... %3Orbei%%...\n"
         "They have departed..."),
        ("#018//Targhutai", 
         "You plead for us to stay? %2Only\n"
         "if you can best the champion of\n"
         "our Taichi'ut: Guwen!%%"),
        ("#019//Temujin", 
         "(That hulking brute %3Guwen%%?!)\n"
         "Very well, I accept the contest!"),
        ("#020//Targhutai", 
         "Step inside then!\n"
         "(This shall be a fine spectacle!)"),
        ("#021//Guwen", 
         "Hmph... Daring to challenge me?\n"
         "I can crush a runt like you\n"
         "with a single fist!"),
        ("#022//Guwen", 
         "Gah...! Curse it!\n"
         "This little demon...!"),
        ("#023//Temujin", "Haha! I have prevailed!"),
        ("#024//Targhutai", 
         "(The whelp truly has talent.\n"
         "Once the %3Kiyad clan%% falls\n"
         "apart, I must return and wipe\n"
         "him out for good.)\n"
         "Aye, you won. Remarkable!\n"
         "Yet you are a mere boy--why\n"
         "should seasoned men heed a child?\n"
         "Let us ride!"),
        ("#025//Temujin", "Faithless coward without honor!"),
        ("#026//Jamukha", 
         "Temujin... A true man must hold\n"
         "his head high. I must depart\n"
         "now. Take care of yourself!"),
        ("#027//Menglik", 
         "Sister-in-law, I know not how\n"
         "to speak... I... this..."),
        ("#028//Mother", 
         "I know what burdens your heart.\n"
         "You have your hardships, and I\n"
         "will not reproach you..."),
        ("#029//Menglik", 
         "Curse me! Forgive me, sister...\n"
         "I should not desert you in such\n"
         "a desperate hour..."),
        ("#030//Mother", 
         "You did no wrong; no one is to\n"
         "blame.\n\n"
         "Heaven never bars every\n"
         "road. If I can raise these boys,\n"
         "Yesugei's spirit in Heaven will\n"
         "be comforted."),
        ("#031//Menglik", 
         "(Sobbing...)\n"
         "Farewell... Farewell...!"),
        ("#032", 
         "Every soul had departed...\n\n"
         "Upon the once-lively steppe,\n"
         "only a single, lonely yurt was\n"
         "left standing. Cold winds howled\n"
         "across the vast plain, as the\n"
         "widowed mother and her young\n"
         "clung tightly to one another.\n"
         "The days to come would be\n"
         "colder still..."),
        ("#033//Temujin", "The sheep have all returned."),
        ("#034//Temujin", 
         "The cave collapsed! The grey\n"
         "wolves have nowhere to lurk now!\n"
         "Hahaha!"),
        ("#035", 
         "%3Menglik%% comes to meet\n"
         "Lady %3Hoelun%%."),
        ("#036", ""),
        ("#037", ""),
        ("#038", ""),
        ("#039", ""),
        ("#040", ""),
        ("#041", ""),
        ("#042", ""),
        ("#043", ""),
        ("#044", ""),
        ("#045", ""),
        ("#046", ""),
        ("#047", ""),
        ("#048", ""),
        ("#049", ""),
        ("#050", ""),
        ("#051", ""),
        ("#052", ""),
        ("#053", ""),
        ("#054", ""),
        ("#055", ""),
        ("#056", ""),
        ("#057", ""),
        ("#058", ""),
        ("#059", ""),
        ("#06", ""),
        ("#200", 
         "Objective: Entreat the clansmen\n"
         "to remain\n"
         "Defeat: Temujin falls in battle\n"
         "Time Limit: 2 Years\n"
         "(End of 1176 AD)"),
        ("#201", 
         "Objective: Herd 10 sheep into\n"
         "pen; defeat Guwen; destroy wolf\n"
         "cave; entreat clansmen to stay\n"
         "Defeat: Temujin falls in battle\n"
         "Time Limit: 2 Years\n"
         "(End of 1176 AD)"),
        ("#202", "Objective:\nDefeat:\nTime Limit:"),
        ("#203", "Objective:\nDefeat:\nTime Limit:"),
        ("#204", "Objective:\nDefeat:\nTime Limit:"),
        ("#297", "Temujin has fallen in battle..."),
        ("#298", "All friendly forces defeated.\nMission Failed."),
        ("#299", "Time limit expired.\nMission Failed."),
    ]
    return format_sections(sections)

def build_talk14():
    sections = [
        ("#000//Intro", "Listen closely..."),
        ("#001//Prologue", 
         "Nomads who lived by herding on\n"
         "the steppe lost all livelihood\n"
         "once severed from clan and tribe.\n"
         "After the Taichi'ut deserted,\n"
         "the nobles and folk of the Kiyad\n"
         "abandoned Temujin and his mother\n"
         "to join the Taichi'ut. Temujin's\n"
         "house fell into an abyss of woe.\n"
         "Widowed mother and orphaned sons\n"
         "endured bitter cold and hunger,\n"
         "wandering in exile through\n"
         "grueling years."),
        ("#099//Epilogue", ""),
        ("#002//Mother", 
         "%3Temujin%%, %2lead the steeds to\n"
         "graze upon thawed meadows%%.\n\n"
         "This winter was harsher than\n"
         "most; once spring returns, our\n"
         "days will brighten."),
        ("#003//Temujin", 
         "I feel no cold at all, Mother!\n"
         "Fierce blood surges within me!"),
        ("#004//Qasar", 
         "Mother, I can catch fish from\n"
         "the melting streams."),
        ("#005//Belgutei", "Mother, I want to fish too!"),
        ("#006//Qasar", 
         "I won't let you! Every time,\n"
         "you snatch what I catch! I\n"
         "despise %3Begter%% and\n"
         "%3Belgutei%%!"),
        ("#007//Mother", 
         "I have told you many times:\n"
         "though born of different wives,\n"
         "%3Begter%% and %3Belgutei%% are\n"
         "my children too. You must love\n"
         "and bear with one another!"),
        ("#008//Temujin", 
         "Mother, we understand.\n"
         "I am ready; I shall take the\n"
         "horses to graze now."),
        ("#009//Temujin", 
         "Good steeds, this is the tender\n"
         "grass of early spring. Feast!"),
        ("#010//Qachi'un", 
         "Waaah... waaah...!\n"
         "Big Brother... sob...\n"
         "%3Begter%% stole my fish again!\n"
         "A beautiful little goldfish!\n"
         "Waaah...!"),
        ("#011//Temujin", 
         "%3Begter%% never heeds our words.\n"
         "%2This time he must be taught a\n"
         "lesson!%% Come, let us find him!"),
        ("#012//Begter", 
         "Just a tiny, dried-up fish! So\n"
         "what if its scales were bright?\n"
         "Nothing special! Take it back!\n"
         "Hmph!"),
        ("#013", 
         "%3Begter%% slammed the goldfish\n"
         "viciously to the earth, crushing\n"
         "it to pieces."),
        ("#014//Qachi'un", 
         "You... You killed my fish!\n"
         "Curse you... curse you!"),
        ("#015//Temujin", "%3Begter%%, you have gone too far!"),
        ("#016//Begter", 
         "What? You want to brawl? Come!\n"
         "I am not afraid of you!"),
        ("#017//Temujin", 
         "Very well, let me teach you a\n"
         "lesson you will never forget!"),
        ("#018//Begter", "Mother... Mother... Father..."),
        ("#019//Qachi'un", 
         "Ah!! Big Brother, %3Begter%% is\n"
         "dead! He is dead...!"),
        ("#020//Temujin", 
         "Ah... gasp... I... wheeze...\n"
         "Let us return and confess all\n"
         "to Mother..."),
        ("#021", 
         "%3Temujin%% recounted the deed...\n"
         "Lady %3Hoelun%% wept bitterly in\n"
         "grief, her heart shattered, and\n"
         "sorrowfully buried the bones of\n"
         "%3Begter%%."),
        ("#022//Mother", 
         "%3Temujin%%, snap this single\n"
         "arrow in two."),
        ("#023//Temujin", 
         "?\n"
         "Aye. (With one flex, Temujin\n"
         "snaps the shaft in two.)"),
        ("#024//Mother", "Now try these five arrows..."),
        ("#025", 
         "This time, no matter how hard\n"
         "%3Temujin%% strained, he could\n"
         "not break the five bound arrows."),
        ("#026//Mother", 
         "This is the strength of unity!\n"
         "Only united can we avoid being\n"
         "trampled; only united can our\n"
         "family flourish! Slaying kin\n"
         "only leads to our ruin. Remember\n"
         "today's lesson: never turn your\n"
         "blades against each other again!"),
        ("#027//Temujin", 
         "Mother, I was rash and foolish!\n"
         "I am filled with remorse...\n\n"
         "Sob... %3Begter%%... sob...\n\n"
         "Henceforth we brothers shall\n"
         "dwell in harmony, and restore\n"
         "the glory of the %3Kiyad clan%%!"),
        ("#028//Menglik", 
         "Sister, I come to warn you! The\n"
         "%3Taichi'ut%% have mobilized in\n"
         "force to hunt you down! You must\n"
         "flee at once!"),
        ("#029//Mother", 
         "Thank you for the warning! Ride\n"
         "swiftly, lest you be caught in\n"
         "our misfortune."),
        ("#030//Temujin", "Mother, the horses are all back."),
        ("#031//Mother", 
         "We must elude the %3Taichi'ut%%!\n"
         "Flee now into the hidden valleys\n"
         "to take refuge..."),
        ("#032//Mother", 
         "Is everyone gathered?\n"
         "Wait...\n\n"
         "Where is %3Belgutei%%?!\n"
         "Disaster! %3Belgutei%% has not\n"
         "caught up!!"),
        ("#033//Temujin", 
         "I shall retrace our steps and\n"
         "search for him. Wait for me!"),
        ("#034//Temujin", 
         "%3Belgutei%%...!\n"
         "%3Belgutei%%...!"),
        ("#035//Enemy Soldier", 
         "Glorious! Seize %3Temujin%%!\n"
         "Lord %3Targhutai%% will reward\n"
         "us lavishly!"),
        ("#036", 
         "%3Temujin%% tragically fell\n"
         "into the clutches of the\n"
         "%3Taichi'ut%%..."),
        ("#037//Menglik", 
         "Sister, take the young ones and\n"
         "flee!\n\n"
         "Before the overwhelming\n"
         "might of the %3Taichi'ut%%, I am\n"
         "powerless. Sister, %3Temujin%%...\n"
         "take care! Farewell!"),
        ("#038//Mother", 
         "Temujin, are the horses back?\n"
         "%2Quickly drive them into the\n"
         "corral!%%"),
        ("#039", 
         "Our yurt was overrun.\n"
         "Mission Failed."),
        ("#040", 
         "Spotted %3Temujin%%'s kin! Quick,\n"
         "ride back and report!"),
        ("#041", 
         "We are discovered! %2Slay him\n"
         "before he carries word!%%"),
        ("#042", 
         "The enemy scout reported back!\n"
         "The %2Taichi'ut%% host butchered\n"
         "%3Temujin%%'s entire family."),
        ("#043//Enemy Soldier", "Surround them!!"),
        ("#044", "Just then, %3Qasar%% rushed over\nin haste."),
        ("#045", "Just then, %3Menglik%% arrived\nin frantic haste."),
        ("#046", "%3Temujin%%'s family failed to\nflee in time and were all slain."),
        ("#047", ""),
        ("#048", ""),
        ("#049", ""),
        ("#050", ""),
        ("#051", ""),
        ("#052", ""),
        ("#053", ""),
        ("#054", ""),
        ("#055", ""),
        ("#056", ""),
        ("#057", ""),
        ("#058", ""),
        ("#059", ""),
        ("#06", ""),
        ("#200", 
         "Objective: Temujin leads horses\n"
         "to graze on the meadows\n"
         "Defeat: Temujin falls in battle\n"
         "Time Limit: 2 Years\n"
         "(End of 1177 AD)"),
        ("#201", 
         "Objective: Teach Begter a lesson\n"
         "Defeat: Temujin falls in battle\n"
         "Time Limit: 2 Years\n"
         "(End of 1177 AD)"),
        ("#202", 
         "Objective: Temujin and Qasar\n"
         "return to the yurt\n"
         "Defeat: Temujin falls in battle\n"
         "Time Limit: 2 Years\n"
         "(End of 1177 AD)"),
        ("#203", 
         "Objective: Herd horses back to\n"
         "the yurt's corral\n"
         "Defeat: Temujin falls in battle\n"
         "Time Limit: 2 Years\n"
         "(End of 1177 AD)"),
        ("#204", 
         "Objective: Relocate all people\n"
         "and horses to the mountain red\n"
         "flag within two months\n"
         "Defeat: Temujin falls in battle\n"
         "Time Limit: 2 Years\n"
         "(End of 1177 AD)"),
        ("#205", 
         "Objective: Temujin returns to\n"
         "the yurt to search for Belgutei\n"
         "Defeat: Temujin falls in battle\n"
         "Time Limit: 2 Years\n"
         "(End of 1177 AD)"),
        ("#206", 
         "Objective: Eliminate the enemy\n"
         "scouts\n"
         "Defeat: Temujin falls in battle\n"
         "Time Limit: 2 Years\n"
         "(End of 1177 AD)"),
        ("#297", "Temujin has fallen in battle..."),
        ("#298", "All friendly forces defeated.\nMission Failed."),
        ("#299", "Time limit expired.\nMission Failed."),
    ]
    return format_sections(sections)

def build_talk15():
    sections = [
        ("#000//Intro", "Listen closely..."),
        ("#001//Prologue", 
         "Targhutai, chieftain of the\n"
         "Taichi'ut, prepared a banquet to\n"
         "celebrate capturing Temujin.\n"
         "Temujin was locked in camp under\n"
         "strict guard. Though some pitied\n"
         "his plight, none dared release\n"
         "him, terrified of Targhutai's\n"
         "ruthless wrath."),
        ("#099//Epilogue", ""),
        ("#002//Guwen", 
         "Lord %3Targhutai%% ordered us to\n"
         "watch %3Temujin%% closely. Not a\n"
         "single mishap is permitted!"),
        ("#003//Temujin", 
         "Brave warrior %3Guwen%%, bound as\n"
         "I am, I could not fly even with\n"
         "wings. With the racket outside,\n"
         "they are surely preparing to\n"
         "sacrifice me to the war banner..."),
        ("#004//Guwen", 
         "My lord holds a banquet tonight,\n"
         "and because of guarding you, I\n"
         "miss out on rich kumis..."),
        ("#005//Temujin", 
         "A bitter trial for you! Bound\n"
         "fast and without a blade, with\n"
         "guards all around--not even a\n"
         "mouse could escape, let alone\n"
         "a captive!"),
        ("#006//Guwen", 
         "Hmph... (Sneaking a few bowls\n"
         "should do no harm...)\n"
         "I will return shortly. Try no\n"
         "tricks!"),
        ("#007", 
         "With the guard gone, %3Temujin%%\n"
         "strained fiercely against his\n"
         "bonds. Enduring the agony of\n"
         "torn flesh, %3Temujin%% finally\n"
         "wrenched off the wooden cangue!"),
        ("#008//Temujin", 
         "(Agony...! Flee now, while the\n"
         "chance remains!)"),
        ("#009//Targhutai", 
         "Brothers! Drink to the capture\n"
         "of the whelp %3Temujin%%! Drink!"),
        ("#010//Soldiers", 
         "Drink!!\n"
         "Drink!!\n"
         "Drink!!"),
        ("#011//Temujin", 
         "(Heaven preserve me! %2I must\n"
         "not be spotted...%%\n"
         "Search for an unguarded way out.)"),
        ("#012//Temujin", 
         "(That is my steed's neigh! %2I\n"
         "must find my horse first.%%)"),
        ("#013//Temujin", "Shh... (Find a way out of here.)"),
        ("#014//Guwen", "Disaster! %3Temujin%% has escaped!"),
        ("#015//Targhutai", 
         "What?! Incompetent fools! Bring\n"
         "%3Temujin%% back at once!!!"),
        ("#016//Temujin", 
         "(Curse it, spotted! Enemy camps\n"
         "lie ahead--%2flee toward the\n"
         "forest!%%)"),
        ("#017//Soldiers", "Hurry! Search over there!"),
        ("#018//Temujin", "%2Take shelter in the camp\nfirst.%%"),
        ("#019//Chilaun", 
         "%3Temujin%%! Weren't you captured?\n"
         "You broke free! I am %3Chilaun%%;\n"
         "we played together as boys!"),
        ("#020//Temujin", 
         "The %3Taichi'ut%% hunt me down.\n"
         "Please, help me...!"),
        ("#021//Chilaun", 
         "I will help you without fail!\n"
         "Hide here for a few days..."),
        ("#022//Targhutai", 
         "Have you seen %3Temujin%%? He\n"
         "could not have fled far! Search\n"
         "every yurt...!"),
        ("#023//Chilaun", 
         "You have searched many times;\n"
         "he is not among us..."),
        ("#024//Targhutai", 
         "If anyone harbors him, I will\n"
         "sacrifice them to the banner!\n"
         "Search elsewhere!"),
        ("#025//Chilaun", 
         "%3Targhutai%% has just left.\n"
         "Flee now while you have the\n"
         "chance!"),
        ("#026//Temujin", 
         "You saved my life. How can I\n"
         "ever repay you?"),
        ("#027//Chilaun", 
         "You are still on %3Taichi'ut%%\n"
         "soil and do not know the path.\n"
         "Treacherous thin ice lies north;\n"
         "without my guidance you cannot\n"
         "cross. I shall ride with you!"),
        ("#028//Temujin", 
         "%3Chilaun%%, your kindness is a\n"
         "debt I can never repay!"),
        ("#029//Chilaun", 
         "%2Never tread on smooth snow!\n"
         "Follow the muddy tracks across\n"
         "the frozen ground.%%"),
        ("#030//Chilaun", "Phew, I crossed safely."),
        ("#031//Temujin", 
         "The %3Taichi'ut%%! There are few\n"
         "of them--%2slay them before they\n"
         "raise the alarm!%%"),
        ("#032//Temujin", "Mother, I have returned!"),
        ("#033//Mother", 
         "My ears do not deceive me--my son\n"
         "has returned! Sob... Mother\n"
         "feared she would never see you\n"
         "again. Look at your wounds...\n"
         "How you have suffered!"),
        ("#034//Temujin", 
         "Mother, I am unharmed.\n"
         "Henceforth our family shall never\n"
         "be torn asunder again!"),
        ("#035//Targhutai", 
         "Curse him! I should have slit\n"
         "his throat at once! %3Temujin%%...\n"
         "He and his brothers will return\n"
         "for blood one day..."),
        ("#036", "%3Chilaun%% has fallen in battle."),
        ("#037//Soldier", "It is %3Temujin%%! Seize him!"),
        ("#038//Soldier", "%3Temujin%% is found! Slay him!"),
        ("#039//Temujin", 
         "We are safe, %3Chilaun%%, all\n"
         "thanks to your courage!"),
        ("#040//Chilaun", 
         "The %3Taichi'ut%% are wicked!\n\n"
         "%3Temujin%%, if ever you face\n"
         "adversity, call upon me; I will\n"
         "come to your aid. Return home\n"
         "swiftly! Farewell!"),
        ("#041//Temujin", 
         "Thank you! You saved my life\n"
         "and stood by my side. I will\n"
         "never forget you. Farewell!"),
        ("#042", 
         "%3Temujin%% plunged through the\n"
         "thin ice and perished."),
        ("#043", 
         "%3Chilaun%% plunged through the\n"
         "thin ice and perished."),
        ("#044//Enemy Soldier", "%3Temujin%% is spotted!!"),
        ("#045", "Disaster!!"),
        ("#046//Qubilai", 
         "Fear not! I shall hold them off!\n"
         "Flee quickly!"),
        ("#047//Chilaun", 
         "%3Qubilai%%, a true friend! You\n"
         "arrived right on time!\n\n"
         "I will lead %3Temujin%% away;\n"
         "leave the pursuers to you!"),
        ("#048//Qubilai", "Leave them to me! Ride swift!"),
        ("#049//Temujin", "Aye! Take great care as well!"),
        ("#050", ""),
        ("#051", ""),
        ("#052", ""),
        ("#053", ""),
        ("#054", ""),
        ("#055", ""),
        ("#056", ""),
        ("#057", ""),
        ("#058", ""),
        ("#059", ""),
        ("#06", ""),
        ("#200", 
         "Objective: Temujin escapes from\n"
         "captivity\n"
         "Defeat: Temujin falls in battle\n"
         "Time Limit: 2 Years\n"
         "(End of 1178 AD)"),
        ("#201", 
         "Objective: Temujin retrieves his\n"
         "horse and dons equipment\n"
         "Defeat: Temujin falls in battle\n"
         "Time Limit: 2 Years\n"
         "(End of 1178 AD)"),
        ("#202", 
         "Objective: Temujin flees from\n"
         "the Taichi'ut territory\n"
         "Defeat: Temujin falls in battle\n"
         "Time Limit: 2 Years\n"
         "(End of 1178 AD)"),
        ("#203", 
         "Objective: Temujin and Chilaun\n"
         "cross the thin ice safely\n"
         "Defeat: Either Temujin or\n"
         "Chilaun falls through thin ice\n"
         "Time Limit: 2 Years\n"
         "(End of 1178 AD)"),
        ("#204", 
         "Objective: Slay pursuers and\n"
         "reach home safely\n"
         "Defeat: Temujin falls in battle\n"
         "Time Limit: 2 Years\n"
         "(End of 1178 AD)"),
        ("#297", "Temujin has fallen in battle..."),
        ("#298", "All friendly forces defeated.\nMission Failed."),
        ("#299", "Time limit expired.\nMission Failed."),
    ]
    return format_sections(sections)

def build_talk16():
    sections = [
        ("#000//Intro", "Listen closely..."),
        ("#001//Prologue", 
         "As Temujin and his brothers grew\n"
         "day by day, nature's hardships\n"
         "lessened. Along the Onon River,\n"
         "they herded, hunted, and fished,\n"
         "and their fortunes improved.\n"
         "In 1179 AD, Temujin turned\n"
         "sixteen, and his brothers Qasar\n"
         "and Belgutei had grown into\n"
         "sturdy youths. The footsteps of\n"
         "spring drew near..."),
        ("#099//Epilogue", ""),
        ("#002//Mother", 
         "How swiftly time passes. Both\n"
         "%3Belgutei%% and %3Qasar%% have\n"
         "grown into men."),
        ("#003//Temujin", 
         "%3Belgutei%% is burly and mighty;\n"
         "%3Qasar%% is a master of the bow.\n"
         "Both are fine brothers to me!"),
        ("#004//Qasar", 
         "I want to be a true warrior\n"
         "like my elder brother!"),
        ("#043//Belgutei", "I want to be a warrior too!"),
        ("#005//Mother", 
         "Haha... You are both valiant sons\n"
         "of our %3Kiyad clan%%!\n"
         "%3Temujin%%, take %3Belgutei%% and\n"
         "%3Qasar%% out to pasture herds!"),
        ("#006//Temujin", 
         "Hark! I hear horses whinnying!\n"
         "Hurry to the lower corral!"),
        ("#007//Temujin", "What do you think you're doing?!"),
        ("#008//Bandit Chief", 
         "Your horses are sturdy indeed!\n\n"
         "Pin them down and seize all the\n"
         "steeds!"),
        ("#009//Bandit Chief", "We have them! Fall back swiftly!"),
        ("#010//Temujin", 
         "The horses have been stolen!\n"
         "Vile thieves! Those were our\n"
         "father's legacy--%2we must win\n"
         "them back!%% Give chase!"),
        ("#011//Bandit", "They pursue us! Block them!"),
        ("#012//Jelme", 
         "Halt! Return my brother and my\n"
         "cattle!"),
        ("#013//Temujin", "?! Your brother and cattle?"),
        ("#014//Jelme", 
         "Feigning ignorance, you thieving\n"
         "raiders...?!"),
        ("#015//Temujin", "Are you unharmed?"),
        ("#016//Jelme", 
         "Ouch! I've been bested by you,\n"
         "why do you show me concern?"),
        ("#017//Temujin", 
         "You misunderstand. We are not\n"
         "raiders; our horses were just\n"
         "stolen, and we are pursuing\n"
         "the thieves."),
        ("#018//Jelme", 
         "It must be the same band! A few\n"
         "days ago, my brother %3Subutai%%\n"
         "was herding when our cattle and\n"
         "he vanished without a trace.\n"
         "I was rallying men to search."),
        ("#019//Temujin", "In that case, let us ride\ntogether!"),
        ("#020//Jelme", 
         "Agreed! I will return to the\n"
         "village to rally more hands."),
        ("#021//Temujin", "The thieves' lair! Attack!"),
        ("#022//Temujin", 
         "Your brother %3Subutai%% and the\n"
         "livestock are not here."),
        ("#023//Jelme", 
         "I heard these thieves hold many\n"
         "dens. Let us search further!"),
        ("#024//Temujin", 
         "I am %3Temujin%%. Have you seen\n"
         "any sign of horse thieves?"),
        ("#025//Bo'orchu", 
         "Thieves... %3Temujin%%?! You are\n"
         "%3Temujin%%?!\n\n"
         "I heard how you broke free from\n"
         "the %3Taichi'ut%%! You are truly\n"
         "a young hero of the steppe!"),
        ("#026//Temujin", 
         "I did not know I was held in\n"
         "such regard, but your words\n"
         "give me great heart. May we be\n"
         "friends?"),
        ("#027//Bo'orchu", 
         "My name is %3Bo'orchu%%. My\n"
         "father and %3Yesugei%% were\n"
         "distant kin; we are brothers of\n"
         "the same blood!"),
        ("#028//Bandit", 
         "Raid this place! Plunder booty\n"
         "to present to the chief!"),
        ("#029//Temujin", 
         "These bandits have no shame,\n"
         "preying on the sweat of others!"),
        ("#030//Bo'orchu", 
         "Thank you for helping our clan\n"
         "through this crisis."),
        ("#031//Temujin", 
         "%4Rest in the village to restore\n"
         "our strength%%, then %2seek out\n"
         "the thieves' main lair!%%"),
        ("#032//Temujin", "Search further ahead!"),
        ("#033//Qasar", 
         "I hear them! It is the whinny\n"
         "of our own horses!"),
        ("#034//Bandit", 
         "Halt! These belong to us now!\n"
         "We just dealt with one brat,\n"
         "and here comes a whole troop!"),
        ("#035//Jelme", 
         "What? My brother...! I will tear\n"
         "you to pieces!"),
        ("#036//Temujin", "All horses have been recovered!"),
        ("#037//Subutai", 
         "Brother, I was reckless. I\n"
         "should not have pursued them\n"
         "alone; I nearly lost my life!"),
        ("#038//Jelme", 
         "As long as you are safe!\n"
         "%3Temujin%% saved us--he united\n"
         "us all to vanquish the bandits!"),
        ("#039//Bo'orchu", 
         "Ever since %3Yesugei%% died, the\n"
         "clans fractured, giving thieves\n"
         "free rein across the steppe."),
        ("#040//Jelme", "Let us follow %3Temujin%%!"),
        ("#041//Temujin", 
         "I am wounded. Help me back to\n"
         "camp to rest."),
        ("#042//Bandit Chief", 
         "Curse you, %3Temujin%%! Mark my\n"
         "words! Flee!"),
        ("#044", 
         "Captured by bandits, Temujin was\n"
         "slain upon the spot."),
        ("#045", ""),
        ("#046", ""),
        ("#047", ""),
        ("#048", ""),
        ("#049", ""),
        ("#050", ""),
        ("#051", ""),
        ("#052", ""),
        ("#053", ""),
        ("#054", ""),
        ("#055", ""),
        ("#056", ""),
        ("#057", ""),
        ("#058", ""),
        ("#059", ""),
        ("#06", ""),
        ("#200", 
         "Objective: Pasture and guard\n"
         "the horses\n"
         "Defeat: Friendly forces wiped\n"
         "out\n"
         "Time Limit: 2 Years\n"
         "(End of 1180 AD)"),
        ("#201", 
         "Objective: Pursue the horse\n"
         "thieves\n"
         "Defeat: Friendly forces wiped\n"
         "out\n"
         "Time Limit: 2 Years\n"
         "(End of 1180 AD)"),
        ("#202", 
         "Objective: Pursue horse thieves;\n"
         "defeat Jelme\n"
         "Defeat: Friendly forces wiped\n"
         "out\n"
         "Time Limit: 2 Years\n"
         "(End of 1180 AD)"),
        ("#203", 
         "Objective: Bo'orchu joins; crush\n"
         "horse thieves, rescue Subutai\n"
         "and livestock\n"
         "Defeat: Friendly forces wiped\n"
         "out\n"
         "Time Limit: 2 Years\n"
         "(End of 1180 AD)"),
        ("#204", "Objective:\nDefeat:\nTime Limit:"),
        ("#297", "Temujin has fallen in battle..."),
        ("#298", "All friendly forces defeated.\nMission Failed."),
        ("#299", "Time limit expired.\nMission Failed."),
    ]
    return format_sections(sections)

def build_talk17():
    sections = [
        ("#000//Intro", "Listen closely..."),
        ("#001//Prologue", 
         "Ever since Temujin was betrothed\n"
         "to Borte at thirteen, his family\n"
         "had endured countless trials.\n"
         "Now Temujin was eighteen, and\n"
         "their fortunes had brightened.\n"
         "Seeing hope to revive their\n"
         "house, Mother Hoelun urged him\n"
         "to ride to the Onggirat and wed\n"
         "his bride.\n"
         "Bo'orchu, Jelme, and Subutai,\n"
         "brothers met in adversity,\n"
         "volunteered to follow him as his\n"
         "nokor. The party set forth to\n"
         "claim the bride..."),
        ("#099//Epilogue", ""),
        ("#002//Dei Sechen", 
         "%3Temujin%%, I can escort you\n"
         "no further."),
        ("#003//Temujin", 
         "Father-in-law, you did not scorn\n"
         "my poverty and gave me your\n"
         "daughter, sending so rich a\n"
         "dowry. I will strive to bring\n"
         "%3Borte%% greatest happiness!"),
        ("#004//Dei Sechen", 
         "I have every faith in you.\n"
         "Through years of hardship, you\n"
         "have become an unyielding man.\n"
         "The future of the steppe is\n"
         "yours to forge!"),
        ("#005//Temujin", 
         "I shall remember your words and\n"
         "face every trial to come!"),
        ("#006//Dei Sechen", 
         "%3Borte%%, however harsh life\n"
         "becomes, stand always by your\n"
         "husband's side. Support him,\n"
         "raise your children, and be his\n"
         "unshakeable pillar!"),
        ("#007//Borte", 
         "Father, your daughter holds your\n"
         "words close. I can no longer\n"
         "stay by your side; pray take\n"
         "good care of your health!"),
        ("#008//Dei Sechen", 
         "An escort of a thousand leagues\n"
         "must end. The way home is long;\n"
         "ride swiftly! Farewell!"),
        ("#009//Toqto'a", 
         "%3Temujin%% takes a bride!\n"
         "Heaven has eyes, granting us\n"
         "vengeance! Seize the bride!"),
        ("#010//Toqto'a", "Retreat!"),
        ("#011//Temujin", 
         "Stay sharp! Guard the bridal\n"
         "cart and the dowry cattle!"),
        ("#012//Borte", "Ah...! What are you doing?!"),
        ("#013//Chiledu", "Aha! What a beautiful maiden...!"),
        ("#014//Temujin", 
         "%3Borte%%! Where is %3Borte%%?!\n"
         "%3Borte%%...!\n"
         "%3Borte%%...!"),
        ("#015//Qasar", 
         "Brother! Sister-in-law... In\n"
         "the panic just now, she\n"
         "vanished!"),
        ("#016//Temujin", 
         "No...! %3Borte%%! Oh, I failed\n"
         "to protect you...!"),
        ("#017//Bo'orchu", 
         "The %3Merkits%% did this! To\n"
         "think the vile steppe custom of\n"
         "bride-stealing struck us!\n"
         "%3Temujin%%, let us return home\n"
         "first to plan!"),
        ("#018", 
         "%3Temujin%% recounted the raid\n"
         "to his mother."),
        ("#019//Mother", 
         "Alas! What bitter karma! This is\n"
         "a feud born of long ago...\n\n"
         "Back then, I was betrothed to\n"
         "%3Chiledu%% of the %3Merkits%%.\n"
         "On our wedding journey home,\n"
         "we met %3Yesugei%% on the hunt.\n"
         "%3Yesugei%% carried me off to be\n"
         "his bride.\n\n"
         "Knowing the steppe ways and\n"
         "powerless to resist, I had to\n"
         "yield to fate...\n"
         "Later, I found your father was a\n"
         "great hero. We loved each other\n"
         "deeply, and even now I have\n"
         "never forgotten his devotion.\n\n"
         "Yet the %3Merkits%% could never\n"
         "swallow that insult. Now they\n"
         "settle that ancient debt...\n"
         "Poor %3Borte%%, suffering for\n"
         "deeds of the past!"),
        ("#020//Temujin", 
         "No! I will tear %3Borte%% back\n"
         "from their grasp!"),
        ("#021//Mother", 
         "%3Temujin%%, this is a bitter\n"
         "pill to swallow. Whatever\n"
         "misfortune befell %3Borte%%,\n"
         "you must cherish and love her.\n"
         "She is your wife forever!"),
        ("#022", 
         "Hearing word, %3Chilaun%% and\n"
         "%3Qubilai%% rushed over with\n"
         "men. %3Temujin%% greeted them,\n"
         "and they weighed how to reclaim\n"
         "%3Borte%%."),
        ("#023//Qubilai", 
         "The %3Merkits%% are vast in\n"
         "number. We alone cannot defeat\n"
         "them, unless other clans agree\n"
         "to ride to war with us!"),
        ("#024//Temujin", 
         "Aye...\n"
         "(Lost in thought...)\n\n"
         "Two men come to mind: %3Jamukha%%,\n"
         "my sworn anda, now chieftain of\n"
         "the %3Jadaran clan%%; and\n"
         "%3Ong Khan%% of the %3Kereit%%,\n"
         "father's sworn anda. Only they\n"
         "can help us!\n"
         "First, %2I must find the two\n"
         "Amethyst Crystals pledged with\n"
         "Jamukha%%, and seek his aid!"),
        ("#025//Temujin", 
         "I must find both %3Amethyst\n"
         "Crystals%% before I can face\n"
         "%3Jamukha%%."),
        ("#026//Temujin", 
         "All tokens found! I can go see\n"
         "%3Jamukha%% now."),
        ("#027//Temujin", 
         "I am %3Temujin%%, requesting\n"
         "audience with Lord %3Jamukha%%."),
        ("#028//Guard", "Enter."),
        ("#029//Jamukha", 
         "%3Temujin%%, my anda! You found\n"
         "both %3Amethyst Crystals%%! It\n"
         "reminds me of our youth upon the\n"
         "steppe! Hahaha... glorious days!"),
        ("#030", 
         "After greeting each other,\n"
         "%3Temujin%% voiced his request."),
        ("#031//Jamukha", 
         "I will help you take vengeance!\n"
         "When you are ready to march,\n"
         "I will send ten thousand men!"),
        ("#032//Temujin", 
         "Thank you! Now I must seek\n"
         "%3Ong Khan%% of the %3Kereit%%,\n"
         "to entreat his aid as well."),
        ("#033//Jamukha", 
         "The %3Kereit%% are the mightiest\n"
         "tribe of the south. %3Ong Khan%%\n"
         "is hunting north; if he marches,\n"
         "all the better! And his general\n"
         "%3Muqali%%--with him beside us,\n"
         "the %3Merkit clan%% will be\n"
         "trampled into dust!"),
        ("#034//Temujin", 
         "I am %3Temujin%%, eldest son of\n"
         "%3Yesugei%%, come to pay respects."),
        ("#035//Ong Khan", 
         "Your father and I were sworn\n"
         "andas; I am as a father to you.\n"
         "Your grievance is my disgrace!\n"
         "And yet...\n"
         "I have many mouths to feed, and\n"
         "the cattle in our pens dwindle.\n"
         "My people must eat!"),
        ("#036//Temujin", 
         "Father Khan, these cattle were\n"
         "%3Borte%%'s bridal dowry. As my\n"
         "father's anda and my elder,\n"
         "pray accept her dowry!"),
        ("#037//Ong Khan", 
         "Haha! Well said! I shall send\n"
         "warriors to support you!"),
        ("#038//Temujin", 
         "Could General %3Muqali%% march\n"
         "with us as well?"),
        ("#039//Ong Khan", 
         "%3Muqali%%? He is not so mighty\n"
         "as they claim, and I had no\n"
         "mind to send him.\n"
         "Yet legends tell of a staff in\n"
         "the %3Namurun Ruins%%. Bring me\n"
         "that staff, and perhaps I will\n"
         "consider!"),
        ("#040//Ong Khan", 
         "Haha! It is indeed the %3White\n"
         "Stag Staff%%! Lost for so long,\n"
         "and now in my hands! Hahaha!\n"
         "I shall send warriors to avenge\n"
         "your grievance!\n"
         "%3Muqali%%, march with the army!"),
        ("#041//Temujin", 
         "A heavy staff, pale and pure.\n"
         "Grasping it, strange warmth\n"
         "courses into my palm. %2Deliver\n"
         "this staff to Father Ong Khan.%%"),
        ("#042//Muqali", 
         "%3Temujin%%, the %3Namurun\n"
         "Ruins%% lie behind us. %3Ong\n"
         "Khan%% sent scouts before, but\n"
         "none found the %3White Stag\n"
         "Staff%%."),
        ("#043//Temujin", 
         "So you are %3Muqali%%! I shall\n"
         "find the %3White Stag Staff%%\n"
         "without fail, so you may march\n"
         "with us!"),
        ("#044", 
         "%3Temujin%% paid polite homage\n"
         "to %3Ong Khan%%, praising his\n"
         "deeds, which pleased the Khan\n"
         "greatly.\n"
         "When %3Temujin%% asked for troops,\n"
         "%3Ong Khan%% pondered a moment..."),
        ("#045//Temujin", "Mother, I understand."),
        ("#046//Muqali", "Aye, Khan!"),
        ("#047", 
         "Your care for your folk is a\n"
         "blessing. %2I offer our cattle\n"
         "to Father Khan.%%\n"
         "(%3Borte%%, without your leave I\n"
         "gave your dowry to Father Khan.\n"
         "May you forgive my choice...)"),
        ("#048", "An %3Amethyst Crystal%%! Pick\nit up."),
        ("#049", "Discovered a staff! Pick it up."),
        ("#050", ""),
        ("#051", ""),
        ("#052", ""),
        ("#053", ""),
        ("#054", ""),
        ("#055", ""),
        ("#056", ""),
        ("#057", ""),
        ("#058", ""),
        ("#059", ""),
        ("#06", ""),
        ("#200", 
         "Objective: Return home safely\n"
         "Defeat: Temujin falls in battle\n"
         "Time Limit: 3 Years\n"
         "(End of 1182 AD)"),
        ("#201", 
         "Objective: Temujin brings two\n"
         "Amethyst Crystals to Jamukha\n"
         "Defeat: Temujin falls in battle\n"
         "Time Limit: 3 Years\n"
         "(End of 1182 AD)"),
        ("#202", 
         "Objective: Entreat Ong Khan for\n"
         "aid; herd 8 cattle into pen\n"
         "Defeat: Temujin falls in battle\n"
         "Time Limit: 3 Years\n"
         "(End of 1182 AD)"),
        ("#203", 
         "Objective: Clear Namurun Ruins;\n"
         "Temujin presents White Stag\n"
         "Staff to Ong Khan\n"
         "Defeat: Temujin falls in battle\n"
         "Time Limit: 3 Years\n"
         "(End of 1182 AD)"),
        ("#204", "Objective:\nDefeat:\nTime Limit:"),
        ("#297", "Temujin has fallen in battle..."),
        ("#298", "All friendly forces defeated.\nMission Failed."),
        ("#299", "Time limit expired.\nMission Failed."),
    ]
    return format_sections(sections)

def format_sections(sections):
    lines = []
    for tag, body in sections:
        lines.append(tag)
        if body:
            lines.append(body)
        lines.append("#")
    return '\n'.join(lines) + '\n'

BUILDERS = {
    'Talk00.txt': build_talk00,
    'Talk01.txt': build_talk01,
    'Talk02.txt': build_talk02,
    'Talk03.txt': build_talk03,
    'Talk04.txt': build_talk04,
    'talk13.txt': build_talk13,
    'Talk14.txt': build_talk14,
    'talk15.txt': build_talk15,
    'talk16.txt': build_talk16,
    'talk17.txt': build_talk17,
}

def verify_file(filepath):
    """Verify ASCII encoding, line widths, tag integrity, and formatting."""
    fname = os.path.basename(filepath)
    errors = []
    with open(filepath, 'rb') as f:
        raw = f.read()

    # 1. 100% ASCII
    try:
        text = raw.decode('ascii')
    except UnicodeDecodeError as e:
        errors.append(f"Non-ASCII character found: {e}")
        return errors

    # Check for placeholder '?'
    # We allow genuine question marks in questions, but no '??' or placeholder patterns
    if '??' in text:
        errors.append("Consecutive question marks '??' detected (likely placeholder)")

    # 2. Check line widths for dialogue lines
    lines = text.splitlines()
    in_section = False
    cur_header = ""
    for idx, line in enumerate(lines, 1):
        if line.startswith('#'):
            cur_header = line
            continue
        # Check line width
        # Ignore empty lines
        if not line.strip():
            continue
        # Line width shouldn't excessively exceed 34 characters
        if len(line) > 34:
            errors.append(f"Line {idx} exceeds 34 characters ({len(line)} chars): '{line}' under header {cur_header}")

    # 3. Check tag integrity (%1...%%, %2...%%, %3...%%, %4...%%)
    # Check that opening and closing tags match
    # Find all % followed by digit
    opens = len([m for m in re.finditer(r'%[1-4]', text)])
    closes = len([m for m in re.finditer(r'%%', text)])
    if opens != closes:
        errors.append(f"Mismatched formatting tags: {opens} opening '%[1-4]' vs {closes} closing '%%'")

    return errors

def main():
    print("==================================================")
    print(" Translating Early Campaign Stages (Talk00-04, 13-17)")
    print("==================================================")
    all_ok = True
    for filename, builder in BUILDERS.items():
        content = builder()
        dst_path = os.path.join(EN_DIR, filename)
        with open(dst_path, 'w', encoding='ascii') as f:
            f.write(content)
        
        errors = verify_file(dst_path)
        if errors:
            all_ok = False
            print(f"[FAIL] {filename} has errors:")
            for e in errors:
                print(f"   - {e}")
        else:
            print(f"[OK] {filename}: {len(content)} bytes, valid ASCII, formatted & wrapped cleanly.")

    if not all_ok:
        sys.exit(1)
    print("\nAll 10 files successfully generated and verified!")

if __name__ == '__main__':
    main()
