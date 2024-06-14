import numpy as np
import cv2 as cv
import matplotlib

img = cv.imread("test_image3.jpg",cv.IMREAD_COLOR)
img_gray = cv.imread("test_image3.jpg",cv.IMREAD_GRAYSCALE)

th2 = cv.adaptiveThreshold(img_gray,255,cv.ADAPTIVE_THRESH_MEAN_C,\
 cv.THRESH_BINARY,7,15)

ret, th1 = cv.threshold(img_gray, 200, 255, 0)


contours, hierarchy = cv.findContours(th1, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

c = max(contours, key = cv.contourArea)
x,y,w,h = cv.boundingRect(c)
cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv.drawContours(img, contours, -1, (0,122,122), 1)
#cv.imshow("ATH",th2)
cv.imshow("fin",img)
cv.imshow("bin",th2)
cv.waitKey(0)

cv.destroyAllWindows()