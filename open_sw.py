import psutil 
import sys
import os
import time
import random
from util.input_handler import VirtualInputHandler

SCRIPT_NAME = 'open_sw'
APP_PATH = "C:\Program Files\Google\Play Games\Bootstrapper.exe"
APP_NAME = "Google Play Games beta.exe"

bot = VirtualInputHandler(SCRIPT_NAME, log_level='warning')
brief_random_sleep = lambda : time.sleep(random.uniform(1, 3))

def is_app_running(app_name: str):
    for p in psutil.process_iter():
        try:
            if p.name().lower() == app_name.lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def launch_game():
    os.startfile(APP_PATH)
    time.sleep(7)
    bot.change_window("Google Play Games beta")
    bot.wait_for_image('swIcon.png')
    time.sleep(5)
    bot.wait_for_image('swPlay.png')
    time.sleep(10)

def navigate_home_screen():
    bot.change_window('Summoners War')
    time.sleep(30)
    #Click through the rest
    while bot.click_image('dont_show_again.png'): 
        brief_random_sleep()
        pass
    brief_random_sleep()
    bot.click_image('touch_to_start.png')
    brief_random_sleep()

def close_popups():
    while bot.click_image('close_popup.png'):
        brief_random_sleep()
        pass
    
def test_image():
    bot.change_window("Google Play Games beta")
    bot.click_image('notice_dont_show_again.png')

if __name__ == '__main__':
    
    if is_app_running(APP_NAME):
        sys.stderr.write(f'{APP_NAME} is already running.')
        exit(1)
    launch_game()
    navigate_home_screen()
    close_popups()
