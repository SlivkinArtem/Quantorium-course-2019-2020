import cv2


img = cv2.imread('pic.jpg') #standart

cv2.line(img, (100, 100), (320, 440), (0, 0, 255), 4)
cv2.rectangle(img, (100, 100), (320, 440), (0, 0, 255), 4)
cv2.circle(img, (210, 270), 60, (0, 0, 255), -1)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OH SHIT', (400, 500), font, 6, (250, 0, 0), 6)

cv2.imshow('simple picture', img) #image show

cv2.waitKey(0) # ждём нажатие клавиши
cv2.destroyAllWindows()