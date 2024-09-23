import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyjokes
import wikipedia
import webbrowser
import ctypes
import subprocess
import sys
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(audio):
	engine.say(audio)
	engine.runAndWait()

	

listener = sr.Recognizer()
machine = pyttsx3.init()
instruction = ""  # Initialize instruction globally

def talk(text):
    machine.say(text)
    machine.runAndWait()

def input_instruction():
    global instruction  # Declare instruction as global
    try:
        with sr.Microphone() as origin:
            print("Listening")
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            if "voice assistant" in instruction:
                instruction = instruction.replace('voice assistant', '')
                print(instruction.encode('utf-8').decode(sys.stdout.encoding))  # Encoding the instruction for printing
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    
    print("Instruction:", instruction.encode('utf-8').decode(sys.stdout.encoding))  # Encoding the instruction for printing
    return instruction

def play_assistant():
    instruction = input_instruction()
    print("Instruction:", instruction.encode('utf-8').decode(sys.stdout.encoding))  # Encoding the instruction for printing
    if "play" in instruction:
        song = instruction.replace('play', '')
        talk("playing "+ song)
        pywhatkit.playonyt(song)
    elif 'time' in instruction:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is '+ time)
    elif 'date' in instruction:
        date = datetime.datetime.now().strftime('%d /%m /%Y')
        talk("Today's date is "+ date)
    elif 'how are you' in instruction:
        talk('I am fine, how about you?')
    elif 'what is your name' in instruction:
        talk('I am your voice Assistant, what can I do for you?')
    elif 'who is' in instruction:
        human = instruction.replace('who is', '')
        info = wikipedia.summary(human, 1)
        print(info.encode('utf-8').decode(sys.stdout.encoding))  # Encoding the info for printing
        talk(info)
    elif 'joke' in instruction:
        speak(pyjokes.get_joke())
    elif 'open google' in instruction:
        speak("Here you go to Google\n")
        webbrowser.open("google.com")
    elif 'open youtube' in instruction:
        speak("Here you go to Youtube\n")
        webbrowser.open("youtube.com")
    elif 'change background' in instruction:
        ctypes.windll.user32.SystemParametersInfoW(20, 
													0, 
													"E:\wallpaperflare.com_wallpaper (8).jpg",
													0)
        speak("Background changed successfully")
    elif 'lock window' in instruction:
        speak("locking the device")
        ctypes.windll.user32.LockWorkStation()
    elif 'shutdown system' in instruction:
        speak("Hold On a Sec ! Your system is on its way to shut down")
        subprocess.call('shutdown / p /f')
   
    else:
        talk('Please repeat, I did not understand')

play_assistant()