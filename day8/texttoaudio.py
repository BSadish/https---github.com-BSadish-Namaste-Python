from gtts import gTTS
import os
from playsound import playsound

user = input("Enter the text you want to spell out: ")

speak = ' '.join(list(user))
tts = gTTS(speak)


audio= "speak.mp3"
tts.save(audio)


playsound(audio)


os.remove(audio)
