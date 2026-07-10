"""
Para mascarar videos em tempo real e "detectar cores"
As funções mais importantes são cv.inRange para criar
mascára por cor. E a operação bitwise_and, de modo a 
marcar apenas a sobreposição com a máscara.
"""
import cv2 as cv
import numpy as np

camera = cv.VideoCapture(0)

while camera.isOpened():
    ret, frame = camera.read()
    if not ret:
        print("Não é possível mostra o vídeo")
        break
    frame_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    azul_claro = np.array([80,50,50])
    azul_escuro = np.array([140,255,255])
    mask = cv.inRange(frame_hsv, azul_claro, azul_escuro)
    frame_masked = cv.bitwise_and(frame,frame, mask=mask)
    cv.imshow('Video Original', frame)
    cv.imshow('Mascara azul', mask)
    cv.imshow('Mascara aplicada', frame_masked)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
camera.release()
cv.destroyAllWindows()