# import pyautogui
# import time
# import random


# # Wait for 5 seconds to give you time to switch to the desired window
# time.sleep(5)

# # Get a list of all open windows
# windows = pyautogui.getAllTitles()

# # Find the window you want to maximize
# window_title = "Summoners War"
# for window in windows:
#     if window.title == window_title:
#         window.activate()
#         break

# # Maximize the window
# # pyautogui.hotkey('winleft', 'up')
# pyautogui.getWindowsWithTitle("Summoners War")[0].maximize()

import win32gui
import time
import win32con


# Wait for 5 seconds to give you time to switch to the desired window
time.sleep(1)

# Find the window you want to maximize by its title
window_title = "Summoners War"
window = win32gui.FindWindow(None, window_title)

# Switch to the window and maximize it
if window:
    win32gui.ShowWindow(window, win32con.SW_MAXIMIZE)
    win32gui.SetForegroundWindow(window)
else:
    print(f"Window with title '{window_title}' not found")