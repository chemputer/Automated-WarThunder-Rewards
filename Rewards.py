import os
import time
import pyautogui
import sys
import random


def warthunder():
    os.startfile("E:\Steam\steamapps\common\War Thunder\win64\aces.exe")#Path to win64 aces.exe here
    a = random.randint(50,500)
    time.sleep(1000) # sleep long enough for the game to start
    time.sleep(a)
    pyautogui.press('enter') # collect reward
    a = random.randint(25,200)
    time.sleep(a) # sleep long enough for the game to start
    pyautogui.press('enter') # collect reward
    a = random.randint(25,200)
    time.sleep(a) # sleep long enough for the game to start
    pyautogui.press('enter') # collect reward
    
def killProcess():
    os.system("taskkill /f /im aces.exe")

def main():
    warthunder()
    time.sleep(random.randint(250,1000)
    killProcess()
    
if __name__ == '__main__':
    main()
