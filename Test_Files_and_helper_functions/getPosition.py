import pyautogui
import time
time.sleep(4)
for i in range(4):
    # Get the current mouse position yessir
    position = pyautogui.position()

    # Print the x and y coordinates
    print("Current mouse position: x=%d, y=%d" % (position.x, position.y))
    time.sleep(4)
