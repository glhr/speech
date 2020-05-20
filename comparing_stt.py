from stt_wrapper import generate_text
import speechutils as utils
import json
import pandas as pd
import numpy as np
from timeit import default_timer as timer

logger = utils.get_logger()
# list of supported speech recognition methods
methods = ['deepspeech', 'google', 'wit', 'sphinx', 'houndify']
# methods = ['google']

results = {}
timings = {}

count = 0   # number of sentences processed
N_MAX = 20  # maximum number of sentences to process

metrics_full = []
metrics_summary = []

with open('audio/dataset.json') as f:
    data = json.load(f)['data']
    for recording in data:
        count += 1
        if count > N_MAX:
            break

        expected = recording['phrase'].lower()
        print("{} ({})".format(expected, recording['file']))

        for method in methods:
            try:
                inference_start = timer()
                output = generate_text('resampled/'+recording['file'], method=method)
                inference_end = timer() - inference_start
                # diff = [word for word in expected if word not in output]

                try:
                    results[method][expected] = output
                    timings[method][expected] = inference_end
                except KeyError:
                    results[method] = {expected: output}
                    timings[method] = {expected: inference_end}
                metrics = utils.evaluate_results(expected, output)
                utils.reset_eval_variables()

                metrics['method'] = method
                metrics['time'] = inference_end
                metrics_full.append(metrics)

                print("--> {}: {} ({:.3f} s)".format(method, output, inference_end))
                # logger.warn("----> {} incorrect word(s) ".format(len(diff), diff))
            except Exception as e:
                print(e)

# store evaluation results

df = pd.DataFrame(metrics_full)
# df = df.set_index('method')
print(df)
df.to_csv('audio/results_full.csv', encoding='utf-8', index=True)


N_PHRASES = len(results[method].keys())
for method in methods:
    print("Evaluation - {}".format(method))
    metrics = utils.evaluate_results(results[method].keys(), results[method].values())
    utils.reset_eval_variables()
    metrics['method'] = method
    metrics['time'] = np.sum(list(timings[method].values())) / N_PHRASES
    metrics_summary.append(metrics)

df = pd.DataFrame(metrics_summary)
df = df.set_index('method')
print(df)
df.to_csv('audio/results_summary.csv', encoding='utf-8', index=True)
