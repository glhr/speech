import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # disable ugly tensorflow logs
from stt_wrapper import generate_text
import json
import coloredlogs, logging

# set up logging
logger = logging.getLogger(__name__)
coloredlogs.install(
    level='DEBUG',
    logger=logger,
    fmt='[%(levelname)s] %(message)s',
    level_styles=coloredlogs.parse_encoded_styles('spam=22;debug=28;verbose=34;notice=220;warning=202;success=118,bold;error=124;critical=background=red'))

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
