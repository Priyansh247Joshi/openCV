#Simple Image Thresholding with matplotlib
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img=cv.imread('gradient.png',0)
_,th1=cv.threshold(img,127,255,cv.THRESH_BINARY)
_,th2=cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
_,th3=cv.threshold(img,127,255,cv.THRESH_TRUNC)
_,th4=cv.threshold(img,127,255,cv.THRESH_TOZERO)
_,th5=cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)

titles=['Original Images','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images=[img,th1,th2,th3,th4,th5]

for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]) , plt.yticks([])
plt.show()