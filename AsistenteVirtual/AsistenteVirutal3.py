import imaplib
import email
from imaplib import IMAP4_SSL

import pyttsx3
# Configuración del servidor de correo IMAP
mail = imaplib.IMAP4_SSL('imap.outlook.com')
mail.login('Elgallodeoro777@outlook.es', 'Elmeromero123')
mail.select('inbox')
# Configuración de la síntesis de voz
engine = pyttsx3.init()
# Función para que el asistente responda en voz alta
def speak(text):
 engine.say(text)
 engine.runAndWait()
# Función para leer los mensajes de correo electrónico
def read_emails():
 result, data = mail.uid('search', None, 'ALL')
 if result == 'OK':
     for uid in data[0].split():
        result, email_data = mail.uid('fetch', uid, '(RFC822)')
        raw_email = email_data[0][1]
        email_message = email.message_from_bytes(raw_email)
        speak(f"De: {email_message['From']}")
        speak(f"Asunto: {email_message['Subject']}")
        speak(f"Cuerpo: {email_message.get_payload()}")
# Función principal para ejecutar el asistente virtual
def run():
 speak("Leyendo correos electrónicos...")
 read_emails()
 speak("Fin de la lectura de correos electrónicos.")
 mail.close()
 mail.logout()
# Ejecutar el asistente virtual
run()