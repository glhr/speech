try:
    import speechutils as utils
except ImportError:
    import speech.speechutils as utils

logger = utils.get_logger()


def stt_wit(filename):
    ACCESS_TOKEN = "6KZOTYV2QOYHSZZQ34NL7YI67OO7MO37"
    r, audio = utils.load_audio_as_source(filename)
    try:
        human_said = r.recognize_wit(audio, key=ACCESS_TOKEN)
        return human_said.lower()
    except Exception as e:
        logger.error(e)
        return None


def stt_houndify(filename):
    ID = "GiNhNfW-OgOlHG3PaDzI9Q=="
    KEY = "Eo4j32ukHBVTkTXfGcKfGzuKyQQiIKaYWsS3yYcOYrEETg-xvI1tkNZg9lSW832ncQux3NPKfiN60mCB4FQx4g=="
    r, audio = utils.load_audio_as_source(filename)
    try:
        human_said = r.recognize_houndify(audio, client_id=ID, client_key=KEY)
        return human_said.lower()
    except Exception as e:
        logger.error(e)
        return None


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
