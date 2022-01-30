from gtts import gTTS
import os
import playsound
import speech_recognition as sr
import hack3
import multiprocessing

#import urllib2

def findfiles(file_str):
        file_str = file_str.lower()
        # found_files = []
        files = os.listdir('.')
        song_title = ''

        for index in range(len(files)):
            #print(files[index] + '\n')
            #files[index] = files[index].lower()
            if(file_str in files[index]):
                song_title = files[index]
                break
        if (song_title != ''):
            playsound.playsound(song_title)
            # Wait some time then exit
        else:
            return "No audiobooks in the local directory matched your request.\n"


def speak(text):
    tts = gTTS(text=text, lang='en')
    
    try:
        os.remove('zzz.mp3')
    except:
        print("")
    filename = "zzz.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    
    os.remove(filename)
    
def my_listen():
        r = sr.Recognizer()                                                                                   
        with sr.Microphone() as source:                                                                       
            print("Speak:")                                                                                   
            audio = r.listen(source, None, 3) 
            
        
        try:
            #print("You said " + r.recognize_google(audio))
            return r.recognize_google(audio)
        except sr.UnknownValueError:
           print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

def fileToString(fileName):
    with open(fileName, 'r', encoding="utf8") as f:
        read_data = f.read()
    f.close()
    return read_data


#speak("Which audio book would you like to listen to in your directory?")
"""
if choice == "local directory":
    speak("Which audio book would you like to listen to in your directory?")
    
    chosenBook = my_listen()
    print(chosenBook)
    findfiles(chosenBook)
    
    

elif choice == "internet":

    speak("Which audio book would you like to listen to?")
    
    chosenBook = my_listen()
    
    file = hack3.getTextFile(chosenBook)
    text = fileToString("facebook.txt")
    text_split = text.split("\n\n")
    #text_split = text.split(" ")
    #print(text_split[1])
    
    for segment in text_split:
        speak(segment)
        #print(segment)
      """  
    
        
