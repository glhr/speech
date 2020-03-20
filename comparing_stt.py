
from stt_wrapper import generate_text
import utils
import json

logger = utils.get_logger()
# list of supported speech recognition methods
methods = ['google', 'sphinx', 'deepspeech']

with open('audio/dataset.json') as f:
    data = json.load(f)['data']
    for recording in data:
        logger.debug("{} ({})".format(recording['phrase'].lower(), recording['file']))
        for method in methods:
            try:
                text = generate_text('resampled/'+recording['file'], method=method)

                # compute ratio of correct words
                expected = recording['phrase'].lower().split()
                output = text.split()
                diff = [word for word in expected if word not in output]

                logger.info("--> {}: {}".format(method, text))
                logger.warn("----> {} incorrect word(s) ".format(len(diff), diff))
            except Exception as e:
                logger.error(e)
