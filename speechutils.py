import speech_recognition as sr
import scipy.io.wavfile as wav
from pathlib import Path
import coloredlogs,logging
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # disable ugly tensorflow logs

# set up logging
logger = logging.getLogger(__name__)
coloredlogs.install(
    level='DEBUG',
    logger=logger,
    fmt='[%(levelname)s] %(message)s',
    level_styles=coloredlogs.parse_encoded_styles('spam=22;debug=28;verbose=34;info=226;notice=220;warning=202;success=118,bold;error=124;critical=background=red'))

r = sr.Recognizer()


def get_logger():
    return logger


def get_current_directory():
    return str(Path(__file__).parent.absolute())


def get_path_from_filename(filename):
    return get_current_directory() + '/audio/' + filename


def record_audio(filename="output.wav"):
    with sr.Microphone(sample_rate=48000, chunk_size=2048) as source:
        # Adjusts the energy threshold dynamically using audio from source (an AudioSource instance) to account for ambient noise.
        logger.info("Please wait one second for calibrating microphone...")
        r.adjust_for_ambient_noise(source, duration=1)
        logger.info("Ok, I am ready...")
        r.dynamic_energy_threshold = True
        audio = r.listen(source)
        with open(get_path_from_filename(filename), "wb") as file:
            file.write(audio.get_wav_data())
        return r, audio


def load_audio_as_source(filename):
    # use the audio file as the audio source
    with sr.AudioFile(get_path_from_filename(filename)) as source:
        audio = r.record(source)  # read the entire audio file
        return r, audio


def load_audio_from_wav(filename):
    _, audio = wav.read(get_path_from_filename(filename))
    return audio
