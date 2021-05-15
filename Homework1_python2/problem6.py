import cv2 as cv

img = cv.imread('pic2.jpg')
img1 = cv.imread('pic2.jpg')

cv.rectangle(img1, (img1.shape[1]//4, img1.shape[0]//4), 
             (img1.shape[0] - img1.shape[0]//4,
              img1.shape[1] - img1.shape[1]//4),
             (0, 165, 255), thickness = 2)

cv.imshow('With_Rectangle', img1)
cv.imshow('Original', img)

cv.waitKey(0)
