import cv2


cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Original', frame)


    if cv2.waitKey() & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()