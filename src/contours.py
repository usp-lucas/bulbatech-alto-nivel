import cv2 as cv
import numpy as np

captura = cv.VideoCapture(0)

if not captura.isOpened():
    print("Operação mal-sucedida ou fim do vídeo")
    exit()
while True:
    ret, frame = captura.read()
    cv.imshow("Webcam", frame)
    if not ret:
        break
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    gray_frame_blurred = cv.GaussianBlur(gray_frame, [3,3], cv.BORDER_DEFAULT)
    canny_blurred_gray = cv.Canny(gray_frame_blurred, 125, 185)
    contours, hierarchies = cv.findContours(canny_blurred_gray, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
    blank_slate = np.zeros(frame.shape[:2], dtype='uint8')
    cv.drawContours(blank_slate, contours, -1, (255,255,255), 2)
    cv.imshow('Contours Drawn', blank_slate)
    '''cv.imshow("Gray Frame", frame_gray)
    cv.imshow("Gray Frame Blurred(Gaussian)", gray_frame_blurred)
    canny = cv.Canny(frame, 125, 175)
    cv.imshow("Canny Edges", canny)
    canny_gray = cv.Canny(frame_gray, 125, 175)
    cv.imshow("Canny Edges Gray Frame", canny_gray)
    cv.imshow("Canny Edges Blurred Gray Frame", canny_blurred_gray)'''
    '''    ret, thresh = cv.threshold(frame_gray, 125, 255, cv.THRESH_BINARY)
    cv.imshow('Threshholded', thresh)'''
    if cv.waitKey(1) & 0xFF == ord('q'):
        print('Saindo do loop de captura')
        break
captura.release()
cv.destroyAllWindows()
