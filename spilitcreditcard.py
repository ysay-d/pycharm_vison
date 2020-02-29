import cv2 as cv
import numpy as np

##截取模板中的每一个数字保存到当前目录下
ini_im = cv.imread("03/images/ocr_a_reference.png")
ini_gray = cv.cvtColor(ini_im, cv.COLOR_BGR2GRAY)
ret, ini_im_2 = cv.threshold(ini_gray, 127, 255, cv.THRESH_BINARY_INV)
contours, n = cv.findContours(ini_im_2, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
# cv.imshow("ini_i", ini_im_2)

# xmin = ini_im_2.shape[1] - 1
# ymin = ini_im_2.shape[0] - 1
# xmax = 0
# ymax = 0
for i in range(len(contours)):
    number = 9-i
    ini_show = ini_im.copy()
    x, y, w, h = cv.boundingRect(contours[i])
    # dst = cv.drawContours(ini_show, contours, i, (0, 0, 255), 2)
    contours1 = cv.rectangle(ini_show, (x, y), (x + w, y + h), (0, 255, 0), 2)
    outputim = ini_im_2[y:y + h, x:x + w]
    cv.imwrite(str(number)+".jpg", outputim)
#
    # cv.imshow(str(number)+".jpg", contours1)
    # cv.waitKey(1000)
    # cv.destroyAllWindows()
