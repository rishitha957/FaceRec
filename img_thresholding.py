import cv2
import numpy as numpy

pic = cv2.imread('monsters_inc_3.jpg',0)

threshold_val = 200

(t_val, binary_threshold) = cv2.threshold(pic,threshold_val,255,cv2.THRESH_BINARY)

cv2.imshow('threshold',binary_threshold)
cv2.waitKey()
cv2.destroyAllWindows()