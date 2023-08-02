import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pywhatkit
import time
import wolframalpha


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170) 

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme(): #for greeting
    
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am dell sir...")
    
def takeCommand(): #take commands
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=0.2)
        print("Listening...")
        
        r.energy_threshold = 4000
        #r.dynamic_energy_threshold = True
        #r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")

    except Exception as e:
       # print(e)
        print("Say that again please...")
        speak("I Cant understand, can you repeat it...")
        return "None"

    return query

if __name__=="__main__":  #main function

    wishme()
    
    while True: 
        query = takeCommand().lower()

        if 'hi dell' in query or "hai" in query: 
            speak("hello sir, Please tell me how may I help you")
            

        elif 'hello dell' in query or "hello" in query:
            speak("hi sir, Please tell me how may I help you")

        elif 'how are you' in query:
            speak("I am good, thank you for asking. I hope you are doing well too. If I can help with anything, just ask...")

        elif 'are you free' in query:
            speak('Yes sir,how I can help you...')

        elif 'wikipedia' in query or "who is" in query: #accessing wikipedia
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'play'in query: #play songs on youtube
            song = query.replace("play", "")
            speak("Playing " + song)
            pywhatkit.playonyt(song)

        elif 'open google' in query: # open google page from edge browser(default browser)
            webbrowser.open("google.com")

        elif 'search' in query: #search on google page from edge browser(default browser) 
            topic = query.replace("search", "")
            T = pywhatkit.search(topic)

        elif 'time' in query: #tells current systems tims
            strTime = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"Sir, the current time is {strTime}")

        elif 'who are you' in query:
            speak("I am a machine made by Om Chavan and my name is dell")
        
        elif 'feelings' in query or 'feel' in query:
            speak("NO sir, Right now I can't feel any human feelings")
        
        elif 'shutdown the system' in query: #shutdown the system
            speak("Ok sir,System is turn off...")
            print("System is turn off...")
            pywhatkit.shutdown()
            
        elif 'cancel shutdown' in query: #cancel shutdown the system
            speak("Ok sir,System shutdown is terminated")
            print("System shutdown is terminated...")
            pywhatkit.cancel_shutdown()

        elif 'open dev cpp' in query: #open dev c plus plus
            speak('wait Opening ...')
            os.startfile("C:\Program Files (x86)\Dev-Cpp\devcpp.exe")

        elif 'open vs code' in query:# open visual studio code
            speak('wait opening...')
            os.startfile("C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

        elif "don't listen" in query or "stop listening" in query:# stop for while , doesnt take commands
            speak("for how much time you want to stop listening ")
            a = takeCommand()
            if 'seconds' in a:
                a = a.replace("seconds", "")
                a = int(a)
            elif 'second' in a:
                a = a.replace("second", "")
                a = int(a)

            elif 'minutes' in a: 
                a = a.replace("minutes", "")
                a = 60*int(a)
            elif 'minute' in a: 
                a = a.replace("minute", "")
                a = 60*int(a)

            elif 'hour' in a: 
                a = a.replace("hour", "")
                a = 3600*int(a)
            elif 'hours' in a: 
                a = a.replace("hours", "")
                a = 3600*int(a)

            speak("Ok Sir...")
           
            while a > 0:
 
                # Timer represents time left on countdown
                timer = datetime.timedelta(seconds = a)
                
                # Prints the time left on the timer
                print(timer, end="\r")
        
                # Delays the program one second
                time.sleep(1)
        
                # Reduces total time by one second
                a -= 1

            speak("Ready to take commands...")
           
 
        elif "what is" in query : #gives mathematical and science related answers
             
            app_id = "VVJ46G-YLLVRW474J"
            client = wolframalpha.Client(app_id)
            res = client.query(query)
             
            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                print ("No results")

        elif "write a note" in query or "add a note" in query or "take a note" in query: #take notes and also save
            speak("What should i write, sir")
            note = takeCommand()
            file = open('notes.txt', 'a')
            print("Sir, Should i include date and time")
            speak("Sir, Should i include date and time")

            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm or 'ok' in snfm : 
                today = str(datetime.date.today())
                strTime = datetime.datetime.now().strftime("%I:%M %p")
                file.write(today)
                file.write("|"+strTime)
                file.write(" :- ")
                file.write(note+"\n")
                speak("ok sir, note added")
            elif "no" in query or "dont" in query:
                file.write(note+"\n")
                speak("ok sir, note added")
         
        elif "show note" in query or "so note" in query or "show me note" in query:# showing notes
            speak("Showing Notes")
            file = open("notes.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif "clear all notes" in query or "clear all note" in query:# clear all notes from file
            file = open("jarvis.txt", 'w')
            speak("all notes are deleted...")


        elif 'exit' in query or 'stop' in query:# exit from programme
            speak("Ok sir...")
            exit()

