import cv2

img = cv2.imread('pic.jpg') #standart
gray_img = cv2.imread('pic.jpg', cv2.IMREAD_GRAYSCALE)
#cv2.resize()
cv2.imshow('simple picture', img) #image show
cv2.imshow('simple picture', gray_img) # image to gray
cv2.waitKey(0) # ждём нажатие клавиши

cv2.destroyAllWindows()

cv2.imwrite('gray_pic.jpg', gray_img)



