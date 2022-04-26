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
    #width = int(img.shape[1] * value / 100)
    #height = int(img.shape[0] * value / 100)

    ratio = float(img.shape[1]) / float(img.shape[0])
    height = int(math.sqrt(value / ratio) + 0.5)
    width = int((height * ratio) + 0.5)
    dim = (width, height)
    resize = cv2.resize(img, dim)
    return resize

def rotation(image, degree):
    # Převod stupnu na raidiany
    rads = math.radians(degree)
    
    # vyska sirka rotated image
    height_rot_img = round(abs(image.shape[0]*math.cos(rads))) + \
                       round(abs(image.shape[1]*math.sin(rads)))
    width_rot_img = round(abs(image.shape[1]*math.cos(rads))) + \
                       round(abs(image.shape[0]*math.sin(rads)))

    rot_img = np.uint8(np.zeros((height_rot_img,width_rot_img,image.shape[2])))
    
    # Center orig img
    cx, cy = (image.shape[1]//2, image.shape[0]//2)

    # Center rotate img
    midx,midy = (width_rot_img//2, height_rot_img//2)
    #
    # aplikovani - [x′y′]=[cos(θ) −sin(θ)
    #                      sin(θ)  cos(θ)]
    #                     [xy]
    for i in range(rot_img.shape[0]):
        for j in range(rot_img.shape[1]):
            x= (i-midx)*math.cos(rads)+(j-midy)*math.sin(rads)
            y= -(i-midx)*math.sin(rads)+(j-midy)*math.cos(rads)

            x=round(x)+cy
            y=round(y)+cx

            if (x>=0 and y>=0 and x<image.shape[0] and  y<image.shape[1]):
                rot_img[i,j,:] = image[x,y,:]

    return rot_img 


if __name__ == "__main__":
    img = cv2.imread('/home/garo/Desktop/UZO-2022/cv3/cv03_robot.bmp')
    resize = resizeImg(300000, img)
    shear = shearImg(img)
    rotated_image1 = rotation(img, 30)
    rotated_image2 = rotation(img, 60)

    rotated_image3 = rotation(img, 90)

    rotated_image4 = rotation(img, 120)
    rotated_image5 = rotation(img, 150)
    rotated_image6 = rotation(img, 180)

    rotated_image7 = rotation(img, 210)
    rotated_image8 = rotation(img, 240)

    rotated_image9 = rotation(img, 270)

    rotated_image10 = rotation(img, 300)

    rotated_image11 = rotation(img, 330)
    rotated_image12 = rotation(img, 360)




    while True:
        cv2.imshow("Original", img)
        #cv2.imshow("Resize", resize)
        #cv2.imshow("Shear", shear)
        cv2.imshow("Rotated 30", rotated_image1)
        cv2.imshow("Rotated 60", rotated_image2)
        cv2.imshow("Rotated 90", rotated_image3)
        cv2.imshow("Rotated 120", rotated_image4)
        cv2.imshow("Rotated 150", rotated_image5)
        cv2.imshow("Rotated 180", rotated_image6)
        cv2.imshow("Rotated 210", rotated_image7)
        cv2.imshow("Rotated 240", rotated_image8)
        cv2.imshow("Rotated 270", rotated_image9)
        cv2.imshow("Rotated 300", rotated_image10)
        cv2.imshow("Rotated 330", rotated_image11)
        cv2.imshow("Rotated 360", rotated_image12)

        key = cv2.waitKey(0)
        if key == 27:
            break