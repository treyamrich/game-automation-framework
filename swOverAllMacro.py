import subprocess
import time
import swmacros
import psutil 
import Test_Files_and_helper_functions.picToCornerCoords as pic
import pyautogui
import random 
import os
import win32gui
import win32con

ENERGY_REFILL = False


def waitForImg(imgPath):
    while True:
        if(pic.picToCornerCoords(imgPath) != []):
            coords = pic.picToCornerCoords(imgPath)
            time.sleep(1)
            randomClickType = random.choice(swmacros.clickTypes)
            randomClickType(swmacros.randomPointWithinRect(coords))   
            break
        else:
            time.sleep(1)
    return

def check_if_app_running(app_name):
    for p in psutil.process_iter():
        try:
            if p.name().lower() == app_name.lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

# Replace the string with the path to the application you want to open
cairossScript = "swmacros.py"
app_path = "C:\Program Files\Google\Play Games\Bootstrapper.exe"


def openSW():
    # Use the Popen function to start the application
    if not check_if_app_running("Google Play Games beta.exe"):
        os.startfile(app_path)
        time.sleep(7)
        # Find the window you want to maximize by its title
        window = win32gui.FindWindow(None, "Google Play Games beta")

        # Switch to the window and maximize it
        if window:
            win32gui.ShowWindow(window, win32con.SW_MAXIMIZE)
            win32gui.SetForegroundWindow(window)
    else:
        print("close the gaddamn program")
        
    while True:
        if(pic.picToCornerCoords("images\\navigateToCaiross\swIcon.png") != []):
            swIconCoords = pic.picToCornerCoords("images\\navigateToCaiross\swIcon.png")
            print(swIconCoords)
            time.sleep(1)
            randomClickType = random.choice(swmacros.clickTypes)
            randomClickType(swmacros.randomPointWithinRect(swIconCoords))   
            break
        else:
            time.sleep(1)
    time.sleep(5)
    waitForImg("images\\navigateToCaiross\swPlay.png")
    time.sleep(10)

    window = win32gui.FindWindow(None, "Summoners War")

    # Switch to the window and maximize it
    if window:
        win32gui.ShowWindow(window, win32con.SW_MAXIMIZE)
        win32gui.SetForegroundWindow(window)
    time.sleep(30)
    waitForImg("images\\navigateToCaiross\\notice_dont_show_again.png")
    time.sleep(random.uniform(1,3))
    touchToPlay = pic.picToCornerCoords("images\\navigateToCaiross\\touch_to_start.png")
    randomClickType = random.choice(swmacros.clickTypes)
    randomClickType(swmacros.randomPointWithinRect(touchToPlay)) 
    time.sleep(random.uniform(1,3))
    monthlyX = pic.picToCornerCoords("images\\navigateToCaiross\monthly_event_X.png")
    randomClickType = random.choice(swmacros.clickTypes)
    randomClickType(swmacros.randomPointWithinRect(monthlyX)) 
    time.sleep(random.uniform(1,3))
    giftX = pic.picToCornerCoords("images\\navigateToCaiross\giftboxX.png")
    randomClickType = random.choice(swmacros.clickTypes)
    randomClickType(swmacros.randomPointWithinRect(giftX)) 
    
    #if there are events keep pressing x
    while(True):
        if(pic.picToCornerCoords("images\\navigateToCaiross\giftboxX.png") != []):
            otherX = pic.picToCornerCoords("images\\navigateToCaiross\giftboxX.png")
            time.sleep(random.uniform(1,3))
            randomClickType = random.choice(swmacros.clickTypes)
            randomClickType(swmacros.randomPointWithinRect(otherX))   
        else:
            break


    time.sleep(random.uniform(1,3))
    navigationBattle = pic.picToCornerCoords("images\\navigateToCaiross\\navigaton_battle.png")
    randomClickType = random.choice(swmacros.clickTypes)
    randomClickType(swmacros.randomPointWithinRect(navigationBattle)) 
    time.sleep(random.uniform(1,3))
    caiross = pic.picToCornerCoords("images\\navigateToCaiross\caiross.png")
    swmacros.tap((swmacros.randomPointWithinRect(caiross))) 
    time.sleep(random.uniform(1,3))
    caiross = pic.picToCornerCoords("images\\navigateToCaiross\giants12battle.png")
    randomClickType = random.choice(swmacros.clickTypes)
    randomClickType(swmacros.randomPointWithinRect(caiross)) 


def runScript(scriptPath):
    # Use the Popen function to run the Python file
    p = subprocess.Popen(["python", cairossScript], stdin=subprocess.PIPE, stdout=subprocess.PIPE)


if __name__ == '__main__':
    if(ENERGY_REFILL == False):
        openSW()
        runScript(cairossScript)
    else:
        #TODO implement energy stoppage after repetitive X's on island
        print("TODO")
