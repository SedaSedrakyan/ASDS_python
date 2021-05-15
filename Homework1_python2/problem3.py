import cv2 as cv

def rescaleFrame(frame, scale = 0.5):
    
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread('pic1.jpg')

img_rescaled = rescaleFrame(img)

cv.imshow('City', img)
cv.imshow('City_rescaled', img_rescaled)


cv.waitKey(0)


