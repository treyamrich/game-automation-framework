import pyautogui
import time
import random
import win32gui
import win32con
import Test_Files_and_helper_functions.detection as detection
import os
import Test_Files_and_helper_functions.picToCornerCoords as picToCornerCoords
import swmacros as sw


sw.changeWindows("Summoners War")
time.sleep(1)
LEGENDARY_YES_SELL = picToCornerCoords.picToCornerCoords("images\legend_rune_yes.png")

print(LEGENDARY_YES_SELL)
if detection.legendaryFlatSellConfirm():
                print("legendary sell")
                time.sleep(1)
                randomClickType = random.choice(sw.clickTypes)
                randomClickType(sw.randomPointWithinRect(LEGENDARY_YES_SELL))   