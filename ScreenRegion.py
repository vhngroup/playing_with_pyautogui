from pyautogui import *
import pyautogui
import os
import time
import keyboard
import random
import win32api, win32con #if you OS is Windows
import mouse #other option to pyautogui

iml = pyautogui.screenshot (region=(390,275,590,448)) #coordenates for area to screenshot
iml.save(r"G:\Mi unidad\VHNGROUP\10. Otros Proyectos\Git\Resolver_Juegos_pyautogui\saved.png") # save route

#pyautogui.displayMousePosition() #when you want coordinates for mouse position and RGB color in your screen