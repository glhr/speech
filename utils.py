import speech_recognition as sr
import scipy.io.wavfile as wav
from asr_evaluation import asr_evaluation as eval
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


def reset_eval_variables():
    # Some defaults
    eval.print_instances_p = False
    eval.print_errors_p = False
    eval.files_head_ids = False
    eval.files_tail_ids = False
    eval.confusions = False
    eval.min_count = 0
    eval.wer_vs_length_p = True

    # For keeping track of the total number of tokens, errors, and matches
    eval.ref_token_count = 0
    eval.error_count = 0
    eval.match_count = 0
    eval.counter = 0
    eval.sent_error_count = 0


def evaluate_results(expected_list, output_list):
    counter = 0
    # Loop through each line of the reference and hypothesis
    for ref_line, hyp_line in zip(expected_list, output_list):
        processed_p = eval.process_line_pair(ref_line, hyp_line, case_insensitive = True)
        if processed_p:
            counter += 1
    # if eval.confusions:
    #     eval.print_confusions()
    # if eval.wer_vs_length_p:
        # eval.print_wer_vs_length()
    # Compute WER and WRR
    if eval.ref_token_count > 0:
        wrr = eval.match_count / eval.ref_token_count
        wer = eval.error_count / eval.ref_token_count
    else:
        wrr = 0.0
        wer = 0.0
    # Compute SER
    if counter > 0:
        ser = eval.sent_error_count / counter
    else:
        ser = 0.0
    logger.debug('Sentence count: {}'.format(counter))
    logger.debug('WRR: {:10.3%} ({:10d} / {:10d})'.format(1-wer, eval.error_count, eval.ref_token_count))
    logger.debug('WCR: {:10.3%} ({:10d} / {:10d})'.format(wrr, eval.match_count, eval.ref_token_count))
    logger.debug('SER: {:10.3%} ({:10d} / {:10d})'.format(ser, eval.sent_error_count, counter))

    return {
            'wrr': 1-wer,
            'wcr': wrr,
            'ser': ser
            }
