


#1 obrazek s poruchou, porucha, image bey poruchz
#2 original, hist original
#  ekvalizace, hist ekvalizace
#3 z každýho obrázku histogram, spočítat vzdálenosti, porovnat a vypsat vzestupně

import numpy as np
import cv2
import matplotlib.pyplot as plt
import os
import math

def sort_histograms(data):
    sum = 0
    dir = os.path.abspath("cv03_v02")
    files = list()
    for file in os.listdir(dir):
        file = os.path.join(dir, file)
        files.append(file)

    print(len(files))
    #for file in files:
        #print(file, data[file])
     #   for i in range (0, 180):
            #print(data[file][i][0])
            #sum = sum + (hist1[i][0]-hist2[i][0])**2
        #dist = math.sqrt(sum)
        #print('euclidean distance:', dist)
    
def load_histograms():
    result = dict()
    dir = os.path.abspath("cv03_v02")
    for file in os.listdir(dir):
        file = os.path.join(dir, file)
        print(file)
        img = cv2.imread(file)
        hue = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        hist = cv2.calcHist([hue], [0], None, [180], [0, 180])
        print(hist)
        result[file] = hist

    return result


def image_correction(file, etalon_file, c, index):
    image = cv2.cvtColor(cv2.imread(file), cv2.COLOR_BGR2RGB)
    etalon = cv2.cvtColor(cv2.imread(etalon_file), cv2.COLOR_BGR2RGB)

    np.seterr(divide='ignore', invalid='ignore')

    corrected_image = np.divide(np.dot(c, image), etalon).astype(np.uint8)

    fig, axs = plt.subplots(1, 3, num=index)
    fig.canvas.set_window_title('Jasová korekce')

    axs[0].imshow(image.astype(np.uint8))
    axs[0].set_title('Před')

    axs[1].imshow(etalon.astype(np.uint8))
    axs[1].set_title('Porucha')

    axs[2].imshow(corrected_image)
    axs[2].set_title('Po')


def image_equalization(file, index):
    image = cv2.cvtColor(cv2.imread(file), cv2.COLOR_BGR2RGB)
    height, width, _ = image.shape

    hist, _ = np.histogram(image[:, :, 0].flatten(), 256, [0, 256])

    q = (255 / (height * width) * np.cumsum(hist)).astype(np.uint8)

    equalized_image = np.empty([height, width])
    for i in range(height):
        for j in range(width):
            equalized_image[i][j] =q[image[i][j][0]]

    fig, axs = plt.subplots(2, 2, num=index)
    fig.canvas.set_window_title('Ekvalizace')
    plt.tight_layout()
    axs[0, 0].set_title('Před')
    axs[0, 0].imshow(image, cmap='gray')

    axs[0, 1].set_title('Před - Histogram')
    axs[0, 1].hist(image.ravel(), 256, [0, 256])

    axs[1, 0].set_title('Po')
    axs[1, 0].imshow(equalized_image, cmap='gray')

    axs[1, 1].set_title('Po - Histogram')
    axs[1, 1].hist(equalized_image.ravel(), 256, [0, 256])



if __name__ == '__main__':
    #image_correction('cv04_f01.bmp', 'cv04_e01.bmp', 255, 1)
    #image_correction('cv04_f02.bmp', 'cv04_e02.bmp', 255, 2)
    #image_equalization('cv04_rentgen.bmp', 3)
    #plt.show()
    histograms = load_histograms()
    sort_histograms(histograms)
