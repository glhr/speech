
from stt_wrapper import generate_text
import utils
import json


logger = utils.get_logger()
# list of supported speech recognition methods
methods = ['google', 'sphinx', 'deepspeech']

results = {}

with open('audio/dataset.json') as f:
    data = json.load(f)['data']
    for recording in data:
        expected = recording['phrase'].lower()

        logger.debug("{} ({})".format(expected, recording['file']))
        for method in methods:
            try:
                output = generate_text('resampled/'+recording['file'], method=method)
                # diff = [word for word in expected if word not in output]
                try:
                    results[method][expected] = output
                except KeyError:
                    results[method] = {expected: output}

                logger.info("--> {}: {}".format(method, output))
                # logger.warn("----> {} incorrect word(s) ".format(len(diff), diff))
            except Exception as e:
                logger.error(e)

# print evaluation results
for method in methods:
    logger.info("Evaluation - {}".format(method))
    utils.evaluate_results(results[method].keys(), results[method].values())
    utils.reset_eval_variables()
