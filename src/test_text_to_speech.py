import pyttsx3

engine = pyttsx3.init()
rate = engine.getProperty('rate')
print(rate)
for voice in engine.getProperty('voices'):
    print(voice)

