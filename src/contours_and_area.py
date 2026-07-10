import cv2 as cv
import numpy as np

captura = cv.VideoCapture(0)

if not captura.isOpened():
    exit()

while True:
    ret, frame = captura.read()
    if not ret:
        break
    # --------------------------------------ESPACO DE COR CINZA---------------------------------------#
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # -------------------------------------CONTORNO---------------------------------------#
    ret, thresh = cv.threshold(gray_frame, 125, 175, 0)
    contours, hierarchies = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    # blank_slate = np.zeros(frame.shape[:2], dtype='uint8')
    # contornos_desenhados = cv.drawContours(blank_slate, contours, -1, (255,255,255), 2)
    # -------------------------------------
    for i, cnt in enumerate(contours):
        area = cv.contourArea(cnt)
        perimeter = cv.arcLength(cnt, True)
        cv.drawContours(frame, [cnt], -1, (255,255,255), 2)
        cv.imshow("Frame com contornos", frame)
        if area < 1000:
            x,y,w,h = cv.boundingRect(cnt)
            retangulo = frame.copy()
            cv.rectangle(retangulo,(x,y),(x+w,y+h),(0,255,0),2)
            cv.imshow("Retangulo", retangulo)
    # Masking with color
    #highlight = np.ones_like(frame)
    #cv.drawContours(highlight, contours, -1, (0, 200, 175), cv.FILLED)
    #cv.imshow("Masking with color", highlight)
    # Masking for extraction
    #mask = np.zeros_like(frame)
    #cv.drawContours(mask, contours, -1, (255, 255, 255), cv.FILLED)
    #foreground = cv.bitwise_and(frame, mask)
    #cv.imshow("Mascara para extração", foreground)

    # cv.imshow('Frame original', frame)
    # cv.imshow('Contornos desenhados', blank_slate)
    # x, y, w, h = cv.boundingRect(contours)
    # print(x,y,w,h)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
captura.release()
cv.destroyAllWindows()