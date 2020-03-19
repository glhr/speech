import speech_recognition as sr
import scipy.io.wavfile as wav

r = sr.Recognizer()


def record_audio(filename="output.wav"):
    with sr.Microphone(sample_rate=48000, chunk_size=2048) as source:
        # Adjusts the energy threshold dynamically using audio from source (an AudioSource instance) to account for ambient noise.
        print("Please wait one second for calibrating microphone...")
        r.adjust_for_ambient_noise(source, duration=1)
        print("Ok, I am ready...")
        r.dynamic_energy_threshold = True
        audio = r.listen(source)
        with open(filename, "wb") as file:
            file.write(audio.get_wav_data())
        return r, audio


def load_audio_as_source(filename):
    # use the audio file as the audio source
    with sr.AudioFile(filename) as source:
        audio = r.record(source)  # read the entire audio file
        return r, audio


def load_audio_from_wav(filename):
    _, audio = wav.read(filename)
    return audio
