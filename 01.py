import cv2 as cv
import numpy as np


def imread():
    im = cv.imread("")


# vc = cv.VideoCapture("01/test.mp4")
# if vc.isOpened():
#     open, frame = vc.read()
#     print("success")
# else:
#     print("error")
#
# while (open):
#     ret, frame = vc.read()
#     cv.imshow("vc", frame)
#     c = cv.waitKey(10)
#     if c == 27:
#         break
# 腐蚀操作
# im = cv.imread("01/dige.png", cv.IMREAD_GRAYSCALE)
# # im_cut = im[0:20,0:200]
# kenel = np.ones((3,3), np.uint8)
# dst = cv.erode(im, kenel, iterations=1)
# # ret, dst=cv.threshold(im,127,255,cv.THRESH_BINARY)
# res = np.hstack((im, dst))
#
#
# im = cv.imread("01/dige.png", cv.IMREAD_GRAYSCALE)
# # im_cut = im[0:20,0:200]
# kenel = np.ones((3,3), np.uint8)
# dst1 = cv.erode(im, kenel, iterations=1)
# dst2= cv.dilate(dst1, kenel, iterations=1)
#
# # ret, dst=cv.threshold(im,127,255,cv.THRESH_BINARY)


im = cv.imread("01/lena.jpg", cv.IMREAD_GRAYSCALE)
dstx = cv.Sobel(im, cv.CV_64F, 1, 0, ksize=3)
dstx = cv.convertScaleAbs(dstx)
dsty = cv.Sobel(im, cv.CV_64F, 0, 1, ksize=3)
dsty = cv.convertScaleAbs(dsty)
last = cv.addWeighted(dstx, 0.5, dsty, 0.5, 0)
shuchu = last + im
lap = cv.Laplacian(im,cv.CV_64F,ksize=3)
lap = cv.convertScaleAbs(lap)
cv.imshow("last", last)
cv.imshow("lap", lap)


# cv.imshow("shuchu", shuchu)


cv.waitKey(0)
cv.destroyAllWindows()
