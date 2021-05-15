import cv2 as cv

img = cv.imread('pic2.jpg')
img1 = cv.imread('pic2.jpg')
cv.circle(img,(img.shape[1]//2, img.shape[0]//2),
		  img.shape[0]//3, (0, 0, 255), thickness = -1)

cv.imshow('With_Circle', img)
cv.imshow('Original', img)

cv.waitKey(0)