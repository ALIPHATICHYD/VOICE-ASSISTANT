#!/usr/bin/env python
# coding: utf-8

# In[52]:


# !pip install pyttsx3
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pywhatkit
import os
import yfinance as yf
import pyjokes
import wikipedia


# In[2]:


#listen to our microphone and return the audio as text using google
def transform():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        said = r.listen(source)
        try:
            print('I am listening')
            q = r.recognize_google(said, language="en")
            return q
        except sr.UnknownValueError:
            print("Sorry I did not understand")
            return "I am waiting"
        except sr.RequestError:
            print('Sorry the service is down')
            return "I am waiting"
        except:
            return "I am waiting"


# In[3]:

transform()

# In[4]:


def speaking(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()


# In[17]:


speaking('hello world')
# speaking('Hello world')


# In[9]:


engine = pyttsx3.init()
for voice in engine.getProperty('voices'):
    print(voice)

    
# In[45]:

id ='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
engine.setProperty('voice',id)
engine.say('Hello World')
engine.runAndWait()

