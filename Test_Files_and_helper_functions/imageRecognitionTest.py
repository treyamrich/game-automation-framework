import pyautogui
s = pyautogui.locateOnScreen("images/vscodesnippet.png", confidence=0.9)
print(s)