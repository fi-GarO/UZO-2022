import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt
import os
import cv2

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
        signalFFT = np.fft.fft2(img)
        fshift = np.fft.fftshift(signalFFT)
        magnitude_spectrum = 20*np.log(np.abs(fshift))  
        img = cv2.imread(file)

        while i != len(data):
            axs[i, 0].set_title('Median - před')
            axs[i, 0].imshow(img)

            axs[i, 1].set_title('Median - po')
            axs[i, 1].imshow(data[i])

            axs[i, 2].set_title('Median - spectrum')
            axs[i, 2].imshow(magnitude_spectrum)

            i = i+1 

    plt.figure()
        

    #plt.imshow(magnitude_spectrum)
    return 0

def laplace(files):

    
    for file in files:
      print(file)
      src = cv2.imread(file)
      src = cv2.GaussianBlur(src, (3, 3), 0)
      src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
      dst = cv2.Laplacian(src_gray, cv2.CV_16S, ksize=3)
      abs_dst = cv2.convertScaleAbs(dst)
      cv2.imshow("laplace", abs_dst)
        
def sobel(files):
    filter = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

    for file in files:
      print(file)
      src = cv2.imread(file)
      src = cv2.GaussianBlur(src, (3, 3), 0)
      conv = np.convolve(src, filter)
      gradient_magnitude = np.sqrt(np.square(conv) + np.square(conv))
 
      gradient_magnitude *= 255.0 / gradient_magnitude.max()
      cv2.imshow("sobel", gradient_magnitude)
    
        

def kirsch(files):
    filter = np.array([[5, 5, 5], [-3, 0, -3], [-3, -3, -3]])
    for file in files:
        src = cv2.imread(file)

    
def loadFiles(folder):
    files = list()
    for file in os.listdir(folder):
        file = os.path.join(folder, file)
        files.append(file)

    return files

if __name__ == '__main__':
    files = loadFiles("images")
    print(files)
    l = laplace(files)
    s = sobel(files)
    k = kirsch(files)  
    cv2.waitKey(0) 


    plt.show()
    
    