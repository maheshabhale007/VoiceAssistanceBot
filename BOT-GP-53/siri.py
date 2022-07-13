import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia
import webbrowser
import os
import random
import pyjokes
import smtplib
import pywhatkit
from pywikihow import search_wikihow
import requests
import bs4
import pyautogui
# Setting up the voice of BOT
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate', 170)
#defining the speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
# This function is for wishing the owner when BOT is started
def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning!")
        speak("Good Morning!")
       
    elif hour>=12 and hour<18:
        print("Good Afternoon!")
        speak("Good Afternoon!")
        

    else:
        print("Good Evening!") 
        speak("Good Evening!")
        
    print("Hello Sir. I am Alexis. How may I help you")    
    speak("Hello Sir. I am Alexis. How may I help you")
# This TakeCommand function converts the voice inputs to text messages    
def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening. . .")
        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print("user said:", query)



    except Exception as e:
        print(e)
        print("Say that again please")
        return "None"
    return query

#For Sending Emails    
def SendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('yourEmail', 'Password')
    server.sendmail('email', to, content)
    server.close()

#for sending Whatsaap Messages     
def Whatsapp():
    speak("what is the message")
    msg = TakeCommand()
    speak("Sir please tell me the time of sending message")
    speak("Tell time in hour!")
    hour = int(input())
    speak("Tell time in minutes")
    min = int(input())
    pywhatkit.sendwhatmsg("Number", msg, hour, min, 20)
    speak("Message has been send")
#For getting Corona report of a country
def CoronaVirus(country):
    countries = str(country).replace(" ", "")
    data_url = f"https://www.worldometers.info/coronavirus/country/{countries}/"
    result = requests.get(data_url)
    soaps = bs4.BeautifulSoup(result.text, 'lxml')
    corona = soaps.find_all('div', class_ = "maincounter-number")
    data = []
    for i in corona:
        span = i.find('span')
        data.append(span.string)
    cases, death, recovered = data
    print(f"Cases: {cases}")
    print(f"Deaths: {death}")
    print(f"Recovered: {recovered}")
    speak(f"Cases: {cases}")
    speak(f"Deaths: {death}")
    speak(f"Recovered: {recovered}")




#Main Function
def Taskexec():
    WishMe()
    
    
    while True:
        query = TakeCommand().lower()
    
        # Searching anything on wikipedia
        if "wikipedia" in query:
            print("Searching Wikipedia...")
            speak("Searching Wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            print("According to wikipedia...")
            speak("According to Wikipedia")
            print(results)
            speak(results)
        #Open youtube    
        elif "open youtube" in query:
            print("Opening Youtube")
            speak("Opening Youtube")
            webbrowser.open("youtube.com")
    
        elif "stackoverflow" in query:
            print("Opening stackoverflow")
            speak("Opening stackoverflow")
            webbrowser.open("stackoverflow.com")
        elif "play movie" in query:
            print("Which movie:")
            speak("Which movie")
        elif "shawshank" in query:
            print("Playing Shawshank Redemption")
            speak("Playing Shawshank Redemption")
            shaw = "E:\\movie\\The.Shawshank.Redemption.1994.720p.BluRay.x264-NeZu\\Screenshots"
            mov = os.listdir(shaw)
            os.startfile(os.path.join(shaw, mov[0]))
        elif "any movie" in query:
            var = random.randint(0,9)
            print("playing random movie")
            speak("Playing Random Movie")
            ran = "D:\\siri test movies"
            mov1 = os.listdir(ran)  
            os.startfile(os.path.join(ran, mov1[var]))    
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(strTime)
        elif "open google chrome" in query:
            chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application"
            print("Opening Google Chrome")
            speak("Opening Google chrome")
            os.startfile(chromePath)
        elif "youtube search" in query:
            speak("Searching Youtube")
            query = query.replace("youtube search", "")
            web = "https://www.youtube.com/results?search_query=" + query
            webbrowser.open(web)
        elif "joke" in query:
            get = pyjokes.get_joke()
            speak("As you wish sir")
            speak(get)
        elif "how are you" in query:
            speak("I am fine Sir. Hope you are also good")

        elif "send email" in query:
            try:
                speak("what should I write")
                content = TakeCommand()
                to = "Email"
                SendEmail(to, content)
                print("Sending Email")
                speak("Sending Email")
                print("Email has been send")
                speak("Email has been send")
            except Exception as e:
                speak("I am not able to send this Email")
        elif "send whatsapp message" in query:
            Whatsapp()      
        elif "open visual studio code" in query:
            print("Opening visual studio code")
            speak("Opening visual studio code")
            os.startfile("C:\\Users\\acer\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
        elif "funny" in query:
            speak("Sorry Sir")
            speak("Anyway thanks for your time")
        elif "google search" in query:
            speak("Searching Google")
            query = query.replace("google search", "")
            pywhatkit.search(query)
        elif "close visual studio code" in query:
            speak("closing visual studio code")
            os.startfile("TASKKILL /F /im Microsoft VS Code.exe")    
        elif "how to" in query:
            speak("Follow the following steps!")
            res = query.replace("Alexis", "")    
            max_result = 1
            how_to_func = search_wikihow(res, max_result)
            assert len(how_to_func)==1
            how_to_func[0].print()
            speak(how_to_func[0].summary)
        elif "news headlines" in query:
            speak("the top five news headlines are")
             # this API key is private, Don't share
            api_key = "Enter you API" 

            news_url = "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=" + api_key # get news from this url
            news = requests.get(news_url).json()
            article = news['articles']
            news_article = []
            for a in article:
                news_article.append(a["title"])
            for i in range(5):
                print(i+1,news_article[i])
                speak(news_article[i])
        elif "corona cases" in query:
            speak("for which country")
            input = TakeCommand().lower()
            CoronaVirus(input) 
        elif "the weather" in query:
            print("Please enter city name: ")
            speak("Please enter city name")
            # enter city name
            city = input()

            url = "https://www.google.com/search?q=" + "weather" + city
            html = requests.get(url).content

            soup = bs4.BeautifulSoup(html, 'html.parser')
            temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text

            str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
            data = str.split('\n')
            time = data[0]
            sky = data[1]

            report = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
            l1 = report[10].text
            l1 = list(l1.split("."))
            l1[0] = " " + l1[0]


            print("Temperature is", temp)
            print("Time: ", time)
            print("Sky Description: ", sky)
            print("Weather Report :-")
            speak(f"Temperature:{temp}")
            speak(f"Time: {time}")
            speak(f"Sky Description: {sky}")
            speak("Weather Report :-")
            for x in l1:
                print(x)    
        elif 'volume up' in query:
            speak("how much")
            print("Enter the volume:")
            inp = int(input())
            for i in range(inp):
                pyautogui.press("volumeup")

        elif 'volume down' in query:
            speak("how much")
            print("Enter the volume:")
            inm = int(input())
            for i in range(inm):
                pyautogui.press('volumedown')

        elif 'volume mute' in query or 'mute' in query:
            pyautogui.press('volumemute')   


          


 






        






        
           


        
            
            
            

                

        
        

    



              




