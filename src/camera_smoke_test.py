import numpy as np
import cv2 as cv
# Carrega um video pelo caminho especificado
cap = cv.VideoCapture('/home/lucas/Estudos/Vault_Obsidian/04_Entregaveis/BulbaTech/media/pratica4_ex1_LUCASALMEIDADESOUZA_SIMULACAO(1).mp4')

# Checa se o vídeo foi aberto corretamente
if not cap.isOpened():
    print("Erro ao abrir o vídeo")
    exit()
while True:
    #ret retorna um booleano indicando se o quadro foi lido corretamente e o quadro em si
    ret, frame = cap.read()
    # Converte de float para int, para o slicing funcionar corretamente
    width=int(cap.get(3))
    height=int(cap.get(4))
    image = np.zeros(frame.shape, np.uint8)
    frame_reduzido=cv.resize(frame,(0,0), fx=0.5, fy=0.5)
    # 1/4 da imagem preenchida, 2º quadrante da imagem.
    image[:height//2,:width//2]=frame_reduzido
    # 1/4 da imagem preenchida, 3º quadrante da imagem.
    image[height//2:,:width//2]=frame_reduzido
    # 1/4 da imagem preenchida, 4º quadrante da imagem.
    image[height//2:,width//2:]=frame_reduzido
    # 1/4 da imagem preenchida, 1º quadrante da imagem.
    image[:height//2,width//2:]=frame_reduzido
    if not ret:
        print("Erro ao capturar o quadro")
        break
    cv.imshow('Video', image)
    # ord retorna o valor ASCII do caractere 'q' e cv.waitKey(1) espera 1 milissegundo para capturar a tecla pressionada
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
# Libera o objeto de captura e fecha todas as janelas
# Libera o recurso para que outros programas possam utilizá-lo
cap.release()
cv.destroyAllWindows()
