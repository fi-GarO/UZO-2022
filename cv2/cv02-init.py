import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
import time

plt.ion()
clear = lambda: os.system('clear')
clear()
plt.close('all')

cap = cv2.VideoCapture('cv02_hrnecek.mp4')
hrnek = cv2.imread('/home/garo/Desktop/UZO-2022/cv2/cv02_vzor_hrnecek.bmp')

# RGB to Hue - hue je od 0 do 1
# Hue to histogram
# Histogram / maximum
# Vezmu hrnicek, prevedu do HUE a pustim na nej histogram
# projit for cyklem pres vsechny body. New(y, x) = histo(H(y,x))
# pouze pro prvni snimek teziste - vezmu predchozi snimek a udelam prevod pres hue a histogram a dopocitani teziste

# new(y,x) = hist(H(y,x))
# This is correct 
hrnekX = hrnek[1]
hrnekY = hrnek[0]
hsv = cv2.cvtColor(hrnek, cv2.COLOR_RGB2HSV)
hist, b = np.histogram(hsv[:,:,0], 256, (0, 256))
hist1 = hist.astype(float)
plt.hist(hist, b)
plt.show()

maxH = np.max(hist)
minH = np.min(hist)
maxG = np.max(b)
minG = np.min(b)

hist1 /= maxH
id = 0
# Tento while je pro druhej a treti snimek
while True:
    ret, bgr = cap.read()
    if not ret:
        break
    hsv = cv2.cvtColor(bgr, cv2.COLOR_RGB2HSV)
    hist, b = np.histogram(hsv[:,:,0], 256, (0, 256))
    # X a Y potreba dopocitat v algoritmu, dosadit
    #velikost ctverce
    
    x1 = maxH
    y1 = maxG

    # Pozice ctverce
    x2 = minH
    y2 = minH
    #cv2.rectangle(bgr, (x1, y1), (x2, y2), (0, 255, 0))
    cv2.imshow('Image', bgr)
    key = 0xFF & cv2.waitKey(0)
    if key == 27:
        break
cv2.destroyAllWindows()