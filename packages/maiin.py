
import speech_recognition as sr  # importing speech recognition package from google api
from pygame import mixer
import playsound    # to play saved mp3 file
from gtts import gTTS   # google text to speech
import os   # to save/open files
import wolframalpha # to calculate strings into formula, its a website which provides api, 100 times per day
from selenium import webdriver  # to control browser operations
from selenium.webdriver.common.keys import Keys
from io import BytesIO
from io import StringIO
import pyglet
num = 1
import time
import wikipedia
import requests 
import random 
def assistant_speaks(output):
    global num
    num +=1
    print("olga : ", output)
    toSpeak = gTTS(text=output, lang='en-UK', slow=False) 
    file = str(num)+"mp3"
    toSpeak.save(file)
   # mp3_fp = BytesIO()
   # toSpeak = gTTS(output, 'en', slow=False)
   # toSpeak.write_to_fp(mp3_fp)
   # os.system("hiba@hiba-X540UB:~/Desktop/person-personal-assistant-mast$/ spoken.mp3")

    '''mixer.int()
    mixer.music.load('hiba@hiba-X540UB:~/Desktop/person-personal-assistant-master/spoken.mp3')
    mixer.music.play()
    time.sleep(5)
    mixer.music.stop()'''
    #song = AudioSegment.from_file(mp3_fp, format="mp3")
   # playsound.playsound(mp3_fp)
    playsound.playsound(file, True)
    os.remove(file)


def get_audio():
    r = sr.Recognizer()
    audio = ''
    with sr.Microphone() as source:
        print("Speak...")
        audio = r.listen(source, phrase_time_limit=5)
    print("Stop.")
    try:
        text = r.recognize_google(audio,language='en-UK') or r.recognize_goole(audio,language='en-FR')
        print("You : ", text)
        return text
    except:
        assistant_speaks("i can't hear you well!")
        return 0


def search_web(input):
    driver = webdriver.Firefox()
    driver.implicitly_wait(1)
    driver.maximize_window()
    if 'youtube' in input.lower():
        assistant_speaks("Opening in youtube")
        indx = input.lower().split().index('youtube')
        query = input.split()[indx+1:]
        driver.get("http://www.youtube.com/results?search_query=" + '+'.join(query))
        return

    elif 'wikipedia' in input.lower():
        assistant_speaks("Opening Wikipedia")
        indx = input.lower().split().index('wikipedia')
        query = input.split()[indx + 1:]
        driver.get("https://en.wikipedia.org/wiki/" + '_'.join(query))
        return
    else:
        if 'google' in input:
            indx = input.lower().split().index('google')
            query = input.split()[indx + 1:]
            driver.get("https://www.google.com/search?q=" + '+'.join(query))
        elif 'search' in input:
            indx = input.lower().split().index('google')
            query = input.split()[indx + 1:]
            driver.get("https://www.google.com/search?q=" + '+'.join(query))
        else:
            driver.get("https://www.google.com/search?q=" + '+'.join(input.split()))
        return


def open_application(input):
    if "chrome" in input:
        assistant_speaks("Google Chrome")
        os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
        return
    elif "firefox" in input or "mozilla" in input:
        assistant_speaks("Opening Mozilla Firefox")
        os.startfile('C:\Program Files\Mozilla Firefox\\firefox.exe')
        return
    else:
        assistant_speaks("Application not available")
        return

def process_text(input):
    try:
        if "who are you" in input or "define yourself" in input:
            speak = '''hello, i am olga , your baby sitter , i am here to play with you , you can ask me whatever you want honey.'''
            assistant_speaks(speak)
            return
        elif "who made you" in input or "created you" in input:
            speak = "I have been created by Hiba ben Hmouda."
            assistant_speaks(speak)
            return


        elif "who is souad" in input:
            speak = "souad it's my grandmother."
            assistant_speaks(speak)
            return
 
        elif "do you want coffee" in input:
            speak =[ "yes , tell Naim to bring me expresso." , "no i want soda " , "i think cappuccino will be good now "]
            assistant_speaks(random.choice(speak))
            return
        elif "how are you" in input:
            speak = [" i am fine as you darling.","very well now", "i am tired know i want to sleep"]
            assistant_speaks(random.choice(speak))
            return
        elif "play music"in input :
            speak="got it!"
            assistant_speaks(speak)
            mus=['nn.wav' , 'bel.wav']
            music = pyglet.resource.media(random.choice(mus) , streaming=False)
            music.play()
            pyglet.app.run()
            return
        elif "are you hungry" in input or "let's eat" in input :
            speak="let's eat!"
            assistant_speaks(speak)
            return
        elif "where is my dady " in input or "i want my dady" in input or " dady" in input :
            speak = "maybe he is at work , don't worry honey , here i am with you , your best friend "
            assistant_speaks(speak)
            return
        elif "calculate" in input.lower():
            app_id= "E46YXW-T5LG6RT7K7"
            client = wolframalpha.Client(app_id)

            indx = input.lower().split().index('calculate')
            query = input.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            assistant_speaks("The answer is " + answer)
            return
        elif 'open' in input:
            open_application(input.lower())
            return
        elif 'search' in input or 'play' in input:
            search_web(input.lower())
            return
        else:
            assistant_speaks("I can search the web for you, Do you want to continue?")
            ans = get_audio()
            if 'yes' in str(ans) or 'yeah' in str(ans):
                question=(input.lower())                
                app_id="KL8K7A-X6HWG8TKAG"
                client = wolframalpha.Client(app_id)
                #indx = input.lower().split().index('evaa')
                #query = input.split()[indx +1:]
                res = client.query(query)
                #answer = next(res.results).text
                try:
                    answer=next(res.results).text
                    assissant_speaks(answer)
                except :
                    assissant_speaks(wikipedia.summary(question))
            else:
                return
    except Exception as e:
        print(e)
        #assistant_speaks("I don't understand, I can search the web for you, Do you want to continue?")
      #  ans = get_audio()
       # if 'yes' in str(ans) or 'yeah' in str(ans):
        #    search_web(input)


if __name__ == "__main__":
    assistant_speaks("Hello, Human?")
    name ='Hiba'
    name = get_audio()
    assistant_speaks("Hello " + name + '.')
    while(1):
        lis=["what can i do for you honey" , "what is next baby" , "what is now darling"]
        assistant_speaks(random.choice(lis))
        text = get_audio().lower()
        if text == 0:
            continue
        #assistant_speaks(text)
        if "exit" in str(text) or "bye" in str(text) or "go " in str(text) or "sleep" in str(text):
            assistant_speaks("Ok bye,see you later "+ name+'.')
            break
        process_text(text)
