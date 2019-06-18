import cv2
from random import randint

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Read the input image
img = cv2.imread('test.jpg')

draw = img.copy()

# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Draw rectangle around the faces

for box in faces:
    for coord in box:
        print(int(coord), end=" ", flush=True)
    print()

for (x, y, w, h) in faces:
  crop_img = draw[y:y+w, x:x+h]
  cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
  cv2.imwrite(str(randint(0,50))+".jpg",crop_img)

# Display the output
cv2.imshow('img', img)
cv2.waitKey()



 