import cv2 as cv

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)

def rescaleFrame(frame, scale=0.75): #works for Images, videos, and live video
    #converting floating to int
    width = int(frame.shape[1] * scale) #frame.shape[1] is the width of image
    height = int(frame.shape[0] * scale) #frame.shape[0] is the height of image
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA) #source, dimension, interpolation 

def changeRes(width, height): # ONLY works for live video
    capture.set(3, width) # 3 stands for width
    capture.set(4,height) # 4 stands for height

cv.imshow('Image', rescaleFrame(img))
capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, 0.20)

    cv.imshow('Video', frame)
    cv.imshow("Video Resized", frame_resized)

    if cv.waitKey(20) &  0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows() 