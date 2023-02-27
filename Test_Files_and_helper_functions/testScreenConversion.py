import pyautogui
import time
import random
import win32gui
import win32con
import Test_Files_and_helper_functions.detection as detection
import os


SHUTDOWN = False
REPEAT_TIMES =7
necroTime1 = 848
necroTime2 = 900


faimonTime1 = 300
faimonTime2 = 310

giantsTime1 = 650
giantsTime2 = 730

now1 = 1
now2 = 3
TIMES = {"now": (1,2), "faimon": (300,310), "giants": (650, 730), "necro": (848,900)}


#HARD CODED VALUES, REPLACE ONCE IMAGE RECOGNITION
REPEAT_BATTLE_DISPLAY_MON_1 = [(1415, 670), (1720, 670), (1720,795), (1415,795)]
REPLAY_BOUNDS_DISPLAY_MON_1 = [(885, 850), (1150, 850), (1150,925), (885,925)]
SELL_SELECTED1_BOUNDS_DISPLAY_MON_1 = [(1495, 880), (1745, 880), (1745,925), (1495,925)]
SELL_SELECTED2_BOUNDS_DISPLAY_MON_1 = [(1305, 875), (1525, 875), (1525,945), (1305,945)]
YES_SELL_BOUNDS_DISPLAY_MON_1 = [(695, 585), (910, 585), (910,675), (695,675)]
OK_SELL_BOUNDS_DISPLAY_MON_1 = [(845,585), (1070,585), (1070,670), (845,670)]
CANCEL_SELL_BOUNDS_DISPLAY_MON_1 = [(1693,880), (1761,880), (1761,940), (1693,940)]

def convScreen(cornerCoords, monOriginal, monNew):
    #my screeens:
    #mon 1 is 1920 x 1080
    #mon 2 is 2560 x 1600
    newCornerCoords = []
    for i in cornerCoords:
        x, y= i[0], i[1]
        xNew = i[0] * monNew[0] / monOriginal[0]
        yNew = i[1] * monNew[1] / monOriginal[1]
        newCornerCoords.append((int(xNew),int(yNew)))
    return newCornerCoords

print(convScreen((REPEAT_BATTLE_DISPLAY_MON_1), (1920,1080), (2560,1600)))