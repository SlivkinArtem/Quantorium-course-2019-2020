import numpy as np
import cv2

img = cv2.imread('tree.jpeg')
size = 15
#rows, cols = img.shape[:2]
print(img)
kernel_motion = np.zeros((size, size))
kernel_motion[int((size-1)/2), :] = np.ones(size)
kernel_motion /= size

light_blurring = cv2.filter2D(img, -1, kernel_motion)

cv2.imshow('original', img)
cv2.imshow('light blur', light_blurring)

cv2.waitKey()
cv2.destroyAllWindows()
