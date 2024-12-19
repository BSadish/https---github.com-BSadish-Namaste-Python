import pyttsx3
user=pyttsx3.init()
speech=input("Enter the text:")
user.say(speech)
user.runAndWait()
