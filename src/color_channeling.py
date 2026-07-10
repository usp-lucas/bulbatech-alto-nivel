import cv2 as cv
import numpy as np

capture = cv.VideoCapture(0)
if not capture.isOpened():
   print("Falha ao carregar o vídeo")
   exit()
while True:
   ret, frame = capture.read()
   b,g,r = cv.split(frame)
   blank_slate = np.zeros(frame.shape[:2], dtype='uint8')
   frame_azul = cv.merge([b,blank_slate,blank_slate])
   frame_verde = cv.merge([blank_slate, g ,blank_slate])
   frame_vermelho = cv.merge([blank_slate, blank_slate, r])
   cv.imshow('Canal Azul', frame_azul)
   cv.imshow('Canal Verde', frame_verde)
   cv.imshow('Canal Vermelho', frame_vermelho)
   if cv.waitKey(1) & 0xFF == ord('q'):
      break
capture.release()
cv.destroyAllWindows()   