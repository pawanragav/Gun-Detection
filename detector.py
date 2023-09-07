# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 22:30:52 2023

@author: harib
"""

cfg_model="ssd_summit.pbtxt"
f_model="frozen_summit.pb"
model=cv2.dnn_DetectionModel(f_model,cfg_model)

model.setInputSize(320,320)
model.setInputScale(1.0/127.5)
model.setInputMean(127.5)
model.setInputSwapRB(True)

def lk():
    

    gun_cascade = cv2.CascadeClassifier('cascade.xml')
    camera = cv2.VideoCapture('U.S. Army Soldiers Conduct Short-Range Rifle Marksmanship Training.mp4')

    firstFrame = None


    gun_exist = False

    while True:
        (grabbed, frame) = camera.read()

        if not grabbed:
            break

        frame = imutils.resize(frame, width=500)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        gun = gun_cascade.detectMultiScale(gray, 1.3, 5, minSize = (100, 100))

        if len(gun) > 0:
            gun_exist = True

        for (x,y,w,h) in gun:
            frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]    

        if firstFrame is None:
            firstFrame = gray
            continue

        

        cv2.imshow("Security Feed", frame)
        key = cv2.waitKey(1) & 0xFF

    if gun_exist:
        print("guns detected")
        msg()
    else:
        print("guns NOT detected")

    camera.release()
    cv2.destroyAllWindows()
    
