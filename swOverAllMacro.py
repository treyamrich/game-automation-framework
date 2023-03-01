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
        
    # Wait for 1 second to give you time to switch to the desired window
    time.sleep(1)

    time.sleep(3)
    swcoord = swmacros.randomPointWithinRect(pic.picToCornerCoords("images\\navigateToCaiross\swIcon.png"))
    pyautogui.moveTo(swcoord)
    time.sleep(.3)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    time.sleep(3)
    swPlayCoord = swmacros.randomPointWithinRect(pic.picToCornerCoords("images\\navigateToCaiross\swPlay.png"))
    pyautogui.moveTo(swPlayCoord)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    time.sleep(10)

    window = win32gui.FindWindow(None, "Summoners War")

    # Switch to the window and maximize it
    if window:
        win32gui.ShowWindow(window, win32con.SW_MAXIMIZE)
        win32gui.SetForegroundWindow(window)
    time.sleep(30)
    while(True):
        if(pic.picToCornerCoords("images\\navigateToCaiross\\notice_dont_show_again.png") != []):
            noticeCoords = swmacros.randomPointWithinRect(pic.picToCornerCoords("images\\navigateToCaiross\\notice_dont_show_again.png"))
            time.sleep(1)
            randomClickType = random.choice(swmacros.clickTypes)
            randomClickType(swmacros.randomPointWithinRect(noticeCoords))   
        else:
            break

def runScript(scriptPath):
    # Use the Popen function to run the Python file
    p = subprocess.Popen(["python", cairossScript], stdin=subprocess.PIPE, stdout=subprocess.PIPE)


if __name__ == '__main__':
    openSW()
