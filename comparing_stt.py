
from stt_wrapper import generate_text
import utils
import json

logger = utils.get_logger()
# list of supported speech recognition methods
methods = ['google','deepspeech']

with open('audio/dataset.json') as f:
    data = json.load(f)['data']
    for recording in data:
        logger.debug("{} ({})".format(recording['phrase'.lower()], recording['file']))
        for method in methods:
            try:
                text = generate_text(recording['file'], method=method)
                logger.info("--> {}: {}".format(method, text))
            except Exception as e:
                logger.error(e)
