# Image Pyramid with python and OPENCV
import cv2
import numpy as np

img=cv2.imread('lena.jpg')
layer=img.copy()
gp=[layer]

for i in range(6):
    layer=cv2.pyrDown(layer)
    gp.append(layer)
  #  cv2.imshow(str(i),layer)

layer=gp[5]
cv2.imshow('Upper Level Gaussian Pyramid',layer)
lp=[layer]

for i in range(5,0,-1):
    gaussian_extended=cv2.pyrUp(gp[i])
    laplacian=cv2.subtract(gp[i-1],gaussian_extended)
    cv2.imshow(str(i),laplacian)
cv2.imshow('Original Image',img)

#lr1=cv2.pyrDown(img)
#lr2=cv2.pyrDown(lr1)
#hr1=cv2.pyrUp(lr2)
#cv2.imshow('pyrDown1 Image',lr1)
#cv2.imshow('pyrDown2 Image',lr2)
#cv2.imshow('pyrUp1 Image',hr1)
cv2.waitKey(0)
cv2.destroyAllWindows()