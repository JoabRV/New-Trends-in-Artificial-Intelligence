# Importamos las librerías necesarias
import pyttsx3
import speech_recognition as sr

# Función para que el asistente hable
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Función para que el asistente escuche
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Dime, ¿cómo te sientes el día de hoy?")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language="es-MX")
            print("Usuario: ", text)
            return text.lower()
        except:
            speak("Lo siento, no he entendido. ¿Podrías repetirlo?")
            return ""

# Función para procesar el texto de entrada y generar una respuesta
def responder(texto):
    # Convertimos el texto a minúsculas para facilitar el procesamiento
    texto = texto.lower()

    # Identificamos las palabras clave en el texto de entrada
    if "triste" in texto:
        return "Lamento que te sientas así. ¿Puedes contarme más sobre lo que te está haciendo sentir triste?"
    elif "ansioso" in texto:
        return "Entiendo que te sientas ansioso. ¿Hay algo en particular que esté causando tu ansiedad?"
    elif "enojado" in texto:
        return "Me preocupa que te sientas enojado. ¿Puedes explicarme qué te está molestando?"
    elif "feliz" in texto:
        return "Me alegra que te sientas feliz. ¿Hay algo en particular que te esté haciendo sentir así?"
    elif "preocupado" in texto:
        return "Comprendo que te sientas preocupado. ¿Puedes decirme más sobre lo que te está preocupando?"
    elif "salir" in texto:
        speak("¡Hasta pronto!")
        return "salir"
    else:
        return "Entiendo que tengas sentimientos complejos. ¿Puedes profundizar más en cómo te estás sintiendo?"

# Función principal del asistente virtual de psicología
def psicologo_virtual():
    speak("Hola, soy tu psicólogo virtual. ¿Cómo te sientes el día de hoy?")

    # Pedimos al usuario que ingrese su mensaje y le respondemos
    while True:
        texto = listen()

        # Llamamos a la función responder para generar una respuesta
        respuesta = responder(texto)

        # Verificamos si el usuario quiere salir del programa
        if respuesta == "salir":
            break

        # Si no quiere salir, le respondemos al usuario
        speak(respuesta)

# Llamamos a la función principal del asistente virtual de psicología
psicologo_virtual()