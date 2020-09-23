# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 17:22:50 2020

@author: Sean
"""

import cv2
import numpy as np


img = cv2.imread('../img/Snivy.jpg')
img2 = cv2.imread('../img/Minccino.jpg')

img  = cv2.resize(img,(400,400))
img2 = cv2.resize(img2,(400,400))

numpy_horizontal = np.hstack((img, img2))
numpy_horizontal_concat = np.concatenate((img,img2),axis=1)

cv2.resizeWindow("enhanced", 400, 800);
cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
cv2.imshow('Image',numpy_horizontal_concat)

#按下 "0" 關閉所有視窗
cv2.waitKey(0)
cv2.destroyAllWindows()