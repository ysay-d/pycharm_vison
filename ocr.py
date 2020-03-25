import cv2 as cv
import numpy as np

#
def order_points(pts):
    rect = np.zeros((4, 2), dtype="float32")
    s = np.sum(pts, axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]
    d = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(d)]
    rect[3] = pts[np.argmax(d)]

    return rect


def four_point_transform(image, pts):
    rect = order_points(pts)
    tl, tr, br, bl = rect
    width = max(np.sqrt((tr[0] - tl[0]) ** 2 + (tr[1] - tl[1]) ** 2),
                np.sqrt((br[0] - bl[0]) ** 2 + (br[1] - bl[1]) ** 2))
    height = max(np.sqrt((bl[0] - tl[0]) ** 2 + (bl[1] - tl[1]) ** 2),
                 np.sqrt((br[0] - tr[0]) ** 2 + (br[1] - tr[1]) ** 2))
    dst = np.array([
        [0, 0],
        [width - 1, 0],
        [width - 1, height - 1],
        [0, height - 1]], dtype='float32')
    M = cv.getPerspectiveTransform(rect, dst)
    warped = cv.warpPerspective(image, M, (int(width), int(height)))

    return warped


origin = cv.imread('./Scan/images/page.jpg')
origin_gray = cv.cvtColor(origin, cv.COLOR_BGR2GRAY)
origin_guassian = cv.GaussianBlur(origin_gray, (7, 7), 0)
edge = cv.Canny(origin_guassian, 75, 200)
contoues, _ = cv.findContours(edge, cv.RETR_EXTERNAL, cv.RETR_TREE)
cnts = sorted(contoues, key=cv.contourArea, reverse=True)
perci = cv.arcLength(cnts[0], True)
cnt = cv.approxPolyDP(cnts[0], 0.02 * perci, True)
cnt = cnt.reshape(4, 2)
# 透视变换
wrap = four_point_transform(origin,cnt)
wrap_gray = cv.cvtColor(wrap,cv.COLOR_BGR2GRAY)
# cv.drawContours(origin, [cnt], -1, (0,0,255), 2)  #[]括起后将转化为一个列表,drawcontours函数需要传入的contours为列表的每一项,否则会绘制出原数组的每个点

_,dst = cv.threshold(wrap_gray,127,255,cv.THRESH_BINARY)
sqKernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
tophat1 = cv.morphologyEx(dst , cv.MORPH_ERODE, sqKernel)
cv.imwrite('scan1.jpg',tophat1)
cv.namedWindow('origin',0)       #不添加0参数会导致不能调整窗口大小
cv.resizeWindow('origin',500,500)
cv.imshow('origin',dst)
cv.waitKey(0)
cv.destroyAllWindows()
