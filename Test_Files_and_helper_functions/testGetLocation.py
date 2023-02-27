import pyautogui
import time
import random
import win32gui
import win32con
import os
import keyboard

while True:
    time.sleep(1)
    if keyboard.is_pressed('b'):
        position = (pyautogui.position()) 
        print("Current mouse position: x=%d, y=%d" % (position.x, position.y))
