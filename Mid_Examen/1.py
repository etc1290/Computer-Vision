# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 10:15:16 2020

@author: ST16
"""

import cv2 as cv
import numpy as np

img = cv.imread("iphone12.jpg")
kernel = np.ones((5,5),np.uint8)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV) 
(B,G,R) = cv.split(img)
img_copy = img.copy()

dimensions = img.shape

#用顏色轉換得到的紅色HSV數值
lower_red = np.array([170,50,50]) 
upper_red = np.array([180,255,255]) 
mask = cv.inRange(hsv, lower_red, upper_red) 
erosion = cv.erode(mask,np.ones((10,10),np.uint8),iterations = 1)
dilation = cv.dilate(erosion,kernel,iterations = 1)
closing = cv.morphologyEx(dilation, cv.MORPH_CLOSE, kernel)

contours, hierarchy = cv.findContours(closing, 1, 2)
cnt = contours[4]
x,y,w,h = cv.boundingRect(cnt)
cv.rectangle(closing,(x,y),(x+w,y+h),(0,255,0),2)

#cv.drawContours(img, contours, -1, (0,255,0), 3)
x,y,w,h = cv.boundingRect(cnt)
midw = int(w/2)
midh = int(h/2)
midx = x+midw
midy = y+midh
cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv.line(img, (x,y),(x+w,y+h), (255, 0, 0), 2)
cv.line(img, (x+w,y),(x,y+h), (255, 0, 0), 2)
cv.circle(img,(midx, midy), 5, (255,255, 255), -1)
text = "X:"+ str(midx) + "   Y:" + str(midy)
cv.putText(img, text, (10, 450), cv.FONT_HERSHEY_DUPLEX,1, (0, 255, 255), 1, cv.LINE_AA)

img_copy = img_copy[y:y+h,x:x+w]
img_copy = cv.cvtColor(img_copy, cv.COLOR_BGR2GRAY) 
ret,thresh = cv.threshold(img_copy,30,255,cv.THRESH_BINARY_INV)
closing = cv.morphologyEx(thresh, cv.MORPH_CLOSE, kernel)
erosion = cv.erode(closing,np.ones((10,10),np.uint8),iterations = 1)
erosion = cv.erode(erosion,np.ones((5,5),np.uint8),iterations = 1)

(cnts, _) = cv.findContours(erosion.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
clone = img.copy()
i = 0
for c in cnts:
    area = cv.contourArea(c)
    perimeter = cv.arcLength(c, True)
    cv.drawContours(clone, c, -1, (0, 255, 0), 2)
    M = cv.moments(c)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    cv.circle(clone, (cX+x, cY+y), 10, (1, 227, 254), -1)
    print("Contour #%d — area: %.2f, perimeter: %.2f" % (i , area, perimeter))
    cv.putText(clone, "#%d" % (i), (cX - 20+x, cY+y), cv.FONT_HERSHEY_SIMPLEX, 1.1, (252, 197, 5), 3)
    i += 1;
    
if i == 2:
    cv.putText(clone, "Iphone 12",(cX + 20 +x, cY+80+y), cv.FONT_HERSHEY_SIMPLEX, 1.1, (252, 197, 5), 3)
if i == 3:
        cv.putText(clone, "Iphone 12 Pro",(cX + 20 + x, cY+80 + y), cv.FONT_HERSHEY_SIMPLEX, 1.1, (252, 197, 5), 3)


res = cv.bitwise_and(img, img, mask=mask)

cv.imshow("Iphone", img)
cv.imshow("Iphone HSV", hsv)
cv.imshow("Iphone red", mask)
cv.waitKey()
cv.destroyAllWindows()
cv.imshow("Iphone crop gray", img_copy)
cv.imshow("Iphone crop bin", thresh)
cv.imshow("Iphone count", clone)
cv.waitKey()
cv.destroyAllWindows()
