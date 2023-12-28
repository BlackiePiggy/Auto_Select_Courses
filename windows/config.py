# config.py
import pyautogui as pg

# 可选分辨率
# 1920*1080
if (pg.size()[0]==1920)&(pg.size()[1]==1080):
    resolution = "1920x1080"
# 1620*1080
elif (pg.size()[0]==1620)&(pg.size()[1]==1080):
    resolution = "1620x1080"