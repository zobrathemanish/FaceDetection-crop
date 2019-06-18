import cv2
import NameFind
from random import randint

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# To capture video from webcam. 
# cap = cv2.VideoCapture(0)
# To use a video file as input 
cap = cv2.VideoCapture(0)

# cap = cv2.VideoCapture('cropvideo.mp4')

# cap.get(cv2.CAP_PROP_FPS)

while True:
    # Read the frame
    _, img = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        gray_face = cv2.resize((gray[y: y+h, x: x+w]), (110, 110))
        eyes = eye_cascade.detectMultiScale(gray_face)

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
    # Display
    cv2.imshow('img', img)

    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
        
# Release the VideoCapture object
cap.release()