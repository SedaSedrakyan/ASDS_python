"""
Open the image pic2.jpg and display it with the name pic2. 
Apply the correct method so that 
only a circle of radius of 70 pixels is left 
right in the middle of the picture. 
Your result should look similar to the example below.
"""
import cv2 as cv
import numpy as np

pic2 = cv.imread('Photos/pic2.jpg') 
cat = cv.imread('Photos/cat.jpg') 
blank = np.zeros(pic2.shape[:2], dtype = 'uint8')

mask = cv.circle(blank, (pic2.shape[1]//2, pic2.shape[0]//2), 70, 255, -1)

cv.imshow('original', pic2) 
cv.imshow('mask', mask) 

masked_image = cv.bitwise_and(pic2, pic2, mask=mask)

cv.imshow('original image', pic2) 
cv.imshow('result', masked_image) 

cv.waitKey(0)