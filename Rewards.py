import os
import time
import pyautogui
import sys



def warthunder():
    os.startfile("E:\Steam\steamapps\common\War Thunder\win64\aces.exe")#Path to win64 aces.exe here
    time.sleep(1000) # sleep long enough for the game to start
    pyautogui.press('enter') # collect reward


def killProcess():
    os.system("taskkill /f /im aces.exe")

def main():
    warthunder()
    time.sleep(500)
    killProcess()
    
if __name__ == '__main__':
    main()
