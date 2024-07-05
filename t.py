import pyttsx3 as voice

engine = voice.init()

voices = engine.getProperty("voices")

for voice in voices:
    print(voice)


