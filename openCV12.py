# BITWISE OPERATIONS
import cv2
import numpy as np

img1=np.zeros((300,400,3),np.uint8)
img1=cv2.rectangle(img1,(200,0),(300,100),(255,255,255),-1)
img2=cv2.imread('pic1.png')
# BITWISE AND OPERATION
#bitAnd= cv2.bitwise_and(img2,img1)

# BITWISE OR OPERATION
#bitwiseOr=cv2.bitwise_or(img2,img1)

# BITWISE XOR OPERATION
#bitwiseXOR=cv2.bitwise_xor(img2,img1)

# BITWISE NOT OPERATION
bitNot1=cv2.bitwise_not(img1)
bitNot2=cv2.bitwise_not(img2)

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
#cv2.imshow('bitAnd',bitwiseAnd)
#cv2.imshow('bitOr',bitwiseOr)
#cv2.imshow('bitXOR',bitwiseXOR)
cv2.imshow('bitNot1',bitNot1)
cv2.imshow('bitNot2',bitNot2)
cv2.waitKey(0)
cv2.destroyAllWindows()