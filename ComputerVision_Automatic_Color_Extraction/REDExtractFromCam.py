'''Extract only the RED portion of the frame'''


#import the necessary packages
import cv2
import numpy as np

cap=cv2.VideoCapture(0) #open the video device to start capturing frames

while(1):
	
	ret,img=cap.read()
	img_hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #conversion of BGR format to HSV format
	#create two masks with Hue values only between 0-10 and 170-180
	lower_red = np.array([0,50,50])
	upper_red = np.array([10,255,255])
	mask0 = cv2.inRange(img_hsv, lower_red, upper_red)
	lower_red = np.array([170,50,50])
	upper_red = np.array([180,255,255])
	mask1 = cv2.inRange(img_hsv, lower_red, upper_red)
	mask = mask0+mask1
	output_img = img.copy()
	output_img[np.where(mask==0)] = 0 #make everything other than RED as BLACK
	
	#show the output
	cv2.imshow("original", img)
	cv2.imshow('output',output_img)
	if (cv2.waitKey(1) & 0xFF == ord('q')):
		break

cv2.destroyAllWindows()
