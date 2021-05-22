"""
Open the image pic2.jpg and display it with the name pic2. 
Try to detect the image edges using Canny edge detector 
and display the result in a separate window. 
Then run the edge detector on a blurred version of an image 
(use a window size of your choice) and display the result 
in a different window to compare.
"""

import cv2 as cv

pic2 = cv.imread('pic2.jpg')
cv.imshow('Toucan', pic2)

canny = cv.Canny(pic2, 125, 127)
cv.imshow('Toucan_edges', canny)

blur = cv.GaussianBlur(pic2, (3,3), cv.BORDER_DEFAULT)
canny = cv.Canny(blur, 125, 127)
cv.imshow('Toucan_edges_blurred', canny)

cv.waitKey(0)
