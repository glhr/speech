import pyaudio
import deepspeech
from deepspeech import Model
import scipy.io.wavfile as wav
import speech_recognition as sr

from pathlib import Path
dirpath = str(Path(__file__).parent.absolute())

def load_deepspeech_model():
    N_FEATURES = 25
    N_CONTEXT = 9
    BEAM_WIDTH = 500
    LM_ALPHA = 0.75
    LM_BETA = 1.85

    ds = Model(dirpath + '/deepspeech-0.6.1-models/output_graph.pbmm', BEAM_WIDTH)
    return ds

ds = load_deepspeech_model()

def deepspeech(audio):
    return ds.stt(audio)

def generate_text(audio, method='deepspeech'):
    return deepspeech(audio)

if __name__ == "__main__":
    r = sr.Recognizer()
    with sr.Microphone(sample_rate=48000,chunk_size=2048) as source:
        # Adjusts the energy threshold dynamically using audio from source (an AudioSource instance) to account for ambient noise.
        print("Please wait one second for calibrating microphone...")
        r.adjust_for_ambient_noise(source,duration=1)
        print("Ok, I am ready...")
        r.dynamic_energy_threshold = True
        audio = r.listen(source)
        text = generate_text(audio, method='deepspeech')
        print(text)
