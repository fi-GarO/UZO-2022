import cv2
import numpy as np
def riceGrains(img):
    output_adapthresh = cv2.adaptiveThreshold (img, 255.0, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 51, -20.0)
    kernel = np.ones((5,5),np.uint8)
    output_erosion = cv2.erode(output_adapthresh, kernel)

    contours, _ = cv2.findContours(output_erosion, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    output_contour = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    cv2.drawContours(output_contour, contours, -1, (0, 0, 255), 2)
    print("Number of detected contours", len(contours))
    return output_contour

def opening(img, kernel):
    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    return opening

def closing(img, kernel):
    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    return closing

if __name__ == '__main__':
    K = np.array([[0, 1, 0], [1,1,1]], np.uint8)
    img = cv2.imread("/home/garo/Desktop/UZO-2022/cv9/cv09_rice.bmp", 0)
    img1 = cv2.imread("/home/garo/Desktop/UZO-2022/cv9/cv09_bunkyB.bmp")
    img2 = cv2.imread("/home/garo/Desktop/UZO-2022/cv9/cv09_bunkyC.bmp")
    openImg = opening(img1, K)
    closeImg = closing(img2, K)
    rice = riceGrains(img)


    while True:
        cv2.imshow("Original", img)
        cv2.imshow("Rice", rice)


        cv2.imshow("Original-Open", img1)
        cv2.imshow("AfterNoise-Open", openImg)


        cv2.imshow("Original-Close", img2)
        cv2.imshow("AfterNoise-Close", closeImg)



        key = cv2.waitKey(0)
        if key == 27:
            break