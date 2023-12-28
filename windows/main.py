import pyautogui as pg
import numpy as np
import subprocess
import cv2
import logging
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime
import matplotlib.pyplot as plt
import time
import win_gui
import requests
from PIL import ImageGrab
from config import resolution
import os

# 定义截图区域的坐标和大小
if resolution == "1920x1080":
    left, top, width, height = 1600, 385, 50, 20
elif resolution == "1620x1080":
    left, top, width, height = 1333, 385, 50, 20

# 日志配置
if not os.path.exists('./logs'):
    os.makedirs('./logs')
    print("The 'logs' folder was not found and has been created.")

log_format = '%(asctime)s - %(message)s'
logging.basicConfig(level=logging.INFO,
                    format=log_format,
                    handlers=[TimedRotatingFileHandler('./logs/log', when='H', interval=1, atTime=datetime.min.time())])

# 定义绿色的范围，这里使用RGB颜色范围
lower_green = np.array([100, 200, 200])
upper_green = np.array([104, 208, 208])

while True:
    # 先刷新页面
    win_gui.refresh()
    win_gui.check_unlogin()

    #-----------------------------First Class--------------------------------
    # 搜索课程1
    win_gui.search_first_class()
    		
    # 捕捉屏幕截图
    screenshot = pg.screenshot(region=(left, top, width, height))
    
    # 将截图转换为NumPy数组
    screenshot_np = np.array(screenshot)
    
    # 在截图中查找绿色
    mask = cv2.inRange(screenshot_np, lower_green, upper_green)
    
    # 如果检测到绿色，则执行某个Linux脚本
    if cv2.countNonZero(mask) > 0:
        win_gui.auto_click()
        logging.info("**********first class green detected**********")
        print("**********first class green detected**********")
        r = requests.get('http://miaotixing.com/trigger?id=tuj1K0C')

        break
            	    
    else:
        logging.info("first class green not detected")
        print("first class green not detected")
        
    time.sleep(0.5)
    #-------------------------------------------------------------------------

    #-----------------------------Second Class--------------------------------
    # 搜索课程2
    win_gui.search_second_class()

    # 捕捉屏幕截图2
    screenshot_2 = pg.screenshot(region=(left, top, width, height))

    # 将截图2转换为NumPy数组
    screenshot_2_np = np.array(screenshot_2)
    
    # 在截图中查找绿色
    mask_2 = cv2.inRange(screenshot_2_np, lower_green, upper_green)

    # 如果检测到绿色，则执行某个Linux脚本
    if cv2.countNonZero(mask_2) > 0:

        # 获取屏幕截图
        screenshot = ImageGrab.grab()
        # 获取当前时间作为文件名
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_name = f"screenshot_{current_time}.png"
        # 保存截图
        screenshot.save(file_name)
        print(f"截图已保存为 {file_name}")

        win_gui.auto_click()
        logging.info("**********second class green detected**********")
        print("**********second class green detected**********")
        r = requests.get('http://miaotixing.com/trigger?id=tuj1K0C')

        break
                    
    else:
        logging.info("second class green not detected")
        print("second class green not detected")
        
    time.sleep(0.5)
    #-------------------------------------------------------------------------
    