import speech_recognition as sr
import pyttsx3
import os
import pathlib
import textwrap
from dotenv import load_dotenv 
import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


API_KEY = "AIzaSyCOVNhP6ppz4z2OWxTewKlOnZ7BhsGQ5Xg"

def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-pro')



recognizer = sr.Recognizer()


engine = pyttsx3.init()


def process_query():
    with sr.Microphone(device_index=1) as source:
        print("Kindly provide me a verbal query")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        print("Understanding....")
        try:
            text = recognizer.recognize_google(audio).lower()
            print("Understanding done.")
            return text
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand the audio.")
            return ""


def detect_wake_word():
    with sr.Microphone(device_index=1) as source:
        print("Listening for wake word...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        print("Processing wake word...")
        try:
            text = recognizer.recognize_google(audio).lower()
            print("Wake word detected.")
            return "khushi" in text
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand the audio.")
            return False


def say(text):
    engine.say(text)
    engine.runAndWait()

while True:
    if detect_wake_word():
        say("How may I help you?")
        query = process_query()
        response = model.generate_content(query+"in a precise and short way as required").text
        say(response)