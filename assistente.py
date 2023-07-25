# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import speech_recognition as sr
import pyttsx3

def ouvir_microfone():
    recognizer = sr.Recognizer()
    microphone_active = True

    with sr.Microphone() as source:
        print("Diga algo...")
        recognizer.adjust_for_ambient_noise(source, duration=1.0)  # Aumenta o tempo de calibração para 1 segundo

        while microphone_active:
            try:
                audio = recognizer.listen(source, timeout=10)  # Definindo um tempo limite de 10 segundos para aguardar a resposta
                texto = recognizer.recognize_google(audio, language="pt-BR").lower()

                if "help" in texto:
                    print("Você disse: " + texto)
                    responder("Claro! Como posso ajudar?")
                    microphone_active = False

                print("Você disse: " + texto)

            except sr.UnknownValueError:
                print("Não entendi o que você disse.")
                responder("Não entendi o que você disse.")
            except sr.RequestError as e:
                print("Erro ao se comunicar com o serviço de reconhecimento de fala; {0}".format(e))
                responder("Desculpe, ocorreu um erro no serviço de reconhecimento de fala.")

def responder(fala):
    engine = pyttsx3.init()
    engine.say(fala)
    engine.runAndWait()

if __name__ == "__main__":
    ouvir_microfone()