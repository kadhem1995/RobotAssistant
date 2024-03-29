"""
__autor__ : It was written by anaibia kadhem and mlawh imed
__date__ : 01/05/2020
__teammates__ : no team
description : This class contains code that enables us to identify and differentiate faces and store them in a json file
"""

import face_recognition
import numpy as np
import codecs, json
import cv2

class face_rec :
    """
    description : This method compares the new face code with the old face
    code so that it recognizes the face if it is present in the json file
    and the name of the face owner is printed
    """
    def __init__(self, config_path):
        """
        this is the class constractor
        @param1 : self
        @type : 
        @param 2 : confing_path
        @type : json file
        @return : String "name for encoding_face"
        """
        config_file = open(config_path,'r')
        config = json.load(config_file)
        self.known_faces_names = []
        self.known_faces_encodings = []
        f = open("encoding.json",'r')
        self.data = json.load(f)
        f.close()
        for name in self.data.keys():
            self.known_faces_encodings.append(np.asarray(self.data[name]))
            self.known_faces_names.append(name)
    def face_to_file(self, image_path, nom):
        ''' 
        description : This method stores new face codes in the json file
        '''
        images = face_recognition.load_image_file(image_path) 
        image_encoding = face_recognition.face_encodings(images)[0]
        print(image_encoding)
        self.data[nom] = image_encoding.tolist()
        self.known_faces_encodings.append(np.asarray(self.data[name]))
        self.known_faces_names.append(name)
        f = open("encoding.json",'w')
        json.dump(self.data,f)
        f.close()
    def face_encode(self, name, image):
        '''
        description : This method gives us a face code for each previously
        entered image
        '''
        im = face_recognition.load_image_file(image)
        encoding = face_recognition.face_encodings(im)[0]
        return encoding

    def face_rec(self, frame):
        '''
        description : This method determines the face or faces that the camera
        captures through video, and the method tells us whether or not it
        recognized the face.
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
