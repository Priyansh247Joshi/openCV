# Adaptive Thresholding
# A method where the threshold value is calculated for the smaller region means
# the threshold value is not global for all pixels. So there will be different threshold
# value for different region.

import cv2 as cv
import numpy as np
img=cv.imread('sudoku.png',0)

_,th1=cv.threshold(img,127,255,cv.THRESH_BINARY)
th2=cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)
th3=cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)
cv.imshow('Image',img)
#cv.imshow('th1',th1)
cv.imshow('th2',th2)
cv.imshow('th3',th3)
cv.waitKey(0)
cv.destroyAllWindows()