import cv2

#Read image
img=cv2.imread('lena.jpg',0)
print(img)

# Display Image
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Writing an image to a file using imwrite function
cv2.imwrite('lena_copy.png',img)
