import cv2
import numpy as np

# Crear una matriz de 4x4 con valores binarios (0 y 1)
image_matrix = np.array([[0, 1, 0, 1, 0],
                         [1, 0, 1, 0, 1],
                         [0, 1, 0, 1, 0],
                         [1, 0, 1, 0, 1],
                         [0, 1, 0, 1, 0]], dtype=np.uint8)


# Escalar los valores binarios para que sean legibles como una imagen
scaled_image_matrix = image_matrix * 255

# Crear la imagen a partir de la matriz
image = cv2.cvtColor(scaled_image_matrix, cv2.COLOR_GRAY2BGR)

# Mostrar la imagen
cv2.imshow("Image", image)
cv2.waitKey(0)
# cv2.destroyAllWindows()

# Crear una matriz de 4x4 con valores binarios (0 y 1)
image_matrix2 = np.array([[1, 1, 0, 1, 0],
                          [1, 0, 1, 0, 1],
                          [0, 1, 0, 1, 0],
                          [1, 0, 1, 0, 1],
                          [0, 1, 0, 1, 0]], dtype=np.uint8)


# Escalar los valores binarios para que sean legibles como una imagen
scaled_image_matrix2 = image_matrix2 * 255

# Crear la imagen a partir de la matriz
image2 = cv2.cvtColor(scaled_image_matrix2, cv2.COLOR_GRAY2BGR)

# Mostrar la imagen
cv2.imshow("Image2", image2)
cv2.waitKey(0)
cv2.destroyAllWindows()