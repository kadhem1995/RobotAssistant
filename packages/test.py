
from facerec import *
face = face_rec("/home/pi/Desktop/RobotAssistant/config/face_config.json")
cam = cv2.VideoCapture("http://192.168.1.104:8080/video/mjpeg")
while True :
    ret, frame = cam.read()
    names = face.face_rec(frame)
    print("i see :", names)
