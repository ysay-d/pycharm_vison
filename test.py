import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

lena = cv.imread("02/lena.jpg", 0)
lena_plate = cv.imread("02/face.jpg", 0)
# cv.imshow('lena', lena)
# cv.imshow('face', lena_plate)



res = cv.matchTemplate(lena, lena_plate, cv.TM_CCORR)

min_val = res.min()
print(min_val)
res = res - min_val
max_val = res.max()

for row in range(res.shape[0]):
    for col in range(res.shape[1]):
        res[row, col] = (res[row, col] / max_val)


plt.hist(res.ravel(),256)
plt.show()
cv.imshow("dst",res)
cv.waitKey(0)
cv.destroyAllWindows()






