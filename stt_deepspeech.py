from deepspeech import Model
try:
    import utils
except ImportError:
    import speech.utils as utils

dirpath = utils.get_current_directory()


def load_deepspeech_model():
    N_FEATURES = 25
    N_CONTEXT = 9
    BEAM_WIDTH = 500
    LM_ALPHA = 0.75
    LM_BETA = 1.85

    ds = Model(dirpath + '/deepspeech-0.6.1-models/output_graph.pbmm', BEAM_WIDTH)
    return ds


ds = load_deepspeech_model()


def stt_deepspeech(filename):
    wav = utils.load_audio_from_wav(filename)
    if len(wav.shape) > 1:  # if audio is stereo, just pick one channel
        wav = wav[:,0]
    return ds.stt(wav)


if __name__ == "__main__":
    try:
        text = stt_deepspeech("output.wav")
    except FileNotFoundError:
        utils.record_audio()
        text = stt_deepspeech("output.wav")
    print(text)
