import pyautogui
import time
import random
import picToCornerCoords  
#Reference Monitor Values:
'''
REPEAT_BATTLE_DISPLAY_MON_1 = [(1415, 670), (1720, 670), (1720,795), (1415,795)]
REPLAY_BOUNDS_DISPLAY_MON_1 = [(885, 850), (1150, 850), (1150,925), (885,925)]
SELL_SELECTED1_BOUNDS_DISPLAY_MON_1 = [(1495, 880), (1745, 880), (1745,925), (1495,925)]
SELL_SELECTED2_BOUNDS_DISPLAY_MON_1 = [(1305, 875), (1525, 875), (1525,945), (1305,945)]
YES_SELL_BOUNDS_DISPLAY_MON_1 = [(695, 585), (910, 585), (910,675), (695,675)]
BOX = [(1112,665),(1112+467,665),(1112+467,665-126),(1112,665-126)]
'''
#Example input:
#[(943, 446), (1146, 446), (1146, 530), (943, 530)]
#[(1886, 992), (2293, 992), (2293, 1177), (1886, 1177)]
def visualizeCorners(cornerCoords):
    for coords in cornerCoords:
        pyautogui.moveTo(coords, duration = 0.5)

#Box(left=1409, top=658, width=321, height=150)
def visualizeBox(boxCoords):
    pyautogui.moveTo((boxCoords.left,boxCoords.top), duration = 0.5)
    pyautogui.moveTo((boxCoords.left + boxCoords.width, boxCoords.top), duration = 0.5)
    pyautogui.moveTo((boxCoords.left + boxCoords.width, boxCoords.top+boxCoords.height), duration = 0.5)
    pyautogui.moveTo((boxCoords.left, boxCoords.top+boxCoords.height), duration = 0.5)
box = picToCornerCoords.picToCornerCoords("images\9x10repeat_battle.png")
visualizeBox(box)
    
