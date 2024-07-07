import webbrowser
import google.generativeai as genai
import os
import win32com.client
import speech_recognition as sr
from config import apiKey

# Replace with your actual API key
gemini_api_key = apiKey

genai.configure(api_key=gemini_api_key)
model = genai.GenerativeModel('gemini-pro')  # Or other model name

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def takeCommand():

    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception:
        # print(e)
        speaker.Speak("Say that again please...")
        return 'None'

    return query


if __name__ == "__main__":
    speaker.Speak("Good Morning! I am Jarvis Ai! How may I help you?")
    while True:
        query = takeCommand().lower()

        if "Open Youtube".lower() in query.lower():
            speaker.Speak("Opening Youtube...")
            webbrowser.open("https://youtube.com")

        elif 'close' in query:
            speaker.Speak("Thank you sir! Good bye!")
            exit()

        else:
            response = model.generate_content(query)
            print(response.text)
            speaker.Speak(response.text)