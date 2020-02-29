import cv2 as cv

import numpy as np

im = cv.imread("01/lena.jpg", cv.IMREAD_GRAYSCALE)
dst1 = cv.Canny(im, 100, 200)
dst2 = cv.Canny(im, 50, 100)
dst = imnp.hstack((dst1, dst2))
cv.imshow("im", dst)
cv.waitKey(0)
cv.destroyAllWindows()
