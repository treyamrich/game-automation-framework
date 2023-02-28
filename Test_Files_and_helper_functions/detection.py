import pyautogui
import time
import random

def isDefeated():
    defeatDetect = pyautogui.locateOnScreen("images\\10xresultpage.png", confidence=0.7)
    return defeatDetect != None 
        
def noItemsToSell():
    itemDetect = pyautogui.locateOnScreen("images\sellfail.png", confidence=0.7)
    return itemDetect != None 

#TODO get legendary confirm image path
def legendaryFlatSellConfirm():
    legendaryFlatSellConfirm = pyautogui.locateOnScreen("images\legend_rune_sell.png", confidence= 0.7)
    return legendaryFlatSellConfirm != None


#pass through a tuple 
def splitTimesAndCheckDefeated(timeRange):
    randTime = random.uniform(timeRange[0], timeRange[1])
    for i in range(5):
        print("sleep iteration: ", i)
        time.sleep(randTime/5)
        if isDefeated():
            print("defeated/done")
            return
    for i in range(5):
        print("sleep iteration: ", i)
        time.sleep(randTime/5)
    return
        
        
