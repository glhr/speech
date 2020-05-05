import os
import sys
import io
import torch
import numpy as np
from collections import OrderedDict

from TTS.models.tacotron import Tacotron
from TTS.layers import *
from TTS.utils.data import *
from TTS.utils.audio import AudioProcessor
from TTS.utils.generic_utils import load_config
from TTS.utils.text import text_to_sequence
from TTS.utils.synthesis import synthesis
from utils.text.symbols import symbols, phonemes
from TTS.utils.visual import visualize

from pathlib import Path
dirpath = str(Path(__file__).parent.absolute())

def load_tts_model():

    MODEL_PATH = dirpath + '/tts_model/best_model.pth.tar'
    CONFIG_PATH = dirpath + '/tts_model/config.json'
    CONFIG = load_config(CONFIG_PATH)
    use_cuda = False

    num_chars = len(phonemes) if CONFIG.use_phonemes else len(symbols)
    model = Tacotron(num_chars, CONFIG.embedding_size, CONFIG.audio['num_freq'], CONFIG.audio['num_mels'], CONFIG.r, attn_windowing=False)

    num_chars = len(phonemes) if CONFIG.use_phonemes else len(symbols)
    model = Tacotron(num_chars, CONFIG.embedding_size, CONFIG.audio['num_freq'], CONFIG.audio['num_mels'], CONFIG.r, attn_windowing=False)

    # load the audio processor
    # CONFIG.audio["power"] = 1.3
    CONFIG.audio["preemphasis"] = 0.97
    ap = AudioProcessor(**CONFIG.audio)

    # load model state
    if use_cuda:
        cp = torch.load(MODEL_PATH)
    else:
        cp = torch.load(MODEL_PATH, map_location=lambda storage, loc: storage)

    # load the model
    model.load_state_dict(cp['model'])
    if use_cuda:
        model.cuda()

    #model.eval()
    model.decoder.max_decoder_steps = 1000
    return model, ap, MODEL_PATH, CONFIG, use_cuda

model, ap, MODEL_PATH, CONFIG, use_cuda  = load_tts_model()

def tts(model, text, CONFIG, use_cuda, ap, OUT_FILE):
    import numpy as np
    waveform, alignment, spectrogram, mel_spectrogram, stop_tokens = synthesis(model, text, CONFIG, use_cuda, ap)
    ap.save_wav(waveform, OUT_FILE)
    wav_norm = waveform * (32767 / max(0.01, np.max(np.abs(waveform))))
    return alignment, spectrogram, stop_tokens, wav_norm

def mozilla(sentence, OUT_FILE):
    align, spec, stop_tokens, wav_norm = tts(model, sentence, CONFIG, use_cuda, ap, OUT_FILE)
    return wav_norm

def generate_speech(sentence, OUT_FILE):
    mozilla(sentence,OUT_FILE)

if __name__ == "__main__":
    generate_speech("Hello Lars this sounds amazing I am offended","test1.wav")
