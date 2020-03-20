def generate_text(filename, method='google'):
    method = method.lower()
    if method == 'deepspeech':
        try:
            from stt_deepspeech import stt_deepspeech
        except ImportError:
            from speech.stt_deepspeech import stt_deepspeech
        return stt_deepspeech(filename)
    elif method == 'google' or method == 'sphinx':
        try:
            from stt_sr import stt_google, stt_sphinx
        except:
            from speech.stt_sr import stt_google, stt_sphinx
        if method == 'google':
            return stt_google(filename)
        elif method == 'sphinx':
            return stt_sphinx(filename)
    else:
        print("Unknown Speech-to-Text method provided")


if __name__ == "__main__":
    # use default method (google) if no method provided as argument
    import sys
    method = sys.argv[1] if len(sys.argv) > 1 else 'google'
    try:
        text = generate_text(filename="output.wav", method=method)
    # record audio from microphone if output.wav doesn't exist
    except FileNotFoundError:
        import utils
        utils.record_audio(filename="output.wav")
        text = generate_text(filename="output.wav", method=method)
    print(text)
