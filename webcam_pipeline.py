import cv2
import time
import random
import pyautogui
import time
import random
import requests
import json
import pprint

camera_port = 0
camera = cv2.VideoCapture(camera_port)
def get_image():
 retval, im = camera.read()
 return im

url = 'https://dev50604.service-now.com/api/now/attachment/upload'
user = 'haripriya'
pwd = 'Haripriya@9699'
x=1
while x<2:
 camera = cv2.VideoCapture(camera_port)
 #print("Taking image...")
 camera_capture = get_image()
 file = "C:\\Users\\hp\\Desktop\\Service Now\\Screenshots\\image_new.jpg"
 cv2.imwrite(file, camera_capture)
 f = open(file, 'rb')

 files = {'image_file': f, 'Content-Type': "image/jpeg"}
 data = {'recognition_type':"face"}

 frurl = 'https://202.53.13.21:5000/api/recognize_without_bbox/'

 response = requests.post(frurl, files=files, data=data, auth = ('bhavani','tele123$'), verify=False)
 resp = json.loads(response.text)
 print(resp)
 #print(resp['result'])
 response1={}
 try:
     if(str(resp['result']) == 'no_faces_detected'):
         print("in catch")
         response1= requests.post('https://dev50604.service-now.com/api/now/table/x_474635_service_webcam',json={'user_seen':'','validation':'no user seen'},auth=('haripriya', 'Haripriya@9699')) 
         
 except:      

     split_data=resp['names_with_bboxes'][0][0].split("_")
     response1= requests.post('https://dev50604.service-now.com/api/now/table/x_474635_service_webcam',json={'user_seen':json.dumps(split_data[0].lower())},auth=('haripriya', 'Haripriya@9699')) 
 finally:
     print('here1')
     temp_files = {'photo': ('image_new.jpg', open(file, 'rb'), 'image/jpg', {'Expires': '0'})}      
     headers = {"Accept":"*/*"} 
     payload = {'table_name':'x_474635_service_webcam', 'table_sys_id':response1.json()['result']['sys_id']}
     print('here2')
     response = requests.post(url, auth=(user, pwd), headers=headers, files=temp_files, data=payload)
     print('after execution')
     del(camera)
     ran=random.randint(5,10)
     time.sleep(ran)
     x+=1
