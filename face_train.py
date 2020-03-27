import os
from PIL import Image
import cv2
import numpy as np
import pickle

base_dir = os.path.dirname(os.path.abspath(__file__))
image_dir=os.path.join(base_dir,"images")

c_id=0
label_id={}

x_train=[]
y_label=[]

face_cascade=cv2.CascadeClassifier('\\Users\\hp\\Desktop\\Service Now\\cascades\\data\\haarcascade_frontalface_alt2.xml')
recognizer =cv2.face.LBPHFaceRecognizer_create()

for root,dirs,files in os.walk(image_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpeg"):
            path=os.path.join(root,file)
            label=os.path.basename(os.path.dirname(path)).replace(" ","-").lower()
            #print(label,path)
            if not label in label_id:
                label_id[label]=c_id
                c_id+=1
                #print("in if not")
                
            cur_id=label_id[label]

            pil_image=Image.open(path).convert("L") #convert grayscale
            size=(550,550)
            final_image=pil_image.resize(size,Image.ANTIALIAS)
            image_array =np.array(pil_image,"uint8")
            faces =face_cascade.detectMultiScale(image_array, scaleFactor=1.1,minNeighbors=3)
            
            for (x,y,w,h) in faces:
                roi=image_array[y:y+h,x:x+w]
                x_train.append(roi)
                y_label.append(cur_id)


with open("labels.pickle","wb") as f:
    pickle.dump(label_id,f)

recognizer.train(np.array(x_train),np.array(y_label))
recognizer.save("model.yml")
