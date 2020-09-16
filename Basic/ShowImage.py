# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 17:22:50 2020

@author: Sean
"""

import cv2
import numpy as np


img = cv2.imread('../img/Snivy.jpg')
cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
cv2.imshow('Image',img)

#按下 "0" 關閉所有視窗
cv2.waitKey(0)
cv2.destroyAllWindows()