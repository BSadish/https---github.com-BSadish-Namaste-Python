import pyttsx3

# Initialize the pyttsx3 engine
user = pyttsx3.init()

# Set properties for the voice
voices = user.getProperty('voices')
# Use Hindi voice (adjust the index based on available voices)
user.setProperty('voice', voices[1].id)  # Change index based on your system's available Hindi voice

# Prompt user to enter text
speech = input("Enter the text (in Hindi): ")

# Say the text in Hindi
user.say(speech)

# Wait for speech to complete
user.runAndWait()
