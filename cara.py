import time
import cv2
import numpy as np
import dlib
import keyboard

def Viola_Jones(frame):
    vgframe = frame.copy()
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(frame, 1.1, 5, minSize=(30, 30), maxSize=(180, 180))
    for (x, y, w, h) in faces:
        cv2.rectangle(vgframe, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow("VJ", vgframe)    
    return vgframe

def hog_face(frame):
    hogf = frame.copy()   
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    boxes, weights = hog.detectMultiScale(hogf, winStride=(8, 8), padding=(8, 8), scale=1.05, useMeanshiftGrouping=False)
    for (x, y, w, h) in boxes:
        cv2.rectangle(hogf, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow("HOG", hogf)
    return hogf
  

def gray(frame):
    frame = cv2.resize(frame, (300, 300))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (3, 3), 0)
    cv2.putText(frame, texto_fps, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    cv2.imshow("cara", frame)
    cv2.imshow("Gray", gray)
    
    return gray

def threshold(frame):
    thresh1 = cv2.threshold(frame, 10, 255, cv2.THRESH_BINARY_INV)[1]
    thresh2 = cv2.threshold(frame, 20, 255, cv2.THRESH_BINARY_INV)[1]
    thresh3 = cv2.threshold(frame, 40, 255, cv2.THRESH_BINARY_INV)[1]

    cv2.imshow("T1", thresh1)
    cv2.imshow("T2", thresh2)
    cv2.imshow("T3", thresh3)

    return thresh1, thresh2, thresh3

#####################################################################################################


#video = cv2.VideoCapture("C:/Users/migue/Documents/ProyectosPython/pruebasVgame/videos/v1.mp4")
#video = cv2.VideoCapture("videos/v5.mp4")
video = cv2.VideoCapture(0) 
if not video.isOpened():
    print("Error: No se pudo abrir el archivo de video.")
    exit()


tiempo_anterior = 0
while True: 
    ret, frame = video.read()
    key = cv2.waitKey(30) 
    if key == 27 or ret is False:
        break
    tiempo_actual = time.time()
    fps = 1 / (tiempo_actual - tiempo_anterior)
    tiempo_anterior = tiempo_actual

    # Convertir los FPS a entero para mostrarlos visualmente
    texto_fps = f"FPS: {int(fps)}"

    gray1 = gray(frame)
    vj1 = Viola_Jones(gray1)
    hog = hog_face(gray1)

    #t1,t2,t3 = threshold(gray1)
    


cv2.destroyAllWindows()