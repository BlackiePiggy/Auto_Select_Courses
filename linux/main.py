import pyautogui
import numpy as np
import subprocess
import cv2
import logging
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime
import matplotlib.pyplot as plt
import time

# 日志配置
log_format = '%(asctime)s - %(message)s'
logging.basicConfig(level=logging.INFO,
                    format=log_format,
                    handlers=[TimedRotatingFileHandler('logs/log', when='H', interval=1, atTime=datetime.min.time())])

# 定义截图区域的坐标和大小
left, top, width, height = 1620, 415, 50, 20

# 定义绿色的范围，这里使用RGB颜色范围
lower_green = np.array([140, 200, 200, 255])
upper_green = np.array([190, 255, 255, 255])

while True:
    # 先刷新页面
    script_command = "sh refresh.sh"
    subprocess.call(script_command, shell=True)

    #-----------------------------First Class--------------------------------
    # 搜索课程1
    script_command = "sh search_first.sh"
    subprocess.call(script_command, shell=True)
    		
    # 捕捉屏幕截图
    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    
    # 将截图转换为NumPy数组
    screenshot_np = np.array(screenshot)
    
    # 在截图中查找绿色
    mask = cv2.inRange(screenshot_np, lower_green, upper_green)
    
    # 绘制截图
    #plt.imshow(screenshot_np)
    #plt.show()
    
    # 如果检测到绿色，则执行某个Linux脚本
    if cv2.countNonZero(mask) > 0:
        script_command = "sh auto_click.sh"
        subprocess.call(script_command, shell=True)
        logging.info("**********first class green detected**********")
        print("**********first class green detected**********")
        script_command = "wget http://miaotixing.com/trigger?id=tuj1K0C"
        subprocess.call(script_command, shell=True)
            	    
    else:
        logging.info("first class green not detected")
        print("first class green not detected")
        
    time.sleep(0.5)
    #-------------------------------------------------------------------------

    #-----------------------------Second Class--------------------------------
    # 搜索课程2
    script_command = "sh search_second.sh"
    subprocess.call(script_command, shell=True)

    # 捕捉屏幕截图2
    screenshot_2 = pyautogui.screenshot(region=(left, top, width, height))

    # 将截图2转换为NumPy数组
    screenshot_2_np = np.array(screenshot_2)
    
    # 在截图中查找绿色
    mask_2 = cv2.inRange(screenshot_2_np, lower_green, upper_green)

    # 绘制截图
    #plt.imshow(screenshot_np)
    #plt.show()

    # 如果检测到绿色，则执行某个Linux脚本
    if cv2.countNonZero(mask_2) > 0:
        script_command = "sh auto_click.sh"
        subprocess.call(script_command, shell=True)
        logging.info("**********second class green detected**********")
        print("**********second class green detected**********")
        script_command = "wget http://miaotixing.com/trigger?id=tuj1K0C"
        subprocess.call(script_command, shell=True)
                    
    else:
        logging.info("second class green not detected")
        print("second class green not detected")
        
    time.sleep(0.5)
    #-------------------------------------------------------------------------
    
