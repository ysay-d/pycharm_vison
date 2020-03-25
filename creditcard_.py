import cv2 as cv
import numpy as np
import pytesseract


# findcontours()函数对于二值图像,会寻找像素值为1的也就是白色区域的边界,
# 因此当采用普通二值图像转换时,(原图为白底黑字),原图最外边是也是外轮廓.应注意将兴趣区域转为像素值为1的区域.
def MarkNumbers():  # 将数字抽取出来存储在字典中
    numbers = cv.imread('03/images/ocr_a_reference.png')
    numbers_gray = cv.cvtColor(numbers, cv.COLOR_BGR2GRAY)
    ret, numbers_binary = cv.threshold(numbers_gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    contours, n = cv.findContours(numbers_binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    for i in range(len(contours)):
        x, y, w, h = cv.boundingRect(contours[i])
        cv.rectangle(numbers_binary, (x, y), (x + w, y + h), (0, 0, 255))
        number_temp[9 - i] = numbers_binary[y:y + h, x:x + w]


def GetNmubersInCard(cardimage):
    cards = []
    card_im = cv.imread('03/images/' + cardimage)
    card_im = cv.GaussianBlur(card_im,(3,3),0)
    card_im = cv.resize(card_im, (583, 368))
    card_gray = cv.cvtColor(card_im, cv.COLOR_BGR2GRAY)

    ret, card_binary = cv.threshold(card_gray, 127, 255, cv.THRESH_BINARY)
    # cv.imshow("bianry",card_binary)
    rectKernel = cv.getStructuringElement(cv.MORPH_RECT, (9, 3))
    sqKernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    tophat = cv.morphologyEx(card_binary, cv.MORPH_DILATE, sqKernel)
    tophat = cv.morphologyEx(tophat1, cv.MORPH_DILATE, rectKernel)
    cv.imshow('tophat',tophat)
    print("信用卡数字为:")
    contours, n = cv.findContours(tophat, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    for i in range(len(contours)):
        x, y, w, h = cv.boundingRect(contours[i])
        if 99 < w < 115 and 25 < h < 50:
            # cv.rectangle(card_im, (x, y), (x + w, y + h), (0, 0, 255))
            cards.append((x,y,w,h))
    # cv.imshow('cardim',card_im)
    cards = sorted(cards,key=lambda x:x[0])
    print
    for i in cards:
        cards[cards.index(i)] = card_binary[i[1]:i[1]+i[3],i[0]:i[0]+i[2]]
    for i in range(len(cards)):
        # gray = cv.cvtColor(cards[i], cv.COLOR_BGR2GRAY)
        # b, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
        binary = cards[i]
        cardcontours, hie = cv.findContours(binary, cv.RETR_EXTERNAL, cv.RETR_TREE)
        # cv.drawContours(cards[i],cardcontours,-1,(0,0,255),2)
        for n in range(len(cardcontours)):
            #
            x, y, w, h = cv.boundingRect(cardcontours[len(cardcontours) - 1 - n])
            # cv.rectangle(cards[i],(x,y),(x+w,y+h),(0,0,255),2)
            maxvalue = []
            for tempnum in range(10):
                num_im = cv.resize(number_temp[tempnum], (w, h))
                loc = cv.matchTemplate(binary[y:y + h, x:x + w], num_im, cv.TM_CCORR_NORMED)
                main, mmax, minloc, maxloc = cv.minMaxLoc(loc)
                maxvalue.append(mmax)
            # cv.imshow("cards",cards[i])
            # cv.waitKey(0)
            print(maxvalue.index(max(maxvalue)), end="")
        print(" ", end="")


if __name__ == '__main__':
    number_temp = dict()
    MarkNumbers()
    GetNmubersInCard('credit_card_05.png')
    cv.waitKey(0)
    cv.destroyAllWindows()
