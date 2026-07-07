import cv2 as cv
# Cria um objeto de captura de vídeo para a câmera padrão (índice 0)
capture = cv.VideoCapture(0)
# Checa se a câmera foi aberta corretamente
if not capture.isOpened():
    print("Erro ao abrir a câmera")
    exit()
#Leia e mostre os quadros da câmera em um loop
while True: 
    # Armazena a tupla de retorno e frames da câmera
    ret, frame = capture.read()
    if not ret:
        print("Erro ao capturar o quadro")
        break
    # Mostra o quadro capturado em uma janela
    cv.imshow('Camera', frame)
    # Pressione 'q' para sair do loop
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
# Libera o objeto de captura e fecha todas as janelas
capture.release()
cv.destroyAllWindows()