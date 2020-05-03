import face_recognition
import numpy as np 

import codecs, json

image = face_recognition.load_image_file("kadhem.jpg")
kadhem_encoding = face_recognition.face_encodings(image)[0]
image = face_recognition.load_image_file("imed.jpg")
imed_encoding = face_recognition.face_encodings(image)[0]

print(kadhem_encoding)
data = {}
data["kadhem"] = kadhem_encoding.tolist()
#data["imed"] = imed_encoding.tolist()
f = open("encoding.json",'w')
json.dump(data,f)
