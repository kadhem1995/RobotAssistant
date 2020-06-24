
import speech_recognition as sr
from gtts import gTTS
import os 
import playsound
import json

f = open("../data/dict_english.json", 'r')
data = json.load(f)
f.close()
r = sr.Recognizer()
known_commands = []
for k in data.keys():
    known_commands.append(k)

with sr.Microphone() as source:
        print("Speak...")
        audio = r.listen(source, phrase_time_limit=5)
        print("Stop.")
try:
        text = r.recognize_google(audio,language='en-UK') or r.recognize_goole(audio,language='en-FR')
        print("You : ", text)
except:
    pass
if text in known_commands :
    for k in data.keys():
        if k in text :
            toSpeak = gTTS(text=data[k], lang='en-UK', slow=False) 
            toSpeak.save("temp.mp3")
            playsound.playsound("temp.mp3", True)
            os.remove("temp.mp3")
else :
    toSpeak = gTTS(text="i didn't understand you", lang='en-UK', slow=False) 
    toSpeak.save("temp.mp3")
    playsound.playsound("temp.mp3", True)
    os.remove("temp.mp3")
