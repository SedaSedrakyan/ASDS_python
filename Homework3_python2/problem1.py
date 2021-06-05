"""
Open the image pic1.jpg and display it with the name pic1. 
Convert the image to the following formats 
and display in separate windows: RGB, HSV, LAB, grayscale.
"""

import cv2 as cv

pic1 = cv.imread('Photos/pic1.jpg') 

rgb = cv.cvtColor(pic1, cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb) 

hsv = cv.cvtColor(pic1, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv) 

lab = cv.cvtColor(pic1, cv.COLOR_BGR2LAB)
cv.imshow('lab', lab) 

gray = cv.cvtColor(pic1, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

cv.waitKey(0)