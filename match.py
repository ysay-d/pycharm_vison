import cv2 as cv
import numpy as np


lena = cv.imread("02/lena.jpg",0)
lena_plate = cv.imread("02/face.jpg",0)
cv.imshow('lena',lena)
cv.imshow('face',lena_plate)
methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
           'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
height,width = lena_plate.shape[0:2]
for meth in methods:
    methe = eval(meth)
    res = cv.matchTemplate(lena,lena_plate,methe)
    lena_show = lena.copy()
    main,max,minloc,maxloc = cv.minMaxLoc(res)
    if meth in ['cv.TM_SQDIFF_NORMED','cv.TM_SQDIFF']:
        left_top = minloc
    else:
        left_top = maxloc
    print(res)
    cv.rectangle(lena_show,left_top,(left_top[0]+width,left_top[1]+height),255,thickness=2)
    cv.imshow(meth,lena_show)
    cv.waitKey(0)
    cv.destroyAllWindows()
