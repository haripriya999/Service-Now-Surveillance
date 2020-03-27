import pyautogui
import time
import random
import requests
import json
import pprint

url = 'https://dev50604.service-now.com/api/now/attachment/upload'
user = 'admin'
pwd = 'Haripriya@9699'
x=1
while x<2:
    img = pyautogui.screenshot()
    print(type(img))
    pyautogui.screenshot('\\Users\\hp\\Desktop\\Service Now\\Screenshots\\issue_screenshot.JPG')
    files = {'file': ('issue_screenshot.JPG', open('\\Users\\hp\Desktop\\Service Now\\Screenshots\\issue_screenshot.JPG', 'rb'), 'image/jpg', {'Expires': '0'})}
    headers = {"Accept":"*/*"}
    # Send the HTTP request to create record
    response1= requests.post('https://dev50604.service-now.com/api/now/table/x_474635_service_screenshots',auth=('admin', 'Haripriya@9699'))
    print(response1.json())
    payload = {'table_name':'x_474635_service_screenshots', 'table_sys_id':response1.json()['result']['sys_id']}
    # Send the HTTP request to upload screenshot to the record
    response = requests.post(url, auth=(user, pwd), headers=headers, files=files, data=payload)
    x+=1
    t=random.randrange(300,600,1)
    time.sleep(t)
