import cv2
import os
img = cv2.imread('pp.jpg', 1)
path = '/home/velar/Desktop/test_face/facedetection-master/checked_images'
cv2.imwrite(os.path.join(path , 'waka.jpg'), img)
cv2.waitKey(0)