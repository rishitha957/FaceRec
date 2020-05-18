import numpy as np 
import cv2

# img = cv2.imread('monsters_inc_3.jpg')
# cv2.imshow('Original',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# pic = np.zeros((500,500,3), dtype='uint8')

# cv2.rectangle(pic, (0,0), (499,150), (123,200,98), lineType=0, shift=0)
# cv2.line(pic, (350, 350), (499, 350), (0, 0, 255))
# cv2.circle(pic, (250,250), 50, (255,0,0))
# cv2.putText(pic, "TEXT", (100,100), cv2.FONT_HERSHEY_DUPLEX, 3, (0,255,0), 4, cv2.LINE_8)
# cv2.imshow('dark',pic)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


pic = cv2.imread('monsters_inc_3.jpg')
print(type(pic))
cols = pic.shape[1]
rows = pic.shape[0]
center = (cols/2, rows/2)
angle=90

M = np.float32([[1,0,150], [0,1,70]])

shifted = cv2.warpAffine(pic, M, (cols,rows))
# cv2.imshow('shifted', shifted)

M1 = cv2.getRotationMatrix2D(center, angle, 1)
rotate = cv2.warpAffine(shifted, M1, (cols,rows))

cv2.imshow('rotated', rotate)
cv2.waitKey(0)
cv2.destroyAllWindows()
