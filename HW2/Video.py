# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 09:15:07 2020

@author: ST16
"""
import os
import cv2
import cv2 as cv
import numpy as np
from datetime import datetime
#import matplotlib.pyplot as plt
#import matplotlib.image as mpimg

 
#Make a New Subfloder
if not os.path.isdir("./Saved Image"):
    #print("New Dir")
    os.makedirs("./Saved Image")

#Initialize
group = 0
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
kernel = np.ones((7,7),np.uint8)


while(1):

    
    # Take each frame
    _, frame = cap.read()
    
    
    
    if group == 0:
        img1 = frame
        img2 = frame
        img3 = frame
    if group == 1:
        (img1,img2,img3) = cv2.split(frame)
        img1 = cv2.cvtColor(img1, cv2.COLOR_GRAY2BGR)
        img2 = cv2.cvtColor(img2, cv2.COLOR_GRAY2BGR)
        img3 = cv2.cvtColor(img3, cv2.COLOR_GRAY2BGR)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
    if group == 2:
        img1 = cv2.flip(frame, 1)
        img2 = cv2.flip(frame, 0)
        img3 = cv2.flip(frame, -1)
        
    
    h1 = np.hstack((frame,img1))
    h2 = np.hstack((img2,img3))
    quard = np.vstack((h1,h2))
    
    if group == 0 or group == 2:
        Text1 = " "
        Text2 = " "
        Text3 = " "
        Text4 = " "
    if group == 1:
        Text1 = "Gray"
        Text2 = "Blue"
        Text3 = "Green"
        Text4 = "Red"
    
    text_size = 3
    cv2.putText(quard, Text1, (15, 40+30), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,text_size, (0, 0, 0), 3, cv2.LINE_AA)
    cv2.putText(quard, Text2, (655, 40+30), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,text_size, (0, 0, 0), 3, cv2.LINE_AA)
    cv2.putText(quard, Text3, (15, 520+30), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,text_size, (0, 0, 0), 3, cv2.LINE_AA)
    cv2.putText(quard, Text4, (655, 520+30), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,text_size, (0, 0, 0), 3, cv2.LINE_AA)
    cv2.putText(quard, Text1, (15, 40+30), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,text_size, (255, 255, 255), 1, cv2.LINE_AA)
    cv2.putText(quard, Text2, (655, 40+30), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,text_size, (255, 255, 255), 1, cv2.LINE_AA)
    cv2.putText(quard, Text3, (15, 520+30), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,text_size, (255, 255, 255), 1, cv2.LINE_AA)
    cv2.putText(quard, Text4, (655, 520+30), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,text_size, (255, 255, 255), 1, cv2.LINE_AA)
    
    #cv2.circle(frame,(200,200 + group*10),50,(0, 0, 0), -1)
    
    cv2.namedWindow('Orignal', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Orignal', 960, 720) 
    cv2.imshow('Orignal',quard)
        
    
    key = cv2.waitKeyEx(5)
    #print(key)
    """
    Please uncomment "print(key)" to chack arrow key value 
    when arrow key does not working correctly  
    2555904(Rrght Arrow) 
    2424832(Left Arrow)
    """
    if key == 2555904:
        if group > 3:
            group = 4
        else:
            group += 1
    if key == 2424832:
        if group <= 0:
            group = 0;
        else:
            group -= 1
    if key == 32:
        now = datetime.now()
        current_time = now.strftime("%Y_%m%d_%H%M%S")
        cv.imwrite('Saved Image/'+current_time+'.jpg',frame)
        cv.imwrite('Saved Image/'+current_time+'quard.jpg',quard)
        #print(current_time)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
