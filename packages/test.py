
from facerec import *
from threading import Thread

class main :
    def __init__(self):
        self.face = face_rec("../config/face_config.json")
        self.cam = cv2.VideoCapture(0)
    def Main(self):
        while True :
            ret, frame = self.cam.read()
            names = self.face.face_rec(frame)
            print("i see :", names)
    def add_user(self, image, nom):
        self.face.face_to_file(image, nom)
main = main()
face_thread = Thread(target=main.Main)
face_thread.start()
while True :
    image_path = input("donner le path de l'image :\n")
    nom = input("donner le nom :\n")
    main.add_user(image_path, nom)

