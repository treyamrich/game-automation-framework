import pyautogui
import time
time.sleep(10)
YES_SELL_BOUNDS_DISPLAY_MON_1 = [(690, 585), (1525, 585), (1525,670), (690,670)]
for position in YES_SELL_BOUNDS_DISPLAY_MON_1: 
    pyautogui.moveTo(position)
    time.sleep(3)
