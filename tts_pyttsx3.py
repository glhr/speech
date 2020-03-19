import pyttsx3

#try:
engine = pyttsx3.init()  # object creation
"""SET RATE"""
engine.setProperty('rate', 140)  # setting up new voice rate
"""SET VOLUME"""
engine.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1
"""SET VOICE"""
voices = engine.getProperty('voices')  # getting details of current voice
engine.setProperty('voice', voices[0].id)  # changing index, changes voices. 0 for male
"""SPEAK"""
#except: pass

def text_to_speech(text):
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def generate_speech(text,out):
    engine.save_to_file(text,out)
    engine.runAndWait()
    engine.stop()

if __name__ == "__main__":
    text_to_speech("Hello Lars this sounds amazing I am offended")
    generate_speech("test","test1.wav")
