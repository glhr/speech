def generate_text(filename, method='google'):
    if method == 'deepspeech':
        from stt_deepspeech import stt_deepspeech
        return stt_deepspeech(filename)
    elif method == 'google':
        from stt_google import stt_google
        return stt_google(filename)
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
