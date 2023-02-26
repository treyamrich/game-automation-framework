import pyautogui
import time
import random

def isDefeated():
    defeatDetect = pyautogui.locateOnScreen("10xresultpage.png", confidence=0.7)
    return defeatDetect != None 
        
def noItemsToSell():
    itemDetect = pyautogui.locateOnScreen("sellfail.png", confidence=0.7)
    return itemDetect != None 


#pass through a tuple 
def splitTimesAndCheckDefeated(timeRange):
    randTime = random.uniform(timeRange[0], timeRange[1])
    for i in range(10):
        print("sleep iteration: ", i)
        time.sleep(randTime/10)
        if isDefeated():
            print("defeated/done")
            return
        
        
