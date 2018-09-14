import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
import subprocess
import wolframalpha
import wikipedia
import webbrowser
import pygame
import vlc
import scrapy

def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")
 
def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
 
    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
 
    return data

def fn_search(word):
    """
    
    If success:
        Searches for the given sentence.
    """
   
    speak('This is what i found')
    #word = word.replace(" ", "+")
    #search_link = "www.google.co.in/#q=" + word
    #speak('Cool. Here are the results.')
    #os.system('guake -n CUR_DIR -e "firefox "' + search_link +'" & >/dev/null"')
    #os.system("guake -s 1")
    #os.system("guake -s 2 -e exit")
    url = "https://www.google.com.tr/search?q={}".format(word)
    webbrowser.open_new_tab(url)
    return
    
    

def jarvis(data):
	word_list = word_tokenize(data)
	print(word_list)
	stop_words = set(stopwords.words('english'))
	if "search" not in word_list and "google" not in word_list:
		filtered_sentence = [w for w in word_list if not w in stop_words]
	else:
		filtered_sentence = [w for w in word_list]

	if "introduce yourself" in data:
		speak("Hello, my name is Friday. I can find answers to your questions!")
	if "how are you" in data:
		speak("I am doing great.Thanks for asking")
	elif "what time is it" in data:
		speak(ctime())
	elif "where" in data:
	        data = data.split(" ")
	        location = data[2]
	        speak("Hold on Sir, I will show you where " + location + " is.")
	        os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")
	elif "Run gesture" in data:
	    	speak("Hold on Sir, I will run  gesture for you")
	    	os.system('python gesture.py')
	elif "Friday hit my music" in data:
			speak("Sure thing sir")
			player = vlc.MediaPlayer("/home/abhimanyu/Desktop/iron.mp3")
			player.play()
			time.sleep(20)
			player.pause()

	elif "thanks" in data:
	    	speak("My pleasure Sir")
	    	speak("I will be here when you need me")
	    	#speak("Its pleasure talking to you sir")
	elif "show your skills Friday" in data:
			speak("Alright Sir! Here I can find all your queries from Wikipedia and Wolframalpha !")
			x=3
			while (x):
			    my_input = input("Question: ")

			    try:
			    	app_id = "QWQQPU-RQLYYE898A"
			    	client = wolframalpha.Client(app_id)
			    	res = client.query(my_input)
			    	answer = next(res.results).text
			    	speak(answer)

			    except:
			    	#wikipedia
			    	#wikipedia.set_lang("es")   # for other languages
			    	print(wikipedia.summary(my_input,sentences=2)) # or speak(wikipedia.summary(my_input,sentences=2))
			    x = x-1
	elif 'close' in filtered_sentence:
		os.system('wmctrl -a firefox; xdotool key Ctrl+w;')
		speak("There you go sir")
	elif 'search' in filtered_sentence:
		if filtered_sentence[-1] == "search":
			speak("Enter the word you would like me to search.")
			search_string = input('Query :')
			fn_search(search_string)
	elif "shutdown" in data:
		 speak("Shutting down system now. Goodbye!")
		 os.system("sudo shutdown -h now")
	elif "open camera" in data:
		speak("Webcam is now opening. Please stand in front of it. Timer for 5 seconds will start!")
		speak("And dont forget to smile!")
		os.system('python image_capture.py')
			
# initialization
time.sleep(3)
speak("Greetings Sir")
speak("How can I help you?")
while 1:
    data = recordAudio()
    #print(data)
    jarvis(data)


#https://developer.wolframalpha.com/portal/signin.html