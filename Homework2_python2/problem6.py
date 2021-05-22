'''
Open the image pic3.jpg and display it with the name pic3. 
Find the edges of the image using Canny edge detector and 
then try to find its contours with parameters of your choice. 
Then convert the original image to grayscale and try to find 
the contours on a blurred version of the grayscale of the original image. 
Display the 2 results in separate windows to compare.
'''

import cv2 as cv

pic3 = cv.imread('pic3.jpg') 
pic3_orig = cv.imread('pic3.jpg')
canny = cv.Canny(pic3, 125, 175)
gray = cv.cvtColor(pic3_orig, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)

contours_can, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
contours_blur, hierarchies = cv.findContours(blur, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

cv.drawContours(pic3, contours_can, -1, (0, 0, 255), 1)
cv.imshow('contours with canny', pic3)
cv.drawContours(pic3_orig, contours_blur, -1, (0,0,255), 1)
cv.imshow('contours with blur', pic3_orig)

cv.waitKey(0)
