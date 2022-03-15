import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

if __name__ == '__main__':

    img = cv.imread('C:/Users/turyj/UZO-2022/cv01_obr.bmp')
    img2 = cv.imread('C:/Users/turyj/UZO-2022/cv01_obr.bmp', 0)


    color = ('b','g','r')

    # Plot RGB
    for i,col in enumerate(color):
        histr = cv.calcHist([img], [i], None, [256], [0,256])
        plt.plot(histr,color = col)
        plt.xlim([0,256])
    plt.show()

    hist,bins = np.histogram(img2.flatten(),256,[0,256])
    cdf = hist.cumsum()
    cdf_normalized = cdf * (1 / (2*2 + 1))

    # Plot Histogram
    plt.figure(1)
    plt.plot(hist)
    plt.xlim([0,256])
    plt.show()

    # Plot Equalized Histogram
    plt.figure(1)
    plt.plot(cdf_normalized)
    plt.xlim([0,256])
    plt.show()

    
