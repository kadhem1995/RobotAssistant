
from facerec import *
face = face_rec('/home/imed/Desktop/work/RobotAssistant/config/face_config.json')
cam = cv2.VideoCapture(2)
while True :
    ret, frame = cam.read()
    names = face.face_rec(frame)
    print("i see :", names)