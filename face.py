import numpy as np
import cv2
import pickle

cap=cv2.VideoCapture(0)

def change_resolution(width,height):
    cap.set(3,width)
    cap.set(4,height)

#change_resolution(x,y)

def rescale_frame(frame,percent=75):
    scale_percent=75
    width= int(frame.shape[1]*scale_percent/100)
    height= int(frame.shape[0]*scale_percent/100)
    dim=(width,height)
    return cv2.resize(frame,dim,interpolation=cv2.INTER_AREA)

face_cascade=cv2.CascadeClassifier('\\Users\\hp\\Desktop\\Service Now\\cascades\\data\\haarcascade_frontalface_alt2.xml')
recognizer =cv2.face.LBPHFaceRecognizer_create()
recognizer.read("model.yml")

labels = {}
with open("labels.pickle","rb") as f:
    labels=pickle.load(f)
    labels={v:k for k,v in labels.items()}

count=0
while(True):
    print('in here')
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray, scaleFactor=1.1,minNeighbors=3)
    for(x,y,w,h) in faces:
        print('in for')

        roi_gray =gray[y:y+h,x:x+w]
        c_id,conf =recognizer.predict(roi_gray)   #label and confidence

        if conf>=45: #and conf<=85:
            print(labels[c_id])
            font=cv2.FONT_HERSHEY_SIMPLEX
            name=labels[c_id]
            color=(255,255,255)
            stroke=2
            cv2.putText(frame,name,(x,y),font,1,color,stroke,cv2.LINE_AA)
            

        
        color=(0,255,0)             #color of rectangle
        stroke=1                    #thickness of rectangle
        cv2.rectangle(frame,(x,y),(x+w,y+h),color,stroke)  #frame, starting co-ordinates, ending co-ordinates, color and stroke
        
        cv2.imshow('frame',frame)
       
        cv2.imwrite('\\Users\\hp\\Desktop\\Service Now\\Screenshots\\my-image.png',frame)  

    
    if cv2.waitKey(20) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
