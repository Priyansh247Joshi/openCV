# Add more Images
# we do it by add() method.
# resize() method is to resize the image
import numpy as np
import cv2

img= cv2.imread('messi5.jpg')
img2=cv2.imread('opencv-logo.png')

print(img.shape) # returns a tuple of number of rows , columns , and channels
print(img.size) # returns total number of pixels is accessed
print(img.dtype) # returns the data-type of image

b , g , r = cv2.split(img)
img = cv2.merge((b,g,r))
# Now copy the ball to another place using ROI(Region of interest)

ball =img[280:340 , 330: 390]
img[273:333,100:160]=ball
img=cv2.resize(img,(512,512))
img2=cv2.resize(img2,(512,512))
dest_img=cv2.add(img,img2)


cv2.imshow('image',dest_img)
cv2.waitKey(0)
cv2.destroyAllWindows()