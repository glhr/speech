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
    import sys
    method = sys.argv[1] if len(sys.argv)>1 else 'google'
    text = generate_text(filename="output.wav", method=method)
    print(text)
