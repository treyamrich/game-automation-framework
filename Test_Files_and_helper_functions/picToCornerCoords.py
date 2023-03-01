import pyautogui
import time
import random
import win32gui
import win32con
import os

def picToBoxCoords(imgPath):
    imgDetect = pyautogui.locateOnScreen(imgPath, confidence=0.7)
    return imgDetect

def picToCornerCoords(imgPath):
    imgDetect = pyautogui.locateOnScreen(imgPath, confidence=0.7)
    cornerCoordReturn = []
    if(imgDetect != None):
        cornerCoordReturn.append((imgDetect.left,imgDetect.top))
        cornerCoordReturn.append((imgDetect.left + imgDetect.width, imgDetect.top))
        cornerCoordReturn.append((imgDetect.left + imgDetect.width, imgDetect.top+imgDetect.height))
        cornerCoordReturn.append((imgDetect.left, imgDetect.top+imgDetect.height))
    return cornerCoordReturn
