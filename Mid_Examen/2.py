import cv2 as cv
import numpy as np

kernel = np.ones((5,5),np.uint8)

img = cv.imread("apple.jpg")


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
(H,S,V) = cv.split(hsv)

Blur = cv.GaussianBlur(H,(15,15),0)
ret,H1 = cv.threshold(H.copy(),155,255,cv.THRESH_BINARY)
ret,H2 = cv.threshold(H.copy(),5,255,cv.THRESH_BINARY_INV)
ret,V = cv.threshold(V,127,255,cv.THRESH_BINARY)
H = cv.bitwise_or(H1,H2)
res = cv.bitwise_and(H,V)
closing = cv.morphologyEx(res, cv.MORPH_CLOSE, kernel)
opening = cv.morphologyEx(closing, cv.MORPH_OPEN, kernel)
Canny = cv.Canny(opening, 100, 160)


(cnts, _) = cv.findContours(Canny.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
clone = img.copy()

i = 1
for c in cnts:
    area = cv.contourArea(c)
    if area > 10000:
        cv.drawContours(clone, c, -1, (0, 255, 0), 2)
        M = cv.moments(c)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        cv.circle(clone, (cX, cY), 10, (1, 227, 254), -1)
        perimeter = cv.arcLength(c, True)    #計算周長
        print("Contour #%d — area: %.2f, perimeter: %.2f" % (i , area, perimeter))
        cv.putText(clone, "#%d" % (i), (cX - 20, cY), cv.FONT_HERSHEY_SIMPLEX, 1.1, (252, 197, 5), 3)
        i += 1;

#cv.imshow("Apple", img)
cv.imshow("Apple V", V)
cv.imshow("Apple H", H)
cv.imshow("Apple AND", Canny)
cv.imshow("Apple Contours", clone)
cv.waitKey()
cv.destroyAllWindows()
