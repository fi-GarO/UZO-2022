import numpy as np
import matplotlib.pyplot as plt
import cv2
from PIL import Image, ImageOps

# # a b c
# # ke všemu (výsledky i původní obrázek) amplituda spektrum
# def plot(filtr, spectrumFiltr, imgSpectrum, file, name):
#     _, axs = plt.subplots(2, 2)

#     img = cv2.imread(file)

#     axs[0, 0].set_title('Original')
#     axs[0, 0].imshow(img)

#     axs[0, 1].set_title('Spectrum: Original')
#     axs[0, 1].imshow(imgSpectrum)

#     axs[1, 0].set_title("Filtr: " + name)
#     axs[1, 0].imshow(filtr)   

#     axs[1, 1].set_title("Spectrum: " + name)
#     axs[1, 1].imshow(spectrumFiltr)   

# def spectrum(data, file, name):
    
#     img = cv2.imread(file, 0)

#     signalFFT = np.fft.ifft2(img)
#     fshift = np.fft.fftshift(signalFFT)
#     spectrumImg = 20*np.log(np.abs(fshift))  

#     img2 = Image.fromarray(data, 'RGB')
#     img2 = ImageOps.grayscale(img2)

#     signalFFT = np.fft.ifft2(img2)
#     fshift = np.fft.fftshift(signalFFT)
#     spectrumFiltr = 20*np.log(np.abs(fshift)) 

#     plot(data, spectrumFiltr, spectrumImg, file, name)

# def medianFilter(file):
#     img = cv2.imread(file)
#     median = cv2.medianBlur(img, 5)

#     return median

# def meanFilter(file):

#     img = cv2.imread(file)
#     image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # convert to HSV
#     figure_size = 5 # the dimension of the x and y axis of the kernel.
#     newImage = cv2.blur(image,(figure_size, figure_size))
#     mean = cv2.cvtColor(newImage, cv2.COLOR_HSV2BGR) # convert to HSV
        
#     return mean

# def neighbors(radius, row_number, column_number, a):
#     # a = [[ 11,  21,  31,  41,  51,  61,  71],
#     #      [ 12,  22,  32,  42,  52,  62,  72],
#     #      [ 13,  23,  33,  43,  53,  63,  73],
#     #      [ 14,  24,  34,  44,  54,  64,  74],
#     #      [ 15,  25,  35,  45,  55,  65,  75],
#     #      [ 16,  26,  36,  46,  56,  66,  76],
#     #      [ 17,  27,  37,  47,  57,  67,  77]]
    
#     q = 0
#     averages = list()
#     variances = list()

    
#     while(q < 3):
#         m = list()
#         k = 0
#         while(k < 3):            
#             for j in range(column_number-1-radius+q, column_number+radius+q):
#                 for i in range(row_number-1-radius+k, row_number+radius+k):
#                     if column_number-1-radius+q < 0:
#                         continue
#                     if row_number-1-radius+k < 0:
#                         continue
#                     if column_number+radius+q > 256:
#                         continue
#                     if column_number+radius+q > 256:
#                         continue
#                     if q == 1 and k == 1:
#                         m.append(0)
#                     elif  i >= 0 and i < len(a) and j >= 0 and j < len(a[0]) and a[i][j] != 0:    
#                         m.append(a[i][j])            
#             if bool(m):
#                 if m[0] != 0:
#                     avg = sum(m)/9
#                     var = np.var(m)
#                     averages.append(avg)
#                     variances.append(var)
#             #m.clear()
#             # print("avg:", avg)
#             # print("var:", var)
#             # print("k:", k)
#             k += 1
#         q += 1
#     return averages, variances

# def rotatingMask(file):
#     img = cv2.imread(file, 0)
#     # newImg = np.zeros((256, 256))

#     # radius = 1
#     # for x in range (img.shape[0]):
#     #     for y in range (img.shape[1]):
#     #         vars, avgs = neighbors(radius, x, y, img)
#     #         minVar = np.min(vars)

#     #         for var in vars:
#     #             if var == minVar:
#     #                 id = vars.index(var)
#     #         newValue = avgs[id]
#     #         newImg[x][y] = newValue

#     temp_img = np.zeros((img.shape[0]+4, img.shape[1]+4))
#     temp_img[2:-2, 2:-2] = img
#     out = np.zeros_like(img)
#     for i in range(2, temp_img.shape[0]-2):
#         for j in range(2, temp_img.shape[1]-2):
#             mask1 = temp_img[i-2:i+1, j-2:j+1]
#             mask2 = temp_img[i-1:i+2, j-2:j+1]
#             mask3 = temp_img[i:i+3, j-2:j+1]
#             mask4 = temp_img[i-2:i+1, j:j+3]
#             mask5 = temp_img[i-1:i+2, j:j+3]
#             mask6 = temp_img[i:i+3, j:j+3]
#             mask7 = temp_img[i-2:i+1, j-1:j+2]
#             mask8 = temp_img[i:i+3, j-1:j+2]
#             masks = [mask1, mask2, mask3, mask4, mask5, mask6, mask7, mask8]

#     vars_arr = []
#     for mask in masks:
#         vars_arr.append(np.var(mask))
#         min_var = np.argmin(vars_arr)
#         out[i-2, j-2] = np.mean(masks[min_var])

#     return out  

