import time
import cv2
import numpy as np
import dlib
import keyboard


def Viola_Jones(frame):
    vjframe = frame.copy()
    coord = []
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(frame, 1.1, 5, minSize=(30, 30), maxSize=(220, 220))
    for (x, y, w, h) in faces:
        cv2.rectangle(vjframe, (x, y), (x+w, y+h), (255, 0, 0), 2)
        coord.append((x, y, x+w, y+h))
    cv2.imshow("VJ", vjframe)   
    cut_face(frame, coord,"VJ")

    return vjframe

def hog_face(frame):
    hogf = frame.copy()
    coord = []   
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    boxes, weights = hog.detectMultiScale(hogf, winStride=(8, 8), padding=(8, 8), scale=1.05, useMeanshiftGrouping=False)
    for (x, y, w, h) in boxes:
        cv2.rectangle(hogf, (x, y), (x+w, y+h), (0, 255, 0), 2)
        coord.append((x, y, x+w, y+h))
    cv2.imshow("HOG", hogf)
    cut_face(frame, coord,"HOG")
    return hogf




def hog_face_dlib(frame):
    hogf = frame.copy()
    coord = []
    faces = detector(hogf, 1)
    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()
        coord.append((x1, y1, x2, y2))
        cv2.rectangle(hogf, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.imshow("HOG DLIB", hogf)
    cut_face(frame, coord,"HOG DLIB")
    return hogf
# 

def cut_face(frame, coord,name: str):
    
    try:
        x1= max(coord[0][0], 0)
        x2= min(coord[0][2], frame.shape[1])
        y1= max(coord[0][1], 0)
        y2= min(coord[0][3], frame.shape[0])

        cut = frame[y1:y2, x1:x2]
        if cut is not None and cut.shape[0] > 0 and cut.shape[1] > 0:
            
            cv2.imshow(name +"Cut", cut)
        else:
            print("No se detectó ningún rostro para recortar. "+name)
    except IndexError or AssertionError or Exception:

        print("No se detectó ningún rostro para recortar. "+name)
        pass


def threshold(frame):
    thresh1 = cv2.threshold(frame, 10, 255, cv2.THRESH_BINARY_INV)[1]
    thresh2 = cv2.threshold(frame, 20, 255, cv2.THRESH_BINARY_INV)[1]
    thresh3 = cv2.threshold(frame, 40, 255, cv2.THRESH_BINARY_INV)[1]

    cv2.imshow("T1", thresh1)
    cv2.imshow("T2", thresh2)
    cv2.imshow("T3", thresh3)

    return thresh1, thresh2, thresh3

def gray(frame):
    frame = cv2.resize(frame, (300, 300))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (3, 3), 0)
    for i, text in enumerate(texto_fps):
        cv2.putText(frame, text, (10, 20 + i * 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
    cv2.imshow("cara", frame)
    cv2.imshow("Gray", gray)
    
    return gray



#####################################################################################################



#video = cv2.VideoCapture("C:/Users/migue/Documents/ProyectosPython/pruebasVgame/videos/v1.mp4")
video = cv2.VideoCapture("videos/video1.mp4")
#video = cv2.VideoCapture(0) 
if not video.isOpened():
    print("Error: No se pudo abrir el archivo de video.")
    exit()

#inicializa el detector de rostros de dlib
detector = dlib.get_frontal_face_detector()

# Variables para medir el tiempo
contador_frames = 0
suma_tiempos = 0.0
tiempo_actual = 0.0
tiempo_min = float('inf')
tiempo_max = 0.0
tiempo_avg = 0.0
tiempo_anterior = 0
texto_fps = []

while True:
    texto_fps = [
        f"Actual: {tiempo_actual:.4f}s",
        f"Min:    {tiempo_min:.4f}s",
        f"Max:    {tiempo_max:.4f}s",
        f"Avg:    {tiempo_avg:.4f}s"
    ]
    
    inicio = round(time.time(), 4)
    ret, frame = video.read()
    key = cv2.waitKey(30) 
    if key == 27 or ret is False:
        break
    
    

    gray1 = gray(frame)
    vj1 = Viola_Jones(gray1)
    hog = hog_face_dlib(gray1)
    tiempo_actual = round(time.time() - inicio, 4)
    
    
    if contador_frames >= 1:
        
        suma_tiempos += tiempo_actual
        if tiempo_actual < tiempo_min:
            tiempo_min = tiempo_actual
        if tiempo_actual > tiempo_max:
            tiempo_max = tiempo_actual
        
        tiempo_avg = suma_tiempos / contador_frames
    contador_frames += 1
    
    #t1,t2,t3 = threshold(gray1)
    

print(contador_frames)
cv2.destroyAllWindows()