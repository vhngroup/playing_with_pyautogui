#Boot with play game of the web aimbooster.com
#Esta es una prueba para entender como funciona pyautogui, el programa busca la imagen indicada en el archivo men.png
from pyautogui import *
import pyautogui
import os
import time
import keyboard
import random
import win32api, win32con #if you OS is Windows
import mouse #other option to pyautogui

time.sleep(2) #Time for launch the program

def clickwindows(x,y): #for Windows
    win32api.SetCursor((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0,0)

def clickotherSO(x,y): #for other SO
    pyautogui.mouseDown(x, y, button="left", duration=duracion)
    time.sleep(0.005)
    pyautogui.mouseUp(button="left")
duracion = 0.04 # Time to sleep mouse move

#Color point of target 255, 219, 195

while keyboard.is_pressed('q') == False:
    pic = pyautogui.screenshot (region=(390,275,590,448)) #saved the area when the interaction game.
    width, heigth = pic.size
    for x in range (0, width, 5):
        for y in range (0,heigth, 5):
            r,g,b = pic.getpixel((x,y))
            if os.name == 'nt' == True: #Detect what OS is current the script
                if r == 255 and b == 195:
                    clickwindows(x+390, y+275)
                    break
            else:
                if r== 255 and g == 219 and b == 195 :
                    clickotherSO(x+390, y+275)
                    print(f"hace click x {x} , Y {y}")
                    break