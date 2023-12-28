import pyautogui as pg
import pyperclip as pc
import time
import numpy as np
import logging
import cv2
from config import resolution

def search_first_class():
    if resolution == "1920x1080":
        pg.moveTo(468,207)
    elif resolution == "1620x1080":
        pg.moveTo(351,207)

    pg.click()

    # Delete search area
    pg.hotkey('ctrl','a')
    pg.press('Delete')

    # Add paste word
    pc.copy('人工智能的数学基础')

    # Paste
    pg.hotkey('ctrl','v')

    if resolution == "1920x1080":
        pg.moveTo(968,277)
    elif resolution == "1620x1080":
        pg.moveTo(804,277)
    # Search
    
    pg.click()

    time.sleep(0.5)

def search_second_class():
    # Move ti search area
    if resolution == "1920x1080":
        pg.moveTo(468,207)
    elif resolution == "1620x1080":
        pg.moveTo(351,207)
    pg.click()

    # Delete search area
    pg.hotkey('ctrl','a')
    pg.press('Delete')

    # Add paste word
    pc.copy('动态测试分析')

    # Paste
    pg.hotkey('ctrl','v')

    # Search
    if resolution == "1920x1080":
        pg.moveTo(968,277)
    elif resolution == "1620x1080":
        pg.moveTo(804,277)
    pg.click()

    time.sleep(0.5)
    
def tui_ke():
    pg.moveTo(817,119)
    pg.click()
    
    time.sleep(0.5)
    
    pg.moveTo(1444,277)
    pg.click()
    
    pg.moveTo(831,622)
    pg.click()
    
    pg.moveTo(363,118)
    pg.click()

def auto_click():
    time.sleep(0.5)
    # line 1 
    if resolution == "1920x1080":
        pg.moveTo(1723,395)
    elif resolution == "1620x1080":
        pg.moveTo(1446,395)
    # line 2
    pg.click()
    time.sleep(0.5)
    if resolution == "1920x1080":
        pg.moveTo(1000,629)
    elif resolution == "1620x1080":
        pg.moveTo(836,629)
    pg.click()
    time.sleep(0.5)
    if resolution == "1920x1080":
        pg.moveTo(1100,632)
    elif resolution == "1620x1080":
        pg.moveTo(952,632)
    pg.click()
    time.sleep(0.5)

def refresh():
    if resolution == "1920x1080":
        pg.moveTo(196,228)
    elif resolution == "1620x1080":
        pg.moveTo(152,228)

    pg.click()
    pg.press('F5')

    time.sleep(1.5)

def check_unlogin():
    lower_red = np.array([226,  67,  52])
    upper_red = np.array([229,  93,  83])
    
    if resolution == "1920x1080":
        checkshot = pg.screenshot(region=(887, 183, 200, 40))
    elif resolution == "1620x1080":
        checkshot = pg.screenshot(region=(735, 183, 100, 40))
        
    checkshot = np.array(checkshot)
    mask_red = cv2.inRange(checkshot, lower_red, upper_red)
    
    if cv2.countNonZero(mask_red) > 0:
        logging.info("**********Restarting logging in......**********")
        print("**********Restarting logging in......**********")
        if resolution == "1920x1080":
            pg.moveTo(958,245)
        elif resolution == "1620x1080":
            pg.moveTo(810,245)
        pg.click()
        
        time.sleep(1)
        
        if resolution == "1920x1080":
            pg.moveTo(1078,620)
        elif resolution == "1620x1080":
            pg.moveTo(934,620)
        pg.click()
        
        time.sleep(1)
        
        if resolution == "1920x1080":
            pg.moveTo(1407,525)
        elif resolution == "1620x1080":
            pg.moveTo(1261,525)
        pg.click()
        
        time.sleep(1)
        
        