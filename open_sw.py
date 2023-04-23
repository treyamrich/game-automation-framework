import psutil 
import sys
import time
import random
import subprocess
from util.input_handler import VirtualInputHandler

SCRIPT_NAME = 'open_sw'
BLUE_STACKS_PATH = 'C:\Program Files\BlueStacks_nxt\HD-Player.exe'
BLUE_STACKS_ARGS = [BLUE_STACKS_PATH, '--instance', 'Pie64', '--cmd', 'launchApp', '--package', 'com.com2us.smon.normal.freefull.google.kr.android.common']

bot = VirtualInputHandler(SCRIPT_NAME, log_serverity_level='warning')
brief_random_sleep = lambda : time.sleep(random.uniform(1, 3))

def is_app_running(app_name: str):
    for p in psutil.process_iter():
        try:
            if p.name().lower() == app_name.lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def launch_bluestacks():
    try:
        subprocess.Popen(BLUE_STACKS_ARGS)
    except FileNotFoundError as err:
        bot.logger.critical(f'{err.returncode}')
        exit(1)
    time.sleep(50)
    bot.change_window('BlueStacks App Player', expand=True)
    time.sleep(20)

def navigate_home_screen():
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
    
    if is_app_running(BLUE_STACKS_PATH):
        sys.stderr.write(f'{BLUE_STACKS_PATH} is already running.')
        exit(1)
    
    launch_bluestacks()
    navigate_home_screen()
    close_popups()
