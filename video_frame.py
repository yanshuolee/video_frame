import numpy as np
import cv2
cap = cv2.VideoCapture(0)

while(True):
    
    ret, frame = cap.read()
	
    img = cv2.imread('frame.png')
    img = cv2.resize(img,(640,480))
	
    rows,cols,channels = img.shape
    roi = frame[0:rows, 0:cols ]
	
    img2gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret, mask01 = cv2.threshold(img2gray, 5, 255, cv2.THRESH_BINARY)
    mask02 = cv2.bitwise_not(mask01)
    dst_bg = cv2.bitwise_and(roi,roi,mask = mask02)
    dst_fg = cv2.bitwise_and(img,img,mask = mask01)
    dst = cv2.add(dst_bg,dst_fg)
    frame[0:rows, 0:cols] = dst

    cv2.imshow('Result',frame)
	# press exc to exit
    if cv2.waitKey(1) & 0xFF == 27:
        break


cap.release()
cv2.destroyAllWindows()