# More mouse event example in OpenCV Python 2
# Read the image and click at any point on image and then show the color
# of points on which I clicked using second window.
import numpy as np
import cv2
def click_event(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        blue= img[x,y,0]
        green = img[x,y,1]
        red = img[x,y,2]
        cv2.circle(img,(x,y),3,(0,0,255),-1)
        mycolorImage=np.zeros((512,512,3),np.uint8)
        mycolorImage[:]=[blue,green,red]
        cv2.imshow('color',mycolorImage)



img=cv2.imread('lena.jpg',1)
cv2.imshow('image',img)
cv2.setMouseCallback('image',click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()