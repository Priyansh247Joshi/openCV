# Draw Geometric Shape on Images using Python openCV
import numpy as np
import cv2

# Create image using numpy zeros method
#img=np.zeros([512,512,3],np.uint8)
img=cv2.imread('lena.jpg',1)
# Now lets draw a line on image that we read from imread function
img=cv2.line(img,(0,0),(255,255),(67,70,150),10)

# Now lets draw an arrowed  line on image that we read from imread function
img=cv2.arrowedLine(img,(0,250),(255,0),(67,70,150),10)

# Now Create Rectangle
img=cv2.rectangle(img,(384,0),(510,128),(200,45,89),5)

# Create Circle
img=cv2.circle(img,(447,63),63,(100,34,67),-1)

# Put Text into image
font=cv2.FONT_ITALIC
img=cv2.putText(img,'Hey lena Here',(1,340),font,1.6,(34,56,78),3,cv2.LINE_4)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
