import cv2
import numpy as np 

cp = cv2.VideoCapture("earth_video.mp4")

while cp.isOpened():
	ret, frame = cp.read()
	cv2.imshow('vid',frame)
	if cv2.waitKey(1) and 0xFF==ord("q"):
		break

cp.release()
cv2.destroyAllWindows()