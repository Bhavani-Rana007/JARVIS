import pyttsx3
import speech_recognition as sr
import datetime
import os
import webbrowser
import wikipedia
import pyjokes
import pyautogui 
import pywhatkit as kit
import webbrowser
import sys
import smtplib
import random
import operator
import requests
from bs4 import BeautifulSoup
from pywikihow import search_wikihow
import psutil
import speedtest
from plyer import notification
from pygame import mixer





for i in range(3): 
    a = input("Enter Password to open Jarvis :- ")
    pw_file = open("password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("WELCOME SIR ! ")
        break
    elif (i==2 and a!=pw):
        exit()  

    elif (a!=pw):
        print("Try Again")


from INTRO import play_gif
play_gif


#text to speach
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voices',voices[0].id)



def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()



#to convert voice into text.
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio = r.listen(source,timeout=7,phrase_time_limit=9)
       
        

    try:
        print("Recognizing...")
        Query = r.recognize_google(audio,language='en-in')
        print(f"user said:{query} ")

    except Exception as e:
       speak("say that again  please...")
    return Query   
    



#to wish.
def wish():

    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("good morning...")
    elif hour>12 and hour<18:
        speak("good afternoon...")
    else:
        speak("good evening...")        
    speak("i am jarvis sir. please tell me how can i help you")


#to send email.
def sendEmail (to, content):
    server = smtplib.SMTP("smtp.gamil.com",587)
    server.ehlo()
    server.starttls()
    server.login('bhavanisinghrana007@gmail.com','ROYALRANA007')
    server.sendmail('bhavanisinghrana007@gmai.com', to,content)
    server.close()





def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")





if __name__ == "__main__":
#def TaskExecution():
    wish()
    while True:
     
        query = takecommand().lower()


        if "change password" in query:
          speak("What's the new password")
          new_pw = input("Enter the new password\n")
          new_password = open("password.txt","w")
          new_password.write(new_pw)
          new_password.close()
          speak("Done sir")
          speak(f"Your new password is{new_pw}")


        

        elif 'open command prompt' in query:
            os.system("start cmd")   


 

        elif 'type' in query:
             query = query.replace("type","")
             pyautogui.typewrite(f"(query)",0.1)

 

        
        elif 'youtube' in query:
            webbrowser.open("https://www.youtube.com/")   



        elif 'play songs on youtube' in query:
            kit.playonyt("love me like you do")   


        # elif "pause" in query:
        #     pyautogui.press("k")
        #     speak("video paused")
        # elif "play" in query:
        #     pyautogui.press("k")
        #     speak("video played")
        # elif "mute" in query:
        #     pyautogui.press("m")
        #     speak("video muted")

        # elif "volume up" in query:
        #     from keyboard import volumeup
        #     speak("Turning volume up,sir")
        #     volumeup()
        # elif "volume down" in query:
        #     from keyboard import volumedown
        #     speak("Turning volume down, sir")
        #     volumedown()    





        elif 'rgpv' in query:
            webbrowser.open("https://www.rgpv.ac.in/")  





        elif 'google' in query:
            speak("sir,what should i search on google")
            cm=takecommand().lower()
            webbrowser.open(f"{cm}")    





        elif 'wikipedia' in query:
            speak("searching wikipedia")
            query = query.replace("wikipedia"," ")
            results = wikipedia.summary(query, sentences=3)
            speak("according to wikipedia")
            speak(results) 
            print(results)   

     


        elif "set an alarm" in query:
             print("input time example:- 10 and 10 and 10")
             speak("Set the time")
             a = input("Please tell the time :- ")
             alarm(a)
             speak("Done,sir")





        elif "open" in query:
          from Dictapp import openappweb
          openappweb(query)
        elif "close" in query:
          from Dictapp import closeappweb
          closeappweb(query)


        # elif "open" in query:   
        #             query = query.replace("open","")
        #             query = query.replace("jarvis","")
        #             pyautogui.press("super")
        #             pyautogui.typewrite(query)
        #             pyautogui.sleep(2)
        #             pyautogui.press("enter")

        

 
        elif "whatsapp" in query:
           from Whatsapp import sendMessage
           sendMessage()





        elif "joke" in query:
            joke_1 = pyjokes.get_joke(language = "en",category = "neutral")
            print(joke_1)
            takecommand(joke_1)      



        elif "schedule my day" in query:
            tasks = []
            speak("Do you want to clear old tasks (Plz speak YES or NO)")
           # query = takeCommand().lower()
            if "yes" in query:
               file = open("tasks.txt","w")
               file.write(f"")
               file.close()
               no_tasks = int(input("Enter the no. of tasks :- "))
               i = 0
               for i in range(no_tasks):
                   tasks.append(input("Enter the task :- "))
                   file = open("tasks.txt","a")
                   file.write(f"{i}. {tasks[i]}\n")
                   file.close()
            elif "no" in query:
              i = 0
              no_tasks = int(input("Enter the no. of tasks :- "))
              for i in range(no_tasks):
                  tasks.append(input("Enter the task :- "))
                  file = open("tasks.txt","a")
                  file.write(f"{i}. {tasks[i]}\n")
                  file.close()


        elif "show my schedule" in query:
             file = open("tasks.txt","r")
             content = file.read()
             file.close()
             mixer.init()
             mixer.music.load("android_notification.mp3")
             mixer.music.play()
             notification.notify(
                title = "My schedule :-",
                message = content,
                timeout = 15
             )







        elif 'email to anu' in query:
            try:
                speak("what should i say ?")
                content = takecommand().lower()
                to = "anuragagrawal510@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent to anu")

            except Exception as e:
                print(e)
                speak("sorry sir,i am not able to send this email")     




        elif "internet speed" in query:
                    wifi  = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576         
                    download_net = wifi.download()/1048576
                    print("Wifi Upload Speed is", upload_net)
                    print("Wifi download speed is ",download_net)
                    speak(f"Wifi download speed is {download_net}")
                    speak(f"Wifi Upload speed is {upload_net}")


        
        # elif "tired" in query:
        #     speak("Playing your favourite songs, sir")
        #     a = (1,2,3) # You can choose any number of songs (I have only choosen 3)
        #     b = random.choice(a)
        #     if b==1:
        #     webbrowser.open()



        elif 'temperature' in query:
            search = "temperature in indore"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"current {search} is {temp}")
            



        elif "the time" in query:
         strTime = datetime.datetime.now().strftime("%H:%M")    
         speak(f"Sir, the time is {strTime}")





        elif "news" in query:
            from NewsRead import latestnews
            latestnews()




        elif "activate how to do mod" in query:
            speak("how to do mode is activated")
            while True:
                speak("please tell me what you want to know")
                how = takecommand()
                try:
                    if "exit" in how or "close " in how:
                        speak("okay sir,how to do mode is closed")
                        break
                    else:
                        max_results = 1
                        how_to = search_wikihow(how, max_results)
                        assert len(how_to) ==1
                        how_to[0].print()
                        speak(how_to[0].summary)
                except Exception as e:
                    speak("sorry sir,i am not able to find this")        
            






        elif "do some calculations" in query or "can you calculate" in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("say what you want to calculate, example: 3 plus 3")
                print("listening...")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            my_string = r.recognize_google(audio)
            print(my_string)
            def get_operator_fn(op):
                return {
                    '+' : operator.add,
                     '-' : operator.sub,
                      'x' : operator.mul,
                       'divided' : operator.__truediv__,
                } [op]
            def eval_binary_expr(op1,oper,op2):
                op1,op2 = int(op1),int(op2)
                return get_operator_fn(oper)(op1,op2)
            speak("your result is")
            speak(eval_binary_expr(*(my_string.split())))





        elif "screenshot" in query:
                     import pyautogui #pip install pyautogui
                     im = pyautogui.screenshot()
                     im.save("ss.jpg")





        elif "how much power left" in query or "battery" in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"sir our system have {percentage} percent battery")





        elif "ipl  score" in query:
                    from plyer import notification  
                    import requests 
                    from bs4 import BeautifulSoup 
                    url = "https://www.cricbuzz.com/"
                    page = requests.get(url)
                    soup = BeautifulSoup(page.text,"html.parser")
                    team1 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
                    team2 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
                    team1_score = soup.find_all(class_ = "cb-ovr-flo")[8].get_text()
                    team2_score = soup.find_all(class_ = "cb-ovr-flo")[10].get_text()

                    a = print(f"{team1} : {team1_score}")
                    b = print(f"{team2} : {team2_score}")

                    notification.notify(
                        title = "IPL SCORE :- ",
                        message = f"{team1} : {team1_score}\n {team2} : {team2_score}",
                        timeout = 15
                    )





        elif "play a game" in query:
                from game import game_play
                game_play()





        elif "translate" in query:
                    from Translator import translategl
                    query = query.replace("jarvis","")
                    query = query.replace("translate","")
                    translategl(query)





        elif "focus mode" in query:
                    a = int(input("Are you sure that you want to enter focus mode :- [1 for YES / 2 for NO "))
                    if (a==1):
                        speak("Entering the focus mode....")
                        os.startfile("C:\\Users\\Rana Bhavani\\Desktop\\JARVIS\\FocusMode.py")
                        exit()

                    
                    else:
                        pass





        elif "shutdown the system" in query:
         speak("Are You sure you want to shutdown")
         shutdown = input("Do you wish to shutdown your computer? (yes/no)")
         if shutdown == "yes":
            os.system("shutdown /s /t 1")

         elif shutdown == "no":
           break




        elif "no thanks" in query:
                    speak("thanks for using me sir ,have a good day")
                    sys.exit()




        speak("sir, do you have any other work")            

