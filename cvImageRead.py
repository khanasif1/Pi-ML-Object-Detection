#https://www.youtube.com/watch?v=qCR2Weh64h4&list=PLzMcBGfZo4-lUA8uGjeXhBUUzPYc6vZRn
# Custom prediction : https://www.youtube.com/watch?v=a1BmKSYZUi8
#https://teachablemachine.withgoogle.com/train/image
from operator import truediv
import cv2
import numpy as np

# img = cv2.imread('assets\person.jpg', cv2.IMREAD_GRAYSCALE)
# cv2.imshow('Image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('frame', gray)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()