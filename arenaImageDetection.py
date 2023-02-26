import pyautogui
import time
import random
import win32gui
import win32con
import Test_Files_and_helper_functions.detection
import pyautogui
UNIQUE_THRESHOLD = 10
time.sleep(2)
# locate all instances of the image

def getArenaBattleLocaton():
    matches = pyautogui.locateAllOnScreen('images/arena_rivals_img.png', confidence=0.9, grayscale=True)

    unique_matches = set()

    # add each unique coordinate to the set
    # add each unique coordinate to the set
    for match in matches:
        is_unique = True
        for unique_match in unique_matches:
            if abs(match.left - unique_match.left) < UNIQUE_THRESHOLD and \
            abs(match.top - unique_match.top) < UNIQUE_THRESHOLD:
                is_unique = False
                break
        if is_unique:
            unique_matches.add(match)
    count = 0
    # print the coordinates of all matches
    for match in unique_matches:
        count+=1
        print(match)
    print("count= ", count)
    return unique_matches

def getMonsterSelectionLocation():
    box = pyautogui.locateAllOnScreen('images/monster_selection.png', confidence=0.9, grayscale=True)
    return box

