import cv2
import numpy as np

img = cv2.imread('/home/garo/Desktop/UZO-2022/cv2/cv02_vzor_hrnecek.bmp')
print('Original Dimensions : ', img.shape)

roi = img[20: 145, 10: 104]
x = 260
y = 157
width = 150
height = 170
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
roi_hist = cv2.calcHist([hsv_roi], [0], None, [180], [0, 180])

cap = cv2.VideoCapture('cv02_hrnecek.mp4')

term_criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

while True: 
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
    
    ret, track_window = cv2.CamShift(mask, (x, y, width, height), term_criteria)
    x = track_window[0]
    y = track_window[1]
    
    #width = track_window[2]
    #height = track_window[3]

    print("x, y, width, height", x, y, width, height)
    #print("trackWindow:", track_window[0])
    print("ret:", ret)


    pts = cv2.boxPoints(ret)
    pts = np.int0(pts)
    cv2.polylines(frame, [pts], True, (0, 255, 0), 2)

    cv2.imshow("mask", mask)
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(30)
    if key == 27:
        break
    if key == 32:
        cv2.waitKey(0)
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()