import cv2 as cv

capture = cv.VideoCapture('vid1.mp4')

while True:
    isTrue, frame = capture.read() 
    
    if frame is not None:
        cv.imshow('vid1', frame)
    else:
        print('empty frame')
        exit(1)
    
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
    
cv.waitKey(0)