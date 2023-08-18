import numpy as np

# Definir las entradas y salidas
entradas = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
salidas = np.array([1, 0, 0, 1])

# Asignar valores aleatorios al bias
np.random.seed(1)
bias = 2 * np.random.random() - 1

# Inicializar los pesos aleatoriamente
pesos = 2 * np.random.random((2,)) - 1

# Definir la función de activación tangente hiperbólica
def activacion(x):
    return np.tanh(x)

# Entrenar el perceptrón
num_epocas = 10000
tasa_aprendizaje = 0.1
for epoca in range(num_epocas):
    for i in range(len(entradas)):
        suma_ponderada = np.dot(entradas[i], pesos) + bias
        salida = activacion(suma_ponderada)
        error = salidas[i] - salida
        pesos += tasa_aprendizaje * error * entradas[i]
        bias += tasa_aprendizaje * error

# Probar el perceptrón
for i in range(len(entradas)):
    suma_ponderada = np.dot(entradas[i], pesos) + bias
    salida = activacion(suma_ponderada)
    print("Entrada:", entradas[i], "Salida deseada:", salidas[i], "Salida obtenida:", round(salida))