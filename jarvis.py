# Import Statements
from tasks import *     

# Key                   
key = "sk-proj-u0FdLjoCTkfry8zS5pg6T3BlbkFJsHFZdQqYBC9cfzK0okkn"
client = j.OpenAI(api_key = key)

voice = Tasks.voice
voice.speak("Hello Aarush, What can I do for you?")

while True:
    me = voice.recognize().lower()
    #me = me.lower()
    #print("You said " + me)
    
    #me = input("Say: ").lower() 

    if "hey jarvis" in me or "jarvis" in me:
        
        #me = voice.recognize()
        #me = me.lower()
        print("You said " + me)

        voice.speak("Searching")

        if me == "bye":
            break

        # if "hello" in me or "hi" in me:
        #     #print("hello, aarush")
        #     voice.speak("Hello Aarush")

        if "open chrome" in me or "go to chrome" in me:
            voice.speak("ok")   
            openBrowser = Tasks.Navigation.goTo("chrome")

        elif "open" in me:
            
            Tasks.Navigation.goTo(help.findNextWord(me, "open"))
        elif "call" in me:

            Tasks.Navigation.call(help.findNextWord(me, "call"))
        else:
            
            
            answer = Tasks.chat(client, me)
            print(answer)
            voice.speak(answer) 

    