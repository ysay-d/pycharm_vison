import cv2 as cv

import numpy as np
#轮廓近似
im = cv.imread('01/contours2.png')
im_gray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
ret, im_2 = cv.threshold(im_gray, 127, 255, cv.THRESH_BINARY)
contours, binary = cv.findContours(im_2, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
im_show = im.copy()

# c =0.15*cv.arcLength(contours[0],True)
# contours1 = cv.approxPolyDP(contours[0],c,True)

x, y, w, h = cv.boundingRect(contours[0])
print(x, y, w, h)
contours1 = cv.rectangle(im_show, (x, y), (x + w,y + h), (0, 255, 0), 2)


cv.imshow("im", im_show)
cv.waitKey(0)
cv.destroyAllWindows()
