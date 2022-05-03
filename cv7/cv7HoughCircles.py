import numpy as np
import cv2 as cv

def minceCounter(img):
    sumOfFives = 0
    sumOfOnes = 0
    img = cv.medianBlur(img, 5)
    cimg = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
    circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT, 1, 20, param1=20, param2=40, minRadius=20, maxRadius=40)
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
            cv.circle(cimg,(i[0], i[1]), i[2], (0,255,0), 2)
            cv.circle(cimg,(i[0], i[1]),2,(0, 0, 255), 3)
            if (i[2] < 35):
                print("Na souřadnici těžiště [", i[0], ";", i[1], "] se nachází: 1")
                sumOfOnes += 1
            else:
                print("Na souřadnici těžiště [", i[0], ";", i[1], "] se nachází: 5")
                sumOfFives += 1   
    celkovaHodnota = sumOfFives*5 + sumOfOnes
    print("Celkova hodnota mincí: ", celkovaHodnota)
    return cimg

if __name__ == "__main__":
    img = cv.imread("cv07_segmentace.bmp", 0)
    mince = minceCounter(img)

    while True:
        cv.imshow("Original", img)
        cv.imshow("Mince", mince)

        key = cv.waitKey(0)
        if key == 27:
            break