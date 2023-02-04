#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.

import tkinter as tk
import openai
import gtts
import os
import random
from playsound import playsound
import speech_recognition as sr
import json
root = tk.Tk()
input_text = ""
print('Copyright (C) 2023  Mathys Penson')

api_key = open('api.key', 'r').read()
openai.api_key = api_key
# get the width and height of the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# calculate the position of the window
width = int(screen_width * 0.4)
height = int(screen_height * 0.1)
x = int((screen_width / 2) - (width / 2))
y = int((screen_height / 3) - (height / 2))


def getAnswer():
    text = Speech2Text()
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=text + ' In het Vlaams',
        temperature=.4,
        max_tokens=1024
    )
    
    response = response['choices'][0]['text']
    print(response)
    Text2Speech(response)
    Text2Speech('Ik sluit af')
    root.destroy()
    exit(0)

def on_ESC_press(event):
    if event.keysym == 'Escape':
        Text2Speech('Ik sluit af')
        root.destroy()
        exit(0)
def Text2Speech(text):
    Startrandomcipher = random.randint(0, 10000)
    StartLocation = f"{os.getenv('TEMP')}/{Startrandomcipher}.mp3"
    print(Startrandomcipher)

    tts = gtts.gTTS(text, lang='nl')
    tts.save(StartLocation)
    playsound(StartLocation)
    os.remove(StartLocation)
    
def Speech2Text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio_text = r.listen(source)
    try:
       return(r.recognize_google(audio_text, language="nl-BE"))
    except:
        Text2Speech("Ik heb het niet verstaan. Herhaal Alstubielft")
        return Speech2Text()
    



root.bind('<Key>', on_ESC_press)
Text2Speech("Ik Luister.")
getAnswer()
root.mainloop()

