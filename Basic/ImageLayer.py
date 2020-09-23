# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 17:22:50 2020

@author: Sean
"""

import cv2
import numpy as np

#Import image
img_r = cv2.imread('../img/Snivy.jpg')





#Join image horizontally
#numpy_horizontal = np.hstack((img, img2))
numpy_horizontal_concat = np.concatenate((img_r),axis=1)


#Show image
cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow("enhanced", 400, 400)
cv2.imshow('Image',img_r)

#按下 "0" 關閉所有視窗
cv2.waitKey(0)
cv2.destroyAllWindows()