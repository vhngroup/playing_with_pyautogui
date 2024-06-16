from pyautogui import *
import pyautogui
import os
import time
import keyboard
import random
import win32api, win32con #if you OS is Windows
import mouse #other option to pyautogui

# Position Columns and carrers
# 587 415 4
# 498 407 3
# 416 414 2
# 332 429 1

def clickwindows(x,y): #for Windows
    win32api.SetCursor((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0,0)

def clickotherSO(x,y): #for other SO
    pyautogui.mouseDown(x, y, button="left", duration=duracion)
    time.sleep(0.003)
    pyautogui.mouseUp(button="left")

duracion = 0.005 # Time to sleep mouse move
while keyboard.is_pressed('q') == False:
    if os.name == 'nt' == True: #Detect what OS is current the script
        if pyautogui.pixel(587, 400) [0] == 0:
            clickwindows(587, 400)
        if pyautogui.pixel(498, 400) [0] == 0:
            clickwindows(498, 400)
        if pyautogui.pixel(416, 400) [0] == 0:
            clickwindows(416, 400)
        if pyautogui.pixel(332, 400) [0] == 0:
            clickwindows(332, 400)
    else: #For Linux
        if pyautogui.pixel(560, 337) [0] == 0:
            clickotherSO(560, 337)
        if pyautogui.pixel(503, 337) [0] == 0:
            clickotherSO(503, 337)
        if pyautogui.pixel(426, 337) [0] == 0:
            clickotherSO(426, 337)
        if pyautogui.pixel(341, 337) [0] == 0:
            clickotherSO(341, 337)
        mouse.on_click(lambda: print("Left Button clicked.")) #Status click