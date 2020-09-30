# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 09:20:37 2020

@author: Sean
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#Import image
imgcv = cv2.imread('../img/Snivy.jpg')
imgmp = mpimg.imread('../img/Snivy.jpg')

#Split layers
(imgB,imgG,imgR) = cv2.split(imgcv)


#Image processing
kernel = np.ones((4,4),np.uint8)

th2 = cv2.adaptiveThreshold(imgG,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(imgG,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

opening = cv2.morphologyEx(th3, cv2.MORPH_OPEN, kernel)

edges = cv2.Canny(opening,100,200)

dilation = cv2.dilate(edges,kernel,iterations = 1)

erosion = cv2.erode(dilation,kernel,iterations = 1)




#Plot image
plt.figure(0)
plt.subplot(231),plt.imshow(imgmp,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(232),plt.imshow(th2,cmap = 'gray')
plt.title('Th1'), plt.xticks([]), plt.yticks([])
plt.subplot(233),plt.imshow(th3,cmap = 'gray')
plt.title('th2'), plt.xticks([]), plt.yticks([])
plt.subplot(234),plt.imshow(opening,cmap = 'gray')
plt.title('opening'), plt.xticks([]), plt.yticks([])
plt.subplot(235),plt.imshow(dilation,cmap = 'gray')
plt.title('dilation'), plt.xticks([]), plt.yticks([])
plt.subplot(236),plt.imshow(erosion,cmap = 'gray')
plt.title('erosion'), plt.xticks([]), plt.yticks([])


plt.figure(1)
plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])




#Show image
'''
cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow("Image", 400, 400)
cv2.imshow('Image',imgcv)


cv2.namedWindow('th2', cv2.WINDOW_NORMAL)
cv2.resizeWindow("th2", 400, 400)
cv2.imshow('th2',th2)

cv2.namedWindow('opening', cv2.WINDOW_NORMAL)
cv2.resizeWindow("opening", 400, 400)
cv2.imshow('opening',opening)

cv2.namedWindow('dilation', cv2.WINDOW_NORMAL)
cv2.resizeWindow("dilation", 400, 400)
cv2.imshow('dilation',dilation)

cv2.namedWindow('erosion', cv2.WINDOW_NORMAL)
cv2.resizeWindow("erosion", 400, 400)
cv2.imshow('erosion',erosion)


#按下 "0" 關閉所有視窗
cv2.waitKey(0)
cv2.destroyAllWindows()
'''