import pyautogui
import time
import random

x=1
while x<4:
    pyautogui.screenshot('\\Users\\hp\Desktop\\Service Now\\Screenshots\\image'+str(x)+'.png')
    x+=1
    t=random.randrange(1,3,1)
    time.sleep(t)
    


