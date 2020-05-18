import cv2
import numpy as np 

pic = cv2.imread('monsters_inc_3.jpg')

threshold_val1 = 50
threshold_val2 = 100

canny = cv2.Canny(pic,threshold_val1,threshold_val2)
cv2.imshow("Canny", canny)
cv2.waitKey(0)
cv2.destroyAllWindows()