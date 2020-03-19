# import speech_recognition as sr
import utils

# Global parameters
clear_flag = 1


def stt_google(filename):
    # Set American English
    global clear_flag
    try:
        r, audio = utils.load_audio_as_source(filename)
    except Exception as e:
        print(e)
        r, audio = utils.record_audio()
    human_said = ""
    try:
        human_said = r.recognize_google(audio, language="en-US")
        clear_flag = 1
        return human_said.lower()
    except Exception as e:
        print(e)
        clear_flag = 0
        return None


if __name__ == "__main__":
    text = stt_google(filename="output.wav")
    print(text)
