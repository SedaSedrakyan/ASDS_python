"""
Open the image pic2.jpg and display it with the name pic2. 
Resize the image to have 2 times bigger width 
and the same height as the original image, 
use INTER_AREA interpolation. 
Then resize the original image 
to have 2 times smaller height 
and the same width as the original image, 
use INTER_CUBIC interpolation. 
Display both versions in separate windows.
"""

import cv2 as cv 

pic2 = cv.imread('pic2.jpg')

pic_resize_wide = cv.resize(pic2, (pic2.shape[1] * 2, pic2.shape[0]),
							interpolation = cv.INTER_AREA)
cv.imshow('Toucan_wide', pic_resize_wide)

pic_resize_short = cv.resize(pic2, (pic2.shape[1], pic2.shape[0]//2),
							 interpolation = cv.INTER_CUBIC)
cv.imshow('Toucan_short', pic_resize_short)

cv.waitKey(0)