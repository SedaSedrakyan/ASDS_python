"""
Open the image pic1.jpg and display it with the name pic1. 
Separate the image into its 3 channels. 
Display both the colored and grayscale versions of each channel in separate windows.
"""

import cv2 as cv
import numpy as np

pic1 = cv.imread('Photos/pic1.jpg') 

b, g, r = cv.split(pic1)

blank = np.zeros(pic1.shape[:2], dtype = 'uint8')
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('blue_grayscale', b)
cv.imshow('blue', blue)
cv.imshow('green_grayscale', g)
cv.imshow('green', green)
cv.imshow('red_grayscale', r)
cv.imshow('red', red)

cv.waitKey(0)

