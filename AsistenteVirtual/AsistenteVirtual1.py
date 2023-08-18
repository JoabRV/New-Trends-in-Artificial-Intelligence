import speech_recognition as sr
import pyttsx3
import datetime

# Configuración del reconocimiento de voz
r = sr.Recognizer()
mic = sr.Microphone()
# Configuración de la síntesis de voz
engine = pyttsx3.init()


# Función para que el asistente responda en voz alta
def speak(text):
    engine.say(text)
    engine.runAndWait()


# Función para que el asistente salude al usuario
def greet():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    if current_time < "12:00:00":
        speak("¡Buenos días!")
    elif "12:00:00" <= current_time < "18:00:00":
        speak("¡Buenas tardes!")
    else:
        speak("¡Buenas noches!")


# Función para que el asistente escuche y procese los comandos de voz
# CÓDIGO DE UN ASISTENTE VIRTUAL
def listen():
    with mic as source:
        print("Escuchando...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio, language="es-ES")
        print(f"Has dicho: {command}")
        return command
    except sr.UnknownValueError:
        print("Lo siento, no he entendido lo que has dicho.")
        return ""
    except sr.RequestError as e:
        print(f"No se pudo procesar la solicitud: {e}")
        return ""


# Función principal para ejecutar el asistente virtual
def run():
    greet()
    while True:
        command = listen()
        if "hola" in command.lower():
            speak("¡Hola! ¿En qué puedo ayudarte?")
        elif "adiós" in command.lower():
            speak("¡Adiós!")
            break
    else:
        speak("Lo siento, no entiendo ese comando.")


# CÓDIGO DE UN ASISTENTE VIRTUAL
if __name__ == "__main__":
    run()