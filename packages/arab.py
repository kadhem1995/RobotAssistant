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
from google.cloud import translate 
import random 
def assistant_speaks(output):
    global num
    num +=1
    print("olga : ", output)
    toSpeak = gTTS(text=output, lang='ar', slow=False) 
    file = str(num)+"mp3"
    toSpeak.save(file)
   # mp3_fp = BytesIO()
   # toSpeak = gTTS(output, 'en', slow=False)
   # toSpeak.write_to_fp(mp3_fp)
   # os.system("hiba@hiba-X540UB:~/Downloads/person-personal-assistant-master/spoken.mp3")
    '''mixer.init()
    mixer.music.load('hiba@hiba-X540UB:~/Downloads/person-personal-assistant-master/spoken.mp3')
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
        print ('تكلم...')
        audio = r.listen(source, phrase_time_limit=5)
    print("قف.")
    try:
        text = r.recognize_google(audio,language='ar') 
        print("أنت : ", text)
        return text
    except:
        assistant_speaks( "لم اسمعك جيد")
        return 0



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

    wikipedia.set_lang("ar")

    try:
        if "من أنت"  in input or "صف نفسك" in input:
            speak = '''مرحبًا ، أنا أولغا ، حاضنة طفلك ، أنا هنا لألعب معك ، يمكنك أن تسألني عما تريد عزيزي.'''
            assistant_speaks(speak)
            return
        elif "من صنعك" in input or "من خلقك" in input:
            speak = "لقد صُنِعْتُ  من قبل هبة بن حمودة."
            assistant_speaks(speak)
            return
        #elif "هل تريد قهوة" in input:
        #    speak =[ " القطة الحائرة في أحد الأيام كانت هناك قطةٌ لطيفةٌ وجميلة تدعى قطقوطة، إلّا أنّها كانت لا تحبّ شكلها، فكانت تتذمّر في كلِّ مرّةٍ في تنظر فيها إلى المرآة، وكانت تقضي وقتها في مراقبة الحيوانات الأخرى، فيوماً تحلم أنّها تستطيع الطيران كالطيور، ويوماً تحلم أنّها تستطيع السباحة كالأسماك، ويوماً تحلم أنّها تستطيع الجري بسرعةٍ كالفهد في الغابات، وكانت خيالاتها تلك تمنعها من إدراك ما تتميز به عن المخلوقات الأخرى من نعم خصّها الله بها، وفي أحد الأيام كانت قطقوطة تلعب قريباً من البحيرة، فرأت بعض البطّات الصغيرة التي تسبح في البحيرة، فتمنّت لو أنّها قادرةً على السّباحة كالبط، وحاولت ذلك إلّا أنّها لم تستطع أن تسبح ببراعتهن، فنفضت جسمها من الماء وسارت غاضبة تكمل طريقها نحو المنزل حتى شاهدت أرنباً يقفز بمرحٍ ويتناول الجزر بشهيّة، فتمنّت أن تصير أرنباً، وعندما حاولت القفز مثله لم تستطع فعل ذلك، فقالت: سأتناول الجزر مثله إذن، إلّا أنّ طعمه لم يعجبها أبداً؛ فالقطط لا تحبُّ الجزر، أدرات قطقوطة ظهرها عائدة إلى المنزل فشاهدت قطيعاً من الخراف التي أعجبها صوفها الكثيف وشكلها المستدير وتخيّلت جمال شكلها إن هي أصبحت خروفاً، فأسرعت تبحث في دولاب البيت عن قطعة من الصوف، وما إن وجدتها حتى لفَّت نفسها بها وبدأت تمشي فرحة مع القطيع، ولكنّ هذا الصوف جعلها تشعر بالحرّ الذي لم تتمكن من احتماله، فحزنت وأزالته عن جسمها وهربت. سارت القطة حزينة في طريقها لا تدري ماذا تفعل، فقررت أن تجلس تحت الشجرة لتستريح قليلاً، وأثناء جلوسها أرادت أن تُسلَي نفسها فأخذت تموء بصوتها اللطيف وتصدر أنغاماً عدّة، فمرّت عليها زرافة طويلة اقتربت منها وقالت لها: يا إلهي ما أجمل صوت موائك! أتمنى لو أنني أمتلك حبالاً صوتيةً تمكنني من الغناء مثلك أيّتها القطة، ابتسمت قطقوطة وعلا صوت موائها من شدّة الفرح بما قالته لها الزرافة، إلّا أنَّها سمعت صوت عجوز تنادي: أنقذوني أنقذوني فهعرت بسرعة إلى مكان الصوت لتجد أفعى كبيرة تحاول لدغ هذه العجوز التي لا تستطيع الدفاع عن نفسها، فوثبت القطة مسرعة ونالت من هذه الأفعى الشريرة بمخالبها القوية وأبعدت "]
         #   assistant_speaks(random.choice(speak))
          #  return


        elif "هل تريد قهوة" in input:
            speak =[ '''نعم ، أخبر نعيم أن يجلب لي أكسبرسو ، لا أريد الصودا ''']
            assistant_speaks(random.choice(speak))
            return

        elif "كيف حالك" in input:
            speak = [" أنا بخير الحَمْدُ لِلهْ "]
            assistant_speaks(random.choice(speak))
            return
        elif "Play musique "in input :
            speak="got it!"
            assistant_speaks(speak)
            mus=['pol.wav' , 'bel.wav']
            music = pyglet.resource.media(random.choice(mus) , streaming=False)
            music.play()
            pyglet.app.run()
            return
        elif "هل انت جوعان" in input or "لنأكل" in input :
            speak="دعنا نأكل!!"
            assistant_speaks(speak)
            return
        elif "اين ابي " in input or "اريد بابا" in input or " بابا" in input :
            speak = "ربما يكون في العمل ، لا تقلق يا عزيزتي ، أنا معك ، أفضل صديق لك "
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
            #assistant_speaks("I can search the web for you, Do you want to continue?")
           # ans = get_audio()
           # if 'yes' in str(ans) or 'yeah' in str(ans):
            question=input.lower()
            app_id="KL8K7A-X6HWG8TKAG"
            client = wolframalpha.Client(app_id)
           # indx = input.lower().split().index('who')
            #query = input.lower
            res = client.query(question)
           # answer = next(res.results).text
            try:
                answer= wikipedia.summary(text, sentences=3)
                assistant_speaks(answer)
            except :
                assistant_speaks(wikipedia.summary(question))



            
    except Exception as e:
        print(e)       
       # else:
#            return
 
        #assistant_speaks("I don't understand, I can search the web for you, Do you want to continue?")
      #  ans = get_audio()
       # if 'yes' in str(ans) or 'yeah' in str(ans):
        #    search_web(input)


if __name__ == "__main__":
    #assistant_speaks("What's your name, Human?")
    name ='هِيبَةُ '
    #name = get_audio()
    assistant_speaks("مرحبا  " + name + '.')
    #print("1:arabe")
    #print("2:français")
    #langue=input("Taper la langue")
    #if(langue=='1'):
    while(1):
        	lis=["كيف يُمْكِنُني  أَنْ  أُسَاعِدُكَ" , "ما هو الآن حبيبي "]
	        assistant_speaks(random.choice(lis))
	        text = get_audio().lower()
        	if text == 0:
                   continue
	        assistant_speaks(text)
	        process_text(text)
   # elif(langue=='2'):
	   # while(1):
            #    lis=["salut " , "çava "]
            #    assistant_speaks(random.choice(lis),'fr')
             #   text = get_audio().lower()
              #  if text == 0:
               #    continue
                #assistant_speaks(text)
                #process_text(text)
	
