"""
__autor__ : 
__date__ :
__teammates__ :
description
"""
import face_recognition
import numpy as np
import json
import cv2
class face_rec :
    """
    description of class
    """
    def __init__(self, config_path):
        """
        this is the class constractor
        @param1 :
        @type :
        @param 2 :
        @type :
        @return :
        """
        config_file = open(config_path,'r')
        config = json.load(config_file)
        self.known_faces_names = []
        self.known_faces_encodings = []
        for name in config :
            self.known_faces_names.append(name)
            self.known_faces_encodings.append(self.face_encode(name, config[name]))
    def face_encode(self, name, image):
        '''
        '''
        im = face_recognition.load_image_file(image)
        encoding = face_recognition.face_encodings(im)[0]
        return encoding

    def face_rec(self, frame):
        '''
        '''
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)
        face_names = []
        for face_encoding in face_encodings :
            matches = face_recognition.compare_faces(self.known_faces_encodings,face_encoding)
            name = "unknown"
            for i in range (len(matches)) :
                if matches[i]:
                    name = self.known_faces_names[i]
                face_names.append(name)
            return face_names

face = face_rec('/home/imed/Desktop/work/RobotAssistant/config/face_config.json')
cam = cv2.VideoCapture(2)
while True :
    ret, frame = cam.read()
    names = face.face_rec(frame)
    print("i see :",names)
    
