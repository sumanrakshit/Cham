import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import json
import requests
import random
import wolframalpha
from urllib.request import urlopen
import pyjokes
import winshell 
import ctypes 
import subprocess 


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<16:
        speak("Good Afternoon!")
    elif hour>=16 and hour<22:
        speak("Good Evening !!!")       

    else:
        speak("Good Night!")  

    speak(" I am your champ Suman Sir. Please tell me how may I help you")       

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

    except Exception as e:
        print(e)
        print("Please say again....")
        return "None"
    return query        
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sumanrakshit1997@gmail.com', '9474183007')
    server.sendmail('sumanrakshit1997@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            try:

                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                print(e)
                speak("please say again.....")    


        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com") 
        elif 'tell me' in query:
            try:
                speak("Please say your question sir")
                question=takeCommand().lower()
                app_id='THJ535-YV3TG5HGE5'
                client=wolframalpha.Client(app_id)
                res=client.query(question)
                ans=next(res.results).text
                speak(ans)
                print(ans)
            except Exception as e:
                print("please say again !!")         
        elif 'news' in query:
            try:
                speak("News for today ....let's begin .")
                url = ("https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=d093053d72bc40248998159804e0e67d")
                news = requests.get(url).text
                news_dict = json.loads(news)
                arts = news_dict['articles']
                for article in arts:
                    speak(article['title'])
                    print(article['title'])
                    print(article['description'] + '\n')
                    speak("Moving on to the next news..Listen Carefully")

                speak("Thanks for listening...") 
            except Exception as e:

                speak(str(e))         



        elif 'play music' in query:
            music_dir = 'E:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            act= random.randint(0,len(songs)-1)    
            os.startfile(os.path.join(music_dir, songs[act]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath ="C:\\Users\\dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'open Chrome' in query:
            codepath="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codepath)   

        elif 'email to Suman' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "sumanrakshit0305@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Suman bhai. I am not able to send this email") 
        elif 'how are you' in query:
            speak("I am fine , Thank you ")
            speak("How are you sir !!")
        elif 'fine' in query or 'good' in query:
            speak("It's good to know that you are fine have a good day sir")
        elif 'to have gf' in query or 'to have bf' in query:
            speak(" I am not sure about this")
        elif 'will you be my gf' in query or 'will you be my bf' in query:
            speak("i am not sure about, may be you should gave me some time to take decision") 
        elif 'who create you' in query or 'who made you' in query:
            speak("I have been created by Mr. Suman Rakshit") 
        elif 'who i am' in query:
            speak("as you talk to me so you are a human")   
        elif 'jokes' in query:
            speak(pyjokes.get_joke()) 
            print(pyjokes.get_joke())
     
    
        elif 'suman' in query:
            speak("yeah ,i know this guy, he actuall name sudipta Rakshit")
            speak("now people calling him as suman da , his crush on susrita ")
            speak("now he study at m.g. college")
        elif 'deep' in query:
            speak("yeah ,in know him, his actuall name is soumdeep,also as pacha ")
            speak("people calling him as jamai, now he study at kamalpur netaji school")
        elif 'f***' in query:
            speak("fuck on bitch, asshole,bokachoda")  
        elif 'tumi ki' in query:
            speak(" searching ......please wait.... its personal matter dont say in public")          


                      

        elif 'calculate' in query:
            try:
                app_id = "THJ535-YV3TG5HGE5" 
                client = wolframalpha.Client(app_id) 
                indx = query.lower().split().index('calculate')  
                query = query.split()[indx + 1:]  
                res = client.query(' '.join(query))  
                answer = next(res.results).text 
                speak(answer)
                print("The answer is " + answer)
            except Exception as e:
                print(e)
                speak("please say again....")    
            
        elif 'lock window' in query: 
                speak("locking the device") 
                ctypes.windll.user32.LockWorkStation() 
  
        elif 'shutdown system' in query: 
                speak("Hold On a Sec ! Your system is on its way to shut down") 
                subprocess.call('shutdown / p /f')
        elif 'sanjeev' in query:
            speak("yeah ,know this guy  ,whose also name fhuchu whose father name jagatnath rakshit")  
            speak(" now he chat with piu kundu") 
            speak("he plays good cricket")
            speak("sometimes he spoke biri")                                     
        
        elif 'exist' in query:
            speak("Thank you giving your  valuable time ")
            exit()
        