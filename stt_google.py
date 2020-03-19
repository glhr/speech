import speech_recognition as sr

# Global parameters
clear_flag = 1

def speech_to_text():
    # Set American English
    global clear_flag
    r = sr.Recognizer()
    with sr.Microphone(sample_rate=48000,chunk_size=2048) as source:
        # Adjusts the energy threshold dynamically using audio from source (an AudioSource instance) to account for ambient noise.
        print("Please wait one second for calibrating microphone...")
        r.adjust_for_ambient_noise(source,duration=1)
        print("Ok, I am ready...")
        r.dynamic_energy_threshold = True
        audio = r.listen(source)
        human_said = ""
        #human_said = r.recognize_google(audio, language="en-US")
        #print("Speech was:" + human_said)
        try:
            human_said = r.recognize_google(audio, language="en-US")
            print(human_said)
            clear_flag = 1
        except Exception as e:
            print(e)
            clear_flag = 0

    return human_said.lower()

if __name__ == "__main__":
    text = speech_to_text()
    print(text)
