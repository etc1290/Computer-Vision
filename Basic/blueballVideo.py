# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 09:15:07 2020

@author: ST16
"""
import cv2
import cv2 as cv
import numpy as np
#import matplotlib.pyplot as plt
#import matplotlib.image as mpimg

cap = cv2.VideoCapture(0)
kernel = np.ones((7,7),np.uint8)

while(1):
    # Take each frame
    _, frame = cap.read()
    
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    (b,g,r) = cv2.split(frame)
    g = cv.bilateralFilter(g,9,75,75)
    g = cv.erode(g,kernel,iterations = 1)
    g = cv.erode(g,kernel,iterations = 1)
    
    
    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    gau_th = cv2.adaptiveThreshold(g,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)
    gau_th_inv = cv2.bitwise_not(gau_th,gau_th)
    opening = cv2.morphologyEx(gau_th_inv, cv.MORPH_OPEN, kernel)
    
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)
    cv2.imshow('blue',b)
    cv2.imshow('green',gau_th_inv)
    cv2.imshow('red',r)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
