"""
Perform appropriate operations to get a results similar to the images below:
"""
import cv2 as cv
import numpy as np

blank = np.zeros((400, 400, 3), dtype='uint8')

rectangle1 = cv.rectangle(blank.copy(), (30, 30), (370, 370), (130, 130, 130), -1)
rectangle2 = cv.rectangle(blank.copy(), (30, 30), (370, 370), (120, 0, 250), -1)

circle1 = cv.circle(blank.copy(), (200, 200), 200, (130, 130, 130), -1)
circle2 = cv.circle(blank.copy(), (200, 200), 200, (120, 0, 250), -1)

bitwise_xor = cv.bitwise_xor(rectangle1, circle1)
bitwise_or1 = cv.bitwise_or(rectangle1, circle1)
bitwise_xor2 = cv.bitwise_xor(rectangle2, circle2)

cv.imshow('bitwise_xor', bitwise_xor)
cv.imshow('bitwise_or1', bitwise_or1)
cv.imshow('bitwise_or2', bitwise_xor2)

cv.waitKey(0)