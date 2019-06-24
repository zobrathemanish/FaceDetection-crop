import os
import base64
import json

import requests
ENCODING = 'utf-8'

matchurl = "https://api.facesoft.io/v1/face/match"

headers = {
  'apikey': "fe0nlnp9bnk-l22eprt295i"  # Insert your API key here
}


with open("/home/velar/Desktop/face_recog_crop/face_recognition_crop/girly_sujal.jpg", "rb") as image_file:
  encoded_string1 = base64.b64encode(image_file.read())

  # print(type(b64string1))

with open("/home/velar/Desktop/face_recog_crop/face_recognition_crop/two.JPG", "rb") as image_file:
  encoded_string2 = base64.b64encode(image_file.read())

base64_string1 =encoded_string1.decode(ENCODING)
base64_string2 = encoded_string2.decode(ENCODING)

payload = {
  'image1': base64_string1,
  'image2': base64_string2
}

jsonData = json.dumps(payload)

response = requests.request("POST", matchurl, data=jsonData, headers=headers)

print(response.text)