import pyautogui
s = pyautogui.locateOnScreen("vscodesnippet.png", confidence=0.5)
print(s)