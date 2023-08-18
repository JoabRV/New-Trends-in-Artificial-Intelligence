import cv2

# Función para capturar y mostrar el video de la cámara
def mostrar_video_camara():
    # Crear un objeto VideoCapture para acceder a la cámara web (0 es el índice de la cámara predeterminada)
    cap = cv2.VideoCapture(0)

    while True:
        # Leer un cuadro del video de la cámara
        ret, frame = cap.read()

        # Mostrar el cuadro en una ventana llamada "Video de la cámara"
        cv2.imshow('Video de la cámara', frame)

        # Esperar 1 milisegundo y revisar si se ha presionado la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Liberar el objeto VideoCapture y cerrar todas las ventanas
    cap.release()
    cv2.destroyAllWindows()

# Llamar a la función para abrir la cámara web
mostrar_video_camara()
