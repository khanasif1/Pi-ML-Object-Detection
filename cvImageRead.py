#https://www.youtube.com/watch?v=qCR2Weh64h4&list=PLzMcBGfZo4-lUA8uGjeXhBUUzPYc6vZRn
import cv2

img = cv2.imread('assets\person.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
