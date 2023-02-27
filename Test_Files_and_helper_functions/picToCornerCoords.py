import pyautogui
import time
import random
import win32gui
import win32con
import os

def picToCornerCoords(imgPath):
    imgDetect = pyautogui.locateOnScreen(imgPath, confidence=0.7)
    return imgDetect
