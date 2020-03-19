from stt_wrapper import generate_text

filename = "output.wav"
for method in ['google', 'deepspeech']:
    text = generate_text(filename, method=method)
    print("--> {}: {}".format(method, text))
