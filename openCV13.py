# HOW TO BIND TRACKBAR TO OPENCV WINDOWS EXAMPLE 1
# TRACKBAR IS USED WHENEVER YOU WANT TO CHANGE SOME VALUE IN YOUR IMAGE DYNAMICALLY AT RUNTIME.
import numpy as np
import cv2 as cv

def nothing(x):
    print(x)

# create a black image in a window
img=np.zeros((300,512,3),np.uint8)

cv.namedWindow('image')

# This trackbar will change the BGR value of the image
cv.createTrackbar('B','image',0,255,nothing)
cv.createTrackbar('G','image',0,255,nothing)
cv.createTrackbar('R','image',0,255,nothing)

# Adding switch using a trackbar
switch='0 : OFF\n 1 : ON'
cv.createTrackbar(switch,'image',0,1,nothing)
while(1):
    cv.imshow('image',img)
    k=cv.waitKey(1) & 0xFF

    if k==27 :
        break

    # To get the current position of trackbar
    b=cv.getTrackbarPos('B','image')
    g = cv.getTrackbarPos('G', 'image')
    r = cv.getTrackbarPos('R', 'image')
    s=  cv.getTrackbarPos(switch, 'image')

    if s==0:
        img[:]=0
    else:
        # Set these value to our image
        img[:]=[b,g,r]

cv.destroyAllWindows()