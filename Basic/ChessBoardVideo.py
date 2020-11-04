# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 16:07:53 2020

@author: Sean
"""

import numpy as np
import cv2 as cv
#import glob
# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((6*7,3), np.float32)
objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.


i = 0
x = 0
cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 1024)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 768)
kernel = np.ones((7,7),np.uint8)

while(1):
    _, frame = cap.read()
    img = frame
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    
    # Find the chess board corners
    ret, corners = cv.findChessboardCorners(gray, (7,6), None)
   
    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)
        corners2 = cv.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
        imgpoints.append(corners)
        # Draw and display the corners
        cv.drawChessboardCorners(img, (7,6), corners2, ret)
        cv.imshow('img', img)
        oimg = './1103_1900/' +'ori' + str(i) + '.jpg'
        corn = './1103_1900/' +'corn' + str(i) + '.jpg'
        cv.imwrite(oimg, gray)
        cv.imwrite(corn, img)
        x += 1
    
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
cv.destroyAllWindows()