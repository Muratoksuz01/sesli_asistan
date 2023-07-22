import speech_recognition as sr
from datetime import datetime
from gtts import gTTS
from playsound import playsound
import random,os,random,webbrowser

r= sr.Recognizer()
def record(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio=r.listen(source)
        voice=""
        try:
            voice= r.recognize_google(audio,language="tr-TR")
        except sr.UnknownValueError:
            speak("anlamadım")
        except sr.RequestError:
            speak("sistem calışmıyor")
    return voice
    
def response(voice):    
    if "nasılsın" in voice:
        speak("iyidir")
    if  voice in ["saat kaç","saat kac"]  :
        hours=datetime.now().strftime("%H:%M")
        speak(hours)
        #speak(str(datetime.now().strftime("%H:%M:%S")))
    if "arama yap" in voice:
        speak("ne aramak istiyorsun")
        search=record()
        print(search)
        url="https://google.com/search?q="+search
        webbrowser.get().open(url)
        speak(search+"bulduklarım")
    if "hangi gündeyiz" in voice:
        day=datetime.now().strftime("%A")
        speak(day)
    if "tamamdır" in voice:
        speak("görüşürüz")
        exit()
    if "uygulama çalıştır" in voice:
        speak("hangi uygulama")
        runapp=record()
        if "kod programı" in runapp:
            os.startfile(r"path of  your want to run ,important!! the should be '.exe' the end of your path ")
        #elif  boyle tum uygulamarın path ekleyin 
    if "not al" in voice:
        speak("dosyanın adı ne ?")
        filename=record()
        with open(filename+".txt","w",encoding="utf-8") as f:
            speak("ne yazdırmak istiyorusun")
            content=record()
            f.writelines(content)
def speak(string):
    tts=gTTS(string,lang="tr",slow=False)
    rand=random.randint(1,1000)
    file=f"audio-{rand}.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)


playsound("ding.mp3")
while 1:
    test=record()
    if test!="":
        test=test.lower()
        print(test)
        if "hey python" in test:
            speak("hello murat ")
            while 1:
                voice=record()
                print(voice)
                response(voice)



