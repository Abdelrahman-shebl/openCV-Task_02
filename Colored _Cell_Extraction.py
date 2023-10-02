import cv2 as cv
import numpy as np

photo=cv.imread("photo.jpg")
cv.imshow("window",photo)
lower=np.array([60, 100, 100])
upper=np.array([180, 255, 255])

hsv=cv.cvtColor(photo,cv.COLOR_BGR2HSV)

mask=cv.inRange(hsv,lower,upper)
contours,_=cv.findContours(mask,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)

number_of_green_cells=len(contours)

filtered_image=cv.bitwise_and(photo,photo,mask=mask)

print("the number of green cells = %d" %number_of_green_cells)
cv.imshow("filtered_image",filtered_image)

cv.waitKey(0)

