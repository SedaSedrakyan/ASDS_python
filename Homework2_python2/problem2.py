"""
Open the image pic1.jpg and display it with the name pic1. 
Blur the image using Gaussian blur using 2 different windows sizes: 
(3, 3) and (11, 11) and display both versions in separate windows 
to compare with the original image.
"""

import cv2 as cv

pic1 = cv.imread('pic1.jpg')
cv.imshow('Sheep', pic1)

blur_3 = cv.GaussianBlur(pic1, (3,3), cv.BORDER_DEFAULT)
cv.imshow('Blurred by 3', blur_3)

blur_11 = cv.GaussianBlur(pic1, (11, 11), cv.BORDER_DEFAULT)
cv.imshow('Blurred by 11', blur_11)

cv.waitKey(0)