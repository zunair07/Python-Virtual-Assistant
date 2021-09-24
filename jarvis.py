
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib


dict={
    
    'john': 'ahmadzunair21@gmail.com',
    'james': 'awaiskayani264@gmail.com'
}

engine= pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():       
    hour =int(datetime.datetime.now().hour)


    if hour >=6 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<=18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("Hello Sir! my name is Jarvis. Please tell me what can I do for you?")    

def takeCmd():
    r=sr.Recognizer()
    with sr.Microphone() as source: 
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 1500
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query= r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, msg):
    server =smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('zunairahmed877@gmail.com', 'zunair4321')
    server.sendmail('zunairahmed877@gmail.com', to, msg)
    server.close()

    

if __name__ == "__main__":
    wishMe()
    #speak("hello world , fuck offf")
    
    if 1:
        query= takeCmd().lower()
        if 'wikipedia' in query:
            print("Searching Wikipedia...")
            query=query.replace("wikipedia", "")
            result=wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(result)
            speak(result)

        elif 'open youtube' in query:
            speak("okay sir!")
            webbrowser.open("youtube.com")
               
        elif 'open google' in query:
            speak("okay sir!")
            webbrowser.open("google.com") 

        elif 'open stackoverflow' in query:
            speak("okay sir!")
            webbrowser.open("stackoverflow.com") 
        
        elif 'play music' in query:
            music_dir = "E:\\dir\\dir"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.join(music_dir, songs[0]))

        elif 'time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strtime}")

        elif 'open code' in query:
            path="C:\\Users\\Zunair Ahmad\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)

        elif 'send email' in query:
            speak("Sir, please tell me the name of person which you want to send email")
            #taking cmd in string then split, then searching name in dict.
            ans=takeCmd().lower()
            temp_dict=dict.keys()
            temp_ans=ans.split(" ")
            Person_name=" "
            print(temp_ans)
            for i in range(len(temp_ans)):
                for name in temp_dict:
                    if temp_ans[i]==name:
                        Person_name=name

            if Person_name== " ":
                speak("this person is not in your contacts, please update your contact list!")
                
            else:
                try:
                    print(Person_name)
                    speak("What should i say to")
                    msg = takeCmd()
                    to = dict[Person_name]
                    sendEmail(to, msg)
                    speak("Email has been sent. goodbye.")

                except Exception as e:
                    print(e)
                    speak("sorry, i'm not able to send email. goobye.")    


        elif 'how are you' in query:
            speak("i'm fine sir! hope you are fine too")        

        elif 'how old are you' in query:
            birthday=datetime.date(2020, 4, 14)
            today=datetime.date.today()
            how_old=(today - birthday).days
            print(f"i am {how_old} days old.")
            speak(f"i am {how_old} days old.")

        elif 'who are you' in query:
            print("i'm jarvis a machine, i'm build by Zunair. He is my creator, and i can do anything for him.")    
            speak("i'm jarvis a machine, i'm build by Zunair. He is my creator, and i can do anything for him.")
        