import cv2
# Cargar la imagen
img = cv2.imread('imagen_danada.png')
# Convertir la imagen a escala de grises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Aplicar umbralización para obtener una imagen binaria
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
# Encontrar los contornos de los objetos en la imagen
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL,
cv2.CHAIN_APPROX_SIMPLE)
# Dibujar los contornos en la imagen original
cv2.drawContours(img, contours, -1, (0, 0, 255), 2)
# Mostrar la imagen resultante
cv2.imshow('Imagen danada', img)
cv2.waitKey(0)
cv2.destroyAllWindows()