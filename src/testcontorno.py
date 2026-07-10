import cv2 
import numpy as np

#o zero significa o numero da sua webcan, caso voce tivesse mais que uma colocaria outro valor
cap = cv2.VideoCapture(0) #carregando uma imagem de video da webcam

while True:
    #o ret é responsavel para saber se sua camera esta disponivel para ser utilizada
    ret, frame = cap.read(); #forma que nossa imagem vai ser apresentada(frame)
    width = int(cap.get(3))
    height = int(cap.get(4))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #pegará os valores de pixel BGR e os converterá em matiz, saturação e luminosidade
    lower_blue = np.array([90, 50, 50]) #valores minimos de azul que voce deseja detectar
    upper_blue = np.array([130, 255, 255]) #valores maximos de azul que voce deseja detectar

    mask = cv2.inRange(hsv, lower_blue, upper_blue) #mascara responsavel por detectar o que é azul na imagem

    #aplicando a mascara na nossa imagem original, de forma que apareça apenas os pixels azuis e o restante dos pixels sejam escurecidos (transformado em um pixel preto)
    result = cv2.bitwise_and(frame, frame, mask = mask) #compara pixel a pixel se é encontrado a cor azul (definida na mascara) - retorna 1 se encontrar e 0 caso não encontrar

    
    cv2.imshow('frame', result)

    if cv2.waitKey(1) == ord('q'): #se o 'q' for pressionado sai da janela
        break

cap.release() #libera o recurso da camera
cv2.destroyAllWindows() #desativando a webcam