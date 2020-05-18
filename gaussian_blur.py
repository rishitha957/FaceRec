import cv2
import numpy as np 

pic = cv2.imread('monsters_inc_3.jpg')

matrix = (7,7)

blur = cv2.GaussianBlur(pic, matrix, 0)

cv2.imshow('blur', blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
