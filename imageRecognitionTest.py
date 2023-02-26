import pyautogui
s = pyautogui.locateOnScreen("vscodesnippet.png", confidence=0.9)
print(s)