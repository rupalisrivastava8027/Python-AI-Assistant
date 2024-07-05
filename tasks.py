import pyautogui as master
import time
import speech_recognition as voice
from speech_recognition.audio import AudioData, get_flac_converter
import pyttsx3
import openai as j
import pyaudio

class Tasks:
   
    messages = []
    
    system = {"role": "system", "content": "You are a assistant"}
    
    messages.append(system)

    def chat(client, prompt):
        user = {"role": "user", "content": prompt}
        Tasks.messages.append(user)
        response = client.chat.completions.create(model = "gpt-3.5-turbo", messages = Tasks.messages)  
        #translated_text = response['choices'][0]['text'].strip()
        
        answer = response.choices[0].message
        for answ in answer:

            ans = answ.__getitem__(1)
            system = {"role": "system", "content": ans}
            Tasks.messages.append(system)
            
            return ans


    class voice:

        def recognize():
            
            recognize = voice.Recognizer()
            
            with voice.Microphone() as source:
                print("Say Something: ")
                recognize.adjust_for_ambient_noise(source)
                listen = recognize.listen(source)
               
            
            print("Recognizing...")
            try:
                said = recognize.recognize_google(listen)
            except voice.exceptions.UnknownValueError:
                said = ""
            
            #if "hey jarvis" in said or "jarvis" in said:
             #   return said
            
            return said

            #return said
        
        def speak(text):
            engine = pyttsx3.init()
                
            engine.say(text)
            engine.runAndWait()


    class Navigation:
        
        global x, y
        x, y = 565, 1046

        def goTo(user):

          master.moveTo(x, y)
          master.click()
          time.sleep(1)
          master.typewrite(user)
          time.sleep(1)
          master.keyDown('enter')
         
        
        
        def call(person):
            Tasks.Navigation.goTo("Whatsapp")
            time.sleep(2)
            master.typewrite(person)
            time.sleep(1)
            #master.moveRel(, -40)
            #master.click()
            master.hotkey("tab")
            master.hotkey('enter')
            #master.typewrite("b")
            
            for i in range(11):
                master.hotkey("tab")
            
            master.hotkey("enter")
            # img = master.locateOnScreen("call.png")

            # if img != None:
                
            #     centerx, centery = master.center(img)
            #     master.click(centerx, centery)
            # else:
            #     print("Image not found")
            
            
          #return "Could not open browser"

class help:
    
    def check(word, sentence):

        for i in range(len(sentence)):
            if sentence[i] == word:
                return True
        return False
    
    def findNextWord(sentence, word):
        
        # for letter in 
        #     if letter == " ":

        # isWord = True
        # for letter in sentence:
        #     for char in word:

        #         if not letter == char:
        
        sentence = sentence.split()
        #print(sentence)
        for char in range(len(sentence)):
            if sentence[char] == word:
                return sentence[char + 1]
        return -1
                


        
        

            
            
        

#master.openNewTab() #TODO: Fix this

        
#task = tasks()
