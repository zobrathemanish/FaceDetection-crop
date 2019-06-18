import cv2
from random import randint
import time

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_profileface.xml')

# To capture video from webcam. 
# cap = cv2.VideoCapture(0)
# To use a video file as input 
cap = cv2.VideoCapture('cropvideo.mp4')


# cap.get(cv2.CAP_PROP_FPS)

def rescale_frame(frame, percent):
    scale_percent = percent
    width = int(frame.shape[0] * scale_percent/50)
    height = int(frame.shape[1] * scale_percent/120)
    dim = (width, height)
    return cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

while True:
    # Read the frame
    _, img = cap.read()
    img = rescale_frame(img, percent = 40)
    draw = img.copy()

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        crop_img = draw[y:y+w, x:x+h]
        cv2.imwrite(str(randint(0,10000000000))+".jpg",crop_img)

    # Display
    cv2.imshow('img', img)

    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
        
# Release the VideoCapture object
cap.release()