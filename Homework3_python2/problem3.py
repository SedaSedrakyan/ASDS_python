"""
Open the image pic2.jpg and display it with the name pic2. 
Blur the picture using average and bilateral blurring methods 
and display in separate windows. 
(For the parameters, use the values of your choice). 
Write a short comment if you see any particular difference 
when using different parameter values for the second method 
and comparing it to the averaging method.
"""

import cv2 as cv
import numpy as np

pic2 = cv.imread('Photos/pic2.jpg') 

cv.imshow('original', pic2)

average = cv.blur(pic2, (7,7))

cv.imshow('average blur', average)

bilateral1 = cv.bilateralFilter(pic2, 5, 15, 15)  

cv.imshow('bilateral_1', bilateral1)

bilateral = cv.bilateralFilter(pic2, 10, 50, 70)

cv.imshow('bilateral_2', bilateral)
# While comparing the averaging and biletral methods
# biletral method is more clear and edges are retained
# Biletral 1 is more clear compared to biletral 2
# as sigmavalue is bigger in case of biletral_2

cv.waitKey(0)