# if __name__ == '__main__':
#     file = "/home/garo/Desktop/UZO-2022/cv5/images/cv05_robotS.bmp"

    
#     name = "Median"
#     median = medianFilter(file)
#     #spectrum(median, file, name)

#     name = "Mean"
#     mean = meanFilter(file)
#     print(type(mean))
#     #spectrum(mean, file, name)

#     name = "Mask"
#     mask = rotatingMask(file)
#     spectrum(mask, file, name)
#     #print(neighbors(1, 0, 0))
    


#     plt.show()

import numpy as np
import cv2
from matplotlib import pyplot as plt

def plot_images(img1, img2, title1, title2):
    plt.subplot(2, 2, 1)
    plt.imshow(img1, cmap='gray')
    plt.title(title1)
    plt.subplot(2, 2, 2)
    ft = np.fft.fftshift(np.fft.fft2(img1))
    ft2 = np.log(np.abs(ft))
    plt.imshow(ft2, cmap='jet')
    plt.title('Spectrum')
    plt.colorbar()
    plt.subplot(2, 2, 3)
    plt.imshow(img2, cmap='gray')
    plt.title(title2)
    plt.subplot(2, 2, 4)
    ft = np.fft.fftshift(np.fft.fft2(img2))
    ft2 = np.log(np.abs(ft))
    plt.imshow(ft2, cmap='jet')
    plt.title('Spectrum')
    plt.colorbar()
    plt.show()

def mean_filter(img, mask):
    # mask must have shape 3x3
    temp_img = np.zeros((img.shape[0]+2, img.shape[1]+2))
    temp_img[1:-1, 1:-1] = img

    mask_len = mask.shape[0]
    out = np.zeros_like(img)
    for i in range(1, temp_img.shape[0]-1):
        for j in range(1, temp_img.shape[1]-1):
            temp = np.sum(temp_img[i-1:i+2, j-1:j+2]*mask)
            out[i-1, j-1] = temp/(mask_len**2)
    return out
def rotation_mask_filter(img):
    temp_img = np.zeros((img.shape[0]+4, img.shape[1]+4))
    temp_img[2:-2, 2:-2] = img

    out = np.zeros_like(img)
    for i in range(2, temp_img.shape[0]-2):
        for j in range(2, temp_img.shape[1]-2):
            mask1 = temp_img[i-2:i+1, j-2:j+1]
            mask2 = temp_img[i-1:i+2, j-2:j+1]
            mask3 = temp_img[i:i+3, j-2:j+1]

            mask4 = temp_img[i-2:i+1, j:j+3]
            mask5 = temp_img[i-1:i+2, j:j+3]
            mask6 = temp_img[i:i+3, j:j+3]

            mask7 = temp_img[i-2:i+1, j-1:j+2]
            mask8 = temp_img[i:i+3, j-1:j+2]

            masks = [mask1, mask2, mask3, mask4, mask5, mask6, mask7, mask8]

            vars_arr = []
            for mask in masks:
                vars_arr.append(np.var(mask))

            min_var = np.argmin(vars_arr)

            out[i-2, j-2] = np.mean(masks[min_var])
    return out

def median_filter(img):
    temp_img = np.zeros((img.shape[0]+4, img.shape[1]+4))
    temp_img[2:-2, 2:-2] = img

    out = np.zeros_like(img)
    for i in range(2, temp_img.shape[0]-2):
        for j in range(2, temp_img.shape[1]-2):
            temp = temp_img[i, j-2:j+3]
            temp2 = temp_img[i-2:i+3, j]
            temp = np.append(temp, temp2[0:2])
            temp = np.append(temp, temp2[3:])
            out[i-2, j-2] = np.median(temp)
    return out

def median_filter_2(img):
    temp_img = np.zeros((img.shape[0]+4, img.shape[1]+4))
    temp_img[2:-2, 2:-2] = img

    out = np.zeros_like(img)
    for i in range(2, temp_img.shape[0]-2):
        for j in range(2, temp_img.shape[1]-2):
            mask1 = temp_img[i-2:i+1, j-2:j+1]
            mask2 = temp_img[i-1:i+2, j-2:j+1]
            mask3 = temp_img[i:i+3, j-2:j+1]

            mask4 = temp_img[i-2:i+1, j:j+3]
            mask5 = temp_img[i-1:i+2, j:j+3]
            mask6 = temp_img[i:i+3, j:j+3]

            mask7 = temp_img[i-2:i+1, j-1:j+2]
            mask8 = temp_img[i:i+3, j-1:j+2]

            masks = [mask1, mask2, mask3, mask4, mask5, mask6, mask7, mask8]

            vars_arr = []
            for mask in masks:
                vars_arr.append(np.var(mask))

            min_var = np.argmin(vars_arr)

            out[i-2, j-2] = np.median(masks[min_var])
    return out

def main():
    file = "/home/garo/Desktop/UZO-2022/cv5/images/cv05_robotS.bmp"
    bgr_img = cv2.imread(file)
    # bgr_img = cv2.imread('cv05_PSS.bmp')
    gray_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2GRAY)

    temp = mean_filter(gray_img, np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]]))
    #plot_images(gray_img, temp, 'Original', 'Mean')

    temp = rotation_mask_filter(gray_img)
    plot_images(gray_img, temp, 'Original', 'Rotation mask')

    temp = median_filter(gray_img)
    #plot_images(gray_img, temp, 'Original', 'Median')
    return


if __name__ == "__main__":
    main()
    