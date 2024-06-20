#Esta es una prueba para entender como funciona pyautogui, el programa busca la imagen indicada en el archivo men.png
from pyautogui import *
import pyautogui
import os
import time
import keyboard
import random
import win32api, win32con #if you OS is Windows
import mouse #other option to pyautogui

screenWidth, screenHeight = pyautogui.size()
while keyboard.is_pressed("q") == False:
    try:    
        if pyautogui.locateOnScreen('men.png', region=(0,0, screenWidth, screenHeight), confidence=0.7) != None:
            print("He Detectado al hombre")
            time.sleep(0.5)
        else:
            print("No he Detectado al hombre")
            time.sleep(0.5)
    except pyautogui.ImageNotFoundException as e:
        print("Error: La imagen esta abierta y visible?")
        pass
