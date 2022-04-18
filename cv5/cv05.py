import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt
import os
import cv2

# a b c
# ke všemu (výsledky i původní obrázek) amplituda spektrum
def plot_histograms(sortedData, files):
    _, axs = plt.subplots(9, 9)
    for i in range(len(sortedData)):
        for j in range(len(sortedData)): 
            image = cv2.cvtColor(cv2.imread(files[sortedData[i][j]]), cv2.COLOR_BGR2RGB)
            axs[i][j].imshow(image)

def amplitudeSpectrum(data, files):
    fig1, axs = plt.subplots(len(data), 3)

    for file in files:
        i = 0

        img = cv2.imread(file, 0)
        signalFFT = np.fft.ifft2(img)
        fshift = np.fft.fftshift(signalFFT)
        magnitude_spectrum = 20*np.log(np.abs(fshift))  
        img = cv2.imread(file)

        while i != len(data):
            axs[i, 0].set_title('Před')
            axs[i, 0].imshow(img)

            axs[i, 1].set_title('Po')
            axs[i, 1].imshow(data[i])

            axs[i, 2].set_title('Spectrum')
            axs[i, 2].imshow(magnitude_spectrum)

            i = i+1         

    #plt.imshow(magnitude_spectrum)
    return 0

def medianFilter(files):
    medians = list()

    for file in files:
        img = cv2.imread(file)
        median = cv2.medianBlur(img, 5)
        medians.append(median)
        
    return medians

def meanFilter(files):
    means = list()

    for file in files:
        img = cv2.imread(file)
        image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # convert to HSV
        figure_size = 5 # the dimension of the x and y axis of the kernel.
        newImage = cv2.blur(image,(figure_size, figure_size))
        newImage = cv2.cvtColor(newImage, cv2.COLOR_HSV2BGR) # convert to HSV

        means.append(newImage)
        
    return means

def rotatingMask(files):
    means = list()

    for file in files:
        img = cv2.imread(file)
        image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # convert to HSV
        figure_size = 5 # the dimension of the x and y axis of the kernel.
        newImage = cv2.blur(image,(figure_size, figure_size))
        newImage = cv2.cvtColor(newImage, cv2.COLOR_HSV2BGR) # convert to HSV

        means.append(newImage)
        
    return means

    
def loadFiles(folder):
    files = list()
    for file in os.listdir(folder):
        file = os.path.join(folder, file)
        files.append(file)

    return files

if __name__ == '__main__':
    data = list()

    files = loadFiles("images")

    medians = medianFilter(files)
    means = meanFilter(files)
    masks = rotatingMask(files)
    data.extend(medians)
    data.extend(means)
    data.extend(masks)
    print(len(data))

    amplitudeSpectrum(data, files)


    plt.show()
    
    