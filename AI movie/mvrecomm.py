import pandas as pd
import speech_recognition as sr
import pyttsx3

# text to speech
def speak(text):
    print(text)
    engine = pyttsx3.init()
    engine.setProperty('rate', 200)
    engine.setProperty('volume', 1)
    engine.say(text)
    engine.runAndWait()
    engine.stop()


data = pd.read_csv("movies.csv")


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        print("Speak Movie Genre...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You said:", text)
        return text.lower()
    except:
        return ""

# recommendation function
def recommend(genre):
    result = data[data['genre'].str.lower()==genre]

    if len(result)==0:
        speak("Sorry No Movies Found")
    else:
        speak("Recommended Movies")
        for i,row in result.iterrows():
            speak(row['movie'])

# main program
speak("Welcome to AI Movie Recommendation System")
speak("Please say a movie genre you like")
genre = listen()

recommend(genre)