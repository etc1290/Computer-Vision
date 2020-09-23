# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 17:22:50 2020

@author: Sean
"""

import cv2
import numpy as np

#Import image
img = cv2.imread('../img/Snivy.jpg')


#Split layers
(B,G,R) = cv2.split(img)

img_r = img[:,:,0]
img_g = img[:,:,1]
img_b = img[:,:,2]

image_b = np.dstack((img_b, np.zeros(img_b.shape, np.uint8), np.zeros(img_b.shape, np.uint8)))
image_g = np.dstack((np.zeros(img_g.shape, np.uint8),img_g , np.zeros(img_g.shape, np.uint8)))
image_r = np.dstack((np.zeros(img_r.shape, np.uint8), np.zeros(img_r.shape, np.uint8), img_r))


#Join image horizontally
numpy_horizontal_concat = np.concatenate((R,G,B),axis=1)
numpy_horizontal_concat_matrix = np.concatenate((img_r,img_g,img_b),axis=1)
numpy_horizontal_concat_rgb = np.concatenate((image_r,image_g,image_b),axis=1)

#Show image
cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow("Image", 1200, 400)
cv2.imshow('Image',numpy_horizontal_concat)

cv2.namedWindow('Matrix', cv2.WINDOW_NORMAL)
cv2.resizeWindow("Matrix", 1200, 400)
cv2.imshow('Matrix',numpy_horizontal_concat_matrix)

cv2.namedWindow('Blue', cv2.WINDOW_NORMAL)
cv2.resizeWindow("Blue", 1200, 400)
cv2.imshow('Blue',numpy_horizontal_concat_rgb)


#按下 "0" 關閉所有視窗
cv2.waitKey(0)
cv2.destroyAllWindows()