import cv2
import numpy as np 

pic = cv2.imread("monsters_inc_3.jpg")

dimpixel = 7
color = 100
space = 100

filter1 = cv2.bilateralFilter(pic, dimpixel,color,space)

cv2.imshow('bilateralFilter', filter1)
cv2.waitKey(0)
cv2.destroyAllWindows()