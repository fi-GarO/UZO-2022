import cv2
import numpy as np
import imutils
import math

def shearImg(img):
    rows, cols, _ = img.shape
    M = np.float32([[1, 0.6, 0],
             	    [0, 1, 0],
            	    [0, 0, 1]])
    shearedImg = cv2.warpPerspective(img,M,(int(cols*1.6),int(rows)))
    return shearedImg

def resizeImg(value, img):
    print('Original Dimensions : ', img.shape)
    #width = int(img.shape[1] * value / 100)
    #height = int(img.shape[0] * value / 100)

    ratio = float(img.shape[1]) / float(img.shape[0])
    height = int(math.sqrt(value / ratio) + 0.5)
    width = int((height * ratio) + 0.5)
    dim = (width, height)
    resize = cv2.resize(img, dim)
    print('Resized Dimensions : ', resize.shape)
    return resize

if __name__ == "__main__":
    img = cv2.imread('/home/garo/Desktop/UZO-2022/cv3/cv03_robot.bmp')
    resize = resizeImg(300000, img)
    shear = shearImg(img)

    while True:
        cv2.imshow("Image", img)
        cv2.imshow("Resize", resize)
        cv2.imshow("Shear", shear)
        key = cv2.waitKey(0)
        if key == 27:
            break