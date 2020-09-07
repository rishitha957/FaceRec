import cv2
import numpy as np 

downsampling_steps = 2
bilateral_filtering_steps = 7

img_color = cv2.imread('pro_pic_4.jpg')
print(img_color.shape)

img_color = cv2.resize(img_color,(800,800))

img_color_1 = img_color
for _ in range(downsampling_steps):
	img_color_1 = cv2.pyrDown(img_color_1)

for _ in range(bilateral_filtering_steps):
	img_color_1 = cv2.bilateralFilter(img_color_1, d=9, sigmaColor=9,sigmaSpace=7)

for _ in range(downsampling_steps):
	img_color_1 = cv2.pyrUp(img_color_1)

img_gray = cv2.cvtColor(img_color,cv2.COLOR_RGB2GRAY)
img_blur = cv2.medianBlur(img_gray,7)

img_edge = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
									cv2.THRESH_BINARY, blockSize=9, C=2)

img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)

img_cartoon = cv2.bitwise_and(img_color_1,img_edge)

stack = np.hstack([img_color,img_cartoon])
cv2.imshow("Stacked Images",stack)
cv2.waitKey(0)