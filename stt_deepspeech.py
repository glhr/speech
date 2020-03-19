import pyaudio
import deepspeech
from deepspeech import Model
# import scipy.io.wavfile as wav
# import speech_recognition as sr
import utils

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


def stt_deepspeech(audio):
    return ds.stt(audio)


if __name__ == "__main__":
    try:
        wav = utils.load_audio_from_wav()
    except Exception:
        utils.record_audio()
        wav = utils.load_audio_from_wav()
    text = stt_deepspeech(wav)
    print(text)
