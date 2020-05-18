import cv2
import numpy as np 

pic = cv2.imread("monsters_inc_3.jpg")

kernel = 3

median = cv2.medianBlur(pic, kernel)

cv2.imshow('Median Blur', median)
cv2.waitKey(0)
cv2.destroyAllWindows()