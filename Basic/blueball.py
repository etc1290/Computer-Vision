# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 11:43:35 2020

@author: ST16
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

imgcv = cv2.imread('../img/blueball.jpg')


hsv = cv2.cvtColor(imgcv, cv2.COLOR_BGR2HSV) 
# define range of blue color in HSV 
lower_blue = np.array([110,50,50]) 
upper_blue = np.array([130,255,255]) 
# Threshold the HSV image to get only blue colors 
mask = cv2.inRange(hsv, lower_blue, upper_blue) 
# Bitwise-AND mask and original image 
res = cv2.bitwise_and(imgcv,imgcv, mask= mask)


cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
cv2.resizeWindow("frame", 400, 400)
cv2.imshow('frame',imgcv)

cv2.namedWindow('mask', cv2.WINDOW_NORMAL)
cv2.resizeWindow("mask", 400, 400) 
cv2.imshow('mask',mask) 

cv2.namedWindow('res', cv2.WINDOW_NORMAL)
cv2.resizeWindow("res", 400, 400)
cv2.imshow('res',res) 

cv2.waitKey(0)
cv2.destroyAllWindows()