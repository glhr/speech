def generate_text(filename, method='google'):
    if method == 'deepspeech':
        from stt_deepspeech import stt_deepspeech
        return stt_deepspeech(filename)
    if method == 'google':
        from stt_google import stt_google
        return stt_google(filename)


if __name__ == "__main__":
    text = generate_text(filename="output.wav")
    print(text)
