
# Summoners War Automation
*Author: Kevin Khong*
*Co-author: Trey Amrich*

This repository is a simple framework that will let you create bots for automating any task. The focus was for automation is the game Summoners War,
however, this framework can be used for other games / tasks that require sending clicks / keyboard presses. 

## Requirements
The following Python packages are required to run this script:

- pyautogui
- time
- random
- win32gui
- win32con

## Quick Start
The script `run_my_scripts.py` is the main script you will want to run each time. This file will use a `ScriptQueue` that runs all your scripts in series.
To create a script, make sure to import the `VirtualInputHandler` from the `util` directory. This class abstracts clicking and image detection to make
your script code more simple.

*If you are using this repo for Summoners War, leave the `open_sw` script inside the `run_my_scripts.py` file. That script will automatically open the game
and click through popups for you.*

## Features
The framework includes the following features with Summoners War as the main focus:

-Randomized clicking and dragging to avoid detection
-Image recognition and detection to check for defeated monsters
-Automatic selling of unwanted items
-Automatic replaying of battles

## Customization
The script can be easily customized to perform different actions or to farm different dungeons. Simply edit the values in the following variables to adjust the script's behavior:

**REPEAT_TIMES**: The number of times to repeat the dungeon run
**TIMES**: The minimum and maximum times to wait for different actions
**REPEAT_BATTLE_DISPLAY_MON_1**: The coordinates of the "repeat battle" button
**REPLAY_BOUNDS_DISPLAY_MON_1**: The coordinates of the "replay" button
**SELL_SELECTED1_BOUNDS_DISPLAY_MON_1**: The coordinates of the first item to sell
**SELL_SELECTED2_BOUNDS_DISPLAY_MON_1**: The coordinates of the second item to sell
**YES_SELL_BOUNDS_DISPLAY_MON_1**: The coordinates of the "yes" button when selling items
**OK_SELL_BOUNDS_DISPLAY_MON_1**: The coordinates of the "ok" button when no items are available to sell
**CANCEL_SELL_BOUNDS_DISPLAY_MON_1**: The coordinates of the "cancel" button when no items are available to sell
## Disclaimer
This script is intended for educational and research purposes only. Using this script to cheat or violate the terms of service of Summoners War is strictly prohibited and can result in the suspension or termination of your account. Use at your own risk.

## Arena Script
The Python script swarenamacros.py is designed to automate the arena rivals process

**DEPENDENCIES:**
Searches for buttons via pyautogui's image detection and is subject to change given art and model changes via COM2US updates.
Automates scrolling, and needs a functioning tricaru team in the first arena monster team in order to function.
You can use this script as a starting point to automate other tasks in the game or modify it to suit your specific needs. However, keep in mind that automating games is against the terms of service of most games and could lead to your account being banned. So, use this script at your own risk.

TODO: for the current arena script, changes needed to be made in order to add an if else detection for the tricaru team in orer to save time.

# Overall Navigation Script
Located in swOverAllMacro.py

This is a Python script that automates the process of opening and navigating to a specific area in the mobile game "Summoners War". The script is designed to be an overall navigation script that encompasses other script uses.

## Features
The script uses several libraries, including PyAutoGUI, psutil, and win32gui, to automate the process of opening the game, navigating to the Caiross dungeon area, and clicking through pop-up notifications and other events that may be present on the screen. The script can also navigate to specific areas within the Caiross dungeon, such as the Giants 12 battle area.
In addition to its main navigation features, the script also includes a number of helper functions for image recognition and random clicking, as well as an optional feature for implementing energy stoppage after repetitive X's on the island.

## Usage
To use the script, simply run it using the following command:
python swOverAllMacro.py

## TODO: 
Future changes will include the addition of a graphical user interface for ease of use, and abstraction for those unfamiliar with code.
