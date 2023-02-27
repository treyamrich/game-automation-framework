import pyautogui
import time
import random
import win32gui
import win32con
import Test_Files_and_helper_functions.detection as detection
import os


SHUTDOWN = False
REPEAT_TIMES =7
necroTime1 = 848
necroTime2 = 900


faimonTime1 = 300
faimonTime2 = 310

giantsTime1 = 650
giantsTime2 = 730

now1 = 1
now2 = 3
TIMES = {"now": (1,2), "faimon": (300,310), "giants": (650, 730), "necro": (848,900)}


#HARD CODED VALUES, REPLACE ONCE IMAGE RECOGNITION
REPEAT_BATTLE_DISPLAY_MON_1 = [(1415, 670), (1720, 670), (1720,795), (1415,795)]
REPLAY_BOUNDS_DISPLAY_MON_1 = [(885, 850), (1150, 850), (1150,925), (885,925)]
SELL_SELECTED1_BOUNDS_DISPLAY_MON_1 = [(1495, 880), (1745, 880), (1745,925), (1495,925)]
SELL_SELECTED2_BOUNDS_DISPLAY_MON_1 = [(1305, 875), (1525, 875), (1525,945), (1305,945)]
YES_SELL_BOUNDS_DISPLAY_MON_1 = [(695, 585), (910, 585), (910,675), (695,675)]
OK_SELL_BOUNDS_DISPLAY_MON_1 = [(845,585), (1070,585), (1070,670), (845,670)]
CANCEL_SELL_BOUNDS_DISPLAY_MON_1 = [(1693,880), (1761,880), (1761,940), (1693,940)]

#TODO get screen offset!!!

def convScreen(cornerCoords, monOriginal, monNew):
    #my screeens:
    #mon 1 is 1920 x 1080
    #mon 2 is 2560 x 1600
    newCornerCoords = []
    for i in cornerCoords:
        x, y= i[0], i[1]
        xNew = i[0] * monNew[0] / monOriginal[0]
        yNew = i[1] * monNew[1] / monOriginal[1]
        newCornerCoords.append((int(xNew),int(yNew)))
    return newCornerCoords


def changeWindows(window_title):
    # Wait for 1 second to give you time to switch to the desired window
    time.sleep(1)

    # Find the window you want to maximize by its title
    window = win32gui.FindWindow(None, window_title)

    # Switch to the window and maximize it
    if window:
        win32gui.ShowWindow(window, win32con.SW_MAXIMIZE)
        win32gui.SetForegroundWindow(window)
    else:
        print(f"Window with title '{window_title}' not found")



def randomPointWithinRect(rect):
    # Define the corners of the rectangle
    top_left = rect[0]
    top_right = rect[1]
    bottom_right = rect[2]
    bottom_left = rect[3]

    # Get the x and y limits of the rectangle
    x_min, y_min = top_left
    x_max, y_max = bottom_right

    # Generate random coordinates within the rectangle
    x = random.uniform(x_min, x_max)
    y = random.uniform(y_min, y_max)
    return (x,y)



def tap(position):
    print("tap!")

    # Move the mouse to the starting position of the object to be dragged
    pyautogui.moveTo(position)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    print("clickDuration: instant")
    print("clickLocation: ", position)
def dragClick(position):
    print("dragClick!")
    xTranslate = random.randint(-15,15)
    yTranslate = random.randint(-15,15)
    durationRandom = random.uniform(0.1,0.4)
    pyautogui.moveTo(position[0]+xTranslate, position[1]+yTranslate)
    pyautogui.mouseDown()
    pyautogui.dragTo(position, duration=durationRandom)
    pyautogui.mouseUp()
    print("clickDuration: ", durationRandom)
    print("clickLocation: ", position)

def dragClick2(position):
    print("dragClick2!")
    xTranslate = random.randint(-15,15)
    yTranslate = random.randint(-15,15)
    xTranslate2 = random.randint(-10,10)
    yTranslate2 = random.randint(-10,10)
    durationRandom = random.uniform(0.1,0.3)
    pyautogui.moveTo(position[0]+xTranslate, position[1]+yTranslate)
    pyautogui.mouseDown()
    pyautogui.dragTo(position, duration=durationRandom)
    durationRandom = random.uniform(0.1,0.3)
    pyautogui.moveTo(position[0]+xTranslate2, position[1]+yTranslate2)
    pyautogui.dragTo(position, duration=durationRandom)
    pyautogui.mouseUp()
    print("clickDuration: ", durationRandom)
    print("clickLocation: ", position)

def holdClick(position):
    print("holdClick!")
    durationRandom = random.uniform(0.2,0.6)
    pyautogui.moveTo(position)
    pyautogui.mouseDown()
    time.sleep(durationRandom)
    pyautogui.mouseUp()
    print("clickDuration: ", durationRandom)
    print("clickLocation: ", position)


# Create a list of functions
clickTypes = [tap, dragClick, holdClick]

if __name__ == '__main__':

    
    changeWindows("Summoners War")
    time.sleep(4)
    for i in range(REPEAT_TIMES):
        print("iteration ", i)
        print("repeat press")
        randomClickType = random.choice(clickTypes)
        randomClickType(randomPointWithinRect(REPEAT_BATTLE_DISPLAY_MON_1))
        #time.sleep(random.uniform(TIMES["giants"][0], TIMES["giants"][1]))
        detection.splitTimesAndCheckDefeated(TIMES["giants"])
        #error when on second display????
        time.sleep(3)
        print("sell 1 press")
        randomClickType = random.choice(clickTypes)
        randomClickType(randomPointWithinRect(SELL_SELECTED1_BOUNDS_DISPLAY_MON_1))
        time.sleep(random.uniform(2, 3))
        print("sell 2 press")
        randomClickType = random.choice(clickTypes)
        randomClickType(randomPointWithinRect(SELL_SELECTED2_BOUNDS_DISPLAY_MON_1))
        time.sleep(random.uniform(4, 9))

        if detection.noItemsToSell():
            print("ok press")
            randomClickType = random.choice(clickTypes)
            randomClickType(randomPointWithinRect(OK_SELL_BOUNDS_DISPLAY_MON_1))
            time.sleep(random.uniform(1,2))
            print("cancel press")
            randomClickType = random.choice(clickTypes)
            randomClickType(randomPointWithinRect(CANCEL_SELL_BOUNDS_DISPLAY_MON_1))       
        else:
            print("yes press")
            randomClickType = random.choice(clickTypes)
            randomClickType(randomPointWithinRect(YES_SELL_BOUNDS_DISPLAY_MON_1))    
        time.sleep(random.uniform(3, 5))
        print("replay press")
        randomClickType = random.choice(clickTypes)
        randomClickType(randomPointWithinRect(REPLAY_BOUNDS_DISPLAY_MON_1))
        time.sleep(random.uniform(2, 4))
    

    if SHUTDOWN:
        os.system("shutdown /s /t 1")

    


