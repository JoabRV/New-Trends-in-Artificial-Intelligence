# Importamos la librería para interactuar con el usuario
import pyttsx3
import speech_recognition as sr

# Definimos la función para que el asistente hable
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Definimos la función para que el asistente escuche
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Dime, ¿en qué puedo ayudarte?")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language="es-MX")
            print("Usuario: ", text)
            return text.lower()
        except:
            speak("Lo siento, no he entendido. ¿Podrías repetirlo?")
            return ""

# Definimos una función para calcular el índice de masa corporal (IMC)
def calcular_imc(peso, estatura):
    estatura_m = estatura / 100
    imc = peso / (estatura_m ** 2)
    return imc

# Definimos la función principal del asistente virtual
def nutriologo_virtual():
    speak("¡Hola! Soy tu asistente virtual de nutrición. ¿En qué puedo ayudarte?")
    while True:
        texto = listen()
        if "salir" in texto:
            speak("¡Hasta pronto!")
            break
        elif "calcula el índice de masa corporal" in texto:
            speak("Por favor, dime tu peso en kilogramos.")
            peso = float(listen())
            speak("Ahora dime tu estatura en centímetros.")
            estatura = float(listen())
            imc = calcular_imc(peso, estatura)
            if imc < 18.5:
                speak("Tu IMC es de {:.1f}, lo que indica que tienes bajo peso. Te recomiendo que consultes con un especialista para recibir la atención adecuada.".format(imc))
            elif imc >= 18.5 and imc < 25:
                speak("Tu IMC es de {:.1f}, lo que indica que tienes un peso saludable. ¡Sigue así!".format(imc))
            elif imc >= 25 and imc < 30:
                speak("Tu IMC es de {:.1f}, lo que indica que tienes sobrepeso. Te recomiendo que hagas cambios en tu estilo de vida, como mejorar tu alimentación y hacer ejercicio regularmente.".format(imc))
            else:
                speak("Tu IMC es de {:.1f}, lo que indica que tienes obesidad. Te recomiendo que consultes con un especialista para recibir la atención adecuada.".format(imc))
        else:
            speak("Lo siento, no entiendo lo que quieres decir. ¿Podrías repetirlo?")

# Llamamos a la función principal del asistente virtual
nutriologo_virtual()