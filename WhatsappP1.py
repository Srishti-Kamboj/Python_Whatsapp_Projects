from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 
import os  

driver = webdriver.Chrome('C:\\Users\\cn\\Documents\\Chromedriver\\Chromedriver.exe')   
driver.get("https://web.whatsapp.com/")

import speech_recognition as s 
#create a object of Recognizer
sr=s.Recognizer() # help in audio recognition mainly it is  a class & Recogniser is a constructor
print("Say Something!") #Microphone is opening
with s.Microphone() as msg:  #Microphone object creation & using with keyword Microphone automatically closes
 audio=sr.listen(msg)
 query=sr.recognize_google(audio,language='eng-in',show_all=True)# Convert audio to text/String messsage using .recognize_google function
 print(query)  # Print audio converted to text/String
jr=input()

tag_list = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]")
taglist.sendkeys(query)

