''' 
Importación de las librerías 
(Leer readme para la instalación de los módulos necesarios)
'''
import speech_recognition as sr
from calculator import Calculator as cal
import pyttsx3

# Iniciación de los módulos a utilizar
listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(op, n1, n2, res):
    engine.say(
                f"el resultado de la {op} de {n1} y {n2} es {res}"
            )
    engine.runAndWait()

try:
    with sr.Microphone() as source:
        listener.adjust_for_ambient_noise(source)
        print('Recording...')
        voice = listener.listen(source)
        rec = listener.recognize_google(voice, language="es-MX")
        rec_str = str(rec)
        arr = rec.split(" ")
        if ("+" in arr or "más" in arr):
            op = "suma"
            res = cal.sumar(cal.num(arr[0]), cal.num(arr[2]))
            talk(op, arr[0], arr[2], res)
            engine.runAndWait()
        elif ("menos" in arr):
            op = "resta"
            res = cal.restar(cal.num(arr[0]), cal.num(arr[2]))
            talk(op, arr[0], arr[2], res)
        elif ("por" in arr):
            op = "multiplicación"
            res = cal.multiplicar(cal.num(arr[0]), cal.num(arr[2]))
            talk(op, arr[0], arr[2], res)
        elif ("entre" in arr or "dividido" in arr):
            op = "división"
            res = cal.dividir(cal.num(arr[0]), cal.num(arr[2]))
            talk(op, arr[0], arr[2], res)
        else:
            engine.say("Lo siento, no logro reconocer lo que dices")
            engine.runAndWait()
except:
    engine.say("Lo siento, no logro reconocer lo que dices")
    engine.runAndWait()