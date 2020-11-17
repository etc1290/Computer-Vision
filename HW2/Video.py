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
from PIL import ImageFont, ImageDraw, Image
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

b,g,r,a = 255,255,255,0
font = ImageFont.truetype("TaipeiSansTCBeta-Bold.ttf", 470)
mask0 = np.zeros((480,640,3),np.uint8)
img_pil = Image.fromarray(mask0)
draw = ImageDraw.Draw(img_pil)
draw.text((100, 0),  "聖", font = font, fill = (b, g, r, a))
mask0 = np.array(img_pil)

mask1 = np.zeros((480,640,3),np.uint8)
img_pil = Image.fromarray(mask1)
draw = ImageDraw.Draw(img_pil)
draw.text((100, 0),  "誕", font = font, fill = (b, g, r, a))
mask1 = np.array(img_pil)

mask2 = np.zeros((480,640,3),np.uint8)
img_pil = Image.fromarray(mask2)
draw = ImageDraw.Draw(img_pil)
draw.text((100, 0),  "快", font = font, fill = (b, g, r, a))
mask2 = np.array(img_pil)

mask3 = np.zeros((480,640,3),np.uint8)
img_pil = Image.fromarray(mask3)
draw = ImageDraw.Draw(img_pil)
draw.text((100, 0),  "樂", font = font, fill = (b, g, r, a))
mask3 = np.array(img_pil)

bar = cv2.imread("Bar.png")


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
        img1 = frame.copy()
        img2 = frame.copy()
        img3 = frame.copy()
        img1[:,:,0] = 0
        img2[:,:,1] = 0
        img3[:,:,2] = 0
    if group == 3:
        img1 = cv2.flip(frame, 1)
        img2 = cv2.flip(frame, 0)
        img3 = cv2.flip(frame, -1)
    if group == 4:
        img1 = cv2.bitwise_and(frame, mask1)
        img2 = cv2.bitwise_and(frame, mask2)
        img3 = cv2.bitwise_and(frame, mask3)
        frame = cv2.bitwise_and(frame, mask0)
    if group == 5:
        img1 = cv2.GaussianBlur(frame,(15,15),0)
        img2 = cv2.GaussianBlur(frame,(15,25),0)
        img3 = cv2.GaussianBlur(frame,(35,35),0)
    if group == 6:
        img1 = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        img2 = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
        img3 = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)
    if group == 7:
        (b,g,r) = cv2.split(frame)
        tempb = cv2.equalizeHist(b)
        tempg = cv2.equalizeHist(g)
        tempr = cv2.equalizeHist(r)
        img1 = np.dstack((tempb, tempg, tempr))
        temp = cv2.Canny(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY),100,200)
        img2 = np.dstack((temp, temp, temp))
        img3 = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)
    
        
        
        
        
    h1 = np.hstack((frame,img1))
    h2 = np.hstack((img2,img3))
    quard = np.vstack((h1,h2))
    quard = np.vstack((quard,bar))
    
    if group == 0 or group == 4 or group == 5:
        Text1 = " "
        Text2 = " "
        Text3 = " "
        Text4 = " "
    if group == 1:
        Text1 = "Gray Scale"
        Text2 = "Blue"
        Text3 = "Green"
        Text4 = "Red"
    if group == 2:
        Text1 = " "
        Text2 = "No Blue"
        Text3 = "No Green"
        Text4 = "No Red"
    if group == 3:
        Text1 = " "
        Text2 = "Horizontally"
        Text3 = "Vertically"
        Text4 = "H+V"
    if group == 6:
        Text1 = " "
        Text2 = "HSV"
        Text3 = "Lab"
        Text4 = "YCrCb"
    if group == 7:
        Text1 = " "
        Text2 = "Histogram"
        Text3 = "Canny"
        Text4 = "YCrCb"
    text_size = 2
    text_Hoffset = 70
    text_Voffset = 15
    cv2.putText(quard, Text1, (text_Voffset, text_Hoffset), cv2.FONT_HERSHEY_DUPLEX,text_size, (0, 0, 0), 3, cv2.LINE_AA)
    cv2.putText(quard, Text2, (640+text_Voffset, text_Hoffset), cv2.FONT_HERSHEY_DUPLEX,text_size, (0, 0, 0), 3, cv2.LINE_AA)
    cv2.putText(quard, Text3, (text_Voffset, 480+text_Hoffset), cv2.FONT_HERSHEY_DUPLEX,text_size, (0, 0, 0), 3, cv2.LINE_AA)
    cv2.putText(quard, Text4, (640+text_Voffset, 480+text_Hoffset), cv2.FONT_HERSHEY_DUPLEX,text_size, (0, 0, 0), 3, cv2.LINE_AA)
    cv2.putText(quard, Text1, (text_Voffset, text_Hoffset), cv2.FONT_HERSHEY_DUPLEX,text_size, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(quard, Text2, (640+text_Voffset, text_Hoffset), cv2.FONT_HERSHEY_DUPLEX,text_size, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(quard, Text3, (text_Voffset, 480+text_Hoffset), cv2.FONT_HERSHEY_DUPLEX,text_size, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(quard, Text4, (640+text_Voffset, 480+text_Hoffset), cv2.FONT_HERSHEY_DUPLEX,text_size, (255, 255, 255), 2, cv2.LINE_AA)
    
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
        if group >= 7:
            group = 7
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
        cv.imwrite('Saved Image/1'+current_time+'.jpg',frame)
        cv.imwrite('Saved Image/2'+current_time+'quard.jpg',quard)
        #print(current_time)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
