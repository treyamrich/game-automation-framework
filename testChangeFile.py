import swmacros
import Test_Files_and_helper_functions.picToCornerCoords as pic
import time
import pyautogui
time.sleep(2)
print(pic.picToCornerCoords("images\\navigateToCaiross\swIcon.png"))
a = (pyautogui.locateAllOnScreen('images\\arena_images\\arena_rivals_img.png', confidence=0.4, grayscale=False))

for a1 in a:
    print(a1.left, a1.top, a1.width, a1.height)
