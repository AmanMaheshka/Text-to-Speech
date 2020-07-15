#!pip install pyttsx3
#!pip install pypiwin32
import pyttsx3

# Initialize the converter
converter = pyttsx3.init()

# Set properties before adding
# Things to say

# Sets speed percent
# Can be more than 100
converter.setProperty('rate', 150)
# Set volume 0-1
converter.setProperty('volume', 1.0)

# Queue the entered text
# There will be a pause between
# each one like a pause in
# a sentence
t=input("Enter a text:")
converter.say(t)
# Empties the say() queue
# Program will not continue
# until all speech is done talking
converter.runAndWait()
