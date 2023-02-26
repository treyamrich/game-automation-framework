
# Summoners War Auto-farmer
*Author: Kevin Khong*

This Python script is designed to automate repetitive tasks in the mobile game Summoners War. The script can be used to automatically farm the Giants dungeon, sell unwanted items, and replay battles.

## Requirements
The following Python packages are required to run this script:

pyautogui
time
random
win32gui
win32con
Usage
To use the script, simply run the following command:

Copy code
python SummonersWarAutoFarmer.py

The script will automatically launch Summoners War and perform the specified actions. The default settings are set to farm the Giants dungeon 7 times, sell unwanted items, and replay battles.

## Features
The script includes the following features:

Randomized clicking and dragging to avoid detection
Image recognition and detection to check for defeated monsters
Automatic selling of unwanted items
Automatic replaying of battles
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