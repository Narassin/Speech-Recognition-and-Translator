import speech_recognition as sr
from translate import Translator
import codecs
import os

#Initial path
path = os.getcwd()
print("Current Directory", path)

# Initial Setup
source_language = 'ms'
target_language = 'en'

# Program starts below

# Initialization
recognizer = sr.Recognizer()
audi = sr.AudioFile("test.wav")

counter = 0

# Reset the text on every iteration
recognized_text = ''

# Record audio
with audi as source:
    print("Start Audio Recognizing")
    recognizer.adjust_for_ambient_noise(source)
    audio= recognizer.record(source)

# Recognize speech
try:
    recognized_text = recognizer.recognize_google(audio, language='ms-MY')
except:
    print("Speech recognition failed")
    pass

print(recognized_text)
counter = counter + 1

# Translate text
translated_text = ''
try:
    translator = Translator(to_lang=target_language, from_lang=source_language)
    translated_text = translator.translate(recognized_text)
except Exception as e:
    print("Translation failed due to the following error:", str(e))
    pass

print(translated_text)

if recognized_text:
    # Write to text file
    output_file = codecs.open('output.txt', 'w', 'utf-8')

    print(recognized_text, file=output_file)
    print(translated_text, file=output_file)

    # Close file
    output_file.close()