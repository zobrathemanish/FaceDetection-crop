import glob
import base64
import cv2
import face_recognition
import os
from random import randint


checkedFolder = 'checked_images/*'

crop_img = 'buffer_for_crop_images/1.jpg'

path = '/home/velar/Desktop/test_face/facedetection-master/test'

falser = []

with open('/home/velar/Desktop/test_face/facedetection-master/checked_images/323198.jpg', "rb") as image_file:
    lmm_image = face_recognition.load_image_file(image_file)
    lmm_face_encoding = face_recognition.face_encodings(lmm_image)[0]


filepath = '/home/velar/Desktop/test_face/facedetection-master/checked_images/590437.jpg'
shot = cv2.imread(filepath)
face_locations = face_recognition.face_locations(shot)
face_encodings = face_recognition.face_encodings(shot, face_locations)

# print(face_encodings)

match = face_recognition.compare_faces(lmm_face_encoding, face_encodings, tolerance=0.6)
print(match)

            


    
 # img = cv2.imread(crop_img, 1)
 #                path = '/home/velar/Desktop/test_face/facedetection-master/checked_images'
 #                cv2.imwrite(os.path.join(path , 'waka.jpg'), img)
 #                cv2.waitKey(0)