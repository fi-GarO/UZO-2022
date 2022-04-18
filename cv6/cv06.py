import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt
import cv2
from PIL import Image, ImageOps

def plot(filtr, spectrumFiltr, imgSpectrum, file, name):
    _, axs = plt.subplots(2, 2)

    img = cv2.imread(file)

    axs[0, 0].set_title('Original')
    axs[0, 0].imshow(img)

    axs[0, 1].set_title('Spectrum: Original')
    axs[0, 1].imshow(imgSpectrum)

    axs[1, 0].set_title(name)
    axs[1, 0].imshow(filtr)   

    axs[1, 1].set_title("Spectrum: " + name)
    axs[1, 1].imshow(spectrumFiltr)   

def spectrum(data, file, name):
    
    img = cv2.imread(file, 0)

    signalFFT = np.fft.fft2(img)
    fshift = np.fft.fftshift(signalFFT)
    spectrumImg = 20*np.log(np.abs(fshift))  

    img2 = Image.fromarray(data)
    img2 = ImageOps.grayscale(img2)

    signalFFT = np.fft.fft2(img2)
    fshift = np.fft.fftshift(signalFFT)
    spectrumFiltr = 20*np.log(np.abs(fshift)) 

    plot(data, spectrumFiltr, spectrumImg, file, name)
    return 0

def laplace(file):
    src = cv2.imread(file)
    src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    src = cv2.GaussianBlur(src_gray, (3, 3), 0)
    laplace = cv2.Laplacian(src_gray, cv2.CV_64F)
    return laplace
        
def sobel(file):
    img = cv2.imread(file)

    edge_x = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
    edge_y = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)    

    abs_grad_x = cv2.convertScaleAbs(edge_x)
    abs_grad_y = cv2.convertScaleAbs(edge_y)
    sobel = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
    print(type(sobel))
    return sobel
            

def kirsch(file):
    img = cv2.imread(file)
    fg_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(fg_rgb, cv2.COLOR_RGB2GRAY)  
    kernelG1 = np.array([[ 5,  5,  5],
                         [-3,  0, -3],
                         [-3, -3, -3]], dtype=np.float32)
    kernelG2 = np.array([[ 5,  5, -3],
                         [ 5,  0, -3],
                         [-3, -3, -3]], dtype=np.float32)
    kernelG3 = np.array([[ 5, -3, -3],
                         [ 5,  0, -3],
                         [ 5, -3, -3]], dtype=np.float32)
    kernelG4 = np.array([[-3, -3, -3],
                         [ 5,  0, -3],
                         [ 5,  5, -3]], dtype=np.float32)
    kernelG5 = np.array([[-3, -3, -3],
                         [-3,  0, -3],
                         [ 5,  5,  5]], dtype=np.float32)
    kernelG6 = np.array([[-3, -3, -3],
                         [-3,  0,  5],
                         [-3,  5,  5]], dtype=np.float32)
    kernelG7 = np.array([[-3, -3,  5],
                         [-3,  0,  5],
                         [-3, -3,  5]], dtype=np.float32)
    kernelG8 = np.array([[-3,  5,  5],
                         [-3,  0,  5],
                         [-3, -3, -3]], dtype=np.float32)

    g1 = cv2.normalize(cv2.filter2D(gray, cv2.CV_32F, kernelG1), None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)
    g2 = cv2.normalize(cv2.filter2D(gray, cv2.CV_32F, kernelG2), None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)
    g3 = cv2.normalize(cv2.filter2D(gray, cv2.CV_32F, kernelG3), None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)
    g4 = cv2.normalize(cv2.filter2D(gray, cv2.CV_32F, kernelG4), None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)
    g5 = cv2.normalize(cv2.filter2D(gray, cv2.CV_32F, kernelG5), None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)
    g6 = cv2.normalize(cv2.filter2D(gray, cv2.CV_32F, kernelG6), None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)
    g7 = cv2.normalize(cv2.filter2D(gray, cv2.CV_32F, kernelG7), None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)
    g8 = cv2.normalize(cv2.filter2D(gray, cv2.CV_32F, kernelG8), None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)
    magn = cv2.max(
        g1, cv2.max(
            g2, cv2.max(
                g3, cv2.max(
                    g4, cv2.max(
                        g5, cv2.max(
                            g6, cv2.max(
                                g7, g8
                            )
                        )
                    )
                )
            )
        )
    )
    return magn

if __name__ == '__main__':
    file = "/home/garo/Desktop/UZO-2022/cv6/images/cv06_robotC.bmp"

    name = "Laplace"
    l = laplace(file)
    spectrum(l, file, name)

    name = "Sobel"
    s = sobel(file)
    spectrum(s, file, name)


    name = "Kirsch"
    k = kirsch(file) 
    spectrum(k, file, name)
    
    plt.show()
    
    