import cv2 as cv
import numpy as np

##遍历输出所有形状的外轮廓
ini_im = cv.imread("01/contours.png")
ini_gray = cv.cvtColor(ini_im, cv.COLOR_BGR2GRAY)
ret, ini_im_2 = cv.threshold(ini_gray, 127, 255, cv.THRESH_BINARY)
contours, n = cv.findContours(ini_im_2, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
# cv.imshow("ini_i",ini_im_2)

for i in contours:
    ini_show = ini_im.copy()
    dst = cv.drawContours(ini_show, contours, contours.index(i), (0, 0, 255), 2)
    cv.imshow("ini_im2", dst)
    cv.waitKey(0)
    cv.destroyAllWindows()
