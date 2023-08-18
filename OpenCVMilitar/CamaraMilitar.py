import cv2
# Obtener la referencia a la cámara
cap = cv2.VideoCapture(0)
while True:
 # Leer un fotograma de la cámara
 ret, frame = cap.read()
 # Mostrar el fotograma en una ventana
 cv2.imshow('Camara', frame)
 # Esperar a que se presione la tecla 'q' para salir
 if cv2.waitKey(1) & 0xFF == ord('q'):
  break
# Liberar la cámara y cerrar la ventana
cap.release()
cv2.destroyAllWindows()
