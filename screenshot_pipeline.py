import pyautogui
import time
import random
import requests
import json
import pprint


url = 'https://dev50604.service-now.com/api/now/attachment/upload'
user = 'haripriya'
pwd = 'Haripriya@9699'
def ocr_test():
    f = open("C:\\Users\\hp\\Desktop\\Service Now\\Screenshots\\Screenshot.png", 'rb')
    files = {'image_file': f, 'Content-Type': "image/jpeg"}

    frurl = 'http://202.53.13.21:8000/api/extract_text_from_image/'

    response = requests.post(frurl, files=files, auth = ('bhavani','tele123$'), verify=False)
    resp = json.loads(response.text)
    print(resp)

def ocr_bool_test():
    f = open("C:\\Users\\hp\\Desktop\\Service Now\\Screenshots\\Screenshot.png", 'rb')
    files = {'image_file': f, 'Content-Type': "image/jpeg"}
    data = {'required_text':"ServiceNow"}

    frurl = 'http://202.53.13.21:8000/api/is_text_in_image/'

    response = requests.post(frurl, files=files, data=data, auth = ('bhavani','tele123$'), verify=False)
    resp = json.loads(response.text)
    print(resp['result'])
    
    files = {'file': ('screenshot.png', open('\\Users\\hp\Desktop\\Service Now\\Screenshots\\Screenshot.png', 'rb'), 'image/jpg', {'Expires': '0'})}
    headers = {"Accept":"*/*"}
    response1={}
    # Send the HTTP request to create record
    if(str(resp['result'])=='True'):
        response1= requests.post('https://dev50604.service-now.com/api/now/table/x_474635_service_screenshots',json={'productivity':'productive'},auth=('haripriya', 'Haripriya@9699'))
    else:
        response1= requests.post('https://dev50604.service-now.com/api/now/table/x_474635_service_screenshots',json={'productivity':'non-productive'},auth=('haripriya', 'Haripriya@9699'))
    
    print(response1.json())
    payload = {'table_name':'x_474635_service_screenshots', 'table_sys_id':response1.json()['result']['sys_id']}
    # Send the HTTP request to upload screenshot to the record
    response = requests.post(url, auth=(user, pwd), headers=headers, files=files, data=payload) 
    

x=1
while x<10:
    time.sleep(3)
    pyautogui.screenshot('\\Users\\hp\Desktop\\Service Now\\Screenshots\\Screenshot.png')
    #ocr_test()
    ocr_bool_test()    
    x+=1
    t=random.randrange(1,3,1)
    time.sleep(t)

