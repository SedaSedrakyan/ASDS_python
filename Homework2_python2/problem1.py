"""
Open the image pic1.jpg and display it with the name pic1. 
Convert the image to grayscale and display in a separate window 
to compare with the original image.
"""
import cv2 as cv

pic1 = cv.imread('pic1.jpg')
cv.imshow('Sheep', pic1)

gray = cv.cvtColor(pic1, cv.COLOR_BGR2GRAY)
cv.imshow('Black and White sheep', gray)
cv.waitKey(0)