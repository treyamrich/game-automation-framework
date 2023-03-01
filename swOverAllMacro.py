import subprocess
import time
import swmacros
import psutil 
import Test_Files_and_helper_functions.picToCornerCoords as pic
import pyautogui

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
        subprocess.Popen(app_path)
        time.sleep(7)
    swmacros.changeWindows("Google Play Games beta")
    time.sleep(.3)
    swcoord = swmacros.randomPointWithinRect(pic.picToCornerCoords("images\\navigateToCaiross\swIcon.png"))
    pyautogui.moveTo(swcoord)
    time.sleep(.3)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    time.sleep(.5)
    swPlayCoord = swmacros.randomPointWithinRect(pic.picToCornerCoords("images\\navigateToCaiross\swPlay.png"))
    pyautogui.moveTo(swPlayCoord)
    time.sleep(.3)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    time.sleep(.5)
def runScript(scriptPath):
    # Use the Popen function to run the Python file
    p = subprocess.Popen(["python", cairossScript], stdin=subprocess.PIPE, stdout=subprocess.PIPE)


if __name__ == '__main__':
    openSW()
