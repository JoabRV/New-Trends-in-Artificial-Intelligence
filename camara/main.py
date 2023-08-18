import cv2
import time

def mostrar_video(camara):
    while True:
        # Capturar un frame de la cámara
        ret, frame = camara.read()

        # Mostrar el frame en una ventana
        cv2.imshow('Camara', frame)

        # Esperar 1 milisegundo y verificar si se presionó la tecla 'q' para salir
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

def tomar_foto(nombre_archivo):
    # Inicializar la cámara
    camara = cv2.VideoCapture(0)

    # Verificar si la cámara se ha abierto correctamente
    if not camara.isOpened():
        print("No se pudo abrir la cámara.")
        return

    # Mostrar el video en tiempo real durante 5 segundos
    print("Mostrando video en tiempo real. Tienes 5 segundos para ajustar la posición.")
    tiempo_inicial = time.time()
    while time.time() - tiempo_inicial < 5:
        mostrar_video(camara)

    # Tomar una foto
    ret, imagen = camara.read()

    # Verificar si se pudo tomar la foto correctamente
    if not ret:
        print("No se pudo tomar la foto.")
        return

    # Guardar la foto en un archivo
    cv2.imwrite(nombre_archivo, imagen)

    # Cerrar la ventana de visualización
    cv2.destroyWindow('Camara')

    # Cerrar la cámara
    camara.release()

if __name__ == '__main__':
    # Nombre del archivo de la foto
    nombre_archivo = "foto.jpg"

    # Tomar la foto y guardarla
    tomar_foto(nombre_archivo)

