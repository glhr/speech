try:
    import utils
except ImportError:
    import speech.utils as utils

logger = utils.get_logger()


def stt_google(filename):
    r, audio = utils.load_audio_as_source(filename)
    try:
        human_said = r.recognize_google(audio, language="en-US")  # Set American English
        return human_said.lower()
    except Exception as e:
        logger.error(e)
        return None


def stt_sphinx(filename):
    r, audio = utils.load_audio_as_source(filename)
    try:
        human_said = r.recognize_sphinx(audio, language="en-US")  # Set American English
        return human_said.lower()
    except Exception as e:
        logger.error(e)
        return None


if __name__ == "__main__":
    try:
        text = stt_google(filename="output.wav")
    except FileNotFoundError:
        utils.record_audio()
        text = stt_google(filename="output.wav")
    logger.info(text)
