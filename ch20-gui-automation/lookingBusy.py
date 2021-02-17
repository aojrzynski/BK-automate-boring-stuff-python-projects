#! python3
# lookingBusy.py - Moves the mouse cursor slightly every 30 seconds. 

import pyautogui, random, time

MOVEMENTS = [(1,1),(1,-1),(-1,-1),(-1, 1)]

print('Press CTRL-C or move the mouse to any corner of the screen to end the program!')
while True:
    time.sleep(30)
    pyautogui.move(random.choice(MOVEMENTS), duration=0.25)
