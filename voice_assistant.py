import pyttsx3
import speech_recognition as sr
import datetime

engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='en-in')
            return query.lower()
        except:
            return ""

def greet():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning")
    elif hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")

def get_time():
    now = datetime.datetime.now()
    speak("The time is " + now.strftime("%I:%M %p"))

def get_date():
    now = datetime.datetime.now()
    speak("Today's date is " + now.strftime("%B %d, %Y"))

def chat_response(query):
    if "how are you" in query:
        speak("I'm fine, thank you!")
    elif "what's your name" in query or "your name" in query:
        speak("I am your voice assistant you can call me anything you want except siri and alexa or google. it hurts.")
    elif "thank you" in query:
        speak("You're welcome")
    else:
        speak("I didn't get that. Can you repeat?")

greet()
speak("How can I help you today?")

while True:
    query = listen()
    if "time" in query:
        get_time()
    elif "date" in query:
        get_date()
    elif "stop" in query or "exit" in query:
        speak("Goodbye!")
        break
    else:
        chat_response(query)
