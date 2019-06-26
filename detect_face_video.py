#!/usr/bin/env python2

import cv2
from random import randint
import time
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import glob
import os
import base64
import json
import time
import requests
import face_recognition
from PIL import Image

a = 0
resolution_error = 0
matchurl = "https://api.facesoft.io/v1/face/match"

headers = {
    'apikey': "fe0nlnp9bnk-l22eprt295i"  # Insert your API key here
}

ENCODING = 'utf-8'

path = '/home/velar/Desktop/test_face/facedetection-master/checked_images'

pather = '/home/velar/Desktop/test_face/facedetection-master/checked_images'

# Load the cascade
# face_cascade = cv2.CascadeClassifier('haarcascade_profileface.xml')

# To capture video from webcam. 
# cap = cv2.VideoCapture(0)
# To use a video file as input 

face_cascade = cv2.CascadeClassifier('haarcascade_profileface.xml')

cap = cv2.VideoCapture('cropvideo.mp4')


# fps = cap.get(cv2.CAP_PROP_FPS)
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

falser = []

def rescale_frame(frame, percent):
    scale_percent = percent
    width = int(frame.shape[0] * scale_percent/50)
    height = int(frame.shape[1] * scale_percent/120)
    dim = (width, height)
    return cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

frame_number = 1



while True:
    # Read the frame
    _, img = cap.read()
    # img = rescale_frame(img, percent = 40)
    draw = img.copy()

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

   

    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        crop_img = draw[y:y+w, x:x+h]
        
        cv2.imwrite('buffer_for_crop_images/' + "1.jpg",crop_img)

        # print("Cropped the face from the shot")

        

        # cv2.imshow('first_crop', first_crop)
        # first_image = cv2.imwrite("ramlal.jpg", crop_img)
        
        checkedFolder = 'checked_images/*'

        if not os.listdir('checked_images'):
            cv2.imwrite('checked_images/' + "first_image.jpg",crop_img)


            # print("written the first image to checked images")
        else:
            with open('buffer_for_crop_images/1.jpg', "rb") as image_file:
                crop_img = 'buffer_for_crop_images/1.jpg'
                lmm_image = face_recognition.load_image_file(image_file)

                # Assume the whole image is the location of the face
                height, width, _ = lmm_image.shape

                # location is in css order - top, right, bottom, left
                face_location = (0, width, height, 0)

                lmm_face_encoding = face_recognition.face_encodings(lmm_image, known_face_locations=[face_location])[0]


                for filepath in glob.iglob('checked_images/*'):

                    # print(filepath)

                    shot = cv2.imread(filepath)
                    face_locations = face_recognition.face_locations(shot)
                    face_encodings = face_recognition.face_encodings(shot, face_locations)

                    # print(face_encodings)
                    try:
                    
                        match = face_recognition.compare_faces(lmm_face_encoding, face_encodings, tolerance=0.65)

                        falser.append(match[0])

                    except Exception:
                        # global resolution_error
                        # resolution_error = resolution_error + 1
                        print("The resolution is too low to figure out!!")
                        resolution_error = 1


        print(falser)

        a = a + 1

        match_count = 0

        for r in falser:
            if(r == True):
                match_count = match_count + 1

        if(match_count == 1):
            print("No need to add")
        elif(match_count == 0):
            print("Please add the image into registration. This is the new face")
            
            try:
                
                img = cv2.imread(crop_img)      
                cv2.imwrite(os.path.join(pather , str(a) + ".jpg"), img)
                if(resolution_error == 1):
                    os.remove("checked_images/" + str(a) + ".jpg")

                resolution_error = 0


            except Exception:
                print("This is the first image, of registration. So this exception has arise!!")

                    # print(match[0])

                    # if(match[0] == False):
                    #     img = cv2.imread(crop_img)      
                    #     # cv2.imwrite(os.path.join(pather , str(randint(1, 1000000)) + ".jpg"), img)


                    #     print(match[0])
                    #     falser.append(match[0])
        # print('Frame Number {} {}'.format(frame_number, falser))
        # frame_number = frame_number + 1
        falser = []
        match_count = 0

        print(resolution_error)

            #         pather = '/home/velar/Desktop/test_face/facedetection-master/test'

            #         false_count = 0     
                            
            #         for g in falser:
            #             if(g == False):
            #                 false_count = false_count + 1
                
            # print(false_count)


                    # if(false_count >= 1):

                    #     img = cv2.imread(crop_img)      
                    #     cv2.imwrite(os.path.join(pather , str(randint(1, 10)) + ".jpg"), img)

                        # falser = []
                            
                    # break


