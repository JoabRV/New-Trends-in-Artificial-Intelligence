import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib
import requests
import json
import re
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
# Descargar los datos necesarios para NLTK
nltk.download('punkt')
# Configuración del reconocimiento de voz
r = sr.Recognizer()
mic = sr.Microphone()
# CÓDIGO DE UN ASISTENTE VIRTUAL
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
def listen():
 with mic as source:
  print("Escuchando...")
  r.adjust_for_ambient_noise(source)
  audio = r.listen(source)
 try:
  command = r.recognize_google(audio, language="es-ES")
  print(f"Has dicho: {command}")
  return command
# CÓDIGO DE UN ASISTENTE VIRTUAL
 except sr.UnknownValueError:
  print("Lo siento, no he entendido lo que has dicho.")
  return ""
 except sr.RequestError as e:
  print(f"No se pudo procesar la solicitud: {e}")
  return ""
# Función para enviar correos electrónicos
def send_email(recipient, subject, body):
 server = smtplib.SMTP('smtp.gmail.com', 587)
 server.starttls()
 server.login('tu_correo@gmail.com', 'tu_contraseña')
 message = f'Subject: {subject}\n\n{body}'
 server.sendmail('tu_correo@gmail.com', recipient, message)
 server.quit()
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
  elif "wikipedia" in command.lower():
    speak("Buscando en Wikipedia...")
    search = re.search('wikipedia (.+)', command.lower())
  elif "abrir" in command.lower():
    search = re.search('abrir (.+)', command.lower())
    if search:
      query = search.group(1)
      if "google" in query:
        webbrowser.open("https://www.google.com")
# CÓDIGO DE UN ASISTENTE VIRTUAL
 if search:
  query = search.group(1)
  try:
    results = wikipedia.summary(query, sentences=2)
    speak("Según Wikipedia...")
    speak(results)
  except wikipedia.exceptions.DisambiguationError as e:
    speak("Lo siento, hay múltiples opciones para esta búsqueda. Por favor, sé más específico.")
 else:
  speak("Lo siento, no he entendido lo que has dicho.")
