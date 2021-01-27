import wolframalpha
import pyttsx3  # pip3 install pyttsx3
import speech_recognition as sr  # pip3 install speechRecognition
import wikipedia


def search(query):
    try:
        # wolframalpha
        app_id = "QWH8JW-96AY6KKAAW"
        client = wolframalpha.Client(app_id)
        res = client.query(query)
        answer = next(res.results).text
        print(answer)
        SpeakText("Your answer is" + answer)
    except:
        query = query.split('')
        query = " ".join(query[0:])

        SpeakText("I am searching for " + query)
        print(wikipedia.summary(query, sentences=3))
        SpeakText(wikipedia.summary(query, sentences=3))

def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say Something ")
    r.adjust_for_ambient_noise(source, 2)
    audio = r.listen(source)

try:
    speech = r.recognize_google(audio)
    search(speech)
except sr.UnknownValueError:
    print("Google Speech Recognition could not \ understand audio")

except sr.RequestError as e:
    print("Could not request results from google \
          Speech Recognition service;{0}".format(e))
else:
    print("Run the program again")
