# More mouse event example in OpenCV Python
# Drawing points and then connecting those points using line.
import numpy as np
import cv2
def click_event(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),3,(58,87,69),-1)
        points.append((x,y))

        if(len(points) >=2):
            cv2.line(img,points[-1],points[-2],(255,0,0),5)
        cv2.imshow('image',img)

img=cv2.imread('lena.jpg',1)
cv2.imshow('image',img)
points=[]
cv2.setMouseCallback('image',click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()