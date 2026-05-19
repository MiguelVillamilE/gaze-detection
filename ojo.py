import cv2


path = 'C:/Users/migue/Documents/ProyectosPython/pruebasVgame/image.png'

frame = cv2.imread(path)
if frame is None:
    print("Error: null.")
else:
    cv2.namedWindow('Pupila', cv2.WINDOW_NORMAL) 
    cv2.imshow('Pupila', frame)
    #cv2.resizeWindow('Pupila', 800, 600)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

"""import cv2
import numpy as np


path = 'C:/Users/migue/Documents/ProyectosPython/pruebasVgame/ojos.jpg'

frame = cv2.imread(path)
if frame is None:
    print("Error: null.")
"""

"""
else:
    cv2.imshow('Pupila', frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Umbralización para detectar la pupila (más oscura)
_, thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY_INV)

# Encontrar contornos
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Seleccionar el mayor contorno y dibujar
if contours:
    cnt = max(contours, key=cv2.contourArea)
    cv2.drawContours(frame, [cnt], -1, (0, 255, 0), 2)

cv2.imshow('Pupila', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()"""